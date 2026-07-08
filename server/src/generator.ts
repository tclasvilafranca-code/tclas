// Generador de lecciones semanales a partir del contenido musical real de una pieza.
// Esta es la pieza clave que permite "replicar" el sistema para cualquier alumno:
// una vez una Pieza esta en la biblioteca, asignarla genera automaticamente
// semanas de practica variada (opcion multiple, escribir, relacionar, ordenar,
// tocar, oido, ritmo, decir en voz alta) derivada de sus notas reales.

import { PieceDef, LessonDef, ExerciseDef, nn, sr, rt, et, mcq, kp, ch, wa, ma, ord, sp } from "./content/defs";
import { toSolfege, onlyLetter, distractorLetters, chordSymbolToNotes, chordSymbolToSpanish } from "./notes";

type Phase = "intro" | "practice" | "final" | "all";

function uniq<T>(arr: T[]): T[] {
  return Array.from(new Set(arr));
}

function pick<T>(arr: T[], index: number): T {
  return arr[index % arr.length];
}

function introExercises(def: PieceDef, weekNum: number): ExerciseDef[] {
  const { content } = def;
  const exercises: ExerciseDef[] = [];

  exercises.push({
    type: "THEORY_MCQ",
    prompt: `¿En que compas esta escrita "${def.title}"?`,
    data: mcq(`¿En que compas esta escrita "${def.title}"?`, uniq([def.timeSignature, "3/4", "4/4", "6/8"]).slice(0, 3), def.timeSignature),
    explanation: `"${def.title}" esta escrita en ${def.timeSignature}, en la tonalidad de ${def.keySignature}.`,
  });

  const featured = content.featuredNotes;
  const note1 = pick(featured, 0);
  const letter1 = onlyLetter(note1);
  exercises.push({
    type: "NOTE_NAME",
    prompt: "¿Como se llama esta nota?",
    data: nn(content.clef === "bass" ? "bass" : "treble", note1, uniq([toSolfege(note1), ...distractorLetters(letter1).map((l) => toSolfege(`${l}4`))]), toSolfege(note1)),
    explanation: `Esta nota aparece en "${def.title}".`,
  });

  if (featured.length >= 3) {
    const pairs = featured.slice(0, 4).map((n) => ({ left: `STAFF:${n}:${content.clef === "bass" ? "bass" : "treble"}`, right: toSolfege(n) }));
    exercises.push({
      type: "MATCHING",
      prompt: `Relaciona cada nota de "${def.title}" con su nombre`,
      data: ma(pairs),
      explanation: "Estas son algunas de las notas principales de la pieza.",
    });
  }

  exercises.push({
    type: "EAR_TRAINING",
    prompt: `Escucha el comienzo de "${def.title}"... ¿cual es la primera nota?`,
    data: et("note", toSolfege(content.melody[0]), uniq([toSolfege(content.melody[0]), ...distractorLetters(onlyLetter(content.melody[0])).map((l) => toSolfege(`${l}4`))]), [content.melody[0]]),
    explanation: `La pieza empieza en ${toSolfege(content.melody[0])}.`,
  });

  return exercises;
}

function practiceExercises(def: PieceDef, weekNum: number): ExerciseDef[] {
  const { content } = def;
  const exercises: ExerciseDef[] = [];

  exercises.push({
    type: "STAFF_READING",
    prompt: `Lee y toca el comienzo de "${def.title}"`,
    data: sr(content.clef === "bass" ? "bass" : "treble", content.melody),
    explanation: content.lyricsHook ? `"${content.lyricsHook}"` : `El inicio de "${def.title}".`,
  });

  exercises.push({
    type: "RHYTHM_TAP",
    prompt: `Marca el ritmo de "${def.title}"`,
    data: rt(genericBpmFor(def), content.melodyRhythm, def.timeSignature),
    explanation: "Este es el ritmo real de la melodia.",
  });

  const featured = content.featuredNotes;
  const note2 = pick(featured, weekNum);
  exercises.push({
    type: "WRITE_ANSWER",
    prompt: "Escribe (en solfeo) el nombre de esta nota",
    data: wa(`Nota: ${note2}`, toSolfege(note2).toLowerCase(), [toSolfege(note2), onlyLetter(note2)], "ej: do, re, mi..."),
    explanation: `Se llama ${toSolfege(note2)}.`,
  });

  if (content.melody.length >= 4) {
    const excerpt = content.melody.slice(0, 5);
    exercises.push({
      type: "ORDERING",
      prompt: `Ordena estas notas para formar el comienzo de "${def.title}"`,
      data: ord(excerpt, content.clef === "bass" ? "bass" : "treble"),
      explanation: "Este es el orden real de la melodia.",
    });
  }

  if (content.chordsUsed && content.chordsUsed.length > 0) {
    const symbol = pick(content.chordsUsed, weekNum);
    const chordNotes = chordSymbolToNotes(symbol);
    const spanishName = chordSymbolToSpanish(symbol);
    const otherSymbols = content.chordsUsed.filter((s) => s !== symbol);
    const options = uniq([spanishName, ...otherSymbols.slice(0, 2).map(chordSymbolToSpanish), "Do Mayor"]).slice(0, 3);
    exercises.push({
      type: "CHORD",
      prompt: "¿Que acorde es este? (aparece en la pieza)",
      data: ch(chordNotes[0], chordNotes, spanishName, options),
      explanation: `${symbol} se llama "${spanishName}" en espanol.`,
    });
  } else {
    exercises.push({
      type: "KEYBOARD_PLAY",
      prompt: `Toca de nuevo el comienzo de "${def.title}"`,
      data: kp(content.melody, content.clef === "bass" ? "bass" : "treble", genericBpmFor(def)),
      explanation: "Cuanto mas repitas, mas natural te saldra.",
    });
  }

  return exercises;
}

function finalExercises(def: PieceDef, weekNum: number): ExerciseDef[] {
  const { content } = def;
  const exercises: ExerciseDef[] = [];

  exercises.push({
    type: "KEYBOARD_PLAY",
    prompt: `¡Toca la mano derecha de "${def.title}" completa!`,
    data: kp(content.melody, content.clef === "bass" ? "bass" : "treble", genericBpmFor(def)),
    explanation: content.isDuet ? "Recuerda: esta pieza se toca a duo, con tu profesora o tu familia acompanando." : "¡Esta es tu pieza de esta semana!",
  });

  if (content.bass && content.bass.length > 0) {
    exercises.push({
      type: "KEYBOARD_PLAY",
      prompt: `Ahora toca la mano izquierda de "${def.title}"`,
      data: kp(content.bass, "bass", genericBpmFor(def)),
      explanation: "La mano izquierda suele llevar el acompanamiento.",
    });
  }

  const note3 = pick(content.featuredNotes, weekNum + 1);
  exercises.push({
    type: "SPEAK_ALOUD",
    prompt: "Di en voz alta el nombre de esta nota",
    data: sp(toSolfege(note3), [onlyLetter(note3)], note3),
    explanation: `Es un ${toSolfege(note3)}. Si tu navegador no soporta el microfono, puedes omitir este ejercicio.`,
  });

  exercises.push({
    type: "THEORY_MCQ",
    prompt: `¡Enhorabuena! ¿Como se titula la pieza que acabas de dominar?`,
    data: mcq(`¡Enhorabuena! ¿Como se titula la pieza que acabas de dominar?`, uniq([def.title, "Para Elisa", "Claro de Luna"]).slice(0, 3), def.title),
    explanation: `¡Llévasela a tu profesora en la proxima clase presencial!`,
  });

  return exercises;
}

function genericBpmFor(def: PieceDef): number {
  return def.difficultyTier <= 2 ? 84 : def.difficultyTier <= 4 ? 96 : 108;
}

/** Genera las lecciones semanales (weekIndex 1..durationWeeks) para una pieza asignada. */
export function generateLessonsForPiece(def: PieceDef, durationWeeks: number): LessonDef[] {
  const weeks = Math.max(1, durationWeeks);
  const lessons: LessonDef[] = [];

  for (let w = 1; w <= weeks; w++) {
    const phase: Phase = weeks === 1 ? "all" : w === 1 ? "intro" : w === weeks ? "final" : "practice";
    let exercises: ExerciseDef[];
    let title: string;
    let description: string;

    if (phase === "all") {
      exercises = [...introExercises(def, w).slice(0, 2), ...practiceExercises(def, w).slice(0, 2), ...finalExercises(def, w)];
      title = def.title;
      description = `Semana unica: descubre, practica y domina "${def.title}".`;
    } else if (phase === "intro") {
      exercises = introExercises(def, w);
      title = `${def.title} — Descubre`;
      description = `Primer contacto con "${def.title}": sus notas, su compas y como suena.`;
    } else if (phase === "final") {
      exercises = finalExercises(def, w);
      title = `${def.title} — ¡Domínala!`;
      description = `Toca "${def.title}" completa. ¡Es la semana final de esta pieza!`;
    } else {
      exercises = practiceExercises(def, w);
      title = `${def.title} — Practica (semana ${w})`;
      description = `Sigue practicando "${def.title}": lectura, ritmo y notas clave.`;
    }

    lessons.push({
      title,
      description,
      xpReward: 15 + def.difficultyTier * 2,
      exercises,
    });
  }

  return lessons;
}
