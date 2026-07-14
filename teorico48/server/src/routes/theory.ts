import { Router } from "express";
import { z } from "zod";
import { PrismaClient } from "@prisma/client";
import { requireAuth, AuthedRequest } from "../middleware/auth";
import { BADGES, XP_PER_THEORY_SESSION, levelForXp, unlockedBadgeIds, updateStreak } from "../gamification";
import { asyncHandler } from "../lib/asyncHandler";

const prisma = new PrismaClient();
export const theoryRouter = Router();

// Debe coincidir con los IDs de sesion definidos en el cliente
// (client/src/content/theoryExpress.ts). Se valida aqui para no dar XP
// por un sessionId inventado.
const VALID_SESSION_IDS = ["s1", "s2", "s3"];

const completeSchema = z.object({ sessionId: z.string() });

theoryRouter.post(
  "/complete-session",
  requireAuth,
  asyncHandler(async (req: AuthedRequest, res) => {
    const parsed = completeSchema.safeParse(req.body);
    if (!parsed.success || !VALID_SESSION_IDS.includes(parsed.data.sessionId)) {
      return res.status(400).json({ error: "Sesión de teoría no reconocida" });
    }
    const { sessionId } = parsed.data;

    const user = await prisma.user.findUniqueOrThrow({ where: { id: req.userId } });

    // Idempotente: si ya se habia completado, no se vuelve a dar XP ni racha.
    if (user.theoryCompletedSessions.includes(sessionId)) {
      return res.json({
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

    res.json({
      alreadyCompleted: false,
      xpGained: XP_PER_THEORY_SESSION,
      totalXp: updated.xp,
      level: levelForXp(updated.xp),
      leveledUp: levelForXp(user.xp) !== levelForXp(updated.xp),
      theoryCompletedSessions: updated.theoryCompletedSessions,
      newBadges,
    });
  })
);
