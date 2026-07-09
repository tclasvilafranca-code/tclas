import { useMemo, useState } from "react";
import type { Exercise } from "../lib/api";
import { PianoKeyboard } from "../components/PianoKeyboard";
import { playNote, playErrorBuzz } from "../lib/audio";
import { noteToMidi, midiToNoteName, notesEqual } from "../lib/notes";

interface Props {
  exercise: Exercise;
  onSubmit: (notes: string[]) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

export function EarBuildExercise({ exercise, onSubmit, feedback }: Props) {
  const { notes } = exercise.data as { notes: string[] };
  const [revealed, setRevealed] = useState(1);
  const [mistakes, setMistakes] = useState(0);

  const { from, to } = useMemo(() => {
    const midis = notes.map(noteToMidi);
    const lowest = Math.min(...midis) - 4;
    const highest = Math.max(...midis) + 4;
    const clamp = (m: number) => Math.max(24, Math.min(96, m));
    return { from: midiToNoteName(clamp(lowest)), to: midiToNoteName(clamp(highest)) };
  }, [notes]);

  function listen() {
    notes.slice(0, revealed).forEach((n, i) => setTimeout(() => playNote(n, 0.5), i * 550));
  }

  function handlePlay(note: string) {
    if (feedback) return;
    const target = notes[revealed - 1];
    if (notesEqual(note, target)) {
      if (revealed >= notes.length) {
        onSubmit(notes);
      } else {
        setRevealed((r) => r + 1);
      }
    } else {
      playErrorBuzz();
      setMistakes((m) => m + 1);
    }
  }

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-2">{exercise.prompt}</p>
      <p className="text-sm text-tclas-ink/60 mb-4">
        Nota {Math.min(revealed, notes.length)} de {notes.length}
      </p>

      <button onClick={listen} className="mb-6 bg-tclas-plum text-tclas-cream rounded-full px-6 py-3 font-semibold hover:bg-tclas-plum-light">
        ▶ Escuchar{revealed > 1 ? " de nuevo" : ""}
      </button>

      <PianoKeyboard from={from} to={to} onPlay={handlePlay} highlightNotes={[]} />

      {mistakes > 0 && !feedback && <p className="text-xs text-tclas-rose mt-2">Intentos fallidos: {mistakes}. ¡Sigue escuchando con atencion!</p>}
      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
