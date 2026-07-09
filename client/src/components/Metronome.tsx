import { useEffect, useRef, useState } from "react";
import { getAudioContext, scheduleClick } from "../lib/audio";

const MIN_BPM = 40;
const MAX_BPM = 208;
const BEATS_PER_MEASURE = 4;
const SCHEDULE_AHEAD_SEC = 0.1;
const LOOKAHEAD_MS = 25;

/** Metronomo con reloj de audio (look-ahead scheduling): programa los clics con
 * antelacion en el reloj del AudioContext en vez de con setTimeout a pelo, para
 * que no se acumule retraso con el paso de los minutos. */
function useMetronomeClicks(bpm: number, running: boolean) {
  const [pulse, setPulse] = useState(0);
  const nextNoteTimeRef = useRef(0);
  const beatNumberRef = useRef(0);
  const intervalIdRef = useRef<number | undefined>(undefined);

  useEffect(() => {
    if (!running) return;
    const audioCtx = getAudioContext();
    nextNoteTimeRef.current = audioCtx.currentTime + 0.05;
    beatNumberRef.current = 0;

    function scheduler() {
      const ctx = getAudioContext();
      while (nextNoteTimeRef.current < ctx.currentTime + SCHEDULE_AHEAD_SEC) {
        const isAccent = beatNumberRef.current % BEATS_PER_MEASURE === 0;
        scheduleClick(nextNoteTimeRef.current, isAccent);
        const delayMs = Math.max(0, (nextNoteTimeRef.current - ctx.currentTime) * 1000);
        setTimeout(() => setPulse((p) => p + 1), delayMs);
        nextNoteTimeRef.current += 60 / bpm;
        beatNumberRef.current += 1;
      }
    }
    scheduler();
    intervalIdRef.current = window.setInterval(scheduler, LOOKAHEAD_MS);
    return () => window.clearInterval(intervalIdRef.current);
  }, [running, bpm]);

  return pulse;
}

export function Metronome() {
  const [open, setOpen] = useState(false);
  const [running, setRunning] = useState(false);
  const [bpm, setBpm] = useState(90);
  const pulse = useMetronomeClicks(bpm, running);

  return (
    <div className="fixed bottom-24 right-4 z-30 flex flex-col items-end gap-2">
      {open && (
        <div className="bg-tclas-cream border border-tclas-ink/15 rounded-2xl shadow-lg p-4 w-56">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/50">Metrónomo</span>
            <span
              key={pulse}
              className={`w-3 h-3 rounded-full ${running ? "bg-tclas-gold animate-pop-in" : "bg-tclas-ink/15"}`}
              aria-hidden="true"
            />
          </div>
          <div className="text-center mb-3">
            <span className="font-mono text-3xl font-bold text-tclas-plum tabular-nums">{bpm}</span>
            <span className="text-xs text-tclas-ink/40 ml-1">bpm</span>
          </div>
          <div className="flex items-center gap-2 mb-3">
            <button
              onClick={() => setBpm((b) => Math.max(MIN_BPM, b - 4))}
              className="w-9 h-9 rounded-lg bg-tclas-ink/5 hover:bg-tclas-ink/10 font-bold"
              aria-label="Bajar tempo"
            >
              −
            </button>
            <input
              type="range"
              min={MIN_BPM}
              max={MAX_BPM}
              value={bpm}
              onChange={(e) => setBpm(Number(e.target.value))}
              className="flex-1 accent-tclas-plum"
            />
            <button
              onClick={() => setBpm((b) => Math.min(MAX_BPM, b + 4))}
              className="w-9 h-9 rounded-lg bg-tclas-ink/5 hover:bg-tclas-ink/10 font-bold"
              aria-label="Subir tempo"
            >
              +
            </button>
          </div>
          <button
            onClick={() => setRunning((r) => !r)}
            className={`btn-push w-full rounded-xl py-2.5 font-bold uppercase tracking-wide text-sm
              ${running ? "bg-tclas-rose border-tclas-rose-shadow text-white" : "bg-tclas-sage border-tclas-sage-shadow text-white"}`}
          >
            {running ? "Detener" : "Empezar"}
          </button>
        </div>
      )}
      <button
        onClick={() => setOpen((v) => !v)}
        className={`btn-push w-14 h-14 rounded-full text-2xl flex items-center justify-center border-4
          ${running ? "bg-tclas-gold border-tclas-gold-light border-b-tclas-gold-shadow" : "bg-tclas-plum border-tclas-plum-light border-b-tclas-plum-shadow"}`}
        title="Metrónomo"
        aria-label="Metrónomo"
      >
        🥁
      </button>
    </div>
  );
}
