import {
  ExerciseType,
  NoteNameData,
  StaffReadingData,
  RhythmTapData,
  EarTrainingData,
  TheoryMcqData,
  KeyboardPlayData,
  IntervalData,
  ChordData,
} from "../types";

export interface ExerciseDef {
  type: ExerciseType;
  prompt: string;
  data: NoteNameData | StaffReadingData | RhythmTapData | EarTrainingData | TheoryMcqData | KeyboardPlayData | IntervalData | ChordData;
  explanation: string;
}

export interface LessonDef {
  title: string;
  description: string;
  xpReward?: number;
  exercises: ExerciseDef[];
}

export interface UnitDef {
  title: string;
  description: string;
  lessons: LessonDef[];
}

export interface LevelDef {
  title: string;
  description: string;
  iconEmoji?: string;
  units: UnitDef[];
}

export interface TrackDef {
  code: string;
  name: string;
  description: string;
  minAge: number;
  maxAge: number;
  order: number;
  levels: LevelDef[];
}

// --- Helpers para construir el "data" de cada tipo de ejercicio ---

export const nn = (clef: "treble" | "bass", note: string, options: string[], correctAnswer: string): NoteNameData => ({
  clef,
  note,
  options,
  correctAnswer,
});

export const sr = (clef: "treble" | "bass", notes: string[]): StaffReadingData => ({ clef, notes });

export const rt = (bpm: number, pattern: number[], timeSignature = "4/4"): RhythmTapData => ({
  bpm,
  pattern,
  timeSignature,
});

export const et = (kind: "note" | "interval" | "chord", answer: string, options: string[], playNotes: string[]): EarTrainingData => ({
  kind,
  answer,
  options,
  playNotes,
});

export const mcq = (question: string, options: string[], correctAnswer: string): TheoryMcqData => ({
  question,
  options,
  correctAnswer,
});

export const kp = (notes: string[], clef: "treble" | "bass" = "treble", tempo = 90): KeyboardPlayData => ({
  notes,
  clef,
  tempo,
});

export const iv = (rootNote: string, answer: string, options: string[]): IntervalData => ({ rootNote, answer, options });

export const ch = (rootNote: string, chordNotes: string[], answer: string, options: string[]): ChordData => ({
  rootNote,
  chordNotes,
  answer,
  options,
});
