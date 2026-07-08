import { useEffect, useRef, useState } from "react";
import { playMelody } from "../lib/melodyPlayer";
import type { MelodyHandle } from "../lib/melodyPlayer";

interface Props {
  notes: string[];
  rhythm?: number[];
  bpm?: number;
  onNoteStart?: (index: number) => void;
  label?: string;
  className?: string;
}

/** Boton reutilizable para escuchar una melodia/secuencia sintetizada antes de
 * intentar tocarla, con el tempo y ritmo reales cuando se conocen. */
export function ListenButton({ notes, rhythm, bpm = 92, onNoteStart, label = "Escuchar", className = "" }: Props) {
  const [playing, setPlaying] = useState(false);
  const handleRef = useRef<MelodyHandle | null>(null);
  const stopTimeoutRef = useRef<number | undefined>(undefined);

  useEffect(
    () => () => {
      handleRef.current?.stop();
      clearTimeout(stopTimeoutRef.current);
    },
    []
  );

  function toggle() {
    if (playing) {
      handleRef.current?.stop();
      clearTimeout(stopTimeoutRef.current);
      setPlaying(false);
      return;
    }
    const effectiveRhythm = rhythm ?? notes.map(() => 1);
    const totalBeats = effectiveRhythm.reduce((a, b) => a + b, 0);
    const totalMs = (totalBeats * 60000) / bpm + 400;
    handleRef.current = playMelody(notes, effectiveRhythm, bpm, onNoteStart);
    setPlaying(true);
    stopTimeoutRef.current = window.setTimeout(() => setPlaying(false), totalMs);
  }

  return (
    <button
      onClick={toggle}
      type="button"
      className={`text-xs font-semibold rounded-full px-3 py-1.5 border transition-colors
        ${playing ? "bg-tclas-plum text-tclas-cream border-tclas-plum" : "bg-tclas-ink/5 border-tclas-ink/15 text-tclas-ink/60 hover:border-tclas-plum/40"} ${className}`}
    >
      {playing ? "⏸ Sonando..." : `🔊 ${label}`}
    </button>
  );
}
