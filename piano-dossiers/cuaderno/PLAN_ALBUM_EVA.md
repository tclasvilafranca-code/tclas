# Álbum de Eva — nivel avanzado · 17 piezas

## De dónde salen las partituras

Carpeta de Drive de Eva, bajada con `gdown --folder` y verificada una a una por
el **título impreso dentro del PDF**, no por el nombre del archivo.

**Quince de las diecisiete son byte a byte las mismas que las de Dilan**
(comprobado por sha256). Solo dos son nuevas:

| pieza | páginas | tonalidad | compás | tempo impreso |
|---|---|---|---|---|
| When We Were Young · Adele | 4 | Re menor (1 bemol) | 4/4 | ♩ = 72 |
| Bohemian Rhapsody · Queen | 2 | Si♭ mayor (2 bemoles) | 4/4 · 5/4 · 2/4 | ♩ = 66 |

Por eso Eva lleva **hojas propias**: mismo material medido, pero ejercicios y
hojas generadas distintos. Y la semilla de las hojas generadas lleva una sal
por alumno (`cancion._sal_alumno`), o las canciones compartidas saldrían
idénticas a las de Dilan.

## El orden: de menos a más difícil

Criterio del cliente. La dificultad se mide por **cuántas cosas distintas tiene
que hacer la alumna a la vez**, no por la velocidad ni por el número de notas.
Las tres de Navidad quedan repartidas por dificultad; el **plan de curso** ya se
encarga de adelantarlas a diciembre, que para eso está.

### 1 · La izquierda hace siempre lo mismo
Un solo molde que se repite; lo único que cambia es dónde se pone.

| nº | pieza | ton. | por qué aquí |
|---|---|---|---|
| 1 | Can't Help Falling in Love | Re M · 3/4 | arpegio fijo fund·3ª·5ª·8ª; la derecha, una nota por compás |
| 2 | A Sky Full of Stars | Fa M · 4/4 | dos notas alternando, y cuatro compases de música en toda la pieza |
| 3 | Poema de Amor | Sol m · 4/4 | molde de cuatro negras que no cambia nunca |
| 4 | What Was I Made For? | Do M · 4/4 | seis acordes; lo difícil no son los dedos, es contar los silencios |

### 2 · Sostener, y entrar a tiempo
La mano deja de moverse y el problema pasa a ser el reloj.

| nº | pieza | ton. | por qué aquí |
|---|---|---|---|
| 5 | Thinking Out Loud | Re M · 4/4 | redondas en la izquierda y una derecha que entra siempre tarde |
| 6 | El Cisne | Sol M · 3/4 | 55 compases de arpegio: no es difícil, es largo y hay que igualarlo |
| 7 | When I Was Your Man | Do M · 4/4 | cinco posiciones de memoria y el salto entre ellas |

### 3 · Dos cosas a la vez
Aquí empieza la independencia de verdad.

| nº | pieza | ton. | por qué aquí |
|---|---|---|---|
| 8 | La Promesa | Sol M · 4/4 | bajo y acorde a más de una octava: no lo aguanta la mano, lo aguanta el pedal |
| 9 | Amiga Mía | Re M · 4/4 | una sola mano sosteniendo una voz y moviendo otra |
| 10 | **When We Were Young** | Re m · 4/4 | corcheas continuas con letra, cuatro páginas y marcas de 8vb |

### 4 · El ritmo manda
La dificultad se va del teclado a la cabeza.

| nº | pieza | ton. | por qué aquí |
|---|---|---|---|
| 11 | Soldadito de Hierro | Do M · 4/4 | tresillos de principio a fin |
| 12 | My Favourite Things | Mi m · 3/4 | vals a ♩=160: el salto dura menos de medio segundo |
| 13 | Have Yourself a Merry Little Christmas | Do M · 4/4 | tres capas sonando a la vez, y hay que decidir el volumen de cada una |

### 5 · Leer la hoja, y tocar con otra persona
Lo último no es técnica: es orientarse y coordinarse.

| nº | pieza | ton. | por qué aquí |
|---|---|---|---|
| 14 | Santa Tell Me | Sol M · 4/4 | segno, dos casillas, coda, 8vb y cruce de manos |
| 15 | It's Beginning to Look a Lot Like Christmas | Do M · 6/8 · 4 manos | el 6/8 contado en dos, y entrar con otra persona |
| 16 | Arabesque | La m · 2/4 · 4 manos | semicorcheas picadas y las dos manos al unísono, a dúo |
| 17 | **Bohemian Rhapsody** | Si♭ M | cambia de compás tres veces, armonía cromática con alteraciones a mano en casi todos los compases, la izquierda cambia de textura entera en la página 2, y D.S. al Fine |

## Estado

| nº | pieza | transcripción | hojas | auditoría |
|---|---|---|---|---|
| 1 | Can't Help Falling in Love | heredada de Dilan | ✔ | OK |
| 2 | A Sky Full of Stars | heredada | ✔ | OK |
| 3 | Poema de Amor | heredada | ✔ | OK |
| 4 | What Was I Made For? | heredada | ✔ | OK |
| 5 | Thinking Out Loud | heredada | ✔ | OK |
| 6 | El Cisne | heredada | ✔ | OK |
| 7 | When I Was Your Man | heredada | ✔ | OK |
| 8 | La Promesa | heredada | ✔ | OK |
| 9 | Amiga Mía | heredada (todo andamio) | ✔ | OK |
| 10 | **When We Were Young** | **nueva** · `TRANSCRIPCION_E10_WWWY.md` | ✔ | OK |
| 11 | Soldadito de Hierro | heredada | ✔ | OK |
| 12 | My Favourite Things | heredada | ✔ | OK |
| 13 | Have Yourself a Merry Little Christmas | heredada | ✔ | OK |
| 14 | Santa Tell Me | heredada | ✔ | OK |
| 15 | It's Beginning to Look a Lot Like Christmas | heredada (4 manos) | ✔ | OK |
| 16 | Arabesque | heredada (4 manos) | pendiente | — |
| 17 | **Bohemian Rhapsody** | **nueva**, por medir | pendiente | — |

Portada, índice y plan de curso de Eva: pendientes, al final.

### Cómo se garantiza que no es una fotocopia del álbum de Dilan

Quince piezas comparten edición con Dilan. Para que las hojas sean propias:

1. **La ruta de estudio es distinta en cada pieza**, y el porqué está escrito
   en el docstring del módulo (a Dilan se le entra por un sitio, a Eva por
   otro, y siempre hay una razón musical).
2. **Las hojas generadas llevan una sal por alumno** (`cancion._sal_alumno`),
   o el calentamiento, la agudeza y la relajación saldrían idénticos.
3. **`cruzar.py` compara sistema a sistema los dos cuadernos.** Lo que puede
   coincidir es la CITA LITERAL de un compás medido —eso es lo correcto, la
   partitura es la misma—; lo que no puede coincidir es un ejercicio de
   ANDAMIO, porque ese me lo he inventado yo y debe ser distinto para cada
   alumna. A 16/08, con las quince primeras escritas, no queda ningún andamio compartido: todo lo que coincide es cita literal de compases medidos.
