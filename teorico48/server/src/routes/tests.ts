import { Router } from "express";
import { z } from "zod";
import { PrismaClient } from "@prisma/client";
import { requireAuth, AuthedRequest } from "../middleware/auth";
import { generateExam, generateReviewOfFails, isPassed, EXAM_SIZE } from "../generator";
import { BADGES, XP_PER_CORRECT, levelForXp, unlockedBadgeIds, updateStreak, xpForAttempt } from "../gamification";
import { asyncHandler } from "../lib/asyncHandler";

const prisma = new PrismaClient();
export const testsRouter = Router();

testsRouter.get(
  "/categories",
  asyncHandler(async (_req, res) => {
    const categories = await prisma.category.findMany({ orderBy: { name: "asc" } });
    res.json({ categories });
  })
);

// Precisión por categoría a partir de TODO el historial de respuestas
// (simulacro, repaso y Modo Aprendizaje incluidos): a diferencia de las
// estadísticas de "aprobados", aquí interesa la señal completa para saber
// de verdad en qué falla cada alumno, no solo lo que cuenta como examen real.
testsRouter.get("/category-stats", requireAuth, asyncHandler(async (req: AuthedRequest, res) => {
  const [categories, answers] = await Promise.all([
    prisma.category.findMany({ orderBy: { name: "asc" } }),
    prisma.answer.findMany({
      where: { attempt: { userId: req.userId, finishedAt: { not: null } } },
      select: { correct: true, question: { select: { categoryId: true } } },
    }),
  ]);

  const totals = new Map<string, { total: number; correct: number }>();
  for (const a of answers) {
    const entry = totals.get(a.question.categoryId) ?? { total: 0, correct: 0 };
    entry.total += 1;
    if (a.correct) entry.correct += 1;
    totals.set(a.question.categoryId, entry);
  }

  const stats = categories
    .map((c) => {
      const t = totals.get(c.id) ?? { total: 0, correct: 0 };
      return {
        slug: c.slug,
        name: c.name,
        answered: t.total,
        correct: t.correct,
        accuracy: t.total > 0 ? Math.round((t.correct / t.total) * 100) : null,
      };
    })
    // Peor precisión primero; las categorías sin practicar van al final.
    .sort((a, b) => {
      if (a.accuracy === null && b.accuracy === null) return 0;
      if (a.accuracy === null) return 1;
      if (b.accuracy === null) return -1;
      return a.accuracy - b.accuracy;
    });

  res.json({ categories: stats });
}));

function publicQuestion(q: { id: string; text: string; imageUrl: string | null; options: unknown; category: { name: string; slug: string } }) {
  return {
    id: q.id,
    text: q.text,
    imageUrl: q.imageUrl,
    options: q.options,
    category: q.category.name,
  };
}

// El modo Aprendizaje corrige al instante, así que a diferencia de
// publicQuestion() sí incluye la respuesta correcta y su explicación
// desde el principio: el cliente solo las revela tras responder.
function learnQuestion(q: {
  id: string;
  text: string;
  imageUrl: string | null;
  options: unknown;
  correctIndex: number;
  explanation: string;
  category: { name: string; slug: string };
}) {
  return {
    id: q.id,
    text: q.text,
    imageUrl: q.imageUrl,
    options: q.options,
    category: q.category.name,
    correctIndex: q.correctIndex,
    explanation: q.explanation,
  };
}

testsRouter.post("/exam", requireAuth, asyncHandler(async (req: AuthedRequest, res) => {
  const user = await prisma.user.findUnique({ where: { id: req.userId } });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });

  const questions = await generateExam(EXAM_SIZE);
  if (questions.length === 0) {
    return res.status(500).json({ error: "Todavía no hay preguntas cargadas" });
  }

  const attempt = await prisma.testAttempt.create({
    data: { userId: user.id, mode: "exam", total: questions.length },
  });

  res.json({
    attemptId: attempt.id,
    questions: questions.map(publicQuestion),
  });
}));

const learnSchema = z.object({ categorySlug: z.string().trim().min(1).optional() });

// Modo Aprendizaje: gratis y sin límite diario, a propósito — es la fase
// previa al simulacro real, pensada para animar a estudiar sin restricciones.
// Admite categorySlug para practicar de forma dirigida solo una categoría.
testsRouter.post("/learn", requireAuth, asyncHandler(async (req: AuthedRequest, res) => {
  const parsed = learnSchema.safeParse(req.body ?? {});
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.issues[0].message });
  }
  const user = await prisma.user.findUnique({ where: { id: req.userId } });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });

  const questions = await generateExam(EXAM_SIZE, parsed.data.categorySlug);
  if (questions.length === 0) {
    return res.status(404).json({ error: "No hay preguntas disponibles para esa categoría todavía" });
  }

  const attempt = await prisma.testAttempt.create({
    data: { userId: user.id, mode: "learn", total: questions.length },
  });

  res.json({
    attemptId: attempt.id,
    questions: questions.map(learnQuestion),
  });
}));

testsRouter.post("/review", requireAuth, asyncHandler(async (req: AuthedRequest, res) => {
  const user = await prisma.user.findUnique({ where: { id: req.userId } });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });

  const questions = await generateReviewOfFails(user.id, EXAM_SIZE);
  if (questions.length === 0) {
    return res.status(404).json({ error: "Todavía no has fallado ninguna pregunta. ¡Bien!" });
  }

  const attempt = await prisma.testAttempt.create({
    data: { userId: user.id, mode: "practice", total: questions.length },
  });

  res.json({
    attemptId: attempt.id,
    questions: questions.map(publicQuestion),
  });
}));

const submitSchema = z.object({
  answers: z.array(
    z.object({
      questionId: z.string(),
      selectedIndex: z.number().int().min(0).max(3).nullable(),
    })
  ),
});

testsRouter.post("/:attemptId/submit", requireAuth, asyncHandler(async (req: AuthedRequest, res) => {
  const parsed = submitSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.issues[0].message });
  }

  const attempt = await prisma.testAttempt.findUnique({ where: { id: req.params.attemptId } });
  if (!attempt || attempt.userId !== req.userId) {
    return res.status(404).json({ error: "Intento no encontrado" });
  }
  if (attempt.finishedAt) {
    return res.status(409).json({ error: "Este intento ya se envió" });
  }

  const questionIds = parsed.data.answers.map((a) => a.questionId);
  const questions = await prisma.question.findMany({ where: { id: { in: questionIds } } });
  const byId = new Map(questions.map((q) => [q.id, q]));

  let score = 0;
  const answerRows = parsed.data.answers.map((a) => {
    const question = byId.get(a.questionId);
    const correct = !!question && a.selectedIndex === question.correctIndex;
    if (correct) score += 1;
    return {
      attemptId: attempt.id,
      questionId: a.questionId,
      selectedIndex: a.selectedIndex,
      correct,
    };
  });

  await prisma.answer.createMany({ data: answerRows });

  const total = answerRows.length;
  const passed = isPassed(score, total);
  // El modo Aprendizaje es una fase previa de estudio, no un intento real:
  // no cuenta para las estadísticas de simulacros ni da el bonus de
  // aprobado/perfecto, solo XP por cada acierto.
  const isLearnMode = attempt.mode === "learn";

  // Snapshot de intentos previos (antes de cerrar este) para saber qué medallas eran nuevas.
  // Se excluye el modo Aprendizaje: no debe contar como "test completado" real.
  const priorAttempts = await prisma.testAttempt.findMany({
    where: { userId: req.userId, finishedAt: { not: null }, mode: { not: "learn" } },
    select: { score: true, total: true, passed: true },
  });

  const updated = await prisma.testAttempt.update({
    where: { id: attempt.id },
    data: { finishedAt: new Date(), score, total, passed },
  });

  const user = await prisma.user.findUniqueOrThrow({ where: { id: req.userId } });
  const xpGained = isLearnMode ? score * XP_PER_CORRECT : xpForAttempt(score, total, passed);
  const streak = updateStreak(user.lastActivityDate, user.currentStreak, user.longestStreak);
  const newXp = user.xp + xpGained;

  const beforeStats = {
    xp: user.xp,
    longestStreak: user.longestStreak,
    totalAttempts: priorAttempts.length,
    totalPassed: priorAttempts.filter((a) => a.passed).length,
    hasPerfect: priorAttempts.some((a) => a.score !== null && a.total !== null && a.score === a.total),
    theorySessionsCompleted: user.theoryCompletedSessions.length,
  };
  const afterStats = {
    xp: newXp,
    longestStreak: streak.longestStreak,
    totalAttempts: beforeStats.totalAttempts + (isLearnMode ? 0 : 1),
    totalPassed: beforeStats.totalPassed + (!isLearnMode && passed ? 1 : 0),
    hasPerfect: beforeStats.hasPerfect || (!isLearnMode && score === total),
    theorySessionsCompleted: beforeStats.theorySessionsCompleted,
  };

  const badgesBefore = new Set(unlockedBadgeIds(beforeStats));
  const newBadgeIds = unlockedBadgeIds(afterStats).filter((id) => !badgesBefore.has(id));
  const newBadges = BADGES.filter((b) => newBadgeIds.includes(b.id)).map((b) => ({ id: b.id, label: b.label, emoji: b.emoji }));

  await prisma.user.update({
    where: { id: user.id },
    data: {
      xp: newXp,
      currentStreak: streak.currentStreak,
      longestStreak: streak.longestStreak,
      lastActivityDate: streak.lastActivityDate,
    },
  });

  const detail = await prisma.answer.findMany({
    where: { attemptId: attempt.id },
    include: { question: { include: { category: true } } },
  });

  res.json({
    score,
    total,
    passed,
    results: detail.map((d) => ({
      questionId: d.questionId,
      text: d.question.text,
      options: d.question.options,
      correctIndex: d.question.correctIndex,
      selectedIndex: d.selectedIndex,
      correct: d.correct,
      explanation: d.question.explanation,
      category: d.question.category.name,
    })),
    attempt: updated,
    gamification: {
      xpGained,
      totalXp: newXp,
      level: levelForXp(newXp),
      leveledUp: levelForXp(user.xp) !== levelForXp(newXp),
      currentStreak: streak.currentStreak,
      newBadges,
    },
  });
}));

testsRouter.get("/stats", requireAuth, asyncHandler(async (req: AuthedRequest, res) => {
  const user = await prisma.user.findUniqueOrThrow({ where: { id: req.userId } });
  const attempts = await prisma.testAttempt.findMany({
    // El modo Aprendizaje no cuenta como simulacro real para estas estadísticas.
    where: { userId: req.userId, finishedAt: { not: null }, mode: { not: "learn" } },
    select: { score: true, total: true, passed: true },
  });

  const stats = {
    xp: user.xp,
    longestStreak: user.longestStreak,
    totalAttempts: attempts.length,
    totalPassed: attempts.filter((a) => a.passed).length,
    hasPerfect: attempts.some((a) => a.score !== null && a.total !== null && a.score === a.total),
    theorySessionsCompleted: user.theoryCompletedSessions.length,
  };

  const unlocked = new Set(unlockedBadgeIds(stats));

  res.json({
    xp: user.xp,
    level: levelForXp(user.xp),
    currentStreak: user.currentStreak,
    longestStreak: user.longestStreak,
    totalAttempts: stats.totalAttempts,
    totalPassed: stats.totalPassed,
    badges: BADGES.map((b) => ({ id: b.id, label: b.label, emoji: b.emoji, unlocked: unlocked.has(b.id) })),
  });
}));

testsRouter.get("/history", requireAuth, asyncHandler(async (req: AuthedRequest, res) => {
  const attempts = await prisma.testAttempt.findMany({
    where: { userId: req.userId, finishedAt: { not: null } },
    orderBy: { finishedAt: "desc" },
    take: 20,
  });
  res.json({ attempts });
}));
