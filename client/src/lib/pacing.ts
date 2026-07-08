import type { AgeGroup } from "./api";

// Ritmo por franja de edad: los peques necesitan mas tiempo para leer y
// responder, los adultos van mas rapido y no hace falta alargarles la espera.
const TIMER_MULTIPLIER: Record<AgeGroup, number> = { KIDS: 1.35, TEENS: 1, ADULTS: 0.85 };
const CORRECT_DELAY_MULTIPLIER: Record<AgeGroup, number> = { KIDS: 1.2, TEENS: 1, ADULTS: 0.85 };
const WRONG_DELAY_MULTIPLIER: Record<AgeGroup, number> = { KIDS: 1.15, TEENS: 1, ADULTS: 0.95 };

export function timerSecondsFor(ageGroup: AgeGroup, baseSeconds: number): number {
  return Math.round(baseSeconds * TIMER_MULTIPLIER[ageGroup]);
}

export function autoAdvanceDelayFor(ageGroup: AgeGroup, correct: boolean): number {
  const base = correct ? 1000 : 3400;
  const multiplier = correct ? CORRECT_DELAY_MULTIPLIER[ageGroup] : WRONG_DELAY_MULTIPLIER[ageGroup];
  return Math.round(base * multiplier);
}
