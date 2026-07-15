import type { Context, Next } from "hono";
import type { PrismaClient } from "@prisma/client";
import type { Env } from "../types";
import { verifyAdminToken, verifyUserToken } from "./jwt";

export interface AppVariables {
  prisma: PrismaClient;
  userId: string;
}

type AppContext = Context<{ Bindings: Env; Variables: AppVariables }>;

function bearerToken(c: Context): string | null {
  const header = c.req.header("authorization");
  return header?.startsWith("Bearer ") ? header.slice(7) : null;
}

export async function requireAuth(c: AppContext, next: Next) {
  const token = bearerToken(c);
  if (!token) {
    return c.json({ error: "No autenticado" }, 401);
  }
  const payload = await verifyUserToken(token, c.env.JWT_SECRET);
  if (!payload) {
    return c.json({ error: "Token inválido o caducado" }, 401);
  }

  const user = await c.get("prisma").user.findUnique({
    where: { id: payload.userId },
    select: { tokenVersion: true },
  });
  // Si la contraseña se restableció, o se inició sesión en otro dispositivo,
  // después de emitir este token, tokenVersion ya no coincide.
  if (!user || user.tokenVersion !== payload.tokenVersion) {
    return c.json({ error: "Sesión caducada, vuelve a iniciar sesión" }, 401);
  }

  c.set("userId", payload.userId);
  await next();
}

export async function requireAdmin(c: Context<{ Bindings: Env }>, next: Next) {
  const token = bearerToken(c);
  if (!token) {
    return c.json({ error: "No autenticado como administrador" }, 401);
  }
  const payload = await verifyAdminToken(token, c.env.JWT_SECRET);
  if (!payload) {
    return c.json({ error: "Sesión de administrador caducada" }, 401);
  }
  await next();
}
