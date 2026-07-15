import { Hono } from "hono";
import Stripe from "stripe";
import type { Env } from "../types";
import type { AppVariables } from "../lib/authMiddleware";
import { sendEmail } from "../lib/mailer";

export const paymentsRoutes = new Hono<{ Bindings: Env; Variables: AppVariables }>();

function stripeClient(env: Env) {
  return new Stripe(env.STRIPE_SECRET_KEY, {
    httpClient: Stripe.createFetchHttpClient(),
  });
}

// Compra de la licencia de acceso, sin necesidad de tener cuenta todavía: el
// cliente paga primero y recibe el código de acceso por email a mano, una vez
// el administrador lo genera desde /admin al ver la notificación de compra.
// Toda licencia da acceso completo a la app desde el registro.
paymentsRoutes.post("/checkout-license", async (c) => {
  if (!c.env.STRIPE_SECRET_KEY || !c.env.STRIPE_PACK_PRICE_ID) {
    return c.json({ error: "Los pagos todavía no están configurados en el servidor" }, 503);
  }
  const stripe = stripeClient(c.env);

  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    payment_method_types: ["card"],
    line_items: [{ price: c.env.STRIPE_PACK_PRICE_ID, quantity: 1 }],
    metadata: { type: "license" },
    success_url: `${c.env.CLIENT_URL}/comprar/gracias`,
    cancel_url: `${c.env.CLIENT_URL}/?compra=cancelada`,
  });

  return c.json({ url: session.url });
});

paymentsRoutes.post("/webhook", async (c) => {
  if (!c.env.STRIPE_SECRET_KEY) return c.text("Stripe no configurado", 503);

  const signature = c.req.header("stripe-signature");
  if (!signature || !c.env.STRIPE_WEBHOOK_SECRET) {
    return c.text("Falta configuración del webhook", 400);
  }

  const stripe = stripeClient(c.env);
  const body = await c.req.text();

  let event: Stripe.Event;
  try {
    // constructEventAsync (en vez de la versión síncrona) porque Workers no
    // tiene el módulo "crypto" de Node: la verificación de la firma se hace
    // con la API nativa SubtleCrypto en su lugar.
    event = await stripe.webhooks.constructEventAsync(
      body,
      signature,
      c.env.STRIPE_WEBHOOK_SECRET,
      undefined,
      Stripe.createSubtleCryptoProvider()
    );
  } catch (err) {
    return c.text(`Webhook error: ${(err as Error).message}`, 400);
  }

  try {
    if (event.type === "checkout.session.completed") {
      const session = event.data.object as Stripe.Checkout.Session;
      const buyerEmail = session.customer_details?.email ?? "email no disponible";
      console.log(`Nueva compra de licencia (sesión ${session.id}): comprador ${buyerEmail}`);
      if (c.env.OWNER_EMAIL) {
        await sendEmail(c.env, {
          to: c.env.OWNER_EMAIL,
          subject: "Nueva compra de licencia — Teórico48",
          html: `
            <p>Alguien acaba de comprar el acceso a Teórico48.</p>
            <p><strong>Email del comprador:</strong> ${buyerEmail}</p>
            <p>Genera un código de acceso desde <a href="${c.env.CLIENT_URL}/admin">${c.env.CLIENT_URL}/admin</a> y
            envíaselo a ese email junto con las instrucciones para registrarse.</p>
          `,
        });
      } else {
        console.warn("OWNER_EMAIL no configurado: no se ha podido notificar la compra por email.");
      }
    }
  } catch (err) {
    // Devolvemos 500 para que Stripe reintente la entrega del webhook más tarde
    // en vez de dar por hecho, silenciosamente, que la compra ya se ha gestionado.
    console.error("Error procesando el webhook de Stripe:", err);
    return c.text("Error interno procesando el webhook", 500);
  }

  return c.json({ received: true });
});
