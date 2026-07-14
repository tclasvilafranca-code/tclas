import { Router } from "express";
import { randomInt } from "crypto";
import { z } from "zod";
import { PrismaClient } from "@prisma/client";
import { signAdminToken, requireAdmin } from "../middleware/auth";
import { asyncHandler } from "../lib/asyncHandler";
import { authLimiter } from "../lib/rateLimit";

const prisma = new PrismaClient();
export const adminRouter = Router();

const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD;

// Sin O/0/I/1 para que no se confundan al copiar el código a mano.
const CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";

function generateCode(): string {
  let code = "";
  for (let i = 0; i < 8; i++) {
    code += CODE_ALPHABET[randomInt(CODE_ALPHABET.length)];
  }
  return code;
}

const loginSchema = z.object({ password: z.string() });

adminRouter.post(
  "/login",
  authLimiter,
  asyncHandler(async (req, res) => {
    if (!ADMIN_PASSWORD) {
      return res.status(503).json({ error: "El panel de administrador no está configurado en el servidor" });
    }
    const parsed = loginSchema.safeParse(req.body);
    if (!parsed.success) {
      return res.status(400).json({ error: "Falta la contraseña" });
    }
    if (parsed.data.password !== ADMIN_PASSWORD) {
      return res.status(401).json({ error: "Contraseña incorrecta" });
    }
    res.json({ token: signAdminToken() });
  })
);

const createCodesSchema = z.object({
  count: z.number().int().min(1).max(50).default(1),
  note: z.string().trim().max(200).optional(),
  expiresInDays: z.number().int().min(1).max(365).optional(),
});

adminRouter.post(
  "/access-codes",
  requireAdmin,
  asyncHandler(async (req, res) => {
    const parsed = createCodesSchema.safeParse(req.body);
    if (!parsed.success) {
      return res.status(400).json({ error: parsed.error.issues[0].message });
    }
    const { count, note, expiresInDays } = parsed.data;
    const expiresAt = expiresInDays ? new Date(Date.now() + expiresInDays * 24 * 60 * 60 * 1000) : null;

    const codes = await Promise.all(
      Array.from({ length: count }).map(async () => {
        // Reintenta si por casualidad choca con un código ya existente (muy improbable).
        for (let attempt = 0; attempt < 5; attempt++) {
          try {
            return await prisma.accessCode.create({
              data: { code: generateCode(), note: note || null, expiresAt },
            });
          } catch (err: any) {
            if (err?.code !== "P2002") throw err;
          }
        }
        throw new Error("No se pudo generar un código único, inténtalo de nuevo");
      })
    );

    res.status(201).json({ codes });
  })
);

adminRouter.get(
  "/access-codes",
  requireAdmin,
  asyncHandler(async (_req, res) => {
    const codes = await prisma.accessCode.findMany({
      orderBy: { createdAt: "desc" },
      take: 200,
      include: { usedByUser: { select: { email: true } } },
    });
    res.json({
      codes: codes.map((c) => ({
        id: c.id,
        code: c.code,
        note: c.note,
        createdAt: c.createdAt,
        expiresAt: c.expiresAt,
        usedAt: c.usedAt,
        usedByEmail: c.usedByUser?.email ?? null,
      })),
    });
  })
);
