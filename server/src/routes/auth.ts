import { Router } from "express";
import bcrypt from "bcryptjs";
import { z } from "zod";
import { prisma } from "../prisma";
import { signToken, requireAuth, AuthedRequest } from "../auth";
import { recomputeHearts } from "../gamification";

const router = Router();

const registerSchema = z.object({
  email: z.string().email(),
  password: z.string().min(6),
  name: z.string().min(1),
});

// Solo para profesores: los alumnos no se autoregistran, su cuenta la crea el/la profesor/a
// desde el panel (ver /teacher/students) y reciben un usuario + PIN para entrar.
router.post("/register", async (req, res) => {
  const parsed = registerSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: "Datos invalidos", details: parsed.error.flatten() });
  }
  const { email, password, name } = parsed.data;

  const existing = await prisma.user.findUnique({ where: { email } });
  if (existing) {
    return res.status(409).json({ error: "Ya existe una cuenta con ese email" });
  }

  const passwordHash = await bcrypt.hash(password, 10);
  const user = await prisma.user.create({
    data: { email, passwordHash, name, role: "TEACHER" },
  });

  const token = signToken({ userId: user.id, role: "TEACHER" });
  res.status(201).json({ token, user: { id: user.id, email: user.email, name: user.name, role: user.role } });
});

const loginSchema = z.object({
  email: z.string().email(),
  password: z.string(),
});

router.post("/login", async (req, res) => {
  const parsed = loginSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: "Datos invalidos" });
  }
  const { email, password } = parsed.data;
  const user = await prisma.user.findUnique({ where: { email } });
  if (!user || !user.passwordHash) return res.status(401).json({ error: "Credenciales incorrectas" });
  const valid = await bcrypt.compare(password, user.passwordHash);
  if (!valid) return res.status(401).json({ error: "Credenciales incorrectas" });

  const token = signToken({ userId: user.id, role: user.role as "STUDENT" | "TEACHER" });
  res.json({ token, user: { id: user.id, email: user.email, name: user.name, role: user.role } });
});

const studentLoginSchema = z.object({
  username: z.string().min(1),
  pin: z.string().min(1),
});

router.post("/student-login", async (req, res) => {
  const parsed = studentLoginSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos" });
  const { username, pin } = parsed.data;

  const user = await prisma.user.findUnique({ where: { username: username.toLowerCase() } });
  if (!user || !user.pinHash) return res.status(401).json({ error: "Usuario o PIN incorrectos" });
  const valid = await bcrypt.compare(pin, user.pinHash);
  if (!valid) return res.status(401).json({ error: "Usuario o PIN incorrectos" });

  const token = signToken({ userId: user.id, role: "STUDENT" });
  res.json({ token, user: { id: user.id, name: user.name, role: user.role, username: user.username } });
});

router.get("/me", requireAuth, async (req: AuthedRequest, res) => {
  const user = await prisma.user.findUnique({
    where: { id: req.auth!.userId },
    include: { studentProfile: true },
  });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });

  let studentProfile = user.studentProfile;
  if (studentProfile) {
    studentProfile = await recomputeHearts(studentProfile);
  }

  res.json({
    id: user.id,
    email: user.email,
    username: user.username,
    name: user.name,
    role: user.role,
    studentProfile,
  });
});

export default router;
