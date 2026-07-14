import { describe, expect, it } from "vitest";
import {
  XP_PASS_BONUS,
  XP_PERFECT_BONUS,
  XP_PER_CORRECT,
  levelForXp,
  unlockedBadgeIds,
  updateStreak,
  xpForAttempt,
  xpIntoLevel,
} from "./gamification";

describe("xpForAttempt", () => {
  it("da 10 XP por cada acierto, sin bonus, si no aprueba ni es perfecto", () => {
    expect(xpForAttempt(20, 30, false)).toBe(20 * XP_PER_CORRECT);
  });

  it("suma el bonus de aprobado cuando passed es true", () => {
    expect(xpForAttempt(27, 30, true)).toBe(27 * XP_PER_CORRECT + XP_PASS_BONUS);
  });

  it("suma también el bonus de perfecto cuando score === total", () => {
    expect(xpForAttempt(30, 30, true)).toBe(30 * XP_PER_CORRECT + XP_PASS_BONUS + XP_PERFECT_BONUS);
  });

  it("no da el bonus de perfecto si el aprobado no es con nota máxima", () => {
    const conFallos = xpForAttempt(28, 30, true);
    const perfecto = xpForAttempt(30, 30, true);
    expect(perfecto - conFallos).toBeGreaterThanOrEqual(XP_PERFECT_BONUS);
  });
});

describe("levelForXp / xpIntoLevel", () => {
  it("empieza en nivel 1 con 0 XP", () => {
    expect(levelForXp(0)).toBe(1);
  });

  it("sube de nivel cada 100 XP", () => {
    expect(levelForXp(99)).toBe(1);
    expect(levelForXp(100)).toBe(2);
    expect(levelForXp(250)).toBe(3);
  });

  it("xpIntoLevel es el resto dentro del nivel actual", () => {
    expect(xpIntoLevel(0)).toBe(0);
    expect(xpIntoLevel(150)).toBe(50);
    expect(xpIntoLevel(999)).toBe(99);
  });
});

describe("updateStreak", () => {
  it("empieza en racha 1 si no había actividad previa", () => {
    const r = updateStreak(null, 0, 0, new Date("2026-07-14T10:00:00Z"));
    expect(r.currentStreak).toBe(1);
    expect(r.longestStreak).toBe(1);
  });

  it("no incrementa la racha si ya hubo actividad hoy mismo", () => {
    const today = new Date("2026-07-14T09:00:00Z");
    const r = updateStreak(today, 5, 5, new Date("2026-07-14T20:00:00Z"));
    expect(r.currentStreak).toBe(5);
  });

  it("incrementa la racha en +1 si la última actividad fue ayer", () => {
    const yesterday = new Date("2026-07-13T09:00:00Z");
    const r = updateStreak(yesterday, 5, 5, new Date("2026-07-14T09:00:00Z"));
    expect(r.currentStreak).toBe(6);
    expect(r.longestStreak).toBe(6);
  });

  it("reinicia la racha a 1 si hay un hueco de más de un día", () => {
    const threeDaysAgo = new Date("2026-07-11T09:00:00Z");
    const r = updateStreak(threeDaysAgo, 10, 10, new Date("2026-07-14T09:00:00Z"));
    expect(r.currentStreak).toBe(1);
    // El récord (longestStreak) no debe perderse aunque la racha actual se reinicie.
    expect(r.longestStreak).toBe(10);
  });
});

describe("unlockedBadgeIds", () => {
  const baseStats = {
    xp: 0,
    longestStreak: 0,
    totalAttempts: 0,
    totalPassed: 0,
    hasPerfect: false,
    theorySessionsCompleted: 0,
  };

  it("no desbloquea nada para un usuario sin actividad", () => {
    expect(unlockedBadgeIds(baseStats)).toEqual([]);
  });

  it("desbloquea 'primer-test' con el primer intento", () => {
    expect(unlockedBadgeIds({ ...baseStats, totalAttempts: 1 })).toContain("primer-test");
  });

  it("desbloquea las medallas de racha en sus umbrales exactos", () => {
    expect(unlockedBadgeIds({ ...baseStats, longestStreak: 3 })).toContain("racha-3");
    expect(unlockedBadgeIds({ ...baseStats, longestStreak: 2 })).not.toContain("racha-3");
    expect(unlockedBadgeIds({ ...baseStats, longestStreak: 7 })).toContain("racha-7");
  });

  it("desbloquea 'teoria-express' solo al completar las 3 sesiones", () => {
    expect(unlockedBadgeIds({ ...baseStats, theorySessionsCompleted: 2 })).not.toContain("teoria-express");
    expect(unlockedBadgeIds({ ...baseStats, theorySessionsCompleted: 3 })).toContain("teoria-express");
  });

  it("desbloquea varias medallas a la vez si se cumplen varios umbrales", () => {
    const unlocked = unlockedBadgeIds({
      ...baseStats,
      xp: 1200,
      totalAttempts: 10,
      totalPassed: 5,
      hasPerfect: true,
      longestStreak: 7,
    });
    expect(unlocked).toEqual(
      expect.arrayContaining(["primer-test", "primer-aprobado", "racha-3", "racha-7", "xp-100", "xp-500", "xp-1000", "perfecto", "diez-tests"])
    );
  });
});
