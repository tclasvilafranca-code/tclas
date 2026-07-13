export const XP_PER_CORRECT = 10;
export const XP_PASS_BONUS = 50;
export const XP_PERFECT_BONUS = 100;
const XP_PER_LEVEL = 100;

export function xpForAttempt(score: number, total: number, passed: boolean) {
  return score * XP_PER_CORRECT + (passed ? XP_PASS_BONUS : 0) + (score === total ? XP_PERFECT_BONUS : 0);
}

export function levelForXp(xp: number) {
  return Math.floor(xp / XP_PER_LEVEL) + 1;
}

export function xpIntoLevel(xp: number) {
  return xp % XP_PER_LEVEL;
}

function startOfDay(date: Date) {
  const d = new Date(date);
  d.setHours(0, 0, 0, 0);
  return d;
}

/** Actualiza la racha diaria: mismo día no suma, día siguiente +1, si hay hueco se reinicia a 1. */
export function updateStreak(
  lastActivityDate: Date | null,
  currentStreak: number,
  longestStreak: number,
  now: Date = new Date()
) {
  const today = startOfDay(now);
  let nextStreak = currentStreak;

  if (!lastActivityDate) {
    nextStreak = 1;
  } else {
    const last = startOfDay(lastActivityDate);
    const diffDays = Math.round((today.getTime() - last.getTime()) / 86_400_000);
    if (diffDays === 0) {
      nextStreak = currentStreak || 1;
    } else if (diffDays === 1) {
      nextStreak = currentStreak + 1;
    } else {
      nextStreak = 1;
    }
  }

  return {
    currentStreak: nextStreak,
    longestStreak: Math.max(longestStreak, nextStreak),
    lastActivityDate: today,
  };
}

export interface BadgeStats {
  xp: number;
  longestStreak: number;
  totalAttempts: number;
  totalPassed: number;
  hasPerfect: boolean;
}

export interface Badge {
  id: string;
  label: string;
  emoji: string;
  check: (s: BadgeStats) => boolean;
}

export const BADGES: Badge[] = [
  { id: "primer-test", label: "Primer test", emoji: "🎯", check: (s) => s.totalAttempts >= 1 },
  { id: "primer-aprobado", label: "Primer aprobado", emoji: "✅", check: (s) => s.totalPassed >= 1 },
  { id: "racha-3", label: "Racha de 3 días", emoji: "🔥", check: (s) => s.longestStreak >= 3 },
  { id: "racha-7", label: "Racha de 7 días", emoji: "🔥🔥", check: (s) => s.longestStreak >= 7 },
  { id: "xp-100", label: "100 XP", emoji: "⭐", check: (s) => s.xp >= 100 },
  { id: "xp-500", label: "500 XP", emoji: "🌟", check: (s) => s.xp >= 500 },
  { id: "xp-1000", label: "1.000 XP", emoji: "💎", check: (s) => s.xp >= 1000 },
  { id: "perfecto", label: "Test perfecto", emoji: "🏆", check: (s) => s.hasPerfect },
  { id: "diez-tests", label: "10 tests completados", emoji: "📚", check: (s) => s.totalAttempts >= 10 },
];

export function unlockedBadgeIds(stats: BadgeStats): string[] {
  return BADGES.filter((b) => b.check(stats)).map((b) => b.id);
}
