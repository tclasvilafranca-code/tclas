import { prisma } from "./prisma";

export type DifficultyLevel = "easy" | "normal" | "hard";

export interface DifficultyAdjustment {
  VISUAL_AGILITY: DifficultyLevel;
  EAR_ACUITY: DifficultyLevel;
  NOTE_RUSH: DifficultyLevel;
}

export const NORMAL_DIFFICULTY: DifficultyAdjustment = { VISUAL_AGILITY: "normal", EAR_ACUITY: "normal", NOTE_RUSH: "normal" };

// Con menos intentos que esto en un bloque, no hay datos suficientes para
// ajustar nada: se queda en "normal" para no adaptar sobre ruido.
const MIN_SAMPLE = 8;

function levelFor(correct: number, total: number): DifficultyLevel {
  if (total < MIN_SAMPLE) return "normal";
  const pct = correct / total;
  if (pct >= 0.85) return "hard";
  if (pct <= 0.55) return "easy";
  return "normal";
}

/**
 * Calcula la dificultad de los bloques de agilidad visual, agudeza auditiva y
 * notas al vuelo segun el acierto historico real del alumno en cada uno.
 * Solo se usa al generar lecciones NUEVAS (una pieza que se le asigna a
 * partir de ahora): no modifica nada de lo ya generado.
 */
export async function computeAdaptiveDifficulty(userId: string): Promise<DifficultyAdjustment> {
  const attempts = await prisma.exerciseAttempt.findMany({
    where: { userId },
    select: { correct: true, exercise: { select: { phase: true } } },
  });

  const totals = new Map<string, { correct: number; total: number }>();
  for (const a of attempts) {
    const entry = totals.get(a.exercise.phase) ?? { correct: 0, total: 0 };
    entry.total += 1;
    if (a.correct) entry.correct += 1;
    totals.set(a.exercise.phase, entry);
  }
  const get = (phase: string) => totals.get(phase) ?? { correct: 0, total: 0 };

  return {
    VISUAL_AGILITY: levelFor(get("VISUAL_AGILITY").correct, get("VISUAL_AGILITY").total),
    EAR_ACUITY: levelFor(get("EAR_ACUITY").correct, get("EAR_ACUITY").total),
    NOTE_RUSH: levelFor(get("NOTE_RUSH").correct, get("NOTE_RUSH").total),
  };
}
