import "dotenv/config";
import express from "express";
import cors from "cors";
import helmet from "helmet";
import { authRouter } from "./routes/auth";
import { testsRouter } from "./routes/tests";
import { paymentsRouter, stripeWebhookHandler } from "./routes/payments";

const app = express();

// API pura en JSON consumida por un frontend en otro origen: sin CSP (no sirve HTML)
// y con CORP en "cross-origin" para que el navegador no bloquee las respuestas.
app.use(
  helmet({
    contentSecurityPolicy: false,
    crossOriginResourcePolicy: { policy: "cross-origin" },
  })
);

// Sin CLIENT_URL configurado (p. ej. en desarrollo) se permite cualquier origen;
// en producción, restringe las peticiones a la propia web de la app.
const CLIENT_URL = process.env.CLIENT_URL;
app.use(cors(CLIENT_URL ? { origin: CLIENT_URL } : {}));

// El webhook de Stripe necesita el body en crudo, se monta antes del json parser global.
app.post("/api/payments/webhook", express.raw({ type: "application/json" }), stripeWebhookHandler);

app.use(express.json());

app.get("/api/health", (_req, res) => res.json({ ok: true }));

app.use("/api/auth", authRouter);
app.use("/api/tests", testsRouter);
app.use("/api/payments", paymentsRouter);

// Middleware de error final: cualquier error inesperado llega aquí (via
// asyncHandler) en vez de tumbar el proceso o filtrar detalles internos.
app.use((err: unknown, _req: express.Request, res: express.Response, _next: express.NextFunction) => {
  console.error("Error no controlado:", err);
  if (res.headersSent) return;
  res.status(500).json({ error: "Ha ocurrido un error inesperado. Inténtalo de nuevo en un momento." });
});

process.on("unhandledRejection", (reason) => {
  console.error("Promesa rechazada sin capturar:", reason);
});

const port = process.env.PORT || 4001;
app.listen(port, () => {
  console.log(`teorico48-server escuchando en el puerto ${port}`);
});
