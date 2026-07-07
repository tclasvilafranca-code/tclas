import { prisma } from "./prisma";
import { sanitizeExerciseData } from "./gamification";
import { ExerciseType } from "./types";

/**
 * Construye el arbol completo del track de un alumno (niveles > unidades > lecciones)
 * calculando dinamicamente el estado de cada leccion:
 * - COMPLETED si existe un Progress con ese estado
 * - AVAILABLE la primera leccion no completada en el orden del camino
 * - LOCKED el resto
 */
export async function buildCurriculumForUser(userId: string, trackId: string) {
  const track = await prisma.track.findUnique({
    where: { id: trackId },
    include: {
      levels: {
        orderBy: { index: "asc" },
        include: {
          units: {
            orderBy: { index: "asc" },
            include: {
              lessons: { orderBy: { index: "asc" } },
            },
          },
        },
      },
    },
  });
  if (!track) return null;

  const allLessonIds = track.levels.flatMap((l) => l.units.flatMap((u) => u.lessons.map((les) => les.id)));
  const progressRows = await prisma.progress.findMany({
    where: { userId, lessonId: { in: allLessonIds } },
  });
  const progressByLesson = new Map(progressRows.map((p) => [p.lessonId, p]));

  let frontierOpen = true;
  const levels = track.levels.map((level) => {
    const units = level.units.map((unit) => {
      const lessons = unit.lessons.map((lesson) => {
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
          index: lesson.index,
          title: lesson.title,
          description: lesson.description,
          xpReward: lesson.xpReward,
          status,
          stars: progress?.stars ?? 0,
        };
      });
      const unitCompleted = lessons.every((l) => l.status === "COMPLETED");
      return {
        id: unit.id,
        index: unit.index,
        title: unit.title,
        description: unit.description,
        completed: unitCompleted,
        lessons,
      };
    });
    const levelCompleted = units.every((u) => u.completed);
    return {
      id: level.id,
      index: level.index,
      title: level.title,
      description: level.description,
      iconEmoji: level.iconEmoji,
      completed: levelCompleted,
      units,
    };
  });

  return {
    id: track.id,
    code: track.code,
    name: track.name,
    description: track.description,
    levels,
  };
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
