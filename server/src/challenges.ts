import { prisma } from "./prisma";
import { awardXP } from "./gamification";

// Semana natural (lunes a domingo), distinta de la ventana movil de "ultimos
// 7 dias" que ya se usa en el Perfil: un reto semanal tiene sentido que
// reinicie cada lunes, no que vaya rodando dia a dia.
function startOfWeek(date: Date): Date {
  const d = new Date(date);
  d.setHours(0, 0, 0, 0);
  const day = d.getDay(); // 0 domingo .. 6 sabado
  const diffToMonday = (day + 6) % 7;
  d.setDate(d.getDate() - diffToMonday);
  return d;
}

interface ChallengeDef {
  code: string;
  label: string;
  icon: string;
  target: number;
  xpReward: number;
}

const CHALLENGE_DEFS: ChallengeDef[] = [
  { code: "practice_days", label: "Practica 3 días esta semana", icon: "📅", target: 3, xpReward: 20 },
  { code: "complete_lessons", label: "Completa 2 lecciones esta semana", icon: "🎯", target: 2, xpReward: 25 },
  { code: "practice_minutes", label: "Practica 60 minutos esta semana", icon: "⏱️", target: 60, xpReward: 20 },
];

export interface ChallengeStatus {
  code: string;
  label: string;
  icon: string;
  progress: number;
  target: number;
  completed: boolean;
  xpReward: number;
}

async function computeProgress(userId: string, weekStart: Date, weekEnd: Date): Promise<Record<string, number>> {
  const [logs, completedLessons] = await Promise.all([
    prisma.practiceLog.findMany({ where: { userId, date: { gte: weekStart, lt: weekEnd } } }),
    prisma.progress.count({ where: { userId, status: "COMPLETED", completedAt: { gte: weekStart, lt: weekEnd } } }),
  ]);
  const practiceDays = logs.filter((l) => l.minutes > 0).length;
  const practiceMinutes = logs.reduce((sum, l) => sum + l.minutes, 0);
  return { practice_days: practiceDays, complete_lessons: completedLessons, practice_minutes: practiceMinutes };
}

/** Lectura pura: progreso de los retos de esta semana, sin dar ninguna
 * recompensa (eso solo pasa en checkAndAwardChallenges). */
export async function getWeeklyChallenges(userId: string): Promise<ChallengeStatus[]> {
  const weekStart = startOfWeek(new Date());
  const weekEnd = new Date(weekStart.getTime() + 7 * 86400000);
  const progressByCode = await computeProgress(userId, weekStart, weekEnd);

  return CHALLENGE_DEFS.map((def) => {
    const progress = progressByCode[def.code] ?? 0;
    return { code: def.code, label: def.label, icon: def.icon, progress, target: def.target, completed: progress >= def.target, xpReward: def.xpReward };
  });
}

/** Se llama tras completar una leccion (que es cuando cambian los tres
 * numeros que alimentan los retos): comprueba si algun reto de esta semana
 * se acaba de cumplir por primera vez y, si es asi, da su XP una sola vez. */
export async function checkAndAwardChallenges(userId: string): Promise<{ code: string; label: string; icon: string; xpReward: number }[]> {
  const weekStart = startOfWeek(new Date());
  const weekEnd = new Date(weekStart.getTime() + 7 * 86400000);
  const progressByCode = await computeProgress(userId, weekStart, weekEnd);

  const alreadyAwarded = await prisma.challengeCompletion.findMany({ where: { userId, weekStart } });
  const awardedCodes = new Set(alreadyAwarded.map((a) => a.challengeCode));

  const newlyCompleted: { code: string; label: string; icon: string; xpReward: number }[] = [];
  for (const def of CHALLENGE_DEFS) {
    if (awardedCodes.has(def.code)) continue;
    const progress = progressByCode[def.code] ?? 0;
    if (progress < def.target) continue;

    await prisma.challengeCompletion.create({
      data: { userId, challengeCode: def.code, weekStart, xpAwarded: def.xpReward },
    });
    await awardXP(userId, def.xpReward, `Reto semanal: ${def.label}`);
    newlyCompleted.push({ code: def.code, label: def.label, icon: def.icon, xpReward: def.xpReward });
  }
  return newlyCompleted;
}
