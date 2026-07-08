// Frases de Misol, la mascota buho de t-clas, que acompana al alumno por toda la app.

function pick(arr: string[]): string {
  return arr[Math.floor(Math.random() * arr.length)];
}

export function greetingMessage(name: string, streakCurrent: number): string {
  if (streakCurrent >= 7) {
    return pick([
      `¡${name}! Llevas ${streakCurrent} dias seguidos practicando. ¡Eres una maquina!`,
      `${streakCurrent} dias de racha, ${name}. ¡Estoy muy orgulloso de ti!`,
    ]);
  }
  if (streakCurrent >= 1) {
    return pick([
      `¡Hola, ${name}! Llevas ${streakCurrent} ${streakCurrent === 1 ? "dia" : "dias"} seguidos. ¡Sigamos asi!`,
      `¡${name}! Tu racha va por ${streakCurrent}. Vamos a por otra semana.`,
    ]);
  }
  return pick([
    `¡Hola, ${name}! Soy Misol. ¿Empezamos a tocar un rato?`,
    `¡${name}! Que ganas de practicar contigo hoy.`,
    `¡Bienvenido/a, ${name}! Vamos a por tu proxima semana de piano.`,
  ]);
}

export function correctMessage(): string {
  return pick([
    "¡Eso es!",
    "¡Perfecto!",
    "¡Muy bien!",
    "¡Lo has clavado!",
    "¡Asi me gusta!",
    "¡Genial!",
    "¡Toma ya!",
  ]);
}

export function wrongMessage(): string {
  return pick([
    "Casi. ¡Prueba otra vez!",
    "No pasa nada, ¡a por la siguiente!",
    "Todos nos equivocamos practicando. ¡Sigue!",
    "Uy, esa no era. ¡Tu puedes!",
    "Fijate bien y lo tendras.",
  ]);
}

export function lessonCompleteMessage(stars: number, pieceTitle: string): string {
  if (stars >= 3) {
    return pick([
      `¡Increible! Te has salido con "${pieceTitle}". ¡3 estrellas!`,
      `¡Menudo nivel! Has bordado esta semana de "${pieceTitle}".`,
    ]);
  }
  if (stars >= 1) {
    return pick([
      `¡Muy bien! Has superado esta semana de "${pieceTitle}".`,
      `¡Bien hecho! Ya vas dominando "${pieceTitle}".`,
    ]);
  }
  return pick([
    "No has llegado esta vez, pero seguro que a la siguiente si. ¡Vamos!",
    "Un poco mas de practica y lo consigues. ¡No te rindas!",
  ]);
}

export function pieceIntroMessage(pieceTitle: string): string {
  return pick([
    `Esta semana toca "${pieceTitle}". ¡Vamos a descubrirla juntos!`,
    `"${pieceTitle}"... ¡una de mis piezas favoritas! Mira lo que he preparado.`,
    `¿Preparado/a para "${pieceTitle}"? Aqui tienes todo lo que necesitas saber.`,
  ]);
}

export function landingMessage(): string {
  return pick([
    "¡Hola! Soy Misol, tu guia en t-clas. ¡Vamos a tocar piano!",
    "¡Bienvenido/a a t-clas! Soy Misol y te voy a acompanar en cada leccion.",
  ]);
}
