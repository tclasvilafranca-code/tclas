import { describe, it, expect, afterAll } from "vitest";
import { prisma } from "./prisma";
import { computeAdaptiveDifficulty } from "./adaptive";

// Integracion contra la BD real: crea intentos de usar-y-tirar para un
// alumno de prueba y verifica que la dificultad calculada refleje su
// acierto historico real en cada bloque.
const cleanupUserIds: string[] = [];
const cleanupExerciseIds: string[] = [];
const cleanupLessonIds: string[] = [];
const cleanupEntryIds: string[] = [];
const cleanupPieceIds: string[] = [];

async function makeAttempts(pattern: { phase: string; correct: boolean }[]) {
  const teacher = await prisma.user.create({
    data: { name: "Test Teacher Adaptive", email: `test-teacher-ad-${Date.now()}-${Math.random().toString(36).slice(2)}@example.com`, passwordHash: "x", role: "TEACHER" },
  });
  cleanupUserIds.push(teacher.id);
  const piece = await prisma.piece.create({
    data: {
      title: `Test Adaptive Piece ${Date.now()}-${Math.random().toString(36).slice(2)}`,
      ageGroup: "KIDS",
      difficultyTier: 1,
      keySignature: "Do Mayor",
      timeSignature: "4/4",
      content: JSON.stringify({ clef: "treble", melody: ["C4"], melodyRhythm: [1], featuredNotes: ["C4"] }),
    },
  });
  cleanupPieceIds.push(piece.id);
  const student = await prisma.user.create({
    data: {
      name: "Test Student Adaptive",
      username: `test-student-ad-${Date.now()}-${Math.random().toString(36).slice(2)}`,
      pinHash: "x",
      role: "STUDENT",
      studentProfile: { create: { ageGroup: "KIDS", teacherId: teacher.id, onboarded: true } },
    },
    include: { studentProfile: true },
  });
  cleanupUserIds.push(student.id);
  const entry = await prisma.repertoireEntry.create({
    data: { studentId: student.studentProfile!.id, pieceId: piece.id, orderIndex: 1, startDate: new Date(), durationWeeks: 1 },
  });
  cleanupEntryIds.push(entry.id);
  const lesson = await prisma.lesson.create({ data: { repertoireEntryId: entry.id, weekIndex: 1, title: "test", description: "test" } });
  cleanupLessonIds.push(lesson.id);

  for (const [i, p] of pattern.entries()) {
    const exercise = await prisma.exercise.create({
      data: { lessonId: lesson.id, index: i + 1, type: "NOTE_NAME", phase: p.phase, prompt: "test", data: "{}", explanation: "" },
    });
    cleanupExerciseIds.push(exercise.id);
    await prisma.exerciseAttempt.create({ data: { userId: student.id, exerciseId: exercise.id, correct: p.correct } });
  }

  return student.id;
}

afterAll(async () => {
  await prisma.exerciseAttempt.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.exercise.deleteMany({ where: { id: { in: cleanupExerciseIds } } });
  await prisma.lesson.deleteMany({ where: { id: { in: cleanupLessonIds } } });
  await prisma.repertoireEntry.deleteMany({ where: { id: { in: cleanupEntryIds } } });
  await prisma.studentProfile.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.user.deleteMany({ where: { id: { in: cleanupUserIds } } });
  await prisma.piece.deleteMany({ where: { id: { in: cleanupPieceIds } } });
});

describe("computeAdaptiveDifficulty", () => {
  it("se queda en normal si no hay suficientes intentos todavia", async () => {
    const userId = await makeAttempts([
      { phase: "VISUAL_AGILITY", correct: true },
      { phase: "VISUAL_AGILITY", correct: true },
    ]);
    const result = await computeAdaptiveDifficulty(userId);
    expect(result.VISUAL_AGILITY).toBe("normal");
  });

  it("sube a dificil si el acierto historico es muy alto", async () => {
    const pattern = Array.from({ length: 10 }, (_, i) => ({ phase: "VISUAL_AGILITY", correct: i < 9 })); // 90%
    const userId = await makeAttempts(pattern);
    const result = await computeAdaptiveDifficulty(userId);
    expect(result.VISUAL_AGILITY).toBe("hard");
  });

  it("baja a facil si el acierto historico es bajo", async () => {
    const pattern = Array.from({ length: 10 }, (_, i) => ({ phase: "EAR_ACUITY", correct: i < 3 })); // 30%
    const userId = await makeAttempts(pattern);
    const result = await computeAdaptiveDifficulty(userId);
    expect(result.EAR_ACUITY).toBe("easy");
  });

  it("cada bloque se calcula de forma independiente", async () => {
    const pattern = [
      ...Array.from({ length: 10 }, (_, i) => ({ phase: "VISUAL_AGILITY", correct: i < 9 })), // hard
      ...Array.from({ length: 10 }, (_, i) => ({ phase: "NOTE_RUSH", correct: i < 3 })), // easy
    ];
    const userId = await makeAttempts(pattern);
    const result = await computeAdaptiveDifficulty(userId);
    expect(result.VISUAL_AGILITY).toBe("hard");
    expect(result.NOTE_RUSH).toBe("easy");
    expect(result.EAR_ACUITY).toBe("normal"); // sin datos
  });
});
