import { describe, expect, it } from "vitest";
import { computeNextStep } from "./plan";
import type { CategoryStat, Stats, User } from "./api";

function makeUser(overrides: Partial<User> = {}): User {
  return {
    id: "u1",
    email: "test@example.com",
    examDate: null,
    isPremium: false,
    xp: 0,
    level: 1,
    currentStreak: 0,
    longestStreak: 0,
    emailVerified: true,
    theoryCompletedSessions: ["s1", "s2", "s3"],
    ...overrides,
  };
}

function makeStats(overrides: Partial<Stats> = {}): Stats {
  return {
    xp: 0,
    level: 1,
    currentStreak: 0,
    longestStreak: 0,
    totalAttempts: 1,
    totalPassed: 1,
    badges: [],
    ...overrides,
  };
}

function makeCategory(overrides: Partial<CategoryStat> = {}): CategoryStat {
  return {
    slug: "senales",
    name: "Señales",
    answered: 10,
    correct: 9,
    accuracy: 90,
    ...overrides,
  };
}

describe("computeNextStep", () => {
  it("recomienda continuar la Teoría Express si no se han completado todas las sesiones", () => {
    const user = makeUser({ theoryCompletedSessions: ["s1"] });
    const step = computeNextStep(user, makeStats(), [makeCategory()]);
    expect(step.href).toBe("/teoria");
    expect(step.icon).toBe("BookOpen");
  });

  it("recomienda el diagnóstico general si no se ha practicado ninguna categoría", () => {
    const user = makeUser();
    const categories = [makeCategory({ answered: 0, accuracy: null }), makeCategory({ slug: "prioridad", answered: 0, accuracy: null })];
    const step = computeNextStep(user, makeStats(), categories);
    expect(step.href).toBe("/learn");
    expect(step.state).toBeUndefined();
    expect(step.title).toBe("Haz tu diagnóstico");
  });

  it("prioriza un simulacro real si el examen está a menos de 24h, aunque haya categorías débiles", () => {
    const soon = new Date(Date.now() + 5 * 3_600_000).toISOString();
    const user = makeUser({ examDate: soon });
    const categories = [makeCategory({ accuracy: 40 })];
    const step = computeNextStep(user, makeStats(), categories);
    expect(step.href).toBe("/exam");
    expect(step.title).toBe("Tu examen está cerca");
  });

  it("no activa el sprint final si el examen está a más de 24h", () => {
    const later = new Date(Date.now() + 48 * 3_600_000).toISOString();
    const user = makeUser({ examDate: later });
    const categories = [makeCategory({ accuracy: 40 })];
    const step = computeNextStep(user, makeStats(), categories);
    expect(step.title).not.toBe("Tu examen está cerca");
  });

  it("recomienda reforzar la categoría más débil si está por debajo del 70%", () => {
    const user = makeUser();
    const categories = [makeCategory({ slug: "senales", name: "Señales", accuracy: 90 }), makeCategory({ slug: "prioridad", name: "Prioridad", accuracy: 55 })];
    const step = computeNextStep(user, makeStats(), categories);
    expect(step.href).toBe("/learn");
    expect(step.state).toEqual({ categorySlug: "prioridad", categoryName: "Prioridad" });
  });

  it("recomienda una categoría sin practicar si todas las practicadas van bien", () => {
    const user = makeUser();
    const categories = [
      makeCategory({ slug: "senales", name: "Señales", accuracy: 90, answered: 10 }),
      makeCategory({ slug: "prioridad", name: "Prioridad", accuracy: null, answered: 0 }),
    ];
    const step = computeNextStep(user, makeStats(), categories);
    expect(step.state).toEqual({ categorySlug: "prioridad", categoryName: "Prioridad" });
  });

  it("recomienda el primer simulacro real si todas las categorías están practicadas y bien, pero aún no hay intentos", () => {
    const user = makeUser();
    const categories = [makeCategory({ accuracy: 90, answered: 10 })];
    const step = computeNextStep(user, makeStats({ totalAttempts: 0 }), categories);
    expect(step.href).toBe("/exam");
    expect(step.title).toBe("Haz tu primer simulacro real");
  });

  it("felicita y sugiere otro simulacro si todo va bien y ya hay intentos previos", () => {
    const user = makeUser();
    const categories = [makeCategory({ accuracy: 90, answered: 10 })];
    const step = computeNextStep(user, makeStats({ totalAttempts: 3 }), categories);
    expect(step.href).toBe("/exam");
    expect(step.title).toBe("Vas muy bien");
  });
});
