import type { Context, Next } from "hono";
import type { Env } from "../types";

interface RateLimitOptions {
  windowSeconds: number;
  limit: number;
  message: string;
}

/** Limitador simple por IP usando Workers KV como contador de ventana fija.
 * KV es de consistencia eventual (no hay incrementos atómicos de verdad), así
 * que bajo mucha concurrencia se puede colar algún intento de más — un
 * compromiso razonable para frenar fuerza bruta básica, no un sistema de
 * alta seguridad. */
export function rateLimiter(name: string, options: RateLimitOptions) {
  return async (c: Context<{ Bindings: Env }>, next: Next) => {
    const ip = c.req.header("cf-connecting-ip") ?? "unknown";
    const key = `ratelimit:${name}:${ip}`;

    const current = await c.env.RATE_LIMIT_KV.get(key);
    const count = current ? Number(current) : 0;

    if (count >= options.limit) {
      return c.json({ error: options.message }, 429);
    }

    await c.env.RATE_LIMIT_KV.put(key, String(count + 1), { expirationTtl: options.windowSeconds });
    await next();
  };
}

export const authLimiter = rateLimiter("auth", {
  windowSeconds: 15 * 60,
  limit: 20,
  message: "Demasiados intentos. Espera unos minutos y vuelve a intentarlo.",
});

export const forgotPasswordLimiter = rateLimiter("forgot-password", {
  windowSeconds: 15 * 60,
  limit: 5,
  message: "Demasiadas solicitudes. Espera unos minutos y vuelve a intentarlo.",
});
