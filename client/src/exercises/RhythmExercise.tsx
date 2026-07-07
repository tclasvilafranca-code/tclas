import { useEffect, useRef, useState } from "react";
import type { Exercise } from "../lib/api";
import { playNote } from "../lib/audio";

interface Props {
  exercise: Exercise;
  onSubmit: (intervals: number[]) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

type Phase = "idle" | "countdown" | "recording" | "submitted";

export function RhythmExercise({ exercise, onSubmit, feedback }: Props) {
  const { data, prompt } = exercise;
  const pattern: number[] = data.pattern;
  const bpm: number = data.bpm;
  const beatMs = 60000 / bpm;
  const beatsPerBar = parseInt(String(data.timeSignature).split("/")[0], 10) || 4;
  const expectedTaps = pattern.length + 1;

  const [phase, setPhase] = useState<Phase>("idle");
  const [tapCount, setTapCount] = useState(0);
  const [countdownBeat, setCountdownBeat] = useState(0);
  const tapsRef = useRef<number[]>([]);

  useEffect(() => {
    function handleKey(e: KeyboardEvent) {
      if (e.code === "Space") {
        e.preventDefault();
        tap();
      }
    }
    window.addEventListener("keydown", handleKey);
    return () => window.removeEventListener("keydown", handleKey);
  });

  function start() {
    setPhase("countdown");
    tapsRef.current = [];
    setTapCount(0);
    let beat = 0;
    setCountdownBeat(0);
    const timer = setInterval(() => {
      beat++;
      playNote("A5", 0.08, 0.4);
      setCountdownBeat(beat);
      if (beat >= beatsPerBar) {
        clearInterval(timer);
        setPhase("recording");
      }
    }, beatMs);
  }

  function tap() {
    if (phase !== "recording" || feedback) return;
    const now = performance.now();
    tapsRef.current.push(now);
    playNote("C5", 0.1, 0.5);
    const count = tapsRef.current.length;
    setTapCount(count);
    if (count >= expectedTaps) {
      const intervals: number[] = [];
      for (let i = 0; i < tapsRef.current.length - 1; i++) {
        intervals.push((tapsRef.current[i + 1] - tapsRef.current[i]) / beatMs);
      }
      setPhase("submitted");
      onSubmit(intervals);
    }
  }

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-2">{prompt}</p>
      <p className="text-xs text-tclas-ink/50 mb-4">Tempo: {bpm} BPM &middot; Compas {data.timeSignature}</p>

      <div className="flex justify-center gap-2 mb-6">
        {pattern.map((dur, i) => (
          <div
            key={i}
            className="bg-tclas-plum/10 border-2 border-tclas-plum/30 rounded-md flex items-center justify-center text-xs font-semibold text-tclas-plum"
            style={{ width: 36 * dur + 20, height: 44 }}
          >
            {dur}
          </div>
        ))}
      </div>

      {phase === "idle" && (
        <button onClick={start} className="bg-tclas-plum text-tclas-cream rounded-full px-6 py-3 font-semibold hover:bg-tclas-plum-light">
          ▶ Empezar (escucha {beatsPerBar} clics y luego marca el ritmo)
        </button>
      )}

      {phase === "countdown" && <p className="text-2xl font-display">Preparate... {countdownBeat}/{beatsPerBar}</p>}

      {phase === "recording" && (
        <div>
          <button
            onClick={tap}
            className="bg-tclas-gold text-tclas-ink rounded-full w-32 h-32 text-xl font-bold hover:bg-tclas-gold-light active:scale-95 transition-transform"
          >
            TOCA
          </button>
          <p className="text-xs text-tclas-ink/50 mt-3">
            Tambien puedes pulsar la barra espaciadora. Toque {tapCount}/{expectedTaps}
          </p>
        </div>
      )}

      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
      {phase === "submitted" && !feedback && <p className="text-sm text-tclas-ink/50 mt-4">Calculando resultado...</p>}
    </div>
  );
}
