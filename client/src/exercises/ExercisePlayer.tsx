import type { Exercise } from "../lib/api";
import { McqLikeExercise } from "./McqLikeExercise";
import { SequenceExercise } from "./SequenceExercise";
import { RhythmExercise } from "./RhythmExercise";
import { WriteAnswerExercise } from "./WriteAnswerExercise";
import { MatchingExercise } from "./MatchingExercise";
import { OrderingExercise } from "./OrderingExercise";
import { SpeakAloudExercise } from "./SpeakAloudExercise";
import { DragStaffExercise } from "./DragStaffExercise";
import { HoldNoteExercise } from "./HoldNoteExercise";
import { ScrollingPlayExercise } from "./ScrollingPlayExercise";
import { FillBlankExercise } from "./FillBlankExercise";
import { EarBuildExercise } from "./EarBuildExercise";
import { NoteDashExercise } from "./NoteDashExercise";
import { SegmentPracticeExercise } from "./SegmentPracticeExercise";

interface Props {
  exercise: Exercise;
  onSubmit: (answer: unknown) => void;
  feedback: { correct: boolean; explanation: string; correctAnswer?: unknown } | null;
}

// Importante: cada ejercicio lleva key={exercise.id} para forzar que React monte
// una instancia nueva del componente al pasar de un ejercicio a otro. Sin esto,
// dos ejercicios consecutivos del mismo tipo (ej. dos de opcion multiple seguidos)
// reutilizarian la misma instancia y arrastrarian el estado local (seleccion,
// progreso...) del ejercicio anterior.
export function ExercisePlayer({ exercise, onSubmit, feedback }: Props) {
  switch (exercise.type) {
    case "STAFF_READING":
    case "KEYBOARD_PLAY":
      return <SequenceExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "RHYTHM_TAP":
      return <RhythmExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "WRITE_ANSWER":
      return <WriteAnswerExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "MATCHING":
      return <MatchingExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "ORDERING":
      return <OrderingExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "SPEAK_ALOUD":
      return <SpeakAloudExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "DRAG_STAFF":
      return <DragStaffExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "HOLD_NOTE":
      return <HoldNoteExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "SCROLLING_PLAY":
      return <ScrollingPlayExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "FILL_BLANK":
      return <FillBlankExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "EAR_BUILD":
      return <EarBuildExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "NOTE_DASH":
      return <NoteDashExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    case "SEGMENT_PRACTICE":
      return <SegmentPracticeExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
    default:
      return <McqLikeExercise key={exercise.id} exercise={exercise} onSubmit={onSubmit} feedback={feedback} />;
  }
}
