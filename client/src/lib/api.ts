// En local, Vite hace de proxy de /api hacia el backend (ver vite.config.ts).
// En produccion, la app web y la API se despliegan por separado, asi que
// VITE_API_URL debe apuntar a la URL publica del backend (ej. https://tclas-api.onrender.com).
const API_BASE = import.meta.env.VITE_API_URL ? `${import.meta.env.VITE_API_URL}/api` : "/api";

const TOKEN_KEY = "tclas_token";

export function getToken(): string | null {
  return localStorage.getItem(TOKEN_KEY);
}
export function setToken(token: string) {
  localStorage.setItem(TOKEN_KEY, token);
}
export function clearToken() {
  localStorage.removeItem(TOKEN_KEY);
}

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const token = getToken();
  const res = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(data.error || `Error ${res.status}`);
  }
  return data as T;
}

export const api = {
  get: <T>(path: string) => request<T>(path),
  post: <T>(path: string, body?: unknown) => request<T>(path, { method: "POST", body: body ? JSON.stringify(body) : undefined }),
  patch: <T>(path: string, body?: unknown) => request<T>(path, { method: "PATCH", body: body ? JSON.stringify(body) : undefined }),
};

// --- Tipos compartidos con el backend ---

export type Role = "STUDENT" | "TEACHER";
export type AgeGroup = "KIDS" | "TEENS" | "ADULTS";
export type ExerciseType = "NOTE_NAME" | "STAFF_READING" | "RHYTHM_TAP" | "EAR_TRAINING" | "THEORY_MCQ" | "KEYBOARD_PLAY" | "INTERVAL" | "CHORD";

export interface StudentProfile {
  id: string;
  ageGroup: AgeGroup;
  trackId: string | null;
  track?: Track | null;
  xpTotal: number;
  heartsCurrent: number;
  heartsMax: number;
  streakCurrent: number;
  streakLongest: number;
  onboarded: boolean;
}

export interface Me {
  id: string;
  email: string;
  name: string;
  role: Role;
  studentProfile: StudentProfile | null;
}

export interface Track {
  id: string;
  code: string;
  name: string;
  description: string;
  minAge: number;
  maxAge: number;
}

export interface LessonNode {
  id: string;
  index: number;
  title: string;
  description: string;
  xpReward: number;
  status: "LOCKED" | "AVAILABLE" | "COMPLETED";
  stars: number;
}

export interface UnitNode {
  id: string;
  index: number;
  title: string;
  description: string;
  completed: boolean;
  lessons: LessonNode[];
}

export interface LevelNode {
  id: string;
  index: number;
  title: string;
  description: string;
  iconEmoji: string;
  completed: boolean;
  units: UnitNode[];
}

export interface CurriculumTree {
  id: string;
  code: string;
  name: string;
  description: string;
  levels: LevelNode[];
}

export interface Exercise {
  id: string;
  index: number;
  type: ExerciseType;
  prompt: string;
  data: any;
}

export interface LessonDetail {
  id: string;
  title: string;
  description: string;
  xpReward: number;
  unitTitle: string;
  levelTitle: string;
  exercises: Exercise[];
}

export interface AttemptResult {
  correct: boolean;
  explanation: string;
  correctAnswer?: unknown;
  heartsCurrent?: number;
}

export interface CompleteLessonResult {
  progress: unknown;
  stars: number;
  xpAwarded: number;
  profile: StudentProfile;
  newBadges: { code: string; name: string; icon: string }[];
}

export interface Badge {
  code: string;
  name: string;
  description: string;
  icon: string;
  earnedAt: string;
}

export interface StudentSummary {
  id: string;
  name: string;
  email: string;
  ageGroup: AgeGroup | null;
  trackName: string | null;
  xpTotal: number;
  streakCurrent: number;
  lastActivityDate: string | null;
  onboarded: boolean;
  completedLessons: number;
  totalLessons: number;
}

export interface Assignment {
  id: string;
  teacherId: string;
  studentId: string;
  lessonId: string | null;
  lesson?: { id: string; title: string } | null;
  classDate: string;
  note: string;
  status: "PENDING" | "DONE";
}
