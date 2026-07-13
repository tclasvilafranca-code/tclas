import { Router } from "express";
import bcrypt from "bcryptjs";
import { randomBytes, createHash } from "crypto";
import { z } from "zod";
import { Prisma, PrismaClient } from "@prisma/client";
import { signToken, requireAuth, AuthedRequest } from "../middleware/auth";
import { levelForXp } from "../gamification";
import { sendEmail } from "../mailer";
import { asyncHandler } from "../lib/asyncHandler";
import { authLimiter, forgotPasswordLimiter } from "../lib/rateLimit";

const prisma = new PrismaClient();
export const authRouter = Router();

const CLIENT_URL = process.env.CLIENT_URL || "http://localhost:5174";
const RESET_TOKEN_TTL_MS = 60 * 60 * 1000; // 1 hora

const credentialsSchema = z.object({
  email: z.string().email(),
  password: z.string().min(6, "La contraseña debe tener al menos 6 caracteres"),
});

const registerSchema = credentialsSchema.extend({
  acceptedTerms: z.literal(true, {
    errorMap: () => ({ message: "Debes aceptar los términos de uso y la política de privacidad" }),
  }),
});

function hashToken(rawToken: string) {
  return createHash("sha256").update(rawToken).digest("hex");
}

authRouter.post(
  "/register",
  authLimiter,
  asyncHandler(async (req, res) => {
    const parsed = registerSchema.safeParse(req.body);
    if (!parsed.success) {
      return res.status(400).json({ error: parsed.error.issues[0].message });
    }
    const { email, password } = parsed.data;

    const existing = await prisma.user.findUnique({ where: { email } });
    if (existing) {
      return res.status(409).json({ error: "Ya existe una cuenta con ese email" });
    }

    const passwordHash = await bcrypt.hash(password, 10);
    try {
      const user = await prisma.user.create({
        data: { email, passwordHash, termsAcceptedAt: new Date() },
      });
      res.status(201).json({ token: signToken(user.id, user.tokenVersion), user: toPublicUser(user) });
    } catch (err) {
      // Carrera entre el chequeo anterior y la creación: dos registros a la vez con el mismo email.
      if (err instanceof Prisma.PrismaClientKnownRequestError && err.code === "P2002") {
        return res.status(409).json({ error: "Ya existe una cuenta con ese email" });
      }
      throw err;
    }
  })
);

authRouter.post(
  "/login",
  authLimiter,
  asyncHandler(async (req, res) => {
    const parsed = credentialsSchema.safeParse(req.body);
    if (!parsed.success) {
      return res.status(400).json({ error: parsed.error.issues[0].message });
    }
    const { email, password } = parsed.data;

    const user = await prisma.user.findUnique({ where: { email } });
    if (!user) return res.status(401).json({ error: "Email o contraseña incorrectos" });

    const valid = await bcrypt.compare(password, user.passwordHash);
    if (!valid) return res.status(401).json({ error: "Email o contraseña incorrectos" });

    res.json({ token: signToken(user.id, user.tokenVersion), user: toPublicUser(user) });
  })
);

authRouter.get(
  "/me",
  requireAuth,
  asyncHandler(async (req: AuthedRequest, res) => {
    const user = await prisma.user.findUnique({ where: { id: req.userId } });
    if (!user) return res.status(404).json({ error: "Usuario no encontrado" });
    res.json({ user: toPublicUser(user) });
  })
);

const examDateSchema = z.object({
  examDate: z.string().datetime().nullable(),
});

authRouter.put(
  "/me/exam-date",
  requireAuth,
  asyncHandler(async (req: AuthedRequest, res) => {
    const parsed = examDateSchema.safeParse(req.body);
    if (!parsed.success) {
      return res.status(400).json({ error: parsed.error.issues[0].message });
    }
    const user = await prisma.user.update({
      where: { id: req.userId },
      data: { examDate: parsed.data.examDate ? new Date(parsed.data.examDate) : null },
    });
    res.json({ user: toPublicUser(user) });
  })
);

const forgotPasswordSchema = z.object({ email: z.string().email() });

authRouter.post(
  "/forgot-password",
  forgotPasswordLimiter,
  asyncHandler(async (req, res) => {
    const parsed = forgotPasswordSchema.safeParse(req.body);
    if (!parsed.success) {
      return res.status(400).json({ error: parsed.error.issues[0].message });
    }

    const user = await prisma.user.findUnique({ where: { email: parsed.data.email } });

    // Respuesta siempre igual, exista o no la cuenta: evita revelar qué emails están registrados.
    if (user) {
      const rawToken = randomBytes(32).toString("hex");
      await prisma.user.update({
        where: { id: user.id },
        data: {
          resetTokenHash: hashToken(rawToken),
          resetTokenExpiresAt: new Date(Date.now() + RESET_TOKEN_TTL_MS),
        },
      });

      const resetUrl = `${CLIENT_URL}/reset-password?uid=${user.id}&token=${rawToken}`;
      await sendEmail({
        to: user.email,
        subject: "Recupera tu contraseña de Teórico48",
        html: `
          <p>Hola,</p>
          <p>Hemos recibido una solicitud para restablecer tu contraseña de Teórico48.</p>
          <p><a href="${resetUrl}">Elige una nueva contraseña</a></p>
          <p>Este enlace caduca en 1 hora. Si no has sido tú, puedes ignorar este email.</p>
        `,
      });
    }

    res.json({ message: "Si existe una cuenta con ese email, te hemos enviado un enlace para restablecer la contraseña." });
  })
);

const resetPasswordSchema = z.object({
  userId: z.string(),
  token: z.string(),
  newPassword: z.string().min(6, "La contraseña debe tener al menos 6 caracteres"),
});

authRouter.post(
  "/reset-password",
  authLimiter,
  asyncHandler(async (req, res) => {
    const parsed = resetPasswordSchema.safeParse(req.body);
    if (!parsed.success) {
      return res.status(400).json({ error: parsed.error.issues[0].message });
    }
    const { userId, token, newPassword } = parsed.data;

    const user = await prisma.user.findUnique({ where: { id: userId } });
    if (
      !user ||
      !user.resetTokenHash ||
      !user.resetTokenExpiresAt ||
      user.resetTokenExpiresAt.getTime() < Date.now() ||
      user.resetTokenHash !== hashToken(token)
    ) {
      return res.status(400).json({ error: "El enlace no es válido o ha caducado. Pide uno nuevo." });
    }

    const passwordHash = await bcrypt.hash(newPassword, 10);
    await prisma.user.update({
      where: { id: user.id },
      data: {
        passwordHash,
        resetTokenHash: null,
        resetTokenExpiresAt: null,
        // Invalida cualquier token JWT emitido antes de este cambio (por ejemplo, en otro dispositivo).
        tokenVersion: { increment: 1 },
      },
    });

    await sendEmail({
      to: user.email,
      subject: "Tu contraseña de Teórico48 ha cambiado",
      html: `
        <p>Hola,</p>
        <p>Te confirmamos que la contraseña de tu cuenta de Teórico48 se ha cambiado correctamente.</p>
        <p>Si no has sido tú, escríbenos cuanto antes para proteger tu cuenta.</p>
      `,
    });

    res.json({ message: "Contraseña actualizada. Ya puedes iniciar sesión." });
  })
);

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
