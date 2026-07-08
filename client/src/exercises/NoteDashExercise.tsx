import { useEffect, useMemo, useRef, useState } from "react";
import type { Exercise } from "../lib/api";
import { StaffView } from "../components/StaffView";
import { PianoKeyboard } from "../components/PianoKeyboard";
import { noteToMidi, midiToNoteName } from "../lib/notes";
import { playErrorBuzz } from "../lib/audio";

interface Props {
  exercise: Exercise;
  onSubmit: (playedNotes: string[]) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

export function NoteDashExercise({ exercise, onSubmit, feedback }: Props) {
  const { clef, notes, timeLimitSec } = exercise.data as { clef: "treble" | "bass"; notes: string[]; timeLimitSec: number };
  const [cursor, setCursor] = useState(0);
  const [progress, setProgress] = useState<("pending" | "correct" | "wrong")[]>(() => notes.map(() => "pending"));
  const [started, setStarted] = useState(false);
  const [timeLeft, setTimeLeft] = useState(timeLimitSec);
  const submittedRef = useRef(false);
  const done = cursor >= notes.length;

  useEffect(() => {
    if (!started || feedback || submittedRef.current) return;
    if (timeLeft <= 0) {
      submittedRef.current = true;
      onSubmit(notes.slice(0, cursor));
      return;
    }
    const t = setTimeout(() => setTimeLeft((s) => Math.max(0, s - 0.1)), 100);
    return () => clearTimeout(t);
  }, [started, timeLeft, feedback]);

  const { from, to } = useMemo(() => {
    const midis = notes.map(noteToMidi);
    const lowest = Math.min(...midis) - 3;
    const highest = Math.max(...midis) + 3;
    const clamp = (m: number) => Math.max(24, Math.min(96, m));
    return { from: midiToNoteName(clamp(lowest)), to: midiToNoteName(clamp(highest)) };
  }, [notes]);

  function handlePlay(note: string) {
    if (done || feedback || !started) return;
    if (note === notes[cursor]) {
      setProgress((p) => {
        const c = [...p];
        c[cursor] = "correct";
        return c;
      });
      const next = cursor + 1;
      setCursor(next);
      if (next >= notes.length) {
        submittedRef.current = true;
        onSubmit(notes);
      }
    } else {
      playErrorBuzz();
      setProgress((p) => {
        const c = [...p];
        c[cursor] = "wrong";
        return c;
      });
      setTimeout(
        () =>
          setProgress((p) => {
            const c = [...p];
            if (c[cursor] === "wrong") c[cursor] = "pending";
            return c;
          }),
        250
      );
    }
  }

  const pct = Math.max(0, timeLeft / timeLimitSec);
  const barColor = pct > 0.5 ? "bg-tclas-sage" : pct > 0.2 ? "bg-tclas-gold" : "bg-tclas-rose";

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-2">{exercise.prompt}</p>

      {!started ? (
        <button
          onClick={() => setStarted(true)}
          className="btn-push bg-tclas-plum border-tclas-plum-shadow text-tclas-cream rounded-2xl px-6 py-3 font-bold uppercase tracking-wide text-sm mb-6"
        >
          ▶ Empezar el reto
        </button>
      ) : (
        <div className="max-w-sm mx-auto mb-4">
          <div className="h-2.5 bg-tclas-ink/10 rounded-full overflow-hidden">
            <div className={`h-full ${barColor}`} style={{ width: `${pct * 100}%`, transition: "width 100ms linear" }} />
          </div>
          <p className="text-xs text-tclas-ink/40 mt-1 font-mono tabular-nums">{Math.ceil(timeLeft)}s</p>
        </div>
      )}

      <div className="mb-6 overflow-x-auto">
        <StaffView clef={clef} notes={notes} activeIndex={done || !started ? undefined : cursor} correctness={progress} />
      </div>

      {started && <PianoKeyboard from={from} to={to} onPlay={handlePlay} highlightNotes={done || feedback ? [] : [notes[cursor]]} />}

      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
