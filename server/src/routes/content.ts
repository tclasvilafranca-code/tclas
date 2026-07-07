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

router.get("/tracks", async (_req, res) => {
  const tracks = await prisma.track.findMany({ orderBy: { order: "asc" } });
  res.json(tracks);
});

const onboardingSchema = z.object({
  ageGroup: z.enum(["KIDS", "TEENS", "ADULTS"]),
  trackId: z.string(),
  birthYear: z.number().int().optional(),
});

router.post("/onboarding", requireAuth, async (req: AuthedRequest, res) => {
  if (req.auth!.role !== "STUDENT") return res.status(403).json({ error: "Solo alumnos" });
  const parsed = onboardingSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos" });

  const track = await prisma.track.findUnique({ where: { id: parsed.data.trackId } });
  if (!track) return res.status(404).json({ error: "Track no encontrado" });

  const profile = await prisma.studentProfile.update({
    where: { userId: req.auth!.userId },
    data: {
      ageGroup: parsed.data.ageGroup,
      trackId: parsed.data.trackId,
      birthYear: parsed.data.birthYear,
      onboarded: true,
    },
  });
  res.json(profile);
});

router.get("/curriculum", requireAuth, async (req: AuthedRequest, res) => {
  const profile = await prisma.studentProfile.findUnique({ where: { userId: req.auth!.userId } });
  if (!profile?.trackId) return res.status(400).json({ error: "El alumno no tiene track asignado todavia" });
  const tree = await buildCurriculumForUser(req.auth!.userId, profile.trackId);
  res.json(tree);
});

router.get("/lessons/:id", requireAuth, async (req: AuthedRequest, res) => {
  const lesson = await prisma.lesson.findUnique({
    where: { id: req.params.id },
    include: { exercises: { orderBy: { index: "asc" } }, unit: { include: { level: true } } },
  });
  if (!lesson) return res.status(404).json({ error: "Leccion no encontrada" });

  const profile = await prisma.studentProfile.findUnique({ where: { userId: req.auth!.userId } });
  if (!profile?.trackId) return res.status(400).json({ error: "El alumno no tiene track asignado todavia" });
  const tree = await buildCurriculumForUser(req.auth!.userId, profile.trackId);
  const flatStatus = tree?.levels.flatMap((l) => l.units.flatMap((u) => u.lessons)).find((l) => l.id === lesson.id)?.status;
  if (!flatStatus || flatStatus === "LOCKED") return res.status(403).json({ error: "Esta leccion todavia esta bloqueada" });

  res.json({
    id: lesson.id,
    title: lesson.title,
    description: lesson.description,
    xpReward: lesson.xpReward,
    unitTitle: lesson.unit.title,
    levelTitle: lesson.unit.level.title,
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
    correctAnswer: correct ? undefined : data.correctAnswer ?? data.answer ?? data.notes ?? data.pattern,
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

  const lesson = await prisma.lesson.findUnique({ where: { id: req.params.id } });
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
    }
  }
  profile = profile ? await recomputeHearts(profile) : profile;

  res.json({ progress, stars, xpAwarded, profile, newBadges });
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

router.get("/badges", requireAuth, async (req: AuthedRequest, res) => {
  const userBadges = await prisma.userBadge.findMany({
    where: { userId: req.auth!.userId },
    include: { badge: true },
    orderBy: { earnedAt: "desc" },
  });
  res.json(userBadges.map((ub) => ({ code: ub.badge.code, name: ub.badge.name, description: ub.badge.description, icon: ub.badge.icon, earnedAt: ub.earnedAt })));
});

export default router;
