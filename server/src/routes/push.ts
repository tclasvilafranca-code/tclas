import { Router } from "express";
import { z } from "zod";
import { prisma } from "../prisma";
import { requireAuth, AuthedRequest } from "../auth";
import { getVapidPublicKey, isPushConfigured } from "../push";

const router = Router();

router.get("/vapid-public-key", (_req, res) => {
  res.json({ publicKey: getVapidPublicKey(), configured: isPushConfigured() });
});

const subscribeSchema = z.object({
  endpoint: z.string().url(),
  keys: z.object({ p256dh: z.string().min(1), auth: z.string().min(1) }),
});

router.post("/subscribe", requireAuth, async (req: AuthedRequest, res) => {
  const parsed = subscribeSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos" });

  await prisma.pushSubscription.upsert({
    where: { endpoint: parsed.data.endpoint },
    create: { userId: req.auth!.userId, endpoint: parsed.data.endpoint, p256dh: parsed.data.keys.p256dh, auth: parsed.data.keys.auth },
    update: { userId: req.auth!.userId, p256dh: parsed.data.keys.p256dh, auth: parsed.data.keys.auth },
  });

  res.status(201).json({ ok: true });
});

const unsubscribeSchema = z.object({ endpoint: z.string().url() });

router.post("/unsubscribe", requireAuth, async (req: AuthedRequest, res) => {
  const parsed = unsubscribeSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: "Datos invalidos" });
  await prisma.pushSubscription.deleteMany({ where: { endpoint: parsed.data.endpoint, userId: req.auth!.userId } });
  res.json({ ok: true });
});

router.get("/status", requireAuth, async (req: AuthedRequest, res) => {
  const count = await prisma.pushSubscription.count({ where: { userId: req.auth!.userId } });
  res.json({ subscribed: count > 0 });
});

export default router;
