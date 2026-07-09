// Generador de sesiones semanales a partir del contenido musical real de una pieza.
// Cada semana se estructura en 4 bloques, tal como pidio Azucena:
// 1. Agilidad visual (nombrar notas rapido, clave de Sol y clave de Fa)
// 2. Agudeza auditiva (reconocer u tocar de oido, registro agudo y grave)
// 3. Notas al vuelo (tirada larga de notas contrarreloj)
// 4. Practica de partitura: primero ejercicios variados sobre la pieza real,
//    despues practica directa al piano (incluido por tramos, para poder
//    ensayar la pieza facilmente entre sesion y sesion con la profesora).
// Esta es la pieza clave que permite "replicar" el sistema para cualquier alumno:
// una vez una Pieza esta en la biblioteca, asignarla genera automaticamente
// toda la sesion semanal derivada de su musica real.

import { PieceDef, LessonDef, ExerciseDef, nn, sr, rt, et, mcq, kp, ch, iv, wa, ma, ord, sp, ds, hn, scp, fb, eb, nd, sgp } from "./content/defs";
import { toSolfege, onlyLetter, distractorLetters, chordSymbolToNotes, chordSymbolToSpanish, scaleForKey, scaleForKeyBass, intervalName, parseNote } from "./notes";
import { DifficultyAdjustment, DifficultyLevel, NORMAL_DIFFICULTY } from "./adaptive";

// Cuantos distractores (opciones incorrectas) se ofrecen en preguntas de
// reconocimiento de nota, segun la dificultad ajustada al alumno.
function distractorCountFor(level: DifficultyLevel): number {
  return level === "hard" ? 3 : level === "easy" ? 1 : 2;
}

function uniq<T>(arr: T[]): T[] {
  return Array.from(new Set(arr));
}

function pick<T>(arr: T[], index: number): T {
  return arr[((index % arr.length) + arr.length) % arr.length];
}

function chunk<T>(arr: T[], size: number): T[][] {
  const chunks: T[][] = [];
  for (let i = 0; i < arr.length; i += size) chunks.push(arr.slice(i, i + size));
  return chunks;
}

function genericBpmFor(def: PieceDef): number {
  return def.difficultyTier <= 2 ? 84 : def.difficultyTier <= 4 ? 96 : 108;
}

// --- Bloque 1: Agilidad visual (nombrar notas rapido, clave de Sol Y clave de Fa) ---
function visualAgilityExercises(def: PieceDef, weekNum: number, level: DifficultyLevel = "normal"): ExerciseDef[] {
  const trebleScale = scaleForKey(def.keySignature);
  const bassScale = scaleForKeyBass(def.keySignature);
  const distractorCount = distractorCountFor(level);
  const exercises: ExerciseDef[] = [];

  for (let i = 0; i < 3; i++) {
    const trebleNote = pick(trebleScale, weekNum + i);
    exercises.push({
      type: "NOTE_NAME",
      phase: "VISUAL_AGILITY",
      prompt: "Agilidad visual: ¿como se llama esta nota? (clave de Sol)",
      data: nn("treble", trebleNote, uniq([toSolfege(trebleNote), ...distractorLetters(onlyLetter(trebleNote), distractorCount).map((l) => toSolfege(`${l}4`))]), toSolfege(trebleNote)),
      explanation: "Reconocer notas rapido en clave de Sol es la base de la lectura a primera vista.",
    });

    const bassNote = pick(bassScale, weekNum + i + 2);
    exercises.push({
      type: "NOTE_NAME",
      phase: "VISUAL_AGILITY",
      prompt: "Agilidad visual: ¿como se llama esta nota? (clave de Fa)",
      data: nn("bass", bassNote, uniq([toSolfege(bassNote), ...distractorLetters(onlyLetter(bassNote), distractorCount).map((l) => toSolfege(`${l}4`))]), toSolfege(bassNote)),
      explanation: "La clave de Fa es la de la mano izquierda: cuanto mas la practiques, mas facil se vuelve.",
    });
  }

  return exercises;
}

// --- Bloque 2: Agudeza auditiva (escuchar nota/melodia/acorde, clave de Sol y de Fa, o tocar lo escuchado) ---
function earAcuityExercises(def: PieceDef, weekNum: number, level: DifficultyLevel = "normal"): ExerciseDef[] {
  const { content } = def;
  const trebleScale = scaleForKey(def.keySignature);
  const bassScale = scaleForKeyBass(def.keySignature);
  const distractorCount = distractorCountFor(level);
  const exercises: ExerciseDef[] = [];

  const trebleNote = pick(trebleScale, weekNum + 1);
  exercises.push({
    type: "EAR_TRAINING",
    phase: "EAR_ACUITY",
    prompt: "Agudeza auditiva: escucha... ¿que nota es? (registro agudo, clave de Sol)",
    data: et("note", toSolfege(trebleNote), uniq([toSolfege(trebleNote), ...distractorLetters(onlyLetter(trebleNote), distractorCount).map((l) => toSolfege(`${l}4`))]), [trebleNote]),
    explanation: `Has escuchado un ${toSolfege(trebleNote)}.`,
  });

  const bassNote = pick(bassScale, weekNum + 3);
  exercises.push({
    type: "EAR_TRAINING",
    phase: "EAR_ACUITY",
    prompt: "Agudeza auditiva: escucha... ¿que nota es? (registro grave, clave de Fa)",
    data: et("note", toSolfege(bassNote), uniq([toSolfege(bassNote), ...distractorLetters(onlyLetter(bassNote), distractorCount).map((l) => toSolfege(`${l}4`))]), [bassNote]),
    explanation: `Has escuchado un ${toSolfege(bassNote)}, en el registro grave de la clave de Fa.`,
  });

  if (content.chordsUsed && content.chordsUsed.length > 0) {
    const symbol = pick(content.chordsUsed, weekNum);
    const chordNotes = chordSymbolToNotes(symbol);
    const spanishName = chordSymbolToSpanish(symbol);
    const otherSymbols = content.chordsUsed.filter((s) => s !== symbol);
    const options = uniq([spanishName, ...otherSymbols.slice(0, 2).map(chordSymbolToSpanish), "Do Mayor"]).slice(0, 3);
    exercises.push({
      type: "CHORD",
      phase: "EAR_ACUITY",
      prompt: "Escucha este acorde de la pieza... ¿cual es?",
      data: ch(chordNotes[0], chordNotes, spanishName, options),
      explanation: `${symbol} se llama "${spanishName}" en espanol.`,
    });
  } else {
    const rootNote = content.featuredNotes[0];
    const otherNote = pick(content.featuredNotes, weekNum + 1);
    const answer = intervalName(rootNote, otherNote);
    const distractorPool = ["2da mayor", "3ra mayor", "4ta justa", "5ta justa", "6ta mayor", "Octava"].filter((n) => n !== answer);
    exercises.push({
      type: "INTERVAL",
      phase: "EAR_ACUITY",
      prompt: "Escucha estas dos notas de la pieza... ¿que intervalo forman?",
      data: iv(rootNote, answer, uniq([answer, distractorPool[0], distractorPool[1]])),
      explanation: `Entre ${toSolfege(rootNote)} y ${toSolfege(otherNote)} hay una ${answer}.`,
    });
  }

  if (content.featuredNotes.length >= 3) {
    exercises.push({
      type: "EAR_BUILD",
      phase: "EAR_ACUITY",
      prompt: `Escucha y toca: reconstruye esta frase de "${def.title}" nota a nota, solo de oido`,
      data: eb(content.featuredNotes.slice(0, 4)),
      explanation: "Tocar lo que escuchas, sin ver la partitura, es el entrenamiento de oido mas completo.",
    });
  }

  return exercises;
}

// --- Bloque 3: Notas al vuelo (tirada larga de notas contrarreloj) ---
function noteRushExercises(def: PieceDef, weekNum: number, level: DifficultyLevel = "normal"): ExerciseDef[] {
  const clef = def.content.clef === "bass" ? "bass" : "treble";
  const scale = clef === "bass" ? scaleForKeyBass(def.keySignature) : scaleForKey(def.keySignature);
  const lengthAdjust = level === "hard" ? 3 : level === "easy" ? -3 : 0;
  const dashLength = Math.max(6, 10 + (weekNum % 3) * 2 + lengthAdjust);
  const notes: string[] = [];
  for (let i = 0; i < dashLength; i++) notes.push(pick(scale, weekNum * 3 + i * 5));
  const timeMultiplier = level === "hard" ? 0.85 : level === "easy" ? 1.3 : 1;
  const timeLimitSec = Math.round(dashLength * 2.2 * timeMultiplier);

  return [
    {
      type: "NOTE_DASH",
      phase: "NOTE_RUSH",
      prompt: `Notas al vuelo: toca estas ${dashLength} notas antes de que se acabe el tiempo`,
      data: nd(clef, notes, timeLimitSec),
      explanation: "La velocidad se entrena poco a poco: cada semana el reto crece un poco mas.",
    },
  ];
}

// --- Bloque 4: Practica de partitura (variada + directa al piano, por tramos) ---
function sheetPracticeExercises(def: PieceDef, weekNum: number): ExerciseDef[] {
  const { content } = def;
  const clef = content.clef === "bass" ? "bass" : "treble";
  const exercises: ExerciseDef[] = [];
  const featured = content.featuredNotes.slice(0, 6);

  // --- Parte A: ejercicios variados aplicados a la pieza real ---
  exercises.push({
    type: "THEORY_MCQ",
    phase: "SHEET_PRACTICE",
    prompt: `¿En que compas esta escrita "${def.title}"?`,
    data: mcq(`¿En que compas esta escrita "${def.title}"?`, uniq([def.timeSignature, "3/4", "4/4", "6/8"]).slice(0, 3), def.timeSignature),
    explanation: `"${def.title}" esta escrita en ${def.timeSignature}, en la tonalidad de ${def.keySignature}.`,
  });

  featured.forEach((note, i) => {
    const letter = onlyLetter(note);
    const options = uniq([toSolfege(note), ...distractorLetters(letter).map((l) => toSolfege(`${l}4`))]);
    if (i % 2 === 0) {
      exercises.push({
        type: "NOTE_NAME",
        phase: "SHEET_PRACTICE",
        prompt: "¿Como se llama esta nota de la pieza?",
        data: nn(clef, note, options, toSolfege(note)),
        explanation: `Esta nota aparece en "${def.title}".`,
      });
    } else {
      exercises.push({
        type: "WRITE_ANSWER",
        phase: "SHEET_PRACTICE",
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
      phase: "SHEET_PRACTICE",
      prompt: `Relaciona cada nota de "${def.title}" con su nombre`,
      data: ma(pairs),
      explanation: "Estas son las notas principales de la pieza.",
    });
  }

  // Arrastrar sobre el pentagrama solo puede soltar en posiciones naturales (sin
  // sostenido/bemol), asi que la nota objetivo tiene que ser siempre natural o
  // el ejercicio seria imposible de completar.
  const naturalFeatured = featured.filter((n) => parseNote(n).accidental === 0);
  const dragNote = pick(naturalFeatured.length > 0 ? naturalFeatured : featured, weekNum + 4);
  exercises.push({
    type: "DRAG_STAFF",
    phase: "SHEET_PRACTICE",
    prompt: `Arrastra la nota "${toSolfege(dragNote)}" hasta su sitio correcto en el pentagrama`,
    data: ds(clef, toSolfege(dragNote), dragNote),
    explanation: `${toSolfege(dragNote)} (${dragNote}) es una de las notas de "${def.title}".`,
  });

  const sightExcerpt = content.melody.slice(0, Math.min(10, content.melody.length));
  exercises.push({
    type: "STAFF_READING",
    phase: "SHEET_PRACTICE",
    prompt: `Lee y toca el comienzo de "${def.title}"`,
    data: sr(clef, sightExcerpt),
    explanation: content.lyricsHook ? `"${content.lyricsHook}"` : `El inicio de "${def.title}".`,
  });

  exercises.push({
    type: "RHYTHM_TAP",
    phase: "SHEET_PRACTICE",
    prompt: `Marca el ritmo real de "${def.title}"`,
    data: rt(genericBpmFor(def), content.melodyRhythm.slice(0, Math.min(10, content.melodyRhythm.length)), def.timeSignature),
    explanation: "Este es el ritmo real de la melodia.",
  });

  if (content.melody.length >= 4) {
    const excerpt = content.melody.slice(0, 5);
    exercises.push({
      type: "ORDERING",
      phase: "SHEET_PRACTICE",
      prompt: `Ordena estas notas para formar el comienzo de "${def.title}"`,
      data: ord(excerpt, clef),
      explanation: "Este es el orden real de la melodia.",
    });
  }

  if (content.melody.length >= 3) {
    const blankIndex = Math.floor(content.melody.length / 2);
    const blankNote = content.melody[blankIndex];
    const windowBefore = content.melody.slice(Math.max(0, blankIndex - 3), blankIndex);
    const windowAfter = content.melody.slice(blankIndex + 1, blankIndex + 4);
    const blankOptions = uniq([toSolfege(blankNote), ...distractorLetters(onlyLetter(blankNote)).map((l) => toSolfege(`${l}4`))]);
    exercises.push({
      type: "FILL_BLANK",
      phase: "SHEET_PRACTICE",
      prompt: `Completa la nota que falta en "${def.title}"`,
      data: fb(clef, windowBefore, windowAfter, blankOptions, toSolfege(blankNote)),
      explanation: `La nota que falta es ${toSolfege(blankNote)}.`,
    });
  }

  if (featured.length >= 2) {
    const rootNote = featured[0];
    const otherNote = pick(featured, weekNum + 1);
    const answer = intervalName(rootNote, otherNote);
    const distractorPool = ["2da mayor", "3ra mayor", "4ta justa", "5ta justa", "6ta mayor", "Octava"].filter((n) => n !== answer);
    exercises.push({
      type: "INTERVAL",
      phase: "SHEET_PRACTICE",
      prompt: `¿Que distancia (intervalo) hay entre estas dos notas de la pieza?`,
      data: iv(rootNote, answer, uniq([answer, distractorPool[0], distractorPool[1]])),
      explanation: `Entre ${toSolfege(rootNote)} y ${toSolfege(otherNote)} hay una ${answer}.`,
    });
  }

  // --- Parte B: practica directa al piano (incluida por tramos) ---
  exercises.push({
    type: "KEYBOARD_PLAY",
    phase: "SHEET_PRACTICE",
    prompt: `¡A tocar de verdad! Toca la mano derecha completa de "${def.title}"`,
    data: kp(content.melody, clef, genericBpmFor(def)),
    explanation: content.isDuet ? "Recuerda: esta pieza se toca a duo, con tu profesora o tu familia acompanando." : "Tocala con calma y luego un poco mas rapido.",
  });

  if (content.bass && content.bass.length > 0) {
    exercises.push({
      type: "KEYBOARD_PLAY",
      phase: "SHEET_PRACTICE",
      prompt: `Ahora toca la mano izquierda completa de "${def.title}"`,
      data: kp(content.bass, "bass", genericBpmFor(def)),
      explanation: "La mano izquierda suele llevar el acompanamiento.",
    });
  }

  exercises.push({
    type: "SCROLLING_PLAY",
    phase: "SHEET_PRACTICE",
    prompt: `¡Modo partitura en marcha! Toca "${def.title}" entera cuando cada nota llegue a la linea`,
    data: scp(content.melody, content.melodyRhythm, genericBpmFor(def), clef),
    explanation: "Tocar la pieza entera siguiendo el tempo real es el paso definitivo antes de dominarla.",
  });

  const segments = chunk(content.melody, 5);
  if (segments.length >= 2) {
    exercises.push({
      type: "SEGMENT_PRACTICE",
      phase: "SHEET_PRACTICE",
      prompt: `Practica "${def.title}" por tramos, a tu ritmo`,
      data: sgp(clef, segments),
      explanation: "Practicar por tramos cortos es la mejor manera de aprenderte una pieza entera. Vuelve aqui siempre que quieras entre clase y clase.",
    });
  }

  const note3 = pick(content.featuredNotes, weekNum + 2);
  exercises.push({
    type: "SPEAK_ALOUD",
    phase: "SHEET_PRACTICE",
    prompt: "Di en voz alta el nombre de esta nota",
    data: sp(toSolfege(note3), [onlyLetter(note3)], note3),
    explanation: `Es un ${toSolfege(note3)}. Si tu navegador no soporta el microfono, puedes omitir este ejercicio.`,
  });

  exercises.push({
    type: "THEORY_MCQ",
    phase: "SHEET_PRACTICE",
    prompt: `¡Muy bien! ¿Como se titula la pieza de esta semana?`,
    data: mcq(`¡Muy bien! ¿Como se titula la pieza de esta semana?`, uniq([def.title, "Para Elisa", "Claro de Luna"]).slice(0, 3), def.title),
    explanation: `Llevala a tu proxima clase presencial con Azucena.`,
  });

  return exercises;
}

/** Genera las lecciones semanales (weekIndex 1..durationWeeks) para una pieza asignada.
 * Cada semana es una sesion de 15-20 min en 4 bloques: agilidad visual, agudeza
 * auditiva, notas al vuelo contrarreloj, y practica de partitura (variada + piano).
 * El parametro adjustment ajusta la dificultad de los 3 primeros bloques segun el
 * acierto historico real del alumno (ver adaptive.ts); por defecto no ajusta nada. */
export function generateLessonsForPiece(def: PieceDef, durationWeeks: number, adjustment: DifficultyAdjustment = NORMAL_DIFFICULTY): LessonDef[] {
  const weeks = Math.max(1, durationWeeks);
  const lessons: LessonDef[] = [];

  for (let w = 1; w <= weeks; w++) {
    const exercises = [
      ...visualAgilityExercises(def, w, adjustment.VISUAL_AGILITY),
      ...earAcuityExercises(def, w, adjustment.EAR_ACUITY),
      ...noteRushExercises(def, w, adjustment.NOTE_RUSH),
      ...sheetPracticeExercises(def, w),
    ];
    lessons.push({
      title: def.title,
      description:
        weeks === 1
          ? `Sesion unica de "${def.title}": agilidad visual, agudeza auditiva, notas al vuelo y practica de partitura.`
          : `Semana ${w} de ${weeks} con "${def.title}": agilidad visual, agudeza auditiva, notas al vuelo y practica de partitura.`,
      xpReward: 20 + def.difficultyTier * 2,
      exercises,
    });
  }

  return lessons;
}
