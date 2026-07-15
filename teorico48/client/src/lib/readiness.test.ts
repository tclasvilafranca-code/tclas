import { describe, expect, it } from "vitest";
import { computeReadiness } from "./readiness";
import type { Attempt, CategoryStat } from "./api";

function makeAttempt(overrides: Partial<Attempt> = {}): Attempt {
  return {
    id: "a1",
    mode: "exam",
    startedAt: "2026-07-01T10:00:00Z",
    finishedAt: "2026-07-01T10:20:00Z",
    score: 30,
    total: 30,
    passed: true,
    ...overrides,
  };
}

describe("computeReadiness", () => {
  it("devuelve null si no hay ningún simulacro real completado", () => {
    expect(computeReadiness([], [])).toBeNull();
  });

  it("ignora el Modo Aprendizaje y el repaso: solo cuentan los simulacros reales", () => {
    const attempts = [
      makeAttempt({ mode: "learn", score: 5, total: 30, passed: false }),
      makeAttempt({ mode: "practice", score: 10, total: 30, passed: false }),
    ];
    expect(computeReadiness(attempts, [])).toBeNull();
  });

  it("da 100 con un simulacro perfecto y sin categorías registradas", () => {
    const result = computeReadiness([makeAttempt({ score: 30, total: 30, passed: true })], []);
    expect(result).toEqual({ percent: 100, examsConsidered: 1 });
  });

  it("combina precisión media, tasa de aprobados y precisión por categoría", () => {
    const result = computeReadiness([makeAttempt({ score: 20, total: 30, passed: false })], []);
    // avgAccuracy=66.67*0.5 + passRate=0*0.3 + avgCategoryAccuracy(fallback a avgAccuracy)=66.67*0.2 = 46.67 -> 47
    expect(result?.percent).toBe(47);
  });

  it("una categoría floja penaliza aunque el simulacro haya sido perfecto", () => {
    const categories: CategoryStat[] = [
      { slug: "a", name: "A", answered: 10, correct: 4, accuracy: 40 },
      { slug: "b", name: "B", answered: 10, correct: 9, accuracy: 90 },
    ];
    const result = computeReadiness([makeAttempt({ score: 30, total: 30, passed: true })], categories);
    // 100*0.5 + 100*0.3 + 65*0.2 = 93
    expect(result?.percent).toBe(93);
  });

  it("solo tiene en cuenta los últimos 5 simulacros, aunque haya más en el historial", () => {
    const goodOnes = Array.from({ length: 5 }, () => makeAttempt({ score: 30, total: 30, passed: true }));
    const badOnes = Array.from({ length: 2 }, () => makeAttempt({ score: 5, total: 30, passed: false }));
    // Más recientes primero, como devuelve la API de historial.
    const result = computeReadiness([...goodOnes, ...badOnes], []);
    expect(result).toEqual({ percent: 100, examsConsidered: 5 });
  });
});
