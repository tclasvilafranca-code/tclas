import { useEffect, useMemo, useRef, useState } from "react";
import type { Exercise } from "../lib/api";
import { PianoKeyboard } from "../components/PianoKeyboard";
import { noteToMidi, midiToNoteName } from "../lib/notes";
import { playErrorBuzz } from "../lib/audio";

interface Props {
  exercise: Exercise;
  onSubmit: (playedNotes: string[]) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

const MS_PER_UNIT = 550;
const HIT_X = 18;

export function ScrollingPlayExercise({ exercise, onSubmit, feedback }: Props) {
  const { notes, durations } = exercise.data as { notes: string[]; durations: number[] };
  const [cursor, setCursor] = useState(0);
  const [hit, setHit] = useState<boolean[]>(() => notes.map(() => false));
  const [running, setRunning] = useState(false);
  const [now, setNow] = useState(0);
  const startRef = useRef(0);
  const rafRef = useRef<number>();
  const done = cursor >= notes.length;

  const startTimes = useMemo(() => {
    const times: number[] = [];
    let acc = 0;
    for (const d of durations) {
      times.push(acc);
      acc += d * MS_PER_UNIT;
    }
    return times;
  }, [durations]);
  const totalMs = (startTimes[startTimes.length - 1] ?? 0) + 900;

  useEffect(() => {
    if (!running) return;
    function loop() {
      setNow(performance.now() - startRef.current);
      rafRef.current = requestAnimationFrame(loop);
    }
    rafRef.current = requestAnimationFrame(loop);
    return () => {
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
    };
  }, [running]);

  function start() {
    setRunning(true);
    startRef.current = performance.now();
  }

  const { from, to } = useMemo(() => {
    const midis = notes.map(noteToMidi);
    const lowest = Math.min(...midis) - 3;
    const highest = Math.max(...midis) + 3;
    const clamp = (m: number) => Math.max(24, Math.min(96, m));
    const toName = (m: number) => midiToNoteName(clamp(m));
    return { from: toName(lowest), to: toName(highest) };
  }, [notes]);

  function handlePlay(note: string) {
    if (done || feedback || !running) return;
    if (note === notes[cursor]) {
      setHit((h) => {
        const c = [...h];
        c[cursor] = true;
        return c;
      });
      const newCursor = cursor + 1;
      setCursor(newCursor);
      if (newCursor >= notes.length) {
        setRunning(false);
        onSubmit(notes);
      }
    } else {
      playErrorBuzz();
    }
  }

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-4">{exercise.prompt}</p>

      <div className="relative h-24 bg-tclas-ink/5 rounded-xl overflow-hidden mb-6 max-w-xl mx-auto">
        <div className="absolute top-0 bottom-0 border-l-2 border-tclas-gold z-10" style={{ left: `${HIT_X}%` }} />
        {running &&
          notes.map((n, i) => {
            if (hit[i]) return null;
            const x = HIT_X + ((startTimes[i] - now) / totalMs) * (100 - HIT_X);
            if (x < -8 || x > 104) return null;
            const isNext = i === cursor;
            return (
              <div
                key={i}
                className={`absolute top-1/2 -translate-y-1/2 w-9 h-9 rounded-full text-xs font-bold flex items-center justify-center transition-colors
                  ${isNext ? "bg-tclas-gold text-tclas-ink" : "bg-tclas-plum text-tclas-cream"}`}
                style={{ left: `${x}%` }}
              >
                {n.replace(/[0-9#b]/g, "")}
              </div>
            );
          })}
        {!running && (
          <button onClick={start} className="absolute inset-0 flex items-center justify-center bg-tclas-plum/90 text-tclas-cream font-semibold">
            {done ? "¡Hecho!" : "▶ Empezar"}
          </button>
        )}
      </div>

      <PianoKeyboard from={from} to={to} onPlay={handlePlay} highlightNotes={done || feedback || !running ? [] : [notes[cursor]]} />

      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
