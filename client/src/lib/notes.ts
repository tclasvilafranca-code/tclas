const LETTER_SEMITONES: Record<string, number> = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
const LETTER_DIATONIC: Record<string, number> = { C: 0, D: 1, E: 2, F: 3, G: 4, A: 5, B: 6 };

export interface ParsedNote {
  letter: string;
  accidental: 0 | 1 | -1;
  octave: number;
}

export function parseNote(note: string): ParsedNote {
  const match = note.match(/^([A-G])(#|b)?(-?\d+)$/);
  if (!match) throw new Error(`Nota invalida: ${note}`);
  const [, letter, acc, octaveStr] = match;
  return {
    letter,
    accidental: acc === "#" ? 1 : acc === "b" ? -1 : 0,
    octave: parseInt(octaveStr, 10),
  };
}

export function noteToMidi(note: string): number {
  const { letter, accidental, octave } = parseNote(note);
  return LETTER_SEMITONES[letter] + accidental + (octave + 1) * 12;
}

export function midiToFrequency(midi: number): number {
  return 440 * Math.pow(2, (midi - 69) / 12);
}

export function noteToFrequency(note: string): number {
  return midiToFrequency(noteToMidi(note));
}

/** Paso diatonico absoluto (para posicionar la nota en el pentagrama). */
export function diatonicStep(note: string): number {
  const { letter, octave } = parseNote(note);
  return octave * 7 + LETTER_DIATONIC[letter];
}

const SHARP_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];

export function midiToNoteName(midi: number): string {
  const octave = Math.floor(midi / 12) - 1;
  const name = SHARP_NAMES[midi % 12];
  return `${name}${octave}`;
}

export function isBlackKey(note: string): boolean {
  return note.includes("#") || note.includes("b");
}

const SOLFEGE: Record<string, string> = { C: "Do", D: "Re", E: "Mi", F: "Fa", G: "Sol", A: "La", B: "Si" };
export function toSolfege(note: string): string {
  const { letter, accidental } = parseNote(note);
  const suffix = accidental === 1 ? " sostenido" : accidental === -1 ? " bemol" : "";
  return SOLFEGE[letter] + suffix;
}
