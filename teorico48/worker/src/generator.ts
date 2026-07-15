import type { PrismaClient } from "@prisma/client";

const EXAM_SIZE = 30;
// Un examen real de la DGT no admite superar 3 fallos para aprobar.
const MAX_ALLOWED_FAILS = 3;

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/** Genera un simulacro. Sin categorySlug, reparte entre todas las categorías
 * disponibles (simula el examen real); con categorySlug, se centra solo en
 * esa categoría (práctica dirigida del Modo Aprendizaje). */
export async function generateExam(prisma: PrismaClient, size: number = EXAM_SIZE, categorySlug?: string) {
  const allQuestions = await prisma.question.findMany({
    where: categorySlug ? { category: { slug: categorySlug } } : undefined,
    include: { category: true },
  });
  if (allQuestions.length === 0) return [];
  const shuffled = shuffle(allQuestions);
  return shuffled.slice(0, Math.min(size, shuffled.length));
}

/** Genera un repaso centrado en las preguntas que el alumno ha fallado antes. */
export async function generateReviewOfFails(prisma: PrismaClient, userId: string, size: number = EXAM_SIZE) {
  const failedAnswers = await prisma.answer.findMany({
    where: { correct: false, attempt: { userId } },
    include: { question: { include: { category: true } } },
    distinct: ["questionId"],
  });
  const shuffled = shuffle(failedAnswers.map((a) => a.question));
  return shuffled.slice(0, size);
}

export function isPassed(score: number, total: number) {
  const fails = total - score;
  return fails <= MAX_ALLOWED_FAILS;
}

export { EXAM_SIZE, MAX_ALLOWED_FAILS };
