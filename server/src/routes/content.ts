import { Router } from "express";
import { z } from "zod";
import { prisma } from "../prisma";
import { requireAuth, AuthedRequest } from "../auth";
import { buildCurriculumForUser, sanitizeExercise } from "../curriculum";
import {
  recomputeHearts,
  loseHeart,
  registerDailyActivity,
  awardXP,
  gradeExercise,
  starsForScore,
} from "../gamification";
import { ExerciseType } from "../types";

const router = Router();

router.get("/curriculum", requireAuth, async (req: AuthedRequest, res) => {
  const profile = await prisma.studentProfile.findUnique({ where: { userId: req.auth!.userId } });
  if (!profile) return res.status(400).json({ error: "Perfil de alumno no encontrado" });
  const tree = await buildCurriculumForUser(req.auth!.userId, profile.id);
  res.json(tree);
});

router.get("/lessons/:id", requireAuth, async (req: AuthedRequest, res) => {
  const lesson = await prisma.lesson.findUnique({
    where: { id: req.params.id },
    include: { exercises: { orderBy: { index: "asc" } }, repertoireEntry: { include: { piece: true } } },
  });
  if (!lesson) return res.status(404).json({ error: "Leccion no encontrada" });

  let weekNumber = lesson.weekIndex;
  if (req.auth!.role === "STUDENT") {
    const profile = await prisma.studentProfile.findUnique({ where: { userId: req.auth!.userId } });
    if (!profile) return res.status(400).json({ error: "Perfil de alumno no encontrado" });
    const tree = await buildCurriculumForUser(req.auth!.userId, profile.id);
    const flatLesson = tree.pieces.flatMap((p) => p.lessons).find((l) => l.id === lesson.id);
    if (!flatLesson || flatLesson.status === "LOCKED") {
      return res.status(403).json({ error: "Esta leccion todavia esta bloqueada" });
    }
    if (flatLesson.status === "SCHEDULED") {
      const dateStr = new Date(flatLesson.scheduledDate).toLocaleDateString("es-ES");
      return res.status(403).json({ error: `Esta semana todavia no ha llegado. Estara disponible el ${dateStr}.` });
    }
    weekNumber = flatLesson.weekNumber;
  }

  res.json({
    id: lesson.id,
    title: lesson.title,
    description: lesson.description,
    xpReward: lesson.xpReward,
    weekIndex: lesson.weekIndex,
    weekNumber,
    pieceTitle: lesson.repertoireEntry.piece.title,
    exercises: lesson.exercises.map(sanitizeExercise),
  });
});

const attemptSchema = z.object({ answer: z.unknown() });

router.post("/exercises/:id/attempt", requireAuth, async (req: AuthedRequest, res) => {
  const parsed = attemptSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Falta la respuesta" });

  const exercise = await prisma.exercise.findUnique({ where: { id: req.params.id } });
  if (!exercise) return res.status(404).json({ error: "Ejercicio no encontrado" });

  const data = JSON.parse(exercise.data);
  const correct = gradeExercise(exercise.type as ExerciseType, data, parsed.data.answer);

  await prisma.exerciseAttempt.create({
    data: { userId: req.auth!.userId, exerciseId: exercise.id, correct },
  });

  let heartsCurrent: number | undefined;
  if (!correct) {
    const profile = await prisma.studentProfile.findUnique({ where: { userId: req.auth!.userId } });
    if (profile) {
      const updated = await loseHeart(profile);
      heartsCurrent = updated.heartsCurrent;
    }
  }

  res.json({
    correct,
    explanation: exercise.explanation,
    correctAnswer: correct
      ? undefined
      : data.correctAnswer ??
        data.answer ??
        data.notes ??
        data.pattern ??
        data.correctOrder ??
        data.expectedAnswer ??
        data.targetNote ??
        (data.segments ? (data.segments as string[][]).flat() : undefined),
    heartsCurrent,
  });
});

const completeSchema = z.object({
  correctCount: z.number().int().min(0),
  totalCount: z.number().int().min(1),
});

router.post("/lessons/:id/complete", requireAuth, async (req: AuthedRequest, res) => {
  const parsed = completeSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos" });
  const { correctCount, totalCount } = parsed.data;

  const lesson = await prisma.lesson.findUnique({ where: { id: req.params.id }, include: { repertoireEntry: true } });
  if (!lesson) return res.status(404).json({ error: "Leccion no encontrada" });

  const pct = correctCount / totalCount;
  const stars = starsForScore(pct);
  const userId = req.auth!.userId;

  const existing = await prisma.progress.findUnique({ where: { userId_lessonId: { userId, lessonId: lesson.id } } });
  const passed = stars >= 1;

  const progress = await prisma.progress.upsert({
    where: { userId_lessonId: { userId, lessonId: lesson.id } },
    create: {
      userId,
      lessonId: lesson.id,
      status: passed ? "COMPLETED" : "AVAILABLE",
      stars,
      bestScore: Math.round(pct * 100),
      attempts: 1,
      completedAt: passed ? new Date() : null,
    },
    update: {
      status: passed ? "COMPLETED" : "AVAILABLE",
      stars: Math.max(stars, existing?.stars ?? 0),
      bestScore: Math.max(Math.round(pct * 100), existing?.bestScore ?? 0),
      attempts: { increment: 1 },
      completedAt: passed ? new Date() : existing?.completedAt ?? null,
    },
  });

  let xpAwarded = 0;
  let newBadges: { code: string; name: string; icon: string }[] = [];
  let profile = await prisma.studentProfile.findUnique({ where: { userId } });

  if (passed && profile) {
    const wasAlreadyCompleted = existing?.status === "COMPLETED";
    if (!wasAlreadyCompleted) {
      xpAwarded = Math.round(lesson.xpReward * (0.5 + 0.5 * (stars / 3)));
      profile = await awardXP(userId, xpAwarded, `Leccion completada: ${lesson.title}`);
      profile = await registerDailyActivity(profile);
      newBadges = await checkAndAwardBadges(userId, profile);

      const allLessonsInPiece = await prisma.lesson.findMany({ where: { repertoireEntryId: lesson.repertoireEntryId } });
      const completedInPiece = await prisma.progress.count({
        where: { userId, status: "COMPLETED", lessonId: { in: allLessonsInPiece.map((l) => l.id) } },
      });
      if (completedInPiece >= allLessonsInPiece.length) {
        await prisma.repertoireEntry.update({ where: { id: lesson.repertoireEntryId }, data: { status: "COMPLETED" } });
      } else {
        await prisma.repertoireEntry.updateMany({
          where: { id: lesson.repertoireEntryId, status: "UPCOMING" },
          data: { status: "ACTIVE" },
        });
      }
    }
  }
  profile = profile ? await recomputeHearts(profile) : profile;
  const score = Math.round(pct * 1000);

  res.json({ progress, stars, score, xpAwarded, profile, newBadges });
});

async function checkAndAwardBadges(userId: string, profile: { xpTotal: number; streakCurrent: number }) {
  const completedCount = await prisma.progress.count({ where: { userId, status: "COMPLETED" } });
  const candidates: string[] = [];
  if (completedCount === 1) candidates.push("primera_leccion");
  if (profile.streakCurrent === 7) candidates.push("racha_7");
  if (profile.streakCurrent === 30) candidates.push("racha_30");
  if (profile.xpTotal >= 100) candidates.push("xp_100");
  if (profile.xpTotal >= 500) candidates.push("xp_500");
  if (candidates.length === 0) return [];

  const badges = await prisma.badge.findMany({ where: { code: { in: candidates } } });
  const owned = await prisma.userBadge.findMany({ where: { userId, badgeId: { in: badges.map((b) => b.id) } } });
  const ownedIds = new Set(owned.map((o) => o.badgeId));
  const toAward = badges.filter((b) => !ownedIds.has(b.id));

  await Promise.all(toAward.map((b) => prisma.userBadge.create({ data: { userId, badgeId: b.id } })));
  return toAward.map((b) => ({ code: b.code, name: b.name, icon: b.icon }));
}

router.get("/pieces/:id", requireAuth, async (req: AuthedRequest, res) => {
  const piece = await prisma.piece.findUnique({ where: { id: req.params.id } });
  if (!piece) return res.status(404).json({ error: "Pieza no encontrada" });

  res.json({
    id: piece.id,
    title: piece.title,
    composer: piece.composer,
    arranger: piece.arranger,
    keySignature: piece.keySignature,
    timeSignature: piece.timeSignature,
    seasonalTag: piece.seasonalTag,
    iconEmoji: piece.iconEmoji,
    aboutText: piece.aboutText,
    tips: piece.tips,
    content: JSON.parse(piece.content),
  });
});

router.get("/badges", requireAuth, async (req: AuthedRequest, res) => {
  const userBadges = await prisma.userBadge.findMany({
    where: { userId: req.auth!.userId },
    include: { badge: true },
    orderBy: { earnedAt: "desc" },
  });
  res.json(userBadges.map((ub) => ({ code: ub.badge.code, name: ub.badge.name, description: ub.badge.description, icon: ub.badge.icon, earnedAt: ub.earnedAt })));
});

export default router;
