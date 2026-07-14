const API_BASE = import.meta.env.VITE_API_URL ?? "";

export class ApiError extends Error {
  status: number;
  upgradeRequired?: boolean;
  constructor(message: string, status: number, upgradeRequired?: boolean) {
    super(message);
    this.status = status;
    this.upgradeRequired = upgradeRequired;
  }
}

/** Emitido cuando una petición autenticada recibe 401: la sesión ya no es válida
 * (token caducado, o invalidado por un cambio de contraseña en otro dispositivo). */
export const SESSION_EXPIRED_EVENT = "teorico48:session-expired";

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const token = localStorage.getItem("token");
  const res = await fetch(`${API_BASE}/api${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...(options.headers ?? {}),
    },
  });

  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    if (res.status === 401 && token) {
      localStorage.removeItem("token");
      window.dispatchEvent(new Event(SESSION_EXPIRED_EVENT));
    }
    throw new ApiError(data.error ?? "Error de red", res.status, data.upgradeRequired);
  }
  return data as T;
}

export const api = {
  register: (email: string, password: string, acceptedTerms: boolean, accessCode: string) =>
    request<{ token: string; user: User }>("/auth/register", {
      method: "POST",
      body: JSON.stringify({ email, password, acceptedTerms, accessCode }),
    }),
  login: (email: string, password: string) =>
    request<{ token: string; user: User }>("/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    }),
  forgotPassword: (email: string) =>
    request<{ message: string }>("/auth/forgot-password", {
      method: "POST",
      body: JSON.stringify({ email }),
    }),
  resetPassword: (userId: string, token: string, newPassword: string) =>
    request<{ message: string }>("/auth/reset-password", {
      method: "POST",
      body: JSON.stringify({ userId, token, newPassword }),
    }),
  verifyEmail: (userId: string, token: string) =>
    request<{ message: string }>("/auth/verify-email", {
      method: "POST",
      body: JSON.stringify({ userId, token }),
    }),
  resendVerification: () =>
    request<{ message: string }>("/auth/resend-verification", { method: "POST" }),
  me: () => request<{ user: User }>("/auth/me"),
  setExamDate: (examDate: string | null) =>
    request<{ user: User }>("/auth/me/exam-date", {
      method: "PUT",
      body: JSON.stringify({ examDate }),
    }),
  categories: () => request<{ categories: Category[] }>("/tests/categories"),
  categoryStats: () => request<{ categories: CategoryStat[] }>("/tests/category-stats"),
  startExam: () => request<{ attemptId: string; questions: Question[] }>("/tests/exam", { method: "POST" }),
  startReview: () => request<{ attemptId: string; questions: Question[] }>("/tests/review", { method: "POST" }),
  startLearn: (categorySlug?: string) =>
    request<{ attemptId: string; questions: LearnQuestion[] }>("/tests/learn", {
      method: "POST",
      body: JSON.stringify(categorySlug ? { categorySlug } : {}),
    }),
  submitAttempt: (attemptId: string, answers: { questionId: string; selectedIndex: number | null }[]) =>
    request<SubmitResult>(`/tests/${attemptId}/submit`, {
      method: "POST",
      body: JSON.stringify({ answers }),
    }),
  history: () => request<{ attempts: Attempt[] }>("/tests/history"),
  stats: () => request<Stats>("/tests/stats"),
  checkout: () => request<{ url: string }>("/payments/checkout", { method: "POST" }),
  checkoutLicense: () => request<{ url: string }>("/payments/checkout-license", { method: "POST" }),
  completeTheorySession: (sessionId: string) =>
    request<CompleteTheorySessionResult>("/theory/complete-session", {
      method: "POST",
      body: JSON.stringify({ sessionId }),
    }),
};

export interface User {
  id: string;
  email: string;
  examDate: string | null;
  isPremium: boolean;
  xp: number;
  level: number;
  currentStreak: number;
  longestStreak: number;
  emailVerified: boolean;
  theoryCompletedSessions: string[];
}

export interface CompleteTheorySessionResult {
  alreadyCompleted: boolean;
  xpGained: number;
  totalXp: number;
  level: number;
  leveledUp?: boolean;
  theoryCompletedSessions: string[];
  newBadges: { id: string; label: string; emoji: string }[];
}

export interface Badge {
  id: string;
  label: string;
  emoji: string;
  unlocked: boolean;
}

export interface Stats {
  xp: number;
  level: number;
  currentStreak: number;
  longestStreak: number;
  totalAttempts: number;
  totalPassed: number;
  badges: Badge[];
}

export interface Category {
  id: string;
  slug: string;
  name: string;
}

export interface CategoryStat {
  slug: string;
  name: string;
  answered: number;
  correct: number;
  accuracy: number | null;
}

export interface Question {
  id: string;
  text: string;
  imageUrl: string | null;
  options: string[];
  category: string;
}

/** En modo Aprendizaje la respuesta correcta y su explicación llegan desde
 * el principio: el cliente solo las revela después de que el usuario responda. */
export interface LearnQuestion extends Question {
  correctIndex: number;
  explanation: string;
}

export interface SubmitResult {
  score: number;
  total: number;
  passed: boolean;
  results: {
    questionId: string;
    text: string;
    options: string[];
    correctIndex: number;
    selectedIndex: number | null;
    correct: boolean;
    explanation: string;
    category: string;
  }[];
  gamification: {
    xpGained: number;
    totalXp: number;
    level: number;
    leveledUp: boolean;
    currentStreak: number;
    newBadges: { id: string; label: string; emoji: string }[];
  };
  attempt: Attempt;
}

export interface Attempt {
  id: string;
  mode: "practice" | "exam" | "learn";
  startedAt: string;
  finishedAt: string | null;
  score: number | null;
  total: number | null;
  passed: boolean | null;
}
