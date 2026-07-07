import { TrackDef, nn, sr, rt, et, mcq, kp, ch } from "./defs";

export const kidsTrack: TrackDef = {
  code: "kids",
  name: "Los Exploradores del Piano",
  description: "Un camino musical pensado para ninos de 6 a 11 anos: mucho juego, colores y canciones conocidas.",
  minAge: 6,
  maxAge: 11,
  order: 1,
  levels: [
    {
      title: "Primeros Sonidos",
      description: "Descubre el piano, el pentagrama y tus primeras notas.",
      iconEmoji: "🐣",
      units: [
        {
          title: "Conoce tu piano",
          description: "Blancas, negras y tu primer Do.",
          lessons: [
            {
              title: "Teclas blancas y negras",
              description: "Explora el teclado y encuentra los grupos de teclas negras.",
              exercises: [
                {
                  type: "THEORY_MCQ",
                  prompt: "Las teclas negras del piano estan agrupadas en...",
                  data: mcq("Las teclas negras del piano estan agrupadas en...", ["Grupos de 2 y 3", "Grupos de 4 y 5", "Todas juntas"], "Grupos de 2 y 3"),
                  explanation: "Si te fijas bien, las teclas negras siempre forman grupitos de 2 y de 3.",
                },
                {
                  type: "THEORY_MCQ",
                  prompt: "Las teclas negras sirven para...",
                  data: mcq("Las teclas negras sirven para...", ["Tocar sonidos distintos entre las teclas blancas", "Decorar el piano", "No sirven para nada"], "Tocar sonidos distintos entre las teclas blancas"),
                  explanation: "Las teclas negras nos dan sonidos 'intermedios' entre las blancas.",
                },
                {
                  type: "KEYBOARD_PLAY",
                  prompt: "Busca el grupo de 2 teclas negras y toca la tecla blanca justo a su izquierda: ¡es un Do!",
                  data: kp(["C4"], "treble", 90),
                  explanation: "El Do siempre esta a la izquierda de un grupo de 2 teclas negras.",
                },
              ],
            },
            {
              title: "Do Re Mi con las manos",
              description: "Aprende a reconocer y tocar Do, Re y Mi.",
              exercises: [
                { type: "NOTE_NAME", prompt: "¿Como se llama esta nota?", data: nn("treble", "C4", ["Do", "Re", "Mi"], "Do"), explanation: "Esta nota es el Do central del piano." },
                { type: "NOTE_NAME", prompt: "¿Como se llama esta nota?", data: nn("treble", "D4", ["Do", "Re", "Mi"], "Re"), explanation: "Justo despues del Do viene el Re." },
                { type: "NOTE_NAME", prompt: "¿Como se llama esta nota?", data: nn("treble", "E4", ["Do", "Re", "Mi"], "Mi"), explanation: "Despues del Re viene el Mi." },
                { type: "KEYBOARD_PLAY", prompt: "Toca Do, Re y Mi en orden", data: kp(["C4", "D4", "E4"]), explanation: "¡Las tres primeras notas de la escala!" },
              ],
            },
            {
              title: "El pentagrama magico",
              description: "Tu primer vistazo a la partitura.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "¿Cuantas lineas tiene el pentagrama?", data: mcq("¿Cuantas lineas tiene el pentagrama?", ["5", "3", "7"], "5"), explanation: "El pentagrama tiene 5 lineas y 4 espacios." },
                { type: "STAFF_READING", prompt: "Lee y toca esta pequena melodia", data: sr("treble", ["C4", "D4", "E4", "D4", "C4"]), explanation: "Sube de Do a Mi y vuelve a bajar." },
                { type: "EAR_TRAINING", prompt: "Escucha la nota... ¿cual es?", data: et("note", "Do", ["Do", "Mi", "Sol"], ["C4"]), explanation: "El Do central tiene un sonido calido y conocido." },
              ],
            },
          ],
        },
        {
          title: "El ritmo del corazon",
          description: "Negras, blancas, silencios y tu primer ritmo.",
          lessons: [
            {
              title: "Negras y blancas",
              description: "Cuanto dura cada figura musical.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "Una nota negra (♩) dura...", data: mcq("Una nota negra (♩) dura...", ["1 tiempo", "2 tiempos", "Medio tiempo"], "1 tiempo"), explanation: "La negra vale 1 tiempo, la unidad basica del pulso." },
                { type: "THEORY_MCQ", prompt: "Una nota blanca (𝅗𝅥) dura...", data: mcq("Una nota blanca (𝅗𝅥) dura...", ["2 tiempos", "1 tiempo", "4 tiempos"], "2 tiempos"), explanation: "La blanca dura el doble que la negra." },
                { type: "RHYTHM_TAP", prompt: "Marca este ritmo: negra, negra, blanca", data: rt(80, [1, 1, 2], "4/4"), explanation: "1 + 1 + 2 = 4 tiempos, un compas completo." },
              ],
            },
            {
              title: "Los silencios",
              description: "A veces la musica calla, pero el tiempo sigue.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "Un silencio en musica significa...", data: mcq("Un silencio en musica significa...", ["Un momento sin sonido, pero se sigue contando el tiempo", "Un error", "El final de la cancion"], "Un momento sin sonido, pero se sigue contando el tiempo"), explanation: "Los silencios tambien tienen duracion, ¡se cuentan igual!" },
                { type: "RHYTHM_TAP", prompt: "Toca, calla, toca, toca", data: rt(80, [1, 0, 1, 1], "4/4"), explanation: "El 0 representa el silencio: no tocas, pero cuentas el tiempo." },
                { type: "RHYTHM_TAP", prompt: "Blanca, negra, negra", data: rt(90, [2, 1, 1], "4/4"), explanation: "2 + 1 + 1 = 4 tiempos." },
              ],
            },
            {
              title: "Mi primera cancion ritmica",
              description: "Junta ritmo y notas por primera vez.",
              exercises: [
                { type: "RHYTHM_TAP", prompt: "Repite este patron", data: rt(90, [1, 1, 1, 1, 2], "4/4"), explanation: "Cuatro negras y una blanca final." },
                { type: "KEYBOARD_PLAY", prompt: "Toca Do Do Sol Sol, el inicio de una cancion muy conocida", data: kp(["C4", "C4", "G4", "G4"], "treble", 100), explanation: "¡Reconoces el inicio de 'Estrellita'!" },
                { type: "THEORY_MCQ", prompt: "¿Que compas tiene 4 tiempos en cada compas?", data: mcq("¿Que compas tiene 4 tiempos en cada compas?", ["4/4", "3/4", "2/4"], "4/4"), explanation: "El numero de arriba nos dice cuantos tiempos hay por compas." },
              ],
            },
          ],
        },
        {
          title: "Mi primera melodia",
          description: "Toca tu primera cancion completa.",
          lessons: [
            {
              title: "Estrellita donde estas",
              description: "Primera frase de la cancion.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca el comienzo de 'Estrellita donde estas'", data: kp(["C4", "C4", "G4", "G4", "A4", "A4", "G4"], "treble", 90), explanation: "Do Do Sol Sol La La Sol." },
                { type: "STAFF_READING", prompt: "Lee y toca la segunda frase", data: sr("treble", ["F4", "F4", "E4", "E4", "D4", "D4", "C4"]), explanation: "Fa Fa Mi Mi Re Re Do, bajando poco a poco." },
                { type: "EAR_TRAINING", prompt: "¿Suenan igual o diferente estas dos notas?", data: et("interval", "Igual", ["Igual", "Diferente"], ["C4", "C4"]), explanation: "Son la misma nota repetida." },
              ],
            },
            {
              title: "Oido magico",
              description: "Entrena tu oido musical.",
              exercises: [
                { type: "EAR_TRAINING", prompt: "Escucha... ¿cual es esta nota?", data: et("note", "Sol", ["Do", "Mi", "Sol"], ["G4"]), explanation: "El Sol suena mas brillante que el Do." },
                { type: "EAR_TRAINING", prompt: "¿La melodia sube o baja?", data: et("interval", "Sube", ["Sube", "Baja"], ["C4", "G4"]), explanation: "De Do a Sol la nota sube." },
                { type: "EAR_TRAINING", prompt: "¿La melodia sube o baja?", data: et("interval", "Baja", ["Sube", "Baja"], ["G4", "C4"]), explanation: "De Sol a Do la nota baja." },
              ],
            },
            {
              title: "Repaso y mini-concierto",
              description: "Toca Estrellita completa y celebra tu progreso.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca la escala de Do a Sol", data: kp(["C4", "D4", "E4", "F4", "G4"], "treble", 100), explanation: "Las primeras 5 notas de la escala de Do Mayor." },
                { type: "STAFF_READING", prompt: "¡Toca Estrellita completa!", data: sr("treble", ["C4", "C4", "G4", "G4", "A4", "A4", "G4", "F4", "F4", "E4", "E4", "D4", "D4", "C4"]), explanation: "¡Enhorabuena, ya tocaste una cancion entera!" },
                { type: "THEORY_MCQ", prompt: "¿Cual de estas notas es mas aguda?", data: mcq("¿Cual de estas notas es mas aguda?", ["Sol", "Do"], "Sol"), explanation: "Cuanto mas a la derecha en el piano, mas aguda es la nota." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Ritmo y Compas",
      description: "Compases de 2, 3 y 4 tiempos, y las corcheas.",
      iconEmoji: "🥁",
      units: [
        {
          title: "Compases de 2 y 3 tiempos",
          description: "Marchas y valses.",
          lessons: [
            {
              title: "Vals de 3 tiempos",
              description: "El compas del vals.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "¿Cuantos tiempos tiene un compas de 3/4?", data: mcq("¿Cuantos tiempos tiene un compas de 3/4?", ["3", "4", "2"], "3"), explanation: "El 3/4 se usa en los valses." },
                { type: "RHYTHM_TAP", prompt: "Marca un compas de vals", data: rt(100, [1, 1, 1], "3/4"), explanation: "Negra, negra, negra: un-dos-tres, un-dos-tres." },
                { type: "KEYBOARD_PLAY", prompt: "Toca este acorde de vals", data: kp(["C4", "E4", "G4"], "treble", 100), explanation: "Do-Mi-Sol suenan bien juntos: es un acorde." },
              ],
            },
            {
              title: "Marcha de 2 tiempos",
              description: "El compas de las marchas.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "2/4 se usa mucho en...", data: mcq("2/4 se usa mucho en...", ["Marchas", "Valses", "Baladas lentas"], "Marchas"), explanation: "Su pulso firme de 2 tiempos encaja con el paso militar." },
                { type: "RHYTHM_TAP", prompt: "Marca un compas de 2/4", data: rt(110, [1, 1], "2/4"), explanation: "Un-dos, un-dos." },
                { type: "RHYTHM_TAP", prompt: "Repite el patron dos veces", data: rt(110, [1, 1, 1, 1], "2/4"), explanation: "Dos compases seguidos de 2/4." },
              ],
            },
          ],
        },
        {
          title: "Corcheas: notas rapidas",
          description: "Notas que van al doble de velocidad.",
          lessons: [
            {
              title: "Dos corcheas por tiempo",
              description: "La figura de las notas rapidas.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "Dos corcheas juntas duran lo mismo que...", data: mcq("Dos corcheas juntas duran lo mismo que...", ["Una negra", "Una blanca", "Una redonda"], "Una negra"), explanation: "Cada corchea vale medio tiempo; dos corcheas = 1 tiempo." },
                { type: "RHYTHM_TAP", prompt: "Marca este ritmo con corcheas", data: rt(90, [0.5, 0.5, 1, 1], "4/4"), explanation: "Corchea-corchea-negra-negra." },
              ],
            },
            {
              title: "Mezclando negras y corcheas",
              description: "Combina las dos velocidades.",
              exercises: [
                { type: "RHYTHM_TAP", prompt: "Marca este ritmo mixto", data: rt(90, [0.5, 0.5, 1, 0.5, 0.5, 1], "4/4"), explanation: "Practica alternar rapido y normal." },
                { type: "KEYBOARD_PLAY", prompt: "Toca esta melodia con ritmo de corcheas", data: kp(["C4", "D4", "E4", "D4", "C4"], "treble", 100), explanation: "¡Notas rapidas y una melodia sencilla!" },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Acordes y Armonia",
      description: "Tus primeros acordes: Do Mayor y Sol Mayor.",
      iconEmoji: "🎶",
      units: [
        {
          title: "Acordes mayores faciles",
          description: "Tres notas que suenan bien juntas.",
          lessons: [
            {
              title: "El acorde de Do Mayor",
              description: "Do - Mi - Sol.",
              exercises: [
                { type: "CHORD", prompt: "¿Que acorde es este?", data: ch("C4", ["C4", "E4", "G4"], "Do Mayor", ["Do Mayor", "Sol Mayor", "Fa Mayor"]), explanation: "Do-Mi-Sol forman el acorde de Do Mayor." },
                { type: "KEYBOARD_PLAY", prompt: "Toca las tres notas juntas: Do-Mi-Sol", data: kp(["C4", "E4", "G4"], "treble", 90), explanation: "Intenta tocarlas al mismo tiempo con 3 dedos." },
              ],
            },
            {
              title: "El acorde de Sol Mayor",
              description: "Sol - Si - Re.",
              exercises: [
                { type: "CHORD", prompt: "¿Que acorde es este?", data: ch("G4", ["G4", "B4", "D5"], "Sol Mayor", ["Do Mayor", "Sol Mayor", "Fa Mayor"]), explanation: "Sol-Si-Re forman el acorde de Sol Mayor." },
                { type: "KEYBOARD_PLAY", prompt: "Toca Sol-Si-Re juntos", data: kp(["G4", "B4", "D5"], "treble", 90), explanation: "El segundo acorde mas usado despues de Do Mayor." },
              ],
            },
          ],
        },
        {
          title: "Acompano una cancion",
          description: "Usa tus acordes para acompanar melodias.",
          lessons: [
            {
              title: "Do y Sol se turnan",
              description: "Cambiar entre dos acordes.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca Do Mayor y despues Sol Mayor", data: kp(["C4", "E4", "G4", "G4", "B4", "D5"], "treble", 90), explanation: "Alternar acordes es la base de acompanar canciones." },
                { type: "THEORY_MCQ", prompt: "Cuando cambiamos de acorde en una cancion, a eso lo llamamos...", data: mcq("Cuando cambiamos de acorde en una cancion, a eso lo llamamos...", ["Progresion de acordes", "Escala", "Silencio"], "Progresion de acordes"), explanation: "Una progresion es una secuencia de acordes." },
              ],
            },
            {
              title: "Mi acompanamiento de Estrellita",
              description: "Acordes para tu primera cancion.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca esta progresion: Do - Fa - Sol - Do", data: kp(["C4", "E4", "G4", "F4", "A4", "C5", "G4", "B4", "D5", "C4", "E4", "G4"], "treble", 80), explanation: "¡Ya puedes acompanar una cancion completa con acordes!" },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Mis Primeras Piezas",
      description: "Canciones populares para disfrutar tocando.",
      iconEmoji: "🎼",
      units: [
        {
          title: "Canciones populares",
          description: "Melodias que ya conoces.",
          lessons: [
            {
              title: "Cumpleanos feliz",
              description: "Una de las canciones mas famosas del mundo.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca el comienzo de Cumpleanos Feliz", data: kp(["C4", "C4", "D4", "C4", "F4", "E4"], "treble", 100), explanation: "Do Do Re Do Fa Mi." },
                { type: "STAFF_READING", prompt: "Lee y toca esta frase", data: sr("treble", ["C4", "C4", "D4", "C4", "F4", "E4"]), explanation: "La misma frase, ahora leyendola en el pentagrama." },
              ],
            },
            {
              title: "Los pollitos dicen",
              description: "Una cancion infantil clasica.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca esta melodia", data: kp(["E4", "D4", "C4", "D4", "E4", "E4", "E4"], "treble", 100), explanation: "Mi Re Do Re Mi Mi Mi." },
                { type: "RHYTHM_TAP", prompt: "Marca este ritmo", data: rt(100, [1, 1, 1, 1, 1, 1, 2]), explanation: "Seis negras y una blanca final." },
              ],
            },
          ],
        },
        {
          title: "Pequeno repertorio",
          description: "Tus primeras piezas con acordes.",
          lessons: [
            {
              title: "Vals sencillo",
              description: "Un pequeno vals con acordes.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca este pequeno vals con acordes", data: kp(["C4", "E4", "G4", "F4", "A4", "C5"], "treble", 90), explanation: "Do Mayor seguido de Fa Mayor." },
              ],
            },
            {
              title: "Mi propia cancion",
              description: "Crea tu primera melodia.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "¿Que necesitas para crear tu propia melodia?", data: mcq("¿Que necesitas para crear tu propia melodia?", ["Notas, ritmo y mucha imaginacion", "Solo un piano", "Nada, es imposible"], "Notas, ritmo y mucha imaginacion"), explanation: "¡Componer esta al alcance de cualquiera que se anime a intentarlo!" },
                { type: "KEYBOARD_PLAY", prompt: "Toca y despues inventa tu variacion de esta melodia", data: kp(["C4", "D4", "E4", "G4", "E4", "D4", "C4"], "treble", 90), explanation: "Prueba a cambiar el orden de las notas para crear algo tuyo." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Tecnica y Creatividad",
      description: "La escala completa y tus primeras improvisaciones.",
      iconEmoji: "🚀",
      units: [
        {
          title: "Escalas y dedos",
          description: "La escala de Do Mayor completa.",
          lessons: [
            {
              title: "La escala de Do Mayor completa",
              description: "Sube toda la escala.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca la escala completa de Do Mayor, subiendo", data: kp(["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"], "treble", 100), explanation: "¡Las 7 notas mas la octava!" },
                { type: "THEORY_MCQ", prompt: "¿Cuantas notas distintas tiene una escala mayor?", data: mcq("¿Cuantas notas distintas tiene una escala mayor?", ["7", "5", "8"], "7"), explanation: "La octava repite el nombre de la primera nota." },
              ],
            },
            {
              title: "Bajando la escala",
              description: "Ahora en sentido contrario.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca la escala de Do Mayor bajando", data: kp(["C5", "B4", "A4", "G4", "F4", "E4", "D4", "C4"], "treble", 100), explanation: "Practicar en ambas direcciones fortalece los dedos." },
              ],
            },
          ],
        },
        {
          title: "Improviso mi melodia",
          description: "Juega libremente con las notas que ya conoces.",
          lessons: [
            {
              title: "Jugando con las notas de Do Mayor",
              description: "Sin miedo a equivocarte.",
              exercises: [
                { type: "EAR_TRAINING", prompt: "Escucha... ¿cual es esta nota?", data: et("note", "Mi", ["Do", "Mi", "Sol"], ["E4"]), explanation: "Entrenar el oido te ayuda a improvisar mejor." },
                { type: "KEYBOARD_PLAY", prompt: "Toca esta melodia improvisada usando solo notas de Do Mayor", data: kp(["C4", "E4", "D4", "G4", "E4", "C4"], "treble", 90), explanation: "Todas las notas pertenecen a la escala de Do Mayor, ¡nunca suenan mal!" },
              ],
            },
            {
              title: "Tu concierto final",
              description: "Celebra todo lo aprendido en este nivel.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca esta pieza final combinando todo lo aprendido", data: kp(["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "G4", "E4", "C4"], "treble", 100), explanation: "¡Enhorabuena, has completado el camino de Fundamentos!" },
                { type: "THEORY_MCQ", prompt: "¡Felicidades! ¿Que acabas de aprender a tocar un poquito mejor?", data: mcq("¡Felicidades! ¿Que acabas de aprender a tocar un poquito mejor?", ["El piano", "La guitarra", "El violin"], "El piano"), explanation: "Sigue practicando en tus clases con Azucena para avanzar aun mas." },
              ],
            },
          ],
        },
      ],
    },
  ],
};
