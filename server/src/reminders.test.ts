import { describe, it, expect, afterAll, vi } from "vitest";
import { prisma } from "./prisma";

// Simula el envio real (que depende de red y VAPID) para poder probar la
// logica de seleccion de candidatos sin depender de infraestructura externa.
vi.mock("./push", () => ({
  sendPush: vi.fn().mockResolvedValue(true),
  isPushConfigured: () => true,
  getVapidPublicKey: () => "test-key",
}));

import { runReminderSweep } from "./reminders";
import { sendPush } from "./push";

const cleanupUserIds: string[] = [];

async function makeStudent(opts: { lastActivityDate: Date | null; lastReminderSentAt: Date | null; withSubscription: boolean }) {
  const teacher = await prisma.user.create({
    data: { name: "Test Teacher Reminders", email: `test-teacher-rem-${Date.now()}-${Math.random().toString(36).slice(2)}@example.com`, passwordHash: "x", role: "TEACHER" },
  });
  cleanupUserIds.push(teacher.id);
  const student = await prisma.user.create({
    data: {
      name: "Test Student Reminders",
      username: `test-student-rem-${Date.now()}-${Math.random().toString(36).slice(2)}`,
      pinHash: "x",
      role: "STUDENT",
      studentProfile: {
        create: { ageGroup: "KIDS", teacherId: teacher.id, onboarded: true, lastActivityDate: opts.lastActivityDate, lastReminderSentAt: opts.lastReminderSentAt },
      },
    },
    include: { studentProfile: true },
  });
  cleanupUserIds.push(student.id);
  if (opts.withSubscription) {
    await prisma.pushSubscription.create({
      data: { userId: student.id, endpoint: `https://fcm.googleapis.com/fcm/send/test-${student.id}`, p256dh: "x", auth: "x" },
    });
  }
  return student.studentProfile!.id;
}

afterAll(async () => {
  await prisma.pushSubscription.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.studentProfile.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.user.deleteMany({ where: { id: { in: cleanupUserIds } } });
});

describe("runReminderSweep", () => {
  it("solo manda a alumnos con suscripcion que no han practicado hoy ni recibido ya un aviso hoy", async () => {
    const yesterday = new Date(Date.now() - 26 * 60 * 60 * 1000);
    const today = new Date();

    const dueId = await makeStudent({ lastActivityDate: yesterday, lastReminderSentAt: null, withSubscription: true });
    const alreadyPracticedId = await makeStudent({ lastActivityDate: today, lastReminderSentAt: null, withSubscription: true });
    const alreadyRemindedId = await makeStudent({ lastActivityDate: yesterday, lastReminderSentAt: today, withSubscription: true });
    const noSubscriptionId = await makeStudent({ lastActivityDate: yesterday, lastReminderSentAt: null, withSubscription: false });

    const callsBefore = (sendPush as any).mock.calls.length;
    await runReminderSweep();
    const callsAfter = (sendPush as any).mock.calls.length;
    expect(callsAfter - callsBefore).toBe(1); // solo el elegible

    const due = await prisma.studentProfile.findUnique({ where: { id: dueId } });
    expect(due?.lastReminderSentAt).not.toBeNull();

    const alreadyPracticed = await prisma.studentProfile.findUnique({ where: { id: alreadyPracticedId } });
    expect(alreadyPracticed?.lastReminderSentAt).toBeNull();

    const alreadyReminded = await prisma.studentProfile.findUnique({ where: { id: alreadyRemindedId } });
    expect(alreadyReminded?.lastReminderSentAt?.getTime()).toBe(today.getTime());

    const noSubscription = await prisma.studentProfile.findUnique({ where: { id: noSubscriptionId } });
    expect(noSubscription?.lastReminderSentAt).toBeNull();
  });
});
