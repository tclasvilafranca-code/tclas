import { useCallback, useEffect, useRef, useState } from "react";
import { midiToNoteName } from "./notes";

export type PitchInputStatus = "idle" | "requesting" | "listening" | "denied" | "unsupported" | "error";

const FFT_SIZE = 2048;
const MIN_RMS = 0.01; // por debajo de esto se considera silencio/ruido de fondo
const STABLE_FRAMES_REQUIRED = 3; // frames seguidos con la misma nota antes de darla por buena
const RETRIGGER_COOLDOWN_MS = 220; // evita contar una misma nota sostenida como varios golpes

/**
 * Autocorrelacion normalizada con interpolacion parabolica (metodo clasico de
 * deteccion de tono monofonico): recorta silencio de los bordes, busca el
 * primer minimo de la funcion de autocorrelacion y luego el maximo tras el,
 * y afina la posicion del pico con una parabola para mas precision. Solo
 * sirve para una nota a la vez (no acordes), que es justo lo que necesitan
 * los ejercicios de tocar una melodia real.
 */
function autoCorrelate(buffer: Float32Array, sampleRate: number): number {
  const size = buffer.length;

  let rms = 0;
  for (let i = 0; i < size; i++) rms += buffer[i] * buffer[i];
  rms = Math.sqrt(rms / size);
  if (rms < MIN_RMS) return -1;

  const threshold = 0.2;
  let start = 0;
  let end = size - 1;
  for (let i = 0; i < size / 2; i++) {
    if (Math.abs(buffer[i]) >= threshold) {
      start = i;
      break;
    }
  }
  for (let i = 1; i < size / 2; i++) {
    if (Math.abs(buffer[size - i]) >= threshold) {
      end = size - i;
      break;
    }
  }
  const trimmed = buffer.subarray(start, end);
  const n = trimmed.length;
  if (n < 8) return -1;

  const c = new Float32Array(n);
  for (let lag = 0; lag < n; lag++) {
    let sum = 0;
    for (let i = 0; i < n - lag; i++) sum += trimmed[i] * trimmed[i + lag];
    c[lag] = sum;
  }

  let d = 0;
  while (d + 1 < n && c[d] > c[d + 1]) d++;

  let maxVal = -1;
  let maxPos = -1;
  for (let i = d; i < n; i++) {
    if (c[i] > maxVal) {
      maxVal = c[i];
      maxPos = i;
    }
  }
  if (maxPos <= 0) return -1;

  let t0 = maxPos;
  const prev = c[t0 - 1] ?? c[t0];
  const curr = c[t0];
  const next = c[t0 + 1] ?? c[t0];
  const a = (prev + next - 2 * curr) / 2;
  const b = (next - prev) / 2;
  if (a !== 0) t0 = t0 - b / (2 * a);

  if (t0 <= 0) return -1;
  return sampleRate / t0;
}

function frequencyToNote(freq: number): string {
  const midi = Math.round(69 + 12 * Math.log2(freq / 440));
  return midiToNoteName(midi);
}

/**
 * Escucha el microfono y detecta que nota de piano se esta tocando en cada
 * momento (una nota cada vez, no acordes). Pensado para pianos acusticos
 * reales sin salida MIDI: el alumno toca su piano de verdad y la app "oye"
 * la nota, igual que si la hubiera tocado en el teclado en pantalla.
 *
 * Requiere una accion explicita del usuario para empezar (permiso de
 * microfono), y funciona mejor con una sola nota sonando a la vez, en una
 * habitacion razonablemente silenciosa.
 */
export function usePitchInput(onNote: (note: string) => void) {
  const [status, setStatus] = useState<PitchInputStatus>("idle");
  const callbackRef = useRef(onNote);
  callbackRef.current = onNote;

  const streamRef = useRef<MediaStream | null>(null);
  const audioCtxRef = useRef<AudioContext | null>(null);
  const rafRef = useRef<number | undefined>(undefined);
  const lastNoteRef = useRef<string | null>(null);
  const stableCountRef = useRef(0);
  const lastTriggerAtRef = useRef(0);
  const [detectedNote, setDetectedNote] = useState<string | null>(null);

  const stop = useCallback(() => {
    if (rafRef.current) cancelAnimationFrame(rafRef.current);
    rafRef.current = undefined;
    streamRef.current?.getTracks().forEach((t) => t.stop());
    streamRef.current = null;
    audioCtxRef.current?.close().catch(() => {});
    audioCtxRef.current = null;
    lastNoteRef.current = null;
    stableCountRef.current = 0;
    setDetectedNote(null);
    setStatus("idle");
  }, []);

  const start = useCallback(async () => {
    if (!navigator.mediaDevices?.getUserMedia) {
      setStatus("unsupported");
      return;
    }
    setStatus("requesting");
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: { echoCancellation: false, noiseSuppression: false, autoGainControl: false },
      });
      streamRef.current = stream;

      const AudioContextCtor = window.AudioContext || (window as any).webkitAudioContext;
      const audioCtx: AudioContext = new AudioContextCtor();
      audioCtxRef.current = audioCtx;

      const source = audioCtx.createMediaStreamSource(stream);
      const analyser = audioCtx.createAnalyser();
      analyser.fftSize = FFT_SIZE;
      source.connect(analyser);

      const buffer = new Float32Array(analyser.fftSize);

      function tick() {
        analyser.getFloatTimeDomainData(buffer);
        const freq = autoCorrelate(buffer, audioCtx.sampleRate);

        if (freq === -1) {
          lastNoteRef.current = null;
          stableCountRef.current = 0;
          setDetectedNote(null);
        } else {
          const note = frequencyToNote(freq);
          setDetectedNote(note);
          if (note === lastNoteRef.current) {
            stableCountRef.current += 1;
          } else {
            lastNoteRef.current = note;
            stableCountRef.current = 1;
          }
          const now = performance.now();
          if (stableCountRef.current === STABLE_FRAMES_REQUIRED && now - lastTriggerAtRef.current > RETRIGGER_COOLDOWN_MS) {
            lastTriggerAtRef.current = now;
            callbackRef.current(note);
          }
        }
        rafRef.current = requestAnimationFrame(tick);
      }
      rafRef.current = requestAnimationFrame(tick);
      setStatus("listening");
    } catch {
      setStatus("denied");
    }
  }, []);

  useEffect(() => stop, [stop]);

  return { status, start, stop, detectedNote };
}
