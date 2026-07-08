import { prisma } from "./prisma";
import { sendPush, isPushConfigured } from "./push";

function startOfDay(date: Date): Date {
  const d = new Date(date);
  d.setHours(0, 0, 0, 0);
  return d;
}

const REMINDER_MESSAGES = [
  "Misol te espera para una sesion rapida de piano 🎹",
  "Solo 15 minutos y mantienes viva tu racha 🔥",
  "¿Practicamos un ratito hoy? Tu pieza te esta esperando 🎵",
];

/**
 * Revisa que alumnos no han practicado hoy y les manda un unico recordatorio
 * push al dia (si tienen alguna suscripcion activa). Pensado para llamarse
 * periodicamente desde index.ts, nunca desde los tests (que importan app.ts,
 * no index.ts, asi que esto nunca corre durante la suite de tests).
 *
 * Limitacion conocida: usa la hora del servidor, no la zona horaria de cada
 * alumno (no se guarda en ningun sitio), asi que la ventana horaria de envio
 * es la misma para todos independientemente de donde vivan.
 */
export async function runReminderSweep(): Promise<{ sent: number; skipped: number }> {
  if (!isPushConfigured()) return { sent: 0, skipped: 0 };

  const today = startOfDay(new Date());
  const candidates = await prisma.studentProfile.findMany({
    where: {
      user: { pushSubscriptions: { some: {} } },
      AND: [
        { OR: [{ lastActivityDate: null }, { lastActivityDate: { lt: today } }] },
        { OR: [{ lastReminderSentAt: null }, { lastReminderSentAt: { lt: today } }] },
      ],
    },
    include: { user: { include: { pushSubscriptions: true } } },
  });

  let sent = 0;
  let skipped = 0;
  for (const profile of candidates) {
    const message = REMINDER_MESSAGES[Math.floor(Math.random() * REMINDER_MESSAGES.length)];
    const payload = { title: "t-clas 🎹", body: message };
    let anySucceeded = false;
    const deadEndpoints: string[] = [];

    for (const sub of profile.user.pushSubscriptions) {
      const ok = await sendPush({ endpoint: sub.endpoint, p256dh: sub.p256dh, auth: sub.auth }, payload);
      if (ok) anySucceeded = true;
      else deadEndpoints.push(sub.endpoint);
    }

    if (deadEndpoints.length > 0) {
      await prisma.pushSubscription.deleteMany({ where: { endpoint: { in: deadEndpoints } } });
    }
    if (anySucceeded) {
      sent += 1;
      await prisma.studentProfile.update({ where: { id: profile.id }, data: { lastReminderSentAt: new Date() } });
    } else {
      skipped += 1;
    }
  }

  return { sent, skipped };
}
