import { prisma } from "./prisma";
import { sanitizeExerciseData } from "./gamification";
import { ExerciseType } from "./types";

/**
 * Construye el camino completo de un alumno: su repertorio de piezas, en orden,
 * cada una con sus lecciones semanales. El estado de cada leccion se calcula
 * dinamicamente:
 * - COMPLETED si existe un Progress con ese estado
 * - AVAILABLE la primera leccion no completada en el orden del camino
 * - LOCKED el resto
 */
export async function buildCurriculumForUser(userId: string, studentProfileId: string) {
  const entries = await prisma.repertoireEntry.findMany({
    where: { studentId: studentProfileId },
    orderBy: { orderIndex: "asc" },
    include: {
      piece: true,
      lessons: { orderBy: { weekIndex: "asc" } },
    },
  });

  const allLessonIds = entries.flatMap((e) => e.lessons.map((l) => l.id));
  const progressRows = await prisma.progress.findMany({
    where: { userId, lessonId: { in: allLessonIds } },
  });
  const progressByLesson = new Map(progressRows.map((p) => [p.lessonId, p]));

  let frontierOpen = true;
  const pieces = entries.map((entry) => {
    const lessons = entry.lessons.map((lesson) => {
      const progress = progressByLesson.get(lesson.id);
      let status: "LOCKED" | "AVAILABLE" | "COMPLETED";
      if (progress?.status === "COMPLETED") {
        status = "COMPLETED";
      } else if (frontierOpen) {
        status = "AVAILABLE";
        frontierOpen = false;
      } else {
        status = "LOCKED";
      }
      return {
        id: lesson.id,
        weekIndex: lesson.weekIndex,
        title: lesson.title,
        description: lesson.description,
        xpReward: lesson.xpReward,
        status,
        stars: progress?.stars ?? 0,
      };
    });
    const completed = lessons.every((l) => l.status === "COMPLETED");
    return {
      id: entry.id,
      orderIndex: entry.orderIndex,
      startDate: entry.startDate,
      durationWeeks: entry.durationWeeks,
      teacherNote: entry.teacherNote,
      status: entry.status,
      completed,
      piece: {
        id: entry.piece.id,
        title: entry.piece.title,
        composer: entry.piece.composer,
        iconEmoji: entry.piece.iconEmoji,
        seasonalTag: entry.piece.seasonalTag,
        keySignature: entry.piece.keySignature,
        timeSignature: entry.piece.timeSignature,
      },
      lessons,
    };
  });

  return { pieces };
}

export function sanitizeExercise(ex: { id: string; index: number; type: string; prompt: string; data: string; explanation: string }) {
  const parsed = JSON.parse(ex.data);
  return {
    id: ex.id,
    index: ex.index,
    type: ex.type as ExerciseType,
    prompt: ex.prompt,
    data: sanitizeExerciseData(ex.type as ExerciseType, parsed),
  };
}
