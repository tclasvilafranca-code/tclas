import { Router } from "express";
import bcrypt from "bcryptjs";
import { z } from "zod";
import { prisma } from "../prisma";
import { requireAuth, requireRole, AuthedRequest } from "../auth";
import { buildCurriculumForUser, computePhaseStats, computePracticeStats } from "../curriculum";
import { createRepertoireEntryWithLessons, bulkAssignRepertoire } from "../repertoire";
import { getThread, sendMessage, countUnread } from "../messages";
import { getWeeklyChallenges } from "../challenges";

const router = Router();
router.use(requireAuth, requireRole("TEACHER"));

function slugifyUsername(name: string): string {
  return name
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "")
    .slice(0, 16);
}

// PIN por defecto para cualquier acceso nuevo (alumno o profesor/a): sencillo
// de dar de viva voz o apuntar en un papel, y siempre obliga a cambiarlo en
// el primer login (ver mustChangePin) para que no quede como PIN definitivo.
const DEFAULT_PIN = "1234";

/** Busca un alumno por id, pero SOLO si pertenece a este profesor: evita que
 * un profesor pueda ver o modificar los alumnos de otro adivinando/copiando
 * un id (p.ej. desde la URL del panel de otro profesor). */
async function findOwnedStudent(studentUserId: string, teacherId: string) {
  return prisma.user.findFirst({
    where: { id: studentUserId, role: "STUDENT", studentProfile: { teacherId } },
    include: { studentProfile: true },
  });
}

router.get("/students", async (req: AuthedRequest, res) => {
  const students = await prisma.user.findMany({
    where: { role: "STUDENT", studentProfile: { teacherId: req.auth!.userId } },
    include: { studentProfile: true },
    orderBy: { name: "asc" },
  });

  const results = await Promise.all(
    students.map(async (s) => {
      const entries = await prisma.repertoireEntry.findMany({ where: { studentId: s.studentProfile!.id }, include: { lessons: true } });
      const totalLessons = entries.reduce((a, e) => a + e.lessons.length, 0);
      const lessonIds = entries.flatMap((e) => e.lessons.map((l) => l.id));
      const completedLessons = await prisma.progress.count({ where: { userId: s.id, status: "COMPLETED", lessonId: { in: lessonIds } } });
      const { last7Days } = await computePracticeStats(s.id, s.studentProfile!.id);
      const weeklyMinutes = last7Days.reduce((sum, d) => sum + d.minutes, 0);
      const unreadMessages = await countUnread(req.auth!.userId, s.id);
      const challenges = await getWeeklyChallenges(s.id);
      const challengesCompleted = challenges.filter((c) => c.completed).length;
      return {
        id: s.id,
        name: s.name,
        username: s.username,
        ageGroup: s.studentProfile?.ageGroup,
        xpTotal: s.studentProfile?.xpTotal ?? 0,
        streakCurrent: s.studentProfile?.streakCurrent ?? 0,
        lastActivityDate: s.studentProfile?.lastActivityDate ?? null,
        piecesAssigned: entries.length,
        completedLessons,
        totalLessons,
        weeklyMinutes,
        dailyGoalMinutes: s.studentProfile?.dailyGoalMinutes ?? 15,
        unreadMessages,
        challengesCompleted,
        challengesTotal: challenges.length,
        nextClassAt: s.studentProfile?.nextClassAt ?? null,
      };
    })
  );
  res.json(results);
});

const createStudentSchema = z.object({
  name: z.string().min(1),
  ageGroup: z.enum(["KIDS", "TEENS", "ADULTS"]),
  birthYear: z.number().int().optional(),
});

router.post("/students", async (req: AuthedRequest, res) => {
  const parsed = createStudentSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos", details: parsed.error.flatten() });

  const base = slugifyUsername(parsed.data.name) || "alumno";
  let username = base;
  let suffix = 0;
  while (await prisma.user.findUnique({ where: { username } })) {
    suffix += 1;
    username = `${base}${suffix}`;
  }
  const pinHash = await bcrypt.hash(DEFAULT_PIN, 10);

  const user = await prisma.user.create({
    data: {
      name: parsed.data.name,
      role: "STUDENT",
      username,
      pinHash,
      mustChangePin: true,
      studentProfile: {
        create: { ageGroup: parsed.data.ageGroup, birthYear: parsed.data.birthYear, teacherId: req.auth!.userId, onboarded: true },
      },
    },
    include: { studentProfile: true },
  });

  res.status(201).json({ id: user.id, name: user.name, username, pin: DEFAULT_PIN, ageGroup: user.studentProfile?.ageGroup });
});

router.get("/students/:id", async (req: AuthedRequest, res) => {
  const student = await findOwnedStudent(req.params.id, req.auth!.userId);
  if (!student?.studentProfile) return res.status(404).json({ error: "Alumno no encontrado" });

  const curriculum = await buildCurriculumForUser(student.id, student.studentProfile.id);

  const recentBadges = await prisma.userBadge.findMany({
    where: { userId: student.id },
    include: { badge: true },
    orderBy: { earnedAt: "desc" },
  });

  // Rendimiento por bloque: cuantas respuestas acierta el alumno en cada tipo
  // de bloque de la sesion (agilidad visual, agudeza auditiva, notas al vuelo,
  // practica de partitura), para que la profesora vea en que flaquea de un vistazo.
  const [phaseStats, practiceStats, challenges] = await Promise.all([
    computePhaseStats(student.id),
    computePracticeStats(student.id, student.studentProfile.id),
    getWeeklyChallenges(student.id),
  ]);

  res.json({
    id: student.id,
    name: student.name,
    username: student.username,
    profile: student.studentProfile,
    curriculum,
    badges: recentBadges.map((b) => ({ code: b.badge.code, name: b.badge.name, icon: b.badge.icon, earnedAt: b.earnedAt })),
    phaseStats,
    practiceStats,
    challenges,
  });
});

const teacherMessageSchema = z.object({ body: z.string().trim().min(1).max(2000) });

router.get("/students/:id/messages", async (req: AuthedRequest, res) => {
  const student = await findOwnedStudent(req.params.id, req.auth!.userId);
  if (!student) return res.status(404).json({ error: "Alumno no encontrado" });
  const messages = await getThread(req.auth!.userId, student.id);
  res.json({ messages });
});

router.post("/students/:id/messages", async (req: AuthedRequest, res) => {
  const parsed = teacherMessageSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "El mensaje no puede estar vacio" });

  const student = await findOwnedStudent(req.params.id, req.auth!.userId);
  if (!student) return res.status(404).json({ error: "Alumno no encontrado" });

  const message = await sendMessage(req.auth!.userId, student.id, parsed.data.body);
  res.status(201).json({ id: message.id, body: message.body, fromMe: true, createdAt: message.createdAt.toISOString() });
});

router.get("/pieces", async (req, res) => {
  const ageGroup = req.query.ageGroup as string | undefined;
  const pieces = await prisma.piece.findMany({
    where: ageGroup ? { ageGroup } : undefined,
    orderBy: [{ difficultyTier: "asc" }, { title: "asc" }],
  });
  res.json(
    pieces.map((p) => ({
      id: p.id,
      title: p.title,
      composer: p.composer,
      ageGroup: p.ageGroup,
      difficultyTier: p.difficultyTier,
      defaultWeeks: p.defaultWeeks,
      keySignature: p.keySignature,
      timeSignature: p.timeSignature,
      seasonalTag: p.seasonalTag,
      iconEmoji: p.iconEmoji,
    }))
  );
});

const nextClassSchema = z.object({ date: z.string().nullable() });

// Fecha de la proxima clase presencial: la pone la profesora a mano (no hay
// un sistema de reservas, solo un recordatorio simple para el alumno).
router.patch("/students/:id/next-class", async (req: AuthedRequest, res) => {
  const parsed = nextClassSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Fecha invalida" });

  const student = await findOwnedStudent(req.params.id, req.auth!.userId);
  if (!student?.studentProfile) return res.status(404).json({ error: "Alumno no encontrado" });

  await prisma.studentProfile.update({
    where: { id: student.studentProfile.id },
    data: { nextClassAt: parsed.data.date ? new Date(parsed.data.date) : null },
  });
  res.json({ ok: true });
});

const assignSchema = z.object({
  pieceId: z.string(),
  startDate: z.string(),
  durationWeeks: z.number().int().min(1).max(12).optional(),
  teacherNote: z.string().default(""),
});

router.post("/students/:id/repertoire", async (req: AuthedRequest, res) => {
  const parsed = assignSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos", details: parsed.error.flatten() });

  const student = await findOwnedStudent(req.params.id, req.auth!.userId);
  if (!student?.studentProfile) return res.status(404).json({ error: "Alumno no encontrado" });

  const piece = await prisma.piece.findUnique({ where: { id: parsed.data.pieceId } });
  if (!piece) return res.status(404).json({ error: "Pieza no encontrada" });

  const lastEntry = await prisma.repertoireEntry.findFirst({ where: { studentId: student.studentProfile.id }, orderBy: { orderIndex: "desc" } });
  const orderIndex = (lastEntry?.orderIndex ?? 0) + 1;

  const entry = await createRepertoireEntryWithLessons({
    studentProfileId: student.studentProfile.id,
    piece,
    orderIndex,
    startDate: new Date(parsed.data.startDate),
    durationWeeks: parsed.data.durationWeeks,
    teacherNote: parsed.data.teacherNote,
  });

  res.status(201).json(entry);
});

const bulkAssignSchema = z.object({
  startDate: z.string().optional(),
  items: z
    .array(
      z.object({
        pieceId: z.string(),
        durationWeeks: z.number().int().min(1).max(12).optional(),
        teacherNote: z.string().optional(),
      })
    )
    .min(1),
});

router.post("/students/:id/repertoire/bulk", async (req: AuthedRequest, res) => {
  const parsed = bulkAssignSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos", details: parsed.error.flatten() });

  const student = await findOwnedStudent(req.params.id, req.auth!.userId);
  if (!student?.studentProfile) return res.status(404).json({ error: "Alumno no encontrado" });

  const created = await bulkAssignRepertoire({
    studentProfileId: student.studentProfile.id,
    items: parsed.data.items,
    startDate: parsed.data.startDate ? new Date(parsed.data.startDate) : undefined,
  });

  res.status(201).json(created);
});

const duplicateSchema = z.object({
  fromStudentId: z.string(),
  startDate: z.string().optional(),
});

router.post("/students/:id/repertoire/duplicate", async (req: AuthedRequest, res) => {
  const parsed = duplicateSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos", details: parsed.error.flatten() });

  const student = await findOwnedStudent(req.params.id, req.auth!.userId);
  if (!student?.studentProfile) return res.status(404).json({ error: "Alumno no encontrado" });

  // El alumno de origen tambien debe ser tuyo: si no, no se puede copiar su repertorio.
  const source = await findOwnedStudent(parsed.data.fromStudentId, req.auth!.userId);
  if (!source?.studentProfile) return res.status(404).json({ error: "Alumno de origen no encontrado" });

  const sourceEntries = await prisma.repertoireEntry.findMany({
    where: { studentId: source.studentProfile.id },
    orderBy: { orderIndex: "asc" },
  });
  if (sourceEntries.length === 0) return res.status(400).json({ error: "Ese alumno todavia no tiene repertorio para copiar" });

  const created = await bulkAssignRepertoire({
    studentProfileId: student.studentProfile.id,
    items: sourceEntries.map((e) => ({ pieceId: e.pieceId, durationWeeks: e.durationWeeks, teacherNote: e.teacherNote })),
    startDate: parsed.data.startDate ? new Date(parsed.data.startDate) : undefined,
  });

  res.status(201).json(created);
});

router.delete("/students/:id/repertoire/:entryId", async (req: AuthedRequest, res) => {
  const student = await findOwnedStudent(req.params.id, req.auth!.userId);
  if (!student?.studentProfile) return res.status(404).json({ error: "Alumno no encontrado" });

  const entry = await prisma.repertoireEntry.findFirst({
    where: { id: req.params.entryId, studentId: student.studentProfile.id },
    include: { lessons: true },
  });
  if (!entry) return res.status(404).json({ error: "Asignacion no encontrada" });

  const lessonIds = entry.lessons.map((l) => l.id);
  const exercises = await prisma.exercise.findMany({ where: { lessonId: { in: lessonIds } } });
  const exerciseIds = exercises.map((e) => e.id);

  await prisma.exerciseAttempt.deleteMany({ where: { exerciseId: { in: exerciseIds } } });
  await prisma.progress.deleteMany({ where: { lessonId: { in: lessonIds } } });
  await prisma.exercise.deleteMany({ where: { lessonId: { in: lessonIds } } });
  await prisma.lesson.deleteMany({ where: { repertoireEntryId: entry.id } });
  await prisma.repertoireEntry.delete({ where: { id: entry.id } });

  res.status(204).send();
});

export default router;
