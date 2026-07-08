import { getAudioContext, scheduleNote } from "./audio";

export interface MelodyHandle {
  stop: () => void;
}

const DEFAULT_BPM = 92;

/** Reproduce una melodia completa (con su ritmo real) programandola de golpe en
 * el reloj de audio, para que suene con el tempo correcto sin acumular
 * retraso. onNoteStart, si se pasa, se llama justo cuando empieza cada nota
 * (por ejemplo para resaltarla visualmente mientras suena). */
export function playMelody(notes: string[], rhythm: number[], bpm = DEFAULT_BPM, onNoteStart?: (index: number) => void): MelodyHandle {
  const audioCtx = getAudioContext();
  const beatMs = 60000 / bpm;
  const startTime = audioCtx.currentTime + 0.15;
  const stops: (() => void)[] = [];
  const timeouts: number[] = [];

  let cursorMs = 0;
  notes.forEach((note, i) => {
    const durationMs = (rhythm[i] ?? 1) * beatMs;
    const noteTime = startTime + cursorMs / 1000;
    const handle = scheduleNote(note, noteTime, Math.min(durationMs / 1000, 1.1) * 0.88);
    stops.push(handle.stop);
    if (onNoteStart) {
      const delayMs = Math.max(0, (noteTime - audioCtx.currentTime) * 1000);
      timeouts.push(window.setTimeout(() => onNoteStart(i), delayMs));
    }
    cursorMs += durationMs;
  });

  return {
    stop: () => {
      stops.forEach((s) => s());
      timeouts.forEach((id) => clearTimeout(id));
    },
  };
}
