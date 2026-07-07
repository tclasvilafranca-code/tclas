export type Role = "STUDENT" | "TEACHER";
export type AgeGroup = "KIDS" | "TEENS" | "ADULTS";
export type ProgressStatus = "LOCKED" | "AVAILABLE" | "COMPLETED";
export type AssignmentStatus = "PENDING" | "DONE";

export type ExerciseType =
  | "NOTE_NAME" // identificar el nombre de una nota en el pentagrama
  | "STAFF_READING" // leer y tocar una nota/secuencia en el pentagrama
  | "RHYTHM_TAP" // reproducir un patron ritmico tocando en tiempo
  | "EAR_TRAINING" // reconocer por oido una nota/intervalo/acorde
  | "THEORY_MCQ" // pregunta de teoria de opcion multiple
  | "KEYBOARD_PLAY" // tocar una secuencia de notas en el teclado (virtual o MIDI)
  | "INTERVAL" // identificar/tocar un intervalo
  | "CHORD"; // identificar/tocar un acorde

// Formas del campo Exercise.data (JSON serializado) segun el tipo.
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
