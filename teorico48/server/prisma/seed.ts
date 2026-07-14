import { PrismaClient } from "@prisma/client";
import { categories, questions } from "../src/content/questions";

const prisma = new PrismaClient();

/** Baraja las opciones para que la respuesta correcta no quede siempre en la misma posición. */
function shuffleOptions(options: [string, string, string, string], correctIndex: number) {
  const indices = [0, 1, 2, 3];
  for (let i = indices.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [indices[i], indices[j]] = [indices[j], indices[i]];
  }
  const shuffled = indices.map((i) => options[i]) as [string, string, string, string];
  const newCorrectIndex = indices.indexOf(correctIndex);
  return { options: shuffled, correctIndex: newCorrectIndex };
}

async function main() {
  const categoryIds = new Map<string, string>();

  for (const cat of categories) {
    const created = await prisma.category.upsert({
      where: { slug: cat.slug },
      update: { name: cat.name },
      create: cat,
    });
    categoryIds.set(cat.slug, created.id);
  }

  // Idempotente por pregunta (no por arranque): permite ampliar el banco de
  // preguntas.ts en el futuro y volver a sembrar sin duplicar las que ya
  // existen en la base de datos.
  const existingTexts = new Set((await prisma.question.findMany({ select: { text: true } })).map((q) => q.text));

  let created = 0;
  for (const q of questions) {
    if (existingTexts.has(q.text)) continue;
    const categoryId = categoryIds.get(q.category);
    if (!categoryId) throw new Error(`Categoria desconocida: ${q.category}`);
    const { options, correctIndex } = shuffleOptions(q.options, q.correctIndex);
    await prisma.question.create({
      data: {
        categoryId,
        text: q.text,
        options,
        correctIndex,
        explanation: q.explanation,
        isSerious: q.isSerious ?? false,
      },
    });
    created += 1;
  }

  console.log(`Cargadas ${created} preguntas nuevas (${questions.length - created} ya existían) en ${categories.length} categorías.`);
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
