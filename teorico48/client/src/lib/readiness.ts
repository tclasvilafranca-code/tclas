import type { Attempt, CategoryStat } from "./api";

export interface Readiness {
  percent: number;
  examsConsidered: number;
}

const MAX_EXAMS_CONSIDERED = 5;

/** Estima, de forma orientativa, la preparación del usuario para el examen
 * real a partir de sus últimos simulacros (mismo formato que el examen: 30
 * preguntas, máx. 3 fallos) y la precisión por categoría. No es una
 * predicción científica, solo una señal para ayudar a decidir si arriesgarse
 * ya o seguir practicando un poco más.
 *
 * `attempts` debe venir ordenado del más reciente al más antiguo (como ya
 * hace la API de historial), para que solo se tengan en cuenta los últimos
 * simulacros reales. Devuelve `null` si todavía no hay ningún simulacro real
 * completado (Modo Aprendizaje y repaso no cuentan: no son el mismo formato).
 */
export function computeReadiness(attempts: Attempt[], categories: CategoryStat[]): Readiness | null {
  const examAttempts = attempts.filter(
    (a): a is Attempt & { score: number; total: number } => a.mode === "exam" && a.score !== null && a.total !== null
  );
  if (examAttempts.length === 0) return null;

  const recent = examAttempts.slice(0, MAX_EXAMS_CONSIDERED);
  const avgAccuracy = recent.reduce((sum, a) => sum + (a.score / a.total) * 100, 0) / recent.length;
  const passRate = (recent.filter((a) => a.passed).length / recent.length) * 100;

  const practiced = categories.filter((c): c is CategoryStat & { accuracy: number } => c.accuracy !== null);
  const avgCategoryAccuracy = practiced.length > 0 ? practiced.reduce((sum, c) => sum + c.accuracy, 0) / practiced.length : avgAccuracy;

  const weighted = avgAccuracy * 0.5 + passRate * 0.3 + avgCategoryAccuracy * 0.2;
  const percent = Math.round(Math.min(100, Math.max(0, weighted)));

  return { percent, examsConsidered: recent.length };
}
