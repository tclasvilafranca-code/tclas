import { useState } from "react";
import type { Exercise } from "../lib/api";
import { StaffView } from "../components/StaffView";

interface Props {
  exercise: Exercise;
  onSubmit: (answer: string) => void;
  feedback: { correct: boolean; explanation: string; correctAnswer?: unknown } | null;
}

export function FillBlankExercise({ exercise, onSubmit, feedback }: Props) {
  const { clef, notesBefore, notesAfter, options } = exercise.data as {
    clef: "treble" | "bass";
    notesBefore: string[];
    notesAfter: string[];
    options: string[];
  };
  const [selected, setSelected] = useState<string | null>(null);

  function choose(opt: string) {
    if (selected || feedback) return;
    setSelected(opt);
    onSubmit(opt);
  }

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-4">{exercise.prompt}</p>
      <div className="flex items-center justify-center gap-1 mb-6 flex-wrap">
        {notesBefore.length > 0 && <StaffView clef={clef} notes={notesBefore} />}
        <div className="w-12 h-12 rounded-full border-2 border-dashed border-tclas-gold flex items-center justify-center text-tclas-gold font-bold text-xl shrink-0">
          ?
        </div>
        {notesAfter.length > 0 && <StaffView clef={clef} notes={notesAfter} />}
      </div>
      <div className="grid grid-cols-1 gap-2 max-w-sm mx-auto">
        {options.map((opt) => {
          const isSelected = selected === opt;
          const isCorrectAnswer = !!feedback && !feedback.correct && typeof feedback.correctAnswer !== "object" && String(feedback.correctAnswer).toLowerCase() === opt.toLowerCase();
          const showCorrect = (feedback && isSelected && feedback.correct) || isCorrectAnswer;
          const showWrong = feedback && isSelected && !feedback.correct;
          return (
            <button
              key={opt}
              onClick={() => choose(opt)}
              disabled={!!selected || !!feedback}
              className={`rounded-xl border-2 py-3 px-4 font-semibold transition-colors
                ${showCorrect ? "border-tclas-sage bg-tclas-sage/15" : showWrong ? "border-tclas-rose bg-tclas-rose/15" : "border-tclas-ink/15 hover:border-tclas-gold hover:bg-tclas-gold/10"}
                ${feedback && !isSelected && !showCorrect ? "opacity-40" : ""}`}
            >
              {opt}
            </button>
          );
        })}
      </div>
      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
