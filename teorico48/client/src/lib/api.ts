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
    throw new ApiError(data.error ?? "Error de red", res.status, data.upgradeRequired);
  }
  return data as T;
}

export const api = {
  register: (email: string, password: string) =>
    request<{ token: string; user: User }>("/auth/register", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    }),
  login: (email: string, password: string) =>
    request<{ token: string; user: User }>("/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    }),
  me: () => request<{ user: User }>("/auth/me"),
  setExamDate: (examDate: string | null) =>
    request<{ user: User }>("/auth/me/exam-date", {
      method: "PUT",
      body: JSON.stringify({ examDate }),
    }),
  categories: () => request<{ categories: Category[] }>("/tests/categories"),
  startExam: () => request<{ attemptId: string; questions: Question[] }>("/tests/exam", { method: "POST" }),
  startReview: () => request<{ attemptId: string; questions: Question[] }>("/tests/review", { method: "POST" }),
  submitAttempt: (attemptId: string, answers: { questionId: string; selectedIndex: number | null }[]) =>
    request<SubmitResult>(`/tests/${attemptId}/submit`, {
      method: "POST",
      body: JSON.stringify({ answers }),
    }),
  history: () => request<{ attempts: Attempt[] }>("/tests/history"),
  stats: () => request<Stats>("/tests/stats"),
  checkout: () => request<{ url: string }>("/payments/checkout", { method: "POST" }),
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

export interface Question {
  id: string;
  text: string;
  imageUrl: string | null;
  options: string[];
  category: string;
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
}

export interface Attempt {
  id: string;
  mode: "practice" | "exam";
  startedAt: string;
  finishedAt: string | null;
  score: number | null;
  total: number | null;
  passed: boolean | null;
}
