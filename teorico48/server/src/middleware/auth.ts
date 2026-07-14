import { NextFunction, Request, Response } from "express";
import jwt from "jsonwebtoken";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export interface AuthedRequest extends Request {
  userId?: string;
}

const JWT_SECRET = process.env.JWT_SECRET;
if (!JWT_SECRET) {
  throw new Error("JWT_SECRET no configurado");
}

export function signToken(userId: string, tokenVersion: number) {
  return jwt.sign({ userId, tokenVersion }, JWT_SECRET!, { expiresIn: "30d" });
}

export async function requireAuth(req: AuthedRequest, res: Response, next: NextFunction) {
  const header = req.headers.authorization;
  const token = header?.startsWith("Bearer ") ? header.slice(7) : null;
  if (!token) {
    return res.status(401).json({ error: "No autenticado" });
  }
  try {
    const payload = jwt.verify(token, JWT_SECRET!) as { userId: string; tokenVersion: number };
    const user = await prisma.user.findUnique({
      where: { id: payload.userId },
      select: { tokenVersion: true },
    });
    // Si la contraseña se restableció después de emitir este token, tokenVersion ya no coincide.
    if (!user || user.tokenVersion !== payload.tokenVersion) {
      return res.status(401).json({ error: "Sesión caducada, vuelve a iniciar sesión" });
    }
    req.userId = payload.userId;
    next();
  } catch {
    return res.status(401).json({ error: "Token inválido o caducado" });
  }
}

// --- Panel de administrador (Bruno) ---
// No hay tabla de administradores: una única contraseña por variable de
// entorno y un JWT de corta duración con un campo "admin" que no puede
// aparecer en un token de usuario normal.

export function signAdminToken() {
  return jwt.sign({ admin: true }, JWT_SECRET!, { expiresIn: "12h" });
}

export function requireAdmin(req: Request, res: Response, next: NextFunction) {
  const header = req.headers.authorization;
  const token = header?.startsWith("Bearer ") ? header.slice(7) : null;
  if (!token) {
    return res.status(401).json({ error: "No autenticado como administrador" });
  }
  try {
    const payload = jwt.verify(token, JWT_SECRET!) as { admin?: boolean };
    if (payload.admin !== true) {
      return res.status(401).json({ error: "Token de administrador inválido" });
    }
    next();
  } catch {
    return res.status(401).json({ error: "Sesión de administrador caducada" });
  }
}
