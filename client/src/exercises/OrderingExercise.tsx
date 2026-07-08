import { useState } from "react";
import type { Exercise } from "../lib/api";
import { StaffView } from "../components/StaffView";
import { playNote } from "../lib/audio";

interface Props {
  exercise: Exercise;
  onSubmit: (order: string[]) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

export function OrderingExercise({ exercise, onSubmit, feedback }: Props) {
  const shuffled: string[] = exercise.data.shuffledNotes;
  const clef = exercise.data.clef ?? "treble";
  const [placed, setPlaced] = useState<number[]>([]); // indices into `shuffled`, in chosen order
  const submitted = placed.length === shuffled.length;

  function place(idx: number) {
    if (feedback || placed.includes(idx) || submitted) return;
    playNote(shuffled[idx], 0.35);
    const next = [...placed, idx];
    setPlaced(next);
    if (next.length === shuffled.length) {
      onSubmit(next.map((i) => shuffled[i]));
    }
  }

  function removeLast() {
    if (feedback) return;
    setPlaced((p) => p.slice(0, -1));
  }

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-4">{exercise.prompt}</p>

      <div className="mb-6 min-h-[100px] flex items-center justify-center">
        {placed.length > 0 ? (
          <StaffView clef={clef} notes={placed.map((i) => shuffled[i])} />
        ) : (
          <p className="text-tclas-ink/40 text-sm">Toca las notas de abajo en el orden que creas correcto</p>
        )}
      </div>

      <div className="flex flex-wrap gap-2 justify-center max-w-md mx-auto">
        {shuffled.map((note, idx) => (
          <button
            key={idx}
            onClick={() => place(idx)}
            disabled={placed.includes(idx) || !!feedback}
            className={`rounded-full border-2 w-14 h-14 font-semibold transition-colors
              ${placed.includes(idx) ? "opacity-30 border-tclas-ink/10" : "border-tclas-plum text-tclas-plum hover:bg-tclas-plum/10"}`}
          >
            {note}
          </button>
        ))}
      </div>

      {placed.length > 0 && !submitted && (
        <button onClick={removeLast} className="text-xs text-tclas-ink/50 mt-3 underline">
          Deshacer ultima
        </button>
      )}

      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
