import "dotenv/config";
import { app } from "./app";
import { runReminderSweep } from "./reminders";

const PORT = Number(process.env.PORT) || 4000;
app.listen(PORT, () => {
  console.log(`t-clas API escuchando en http://localhost:${PORT}`);
});

// Recordatorios de practica: se revisa cada 30 min, pero solo se manda algo
// entre las 16:00 y las 21:00 (hora del servidor) para no molestar de
// madrugada. Limitacion conocida: no sabemos la zona horaria real de cada
// alumno, asi que esta franja es la misma para todos.
const REMINDER_CHECK_MS = 30 * 60 * 1000;
const REMINDER_WINDOW_START_HOUR = 16;
const REMINDER_WINDOW_END_HOUR = 21;

setInterval(async () => {
  const hour = new Date().getHours();
  if (hour < REMINDER_WINDOW_START_HOUR || hour >= REMINDER_WINDOW_END_HOUR) return;
  try {
    const { sent, skipped } = await runReminderSweep();
    if (sent > 0 || skipped > 0) console.log(`Recordatorios de practica: ${sent} enviados, ${skipped} omitidos.`);
  } catch (err) {
    console.error("Error en el barrido de recordatorios:", err);
  }
}, REMINDER_CHECK_MS);
