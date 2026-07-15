import { Hono } from "hono";
import { cors } from "hono/cors";
import type { Env } from "./types";
import type { AppVariables } from "./lib/authMiddleware";
import { createPrisma } from "./db";
import { authRoutes } from "./routes/auth";
import { testsRoutes } from "./routes/tests";
import { paymentsRoutes } from "./routes/payments";
import { adminRoutes } from "./routes/admin";
import { theoryRoutes } from "./routes/theory";

const app = new Hono<{ Bindings: Env; Variables: AppVariables }>();

// API pura en JSON consumida por un frontend en otro origen: sin CSP (no
// sirve HTML) y con CORP en "cross-origin" para que el navegador no bloquee
// las respuestas.
app.use("*", async (c, next) => {
  await next();
  c.header("X-Content-Type-Options", "nosniff");
  c.header("X-Frame-Options", "DENY");
  c.header("Cross-Origin-Resource-Policy", "cross-origin");
  c.header("Referrer-Policy", "no-referrer");
});

// Sin CLIENT_URL configurado (p. ej. en desarrollo) se permite cualquier
// origen; en producción, restringe las peticiones a la propia web de la app.
app.use("*", async (c, next) => {
  const middleware = cors({ origin: c.env.CLIENT_URL || "*" });
  return middleware(c, next);
});

// Un cliente Prisma nuevo por petición (necesario en un Worker, que no
// mantiene estado entre peticiones como sí puede un servidor Node normal).
app.use("*", async (c, next) => {
  c.set("prisma", createPrisma(c.env));
  await next();
});

app.get("/api/health", (c) => c.json({ ok: true }));

app.route("/api/auth", authRoutes);
app.route("/api/tests", testsRoutes);
app.route("/api/payments", paymentsRoutes);
app.route("/api/admin", adminRoutes);
app.route("/api/theory", theoryRoutes);

// Cualquier error inesperado llega aquí en vez de filtrar detalles internos.
app.onError((err, c) => {
  console.error("Error no controlado:", err);
  return c.json({ error: "Ha ocurrido un error inesperado. Inténtalo de nuevo en un momento." }, 500);
});

export default app;
