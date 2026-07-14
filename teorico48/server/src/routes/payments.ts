import { Router } from "express";
import Stripe from "stripe";
import { PrismaClient } from "@prisma/client";
import { requireAuth, AuthedRequest } from "../middleware/auth";
import { asyncHandler } from "../lib/asyncHandler";
import { sendEmail } from "../mailer";

const prisma = new PrismaClient();
export const paymentsRouter = Router();

const stripeSecret = process.env.STRIPE_SECRET_KEY;
const stripe = stripeSecret ? new Stripe(stripeSecret) : null;

const PACK_PRICE_ID = process.env.STRIPE_PACK_PRICE_ID; // precio "Pack 48h" creado en el dashboard de Stripe
const CLIENT_URL = process.env.CLIENT_URL || "http://localhost:5173";
const OWNER_EMAIL = process.env.OWNER_EMAIL;

paymentsRouter.post(
  "/checkout",
  requireAuth,
  asyncHandler(async (req: AuthedRequest, res) => {
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
  })
);

// Compra de la licencia de acceso, sin necesidad de tener cuenta todavía: el
// cliente paga primero y recibe el código de acceso por email a mano, una vez
// el administrador lo genera desde /admin al ver la notificación de compra.
paymentsRouter.post(
  "/checkout-license",
  asyncHandler(async (_req, res) => {
    if (!stripe || !PACK_PRICE_ID) {
      return res.status(503).json({ error: "Los pagos todavía no están configurados en el servidor" });
    }

    const session = await stripe.checkout.sessions.create({
      mode: "payment",
      payment_method_types: ["card"],
      line_items: [{ price: PACK_PRICE_ID, quantity: 1 }],
      metadata: { type: "license" },
      success_url: `${CLIENT_URL}/comprar/gracias`,
      cancel_url: `${CLIENT_URL}/?compra=cancelada`,
    });

    res.json({ url: session.url });
  })
);

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

  try {
    if (event.type === "checkout.session.completed") {
      const session = event.data.object as Stripe.Checkout.Session;

      if (session.metadata?.type === "license") {
        const buyerEmail = session.customer_details?.email ?? "email no disponible";
        console.log(`Nueva compra de licencia (sesión ${session.id}): comprador ${buyerEmail}`);
        if (OWNER_EMAIL) {
          await sendEmail({
            to: OWNER_EMAIL,
            subject: "Nueva compra de licencia — Teórico48",
            html: `
              <p>Alguien acaba de comprar el acceso a Teórico48.</p>
              <p><strong>Email del comprador:</strong> ${buyerEmail}</p>
              <p>Genera un código de acceso marcado como "Concede Pack 48h" desde
              <a href="${CLIENT_URL}/admin">${CLIENT_URL}/admin</a> y envíaselo a ese email junto con las
              instrucciones para registrarse.</p>
            `,
          });
        } else {
          console.warn("OWNER_EMAIL no configurado: no se ha podido notificar la compra por email.");
        }
      } else {
        const userId = session.client_reference_id;
        if (userId) {
          await prisma.user.update({
            where: { id: userId },
            data: { isPremium: true, stripeCustomerId: (session.customer as string) ?? undefined },
          });
          console.log(`Pack 48h activado para el usuario ${userId} (sesión ${session.id})`);
        } else {
          console.error(`checkout.session.completed sin client_reference_id (sesión ${session.id})`);
        }
      }
    }
  } catch (err) {
    // Devolvemos 500 para que Stripe reintente la entrega del webhook más tarde
    // en vez de dar por hecho, silenciosamente, que el usuario ya tiene acceso.
    console.error("Error procesando el webhook de Stripe:", err);
    return res.status(500).send("Error interno procesando el webhook");
  }

  res.json({ received: true });
}
