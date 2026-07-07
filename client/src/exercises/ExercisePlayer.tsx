import type { Exercise } from "../lib/api";
import { McqLikeExercise } from "./McqLikeExercise";
import { SequenceExercise } from "./SequenceExercise";
import { RhythmExercise } from "./RhythmExercise";

interface Props {
  exercise: Exercise;
  onSubmit: (answer: unknown) => void;
  feedback: { correct: boolean; explanation: string; correctAnswer?: unknown } | null;
}

export function ExercisePlayer({ exercise, onSubmit, feedback }: Props) {
  switch (exercise.type) {
    case "STAFF_READING":
    case "KEYBOARD_PLAY":
      return <SequenceExercise exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "RHYTHM_TAP":
      return <RhythmExercise exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    default:
      return <McqLikeExercise exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
  }
}
