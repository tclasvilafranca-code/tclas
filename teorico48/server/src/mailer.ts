const RESEND_API_KEY = process.env.RESEND_API_KEY;
const MAIL_FROM = process.env.MAIL_FROM || "Teórico48 <onboarding@resend.dev>";

interface SendEmailInput {
  to: string;
  subject: string;
  html: string;
}

/**
 * Envia un email transaccional via Resend si hay API key configurada.
 * Sin clave (p. ej. en desarrollo), lo escribe en la consola del servidor
 * para poder probar el flujo completo sin depender de un proveedor externo.
 */
export async function sendEmail({ to, subject, html }: SendEmailInput): Promise<void> {
  if (!RESEND_API_KEY) {
    const links = [...html.matchAll(/href="([^"]+)"/g)].map((m) => m[1]);
    console.log("\n[email simulado — configura RESEND_API_KEY para enviarlo de verdad]");
    console.log(`Para: ${to}`);
    console.log(`Asunto: ${subject}`);
    console.log(html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim());
    if (links.length > 0) {
      console.log(`Enlace(s): ${links.join(", ")}`);
    }
    console.log("");
    return;
  }

  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${RESEND_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ from: MAIL_FROM, to, subject, html }),
  });

  if (!res.ok) {
    const body = await res.text().catch(() => "");
    console.error(`No se pudo enviar el email a ${to}: ${res.status} ${body}`);
  }
}
