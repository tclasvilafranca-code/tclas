import type { CategoryStat, Stats, User } from "./api";
import { THEORY_EXPRESS } from "../content/theoryExpress";

export type PlanIcon = "BookOpen" | "CheckCircle" | "Target" | "BarChart" | "Star";

export interface PlanStep {
  icon: PlanIcon;
  title: string;
  description: string;
  ctaLabel: string;
  href: string;
  state?: Record<string, string>;
}

// Umbral por debajo del cual una categoría se considera un punto débil que
// merece atención prioritaria frente a simplemente "seguir practicando".
const WEAK_CATEGORY_THRESHOLD = 70;
// Si el examen real está a menos de esto, toca priorizar un simulacro en
// condiciones reales por encima de seguir estudiando teoría o categorías sueltas.
const FINAL_SPRINT_HOURS = 24;

/** Decide cuál es el siguiente paso recomendado, combinando la cuenta atrás,
 * el progreso en Teoría Express y la precisión por categoría. Es una función
 * pura: no llama a la API, solo decide a partir de los datos ya cargados. */
export function computeNextStep(user: User, stats: Stats, categories: CategoryStat[]): PlanStep {
  const theoryDone = user.theoryCompletedSessions?.length ?? 0;
  const theoryTotal = THEORY_EXPRESS.length;

  if (theoryDone < theoryTotal) {
    return {
      icon: "BookOpen",
      title: "Sigue con la Teoría Express",
      description: `Sesión ${theoryDone + 1} de ${theoryTotal} — lo esencial antes de practicar en serio.`,
      ctaLabel: "Continuar",
      href: "/teoria",
    };
  }

  const practiced = categories.filter((c) => c.answered > 0);
  if (practiced.length === 0) {
    return {
      icon: "CheckCircle",
      title: "Haz tu diagnóstico",
      description: "Un Modo Aprendizaje general para ver en qué categorías fallas más.",
      ctaLabel: "Empezar",
      href: "/learn",
    };
  }

  let hoursUntilExam: number | null = null;
  if (user.examDate) {
    const diff = (new Date(user.examDate).getTime() - Date.now()) / 3_600_000;
    if (diff > 0) hoursUntilExam = diff;
  }

  if (hoursUntilExam !== null && hoursUntilExam < FINAL_SPRINT_HOURS) {
    return {
      icon: "Target",
      title: "Tu examen está cerca",
      description: "Haz un simulacro en condiciones reales para llegar con confianza.",
      ctaLabel: "Hacer simulacro",
      href: "/exam",
    };
  }

  const withAccuracy = categories.filter((c): c is CategoryStat & { accuracy: number } => c.accuracy !== null);
  const worst = [...withAccuracy].sort((a, b) => a.accuracy - b.accuracy)[0];
  if (worst && worst.accuracy < WEAK_CATEGORY_THRESHOLD) {
    return {
      icon: "BarChart",
      title: `Refuerza "${worst.name}"`,
      description: `Vas al ${worst.accuracy}% — es tu punto más débil ahora mismo.`,
      ctaLabel: "Practicar",
      href: "/learn",
      state: { categorySlug: worst.slug, categoryName: worst.name },
    };
  }

  const unpracticed = categories.find((c) => c.answered === 0);
  if (unpracticed) {
    return {
      icon: "BarChart",
      title: `Prueba "${unpracticed.name}"`,
      description: "Todavía no la has practicado nada.",
      ctaLabel: "Practicar",
      href: "/learn",
      state: { categorySlug: unpracticed.slug, categoryName: unpracticed.name },
    };
  }

  if (stats.totalAttempts === 0) {
    return {
      icon: "Target",
      title: "Haz tu primer simulacro real",
      description: "30 preguntas, en las mismas condiciones que el examen de verdad.",
      ctaLabel: "Empezar",
      href: "/exam",
    };
  }

  return {
    icon: "Star",
    title: "Vas muy bien",
    description: "Todas tus categorías están en buena forma — otro simulacro para no perder el ritmo.",
    ctaLabel: "Otro simulacro",
    href: "/exam",
  };
}
