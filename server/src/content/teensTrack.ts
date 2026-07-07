import { TrackDef, nn, sr, rt, et, mcq, kp, iv, ch } from "./defs";

export const teensTrack: TrackDef = {
  code: "teens",
  name: "Piano Level Up",
  description: "Ritmo, acordes y canciones actuales para adolescentes de 12 a 17 anos.",
  minAge: 12,
  maxAge: 17,
  order: 2,
  levels: [
    {
      title: "Bases Solidas",
      description: "Teclado, claves, ritmo y tu primer riff.",
      iconEmoji: "🎧",
      units: [
        {
          title: "El teclado y las claves",
          description: "Clave de Sol, clave de Fa y alteraciones.",
          lessons: [
            {
              title: "Clave de Sol y clave de Fa",
              description: "Las dos claves del piano.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "¿Que clave se usa habitualmente para la mano izquierda?", data: mcq("¿Que clave se usa habitualmente para la mano izquierda?", ["Clave de Fa", "Clave de Sol", "Clave de Do"], "Clave de Fa"), explanation: "La clave de Fa cubre el registro grave, tipico de la mano izquierda." },
                { type: "THEORY_MCQ", prompt: "La clave de Sol se usa normalmente para...", data: mcq("La clave de Sol se usa normalmente para...", ["La mano derecha / notas agudas", "La mano izquierda / notas graves", "Ninguna de las dos"], "La mano derecha / notas agudas"), explanation: "El registro agudo suele escribirse en clave de Sol." },
                { type: "NOTE_NAME", prompt: "En clave de Fa, ¿que nota es esta?", data: nn("bass", "C3", ["Do", "Re", "Mi"], "Do"), explanation: "Es el Do una octava por debajo del Do central." },
              ],
            },
            {
              title: "Todas las notas naturales",
              description: "Repaso rapido de Do a Si.",
              exercises: [
                { type: "NOTE_NAME", prompt: "¿Como se llama esta nota?", data: nn("treble", "F4", ["Fa", "Sol", "La"], "Fa"), explanation: "Fa esta justo despues de Mi." },
                { type: "NOTE_NAME", prompt: "¿Como se llama esta nota?", data: nn("treble", "A4", ["Fa", "Sol", "La"], "La"), explanation: "La esta entre Sol y Si." },
                { type: "NOTE_NAME", prompt: "¿Como se llama esta nota?", data: nn("treble", "B4", ["Si", "La", "Do"], "Si"), explanation: "Si es la ultima nota antes de repetir el Do." },
                { type: "STAFF_READING", prompt: "Lee y toca esta secuencia", data: sr("treble", ["C4", "E4", "G4", "B4", "G4", "E4"]), explanation: "Un arpegio que sube y baja." },
              ],
            },
            {
              title: "Sostenidos y bemoles",
              description: "Las alteraciones y las teclas negras.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "Un sostenido (#) sube la nota...", data: mcq("Un sostenido (#) sube la nota...", ["Medio tono", "Un tono entero", "Una octava"], "Medio tono"), explanation: "El sostenido siempre sube medio tono (un semitono)." },
                { type: "THEORY_MCQ", prompt: "Un bemol (♭) baja la nota...", data: mcq("Un bemol (♭) baja la nota...", ["Medio tono", "Un tono entero", "Una octava"], "Medio tono"), explanation: "El bemol baja medio tono." },
                { type: "KEYBOARD_PLAY", prompt: "Toca Do, Do sostenido y Re", data: kp(["C4", "C#4", "D4"], "treble", 90), explanation: "Do# es la tecla negra entre Do y Re." },
              ],
            },
          ],
        },
        {
          title: "Ritmo y pulso",
          description: "Corcheas, sincopa y groove.",
          lessons: [
            {
              title: "Corcheas y sincopa ligera",
              description: "Ritmos que 'sorprenden' al oido.",
              exercises: [
                { type: "RHYTHM_TAP", prompt: "Marca este ritmo", data: rt(100, [0.5, 0.5, 1, 0.5, 0.5, 1]), explanation: "Corchea-corchea-negra, dos veces." },
                { type: "THEORY_MCQ", prompt: "La sincopa es...", data: mcq("La sincopa es...", ["Un acento en un tiempo debil, que 'sorprende' al oido", "Silencio total", "Solo notas graves"], "Un acento en un tiempo debil, que 'sorprende' al oido"), explanation: "Muy usada en pop, funk y jazz." },
              ],
            },
            {
              title: "Corcheas con puntillo y semicorcheas",
              description: "Ritmos mas complejos.",
              exercises: [
                { type: "RHYTHM_TAP", prompt: "Marca este ritmo con puntillo", data: rt(90, [1.5, 0.5, 1, 1]), explanation: "El puntillo alarga la nota la mitad de su valor." },
                { type: "THEORY_MCQ", prompt: "Un puntillo junto a una nota...", data: mcq("Un puntillo junto a una nota...", ["Suma la mitad de su duracion", "La resta a la mitad", "No cambia nada"], "Suma la mitad de su duracion"), explanation: "Por ejemplo, una negra con puntillo dura 1.5 tiempos." },
              ],
            },
            {
              title: "Groove de pop",
              description: "Un patron ritmico tipico de canciones actuales.",
              exercises: [
                { type: "RHYTHM_TAP", prompt: "Marca este groove", data: rt(96, [1, 0.5, 0.5, 1, 1]), explanation: "La base de muchisimas canciones pop." },
                { type: "KEYBOARD_PLAY", prompt: "Toca este patron de acompanamiento", data: kp(["C4", "E4", "G4", "E4"], "treble", 96), explanation: "Un patron de acorde roto muy usado en pop." },
              ],
            },
          ],
        },
        {
          title: "Tu primer riff",
          description: "Intervalos y tu primera melodia con actitud.",
          lessons: [
            {
              title: "Intervalos: 2das y 3ras",
              description: "La distancia entre dos notas.",
              exercises: [
                { type: "INTERVAL", prompt: "¿Que intervalo hay entre Do y Mi?", data: iv("C4", "3ra mayor", ["2da mayor", "3ra mayor", "5ta justa"]), explanation: "De Do a Mi hay una tercera mayor." },
                { type: "INTERVAL", prompt: "¿Que intervalo hay entre Do y Sol?", data: iv("C4", "5ta justa", ["3ra menor", "5ta justa", "Octava"]), explanation: "De Do a Sol hay una quinta justa, muy estable y consonante." },
              ],
            },
            {
              title: "Riff sencillo",
              description: "Tu primer riff estilo pop-rock.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca este riff estilo pop-rock", data: kp(["E4", "G4", "A4", "G4", "E4"], "treble", 100), explanation: "Un riff corto y pegadizo con solo 3 notas distintas." },
                { type: "EAR_TRAINING", prompt: "¿La melodia sube o baja?", data: et("interval", "Sube", ["Sube", "Baja"], ["E4", "A4"]), explanation: "De Mi a La la nota sube." },
              ],
            },
            {
              title: "Tu primera cancion completa",
              description: "Junta todo lo aprendido en este nivel.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca esta melodia completa", data: kp(["C4", "E4", "G4", "A4", "G4", "E4", "C4"], "treble", 100), explanation: "¡Enhorabuena, terminaste tu primer nivel!" },
                { type: "RHYTHM_TAP", prompt: "Marca este ritmo final", data: rt(100, [1, 1, 0.5, 0.5, 1, 2]), explanation: "Combina negras, corcheas y una blanca final." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Acordes y Progresiones",
      description: "Triadas mayores y menores, y la progresion favorita del pop.",
      iconEmoji: "🎸",
      units: [
        {
          title: "Triadas mayores y menores",
          description: "La diferencia esta en la tercera.",
          lessons: [
            {
              title: "Acordes mayores",
              description: "Triadas mayores basicas.",
              exercises: [
                { type: "CHORD", prompt: "¿Que acorde es este?", data: ch("C4", ["C4", "E4", "G4"], "Do Mayor", ["Do Mayor", "Do menor", "Fa Mayor"]), explanation: "Do-Mi-Sol: triada mayor." },
                { type: "KEYBOARD_PLAY", prompt: "Toca este acorde", data: kp(["C4", "E4", "G4"], "treble", 90), explanation: "Practica tocando las 3 notas a la vez." },
              ],
            },
            {
              title: "Acordes menores",
              description: "Triadas menores, mas melancolicas.",
              exercises: [
                { type: "CHORD", prompt: "¿Que acorde es este?", data: ch("A4", ["A4", "C5", "E5"], "La menor", ["La Mayor", "La menor", "Mi menor"]), explanation: "La-Do-Mi: triada menor, sonido mas melancolico." },
                { type: "THEORY_MCQ", prompt: "La diferencia entre un acorde mayor y uno menor esta en...", data: mcq("La diferencia entre un acorde mayor y uno menor esta en...", ["La tercera (mayor o menor)", "La quinta", "El bajo"], "La tercera (mayor o menor)"), explanation: "Bajar medio tono la tercera convierte un acorde mayor en menor." },
              ],
            },
          ],
        },
        {
          title: "La progresion I-V-vi-IV",
          description: "La progresion mas famosa del pop.",
          lessons: [
            {
              title: "La progresion mas famosa del pop",
              description: "Presente en cientos de canciones.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "La progresion I-V-vi-IV (Do-Sol-Lam-Fa) aparece en muchisimas canciones pop.", data: mcq("La progresion I-V-vi-IV (Do-Sol-Lam-Fa) aparece en muchisimas canciones pop.", ["Verdadero", "Falso"], "Verdadero"), explanation: "Es una de las progresiones mas usadas en la musica popular." },
                { type: "KEYBOARD_PLAY", prompt: "Toca la progresion Do - Sol - Lam - Fa", data: kp(["C4", "E4", "G4", "G4", "B4", "D5", "A4", "C5", "E5", "F4", "A4", "C5"], "treble", 90), explanation: "I - V - vi - IV en la tonalidad de Do Mayor." },
              ],
            },
            {
              title: "Compon con la progresion",
              description: "Usa la progresion para crear algo tuyo.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca Do Mayor seguido de La menor", data: kp(["C4", "E4", "G4", "A4", "C5", "E5"], "treble", 95), explanation: "El cambio de I a vi es muy usado para dar un giro emocional." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Lectura a Primera Vista",
      description: "Lee musica que nunca has visto, con ambas manos.",
      iconEmoji: "👀",
      units: [
        {
          title: "Ambas claves a la vez",
          description: "Coordinar clave de Sol y clave de Fa.",
          lessons: [
            {
              title: "Manos por separado",
              description: "Lee cada mano de forma independiente.",
              exercises: [
                { type: "STAFF_READING", prompt: "Lee y toca con la mano derecha", data: sr("treble", ["C4", "E4", "G4", "E4"]), explanation: "Un pequeno arpegio en clave de Sol." },
                { type: "STAFF_READING", prompt: "Lee y toca con la mano izquierda", data: sr("bass", ["C3", "G3", "C3"]), explanation: "Notas en clave de Fa, registro grave." },
              ],
            },
            {
              title: "Coordinacion de manos",
              description: "Combina ambas manos.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Mano derecha: Do-Mi-Sol", data: kp(["C4", "E4", "G4"], "treble", 90), explanation: "Preparate para combinarlo con la mano izquierda." },
                { type: "KEYBOARD_PLAY", prompt: "Mano izquierda: Do-Sol grave", data: kp(["C3", "G3"], "bass", 90), explanation: "Una quinta grave de acompanamiento." },
              ],
            },
          ],
        },
        {
          title: "Melodias a primera vista",
          description: "Practica leer sin haber visto antes la partitura.",
          lessons: [
            {
              title: "Lectura rapida 1",
              description: "Primer ejercicio de lectura sorpresa.",
              exercises: [
                { type: "STAFF_READING", prompt: "Lee y toca esta melodia por primera vez", data: sr("treble", ["D4", "F4", "A4", "F4", "D4"]), explanation: "Un arpegio de Re menor." },
              ],
            },
            {
              title: "Lectura rapida 2",
              description: "Segundo ejercicio de lectura sorpresa.",
              exercises: [
                { type: "STAFF_READING", prompt: "Lee y toca esta melodia por primera vez", data: sr("treble", ["G4", "B4", "D5", "B4", "G4"]), explanation: "Un arpegio de Sol Mayor." },
                { type: "THEORY_MCQ", prompt: "Leer a primera vista significa...", data: mcq("Leer a primera vista significa...", ["Tocar una partitura que no has visto antes", "Memorizar una pieza", "Tocar de oido"], "Tocar una partitura que no has visto antes"), explanation: "Es una habilidad clave para cualquier pianista." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Tus Canciones Favoritas",
      description: "Pop actual y baladas.",
      iconEmoji: "🎤",
      units: [
        {
          title: "Pop actual",
          description: "Acordes y progresiones de canciones actuales.",
          lessons: [
            {
              title: "Acordes con cejilla simplificados",
              description: "Sol Mayor y Mi menor al piano.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca el acorde de Sol Mayor", data: kp(["G4", "B4", "D5"], "treble", 90), explanation: "Sol-Si-Re." },
                { type: "KEYBOARD_PLAY", prompt: "Toca el acorde de Mi menor", data: kp(["E4", "G4", "B4"], "treble", 90), explanation: "Mi-Sol-Si, uno de los acordes menores mas usados." },
              ],
            },
            {
              title: "Tu primer cover",
              description: "Una progresion tipica de radio.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca esta progresion de acordes (uno por tiempo)", data: kp(["C4", "G4", "A4", "F4"], "treble", 90), explanation: "I - V - vi - IV, otra vez presente." },
              ],
            },
          ],
        },
        {
          title: "Balada",
          description: "Arpegios suaves para acompanar.",
          lessons: [
            {
              title: "Arpegios para balada",
              description: "Notas de un acorde tocadas una a una.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca este arpegio de Do Mayor", data: kp(["C4", "E4", "G4", "E4"], "treble", 80), explanation: "Un patron de arpegio suave, ideal para baladas." },
              ],
            },
            {
              title: "Tu balada completa",
              description: "Combina arpegios en una progresion.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca esta secuencia de arpegios", data: kp(["C4", "E4", "G4", "E4", "A4", "C5", "E5", "C5"], "treble", 80), explanation: "Do Mayor seguido de La menor, en arpegio." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Tecnica y Estilo",
      description: "Escalas, arpegios y tu propio sonido.",
      iconEmoji: "🔥",
      units: [
        {
          title: "Escalas y arpegios",
          description: "Mas alla de Do Mayor.",
          lessons: [
            {
              title: "Escala de Sol Mayor",
              description: "Tu segunda escala mayor.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca la escala de Sol Mayor (con Fa sostenido)", data: kp(["G4", "A4", "B4", "C5", "D5", "E5", "F#5", "G5"], "treble", 100), explanation: "Sol Mayor tiene un sostenido: Fa#." },
              ],
            },
            {
              title: "Arpegios en triadas basicas",
              description: "Practica arpegios de Do y Sol Mayor.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca este arpegio", data: kp(["C4", "E4", "G4", "C5"], "treble", 100), explanation: "Arpegio de Do Mayor con octava." },
                { type: "KEYBOARD_PLAY", prompt: "Toca este arpegio", data: kp(["G4", "B4", "D5", "G5"], "treble", 100), explanation: "Arpegio de Sol Mayor con octava." },
              ],
            },
          ],
        },
        {
          title: "Tu estilo personal",
          description: "Crea tu propio proyecto musical.",
          lessons: [
            {
              title: "Groove lo-fi",
              description: "Un patron relajado y actual.",
              exercises: [
                { type: "RHYTHM_TAP", prompt: "Marca este groove lo-fi", data: rt(80, [1, 0.5, 0.5, 1, 1]), explanation: "Un ritmo relajado, tipico del estilo lo-fi." },
                { type: "KEYBOARD_PLAY", prompt: "Toca este acompanamiento", data: kp(["C4", "E4", "G4", "E4"], "treble", 80), explanation: "Combina el groove con este arpegio suave." },
              ],
            },
            {
              title: "Proyecto final: tu cancion",
              description: "Combina todo lo aprendido en este camino.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca tu composicion final combinando acordes y melodia", data: kp(["C4", "E4", "G4", "A4", "F4", "G4", "C4"], "treble", 95), explanation: "¡Enhorabuena! Has completado el camino Piano Level Up." },
              ],
            },
          ],
        },
      ],
    },
  ],
};
