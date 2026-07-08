import { StudentProfile } from "@prisma/client";
import { prisma } from "./prisma";
import { ExerciseType } from "./types";

const HEART_REGEN_MS = 2 * 60 * 60 * 1000; // 1 corazon cada 2h

/** Recalcula los corazones actuales segun el tiempo transcurrido y persiste el resultado. */
export async function recomputeHearts(profile: StudentProfile): Promise<StudentProfile> {
  if (profile.heartsCurrent >= profile.heartsMax) return profile;
  const elapsed = Date.now() - new Date(profile.heartsUpdatedAt).getTime();
  const regained = Math.floor(elapsed / HEART_REGEN_MS);
  if (regained <= 0) return profile;
  const newHearts = Math.min(profile.heartsMax, profile.heartsCurrent + regained);
  return prisma.studentProfile.update({
    where: { id: profile.id },
    data: { heartsCurrent: newHearts, heartsUpdatedAt: new Date() },
  });
}

export async function loseHeart(profile: StudentProfile): Promise<StudentProfile> {
  const fresh = await recomputeHearts(profile);
  if (fresh.heartsCurrent <= 0) return fresh;
  return prisma.studentProfile.update({
    where: { id: fresh.id },
    data: { heartsCurrent: fresh.heartsCurrent - 1, heartsUpdatedAt: new Date() },
  });
}

function isSameDay(a: Date, b: Date): boolean {
  return a.toDateString() === b.toDateString();
}
function isYesterday(a: Date, b: Date): boolean {
  const d = new Date(b);
  d.setDate(d.getDate() - 1);
  return isSameDay(a, d);
}

/** Actualiza la racha (streak) de practica diaria al registrar actividad. */
export async function registerDailyActivity(profile: StudentProfile): Promise<StudentProfile> {
  const now = new Date();
  let streakCurrent = profile.streakCurrent;
  if (!profile.lastActivityDate) {
    streakCurrent = 1;
  } else if (isSameDay(new Date(profile.lastActivityDate), now)) {
    // ya conto hoy, no cambia
  } else if (isYesterday(new Date(profile.lastActivityDate), now)) {
    streakCurrent = profile.streakCurrent + 1;
  } else {
    streakCurrent = 1;
  }
  const streakLongest = Math.max(profile.streakLongest, streakCurrent);
  return prisma.studentProfile.update({
    where: { id: profile.id },
    data: { streakCurrent, streakLongest, lastActivityDate: now },
  });
}

export async function awardXP(userId: string, amount: number, reason: string) {
  await prisma.xPEvent.create({ data: { userId, amount, reason } });
  return prisma.studentProfile.update({
    where: { userId },
    data: { xpTotal: { increment: amount } },
  });
}

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

/** Normaliza texto libre para comparar respuestas escritas o dictadas: minusculas, sin acentos, sin espacios de sobra. */
function normalizeText(v: unknown): string {
  return String(v)
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .trim()
    .replace(/\s+/g, " ");
}

export function gradeExercise(type: ExerciseType, data: any, userAnswer: unknown): boolean {
  const normalize = (v: unknown) =>
    Array.isArray(v) ? v.map((x) => String(x).toUpperCase()) : String(v).toUpperCase();

  switch (type) {
    case "NOTE_NAME":
      return normalize(userAnswer) === normalize(data.correctAnswer);
    case "THEORY_MCQ":
      return normalize(userAnswer) === normalize(data.correctAnswer);
    case "EAR_TRAINING":
      return normalize(userAnswer) === normalize(data.answer);
    case "INTERVAL":
      return normalize(userAnswer) === normalize(data.answer);
    case "CHORD":
      return normalize(userAnswer) === normalize(data.answer);
    case "STAFF_READING":
    case "KEYBOARD_PLAY": {
      const expected = (data.notes as string[]).map((n) => n.toUpperCase());
      const got = Array.isArray(userAnswer) ? (userAnswer as string[]).map((n) => String(n).toUpperCase()) : [];
      return expected.length === got.length && expected.every((n, i) => n === got[i]);
    }
    case "RHYTHM_TAP": {
      const expected = data.pattern as number[];
      const got = Array.isArray(userAnswer) ? (userAnswer as number[]) : [];
      if (expected.length !== got.length) return false;
      return expected.every((v, i) => Math.abs(v - Number(got[i])) < 0.3);
    }
    case "WRITE_ANSWER": {
      const accepted = [data.correctAnswer, ...(data.acceptableAnswers ?? [])].map(normalizeText);
      return accepted.includes(normalizeText(userAnswer));
    }
    case "SPEAK_ALOUD": {
      const accepted = [data.expectedAnswer, ...(data.acceptableAnswers ?? [])].map(normalizeText);
      const said = normalizeText(userAnswer);
      if (!said) return false;
      return accepted.some((a) => said === a || said.includes(a) || a.includes(said));
    }
    case "ORDERING": {
      const expected = (data.correctOrder as string[]).map((n) => n.toUpperCase());
      const got = Array.isArray(userAnswer) ? (userAnswer as string[]).map((n) => String(n).toUpperCase()) : [];
      return expected.length === got.length && expected.every((n, i) => n === got[i]);
    }
    case "MATCHING": {
      const pairs = data.pairs as { left: string; right: string }[];
      const got = Array.isArray(userAnswer) ? (userAnswer as { left: string; right: string }[]) : [];
      if (got.length !== pairs.length) return false;
      return pairs.every((p) =>
        got.some((g) => normalizeText(g.left) === normalizeText(p.left) && normalizeText(g.right) === normalizeText(p.right))
      );
    }
    default:
      return false;
  }
}

/** Quita del payload los campos que revelarian la respuesta correcta antes de enviarlo al cliente. */
export function sanitizeExerciseData(type: ExerciseType, data: any) {
  const clone = { ...data };
  switch (type) {
    case "NOTE_NAME":
    case "THEORY_MCQ":
      delete clone.correctAnswer;
      break;
    case "EAR_TRAINING":
    case "INTERVAL":
    case "CHORD":
      delete clone.answer;
      break;
    case "WRITE_ANSWER":
      delete clone.correctAnswer;
      delete clone.acceptableAnswers;
      break;
    case "SPEAK_ALOUD":
      delete clone.expectedAnswer;
      delete clone.acceptableAnswers;
      break;
    case "ORDERING":
      delete clone.correctOrder;
      break;
    case "MATCHING": {
      // no enviar los pares ya emparejados: el cliente recibe las dos columnas
      // por separado (la derecha mezclada) y el alumno debe reconstruir la relacion.
      const pairs = clone.pairs as { left: string; right: string }[];
      delete clone.pairs;
      clone.leftItems = pairs.map((p) => p.left);
      clone.rightItems = shuffle(pairs.map((p) => p.right));
      break;
    }
    default:
      break;
  }
  return clone;
}

export function starsForScore(pctCorrect: number): number {
  if (pctCorrect >= 1) return 3;
  if (pctCorrect >= 0.7) return 2;
  if (pctCorrect >= 0.4) return 1;
  return 0;
}
