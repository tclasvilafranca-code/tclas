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

  // Idempotente: si ya hay preguntas, no duplicar en cada arranque.
  const existing = await prisma.question.count();
  if (existing > 0) {
    console.log(`Ya existen ${existing} preguntas, se omite la carga del banco.`);
    return;
  }

  for (const q of questions) {
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
  }

  console.log(`Cargadas ${questions.length} preguntas en ${categories.length} categorias.`);
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
