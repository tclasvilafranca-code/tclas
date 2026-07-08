import webpush from "web-push";

const publicKey = process.env.VAPID_PUBLIC_KEY;
const privateKey = process.env.VAPID_PRIVATE_KEY;
const subject = process.env.VAPID_SUBJECT || "mailto:hello@t-clas.com";

const configured = Boolean(publicKey && privateKey);
if (configured) {
  webpush.setVapidDetails(subject, publicKey!, privateKey!);
} else {
  console.warn("VAPID_PUBLIC_KEY/VAPID_PRIVATE_KEY no configuradas: los recordatorios push quedan desactivados.");
}

export function isPushConfigured(): boolean {
  return configured;
}

export function getVapidPublicKey(): string | null {
  return publicKey ?? null;
}

export interface PushTarget {
  endpoint: string;
  p256dh: string;
  auth: string;
}

/** Envia una notificacion push. Devuelve false (sin lanzar) si la suscripcion
 * ya no es valida (p.ej. el alumno desinstalo la app o borro datos del navegador),
 * para que quien llama pueda borrarla de la base de datos. */
export async function sendPush(target: PushTarget, payload: { title: string; body: string }): Promise<boolean> {
  if (!configured) return false;
  try {
    await webpush.sendNotification(
      { endpoint: target.endpoint, keys: { p256dh: target.p256dh, auth: target.auth } },
      JSON.stringify(payload)
    );
    return true;
  } catch (err: any) {
    if (err?.statusCode === 404 || err?.statusCode === 410) return false; // suscripcion caducada/invalida
    console.error("Error enviando push:", err?.message || err);
    return false;
  }
}
