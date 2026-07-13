import "dotenv/config";
import express from "express";
import cors from "cors";
import { authRouter } from "./routes/auth";
import { testsRouter } from "./routes/tests";
import { paymentsRouter, stripeWebhookHandler } from "./routes/payments";

const app = express();

app.use(cors());

// El webhook de Stripe necesita el body en crudo, se monta antes del json parser global.
app.post("/api/payments/webhook", express.raw({ type: "application/json" }), stripeWebhookHandler);

app.use(express.json());

app.get("/api/health", (_req, res) => res.json({ ok: true }));

app.use("/api/auth", authRouter);
app.use("/api/tests", testsRouter);
app.use("/api/payments", paymentsRouter);

const port = process.env.PORT || 4001;
app.listen(port, () => {
  console.log(`teorico48-server escuchando en el puerto ${port}`);
});
