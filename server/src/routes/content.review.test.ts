import { describe, it, expect, afterAll } from "vitest";
import request from "supertest";
import { app } from "../app";
import { prisma } from "../prisma";
import { signToken } from "../auth";

// Verifica el ciclo de repaso espaciado de extremo a extremo: completar una
// pieza entera programa un primer repaso, y repetir la leccion despues
// (repaso) alarga el intervalo si va bien. Fixtures de usar-y-tirar.
const cleanupUserIds: string[] = [];
const cleanupPieceIds: string[] = [];

async function makeSinglePieceStudent() {
  const teacher = await prisma.user.create({
    data: { name: "Test Teacher Review", email: `test-teacher-rv-${Date.now()}-${Math.random().toString(36).slice(2)}@example.com`, passwordHash: "x", role: "TEACHER" },
  });
  cleanupUserIds.push(teacher.id);

  const piece = await prisma.piece.create({
    data: {
      title: `Test Review Piece ${Date.now()}-${Math.random().toString(36).slice(2)}`,
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
      name: "Test Student Review",
      username: `test-student-rv-${Date.now()}-${Math.random().toString(36).slice(2)}`,
      pinHash: "x",
      role: "STUDENT",
      studentProfile: { create: { ageGroup: "KIDS", teacherId: teacher.id, onboarded: true, heartsCurrent: 5, heartsMax: 5 } },
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
  return { token, lessonId: lesson.id, entryId: entry.id };
}

afterAll(async () => {
  const entries = await prisma.repertoireEntry.findMany({ where: { student: { userId: { in: cleanupUserIds } } }, select: { id: true } });
  const entryIds = entries.map((e) => e.id);
  const lessons = await prisma.lesson.findMany({ where: { repertoireEntryId: { in: entryIds } }, select: { id: true } });
  const lessonIds = lessons.map((l) => l.id);
  const exercises = await prisma.exercise.findMany({ where: { lessonId: { in: lessonIds } }, select: { id: true } });
  const exerciseIds = exercises.map((e) => e.id);

  await prisma.exerciseAttempt.deleteMany({ where: { OR: [{ userId: { in: cleanupUserIds } }, { exerciseId: { in: exerciseIds } }] } });
  await prisma.progress.deleteMany({ where: { OR: [{ userId: { in: cleanupUserIds } }, { lessonId: { in: lessonIds } }] } });
  await prisma.xPEvent.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.userBadge.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.exercise.deleteMany({ where: { id: { in: exerciseIds } } });
  await prisma.lesson.deleteMany({ where: { id: { in: lessonIds } } });
  await prisma.repertoireEntry.deleteMany({ where: { id: { in: entryIds } } });
  await prisma.studentProfile.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.user.deleteMany({ where: { id: { in: cleanupUserIds } } });
  await prisma.piece.deleteMany({ where: { id: { in: cleanupPieceIds } } });
});

describe("Repaso espaciado", () => {
  it("completar la ultima leccion de una pieza programa el primer repaso a +3 dias", async () => {
    const { token, lessonId, entryId } = await makeSinglePieceStudent();

    const res = await request(app)
      .post(`/api/lessons/${lessonId}/complete`)
      .set("Authorization", `Bearer ${token}`)
      .send({ correctCount: 1, totalCount: 1 });
    expect(res.status).toBe(200);
    expect(res.body.isReview).toBe(false);

    const entry = await prisma.repertoireEntry.findUnique({ where: { id: entryId } });
    expect(entry?.status).toBe("COMPLETED");
    expect(entry?.reviewStage).toBe(0);
    const daysUntilReview = ((entry?.nextReviewAt?.getTime() ?? 0) - Date.now()) / 86400000;
    expect(daysUntilReview).toBeGreaterThan(2.9);
    expect(daysUntilReview).toBeLessThan(3.1);
  });

  it("aparece en /reviews/due cuando el repaso ya ha llegado, y repetirla con exito alarga el intervalo", async () => {
    const { token, lessonId, entryId } = await makeSinglePieceStudent();
    await request(app).post(`/api/lessons/${lessonId}/complete`).set("Authorization", `Bearer ${token}`).send({ correctCount: 1, totalCount: 1 });

    // Simula que ya ha pasado el tiempo suficiente para que toque repasar.
    await prisma.repertoireEntry.update({ where: { id: entryId }, data: { nextReviewAt: new Date(Date.now() - 1000) } });

    const dueRes = await request(app).get("/api/reviews/due").set("Authorization", `Bearer ${token}`);
    expect(dueRes.status).toBe(200);
    expect(dueRes.body.due.some((d: any) => d.entryId === entryId)).toBe(true);

    const completeRes = await request(app)
      .post(`/api/lessons/${lessonId}/complete`)
      .set("Authorization", `Bearer ${token}`)
      .send({ correctCount: 1, totalCount: 1 });
    expect(completeRes.body.isReview).toBe(true);
    expect(completeRes.body.xpAwarded).toBe(5);

    const entry = await prisma.repertoireEntry.findUnique({ where: { id: entryId } });
    expect(entry?.reviewStage).toBe(1);
    const daysUntilReview = ((entry?.nextReviewAt?.getTime() ?? 0) - Date.now()) / 86400000;
    expect(daysUntilReview).toBeGreaterThan(6.9); // stage 1 -> siguiente intervalo es de 7 dias
    expect(daysUntilReview).toBeLessThan(7.1);
  });
});
