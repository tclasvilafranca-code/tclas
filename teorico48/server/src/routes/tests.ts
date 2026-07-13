import { Router } from "express";
import { z } from "zod";
import { PrismaClient } from "@prisma/client";
import { requireAuth, AuthedRequest } from "../middleware/auth";
import { generateExam, generateReviewOfFails, isPassed, EXAM_SIZE } from "../generator";

const prisma = new PrismaClient();
export const testsRouter = Router();

const FREE_DAILY_EXAMS = 1;

testsRouter.get("/categories", async (_req, res) => {
  const categories = await prisma.category.findMany({ orderBy: { name: "asc" } });
  res.json({ categories });
});

function publicQuestion(q: { id: string; text: string; imageUrl: string | null; options: unknown; category: { name: string; slug: string } }) {
  return {
    id: q.id,
    text: q.text,
    imageUrl: q.imageUrl,
    options: q.options,
    category: q.category.name,
  };
}

testsRouter.post("/exam", requireAuth, async (req: AuthedRequest, res) => {
  const user = await prisma.user.findUnique({ where: { id: req.userId } });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });

  if (!user.isPremium) {
    const since = new Date();
    since.setHours(0, 0, 0, 0);
    const todaysExams = await prisma.testAttempt.count({
      where: { userId: user.id, mode: "exam", startedAt: { gte: since } },
    });
    if (todaysExams >= FREE_DAILY_EXAMS) {
      return res.status(403).json({
        error: "Has alcanzado el límite de simulacros gratuitos de hoy. Hazte con el Pack 48h para simulacros ilimitados.",
        upgradeRequired: true,
      });
    }
  }

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
});

testsRouter.post("/review", requireAuth, async (req: AuthedRequest, res) => {
  const user = await prisma.user.findUnique({ where: { id: req.userId } });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });

  if (!user.isPremium) {
    return res.status(403).json({
      error: "El modo repaso de fallos es una función premium. Hazte con el Pack 48h para desbloquearlo.",
      upgradeRequired: true,
    });
  }

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
});

const submitSchema = z.object({
  answers: z.array(
    z.object({
      questionId: z.string(),
      selectedIndex: z.number().int().min(0).max(3).nullable(),
    })
  ),
});

testsRouter.post("/:attemptId/submit", requireAuth, async (req: AuthedRequest, res) => {
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

  const updated = await prisma.testAttempt.update({
    where: { id: attempt.id },
    data: { finishedAt: new Date(), score, total, passed },
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
  });
});

testsRouter.get("/history", requireAuth, async (req: AuthedRequest, res) => {
  const attempts = await prisma.testAttempt.findMany({
    where: { userId: req.userId, finishedAt: { not: null } },
    orderBy: { finishedAt: "desc" },
    take: 20,
  });
  res.json({ attempts });
});
