// Utilidades de teoria musical usadas por el generador de contenido (servidor).

const LETTER_SEMITONES: Record<string, number> = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
const NATURAL_LETTERS = ["C", "D", "E", "F", "G", "A", "B"];
const SOLFEGE: Record<string, string> = { C: "Do", D: "Re", E: "Mi", F: "Fa", G: "Sol", A: "La", B: "Si" };

export interface ParsedNote {
  letter: string;
  accidental: 0 | 1 | -1;
  octave: number;
}

export function parseNote(note: string): ParsedNote {
  const match = note.match(/^([A-G])(#|b)?(-?\d+)$/);
  if (!match) throw new Error(`Nota invalida: ${note}`);
  const [, letter, acc, octaveStr] = match;
  return { letter, accidental: acc === "#" ? 1 : acc === "b" ? -1 : 0, octave: parseInt(octaveStr, 10) };
}

export function noteToMidi(note: string): number {
  const { letter, accidental, octave } = parseNote(note);
  return LETTER_SEMITONES[letter] + accidental + (octave + 1) * 12;
}

const SHARP_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
export function midiToNoteName(midi: number): string {
  const octave = Math.floor(midi / 12) - 1;
  return `${SHARP_NAMES[midi % 12]}${octave}`;
}

/** Nombre en solfeo (Do, Re, Mi...) de una nota, con sufijo de alteracion si aplica. */
export function toSolfege(note: string): string {
  const { letter, accidental } = parseNote(note);
  const suffix = accidental === 1 ? " sostenido" : accidental === -1 ? " bemol" : "";
  return SOLFEGE[letter] + suffix;
}

export function onlyLetter(note: string): string {
  return parseNote(note).letter;
}

/** Genera 2 opciones de nota distintas (para preguntas de opcion multiple) cercanas a la correcta. */
export function distractorLetters(correctLetter: string, count = 2): string[] {
  const idx = NATURAL_LETTERS.indexOf(correctLetter);
  const pool = NATURAL_LETTERS.filter((l) => l !== correctLetter);
  // preferir letras cercanas para que la pregunta tenga sentido, pero con variedad
  pool.sort((a, b) => {
    const da = Math.abs(NATURAL_LETTERS.indexOf(a) - idx);
    const db = Math.abs(NATURAL_LETTERS.indexOf(b) - idx);
    return da - db;
  });
  return pool.slice(0, count);
}

/** Construye una triada aproximada (fundamental-3ra-5ta) a partir de un simbolo de cifrado como "C", "Am", "F", "G7", "Bb6". */
export function chordSymbolToNotes(symbol: string, octave = 4): string[] {
  const match = symbol.match(/^([A-G])(#|b)?(.*)$/);
  if (!match) return [`C${octave}`];
  const [, letter, acc, quality] = match;
  const rootMidi = noteToMidi(`${letter}${acc ?? ""}${octave}`);
  const isMinor = quality.startsWith("m") && !quality.startsWith("maj");
  const third = rootMidi + (isMinor ? 3 : 4);
  const fifth = rootMidi + 7;
  return [midiToNoteName(rootMidi), midiToNoteName(third), midiToNoteName(fifth)];
}

/** Traduce un simbolo de cifrado americano a un nombre en espanol, ej. "Am" -> "La menor", "G7" -> "Sol 7". */
export function chordSymbolToSpanish(symbol: string): string {
  const match = symbol.match(/^([A-G])(#|b)?(.*)$/);
  if (!match) return symbol;
  const [, letter, acc, quality] = match;
  const rootName = SOLFEGE[letter] + (acc === "#" ? " sostenido" : acc === "b" ? " bemol" : "");
  if (quality === "" || quality === "maj") return `${rootName} Mayor`;
  if (quality === "m") return `${rootName} menor`;
  if (quality === "7") return `${rootName} 7`;
  if (quality === "m7") return `${rootName} menor 7`;
  if (quality === "maj7") return `${rootName} Mayor 7`;
  if (quality === "dim") return `${rootName} disminuido`;
  return `${rootName} ${quality}`;
}

/** Nombre en espanol del intervalo (en semitonos, sin importar la direccion) entre dos notas. */
const INTERVAL_NAMES = [
  "Unisono", "2da menor", "2da mayor", "3ra menor", "3ra mayor", "4ta justa",
  "4ta aumentada", "5ta justa", "6ta menor", "6ta mayor", "7ma menor", "7ma mayor", "Octava",
];
export function intervalName(noteA: string, noteB: string): string {
  const semitones = Math.abs(noteToMidi(noteB) - noteToMidi(noteA)) % 12;
  return INTERVAL_NAMES[semitones];
}

/** Escala mayor (8 notas) para las tonalidades usadas en el repertorio, en un registro comodo para calentar. */
const MAJOR_SCALES: Record<string, string[]> = {
  "Do Mayor": ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"],
  "Fa Mayor": ["F4", "G4", "A4", "Bb4", "C5", "D5", "E5", "F5"],
  "Sol Mayor": ["G4", "A4", "B4", "C5", "D5", "E5", "F#5", "G5"],
  "Re Mayor": ["D4", "E4", "F#4", "G4", "A4", "B4", "C#5", "D5"],
};
export function scaleForKey(keySignature: string): string[] {
  return MAJOR_SCALES[keySignature] ?? MAJOR_SCALES["Do Mayor"];
}

function shiftOctave(note: string, delta: number): string {
  const { letter, accidental, octave } = parseNote(note);
  const acc = accidental === 1 ? "#" : accidental === -1 ? "b" : "";
  return `${letter}${acc}${octave + delta}`;
}

/** La misma escala que scaleForKey, desplazada al registro grave (clave de Fa). */
export function scaleForKeyBass(keySignature: string): string[] {
  return scaleForKey(keySignature).map((n) => shiftOctave(n, -2));
}
