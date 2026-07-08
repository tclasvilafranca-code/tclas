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

export class ApiError extends Error {
  status: number;
  data: any;
  constructor(message: string, status: number, data: any) {
    super(message);
    this.status = status;
    this.data = data;
  }
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
    throw new ApiError(data.error || `Error ${res.status}`, res.status, data);
  }
  return data as T;
}

export const api = {
  get: <T>(path: string) => request<T>(path),
  post: <T>(path: string, body?: unknown) => request<T>(path, { method: "POST", body: body ? JSON.stringify(body) : undefined }),
  patch: <T>(path: string, body?: unknown) => request<T>(path, { method: "PATCH", body: body ? JSON.stringify(body) : undefined }),
  delete: <T>(path: string) => request<T>(path, { method: "DELETE" }),
};

// --- Tipos compartidos con el backend ---

export type Role = "STUDENT" | "TEACHER";
export type AgeGroup = "KIDS" | "TEENS" | "ADULTS";
export type ExerciseType =
  | "NOTE_NAME"
  | "STAFF_READING"
  | "RHYTHM_TAP"
  | "EAR_TRAINING"
  | "THEORY_MCQ"
  | "KEYBOARD_PLAY"
  | "INTERVAL"
  | "CHORD"
  | "WRITE_ANSWER"
  | "MATCHING"
  | "ORDERING"
  | "SPEAK_ALOUD"
  | "DRAG_STAFF"
  | "HOLD_NOTE"
  | "SCROLLING_PLAY"
  | "FILL_BLANK"
  | "EAR_BUILD"
  | "NOTE_DASH"
  | "SEGMENT_PRACTICE";

export interface StudentProfile {
  id: string;
  ageGroup: AgeGroup;
  xpTotal: number;
  heartsCurrent: number;
  heartsMax: number;
  streakCurrent: number;
  streakLongest: number;
  onboarded: boolean;
  lastActivityDate: string | null;
  heartsUpdatedAt: string;
}

export interface Me {
  id: string;
  email: string | null;
  username: string | null;
  name: string;
  role: Role;
  studentProfile: StudentProfile | null;
}

export type LessonStatus = "LOCKED" | "SCHEDULED" | "AVAILABLE" | "COMPLETED";

export interface LessonNode {
  id: string;
  weekIndex: number;
  weekNumber: number;
  scheduledDate: string;
  title: string;
  description: string;
  xpReward: number;
  status: LessonStatus;
  stars: number;
  precisionScore: number;
}

export interface PieceInfo {
  id: string;
  title: string;
  composer: string;
  iconEmoji: string;
  seasonalTag: string | null;
  keySignature: string;
  timeSignature: string;
}

export interface RepertoireNode {
  id: string;
  orderIndex: number;
  startDate: string;
  durationWeeks: number;
  teacherNote: string;
  status: "UPCOMING" | "ACTIVE" | "COMPLETED";
  completed: boolean;
  piece: PieceInfo;
  lessons: LessonNode[];
}

export interface CurriculumTree {
  pieces: RepertoireNode[];
}

export type ExercisePhase = "VISUAL_AGILITY" | "EAR_ACUITY" | "NOTE_RUSH" | "SHEET_PRACTICE";

export interface Exercise {
  id: string;
  index: number;
  type: ExerciseType;
  phase: ExercisePhase;
  prompt: string;
  data: any;
}

export interface LessonDetail {
  id: string;
  title: string;
  description: string;
  xpReward: number;
  weekIndex: number;
  weekNumber: number;
  pieceTitle: string;
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
  score: number;
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
  username: string | null;
  ageGroup: AgeGroup | null;
  xpTotal: number;
  streakCurrent: number;
  lastActivityDate: string | null;
  piecesAssigned: number;
  completedLessons: number;
  totalLessons: number;
}

export interface PieceLibraryItem {
  id: string;
  title: string;
  composer: string;
  ageGroup: AgeGroup;
  difficultyTier: number;
  defaultWeeks: number;
  keySignature: string;
  timeSignature: string;
  seasonalTag: string | null;
  iconEmoji: string;
}

export interface PieceContent {
  clef: "treble" | "bass" | "grand";
  melody: string[];
  melodyRhythm: number[];
  bass?: string[];
  bassRhythm?: number[];
  chordsUsed?: string[];
  featuredNotes: string[];
  lyricsHook?: string;
  isDuet?: boolean;
}

export interface PieceDetail {
  id: string;
  title: string;
  composer: string;
  arranger: string;
  keySignature: string;
  timeSignature: string;
  seasonalTag: string | null;
  iconEmoji: string;
  aboutText: string;
  tips: string;
  content: PieceContent;
}

export interface BulkRepertoireItem {
  pieceId: string;
  durationWeeks?: number;
  teacherNote?: string;
}

export interface NewStudentCredentials {
  id: string;
  name: string;
  username: string;
  pin: string;
  ageGroup: AgeGroup;
}
