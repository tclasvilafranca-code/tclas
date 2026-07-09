import { Router } from "express";
import { z } from "zod";
import { prisma } from "../prisma";
import { requireAuth, AuthedRequest } from "../auth";
import { buildCurriculumForUser, sanitizeExercise, computePhaseStats, computePracticeStats } from "../curriculum";
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

// El propio alumno ve en que bloque flaquea, no solo su profesora.
router.get("/me/stats", requireAuth, async (req: AuthedRequest, res) => {
  const phaseStats = await computePhaseStats(req.auth!.userId);
  res.json({ phaseStats });
});

// Estadisticas para la pantalla de Perfil: minutos practicados (total y ultimos
// 7 dias), racha, XP, insignias y piezas terminadas.
router.get("/me/profile-stats", requireAuth, async (req: AuthedRequest, res) => {
  const userId = req.auth!.userId;
  const profile = await prisma.studentProfile.findUnique({ where: { userId } });
  if (!profile) return res.status(400).json({ error: "Perfil de alumno no encontrado" });

  const [practiceStats, badgeCount, phaseStats] = await Promise.all([
    computePracticeStats(userId, profile.id),
    prisma.userBadge.count({ where: { userId } }),
    computePhaseStats(userId),
  ]);

  res.json({
    ...practiceStats,
    streakCurrent: profile.streakCurrent,
    streakLongest: profile.streakLongest,
    xpTotal: profile.xpTotal,
    badgeCount,
    phaseStats,
  });
});

const dailyGoalSchema = z.object({ dailyGoalMinutes: z.number().int().min(5).max(180) });

router.patch("/me/daily-goal", requireAuth, async (req: AuthedRequest, res) => {
  const parsed = dailyGoalSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Objetivo invalido (entre 5 y 180 minutos)" });

  const profile = await prisma.studentProfile.update({
    where: { userId: req.auth!.userId },
    data: { dailyGoalMinutes: parsed.data.dailyGoalMinutes },
  });
  res.json({ dailyGoalMinutes: profile.dailyGoalMinutes });
});

// Repaso espaciado: piezas ya terminadas cuyo proximo repaso ya ha llegado.
// Para cada una, propone la leccion donde peor precision tuvo (su punto mas debil).
router.get("/reviews/due", requireAuth, async (req: AuthedRequest, res) => {
  const profile = await prisma.studentProfile.findUnique({ where: { userId: req.auth!.userId } });
  if (!profile) return res.status(400).json({ error: "Perfil de alumno no encontrado" });

  const dueEntries = await prisma.repertoireEntry.findMany({
    where: { studentId: profile.id, status: "COMPLETED", nextReviewAt: { lte: new Date() } },
    include: {
      piece: true,
      lessons: { include: { progress: { where: { userId: req.auth!.userId } } } },
    },
  });

  const due = dueEntries
    .map((entry) => {
      const withProgress = entry.lessons.map((l) => ({ lesson: l, precisionScore: l.progress[0]?.precisionScore ?? 0 }));
      if (withProgress.length === 0) return null;
      const weakest = withProgress.reduce((min, cur) => (cur.precisionScore < min.precisionScore ? cur : min));
      return {
        entryId: entry.id,
        pieceId: entry.pieceId,
        pieceTitle: entry.piece.title,
        iconEmoji: entry.piece.iconEmoji,
        lessonId: weakest.lesson.id,
        reviewStage: entry.reviewStage,
      };
    })
    .filter((x): x is NonNullable<typeof x> => x !== null);

  res.json({ due });
});

router.get("/lessons/:id", requireAuth, async (req: AuthedRequest, res) => {
  const lesson = await prisma.lesson.findUnique({
    where: { id: req.params.id },
    include: { exercises: { orderBy: { index: "asc" } }, repertoireEntry: { include: { piece: true } } },
  });
  if (!lesson) return res.status(404).json({ error: "Leccion no encontrada" });

  let weekNumber = lesson.weekIndex;
  if (req.auth!.role === "STUDENT") {
    let profile = await prisma.studentProfile.findUnique({ where: { userId: req.auth!.userId } });
    if (!profile) return res.status(400).json({ error: "Perfil de alumno no encontrado" });
    profile = await recomputeHearts(profile);
    const tree = await buildCurriculumForUser(req.auth!.userId, profile.id);
    const flatLesson = tree.pieces.flatMap((p) => p.lessons).find((l) => l.id === lesson.id);
    if (!flatLesson || flatLesson.status === "LOCKED") {
      return res.status(403).json({ error: "Esta leccion todavia esta bloqueada" });
    }
    if (flatLesson.status === "SCHEDULED") {
      const dateStr = new Date(flatLesson.scheduledDate).toLocaleDateString("es-ES");
      return res.status(403).json({ error: `Esta semana todavia no ha llegado. Estara disponible el ${dateStr}.` });
    }
    // Sin corazones no se puede empezar una leccion nueva (las ya completadas se
    // pueden seguir repasando: no gastan corazones adicionales una vez a 0).
    if (flatLesson.status === "AVAILABLE" && profile.heartsCurrent <= 0) {
      return res.status(403).json({
        error: "Te has quedado sin corazones. Espera a que se recarguen para empezar una leccion nueva.",
        code: "NO_HEARTS",
        heartsCurrent: profile.heartsCurrent,
        heartsMax: profile.heartsMax,
        heartsUpdatedAt: profile.heartsUpdatedAt,
      });
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

// Repaso espaciado: intervalos crecientes (en dias) entre cada repaso de una
// pieza ya terminada. A partir del ultimo, se repite ese mismo intervalo
// indefinidamente como "mantenimiento".
const REVIEW_INTERVALS_DAYS = [3, 7, 14, 30];
const REVIEW_XP = 5;

const completeSchema = z.object({
  correctCount: z.number().int().min(0),
  totalCount: z.number().int().min(1),
  practiceSeconds: z.number().min(0).optional(),
});

// Trunca una fecha a medianoche (hora local del servidor), para agrupar
// la practica en un registro por dia (ver PracticeLog en schema.prisma).
function startOfDay(d: Date): Date {
  const truncated = new Date(d);
  truncated.setHours(0, 0, 0, 0);
  return truncated;
}

router.post("/lessons/:id/complete", requireAuth, async (req: AuthedRequest, res) => {
  const parsed = completeSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos" });
  const { correctCount, totalCount, practiceSeconds } = parsed.data;

  const lesson = await prisma.lesson.findUnique({ where: { id: req.params.id }, include: { repertoireEntry: true } });
  if (!lesson) return res.status(404).json({ error: "Leccion no encontrada" });

  const pct = correctCount / totalCount;
  const stars = starsForScore(pct);
  const userId = req.auth!.userId;
  const precisionScore = Math.round(pct * 1000);

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
      precisionScore,
      attempts: 1,
      completedAt: passed ? new Date() : null,
    },
    update: {
      status: passed ? "COMPLETED" : "AVAILABLE",
      stars: Math.max(stars, existing?.stars ?? 0),
      bestScore: Math.max(Math.round(pct * 100), existing?.bestScore ?? 0),
      precisionScore: Math.max(precisionScore, existing?.precisionScore ?? 0),
      attempts: { increment: 1 },
      completedAt: passed ? new Date() : existing?.completedAt ?? null,
    },
  });

  let xpAwarded = 0;
  let newBadges: { code: string; name: string; icon: string }[] = [];
  let profile = await prisma.studentProfile.findUnique({ where: { userId } });
  let isReview = false;
  const wasAlreadyCompleted = existing?.status === "COMPLETED";

  if (passed && profile && !wasAlreadyCompleted) {
    xpAwarded = Math.round(lesson.xpReward * (0.5 + 0.5 * (stars / 3)));
    profile = await awardXP(userId, xpAwarded, `Leccion completada: ${lesson.title}`);
    profile = await registerDailyActivity(profile);
    newBadges = await checkAndAwardBadges(userId, profile);

    const allLessonsInPiece = await prisma.lesson.findMany({ where: { repertoireEntryId: lesson.repertoireEntryId } });
    const completedInPiece = await prisma.progress.count({
      where: { userId, status: "COMPLETED", lessonId: { in: allLessonsInPiece.map((l) => l.id) } },
    });
    if (completedInPiece >= allLessonsInPiece.length) {
      await prisma.repertoireEntry.update({
        where: { id: lesson.repertoireEntryId },
        data: { status: "COMPLETED", reviewStage: 0, nextReviewAt: new Date(Date.now() + REVIEW_INTERVALS_DAYS[0] * 86400000) },
      });
    } else {
      await prisma.repertoireEntry.updateMany({
        where: { id: lesson.repertoireEntryId, status: "UPCOMING" },
        data: { status: "ACTIVE" },
      });
    }
  } else if (profile && wasAlreadyCompleted && lesson.repertoireEntry.status === "COMPLETED") {
    // La pieza entera ya estaba terminada: esta repeticion es una sesion de
    // repaso espaciado. Si le va bien, alarga el intervalo; si no, se vuelve
    // a proponer manana en vez de esperar semanas.
    isReview = true;
    const stage = lesson.repertoireEntry.reviewStage;
    const nextStage = passed ? stage + 1 : stage;
    const nextReviewAt = passed
      ? new Date(Date.now() + REVIEW_INTERVALS_DAYS[Math.min(nextStage, REVIEW_INTERVALS_DAYS.length - 1)] * 86400000)
      : new Date(Date.now() + 86400000);
    await prisma.repertoireEntry.update({
      where: { id: lesson.repertoireEntryId },
      data: { reviewStage: nextStage, nextReviewAt },
    });
    xpAwarded = REVIEW_XP;
    profile = await awardXP(userId, REVIEW_XP, `Repaso: ${lesson.title}`);
    profile = await registerDailyActivity(profile);
  }
  profile = profile ? await recomputeHearts(profile) : profile;

  if (practiceSeconds && practiceSeconds > 0) {
    const minutes = Math.max(1, Math.round(practiceSeconds / 60));
    const date = startOfDay(new Date());
    await prisma.practiceLog.upsert({
      where: { userId_date: { userId, date } },
      create: { userId, date, minutes },
      update: { minutes: { increment: minutes } },
    });
  }

  res.json({ progress, stars, score: precisionScore, xpAwarded, profile, newBadges, isReview });
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
