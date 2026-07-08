import { Piece } from "@prisma/client";
import { prisma } from "./prisma";
import { generateLessonsForPiece } from "./generator";
import { PieceDef } from "./content/defs";

export function pieceToDef(piece: Piece): PieceDef {
  return {
    title: piece.title,
    composer: piece.composer,
    arranger: piece.arranger,
    ageGroup: piece.ageGroup as any,
    difficultyTier: piece.difficultyTier,
    defaultWeeks: piece.defaultWeeks,
    keySignature: piece.keySignature,
    timeSignature: piece.timeSignature,
    seasonalTag: piece.seasonalTag ?? undefined,
    iconEmoji: piece.iconEmoji,
    content: JSON.parse(piece.content),
  };
}

/** Crea una asignacion de repertorio para un alumno y genera sus lecciones/ejercicios semanales. */
export async function createRepertoireEntryWithLessons(params: {
  studentProfileId: string;
  piece: Piece;
  orderIndex: number;
  startDate: Date;
  durationWeeks?: number;
  teacherNote?: string;
  status?: string;
}) {
  const durationWeeks = params.durationWeeks ?? params.piece.defaultWeeks;

  const entry = await prisma.repertoireEntry.create({
    data: {
      studentId: params.studentProfileId,
      pieceId: params.piece.id,
      orderIndex: params.orderIndex,
      startDate: params.startDate,
      durationWeeks,
      teacherNote: params.teacherNote ?? "",
      status: params.status ?? (params.orderIndex === 1 ? "ACTIVE" : "UPCOMING"),
    },
  });

  const lessonDefs = generateLessonsForPiece(pieceToDef(params.piece), durationWeeks);
  for (const [li, lessonDef] of lessonDefs.entries()) {
    const lesson = await prisma.lesson.create({
      data: {
        repertoireEntryId: entry.id,
        weekIndex: li + 1,
        title: lessonDef.title,
        description: lessonDef.description,
        xpReward: lessonDef.xpReward ?? 15,
      },
    });
    for (const [ei, ex] of lessonDef.exercises.entries()) {
      await prisma.exercise.create({
        data: {
          lessonId: lesson.id,
          index: ei + 1,
          type: ex.type,
          phase: ex.phase,
          prompt: ex.prompt,
          data: JSON.stringify(ex.data),
          explanation: ex.explanation,
        },
      });
    }
  }

  return entry;
}

/**
 * Borra y regenera las lecciones/ejercicios de una asignacion ya existente,
 * conservando la propia asignacion (fechas, orden, nota). Se usa cuando el
 * generador de contenido cambia de forma incompatible (p.ej. nuevas fases).
 */
export async function regenerateLessonsForEntry(entryId: string, piece: Piece, durationWeeks: number) {
  const lessonIds = (await prisma.lesson.findMany({ where: { repertoireEntryId: entryId }, select: { id: true } })).map((l) => l.id);
  const exerciseIds = (await prisma.exercise.findMany({ where: { lessonId: { in: lessonIds } }, select: { id: true } })).map((e) => e.id);
  await prisma.exerciseAttempt.deleteMany({ where: { exerciseId: { in: exerciseIds } } });
  await prisma.progress.deleteMany({ where: { lessonId: { in: lessonIds } } });
  await prisma.exercise.deleteMany({ where: { lessonId: { in: lessonIds } } });
  await prisma.lesson.deleteMany({ where: { repertoireEntryId: entryId } });

  const lessonDefs = generateLessonsForPiece(pieceToDef(piece), durationWeeks);
  for (const [li, lessonDef] of lessonDefs.entries()) {
    const lesson = await prisma.lesson.create({
      data: {
        repertoireEntryId: entryId,
        weekIndex: li + 1,
        title: lessonDef.title,
        description: lessonDef.description,
        xpReward: lessonDef.xpReward ?? 15,
      },
    });
    for (const [ei, ex] of lessonDef.exercises.entries()) {
      await prisma.exercise.create({
        data: {
          lessonId: lesson.id,
          index: ei + 1,
          type: ex.type,
          phase: ex.phase,
          prompt: ex.prompt,
          data: JSON.stringify(ex.data),
          explanation: ex.explanation,
        },
      });
    }
  }
}

/**
 * Asigna varias piezas seguidas a un alumno (constructor de repertorio / duplicado
 * desde otro alumno). Cada pieza empieza justo cuando termina la anterior; si el
 * alumno ya tiene repertorio, continua desde el final de su ultima pieza salvo que
 * se indique una fecha de inicio explicita.
 */
export async function bulkAssignRepertoire(params: {
  studentProfileId: string;
  items: { pieceId: string; durationWeeks?: number; teacherNote?: string }[];
  startDate?: Date;
}) {
  const pieces = await prisma.piece.findMany({ where: { id: { in: params.items.map((i) => i.pieceId) } } });
  const pieceMap = new Map(pieces.map((p) => [p.id, p]));

  const lastEntry = await prisma.repertoireEntry.findFirst({
    where: { studentId: params.studentProfileId },
    orderBy: { orderIndex: "desc" },
  });

  let orderIndex = lastEntry?.orderIndex ?? 0;
  let cursor =
    params.startDate ??
    (lastEntry ? new Date(lastEntry.startDate.getTime() + lastEntry.durationWeeks * 7 * 86400000) : new Date());

  const created = [];
  for (const item of params.items) {
    const piece = pieceMap.get(item.pieceId);
    if (!piece) continue;
    orderIndex += 1;
    const durationWeeks = item.durationWeeks ?? piece.defaultWeeks;
    const entry = await createRepertoireEntryWithLessons({
      studentProfileId: params.studentProfileId,
      piece,
      orderIndex,
      startDate: cursor,
      durationWeeks,
      teacherNote: item.teacherNote ?? "",
    });
    created.push(entry);
    cursor = new Date(cursor.getTime() + durationWeeks * 7 * 86400000);
  }
  return created;
}
