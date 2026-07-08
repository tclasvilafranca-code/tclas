import { useRef, useState } from "react";
import type { PointerEvent } from "react";
import type { Exercise } from "../lib/api";
import { playNote } from "../lib/audio";
import { toSolfege } from "../lib/notes";

interface Props {
  exercise: Exercise;
  onSubmit: (answer: { note: string; heldMs: number }) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

export function HoldNoteExercise({ exercise, onSubmit, feedback }: Props) {
  const { note, beats, bpm } = exercise.data as { note: string; beats: number; bpm: number };
  const requiredMs = beats * (60000 / bpm);
  const [holding, setHolding] = useState(false);
  const [progress, setProgress] = useState(0);
  const [releasedEarly, setReleasedEarly] = useState(false);
  const startRef = useRef(0);
  const rafRef = useRef<number>();
  const submitted = !!feedback;

  function tick() {
    const elapsed = performance.now() - startRef.current;
    const pct = Math.min(1, elapsed / requiredMs);
    setProgress(pct);
    if (pct < 1) rafRef.current = requestAnimationFrame(tick);
  }

  function start(e: PointerEvent) {
    e.preventDefault();
    if (submitted) return;
    setReleasedEarly(false);
    setHolding(true);
    startRef.current = performance.now();
    playNote(note, (requiredMs / 1000) * 1.15);
    tick();
  }

  function release() {
    if (!holding || submitted) return;
    setHolding(false);
    if (rafRef.current) cancelAnimationFrame(rafRef.current);
    const heldMs = performance.now() - startRef.current;
    if (heldMs < requiredMs * 0.5) {
      setReleasedEarly(true);
      setProgress(0);
      return;
    }
    onSubmit({ note, heldMs });
  }

  const circumference = 2 * Math.PI * 44;
  const color = feedback ? (feedback.correct ? "#6f8a6e" : "#c65b6c") : "#d4a94c";

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-2">{exercise.prompt}</p>
      <p className="text-sm text-tclas-ink/60 mb-6">
        Nota: <strong className="text-tclas-plum">{toSolfege(note)}</strong> · mantén {beats} tiempo{beats === 1 ? "" : "s"}
      </p>

      <div className="relative w-40 h-40 mx-auto mb-4">
        <svg viewBox="0 0 100 100" className="w-full h-full -rotate-90">
          <circle cx="50" cy="50" r="44" fill="none" stroke="currentColor" className="text-tclas-ink/10" strokeWidth="8" />
          <circle
            cx="50"
            cy="50"
            r="44"
            fill="none"
            stroke={color}
            strokeWidth="8"
            strokeDasharray={circumference}
            strokeDashoffset={circumference * (1 - progress)}
            strokeLinecap="round"
            style={{ transition: holding ? "none" : "stroke-dashoffset 0.15s ease" }}
          />
        </svg>
        <button
          onPointerDown={start}
          onPointerUp={release}
          onPointerLeave={release}
          disabled={submitted}
          className={`absolute inset-3 rounded-full font-bold text-base transition-colors select-none touch-none
            ${holding ? "bg-tclas-gold text-tclas-ink" : "bg-tclas-plum text-tclas-cream hover:bg-tclas-plum-light"}`}
        >
          {holding ? "Mantén..." : "Mantén pulsado"}
        </button>
      </div>

      {releasedEarly && <p className="text-xs text-tclas-rose mt-2">Has soltado demasiado pronto. ¡Intentalo otra vez!</p>}
      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
