import { Router } from "express";
import Stripe from "stripe";
import { PrismaClient } from "@prisma/client";
import { requireAuth, AuthedRequest } from "../middleware/auth";

const prisma = new PrismaClient();
export const paymentsRouter = Router();

const stripeSecret = process.env.STRIPE_SECRET_KEY;
const stripe = stripeSecret ? new Stripe(stripeSecret) : null;

const PACK_PRICE_ID = process.env.STRIPE_PACK_PRICE_ID; // precio "Pack 48h" creado en el dashboard de Stripe
const CLIENT_URL = process.env.CLIENT_URL || "http://localhost:5173";

paymentsRouter.post("/checkout", requireAuth, async (req: AuthedRequest, res) => {
  if (!stripe || !PACK_PRICE_ID) {
    return res.status(503).json({ error: "Los pagos todavía no están configurados en el servidor" });
  }

  const user = await prisma.user.findUnique({ where: { id: req.userId } });
  if (!user) return res.status(404).json({ error: "Usuario no encontrado" });
  if (user.isPremium) return res.status(400).json({ error: "Ya tienes el Pack 48h activo" });

  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    payment_method_types: ["card"],
    line_items: [{ price: PACK_PRICE_ID, quantity: 1 }],
    customer_email: user.email,
    client_reference_id: user.id,
    success_url: `${CLIENT_URL}/paywall?success=1`,
    cancel_url: `${CLIENT_URL}/paywall?canceled=1`,
  });

  res.json({ url: session.url });
});

// Nota: esta ruta necesita el body en crudo (raw), se monta por separado en index.ts
export async function stripeWebhookHandler(req: import("express").Request, res: import("express").Response) {
  if (!stripe) return res.status(503).send("Stripe no configurado");

  const signature = req.headers["stripe-signature"];
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
  if (!signature || !webhookSecret) {
    return res.status(400).send("Falta configuración del webhook");
  }

  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(req.body, signature, webhookSecret);
  } catch (err) {
    return res.status(400).send(`Webhook error: ${(err as Error).message}`);
  }

  if (event.type === "checkout.session.completed") {
    const session = event.data.object as Stripe.Checkout.Session;
    const userId = session.client_reference_id;
    if (userId) {
      await prisma.user.update({
        where: { id: userId },
        data: { isPremium: true, stripeCustomerId: (session.customer as string) ?? undefined },
      });
    }
  }

  res.json({ received: true });
}
