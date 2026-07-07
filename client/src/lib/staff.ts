import { diatonicStep, parseNote } from "./notes";

// Referencia: nota en la linea inferior del pentagrama (posicion 0).
const BOTTOM_LINE_REF: Record<"treble" | "bass", string> = { treble: "E4", bass: "G2" };

/** Posicion en "medios espacios" desde la linea inferior del pentagrama (positivo = hacia arriba). */
export function staffPosition(note: string, clef: "treble" | "bass"): number {
  return diatonicStep(note) - diatonicStep(BOTTOM_LINE_REF[clef]);
}

export function needsLedgerLines(position: number): number[] {
  const lines: number[] = [];
  if (position < 0) {
    for (let p = -2; p >= position; p -= 2) lines.push(p);
  } else if (position > 8) {
    for (let p = 10; p <= position; p += 2) lines.push(p);
  }
  return lines;
}

export function accidentalSymbol(note: string): string | null {
  const { accidental } = parseNote(note);
  if (accidental === 1) return "♯";
  if (accidental === -1) return "♭";
  return null;
}
