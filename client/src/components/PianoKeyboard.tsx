import { useCallback, useEffect, useMemo, useState } from "react";
import { isBlackKey, noteToMidi, midiToNoteName } from "../lib/notes";
import { playNote } from "../lib/audio";
import { useMidiInput } from "../lib/midi";
import { usePitchInput } from "../lib/pitchDetection";

interface PianoKeyboardProps {
  from?: string;
  to?: string;
  highlightNotes?: string[];
  feedback?: Record<string, "correct" | "wrong">;
  onPlay?: (note: string) => void;
  compact?: boolean;
}

const KEY_MAP: Record<string, number> = {
  a: 0, w: 1, s: 2, e: 3, d: 4, f: 5, t: 6, g: 7, y: 8, h: 9, u: 10, j: 11, k: 12,
};

function range(from: string, to: string): string[] {
  const notes: string[] = [];
  const fromMidi = noteToMidi(from);
  const toMidi = noteToMidi(to);
  for (let m = fromMidi; m <= toMidi; m++) notes.push(midiToNoteName(m));
  return notes;
}

export function PianoKeyboard({ from = "C3", to = "C5", highlightNotes = [], feedback = {}, onPlay, compact = false }: PianoKeyboardProps) {
  const [pressed, setPressed] = useState<Set<string>>(new Set());
  const allNotes = useMemo(() => range(from, to), [from, to]);
  const whiteWidth = compact ? 34 : 44;
  const blackWidth = whiteWidth * 0.62;

  const trigger = useCallback(
    (note: string, opts?: { silent?: boolean }) => {
      // Silent: la nota ya suena de verdad (piano acustico via microfono), no hace
      // falta sintetizarla tambien o sonaria "doblada".
      if (!opts?.silent) playNote(note);
      setPressed((prev) => new Set(prev).add(note));
      setTimeout(() => setPressed((prev) => { const n = new Set(prev); n.delete(note); return n; }), 180);
      onPlay?.(note);
    },
    [onPlay]
  );

  const { status: midiStatus, deviceName } = useMidiInput(trigger);
  const micTrigger = useCallback((note: string) => trigger(note, { silent: true }), [trigger]);
  const { status: micStatus, start: startMic, stop: stopMic, detectedNote } = usePitchInput(micTrigger);

  useEffect(() => {
    const baseMidi = noteToMidi("C4");
    function handleKeyDown(e: KeyboardEvent) {
      if (e.repeat) return;
      const offset = KEY_MAP[e.key.toLowerCase()];
      if (offset === undefined) return;
      trigger(midiToNoteName(baseMidi + offset));
    }
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [trigger]);

  let whiteIndex = -1;

  return (
    <div className="w-full">
      <div className="flex items-center justify-between mb-2 text-xs text-tclas-ink/60 px-1 flex-wrap gap-1">
        <span>Toca con el raton, con el teclado (A S D F G H J...), conecta un piano MIDI o usa tu piano real con el micrófono.</span>
        <div className="flex items-center gap-1.5 shrink-0">
          <span className={`px-2 py-0.5 rounded-full ${midiStatus === "connected" ? "bg-tclas-sage/20 text-tclas-sage" : "bg-tclas-ink/5"}`}>
            {midiStatus === "connected" ? `🎹 MIDI: ${deviceName}` : midiStatus === "unsupported" ? "MIDI no soportado" : "Sin piano MIDI"}
          </span>
          <button
            type="button"
            onClick={() => (micStatus === "listening" ? stopMic() : startMic())}
            className={`px-2 py-0.5 rounded-full font-semibold transition-colors
              ${micStatus === "listening" ? "bg-tclas-rose/20 text-tclas-rose" : micStatus === "denied" ? "bg-tclas-ink/5 text-tclas-ink/30" : "bg-tclas-ink/5 hover:bg-tclas-ink/10"}`}
            disabled={micStatus === "unsupported"}
            title="Toca tu piano acustico real y la app intentara reconocer la nota (una nota cada vez, en una sala silenciosa)"
          >
            {micStatus === "listening" ? `🎤 Escuchando${detectedNote ? `: ${detectedNote}` : "..."}` : micStatus === "requesting" ? "🎤 Pidiendo permiso..." : micStatus === "denied" ? "🎤 Permiso denegado" : "🎤 Usar micrófono"}
          </button>
        </div>
      </div>
      <div className="overflow-x-auto pb-2">
        <div className="relative inline-flex" style={{ height: compact ? 110 : 150 }}>
          {allNotes
            .filter((n) => !isBlackKey(n))
            .map((note) => {
              whiteIndex++;
              const isHighlighted = highlightNotes.includes(note);
              const fb = feedback[note];
              return (
                <button
                  key={note}
                  onClick={() => trigger(note)}
                  style={{ width: whiteWidth, left: whiteIndex * whiteWidth }}
                  className={`absolute top-0 h-full rounded-b-md border border-tclas-ink/20 piano-key-shadow transition-colors
                    ${fb === "correct" ? "bg-tclas-sage/40" : fb === "wrong" ? "bg-tclas-rose/40" : pressed.has(note) ? "bg-tclas-gold/40" : "bg-white"}
                    ${isHighlighted ? "ring-2 ring-tclas-gold ring-inset" : ""}`}
                >
                  <span className="absolute bottom-1 left-1/2 -translate-x-1/2 text-[10px] text-tclas-ink/40">{note}</span>
                </button>
              );
            })}
          {(() => {
            let wIdx = -1;
            return allNotes.map((note) => {
              if (!isBlackKey(note)) {
                wIdx++;
                return null;
              }
              const isHighlighted = highlightNotes.includes(note);
              const fb = feedback[note];
              return (
                <button
                  key={note}
                  onClick={() => trigger(note)}
                  style={{ width: blackWidth, left: wIdx * whiteWidth + whiteWidth - blackWidth / 2, height: "60%" }}
                  className={`absolute top-0 rounded-b-md z-10 transition-colors
                    ${fb === "correct" ? "bg-tclas-sage" : fb === "wrong" ? "bg-tclas-rose" : pressed.has(note) ? "bg-tclas-gold" : "bg-tclas-ink"}
                    ${isHighlighted ? "ring-2 ring-tclas-gold" : ""}`}
                />
              );
            });
          })()}
        </div>
      </div>
    </div>
  );
}
