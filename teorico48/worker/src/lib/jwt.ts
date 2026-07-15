import { sign, verify } from "hono/jwt";

const USER_TOKEN_TTL_SECONDS = 30 * 24 * 60 * 60; // 30 días, igual que antes
const ADMIN_TOKEN_TTL_SECONDS = 12 * 60 * 60; // 12 horas

export interface UserTokenPayload {
  userId: string;
  tokenVersion: number;
  exp: number;
}

export interface AdminTokenPayload {
  admin: true;
  exp: number;
}

export function signUserToken(userId: string, tokenVersion: number, secret: string): Promise<string> {
  const exp = Math.floor(Date.now() / 1000) + USER_TOKEN_TTL_SECONDS;
  return sign({ userId, tokenVersion, exp }, secret);
}

export async function verifyUserToken(token: string, secret: string): Promise<UserTokenPayload | null> {
  try {
    return (await verify(token, secret, "HS256")) as unknown as UserTokenPayload;
  } catch {
    return null;
  }
}

export function signAdminToken(secret: string): Promise<string> {
  const exp = Math.floor(Date.now() / 1000) + ADMIN_TOKEN_TTL_SECONDS;
  return sign({ admin: true, exp }, secret);
}

export async function verifyAdminToken(token: string, secret: string): Promise<AdminTokenPayload | null> {
  try {
    const payload = (await verify(token, secret, "HS256")) as unknown as AdminTokenPayload;
    return payload.admin === true ? payload : null;
  } catch {
    return null;
  }
}
