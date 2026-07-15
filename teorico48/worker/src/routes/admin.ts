import { Hono } from "hono";
import { z } from "zod";
import type { Env } from "../types";
import type { AppVariables } from "../lib/authMiddleware";
import { requireAdmin } from "../lib/authMiddleware";
import { authLimiter } from "../lib/rateLimit";
import { signAdminToken } from "../lib/jwt";
import { generateAccessCode } from "../lib/tokens";

export const adminRoutes = new Hono<{ Bindings: Env; Variables: AppVariables }>();

const loginSchema = z.object({ password: z.string() });

adminRoutes.post("/login", authLimiter, async (c) => {
  if (!c.env.ADMIN_PASSWORD) {
    return c.json({ error: "El panel de administrador no está configurado en el servidor" }, 503);
  }
  const body = await c.req.json().catch(() => ({}));
  const parsed = loginSchema.safeParse(body);
  if (!parsed.success) {
    return c.json({ error: "Falta la contraseña" }, 400);
  }
  if (parsed.data.password !== c.env.ADMIN_PASSWORD) {
    return c.json({ error: "Contraseña incorrecta" }, 401);
  }
  const token = await signAdminToken(c.env.JWT_SECRET);
  return c.json({ token });
});

const createCodesSchema = z.object({
  count: z.number().int().min(1).max(50).default(1),
  note: z.string().trim().max(200).optional(),
  expiresInDays: z.number().int().min(1).max(365).optional(),
});

adminRoutes.post("/access-codes", requireAdmin, async (c) => {
  const body = await c.req.json().catch(() => ({}));
  const parsed = createCodesSchema.safeParse(body);
  if (!parsed.success) {
    return c.json({ error: parsed.error.issues[0].message }, 400);
  }
  const { count, note, expiresInDays } = parsed.data;
  const expiresAt = expiresInDays ? new Date(Date.now() + expiresInDays * 24 * 60 * 60 * 1000) : null;
  const prisma = c.get("prisma");

  const codes = await Promise.all(
    Array.from({ length: count }).map(async () => {
      // Reintenta si por casualidad choca con un código ya existente (muy improbable).
      for (let attempt = 0; attempt < 5; attempt++) {
        try {
          return await prisma.accessCode.create({
            data: { code: generateAccessCode(), note: note || null, expiresAt },
          });
        } catch (err: any) {
          if (err?.code !== "P2002") throw err;
        }
      }
      throw new Error("No se pudo generar un código único, inténtalo de nuevo");
    })
  );

  return c.json({ codes }, 201);
});

adminRoutes.get("/access-codes", requireAdmin, async (c) => {
  const codes = await c.get("prisma").accessCode.findMany({
    orderBy: { createdAt: "desc" },
    take: 200,
    include: { usedByUser: { select: { email: true } } },
  });
  return c.json({
    codes: codes.map((code) => ({
      id: code.id,
      code: code.code,
      note: code.note,
      createdAt: code.createdAt,
      expiresAt: code.expiresAt,
      usedAt: code.usedAt,
      usedByEmail: code.usedByUser?.email ?? null,
    })),
  });
});
