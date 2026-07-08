import { describe, it, expect, afterAll } from "vitest";
import request from "supertest";
import { app } from "../app";
import { prisma } from "../prisma";
import { signToken } from "../auth";

// Integracion de extremo a extremo contra la base de datos local real: crea su
// propio profesor/alumno/pieza/leccion de usar-y-tirar, y lo borra todo al final.
const cleanupUserIds: string[] = [];
const cleanupPieceIds: string[] = [];

async function makeStudentWithLesson(opts: { heartsCurrent: number }) {
  const teacher = await prisma.user.create({
    data: { name: "Test Teacher", email: `test-teacher-${Date.now()}-${Math.random().toString(36).slice(2)}@example.com`, passwordHash: "x", role: "TEACHER" },
  });
  cleanupUserIds.push(teacher.id);

  const piece = await prisma.piece.create({
    data: {
      title: `Test Piece ${Date.now()}-${Math.random().toString(36).slice(2)}`,
      ageGroup: "KIDS",
      difficultyTier: 1,
      keySignature: "Do Mayor",
      timeSignature: "4/4",
      content: JSON.stringify({ clef: "treble", melody: ["C4", "D4"], melodyRhythm: [1, 1], featuredNotes: ["C4", "D4"] }),
    },
  });
  cleanupPieceIds.push(piece.id);

  const student = await prisma.user.create({
    data: {
      name: "Test Student",
      username: `test-student-${Date.now()}-${Math.random().toString(36).slice(2)}`,
      pinHash: "x",
      role: "STUDENT",
      studentProfile: {
        create: { ageGroup: "KIDS", teacherId: teacher.id, onboarded: true, heartsCurrent: opts.heartsCurrent, heartsMax: 5 },
      },
    },
    include: { studentProfile: true },
  });
  cleanupUserIds.push(student.id);

  const entry = await prisma.repertoireEntry.create({
    data: { studentId: student.studentProfile!.id, pieceId: piece.id, orderIndex: 1, startDate: new Date(), durationWeeks: 1, status: "ACTIVE" },
  });

  const lesson = await prisma.lesson.create({
    data: { repertoireEntryId: entry.id, weekIndex: 1, title: piece.title, description: "test", xpReward: 15 },
  });

  await prisma.exercise.create({
    data: {
      lessonId: lesson.id,
      index: 1,
      type: "NOTE_NAME",
      phase: "VISUAL_AGILITY",
      prompt: "test",
      data: JSON.stringify({ clef: "treble", note: "C4", options: ["Do", "Re"], correctAnswer: "Do" }),
      explanation: "test",
    },
  });

  const token = signToken({ userId: student.id, role: "STUDENT" });
  return { token, lessonId: lesson.id };
}

afterAll(async () => {
  const entries = await prisma.repertoireEntry.findMany({
    where: { student: { userId: { in: cleanupUserIds } } },
    select: { id: true },
  });
  const entryIds = entries.map((e) => e.id);
  const lessons = await prisma.lesson.findMany({ where: { repertoireEntryId: { in: entryIds } }, select: { id: true } });
  const lessonIds = lessons.map((l) => l.id);
  const exercises = await prisma.exercise.findMany({ where: { lessonId: { in: lessonIds } }, select: { id: true } });
  const exerciseIds = exercises.map((e) => e.id);

  await prisma.exerciseAttempt.deleteMany({ where: { OR: [{ userId: { in: cleanupUserIds } }, { exerciseId: { in: exerciseIds } }] } });
  await prisma.progress.deleteMany({ where: { OR: [{ userId: { in: cleanupUserIds } }, { lessonId: { in: lessonIds } }] } });
  await prisma.exercise.deleteMany({ where: { id: { in: exerciseIds } } });
  await prisma.lesson.deleteMany({ where: { id: { in: lessonIds } } });
  await prisma.repertoireEntry.deleteMany({ where: { id: { in: entryIds } } });
  await prisma.studentProfile.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.user.deleteMany({ where: { id: { in: cleanupUserIds } } });
  await prisma.piece.deleteMany({ where: { id: { in: cleanupPieceIds } } });
});

describe("GET /api/lessons/:id — bloqueo por corazones", () => {
  it("devuelve 403 NO_HEARTS si el alumno esta a 0 corazones y la leccion aun no esta hecha", async () => {
    const { token, lessonId } = await makeStudentWithLesson({ heartsCurrent: 0 });
    const res = await request(app).get(`/api/lessons/${lessonId}`).set("Authorization", `Bearer ${token}`);
    expect(res.status).toBe(403);
    expect(res.body.code).toBe("NO_HEARTS");
  });

  it("deja entrar con normalidad si hay corazones", async () => {
    const { token, lessonId } = await makeStudentWithLesson({ heartsCurrent: 3 });
    const res = await request(app).get(`/api/lessons/${lessonId}`).set("Authorization", `Bearer ${token}`);
    expect(res.status).toBe(200);
    expect(res.body.exercises.length).toBeGreaterThan(0);
  });
});
