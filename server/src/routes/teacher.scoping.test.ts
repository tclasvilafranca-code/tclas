import { describe, it, expect, afterAll } from "vitest";
import request from "supertest";
import { app } from "../app";
import { prisma } from "../prisma";
import { signToken } from "../auth";

// Un profesor NUNCA debe poder ver ni tocar a los alumnos de otro profesor,
// aunque adivine o copie el id (p.ej. desde la URL de otro panel). Crea dos
// profesores independientes, cada uno con su propio alumno, de usar y tirar.
const cleanupUserIds: string[] = [];

async function makeTeacherWithStudent() {
  const teacher = await prisma.user.create({
    data: { name: "Test Teacher Scoping", email: `test-teacher-sc-${Date.now()}-${Math.random().toString(36).slice(2)}@example.com`, passwordHash: "x", role: "TEACHER" },
  });
  cleanupUserIds.push(teacher.id);
  const student = await prisma.user.create({
    data: {
      name: "Test Student Scoping",
      username: `test-student-sc-${Date.now()}-${Math.random().toString(36).slice(2)}`,
      pinHash: "x",
      role: "STUDENT",
      studentProfile: { create: { ageGroup: "KIDS", teacherId: teacher.id, onboarded: true } },
    },
    include: { studentProfile: true },
  });
  cleanupUserIds.push(student.id);
  const teacherToken = signToken({ userId: teacher.id, role: "TEACHER" });
  return { teacherToken, studentId: student.id };
}

afterAll(async () => {
  await prisma.studentProfile.deleteMany({ where: { userId: { in: cleanupUserIds } } });
  await prisma.user.deleteMany({ where: { id: { in: cleanupUserIds } } });
});

describe("Aislamiento entre profesores", () => {
  it("un profesor no puede ver la ficha de un alumno de otro profesor", async () => {
    const { studentId } = await makeTeacherWithStudent();
    const { teacherToken: otherTeacherToken } = await makeTeacherWithStudent();

    const res = await request(app).get(`/api/teacher/students/${studentId}`).set("Authorization", `Bearer ${otherTeacherToken}`);
    expect(res.status).toBe(404);
  });

  it("un profesor si puede ver la ficha de su propio alumno", async () => {
    const { teacherToken, studentId } = await makeTeacherWithStudent();
    const res = await request(app).get(`/api/teacher/students/${studentId}`).set("Authorization", `Bearer ${teacherToken}`);
    expect(res.status).toBe(200);
  });

  it("un profesor no puede asignar repertorio al alumno de otro profesor", async () => {
    const { studentId } = await makeTeacherWithStudent();
    const { teacherToken: otherTeacherToken } = await makeTeacherWithStudent();

    const res = await request(app)
      .post(`/api/teacher/students/${studentId}/repertoire`)
      .set("Authorization", `Bearer ${otherTeacherToken}`)
      .send({ pieceId: "does-not-matter", startDate: new Date().toISOString() });
    expect(res.status).toBe(404);
  });

  it("un profesor no puede duplicar repertorio usando el alumno de otro profesor como origen", async () => {
    const { studentId: victimStudentId } = await makeTeacherWithStudent();
    const { teacherToken: attackerToken, studentId: attackerStudentId } = await makeTeacherWithStudent();

    const res = await request(app)
      .post(`/api/teacher/students/${attackerStudentId}/repertoire/duplicate`)
      .set("Authorization", `Bearer ${attackerToken}`)
      .send({ fromStudentId: victimStudentId });
    expect(res.status).toBe(404);
  });
});
