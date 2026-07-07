import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";
import { Role } from "./types";

const JWT_SECRET = process.env.JWT_SECRET || "tclas-dev-secret-change-in-production";

export interface AuthPayload {
  userId: string;
  role: Role;
}

export interface AuthedRequest extends Request {
  auth?: AuthPayload;
}

export function signToken(payload: AuthPayload): string {
  return jwt.sign(payload, JWT_SECRET, { expiresIn: "30d" });
}

export function requireAuth(req: AuthedRequest, res: Response, next: NextFunction) {
  const header = req.headers.authorization;
  if (!header || !header.startsWith("Bearer ")) {
    return res.status(401).json({ error: "No autorizado" });
  }
  const token = header.slice("Bearer ".length);
  try {
    const decoded = jwt.verify(token, JWT_SECRET) as AuthPayload;
    req.auth = decoded;
    next();
  } catch {
    return res.status(401).json({ error: "Token invalido o expirado" });
  }
}

export function requireRole(role: Role) {
  return (req: AuthedRequest, res: Response, next: NextFunction) => {
    if (!req.auth || req.auth.role !== role) {
      return res.status(403).json({ error: "No tienes permiso para esta accion" });
    }
    next();
  };
}
