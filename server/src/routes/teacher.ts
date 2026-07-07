import { Router } from "express";
import { z } from "zod";
import { prisma } from "../prisma";
import { requireAuth, requireRole, AuthedRequest } from "../auth";
import { buildCurriculumForUser } from "../curriculum";

const router = Router();
router.use(requireAuth, requireRole("TEACHER"));

router.get("/students", async (_req, res) => {
  const students = await prisma.user.findMany({
    where: { role: "STUDENT" },
    include: { studentProfile: { include: { track: true } } },
    orderBy: { name: "asc" },
  });

  const results = await Promise.all(
    students.map(async (s) => {
      const completedCount = await prisma.progress.count({ where: { userId: s.id, status: "COMPLETED" } });
      const totalLessons = s.studentProfile?.trackId
        ? await prisma.lesson.count({ where: { unit: { level: { trackId: s.studentProfile.trackId } } } })
        : 0;
      return {
        id: s.id,
        name: s.name,
        email: s.email,
        ageGroup: s.studentProfile?.ageGroup,
        trackName: s.studentProfile?.track?.name ?? null,
        xpTotal: s.studentProfile?.xpTotal ?? 0,
        streakCurrent: s.studentProfile?.streakCurrent ?? 0,
        lastActivityDate: s.studentProfile?.lastActivityDate ?? null,
        onboarded: s.studentProfile?.onboarded ?? false,
        completedLessons: completedCount,
        totalLessons,
      };
    })
  );
  res.json(results);
});

router.get("/students/:id", async (req, res) => {
  const student = await prisma.user.findUnique({
    where: { id: req.params.id },
    include: { studentProfile: { include: { track: true } } },
  });
  if (!student || student.role !== "STUDENT") return res.status(404).json({ error: "Alumno no encontrado" });

  const curriculum = student.studentProfile?.trackId
    ? await buildCurriculumForUser(student.id, student.studentProfile.trackId)
    : null;

  const assignments = await prisma.assignment.findMany({
    where: { studentId: student.id },
    include: { lesson: true },
    orderBy: { classDate: "desc" },
  });

  const recentBadges = await prisma.userBadge.findMany({
    where: { userId: student.id },
    include: { badge: true },
    orderBy: { earnedAt: "desc" },
  });

  res.json({
    id: student.id,
    name: student.name,
    email: student.email,
    profile: student.studentProfile,
    curriculum,
    assignments,
    badges: recentBadges.map((b) => ({ code: b.badge.code, name: b.badge.name, icon: b.badge.icon, earnedAt: b.earnedAt })),
  });
});

const assignmentSchema = z.object({
  studentId: z.string(),
  lessonId: z.string().optional(),
  classDate: z.string(),
  note: z.string().default(""),
});

router.post("/assignments", async (req: AuthedRequest, res) => {
  const parsed = assignmentSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos", details: parsed.error.flatten() });

  const assignment = await prisma.assignment.create({
    data: {
      teacherId: req.auth!.userId,
      studentId: parsed.data.studentId,
      lessonId: parsed.data.lessonId,
      classDate: new Date(parsed.data.classDate),
      note: parsed.data.note,
    },
    include: { lesson: true },
  });
  res.status(201).json(assignment);
});

router.get("/assignments", async (req, res) => {
  const studentId = req.query.studentId as string | undefined;
  const assignments = await prisma.assignment.findMany({
    where: studentId ? { studentId } : undefined,
    include: { lesson: true, student: true },
    orderBy: { classDate: "desc" },
  });
  res.json(assignments);
});

const updateAssignmentSchema = z.object({ status: z.enum(["PENDING", "DONE"]) });

router.patch("/assignments/:id", async (req, res) => {
  const parsed = updateAssignmentSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos" });
  const assignment = await prisma.assignment.update({
    where: { id: req.params.id },
    data: { status: parsed.data.status },
  });
  res.json(assignment);
});

export default router;
