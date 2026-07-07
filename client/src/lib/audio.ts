import { noteToFrequency } from "./notes";

let ctx: AudioContext | null = null;
function getCtx(): AudioContext {
  if (!ctx) ctx = new AudioContext();
  if (ctx.state === "suspended") ctx.resume();
  return ctx;
}

/** Sintetiza un sonido de piano simple (dos osciladores + envolvente) para dar feedback instantaneo. */
export function playNote(note: string, duration = 0.6, velocity = 0.8) {
  const audioCtx = getCtx();
  const freq = noteToFrequency(note);
  const now = audioCtx.currentTime;

  const gain = audioCtx.createGain();
  gain.gain.setValueAtTime(0, now);
  gain.gain.linearRampToValueAtTime(velocity * 0.35, now + 0.01);
  gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);
  gain.connect(audioCtx.destination);

  const osc1 = audioCtx.createOscillator();
  osc1.type = "triangle";
  osc1.frequency.value = freq;
  osc1.connect(gain);

  const osc2 = audioCtx.createOscillator();
  osc2.type = "sine";
  osc2.frequency.value = freq * 2;
  const gain2 = audioCtx.createGain();
  gain2.gain.value = 0.08;
  osc2.connect(gain2);
  gain2.connect(gain);

  osc1.start(now);
  osc2.start(now);
  osc1.stop(now + duration + 0.05);
  osc2.stop(now + duration + 0.05);
}

export function playSuccessChime() {
  ["C5", "E5", "G5"].forEach((n, i) => setTimeout(() => playNote(n, 0.5, 0.5), i * 90));
}

export function playErrorBuzz() {
  const audioCtx = getCtx();
  const now = audioCtx.currentTime;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  osc.type = "sawtooth";
  osc.frequency.value = 130;
  gain.gain.setValueAtTime(0.15, now);
  gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.3);
  osc.connect(gain);
  gain.connect(audioCtx.destination);
  osc.start(now);
  osc.stop(now + 0.3);
}
