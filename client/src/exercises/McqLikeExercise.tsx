import { useState } from "react";
import type { Exercise } from "../lib/api";
import { StaffView } from "../components/StaffView";
import { playNote } from "../lib/audio";
import { toSolfege } from "../lib/notes";

interface Props {
  exercise: Exercise;
  onSubmit: (answer: string) => void;
  feedback: { correct: boolean; explanation: string; correctAnswer?: unknown } | null;
}

export function McqLikeExercise({ exercise, onSubmit, feedback }: Props) {
  const [selected, setSelected] = useState<string | null>(null);
  const { type, data, prompt } = exercise;
  const options: string[] = data.options ?? [];

  function choose(opt: string) {
    if (selected) return;
    setSelected(opt);
    onSubmit(opt);
  }

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-4">{prompt}</p>

      {type === "NOTE_NAME" && (
        <div className="mb-4">
          <StaffView clef={data.clef} notes={[data.note]} />
        </div>
      )}

      {type === "EAR_TRAINING" && (
        <button
          onClick={() => (data.playNotes as string[]).forEach((n: string, i: number) => setTimeout(() => playNote(n, 0.7), i * 500))}
          className="mb-4 bg-tclas-plum text-tclas-cream rounded-full px-5 py-2 font-semibold hover:bg-tclas-plum-light"
        >
          ▶ Escuchar
        </button>
      )}

      {(type === "INTERVAL" || type === "CHORD") && (
        <div className="mb-4 flex flex-col items-center gap-2">
          <StaffView clef="treble" notes={type === "CHORD" ? data.chordNotes : [data.rootNote]} />
          <button
            onClick={() => (type === "CHORD" ? data.chordNotes : [data.rootNote, data.rootNote]).forEach((n: string, i: number) => setTimeout(() => playNote(n, 0.7), i * 400))}
            className="bg-tclas-plum text-tclas-cream rounded-full px-5 py-2 font-semibold hover:bg-tclas-plum-light text-sm"
          >
            ▶ Escuchar
          </button>
        </div>
      )}

      <div className="grid gap-2 max-w-sm mx-auto">
        {options.map((opt) => {
          const isSelected = selected === opt;
          const showCorrect = feedback && isSelected && feedback.correct;
          const showWrong = feedback && isSelected && !feedback.correct;
          return (
            <button
              key={opt}
              onClick={() => choose(opt)}
              disabled={!!selected}
              className={`rounded-xl border-2 py-3 px-4 font-semibold transition-colors
                ${showCorrect ? "border-tclas-sage bg-tclas-sage/15" : showWrong ? "border-tclas-rose bg-tclas-rose/15" : "border-tclas-ink/15 hover:border-tclas-gold hover:bg-tclas-gold/10"}
                ${selected && !isSelected ? "opacity-40" : ""}`}
            >
              {opt}
            </button>
          );
        })}
      </div>

      {type === "NOTE_NAME" && feedback && (
        <p className="text-xs text-tclas-ink/40 mt-3">En solfeo, esta nota se dice "{toSolfege(data.note)}"</p>
      )}

      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
