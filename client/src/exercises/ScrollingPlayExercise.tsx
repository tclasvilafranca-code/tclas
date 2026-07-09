import { useEffect, useMemo, useRef, useState } from "react";
import type { Exercise } from "../lib/api";
import { PianoKeyboard } from "../components/PianoKeyboard";
import type { FallingNote } from "../components/PianoKeyboard";
import { ListenButton } from "../components/ListenButton";
import { noteToMidi, midiToNoteName, notesEqual } from "../lib/notes";
import { playErrorBuzz } from "../lib/audio";

interface Props {
  exercise: Exercise;
  onSubmit: (playedNotes: string[]) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

const MS_PER_UNIT = 550;
// Cuanto antes de su turno aparece una nota cayendo (mas alto en el carril).
// Si se retrasa (el alumno va mas lento que el tempo de referencia), se queda
// "aparcada" justo encima de su tecla en vez de seguir cayendo, esperando a
// que le toque el turno: el juego nunca es contra-reloj, solo marca el ritmo.
const LOOKAHEAD_MS = 1700;
const LANE_HEIGHT = 190;
const STACK_OFFSET_PX = 26;

export function ScrollingPlayExercise({ exercise, onSubmit, feedback }: Props) {
  const { notes, durations, bpm } = exercise.data as { notes: string[]; durations: number[]; bpm: number };
  const [cursor, setCursor] = useState(0);
  const [running, setRunning] = useState(false);
  const [now, setNow] = useState(0);
  const startRef = useRef(0);
  const rafRef = useRef<number | undefined>(undefined);
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
    if (notesEqual(note, notes[cursor])) {
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

  const fallingNotes: FallingNote[] = useMemo(() => {
    if (!running) return [];
    const list: FallingNote[] = [];
    // Si dos notas seguidas comparten la misma tecla y ambas ya estan "aparcadas"
    // en la linea (el alumno va mas lento que el tempo), se apilan una encima de
    // otra en vez de superponerse exactamente: si no, la nota realmente siguiente
    // (isNext, en dorado) quedaria tapada por su propia repeticion futura.
    const parkedCountByMidi = new Map<number, number>();
    for (let i = cursor; i < notes.length; i++) {
      const timeUntilHit = startTimes[i] - now;
      if (timeUntilHit > LOOKAHEAD_MS) break; // las siguientes estan aun mas lejos en el tiempo
      let progress = 1 - timeUntilHit / LOOKAHEAD_MS;
      if (progress >= 1) {
        const midi = noteToMidi(notes[i]);
        const stack = parkedCountByMidi.get(midi) ?? 0;
        parkedCountByMidi.set(midi, stack + 1);
        progress = 1 - (stack * STACK_OFFSET_PX) / LANE_HEIGHT;
      }
      list.push({ id: i, note: notes[i], progress, isNext: i === cursor });
    }
    return list;
  }, [running, cursor, notes, startTimes, now]);

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-3">{exercise.prompt}</p>
      {!running && (
        <div className="flex justify-center mb-3">
          <ListenButton notes={notes} rhythm={durations} bpm={bpm} label="Escuchar antes de tocar" />
        </div>
      )}

      {!running && (
        <button
          onClick={start}
          className="btn-push mb-4 bg-tclas-plum border-2 border-b-4 border-tclas-plum-light border-b-tclas-plum-shadow text-tclas-cream rounded-xl px-6 py-2.5 font-bold uppercase tracking-wide text-sm"
        >
          {done ? "¡Hecho!" : "▶ Empezar"}
        </button>
      )}

      <PianoKeyboard
        from={from}
        to={to}
        onPlay={handlePlay}
        highlightNotes={done || feedback || !running ? [] : [notes[cursor]]}
        fallingNotes={running ? fallingNotes : undefined}
        fallingLaneHeight={LANE_HEIGHT}
      />

      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
