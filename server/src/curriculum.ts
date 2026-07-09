import { prisma } from "./prisma";
import { sanitizeExerciseData } from "./gamification";
import { ExerciseType } from "./types";

const MS_PER_WEEK = 7 * 24 * 60 * 60 * 1000;

/** Porcentaje de acierto historico por bloque (agilidad visual, agudeza
 * auditiva, notas al vuelo, practica de partitura). Se usa tanto para que la
 * profesora vea el rendimiento de un alumno como para que el propio alumno
 * vea el suyo. */
export async function computePhaseStats(userId: string): Promise<Record<string, { correct: number; total: number }>> {
  const attempts = await prisma.exerciseAttempt.findMany({
    where: { userId },
    select: { correct: true, exercise: { select: { phase: true } } },
  });
  const phaseTotals = new Map<string, { correct: number; total: number }>();
  for (const a of attempts) {
    const entry = phaseTotals.get(a.exercise.phase) ?? { correct: 0, total: 0 };
    entry.total += 1;
    if (a.correct) entry.correct += 1;
    phaseTotals.set(a.exercise.phase, entry);
  }
  return Object.fromEntries(phaseTotals);
}

function addWeeks(date: Date, weeks: number): Date {
  return new Date(date.getTime() + weeks * MS_PER_WEEK);
}

function startOfDay(date: Date): Date {
  const d = new Date(date);
  d.setHours(0, 0, 0, 0);
  return d;
}

export interface PracticeStats {
  totalMinutes: number;
  last7Days: { date: string; minutes: number }[];
  piecesCompleted: number;
}

/** Minutos practicados (total y ultimos 7 dias) y piezas terminadas. Se usa
 * tanto en el Perfil del propio alumno como en el panel de su profesor/a,
 * para que ambos vean exactamente los mismos numeros. */
export async function computePracticeStats(userId: string, studentProfileId: string): Promise<PracticeStats> {
  const today = startOfDay(new Date());
  const sevenDaysAgo = new Date(today.getTime() - 6 * 86400000);

  const [totalAgg, recentLogs, piecesCompleted] = await Promise.all([
    prisma.practiceLog.aggregate({ where: { userId }, _sum: { minutes: true } }),
    prisma.practiceLog.findMany({ where: { userId, date: { gte: sevenDaysAgo } } }),
    prisma.repertoireEntry.count({ where: { studentId: studentProfileId, status: "COMPLETED" } }),
  ]);

  const minutesByDate = new Map(recentLogs.map((l) => [startOfDay(l.date).getTime(), l.minutes]));
  const last7Days = Array.from({ length: 7 }, (_, i) => {
    const d = new Date(sevenDaysAgo.getTime() + i * 86400000);
    return { date: d.toISOString().slice(0, 10), minutes: minutesByDate.get(d.getTime()) ?? 0 };
  });

  return { totalMinutes: totalAgg._sum.minutes ?? 0, last7Days, piecesCompleted };
}

/**
 * Construye el camino completo de un alumno: su repertorio de piezas, en orden,
 * cada una con sus lecciones semanales. La numeracion de semana es continua a
 * lo largo de todo el curso (no reinicia en cada pieza), calculada a partir de
 * las fechas reales de inicio de cada pieza.
 *
 * El estado de cada leccion se calcula dinamicamente:
 * - COMPLETED si existe un Progress con ese estado
 * - AVAILABLE la primera leccion no completada en el orden del camino, solo si
 *   ya ha llegado su semana (fecha real <= hoy)
 * - SCHEDULED si seria la siguiente pero su semana todavia no ha llegado
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

  if (entries.length === 0) return { pieces: [] };

  const courseStart = startOfDay(entries.reduce((min, e) => (e.startDate < min ? e.startDate : min), entries[0].startDate));
  const today = startOfDay(new Date());

  const allLessonIds = entries.flatMap((e) => e.lessons.map((l) => l.id));
  const progressRows = await prisma.progress.findMany({
    where: { userId, lessonId: { in: allLessonIds } },
  });
  const progressByLesson = new Map(progressRows.map((p) => [p.lessonId, p]));

  let frontierOpen = true;
  const pieces = entries.map((entry) => {
    const lessons = entry.lessons.map((lesson) => {
      const progress = progressByLesson.get(lesson.id);
      const lessonDate = startOfDay(addWeeks(entry.startDate, lesson.weekIndex - 1));
      const weekNumber = Math.floor((lessonDate.getTime() - courseStart.getTime()) / MS_PER_WEEK) + 1;

      let status: "LOCKED" | "SCHEDULED" | "AVAILABLE" | "COMPLETED";
      if (progress?.status === "COMPLETED") {
        status = "COMPLETED";
      } else if (frontierOpen) {
        if (lessonDate <= today) {
          status = "AVAILABLE";
        } else {
          status = "SCHEDULED";
        }
        frontierOpen = false;
      } else {
        status = "LOCKED";
      }
      return {
        id: lesson.id,
        weekIndex: lesson.weekIndex,
        weekNumber,
        scheduledDate: lessonDate,
        title: lesson.title,
        description: lesson.description,
        xpReward: lesson.xpReward,
        status,
        stars: progress?.stars ?? 0,
        precisionScore: progress?.precisionScore ?? 0,
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

export function sanitizeExercise(ex: { id: string; index: number; type: string; phase: string; prompt: string; data: string; explanation: string }) {
  const parsed = JSON.parse(ex.data);
  return {
    id: ex.id,
    index: ex.index,
    type: ex.type as ExerciseType,
    phase: ex.phase,
    prompt: ex.prompt,
    data: sanitizeExerciseData(ex.type as ExerciseType, parsed),
  };
}
