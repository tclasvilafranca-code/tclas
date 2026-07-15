import { Hono } from "hono";
import { z } from "zod";
import { Prisma } from "@prisma/client";
import type { Env } from "../types";
import type { AppVariables } from "../lib/authMiddleware";
import { requireAuth } from "../lib/authMiddleware";
import { hashPassword, verifyPassword } from "../lib/password";
import { signUserToken } from "../lib/jwt";
import { hashToken, randomToken } from "../lib/tokens";
import { sendEmail } from "../lib/mailer";
import { levelForXp } from "../gamification";
import { authLimiter, forgotPasswordLimiter } from "../lib/rateLimit";

export const authRoutes = new Hono<{ Bindings: Env; Variables: AppVariables }>();

const RESET_TOKEN_TTL_MS = 60 * 60 * 1000; // 1 hora
const VERIFY_TOKEN_TTL_MS = 24 * 60 * 60 * 1000; // 24 horas

const credentialsSchema = z.object({
  email: z.string().email(),
  password: z.string().min(6, "La contraseña debe tener al menos 6 caracteres"),
});

const registerSchema = credentialsSchema.extend({
  acceptedTerms: z.literal(true, {
    errorMap: () => ({ message: "Debes aceptar los términos de uso y la política de privacidad" }),
  }),
  accessCode: z
    .string()
    .trim()
    .min(1, "Introduce tu código de acceso")
    .transform((v) => v.toUpperCase()),
});

class InvalidAccessCodeError extends Error {}

async function sendVerificationEmail(c: { env: Env; get: (k: "prisma") => import("@prisma/client").PrismaClient }, user: { id: string; email: string }) {
  const rawToken = randomToken();
  await c.get("prisma").user.update({
    where: { id: user.id },
    data: {
      verifyTokenHash: await hashToken(rawToken),
      verifyTokenExpiresAt: new Date(Date.now() + VERIFY_TOKEN_TTL_MS),
    },
  });

  const verifyUrl = `${c.env.CLIENT_URL}/verify-email?uid=${user.id}&token=${rawToken}`;
  await sendEmail(c.env, {
    to: user.email,
    subject: "Confirma tu email de Teórico48",
    html: `
      <p>Hola,</p>
      <p>Gracias por crear tu cuenta en Teórico48. Confirma tu email para terminar de configurarla:</p>
      <p><a href="${verifyUrl}">Confirmar mi email</a></p>
      <p>Este enlace caduca en 24 horas. Puedes seguir usando la app aunque no lo confirmes todavía.</p>
    `,
  });
}

authRoutes.post("/register", authLimiter, async (c) => {
  const body = await c.req.json().catch(() => ({}));
  const parsed = registerSchema.safeParse(body);
  if (!parsed.success) {
    return c.json({ error: parsed.error.issues[0].message }, 400);
  }
  const { email, password, accessCode } = parsed.data;
  const prisma = c.get("prisma");

  const existing = await prisma.user.findUnique({ where: { email } });
  if (existing) {
    return c.json({ error: "Ya existe una cuenta con ese email" }, 409);
  }

  const passwordHash = await hashPassword(password);
  try {
    const user = await prisma.$transaction(async (tx) => {
      // Reclama el código de forma atómica: si dos registros compiten por el
      // mismo código a la vez, solo uno consigue marcarlo como usado.
      const claim = await tx.accessCode.updateMany({
        where: {
          code: accessCode,
          usedAt: null,
          OR: [{ expiresAt: null }, { expiresAt: { gt: new Date() } }],
        },
        data: { usedAt: new Date() },
      });
      if (claim.count === 0) {
        throw new InvalidAccessCodeError();
      }

      // Todo código de acceso viene de una compra de la licencia completa,
      // así que toda cuenta nace con acceso total desde el primer momento.
      const createdUser = await tx.user.create({
        data: { email, passwordHash, termsAcceptedAt: new Date(), isPremium: true },
      });

      await tx.accessCode.update({
        where: { code: accessCode },
        data: { usedByUserId: createdUser.id },
      });

      return createdUser;
    });

    const token = await signUserToken(user.id, user.tokenVersion, c.env.JWT_SECRET);
    // No bloquea la respuesta: si el email tarda o falla, el registro ya se ha completado.
    c.executionCtx.waitUntil(
      sendVerificationEmail(c, user).catch((err) => console.error("No se pudo enviar el email de verificación:", err))
    );
    return c.json({ token, user: toPublicUser(user) }, 201);
  } catch (err) {
    if (err instanceof InvalidAccessCodeError) {
      return c.json({ error: "Ese código de acceso no es válido, ya se ha usado o ha caducado" }, 400);
    }
    if (err instanceof Prisma.PrismaClientKnownRequestError && err.code === "P2002") {
      return c.json({ error: "Ya existe una cuenta con ese email" }, 409);
    }
    throw err;
  }
});

authRoutes.post("/login", authLimiter, async (c) => {
  const body = await c.req.json().catch(() => ({}));
  const parsed = credentialsSchema.safeParse(body);
  if (!parsed.success) {
    return c.json({ error: parsed.error.issues[0].message }, 400);
  }
  const { email, password } = parsed.data;
  const prisma = c.get("prisma");

  const user = await prisma.user.findUnique({ where: { email } });
  if (!user) return c.json({ error: "Email o contraseña incorrectos" }, 401);

  const valid = await verifyPassword(password, user.passwordHash);
  if (!valid) return c.json({ error: "Email o contraseña incorrectos" }, 401);

  // Solo se permite una sesión activa a la vez: cada login invalida
  // cualquier token emitido antes (de otro dispositivo), para dificultar
  // que varias personas compartan la misma cuenta a la vez.
  const updated = await prisma.user.update({
    where: { id: user.id },
    data: { tokenVersion: { increment: 1 } },
  });

  const token = await signUserToken(updated.id, updated.tokenVersion, c.env.JWT_SECRET);
  return c.json({ token, user: toPublicUser(updated) });
});

authRoutes.get("/me", requireAuth, async (c) => {
  const user = await c.get("prisma").user.findUnique({ where: { id: c.get("userId") } });
  if (!user) return c.json({ error: "Usuario no encontrado" }, 404);
  return c.json({ user: toPublicUser(user) });
});

const examDateSchema = z.object({ examDate: z.string().datetime().nullable() });

authRoutes.put("/me/exam-date", requireAuth, async (c) => {
  const body = await c.req.json().catch(() => ({}));
  const parsed = examDateSchema.safeParse(body);
  if (!parsed.success) {
    return c.json({ error: parsed.error.issues[0].message }, 400);
  }
  const user = await c.get("prisma").user.update({
    where: { id: c.get("userId") },
    data: { examDate: parsed.data.examDate ? new Date(parsed.data.examDate) : null },
  });
  return c.json({ user: toPublicUser(user) });
});

const forgotPasswordSchema = z.object({ email: z.string().email() });

authRoutes.post("/forgot-password", forgotPasswordLimiter, async (c) => {
  const body = await c.req.json().catch(() => ({}));
  const parsed = forgotPasswordSchema.safeParse(body);
  if (!parsed.success) {
    return c.json({ error: parsed.error.issues[0].message }, 400);
  }
  const prisma = c.get("prisma");

  const user = await prisma.user.findUnique({ where: { email: parsed.data.email } });

  // Respuesta siempre igual, exista o no la cuenta: evita revelar qué emails están registrados.
  if (user) {
    const rawToken = randomToken();
    await prisma.user.update({
      where: { id: user.id },
      data: {
        resetTokenHash: await hashToken(rawToken),
        resetTokenExpiresAt: new Date(Date.now() + RESET_TOKEN_TTL_MS),
      },
    });

    const resetUrl = `${c.env.CLIENT_URL}/reset-password?uid=${user.id}&token=${rawToken}`;
    await sendEmail(c.env, {
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

  return c.json({ message: "Si existe una cuenta con ese email, te hemos enviado un enlace para restablecer la contraseña." });
});

const resetPasswordSchema = z.object({
  userId: z.string(),
  token: z.string(),
  newPassword: z.string().min(6, "La contraseña debe tener al menos 6 caracteres"),
});

authRoutes.post("/reset-password", authLimiter, async (c) => {
  const body = await c.req.json().catch(() => ({}));
  const parsed = resetPasswordSchema.safeParse(body);
  if (!parsed.success) {
    return c.json({ error: parsed.error.issues[0].message }, 400);
  }
  const { userId, token, newPassword } = parsed.data;
  const prisma = c.get("prisma");

  const user = await prisma.user.findUnique({ where: { id: userId } });
  const providedHash = await hashToken(token);
  if (
    !user ||
    !user.resetTokenHash ||
    !user.resetTokenExpiresAt ||
    user.resetTokenExpiresAt.getTime() < Date.now() ||
    user.resetTokenHash !== providedHash
  ) {
    return c.json({ error: "El enlace no es válido o ha caducado. Pide uno nuevo." }, 400);
  }

  const passwordHash = await hashPassword(newPassword);
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

  await sendEmail(c.env, {
    to: user.email,
    subject: "Tu contraseña de Teórico48 ha cambiado",
    html: `
      <p>Hola,</p>
      <p>Te confirmamos que la contraseña de tu cuenta de Teórico48 se ha cambiado correctamente.</p>
      <p>Si no has sido tú, escríbenos cuanto antes para proteger tu cuenta.</p>
    `,
  });

  return c.json({ message: "Contraseña actualizada. Ya puedes iniciar sesión." });
});

const verifyEmailSchema = z.object({ userId: z.string(), token: z.string() });

authRoutes.post("/verify-email", authLimiter, async (c) => {
  const body = await c.req.json().catch(() => ({}));
  const parsed = verifyEmailSchema.safeParse(body);
  if (!parsed.success) {
    return c.json({ error: parsed.error.issues[0].message }, 400);
  }
  const { userId, token } = parsed.data;
  const prisma = c.get("prisma");

  const user = await prisma.user.findUnique({ where: { id: userId } });
  const providedHash = await hashToken(token);
  if (
    !user ||
    !user.verifyTokenHash ||
    !user.verifyTokenExpiresAt ||
    user.verifyTokenExpiresAt.getTime() < Date.now() ||
    user.verifyTokenHash !== providedHash
  ) {
    return c.json({ error: "El enlace no es válido o ha caducado. Pide uno nuevo desde tu panel." }, 400);
  }

  await prisma.user.update({
    where: { id: user.id },
    data: { emailVerified: true, verifyTokenHash: null, verifyTokenExpiresAt: null },
  });

  return c.json({ message: "Email verificado correctamente." });
});

authRoutes.post("/resend-verification", requireAuth, forgotPasswordLimiter, async (c) => {
  const prisma = c.get("prisma");
  const user = await prisma.user.findUnique({ where: { id: c.get("userId") } });
  if (!user) return c.json({ error: "Usuario no encontrado" }, 404);
  if (user.emailVerified) {
    return c.json({ error: "Tu email ya está verificado" }, 400);
  }

  await sendVerificationEmail(c, user);
  return c.json({ message: "Te hemos enviado un nuevo enlace de verificación." });
});

function toPublicUser(user: {
  id: string;
  email: string;
  examDate: Date | null;
  isPremium: boolean;
  xp: number;
  currentStreak: number;
  longestStreak: number;
  emailVerified: boolean;
  theoryCompletedSessions: string[];
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
    emailVerified: user.emailVerified,
    theoryCompletedSessions: user.theoryCompletedSessions,
  };
}
