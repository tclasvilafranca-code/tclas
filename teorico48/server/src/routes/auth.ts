import { Router } from "express";
import bcrypt from "bcryptjs";
import { z } from "zod";
import { PrismaClient } from "@prisma/client";
import { signToken, requireAuth, AuthedRequest } from "../middleware/auth";
import { levelForXp } from "../gamification";

const prisma = new PrismaClient();
export const authRouter = Router();

const credentialsSchema = z.object({
  email: z.string().email(),
  password: z.string().min(6, "La contraseña debe tener al menos 6 caracteres"),
});

authRouter.post("/register", async (req, res) => {
  const parsed = credentialsSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.issues[0].message });
  }
  const { email, password } = parsed.data;

  const existing = await prisma.user.findUnique({ where: { email } });
  if (existing) {
    return res.status(409).json({ error: "Ya existe una cuenta con ese email" });
  }

  const passwordHash = await bcrypt.hash(password, 10);
  const user = await prisma.user.create({ data: { email, passwordHash } });

  res.status(201).json({ token: signToken(user.id), user: toPublicUser(user) });
});

authRouter.post("/login", async (req, res) => {
  const parsed = credentialsSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.issues[0].message });
  }
  const { email, password } = parsed.data;

  const user = await prisma.user.findUnique({ where: { email } });
  if (!user) return res.status(401).json({ error: "Email o contraseña incorrectos" });

  const valid = await bcrypt.compare(password, user.passwordHash);
  if (!valid) return res.status(401).json({ error: "Email o contraseña incorrectos" });

  res.json({ token: signToken(user.id), user: toPublicUser(user) });
});

authRouter.get("/me", requireAuth, async (req: AuthedRequest, res) => {
  const user = await prisma.user.findUnique({ where: { id: req.userId } });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });
  res.json({ user: toPublicUser(user) });
});

const examDateSchema = z.object({
  examDate: z.string().datetime().nullable(),
});

authRouter.put("/me/exam-date", requireAuth, async (req: AuthedRequest, res) => {
  const parsed = examDateSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.issues[0].message });
  }
  const user = await prisma.user.update({
    where: { id: req.userId },
    data: { examDate: parsed.data.examDate ? new Date(parsed.data.examDate) : null },
  });
  res.json({ user: toPublicUser(user) });
});

function toPublicUser(user: {
  id: string;
  email: string;
  examDate: Date | null;
  isPremium: boolean;
  xp: number;
  currentStreak: number;
  longestStreak: number;
}) {
  return {
    id: user.id,
    email: user.email,
    examDate: user.examDate,
    isPremium: user.isPremium,
    xp: user.xp,
    level: levelForXp(user.xp),
    currentStreak: user.currentStreak,
    longestStreak: user.longestStreak,
  };
}
