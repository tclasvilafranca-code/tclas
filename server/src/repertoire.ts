import { Piece } from "@prisma/client";
import { prisma } from "./prisma";
import { generateLessonsForPiece } from "./generator";
import { PieceDef } from "./content/defs";

function pieceToDef(piece: Piece): PieceDef {
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
          prompt: ex.prompt,
          data: JSON.stringify(ex.data),
          explanation: ex.explanation,
        },
      });
    }
  }

  return entry;
}
