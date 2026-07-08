// Generador de sesiones semanales a partir del contenido musical real de una pieza.
// Cada semana es una sesion de practica completa (10-15 min), estructurada como
// lo haria un profesor de piano de verdad: Calentamiento -> Trabajo de la pieza -> A tocar.
// Esta es la pieza clave que permite "replicar" el sistema para cualquier alumno:
// una vez una Pieza esta en la biblioteca, asignarla genera automaticamente
// semanas de practica variada (opcion multiple, escribir, relacionar, ordenar,
// tocar, oido, ritmo, decir en voz alta) derivada de sus notas reales.

import { PieceDef, LessonDef, ExerciseDef, nn, sr, rt, et, mcq, kp, ch, iv, wa, ma, ord, sp, ds, hn, scp, fb, eb } from "./content/defs";
import { toSolfege, onlyLetter, distractorLetters, chordSymbolToNotes, chordSymbolToSpanish, scaleForKey, intervalName } from "./notes";

function uniq<T>(arr: T[]): T[] {
  return Array.from(new Set(arr));
}

function pick<T>(arr: T[], index: number): T {
  return arr[((index % arr.length) + arr.length) % arr.length];
}

function genericBpmFor(def: PieceDef): number {
  return def.difficultyTier <= 2 ? 84 : def.difficultyTier <= 4 ? 96 : 108;
}

// --- Fase 1: Calentamiento (agilidad visual, dedos, oido, pulso) ---
// Usa la escala de la tonalidad de la pieza: es lo que haria cualquier pianista
// antes de abordar una pieza nueva, y ademas refuerza la lectura en esa tonalidad.
function warmupExercises(def: PieceDef, weekNum: number): ExerciseDef[] {
  const scale = scaleForKey(def.keySignature);
  const ascending = weekNum % 2 === 0;
  const scaleSeq = ascending ? scale : [...scale].reverse();
  const clef = def.content.clef === "bass" ? "bass" : "treble";

  const noteA = pick(scale, weekNum);
  const noteB = pick(scale, weekNum + 3);

  return [
    {
      type: "KEYBOARD_PLAY",
      phase: "WARMUP",
      prompt: `Calienta los dedos: toca la escala de ${def.keySignature} ${ascending ? "subiendo" : "bajando"}`,
      data: kp(scaleSeq, clef, 76),
      explanation: "Tocar la escala antes de empezar prepara la mano para la tonalidad de la pieza.",
    },
    {
      type: "NOTE_NAME",
      phase: "WARMUP",
      prompt: "Agilidad visual: ¿como se llama esta nota?",
      data: nn(clef, noteA, uniq([toSolfege(noteA), ...distractorLetters(onlyLetter(noteA)).map((l) => toSolfege(`${l}4`))]), toSolfege(noteA)),
      explanation: "Reconocer notas rapido es un musculo que se entrena, como las escalas.",
    },
    {
      type: "NOTE_NAME",
      phase: "WARMUP",
      prompt: "Otra vez, rapido: ¿como se llama esta nota?",
      data: nn(clef, noteB, uniq([toSolfege(noteB), ...distractorLetters(onlyLetter(noteB)).map((l) => toSolfege(`${l}4`))]), toSolfege(noteB)),
      explanation: "Cuanta mas practica, mas rapido la reconoceras la proxima vez.",
    },
    {
      type: "RHYTHM_TAP",
      phase: "WARMUP",
      prompt: "Marca un pulso tranquilo para encontrar el tempo",
      data: rt(72, [1, 1, 1, 1], "4/4"),
      explanation: "Un buen pulso interno es la base de tocar con seguridad.",
    },
    {
      type: "EAR_TRAINING",
      phase: "WARMUP",
      prompt: "Despierta el oido: escucha... ¿que nota es?",
      data: et("note", toSolfege(scale[0]), uniq([toSolfege(scale[0]), toSolfege(scale[2]), toSolfege(scale[4])]), [scale[0]]),
      explanation: `${toSolfege(scale[0])} es la nota principal (tonica) de ${def.keySignature}.`,
    },
    {
      type: "HOLD_NOTE",
      phase: "WARMUP",
      prompt: `Manten pulsada la tonica (${toSolfege(scale[0])}) durante toda su duracion`,
      data: hn(scale[0], weekNum % 2 === 0 ? 4 : 2, 60),
      explanation: "Sostener una nota el tiempo justo entrena el control de la duracion, como en una redonda o una blanca.",
    },
  ];
}

// --- Fase 2: Trabajo de la pieza (todas las notas, ritmo, acordes, relacionar, escribir, ordenar) ---
function pieceWorkExercises(def: PieceDef, weekNum: number): ExerciseDef[] {
  const { content } = def;
  const clef = content.clef === "bass" ? "bass" : "treble";
  const exercises: ExerciseDef[] = [];
  const featured = content.featuredNotes.slice(0, 6);

  exercises.push({
    type: "THEORY_MCQ",
    phase: "PRACTICE",
    prompt: `¿En que compas esta escrita "${def.title}"?`,
    data: mcq(`¿En que compas esta escrita "${def.title}"?`, uniq([def.timeSignature, "3/4", "4/4", "6/8"]).slice(0, 3), def.timeSignature),
    explanation: `"${def.title}" esta escrita en ${def.timeSignature}, en la tonalidad de ${def.keySignature}.`,
  });

  // Cubrir TODAS las notas destacadas de la pieza, alternando el tipo de ejercicio.
  featured.forEach((note, i) => {
    const letter = onlyLetter(note);
    const options = uniq([toSolfege(note), ...distractorLetters(letter).map((l) => toSolfege(`${l}4`))]);
    if (i % 2 === 0) {
      exercises.push({
        type: "NOTE_NAME",
        phase: "PRACTICE",
        prompt: "¿Como se llama esta nota de la pieza?",
        data: nn(clef, note, options, toSolfege(note)),
        explanation: `Esta nota aparece en "${def.title}".`,
      });
    } else {
      exercises.push({
        type: "WRITE_ANSWER",
        phase: "PRACTICE",
        prompt: "Escribe (en solfeo) el nombre de esta nota",
        data: wa(`Nota: ${note}`, toSolfege(note).toLowerCase(), [toSolfege(note), letter], "ej: do, re, mi..."),
        explanation: `Se llama ${toSolfege(note)}.`,
      });
    }
  });

  if (featured.length >= 3) {
    const pairs = featured.slice(0, 5).map((n) => ({ left: `STAFF:${n}:${clef}`, right: toSolfege(n) }));
    exercises.push({
      type: "MATCHING",
      phase: "PRACTICE",
      prompt: `Relaciona cada nota de "${def.title}" con su nombre`,
      data: ma(pairs),
      explanation: "Estas son las notas principales de la pieza.",
    });
  }

  const dragNote = pick(featured, weekNum + 4);
  exercises.push({
    type: "DRAG_STAFF",
    phase: "PRACTICE",
    prompt: `Arrastra la nota "${toSolfege(dragNote)}" hasta su sitio correcto en el pentagrama`,
    data: ds(clef, toSolfege(dragNote), dragNote),
    explanation: `${toSolfege(dragNote)} (${dragNote}) es una de las notas de "${def.title}".`,
  });

  exercises.push({
    type: "STAFF_READING",
    phase: "PRACTICE",
    prompt: `Lee y toca el comienzo de "${def.title}"`,
    data: sr(clef, content.melody),
    explanation: content.lyricsHook ? `"${content.lyricsHook}"` : `El inicio de "${def.title}".`,
  });

  exercises.push({
    type: "RHYTHM_TAP",
    phase: "PRACTICE",
    prompt: `Marca el ritmo real de "${def.title}"`,
    data: rt(genericBpmFor(def), content.melodyRhythm, def.timeSignature),
    explanation: "Este es el ritmo real de la melodia.",
  });

  if (content.melody.length >= 4) {
    const excerpt = content.melody.slice(0, 5);
    exercises.push({
      type: "ORDERING",
      phase: "PRACTICE",
      prompt: `Ordena estas notas para formar el comienzo de "${def.title}"`,
      data: ord(excerpt, clef),
      explanation: "Este es el orden real de la melodia.",
    });
  }

  if (content.melody.length >= 3) {
    const blankIndex = Math.floor(content.melody.length / 2);
    const blankNote = content.melody[blankIndex];
    const blankOptions = uniq([toSolfege(blankNote), ...distractorLetters(onlyLetter(blankNote)).map((l) => toSolfege(`${l}4`))]);
    exercises.push({
      type: "FILL_BLANK",
      phase: "PRACTICE",
      prompt: `Completa la nota que falta en "${def.title}"`,
      data: fb(clef, content.melody.slice(0, blankIndex), content.melody.slice(blankIndex + 1), blankOptions, toSolfege(blankNote)),
      explanation: `La nota que falta es ${toSolfege(blankNote)}.`,
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
      phase: "PRACTICE",
      prompt: "¿Que acorde es este? (aparece en la pieza)",
      data: ch(chordNotes[0], chordNotes, spanishName, options),
      explanation: `${symbol} se llama "${spanishName}" en espanol.`,
    });
  }

  if (featured.length >= 2) {
    const rootNote = featured[0];
    const otherNote = pick(featured, weekNum + 1);
    const answer = intervalName(rootNote, otherNote);
    const distractorPool = ["2da mayor", "3ra mayor", "4ta justa", "5ta justa", "6ta mayor", "Octava"].filter((n) => n !== answer);
    exercises.push({
      type: "INTERVAL",
      phase: "PRACTICE",
      prompt: `¿Que distancia (intervalo) hay entre estas dos notas de la pieza?`,
      data: iv(rootNote, answer, uniq([answer, distractorPool[0], distractorPool[1]])),
      explanation: `Entre ${toSolfege(rootNote)} y ${toSolfege(otherNote)} hay una ${answer}.`,
    });
  }

  exercises.push({
    type: "EAR_TRAINING",
    phase: "PRACTICE",
    prompt: `Escucha el comienzo de "${def.title}"... ¿cual es la primera nota?`,
    data: et("note", toSolfege(content.melody[0]), uniq([toSolfege(content.melody[0]), ...distractorLetters(onlyLetter(content.melody[0])).map((l) => toSolfege(`${l}4`))]), [content.melody[0]]),
    explanation: `La pieza empieza en ${toSolfege(content.melody[0])}.`,
  });

  return exercises;
}

// --- Fase 3: A tocar (interpretacion, voz, repaso) ---
function performanceExercises(def: PieceDef, weekNum: number): ExerciseDef[] {
  const { content } = def;
  const clef = content.clef === "bass" ? "bass" : "treble";
  const exercises: ExerciseDef[] = [];

  exercises.push({
    type: "KEYBOARD_PLAY",
    phase: "PERFORMANCE",
    prompt: `¡Toca la mano derecha de "${def.title}"!`,
    data: kp(content.melody, clef, genericBpmFor(def)),
    explanation: content.isDuet ? "Recuerda: esta pieza se toca a duo, con tu profesora o tu familia acompanando." : "Tocala con calma y luego un poco mas rapido.",
  });

  if (content.bass && content.bass.length > 0) {
    exercises.push({
      type: "KEYBOARD_PLAY",
      phase: "PERFORMANCE",
      prompt: `Ahora toca la mano izquierda de "${def.title}"`,
      data: kp(content.bass, "bass", genericBpmFor(def)),
      explanation: "La mano izquierda suele llevar el acompanamiento.",
    });
  }

  exercises.push({
    type: "SCROLLING_PLAY",
    phase: "PERFORMANCE",
    prompt: `¡Modo partitura en marcha! Toca "${def.title}" cuando cada nota llegue a la linea`,
    data: scp(content.melody, content.melodyRhythm, genericBpmFor(def), clef),
    explanation: "Tocar siguiendo el tempo real es el ultimo paso antes de dominar la pieza.",
  });

  if (content.featuredNotes.length >= 3) {
    exercises.push({
      type: "EAR_BUILD",
      phase: "PERFORMANCE",
      prompt: `Dictado de oido: reconstruye esta frase de "${def.title}" nota a nota, solo escuchando`,
      data: eb(content.featuredNotes.slice(0, 4)),
      explanation: "Escuchar y reproducir sin ver la partitura es el entrenamiento de oido mas completo.",
    });
  }

  const note3 = pick(content.featuredNotes, weekNum + 2);
  exercises.push({
    type: "SPEAK_ALOUD",
    phase: "PERFORMANCE",
    prompt: "Di en voz alta el nombre de esta nota",
    data: sp(toSolfege(note3), [onlyLetter(note3)], note3),
    explanation: `Es un ${toSolfege(note3)}. Si tu navegador no soporta el microfono, puedes omitir este ejercicio.`,
  });

  exercises.push({
    type: "THEORY_MCQ",
    phase: "PERFORMANCE",
    prompt: `¡Muy bien! ¿Como se titula la pieza de esta semana?`,
    data: mcq(`¡Muy bien! ¿Como se titula la pieza de esta semana?`, uniq([def.title, "Para Elisa", "Claro de Luna"]).slice(0, 3), def.title),
    explanation: `Llevala a tu proxima clase presencial con Azucena.`,
  });

  return exercises;
}

/** Genera las lecciones semanales (weekIndex 1..durationWeeks) para una pieza asignada.
 * Cada semana es una sesion completa de 10-15 min: calentamiento + trabajo de la pieza + interpretacion. */
export function generateLessonsForPiece(def: PieceDef, durationWeeks: number): LessonDef[] {
  const weeks = Math.max(1, durationWeeks);
  const lessons: LessonDef[] = [];

  for (let w = 1; w <= weeks; w++) {
    const exercises = [...warmupExercises(def, w), ...pieceWorkExercises(def, w), ...performanceExercises(def, w)];
    lessons.push({
      title: def.title,
      description:
        weeks === 1
          ? `Sesion unica de "${def.title}": calentamiento, practica completa e interpretacion.`
          : `Semana ${w} de ${weeks} con "${def.title}": calentamiento, practica e interpretacion.`,
      xpReward: 20 + def.difficultyTier * 2,
      exercises,
    });
  }

  return lessons;
}
