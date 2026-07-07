import { TrackDef, nn, sr, rt, mcq, kp, ch } from "./defs";

export const adultsTrack: TrackDef = {
  code: "adults",
  name: "Piano para Adultos",
  description: "Un camino eficaz y sin prisas para adultos (18+), con teoria clara y repertorio real.",
  minAge: 18,
  maxAge: 99,
  order: 3,
  levels: [
    {
      title: "Fundamentos Eficaces",
      description: "Teoria esencial, independencia de manos y tu primera pieza clasica.",
      iconEmoji: "🎯",
      units: [
        {
          title: "Teoria esencial",
          description: "Claves, armadura y duracion de las figuras.",
          lessons: [
            {
              title: "El teclado y las claves de Sol y Fa",
              description: "El mapa completo del piano.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "¿Que clave se usa habitualmente para la mano izquierda?", data: mcq("¿Que clave se usa habitualmente para la mano izquierda?", ["Clave de Fa", "Clave de Sol", "Clave de Do"], "Clave de Fa"), explanation: "La clave de Fa cubre el registro grave del piano." },
                { type: "NOTE_NAME", prompt: "¿Que nota es esta en clave de Fa?", data: nn("bass", "G2", ["Sol", "Do", "Mi"], "Sol"), explanation: "Un Sol grave, tipico de la mano izquierda." },
                { type: "NOTE_NAME", prompt: "¿Que nota es esta en clave de Sol?", data: nn("treble", "C5", ["Do", "Re", "Mi"], "Do"), explanation: "El Do una octava por encima del Do central." },
              ],
            },
            {
              title: "Armadura de clave: Do Mayor y La menor",
              description: "Tonalidades relativas.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "Do Mayor y La menor comparten la misma armadura (sin sostenidos ni bemoles) porque son...", data: mcq("Do Mayor y La menor comparten la misma armadura (sin sostenidos ni bemoles) porque son...", ["Tonalidades relativas", "La misma escala", "No tienen relacion"], "Tonalidades relativas"), explanation: "Cada tonalidad mayor tiene una relativa menor que comparte armadura." },
                { type: "STAFF_READING", prompt: "Lee y toca la escala de Do Mayor", data: sr("treble", ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]), explanation: "La escala mas basica, sin alteraciones." },
              ],
            },
            {
              title: "Duracion de las figuras",
              description: "Redondas, blancas y negras.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "Una redonda dura...", data: mcq("Una redonda dura...", ["4 tiempos", "2 tiempos", "1 tiempo"], "4 tiempos"), explanation: "La redonda ocupa un compas entero de 4/4." },
                { type: "RHYTHM_TAP", prompt: "Marca una redonda completa", data: rt(72, [4], "4/4"), explanation: "Cuenta 4 tiempos mientras suena." },
                { type: "RHYTHM_TAP", prompt: "Marca blanca, negra, negra", data: rt(72, [2, 1, 1], "4/4"), explanation: "2 + 1 + 1 = 4 tiempos." },
              ],
            },
          ],
        },
        {
          title: "Ritmo e independencia de manos",
          description: "El reto central de aprender piano de adulto.",
          lessons: [
            {
              title: "Coordinacion basica",
              description: "Cada mano con su propio papel.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Mano derecha: acorde de Do Mayor", data: kp(["C4", "E4", "G4"], "treble", 80), explanation: "Practica el acorde solo con la mano derecha primero." },
                { type: "KEYBOARD_PLAY", prompt: "Mano izquierda: Do grave sostenido", data: kp(["C3"], "bass", 80), explanation: "Mantén la nota mientras cuentas 4 tiempos." },
              ],
            },
            {
              title: "Bajo Alberti simplificado",
              description: "Un patron de acompanamiento clasico.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca este patron de acompanamiento (bajo Alberti)", data: kp(["C3", "G3", "E3", "G3"], "bass", 90), explanation: "Muy usado en el periodo clasico (Mozart, Haydn)." },
                { type: "RHYTHM_TAP", prompt: "Marca 4 negras seguidas", data: rt(90, [1, 1, 1, 1]), explanation: "El bajo Alberti suele ir en negras constantes." },
              ],
            },
            {
              title: "Independencia real",
              description: "Combina ambas manos en movimiento.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Mano derecha: melodia ascendente", data: kp(["C4", "D4", "E4", "F4"], "treble", 85), explanation: "Una melodia sencilla en la mano derecha." },
                { type: "KEYBOARD_PLAY", prompt: "Mano izquierda: quintas en el bajo", data: kp(["C3", "G3"], "bass", 85), explanation: "Las quintas dan una base solida y estable." },
              ],
            },
          ],
        },
        {
          title: "Tu primera pieza clasica",
          description: "Repertorio real desde el primer nivel.",
          lessons: [
            {
              title: "Himno de la Alegria (fragmento)",
              description: "El tema de la Novena Sinfonia de Beethoven.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca el famoso tema de Beethoven (fragmento)", data: kp(["E4", "E4", "F4", "G4", "G4", "F4", "E4", "D4"], "treble", 90), explanation: "Uno de los temas mas reconocibles de la musica clasica." },
                { type: "STAFF_READING", prompt: "Lee y toca la segunda frase", data: sr("treble", ["C4", "C4", "D4", "E4", "E4", "D4", "C4", "B3"]), explanation: "La frase que responde a la primera." },
              ],
            },
            {
              title: "Minueto sencillo (estilo Bach)",
              description: "Un fragmento inspirado en el Minueto en Sol.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca este fragmento estilo Bach", data: kp(["D4", "G4", "A4", "B4", "G4"], "treble", 90), explanation: "El estilo barroco usa melodias claras y ornamentadas." },
                { type: "THEORY_MCQ", prompt: "Un minueto es una danza barroca en compas...", data: mcq("Un minueto es una danza barroca en compas...", ["3/4", "4/4", "2/4"], "3/4"), explanation: "El minueto es una danza elegante en compas ternario." },
              ],
            },
            {
              title: "Tu interpretacion completa",
              description: "Toca la pieza entera con confianza.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca el Himno de la Alegria completo (fragmento extendido)", data: kp(["E4", "E4", "F4", "G4", "G4", "F4", "E4", "D4", "C4", "C4", "D4", "E4", "D4", "D4"], "treble", 90), explanation: "¡Tu primera pieza clasica completa! Llevala a tu proxima clase presencial." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Armonia Funcional",
      description: "Triadas, inversiones y cadencias.",
      iconEmoji: "🎓",
      units: [
        {
          title: "Triadas e inversiones",
          description: "Mayor, menor, disminuido.",
          lessons: [
            {
              title: "Triadas mayores, menores, disminuidas",
              description: "Los tres colores basicos del acorde.",
              exercises: [
                { type: "CHORD", prompt: "¿Que acorde es este?", data: ch("C4", ["C4", "E4", "G4"], "Do Mayor", ["Do Mayor", "Do menor", "Do disminuido"]), explanation: "Tercera mayor + quinta justa." },
                { type: "CHORD", prompt: "¿Que acorde es este?", data: ch("C4", ["C4", "D#4", "G4"], "Do menor", ["Do Mayor", "Do menor", "Do disminuido"]), explanation: "Tercera menor + quinta justa." },
                { type: "CHORD", prompt: "¿Que acorde es este?", data: ch("B3", ["B3", "D4", "F4"], "Si disminuido", ["Si Mayor", "Si menor", "Si disminuido"]), explanation: "Tercera menor + quinta disminuida: sonido tenso." },
              ],
            },
            {
              title: "Inversiones de la triada",
              description: "Cambiar la nota mas grave del acorde.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "En la primera inversion de un acorde, la nota mas grave es...", data: mcq("En la primera inversion de un acorde, la nota mas grave es...", ["La tercera", "La fundamental", "La quinta"], "La tercera"), explanation: "En estado fundamental la nota mas grave es la fundamental; en primera inversion, la tercera." },
                { type: "KEYBOARD_PLAY", prompt: "Toca Do Mayor en primera inversion (Mi-Sol-Do)", data: kp(["E4", "G4", "C5"], "treble", 90), explanation: "Las inversiones facilitan enlazar acordes con movimiento suave." },
              ],
            },
          ],
        },
        {
          title: "Cadencias I-IV-V-I",
          description: "Como 'terminan' las frases musicales.",
          lessons: [
            {
              title: "La cadencia perfecta",
              description: "V - I, la resolucion mas fuerte.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "La cadencia V-I se llama...", data: mcq("La cadencia V-I se llama...", ["Cadencia perfecta o autentica", "Cadencia plagal", "Cadencia rota"], "Cadencia perfecta o autentica"), explanation: "Es la resolucion armonica mas conclusiva." },
                { type: "KEYBOARD_PLAY", prompt: "Toca Sol Mayor (V) resolviendo a Do Mayor (I)", data: kp(["G4", "B4", "D5", "C4", "E4", "G4"], "treble", 85), explanation: "El movimiento V-I suena como un punto final." },
              ],
            },
            {
              title: "Cadencia plagal (el 'Amen')",
              description: "IV - I, el final religioso.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca Fa Mayor (IV) resolviendo a Do Mayor (I)", data: kp(["F4", "A4", "C5", "C4", "E4", "G4"], "treble", 85), explanation: "Se escucha tipicamente al final de los himnos ('Amen')." },
                { type: "THEORY_MCQ", prompt: "La cadencia IV-I se conoce popularmente como cadencia...", data: mcq("La cadencia IV-I se conoce popularmente como cadencia...", ["Plagal ('Amen')", "Rota", "Autentica"], "Plagal ('Amen')"), explanation: "Por su uso tradicional en musica religiosa." },
              ],
            },
            {
              title: "Progresion I-IV-V-I completa",
              description: "La base de la armonia tonal.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca la progresion completa I-IV-V-I en Do Mayor", data: kp(["C4", "E4", "G4", "F4", "A4", "C5", "G4", "B4", "D5", "C4", "E4", "G4"], "treble", 85), explanation: "Esta progresion es la columna vertebral de siglos de musica occidental." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Repertorio Clasico I",
      description: "Fur Elise y un vals en Do Mayor.",
      iconEmoji: "🎻",
      units: [
        {
          title: "Fur Elise (fragmento)",
          description: "La pieza mas famosa de Beethoven para piano.",
          lessons: [
            {
              title: "El motivo principal",
              description: "Las primeras notas, reconocibles al instante.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca el famoso motivo inicial de Fur Elise", data: kp(["E5", "D#5", "E5", "D#5", "E5", "B4", "D5", "C5"], "treble", 100), explanation: "Uno de los motivos mas reconocibles de toda la musica clasica." },
              ],
            },
            {
              title: "Acompanamiento de mano izquierda",
              description: "El arpegio que sostiene la melodia.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca el acompanamiento arpegiado de la mano izquierda", data: kp(["A3", "E4", "A4"], "bass", 100), explanation: "Un arpegio simple que da estabilidad armonica." },
              ],
            },
          ],
        },
        {
          title: "Vals en Do Mayor",
          description: "Un vals clasico con acompanamiento.",
          lessons: [
            {
              title: "Melodia del vals",
              description: "La linea principal.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca esta melodia de vals", data: kp(["C5", "E5", "G5", "E5", "C5"], "treble", 100), explanation: "Un arpegio elegante tipico de los valses." },
              ],
            },
            {
              title: "Vals completo con acompanamiento",
              description: "Ambas manos juntas.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca el acompanamiento del vals (bajo-acorde-acorde)", data: kp(["C4", "G4", "E4", "G4"], "bass", 100), explanation: "El clasico patron 'oom-pah-pah' del vals." },
                { type: "THEORY_MCQ", prompt: "¿Que compas es caracteristico del vals?", data: mcq("¿Que compas es caracteristico del vals?", ["3/4", "4/4", "6/8"], "3/4"), explanation: "El vals se baila y se escribe siempre en 3/4." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Acompanamiento y Estilo Moderno",
      description: "Cifrado americano, comping y arreglos propios.",
      iconEmoji: "🎹",
      units: [
        {
          title: "Cifrado americano (lead sheets)",
          description: "Leer acordes como un musico profesional.",
          lessons: [
            {
              title: "Leer cifrados de acordes",
              description: "Simbolos como Am7, Cmaj7, G7.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "En un cifrado, 'Am7' significa...", data: mcq("En un cifrado, 'Am7' significa...", ["Acorde de La menor con septima", "Acorde de La Mayor", "La nota La"], "Acorde de La menor con septima"), explanation: "La letra indica la fundamental, 'm' menor y el numero la septima anadida." },
                { type: "KEYBOARD_PLAY", prompt: "Toca el acorde Am7 (La-Do-Mi-Sol)", data: kp(["A4", "C5", "E5", "G5"], "treble", 90), explanation: "Un acorde de cuatro notas muy usado en jazz y pop." },
              ],
            },
            {
              title: "Comping: acompanar con ritmo",
              description: "Tocar acordes con groove, no solo sostenidos.",
              exercises: [
                { type: "RHYTHM_TAP", prompt: "Marca este patron de comping", data: rt(100, [1, 0.5, 0.5, 1, 1]), explanation: "El comping anade variedad ritmica a los acordes." },
                { type: "KEYBOARD_PLAY", prompt: "Toca este patron de comping sobre Do Mayor 7", data: kp(["C4", "E4", "G4", "C5"], "treble", 100), explanation: "Cmaj7 con la septima mayor anadida." },
              ],
            },
          ],
        },
        {
          title: "Balada moderna",
          description: "Arreglos con caracter propio.",
          lessons: [
            {
              title: "Arpegios fluidos",
              description: "Un acompanamiento suave y continuo.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca este arpegio fluido", data: kp(["C4", "G4", "E5", "G4"], "treble", 80), explanation: "Un patron de arpegio amplio, tipico de baladas modernas." },
              ],
            },
            {
              title: "Tu propio arreglo",
              description: "Combina acordes y melodia con tu estilo.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca este arreglo combinando acordes y melodia", data: kp(["C4", "E4", "G4", "A4", "F4", "C5", "G4", "B4"], "treble", 85), explanation: "El objetivo es que empieces a sonar con tu propio caracter." },
              ],
            },
          ],
        },
      ],
    },
    {
      title: "Tecnica Avanzada",
      description: "Escalas, pedal y dinamica.",
      iconEmoji: "🏆",
      units: [
        {
          title: "Escalas en varias tonalidades",
          description: "Mas alla de Do Mayor.",
          lessons: [
            {
              title: "Escala de Sol Mayor",
              description: "Con un sostenido en la armadura.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca la escala de Sol Mayor", data: kp(["G4", "A4", "B4", "C5", "D5", "E5", "F#5", "G5"], "treble", 110), explanation: "Sol Mayor tiene un sostenido: Fa#." },
              ],
            },
            {
              title: "Escala de Fa Mayor",
              description: "Con un bemol en la armadura.",
              exercises: [
                { type: "KEYBOARD_PLAY", prompt: "Toca la escala de Fa Mayor", data: kp(["F4", "G4", "A4", "Bb4", "C5", "D5", "E5", "F5"], "treble", 110), explanation: "Fa Mayor tiene un bemol: Sib." },
              ],
            },
          ],
        },
        {
          title: "Pedal, dinamica y expresion",
          description: "Lo que distingue a un pianista expresivo.",
          lessons: [
            {
              title: "El pedal de resonancia",
              description: "El pedal derecho.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "El pedal derecho (de resonancia) sirve para...", data: mcq("El pedal derecho (de resonancia) sirve para...", ["Prolongar y ligar el sonido de las notas", "Silenciar el piano", "Cambiar el tono"], "Prolongar y ligar el sonido de las notas"), explanation: "Levanta los apagadores y deja vibrar las cuerdas libremente." },
              ],
            },
            {
              title: "Dinamica: piano y forte",
              description: "Tocar suave y fuerte con intencion.",
              exercises: [
                { type: "THEORY_MCQ", prompt: "'Piano' (p) en la partitura indica que hay que tocar...", data: mcq("'Piano' (p) en la partitura indica que hay que tocar...", ["Suave", "Fuerte", "Rapido"], "Suave"), explanation: "'Piano' significa suave, de ahi el nombre del instrumento (pianoforte)." },
                { type: "THEORY_MCQ", prompt: "'Forte' (f) en la partitura indica que hay que tocar...", data: mcq("'Forte' (f) en la partitura indica que hay que tocar...", ["Fuerte", "Suave", "Lento"], "Fuerte"), explanation: "El contraste piano-forte es clave para la expresividad." },
                { type: "KEYBOARD_PLAY", prompt: "Toca esta pieza final aplicando dinamica: empieza piano y termina forte", data: kp(["C4", "E4", "G4", "C5", "G4", "E4", "C4"], "treble", 100), explanation: "¡Enhorabuena! Has completado el camino de Piano para Adultos hasta aqui. Sigue construyendo repertorio con Azucena." },
              ],
            },
          ],
        },
      ],
    },
  ],
};
