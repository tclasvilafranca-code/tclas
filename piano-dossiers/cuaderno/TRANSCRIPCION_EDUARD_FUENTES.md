# Eduard · las veinte partituras, medidas

**Rehecho entero el 26 de agosto de 2026.** Hasta ese día el cuaderno de Eduard
era una copia del de José María: mismo repertorio, mismas diecinueve piezas,
mismo orden. El cliente lo paró en seco —*"el álbum de Eduard no era real a su
nivel"*— y pasó su carpeta de Drive, con una indicación que lo decide todo:

> *"es un señor de unos 65 años con un nivel bajo y que necesita aprender con
> buena teoría y explicaciones"*

Y dos más, contestadas después: **la misma estructura que los demás alumnos,
solo adaptada a su nivel** (no un formato nuevo), y **si alguna partitura del
dosier antiguo cuadra con el nivel, se aprovecha**.

De ahí salen las veinte piezas: **dieciséis de su carpeta** y **cuatro
rescatadas** del dosier viejo.

---

## Lo que se midió, y con qué

Todo sobre el PDF de su carpeta, rasterizado a 300 ppp:

| dato | herramienta | testigo |
|---|---|---|
| compás | recorte ampliado del arranque | `auditar_compas.LEIDO` |
| armadura | el mismo recorte | `auditar_tonalidad.LEIDO` |
| figura más corta | `medir_figuras` | `auditar_figuras` |
| tempo impreso | `pdftotext` | `auditar_tempo.MIRADAS` |
| alturas del arranque | `medir_arranque` + recorte | `auditar_alturas.MIRADAS` |

**La trampa del nombre del fichero**, otra vez. En su carpeta hay un PDF
llamado *"Escalas y Arpegios Facil progresando.pdf"* y **no es un cuaderno de
escalas**: dentro pone *Los aristogatos*, de los hermanos Sherman, arreglo de
A. C. Escobés. Creerse el nombre habría puesto una hoja de técnica donde hay
una canción. Se comprueba siempre con `pdftotext -f 1 -l 1`.

**Y la de la resolución.** Tres de las suyas llevan dentro una foto de 72–76 ppi
(Clementine, el Grandfather's Clock y el Toreador). A esa resolución el agujero
de una blanca desaparece y una cabeza hueca parece rellena. Lo que se hizo:
sumar. En Clementine, la anacrusa vale un tiempo, el compás es de tres y detrás
de la nota dudosa solo hay dos corcheas — negra + corchea + corchea son dos
tiempos y blanca + corchea + corchea son tres. Es una blanca. *Cuando una figura
no cuadre a la vista, súmala.*

---

## Las veinte piezas, en orden de cuaderno

| # | pieza | compás | armadura | manos | lo nuevo |
|---|---|---|---|---|---|
| 1 | Clementine | 3/4 | — | una | anacrusa |
| 2 | Los Aristogatos | 4/4 | — | una | silencio de blanca de entrada |
| 3 | Eso que tú me das | 4/4 | — | una | cifrado y letra |
| 4 | Romance · Diabelli | ¢ | — | dos, al unísono | posición fija, cuatro manos |
| 5 | America | 3/4 | — | dos | negra con puntillo |
| 6 | Star-Spangled Banner | 3/4 | — | dos | entrar tras un silencio |
| 7 | La Pantera Rosa | 4/4 | — | dos, distintas | la izquierda empieza sola |
| 8 | Nocturno op. 9 nº 2 | 3/4 | — | dos, por turnos | notas de tres tiempos |
| 9 | The Beginner · Gurlitt | 3/4 | — | dos, al unísono | 8va y reguladores |
| 10 | Heart and Soul | 4/4 | — | dos, distintas | los cuatro acordes |
| 11 | I Have a Dream | 4/4 | — | dos, distintas | tempo impreso (120) |
| 12 | Deck the Halls | 4/4 | 1 ♭ | dos | el primer bemol |
| 13 | Villancicos a cuatro manos | 4/4 | — | dos, las dos en sol | dos claves de sol |
| 14 | Greensleeves | 3/4 | — | dos, distintas | La menor y el acorde roto |
| 15 | Honor Him · Gladiator | 3/4 | 3 ♯ | dos, por turnos | la armadura grande |
| 16 | Rasputin | 4/4 | 2 ♯ | dos | compases callados |
| 17 | Jingle Bell Rock | 4/4 | — | dos, distintas | cuatro corcheas y ligadura |
| 18 | Piano Man | 3/4 | — | dos, por turnos | más silencios que notas |
| 19 | My Grandfather's Clock | 4/4 | 1 ♯ | dos | **reto** de fin de curso |
| 20 | Toreador · Bizet | 4/4 | 1 ♭ | dos | **reto** de fin de curso |

Las cuatro **rescatadas del dosier antiguo** son la 4, la 5, la 6 y la 12. Las
otras dieciséis salen de su carpeta nueva. Y **siete comparten fichero con otro
alumno, byte a byte** (comprobado por md5): las cuatro rescatadas más Rasputin,
el Grandfather's Clock y el Toreador — esas tres estaban en las dos carpetas con
nombres distintos y resultaron ser el mismo archivo. Eso es lo que vigila
`cruzar_eduard.py`: pueden compartir la **cita literal medida**, nunca el
**andamio inventado**.

---

## Los dos retos del final

El cliente los eligió: **"al final del curso, como reto"**. No están ahí porque
toquen en ese punto de dificultad, sino porque son la pieza con la que se cierra
el año. El Toreador es, además, la vara de medir del proyecto: la comparten
cuatro alumnos y su ritmo de marcha es **corchea con puntillo y semicorchea**,
no negra con puntillo y corchea. Es la única semicorchea del cuaderno de Eduard,
y está anotada como excepción justificada en `niveles.py` porque su partitura la
trae impresa.

---

## Las cinco lecturas que hubo que hacer a ojo

`medir_arranque` no las pudo leer, y lo que se vio está anotado en
`auditar_alturas.MIRADAS`. Mirarlas y no anotar el resultado sería mirarlas para
nada.

| partitura | qué le pasaba al lector | lo que se vio |
|---|---|---|
| Heart and Soul | la palabra **Swing** impresa encima tiene agujeros cerrados y se lee como una blanca | Do4 · Do4 · Do4 |
| I Have a Dream | la primera nota cuelga de dos líneas adicionales y va pegada a la cifra de compás | La3 · Mi4 · Re4 · Fa4 |
| Honor Him | con tres sostenidos el descuento de cabecera se pasa de largo | Do#4 · Fa#4 · La4 |
| Piano Man | el **silencio de blanca** es un rectángulo macizo y pasa por cabeza de nota | (silencio) Fa4 · Fa4 · Sol4 |
| Villancicos 4 manos | a cuatro manos las divisorias no unen los pentagramas del Primo | Mi5 · Mi5 · Mi5 |

Y una sexta que ya estaba: *Eso que tú me das*, cuya edición pega la cifra de
compás a la música y se come la primera nota.

---

## Qué se decidió y por qué

- **Las tres primeras piezas se tocan con una sola mano.** No es una
  simplificación nuestra: sus tres partituras traen un solo pentagrama. Es la
  única forma decente de empezar con un adulto que no ha tocado nunca — una
  cosa cada vez.
- **Las dos manos entran en la 4, y haciendo lo mismo.** Romance de Diabelli y
  The Beginner de Gurlitt son al unísono: se lee una melodía y se toca dos
  veces. Entre las dos está el salto real, que es la 7 (*La Pantera Rosa*), donde
  por primera vez cada mano hace lo suyo — y el arreglo lo pone fácil dejando
  que la izquierda entre sola y regalando tres compases para colocar la derecha.
- **La armadura no aparece hasta la 12.** Once piezas sin un solo sostenido ni
  bemol. Cuando llega, llega de una en una: un bemol (12), después La menor sin
  alteraciones (14), después tres sostenidos (15).
- **Los villancicos se adelantan a noviembre y diciembre** en el plan de curso
  aunque en el cuaderno estén en otro sitio. En enero no sirven.
- **Tres de las veinte son duetos** (4, 9 y 13), y por eso su hoja semanal lleva
  el bloque `a_cuatro_manos`: qué acordar con la otra persona antes de empezar.
  Un dueto no se estudia solo.
