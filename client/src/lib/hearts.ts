// Debe coincidir con HEART_REGEN_MS en server/src/gamification.ts
export const HEART_REGEN_MS = 2 * 60 * 60 * 1000;

/** Milisegundos que faltan para el proximo corazon, dado el ultimo cambio registrado. */
export function msUntilNextHeart(heartsUpdatedAt: string): number {
  const elapsed = Date.now() - new Date(heartsUpdatedAt).getTime();
  const remainder = HEART_REGEN_MS - (elapsed % HEART_REGEN_MS);
  return Math.max(0, remainder);
}

export function formatCountdown(ms: number): string {
  const totalMin = Math.ceil(ms / 60000);
  const h = Math.floor(totalMin / 60);
  const m = totalMin % 60;
  if (h > 0) return `${h}h ${m}min`;
  return `${m} min`;
}
