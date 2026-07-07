import { useMemo, useState } from "react";
import type { Exercise } from "../lib/api";
import { StaffView } from "../components/StaffView";
import { PianoKeyboard } from "../components/PianoKeyboard";
import { playErrorBuzz } from "../lib/audio";
import { noteToMidi } from "../lib/notes";

interface Props {
  exercise: Exercise;
  onSubmit: (playedNotes: string[]) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

export function SequenceExercise({ exercise, onSubmit, feedback }: Props) {
  const { type, data, prompt } = exercise;
  const targetNotes: string[] = data.notes;
  const [progress, setProgress] = useState<("pending" | "correct" | "wrong")[]>(targetNotes.map(() => "pending"));
  const [cursor, setCursor] = useState(0);
  const [mistakes, setMistakes] = useState(0);
  const done = cursor >= targetNotes.length;

  const { from, to } = useMemo(() => {
    const midis = targetNotes.map(noteToMidi);
    const lowest = Math.min(...midis) - 3;
    const highest = Math.max(...midis) + 3;
    const clamp = (m: number) => Math.max(24, Math.min(96, m));
    const toName = (m: number) => {
      const names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
      return `${names[m % 12]}${Math.floor(m / 12) - 1}`;
    };
    return { from: toName(clamp(lowest)), to: toName(clamp(highest)) };
  }, [targetNotes]);

  function handlePlay(note: string) {
    if (done || feedback) return;
    const expected = targetNotes[cursor];
    if (note === expected) {
      const next = [...progress];
      next[cursor] = "correct";
      setProgress(next);
      const newCursor = cursor + 1;
      setCursor(newCursor);
      if (newCursor >= targetNotes.length) {
        onSubmit(targetNotes);
      }
    } else {
      playErrorBuzz();
      setMistakes((m) => m + 1);
      const next = [...progress];
      next[cursor] = "wrong";
      setProgress(next);
      setTimeout(() => setProgress((p) => { const c = [...p]; if (c[cursor] === "wrong") c[cursor] = "pending"; return c; }), 300);
    }
  }

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-4">{prompt}</p>
      <div className="mb-6">
        <StaffView clef={data.clef ?? "treble"} notes={targetNotes} activeIndex={done ? undefined : cursor} correctness={progress} />
      </div>
      <PianoKeyboard from={from} to={to} onPlay={handlePlay} highlightNotes={done || feedback ? [] : [targetNotes[cursor]]} />
      {type === "KEYBOARD_PLAY" && !done && (
        <p className="text-xs text-tclas-ink/50 mt-2">Toca la nota resaltada en color dorado.</p>
      )}
      {mistakes > 0 && !done && <p className="text-xs text-tclas-rose mt-2">Intentos fallidos: {mistakes}. ¡Sigue intentando!</p>}
      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
