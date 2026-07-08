import { describe, it, expect, afterAll } from "vitest";
import request from "supertest";
import bcrypt from "bcryptjs";
import { app } from "../app";
import { prisma } from "../prisma";
import { signToken } from "../auth";

const cleanupUserIds: string[] = [];

async function makeTeacher(password: string) {
  const passwordHash = await bcrypt.hash(password, 10);
  const user = await prisma.user.create({
    data: { name: "Test Teacher Pwd", email: `test-teacher-pwd-${Date.now()}-${Math.random().toString(36).slice(2)}@example.com`, passwordHash, role: "TEACHER" },
  });
  cleanupUserIds.push(user.id);
  return { user, token: signToken({ userId: user.id, role: "TEACHER" }) };
}

afterAll(async () => {
  await prisma.user.deleteMany({ where: { id: { in: cleanupUserIds } } });
});

describe("POST /api/auth/change-password", () => {
  it("rechaza si la contrasena actual es incorrecta", async () => {
    const { token } = await makeTeacher("correcta123");
    const res = await request(app)
      .post("/api/auth/change-password")
      .set("Authorization", `Bearer ${token}`)
      .send({ currentPassword: "incorrecta", newPassword: "nuevacontrasena" });
    expect(res.status).toBe(401);
  });

  it("cambia la contrasena y permite iniciar sesion con la nueva", async () => {
    const { user, token } = await makeTeacher("correcta123");
    const res = await request(app)
      .post("/api/auth/change-password")
      .set("Authorization", `Bearer ${token}`)
      .send({ currentPassword: "correcta123", newPassword: "nuevacontrasena" });
    expect(res.status).toBe(200);

    const loginRes = await request(app).post("/api/auth/login").send({ email: user.email, password: "nuevacontrasena" });
    expect(loginRes.status).toBe(200);

    const oldLoginRes = await request(app).post("/api/auth/login").send({ email: user.email, password: "correcta123" });
    expect(oldLoginRes.status).toBe(401);
  });
});
