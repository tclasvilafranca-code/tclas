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
  role: z.enum(["STUDENT", "TEACHER"]).default("STUDENT"),
});

router.post("/register", async (req, res) => {
  const parsed = registerSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: "Datos invalidos", details: parsed.error.flatten() });
  }
  const { email, password, name, role } = parsed.data;

  const existing = await prisma.user.findUnique({ where: { email } });
  if (existing) {
    return res.status(409).json({ error: "Ya existe una cuenta con ese email" });
  }

  const passwordHash = await bcrypt.hash(password, 10);
  const user = await prisma.user.create({
    data: {
      email,
      passwordHash,
      name,
      role,
      studentProfile:
        role === "STUDENT"
          ? { create: { ageGroup: "ADULTS" } }
          : undefined,
    },
    include: { studentProfile: true },
  });

  const token = signToken({ userId: user.id, role: role as "STUDENT" | "TEACHER" });
  res.status(201).json({
    token,
    user: { id: user.id, email: user.email, name: user.name, role: user.role },
  });
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
  if (!user) return res.status(401).json({ error: "Credenciales incorrectas" });
  const valid = await bcrypt.compare(password, user.passwordHash);
  if (!valid) return res.status(401).json({ error: "Credenciales incorrectas" });

  const token = signToken({ userId: user.id, role: user.role as "STUDENT" | "TEACHER" });
  res.json({ token, user: { id: user.id, email: user.email, name: user.name, role: user.role } });
});

router.get("/me", requireAuth, async (req: AuthedRequest, res) => {
  const user = await prisma.user.findUnique({
    where: { id: req.auth!.userId },
    include: { studentProfile: { include: { track: true } } },
  });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });

  let studentProfile: typeof user.studentProfile = user.studentProfile;
  if (studentProfile) {
    const { track, ...rest } = studentProfile;
    const recomputed = await recomputeHearts(rest);
    studentProfile = { ...recomputed, track };
  }

  res.json({
    id: user.id,
    email: user.email,
    name: user.name,
    role: user.role,
    studentProfile,
  });
});

export default router;
