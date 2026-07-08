import { describe, it, expect, afterAll } from "vitest";
import request from "supertest";
import { app } from "../app";
import { prisma } from "../prisma";
import { signToken } from "../auth";

const cleanupUserIds: string[] = [];

async function makeStudent() {
  const teacher = await prisma.user.create({
    data: { name: "Test Teacher Push", email: `test-teacher-push-${Date.now()}-${Math.random().toString(36).slice(2)}@example.com`, passwordHash: "x", role: "TEACHER" },
  });
  cleanupUserIds.push(teacher.id);
  const student = await prisma.user.create({
    data: {
      name: "Test Student Push",
      username: `test-student-push-${Date.now()}-${Math.random().toString(36).slice(2)}`,
      pinHash: "x",
      role: "STUDENT",
      studentProfile: { create: { ageGroup: "KIDS", teacherId: teacher.id, onboarded: true } },
    },
  });
  cleanupUserIds.push(student.id);
  return signToken({ userId: student.id, role: "STUDENT" });
}

afterAll(async () => {
  await prisma.pushSubscription.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.studentProfile.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.user.deleteMany({ where: { id: { in: cleanupUserIds } } });
});

describe("Push subscriptions", () => {
  it("GET /vapid-public-key no requiere autenticacion", async () => {
    const res = await request(app).get("/api/push/vapid-public-key");
    expect(res.status).toBe(200);
    expect(typeof res.body.configured).toBe("boolean");
  });

  it("suscribe, refleja el estado, y desuscribe correctamente", async () => {
    const token = await makeStudent();
    const endpoint = `https://fcm.googleapis.com/fcm/send/test-${Date.now()}`;

    const before = await request(app).get("/api/push/status").set("Authorization", `Bearer ${token}`);
    expect(before.body.subscribed).toBe(false);

    const sub = await request(app)
      .post("/api/push/subscribe")
      .set("Authorization", `Bearer ${token}`)
      .send({ endpoint, keys: { p256dh: "test-p256dh", auth: "test-auth" } });
    expect(sub.status).toBe(201);

    const after = await request(app).get("/api/push/status").set("Authorization", `Bearer ${token}`);
    expect(after.body.subscribed).toBe(true);

    const unsub = await request(app).post("/api/push/unsubscribe").set("Authorization", `Bearer ${token}`).send({ endpoint });
    expect(unsub.status).toBe(200);

    const afterUnsub = await request(app).get("/api/push/status").set("Authorization", `Bearer ${token}`);
    expect(afterUnsub.body.subscribed).toBe(false);
  });
});
