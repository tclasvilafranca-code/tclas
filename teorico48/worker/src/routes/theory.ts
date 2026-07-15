import { Hono } from "hono";
import { z } from "zod";
import type { Env } from "../types";
import type { AppVariables } from "../lib/authMiddleware";
import { requireAuth } from "../lib/authMiddleware";
import { BADGES, XP_PER_THEORY_SESSION, levelForXp, unlockedBadgeIds, updateStreak } from "../gamification";

export const theoryRoutes = new Hono<{ Bindings: Env; Variables: AppVariables }>();

// Debe coincidir con los IDs de sesion definidos en el cliente
// (client/src/content/theoryExpress.ts). Se valida aqui para no dar XP
// por un sessionId inventado.
const VALID_SESSION_IDS = ["s1", "s2", "s3"];

const completeSchema = z.object({ sessionId: z.string() });

theoryRoutes.post("/complete-session", requireAuth, async (c) => {
  const body = await c.req.json().catch(() => ({}));
  const parsed = completeSchema.safeParse(body);
  if (!parsed.success || !VALID_SESSION_IDS.includes(parsed.data.sessionId)) {
    return c.json({ error: "Sesión de teoría no reconocida" }, 400);
  }
  const { sessionId } = parsed.data;
  const prisma = c.get("prisma");
  const userId = c.get("userId");

  const user = await prisma.user.findUniqueOrThrow({ where: { id: userId } });

  // Idempotente: si ya se habia completado, no se vuelve a dar XP ni racha.
  if (user.theoryCompletedSessions.includes(sessionId)) {
    return c.json({
      alreadyCompleted: true,
      xpGained: 0,
      totalXp: user.xp,
      level: levelForXp(user.xp),
      theoryCompletedSessions: user.theoryCompletedSessions,
      newBadges: [],
    });
  }

  const streak = updateStreak(user.lastActivityDate, user.currentStreak, user.longestStreak);
  const newXp = user.xp + XP_PER_THEORY_SESSION;
  const newCompletedSessions = [...user.theoryCompletedSessions, sessionId];

  const priorAttempts = await prisma.testAttempt.findMany({
    where: { userId: user.id, finishedAt: { not: null } },
    select: { score: true, total: true, passed: true },
  });
  const beforeStats = {
    xp: user.xp,
    longestStreak: user.longestStreak,
    totalAttempts: priorAttempts.length,
    totalPassed: priorAttempts.filter((a) => a.passed).length,
    hasPerfect: priorAttempts.some((a) => a.score !== null && a.total !== null && a.score === a.total),
    theorySessionsCompleted: user.theoryCompletedSessions.length,
  };
  const afterStats = { ...beforeStats, xp: newXp, longestStreak: streak.longestStreak, theorySessionsCompleted: newCompletedSessions.length };

  const badgesBefore = new Set(unlockedBadgeIds(beforeStats));
  const newBadgeIds = unlockedBadgeIds(afterStats).filter((id) => !badgesBefore.has(id));
  const newBadges = BADGES.filter((b) => newBadgeIds.includes(b.id)).map((b) => ({ id: b.id, label: b.label, emoji: b.emoji }));

  const updated = await prisma.user.update({
    where: { id: user.id },
    data: {
      xp: newXp,
      currentStreak: streak.currentStreak,
      longestStreak: streak.longestStreak,
      lastActivityDate: streak.lastActivityDate,
      theoryCompletedSessions: newCompletedSessions,
    },
  });

  return c.json({
    alreadyCompleted: false,
    xpGained: XP_PER_THEORY_SESSION,
    totalXp: updated.xp,
    level: levelForXp(updated.xp),
    leveledUp: levelForXp(user.xp) !== levelForXp(updated.xp),
    theoryCompletedSessions: updated.theoryCompletedSessions,
    newBadges,
  });
});
