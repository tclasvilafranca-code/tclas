import { useMemo, useState } from "react";
import type { Exercise } from "../lib/api";
import { StaffView } from "../components/StaffView";
import { PianoKeyboard } from "../components/PianoKeyboard";
import { ListenButton } from "../components/ListenButton";
import { noteToMidi, midiToNoteName } from "../lib/notes";
import { playErrorBuzz } from "../lib/audio";

interface Props {
  exercise: Exercise;
  onSubmit: (playedNotes: string[]) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

export function SegmentPracticeExercise({ exercise, onSubmit, feedback }: Props) {
  const { clef, segments } = exercise.data as { clef: "treble" | "bass"; segments: string[][] };
  const [segIndex, setSegIndex] = useState(0);
  const [cursor, setCursor] = useState(0);
  const [progress, setProgress] = useState<("pending" | "correct" | "wrong")[]>(() => segments[0].map(() => "pending"));
  const [doneSegments, setDoneSegments] = useState<Set<number>>(new Set());
  const submitted = !!feedback;

  const currentSegment = segments[segIndex];
  const allDone = doneSegments.size >= segments.length;

  const { from, to } = useMemo(() => {
    const all = segments.flat();
    const midis = all.map(noteToMidi);
    const lowest = Math.min(...midis) - 3;
    const highest = Math.max(...midis) + 3;
    const clamp = (m: number) => Math.max(24, Math.min(96, m));
    return { from: midiToNoteName(clamp(lowest)), to: midiToNoteName(clamp(highest)) };
  }, [segments]);

  function goToSegment(i: number) {
    if (submitted) return;
    setSegIndex(i);
    setCursor(0);
    setProgress(segments[i].map(() => "pending"));
  }

  function handlePlay(note: string) {
    if (submitted || cursor >= currentSegment.length) return;
    if (note === currentSegment[cursor]) {
      setProgress((p) => {
        const c = [...p];
        c[cursor] = "correct";
        return c;
      });
      const next = cursor + 1;
      setCursor(next);
      if (next >= currentSegment.length) {
        setDoneSegments((d) => new Set(d).add(segIndex));
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

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-2">{exercise.prompt}</p>

      <div className="flex items-center justify-center gap-2 mb-3 flex-wrap">
        {segments.map((_, i) => (
          <button
            key={i}
            onClick={() => goToSegment(i)}
            disabled={submitted}
            className={`w-9 h-9 rounded-full text-xs font-bold border-2 transition-colors
              ${i === segIndex ? "border-tclas-plum bg-tclas-plum/10" : doneSegments.has(i) ? "border-tclas-sage bg-tclas-sage/15 text-tclas-sage" : "border-tclas-ink/15 text-tclas-ink/40"}`}
          >
            {doneSegments.has(i) ? "✓" : i + 1}
          </button>
        ))}
      </div>
      <p className="text-xs text-tclas-ink/50 mb-3">
        Tramo {segIndex + 1} de {segments.length} · practica cada tramo las veces que quieras
      </p>
      <div className="flex justify-center mb-4">
        <ListenButton notes={currentSegment} bpm={100} label="Escuchar este tramo" />
      </div>

      <div className="mb-6 overflow-x-auto">
        <StaffView clef={clef} notes={currentSegment} activeIndex={cursor >= currentSegment.length ? undefined : cursor} correctness={progress} />
      </div>

      <PianoKeyboard from={from} to={to} onPlay={handlePlay} highlightNotes={submitted || cursor >= currentSegment.length ? [] : [currentSegment[cursor]]} />

      <div className="flex items-center justify-center gap-4 mt-5">
        <button onClick={() => goToSegment(Math.max(0, segIndex - 1))} disabled={segIndex === 0 || submitted} className="text-sm text-tclas-ink/50 disabled:opacity-30 hover:text-tclas-ink">
          ← Tramo anterior
        </button>
        <button
          onClick={() => goToSegment(Math.min(segments.length - 1, segIndex + 1))}
          disabled={segIndex === segments.length - 1 || submitted}
          className="text-sm text-tclas-ink/50 disabled:opacity-30 hover:text-tclas-ink"
        >
          Tramo siguiente →
        </button>
      </div>

      {allDone && !submitted && (
        <button
          onClick={() => onSubmit(segments.flat())}
          className="btn-push bg-tclas-sage border-tclas-sage-shadow text-white rounded-2xl px-6 py-3 font-bold uppercase tracking-wide text-sm mt-5"
        >
          ¡Ya me la se! Terminar
        </button>
      )}

      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
