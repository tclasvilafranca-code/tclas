import { useState } from "react";
import type { Exercise } from "../lib/api";

interface Props {
  exercise: Exercise;
  onSubmit: (answer: string) => void;
  feedback: { correct: boolean; explanation: string; correctAnswer?: unknown } | null;
}

export function WriteAnswerExercise({ exercise, onSubmit, feedback }: Props) {
  const [value, setValue] = useState("");
  const [submitted, setSubmitted] = useState(false);

  function submit() {
    if (!value.trim() || submitted || feedback) return;
    setSubmitted(true);
    onSubmit(value);
  }

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-2">{exercise.prompt}</p>
      <p className="text-sm text-tclas-ink/60 mb-4">{exercise.data.question}</p>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          submit();
        }}
        className="flex gap-2 justify-center max-w-sm mx-auto"
      >
        <input
          autoFocus
          disabled={submitted || !!feedback}
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder={exercise.data.placeholder ?? "Escribe tu respuesta"}
          className={`flex-1 border-2 rounded-xl px-4 py-3 text-center font-semibold outline-none
            ${feedback ? (feedback.correct ? "border-tclas-sage bg-tclas-sage/10" : "border-tclas-rose bg-tclas-rose/10") : "border-tclas-ink/20 focus:border-tclas-gold"}`}
        />
        {!submitted && !feedback && (
          <button type="submit" className="bg-tclas-plum text-tclas-cream rounded-xl px-5 font-semibold hover:bg-tclas-plum-light">
            Enviar
          </button>
        )}
      </form>
      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
