export type Role = "STUDENT" | "TEACHER";
export type AgeGroup = "KIDS" | "TEENS" | "ADULTS";
export type ProgressStatus = "LOCKED" | "SCHEDULED" | "AVAILABLE" | "COMPLETED";
export type RepertoireStatus = "UPCOMING" | "ACTIVE" | "COMPLETED";
export type ExercisePhase = "WARMUP" | "PRACTICE" | "PERFORMANCE";

export type ExerciseType =
  | "NOTE_NAME" // identificar el nombre de una nota en el pentagrama
  | "STAFF_READING" // leer y tocar una nota/secuencia en el pentagrama
  | "RHYTHM_TAP" // reproducir un patron ritmico tocando en tiempo
  | "EAR_TRAINING" // reconocer por oido una nota/intervalo/acorde
  | "THEORY_MCQ" // pregunta de teoria de opcion multiple
  | "KEYBOARD_PLAY" // tocar una secuencia de notas en el teclado (virtual o MIDI)
  | "INTERVAL" // identificar/tocar un intervalo
  | "CHORD" // identificar/tocar un acorde
  | "WRITE_ANSWER" // escribir la respuesta (nombre de nota, acorde...) con el teclado del ordenador
  | "MATCHING" // relacionar pares (notas <-> nombres, ritmos <-> valores...)
  | "ORDERING" // ordenar una secuencia desordenada (notas de una melodia)
  | "SPEAK_ALOUD"; // decir la respuesta en voz alta (Web Speech API, con opcion de omitir)

// --- Formas del campo Exercise.data (JSON serializado) segun el tipo ---

export interface NoteNameData {
  clef: "treble" | "bass";
  note: string; // p.ej. "C4"
  options: string[];
  correctAnswer: string;
}

export interface StaffReadingData {
  clef: "treble" | "bass";
  notes: string[]; // secuencia a tocar, p.ej. ["C4","D4","E4"]
}

export interface RhythmTapData {
  bpm: number;
  pattern: number[]; // duraciones relativas, 1 = negra
  timeSignature: string; // "4/4"
}

export interface EarTrainingData {
  kind: "note" | "interval" | "chord";
  answer: string;
  options: string[];
  playNotes: string[];
}

export interface TheoryMcqData {
  question: string;
  options: string[];
  correctAnswer: string;
}

export interface KeyboardPlayData {
  notes: string[];
  clef?: "treble" | "bass";
  tempo?: number;
}

export interface IntervalData {
  rootNote: string;
  answer: string;
  options: string[];
}

export interface ChordData {
  rootNote: string;
  chordNotes: string[];
  answer: string;
  options: string[];
}

export interface WriteAnswerData {
  question: string;
  correctAnswer: string; // comparacion normalizada (mayusculas, sin acentos/espacios extra)
  acceptableAnswers?: string[]; // alternativas validas (sinonimos, con/sin tilde...)
  placeholder?: string;
}

export interface MatchingPair {
  left: string;
  right: string;
}
export interface MatchingData {
  pairs: MatchingPair[]; // se mezclan ambas columnas en el cliente
}

export interface OrderingData {
  clef?: "treble" | "bass";
  shuffledNotes: string[]; // notas ya desordenadas, a colocar en el orden correcto
  correctOrder: string[]; // el orden correcto real (misma longitud/multiset)
}

export interface SpeakAloudData {
  promptNote?: string; // nota a nombrar en voz alta, si aplica
  expectedAnswer: string;
  acceptableAnswers?: string[];
}

// --- Contenido musical estructurado de una pieza real (biblioteca Piece) ---
export interface PieceContent {
  clef: "treble" | "bass" | "grand";
  melody: string[]; // extracto representativo (frase inicial) de la mano derecha
  melodyRhythm: number[]; // duraciones relativas de esa misma frase
  bass?: string[]; // extracto de la mano izquierda, si la pieza usa ambas manos
  bassRhythm?: number[];
  chordsUsed?: string[]; // acordes que aparecen en la pieza (cifrado americano)
  featuredNotes: string[]; // notas destacadas para practicar (lectura/oido)
  lyricsHook?: string; // primera frase de la letra, si tiene (para dar contexto)
  isDuet?: boolean; // piezas a 4 manos (profesor/familia + alumno)
}
