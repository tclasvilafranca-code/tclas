export type TheoryIconKey =
  | "BookOpen"
  | "Target"
  | "Sign"
  | "Bolt"
  | "Overtake"
  | "Parking"
  | "Lightbulb"
  | "Drop"
  | "Medal"
  | "Wrench"
  | "Radar"
  | "Child"
  | "Users"
  | "Leaf"
  | "Road"
  | "Scooter"
  | "ShieldCheck";

export interface TheoryCard {
  title: string;
  body: string;
}

export interface TheoryCheck {
  question: string;
  options: string[];
  correctIndex: number;
}

export interface TheoryChapter {
  id: string;
  title: string;
  icon: TheoryIconKey;
  cards: TheoryCard[];
  check: TheoryCheck;
}

export interface TheorySession {
  id: string;
  title: string;
  subtitle: string;
  estimatedMinutes: number;
  chapters: TheoryChapter[];
}

export const THEORY_EXPRESS: TheorySession[] = [
  {
    id: "s1",
    title: "Sesión 1",
    subtitle: "Quién pasa primero, lee la vía y cuánta caña",
    estimatedMinutes: 40,
    chapters: [
      {
        id: "basico",
        title: "Lo básico",
        icon: "BookOpen",
        cards: [
          {
            title: "La vía es de todos",
            body: "La calzada es para los vehículos, la acera para los peatones. El arcén es la franja lateral para emergencias, no para circular ni para parar.",
          },
          {
            title: "Usuario de la vía",
            body: "Cualquiera que use la carretera: conductores, peatones, ciclistas, patinetes. Todos tienen obligaciones, no solo el que va en coche.",
          },
          {
            title: "Vía interurbana vs. urbana",
            body: "Interurbana: fuera de población (carretera). Urbana: dentro de una población. Las normas de velocidad y parada cambian según cuál sea.",
          },
        ],
        check: {
          question: "¿Para qué es el arcén?",
          options: ["Para parar un momento si hace falta", "Solo para emergencias y vehículos autorizados", "Para adelantar cuando hay atasco"],
          correctIndex: 1,
        },
      },
      {
        id: "prioridad",
        title: "Quién pasa primero",
        icon: "Target",
        cards: [
          {
            title: "La jerarquía que lo resuelve casi todo",
            body: "Agente > semáforo > señal vertical > marca en el suelo > norma general. Si hay contradicción, siempre gana el de más arriba en esta lista.",
          },
          {
            title: "Cruce sin ninguna señal",
            body: "Prioridad para el que viene por tu derecha.",
          },
          {
            title: "En una rotonda",
            body: "Prioridad para el que ya está circulando dentro del anillo.",
          },
          {
            title: "Si giras, cedes tú",
            body: "Un vehículo que gira siempre cede el paso al que sigue recto, aunque venga por tu derecha.",
          },
          {
            title: "STOP vs. Ceda el paso",
            body: "El STOP obliga a una parada total siempre, haya o no tráfico. El Ceda el Paso solo obliga a detenerte si hace falta para dejar pasar.",
          },
          {
            title: "Cuestas estrechas",
            body: "Si no caben dos vehículos a la vez, quien sube tiene prioridad sobre quien baja.",
          },
          {
            title: "Vehículos de emergencia",
            body: "Ambulancia, policía o bomberos con luces y sirena puestas tienen prioridad absoluta. Hay que facilitarles el paso.",
          },
          {
            title: "Al incorporarte a una vía",
            body: "En un carril de aceleración, cedes tú el paso a quien ya circula por esa vía, no al revés.",
          },
          {
            title: "Los tranvías",
            body: "Tienen prioridad sobre el resto de vehículos, salvo que una señalización indique lo contrario.",
          },
          {
            title: "Un caso que sorprende",
            body: "Si dos vehículos llegan a la vez a un cruce sin señales y ninguno viene por la derecha del otro (por ejemplo, de frente), pasa primero quien vaya a seguir recto, no quien gire.",
          },
        ],
        check: {
          question: "En un cruce sin ninguna señal, ¿quién tiene prioridad?",
          options: ["El que llega primero", "El que viene por tu derecha", "El vehículo más grande"],
          correctIndex: 1,
        },
      },
      {
        id: "senales",
        title: "Lee la vía",
        icon: "Sign",
        cards: [
          {
            title: "Mismo orden de mando",
            body: "Un agente de tráfico anula cualquier señal fija o semáforo. Después manda el semáforo, luego la señal vertical, luego la marca en el suelo.",
          },
          {
            title: "Formas con significado fijo",
            body: "Triángulo = peligro. Círculo con borde rojo = prohibición. Círculo azul = obligación. Cuadrado o rectángulo azul = información.",
          },
          {
            title: "Los colores no son decorativos",
            body: "Rojo = prohibición o parada. Azul = obligación o información. Amarillo = advertencia temporal, casi siempre obras.",
          },
          {
            title: "Doble línea continua",
            body: "Prohibido cruzarla o adelantar, en ambos sentidos.",
          },
          {
            title: "Línea discontinua",
            body: "Se puede cruzar o adelantar si hay visibilidad suficiente.",
          },
          {
            title: "Una continua y otra discontinua",
            body: "Manda siempre la línea de tu propio carril, no la del contrario.",
          },
          {
            title: "STOP y Ceda el Paso con semáforo",
            body: "Si hay un semáforo en funcionamiento, manda el semáforo — esas señales quedan en segundo plano.",
          },
          {
            title: "Flechas pintadas en el carril",
            body: "Son obligatorias, no orientativas: si el carril tiene una flecha de giro, tienes que girar.",
          },
          {
            title: "Marcas amarillas en el bordillo",
            body: "Indican prohibido parar y/o estacionar, según el tipo de línea.",
          },
          {
            title: "Paneles complementarios",
            body: "El cartel pequeño debajo de una señal matiza su alcance: distancia, excepciones, horario. No es decorativo, cambia la norma.",
          },
          {
            title: "Las señales de obra mandan",
            body: "Mientras dure la obra, la señalización temporal (amarilla) prevalece siempre sobre la señal fija de siempre.",
          },
          {
            title: "Fin de una prohibición",
            body: "Se indica con un panel rectangular gris con una franja diagonal — así se sabe dónde termina la restricción.",
          },
        ],
        check: {
          question: "Si un agente de tráfico da una indicación distinta a la de un semáforo, ¿quién manda?",
          options: ["El semáforo, siempre", "El agente, siempre", "Depende de la hora"],
          correctIndex: 1,
        },
      },
      {
        id: "velocidad",
        title: "Cuánta caña",
        icon: "Bolt",
        cards: [
          {
            title: "Fuera de ciudad",
            body: "Autovía y autopista: 120 km/h. Convencional con arcén: 100. Convencional sin arcén: 90.",
          },
          {
            title: "Dentro de ciudad: tres velocidades, no una",
            body: "20 km/h en calles de plataforma única (sin acera diferenciada). 30 km/h en calles de un solo carril por sentido. 50 km/h en vías de dos o más carriles por sentido.",
          },
          {
            title: "El error más común",
            body: "Pensar que toda calle de ciudad va a 50. Hoy la mayoría de calles de un solo carril por sentido — la mayoría de cualquier barrio — van a 30.",
          },
          {
            title: "Con remolque o furgón grande",
            body: "Resta unos 10-20 km/h a esos límites generales.",
          },
          {
            title: "El límite es el máximo, no el objetivo",
            body: "Lluvia, niebla o una curva cerrada obligan a ir más lento aunque el límite permita más.",
          },
          {
            title: "Conductor novel, ¿velocidad más baja?",
            body: "No. Esa reducción se eliminó en 2011: circulas al mismo límite que cualquiera. Lo que sí es obligatorio el primer año es llevar la 'L' (blanca sobre verde) en la parte trasera del coche.",
          },
        ],
        check: {
          question: "Una calle de un solo carril por sentido, sin nada más indicado, ¿a qué velocidad máxima se circula?",
          options: ["50 km/h", "30 km/h", "20 km/h"],
          correctIndex: 1,
        },
      },
    ],
  },
  {
    id: "s2",
    title: "Sesión 2",
    subtitle: "Adelantar bien, parar sin líos, luces, alcohol y puntos",
    estimatedMinutes: 55,
    chapters: [
      {
        id: "adelantar",
        title: "Adelantar bien",
        icon: "Overtake",
        cards: [
          {
            title: "Nunca en...",
            body: "Curva sin visibilidad, cambio de rasante, cruce, paso de peatones o carril reservado.",
          },
          {
            title: "Nunca en cadena",
            body: "Si el coche de delante ya está adelantando a otro, tú no le adelantas a él a la vez.",
          },
          {
            title: "Siempre por la izquierda",
            body: "Salvo casos concretos: un ciclista, o alguien que va a girar a la izquierda con el intermitente puesto.",
          },
          {
            title: "Antes de adelantar",
            body: "Retrovisor, punto ciego, e intermitente puesto con antelación — en ese orden.",
          },
          {
            title: "A un ciclista, más espacio del que crees",
            body: "Mínimo 1,5 metros de separación lateral al pasarlo.",
          },
        ],
        check: {
          question: "¿Se puede adelantar si el coche de delante ya está adelantando a otro?",
          options: ["Sí, si hay espacio de sobra", "No, nunca", "Solo de noche"],
          correctIndex: 1,
        },
      },
      {
        id: "parar",
        title: "Parar sin líos",
        icon: "Parking",
        cards: [
          {
            title: "Parada vs. estacionamiento",
            body: "Parada: hasta 2 minutos, sin alejarte del vehículo. Estacionamiento: más de 2 minutos, o te alejas de él.",
          },
          {
            title: "Prohibido siempre",
            body: "Pasos de peatones, carril bus, curvas, cambios de rasante, dobles filas y vados.",
          },
          {
            title: "En cuesta",
            body: "Ruedas giradas hacia el bordillo cuesta abajo; en sentido contrario al bordillo cuesta arriba.",
          },
        ],
        check: {
          question: "¿Cuál es la diferencia entre parada y estacionamiento?",
          options: ["Ninguna, es lo mismo", "La parada es de hasta 2 min sin alejarte; el estacionamiento es más tiempo o te alejas", "El estacionamiento es solo de noche"],
          correctIndex: 1,
        },
      },
      {
        id: "luces",
        title: "Luces",
        icon: "Lightbulb",
        cards: [
          {
            title: "Cruce obligatorio",
            body: "De noche, en túnel, con lluvia fuerte o poca visibilidad.",
          },
          {
            title: "Antiniebla trasera",
            body: "Solo con muy poca visibilidad real — usarla de más deslumbra al de atrás.",
          },
          {
            title: "Intermitente",
            body: "Obligatorio en cualquier maniobra: girar, cambiar de carril, incorporarte.",
          },
          {
            title: "Luces de emergencia (warning)",
            body: "Solo si eres un peligro u obstáculo real para los demás, nunca como gesto de 'gracias'.",
          },
        ],
        check: {
          question: "¿Cuándo se pueden usar las luces antiniebla traseras?",
          options: ["Siempre que llueva un poco", "Solo con muy poca visibilidad real", "Nunca, están prohibidas"],
          correctIndex: 1,
        },
      },
      {
        id: "alcohol",
        title: "Alcohol y drogas",
        icon: "Drop",
        cards: [
          {
            title: "Límite general",
            body: "0,5 g/l en sangre, o 0,25 mg/l en aire espirado.",
          },
          {
            title: "Novel o profesional",
            body: "0,3 g/l en sangre, o 0,15 mg/l en aire espirado — durante los 2 primeros años de carnet, o siempre si es tu profesión.",
          },
          {
            title: "Drogas: tolerancia cero",
            body: "Cualquier rastro detectado es infracción, no hay un límite tolerado como con el alcohol.",
          },
          {
            title: "Negarte a soplar",
            body: "Es peor que dar positivo — es un delito en sí mismo.",
          },
        ],
        check: {
          question: "¿Cuál es el límite de alcohol para un conductor novel o profesional?",
          options: ["0,5 g/l en sangre", "0,3 g/l en sangre", "1 g/l en sangre"],
          correctIndex: 1,
        },
      },
      {
        id: "puntos",
        title: "Puntos y sanciones",
        icon: "Medal",
        cards: [
          {
            title: "Empiezas con 12 (u 8 si eres novel)",
            body: "Carnet normal: 12 puntos. Si acabas de sacarte el carnet, o recuperas uno que te habían retirado: 8.",
          },
          {
            title: "También puedes subir de 12",
            body: "Con 12 iniciales: 3 años sin infracciones te suben a 14; otros 3 años limpios, a 15 — el máximo posible.",
          },
          {
            title: "El novel también puede llegar a 15",
            body: "Con 8 iniciales: 2 años sin infracciones te suben a 12, y desde ahí sigues la misma escalera hasta 15.",
          },
          {
            title: "Lo que más puntos quita",
            body: "Alcohol o drogas, exceso de velocidad grave, usar el móvil en la mano, no llevar cinturón: entre 2 y 6 puntos según la gravedad.",
          },
          {
            title: "Si te quedas a 0",
            body: "Recuperas el carnet con un curso y un examen — no se recupera solo.",
          },
        ],
        check: {
          question: "¿Cuál es el máximo de puntos que se pueden llegar a tener con buen historial?",
          options: ["12", "15", "20"],
          correctIndex: 1,
        },
      },
    ],
  },
  {
    id: "s3",
    title: "Sesión 3",
    subtitle: "Papeles, otros usuarios, vías rápidas y seguridad",
    estimatedMinutes: 50,
    chapters: [
      {
        id: "papeles",
        title: "Papeles y mecánica",
        icon: "Wrench",
        cards: [
          {
            title: "Documentación obligatoria",
            body: "Permiso de conducir, permiso de circulación del vehículo y seguro en vigor.",
          },
          {
            title: "ITV",
            body: "Obligatoria y periódica según la antigüedad del vehículo. Circular con ella caducada es infracción.",
          },
          {
            title: "Neumáticos",
            body: "Profundidad mínima legal de dibujo: 1,6 mm. Por debajo, frenas mucho peor de lo que crees.",
          },
          {
            title: "Equipo obligatorio",
            body: "Triángulos de emergencia y chaleco reflectante — sí son obligatorios.",
          },
        ],
        check: {
          question: "¿Qué documentación es obligatoria llevar?",
          options: ["Solo el DNI", "Permiso de conducir, permiso de circulación y seguro en vigor", "Solo el seguro"],
          correctIndex: 1,
        },
      },
      {
        id: "adas",
        title: "Asistentes de conducción",
        icon: "Radar",
        cards: [
          {
            title: "ABS",
            body: "Evita que las ruedas se bloqueen al frenar fuerte, para que puedas seguir dirigiendo el coche mientras frenas.",
          },
          {
            title: "ESP (control de estabilidad)",
            body: "Corrige derrapes automáticamente frenando ruedas concretas si el coche empieza a perder el control.",
          },
          {
            title: "Aviso de cambio de carril",
            body: "Te avisa si te sales del carril sin haber puesto el intermitente.",
          },
          {
            title: "Frenada de emergencia autónoma",
            body: "Frena sola si detecta que vas a chocar y no reaccionas a tiempo.",
          },
          {
            title: "Ayudan, no conducen por ti",
            body: "Todos estos sistemas asisten, pero la responsabilidad y la atención siguen siendo tuyas.",
          },
        ],
        check: {
          question: "¿Qué hace el ABS?",
          options: ["Frena más fuerte que tú", "Evita que las ruedas se bloqueen al frenar", "Aparca el coche solo"],
          correctIndex: 1,
        },
      },
      {
        id: "menores",
        title: "Menores en el coche",
        icon: "Child",
        cards: [
          {
            title: "Sistema de retención infantil",
            body: "Obligatorio para menores de 135 cm de altura, homologado según su peso y talla.",
          },
          {
            title: "Nunca a contramarcha con airbag activo",
            body: "Un sistema orientado hacia atrás nunca va en el asiento delantero si el airbag frontal está activo.",
          },
          {
            title: "Nunca solos",
            body: "Dejar a un menor solo dentro del vehículo estacionado es una infracción grave.",
          },
        ],
        check: {
          question: "¿Hasta qué altura es obligatorio el sistema de retención infantil?",
          options: ["120 cm", "135 cm", "150 cm"],
          correctIndex: 1,
        },
      },
      {
        id: "otros-usuarios",
        title: "Los demás usuarios de la vía",
        icon: "Users",
        cards: [
          {
            title: "El peatón manda en el paso de cebra",
            body: "Si un peatón ya ha pisado el paso, tiene prioridad aunque el semáforo esté a punto de cambiar.",
          },
          {
            title: "El ángulo muerto existe para todos",
            body: "Antes de girar o cambiar de carril, gira la cabeza — una moto o bici puede estar justo donde no llega el retrovisor.",
          },
          {
            title: "Personas con movilidad reducida",
            body: "Se les da siempre prioridad y más tiempo, tanto en pasos de peatones como al subir o bajar de un vehículo.",
          },
          {
            title: "A un ciclista, respeto y espacio",
            body: "Mínimo 1,5 m de separación lateral al pasarlo, más aún si hay más de un carril disponible.",
          },
        ],
        check: {
          question: "¿A qué distancia mínima hay que pasar a un ciclista?",
          options: ["0,5 m", "1,5 m", "3 m"],
          correctIndex: 1,
        },
      },
      {
        id: "medio-ambiente",
        title: "Medio ambiente",
        icon: "Leaf",
        cards: [
          {
            title: "Zonas de Bajas Emisiones (ZBE)",
            body: "Restringen el acceso según la etiqueta ambiental del vehículo (0, ECO, C, B o sin etiqueta).",
          },
          {
            title: "Conducción eficiente",
            body: "Revoluciones bajas y frenadas anticipadas ahorran combustible y reducen emisiones.",
          },
        ],
        check: {
          question: "¿Qué son las Zonas de Bajas Emisiones (ZBE)?",
          options: ["Zonas donde solo puede entrar quien tenga la etiqueta ambiental adecuada", "Zonas sin ningún tipo de restricción", "Zonas solo para bicicletas"],
          correctIndex: 0,
        },
      },
      {
        id: "vias-rapidas",
        title: "Vías rápidas",
        icon: "Road",
        cards: [
          {
            title: "Prohibido siempre",
            body: "Marcha atrás, giro en U o parar en el carril, salvo emergencia real.",
          },
          {
            title: "El arcén no es para parar 'un momento'",
            body: "Es solo para emergencias reales o vehículos de asistencia.",
          },
          {
            title: "Si te averías",
            body: "Sal del vehículo por el lado contrario al tráfico y aléjate tras el guardarraíl si puedes.",
          },
        ],
        check: {
          question: "Si te averías en autopista, ¿qué debes hacer?",
          options: ["Quedarte dentro del coche con las luces puestas", "Salir por el lado contrario al tráfico y alejarte tras el guardarraíl si puedes", "Esperar en el arcén sin más"],
          correctIndex: 1,
        },
      },
      {
        id: "vmp",
        title: "Patinetes eléctricos (VMP)",
        icon: "Scooter",
        cards: [
          {
            title: "25 km/h máximo",
            body: "Es la velocidad máxima permitida para un VMP.",
          },
          {
            title: "Nunca por...",
            body: "Aceras, zonas peatonales, autopistas, autovías, vías interurbanas ni túneles urbanos.",
          },
          {
            title: "Carril bici si existe",
            body: "Si hay carril bici, es obligatorio usarlo; si no, se circula por la calzada.",
          },
          {
            title: "Casco obligatorio",
            body: "En cualquier vía urbana, para cualquier conductor de VMP.",
          },
          {
            title: "Edad mínima y seguro",
            body: "15 años como mínimo, seguro obligatorio, y de noche luces encendidas más chaleco reflectante.",
          },
        ],
        check: {
          question: "¿Puede un patinete eléctrico circular por la acera?",
          options: ["Sí, siempre que vaya despacio", "No, nunca", "Solo si no hay peatones"],
          correctIndex: 1,
        },
      },
      {
        id: "seguridad-vial",
        title: "Seguridad vial",
        icon: "ShieldCheck",
        cards: [
          {
            title: "La distancia de seguridad no es un número fijo",
            body: "Depende de la velocidad, el estado de la vía y el estado del vehículo.",
          },
          {
            title: "El móvil, ni en un soporte",
            body: "Prohibido manipularlo conduciendo, incluso montado en un soporte. Solo vale manos libres homologado sin tocarlo.",
          },
          {
            title: "Ante un accidente: P-A-S",
            body: "Proteger, Avisar, Socorrer — en ese orden, siempre.",
          },
          {
            title: "Triángulo y chaleco: sí. Botiquín: no.",
            body: "El triángulo de emergencia y el chaleco reflectante son obligatorios. El botiquín es recomendable, pero no obligatorio — un clásico truco de examen.",
          },
          {
            title: "Fatiga y medicación",
            body: "Conducir cansado, o bajo medicación con efectos narcóticos declarados, es tan peligroso como el alcohol.",
          },
        ],
        check: {
          question: "¿Es obligatorio llevar un botiquín en el coche?",
          options: ["Sí, siempre", "No, es solo recomendable", "Solo en autopista"],
          correctIndex: 1,
        },
      },
    ],
  },
];

export function totalCardCount(session: TheorySession): number {
  return session.chapters.reduce((sum, c) => sum + c.cards.length + 1, 0);
}
