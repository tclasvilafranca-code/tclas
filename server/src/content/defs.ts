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
  WriteAnswerData,
  MatchingData,
  OrderingData,
  SpeakAloudData,
  PieceContent,
  AgeGroup,
} from "../types";

export interface ExerciseDef {
  type: ExerciseType;
  prompt: string;
  data:
    | NoteNameData
    | StaffReadingData
    | RhythmTapData
    | EarTrainingData
    | TheoryMcqData
    | KeyboardPlayData
    | IntervalData
    | ChordData
    | WriteAnswerData
    | MatchingData
    | OrderingData
    | SpeakAloudData;
  explanation: string;
}

export interface LessonDef {
  title: string;
  description: string;
  xpReward?: number;
  exercises: ExerciseDef[];
}

// --- Definicion de una pieza para la biblioteca compartida (autoria de contenido) ---
export interface PieceDef {
  title: string;
  composer?: string;
  arranger?: string;
  ageGroup: AgeGroup;
  difficultyTier: number;
  defaultWeeks?: number;
  keySignature: string;
  timeSignature: string;
  seasonalTag?: string;
  iconEmoji?: string;
  content: PieceContent;
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

export const wa = (question: string, correctAnswer: string, acceptableAnswers?: string[], placeholder?: string): WriteAnswerData => ({
  question,
  correctAnswer,
  acceptableAnswers,
  placeholder,
});

export const ma = (pairs: { left: string; right: string }[]): MatchingData => ({ pairs });

export const ord = (correctOrder: string[], clef: "treble" | "bass" = "treble"): OrderingData => ({
  clef,
  correctOrder,
  shuffledNotes: shuffleArray(correctOrder),
});

export const sp = (expectedAnswer: string, acceptableAnswers?: string[], promptNote?: string): SpeakAloudData => ({
  expectedAnswer,
  acceptableAnswers,
  promptNote,
});

function shuffleArray<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  // asegurar que no salga ya ordenado por casualidad cuando hay mas de 2 elementos
  if (copy.length > 2 && copy.every((v, i) => v === arr[i])) {
    return shuffleArray(arr);
  }
  return copy;
}
