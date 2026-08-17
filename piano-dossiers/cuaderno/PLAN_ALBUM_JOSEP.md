# Álbum de Josep — adulto con recorrido · 19 piezas · seis hojas

Josep es de la edad y el nivel de José María, **pero lleva más tiempo en
clase**, le gustan los retos y las partituras que no son del todo fáciles. El
encargo del cliente fue literal: *"le puedes dar un poco más de caña"*.

El formato no cambia —es el mismo de adulto, seis hojas, con dedos y lectura
separadas— porque es el que corresponde a su perfil. Lo que cambia es el
listón, y cambia en cuatro sitios concretos, no en el tono de los textos.

## Lo que le sube el listón

| bloque | qué hace | dónde va |
|---|---|---|
| **`reto`** | nombra la dificultad concreta de la semana y dice **con qué se gana** | 11 de las 19 hojas |
| **`escalera`** | el metrónomo por escalones, con una **meta escrita** y de dónde sale el número | 8 hojas |
| **`cifrado`** | las letras de acorde que **su partitura trae impresas**: qué notas son | 6 hojas |
| **`cuatro_manos`** | qué hay que acordar con la otra persona antes del primer compás | las 4 piezas que son duetos |

Los dos primeros son de método —lo que separa a un alumno que lleva tiempo de
uno que empieza es que ya puede trabajar con un objetivo medido—. Los dos
últimos **no son decoración: salen de sus partituras**.

- El `cifrado` solo se pone en las **siete piezas cuya edición imprime de
  verdad las letras de acorde** (5, 8, 11, 13, 15, 17 y 19). En las demás,
  Josep no vería en su papel lo que la hoja le pide leer.
- El `cuatro_manos` solo va en los **cuatro duetos** (1, 2, 10 y 14). Su
  carpeta tiene cuatro, que es un rasgo suyo: José María solo tenía uno.

Lo comprueba `jp_recetas.revisar_reparto`, que falla si alguno de los dos cae
donde la partitura no lo justifica.

## Las seis hojas

| hoja | qué es | módulo |
|---|---|---|
| — | la partitura original | el PDF de su carpeta, sin tocar |
| 1 | **Ficha de la partitura** | `ficha_info.py` |
| 2 | **Dedos** — calentamiento, hoja llena y generada | `hoja_calentamiento.py` |
| 3 | **Leer** — agudeza visual, hoja llena y generada | `hoja_lectura.py` |
| 4 | **Cómo se estudia** — el orden de trabajo al piano | `hoja_piano.py` |
| 5 | **El trabajo de esta semana** | `hoja_deberes.py` |
| 6 | **Para escribir** — papel pautado | `hoja_pauta.py` |

## El reparto de las 19 hojas de trabajo

Diez recetas (`jp_recetas.py`), nueve usadas dos veces y una una sola vez. **No
es la rotación simple de José María**: las parejas están elegidas para que las
dos hojas de cada receta caigan donde su bloque tiene sentido.

```
P1  → 1, 10    duetos            P6  → 6, 16
P2  → 2, 14    duetos            P7  → 7, 18
P5  → 5, 15    con cifrado       P8  → 8, 17    con cifrado
P10 → 11, 19   con cifrado       P3  → 3, 12    P4 → 4, 13
P9  → 9        (una sola vez)
```

La distancia mínima entre los dos usos de una receta queda en **ocho hojas**
(la más corta es P10: 11 y 19). En José María eran diez, pero allí ninguna
receta estaba atada a una propiedad de la partitura. `auditar_josep` audita en
ocho, no en los seis del auditor genérico.

**Lo que sale las 19 semanas y no cuenta para el tope de frecuencia:** el
`plan` de minutos por día y el recuadro `para la próxima clase`. Los dos van
como estructurales, porque el hilo entre lo que hace en casa y lo que pregunta
el día de la clase no se corta ninguna semana.

## De dónde salen las partituras

Carpeta de Drive de Josep, bajada con `gdown --folder` y verificada una a una
por el **título impreso dentro del archivo**, con la armadura y el compás
leídos a 250–300 dpi. La tabla completa está en `TRANSCRIPCION_JOSEP_FUENTES.md`.

**Ocho de las diecinueve son el mismo archivo que las de José María**, byte a
byte. Las citas literales pueden coincidir —es la misma partitura—, pero el
material inventado no: lo comprueba `cruzar_josep.py`, y en la primera pasada
encontró seis coincidencias de ocho eventos que hubo que deshacer.

## El orden: de menos a más difícil

### 1 · La mano quieta, y entre dos
Las dos primeras son duetos: se empieza el curso tocando con alguien.

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 1 | Romance · Diabelli (Primo, a 4 manos) | Do · ¢ | posición fija de cinco dedos, y las dos manos al unísono |
| 2 | Petite Chanson · Collu (a 4 manos) | Do · 4/4 | anacrusa, y un salto de octava en el primer compás (medido) |

### 2 · La izquierda sostiene

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 3 | Peaches (Super Mario Bros.) | Do · 4/4 | doce compases con la izquierda en redondas |
| 4 | Counting Stars · OneRepublic | Do · 4/4 | digitación impresa nota a nota: hay que obedecerla |
| 5 | What Was I Made For? · Billie Eilish | Do · 4/4 | notas fáciles y entradas a contratiempo · **primer cifrado** |

### 3 · El swing y el acorde

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 6 | Heart and Soul · Carmichael | Do · 4/4 | primer swing, y la izquierda pasa a bajo + acorde |
| 7 | Hit the Road Jack | Fa (1♭) · 4/4 | **la primera armadura** del cuaderno |
| 8 | Deck the Halls | Fa (1♭) · 4/4 | dobles notas en las dos manos, y el primer acorde con séptima |
| 9 | Jailhouse Rock · Elvis | Do · 4/4 | ♩ = 150: la primera pieza rápida de verdad |

### 4 · Más tonalidades, y las dos manos de verdad

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 10 | Bella Ciao (a 4 manos) | Sol menor (2♭) · 4/4 | primer tono menor, con la sensible escrita a mano |
| 11 | Can't Help Falling in Love · Elvis | Re (2♯) · 3/4 | izquierda en corcheas sin descanso, y cinco acordes |
| 12 | Lovely · Billie Eilish | Mi menor (1♯) · 4/4 | corcheas de principio a fin: resistencia |
| 13 | Rasputin · Boney M | Si menor (2♯) · 4/4 | compases callados a ♩ = 124 |
| 14 | It's Beginning to Look… (a 4 manos) | Do · **6/8** | el único compás ternario del cuaderno |

### 5 · Los cinco retos del final
Llegan en abril, mayo, junio y julio, y a propósito.

| nº | pieza | ton. · compás | por qué al final |
|---|---|---|---|
| 15 | My Favourite Things | Sol (1♯) · 3/4 | 55 compases en una página, a ♩ = 160 |
| 16 | Sweet Child O' Mine · Guns N' Roses | Sib (2♭) · 4/4 | el **pedal escrito** compás a compás |
| 17 | Un Beso y una Flor · Nino Bravo | Fa (1♭) · C | semicorcheas desde el primer compás, y tresillos al final |
| 18 | Merry Go Round of Life · Hisaishi | Sib (2♭) · 3/4 | terceras en corcheas y **dos tempos escritos** (120 y 152) |
| 19 | A comme amour · Clayderman | Mi m → La m · 4/4 | el **único cambio de armadura** del cuaderno |

## Lo medido nota a nota

Tres piezas tienen material medido y no andamio: **Petite Chanson** (anacrusa y
primer compás, con el salto de octava), **Heart and Soul** (los dos primeros
compases) y **Jailhouse Rock** (el compás 12). Todo lo demás va etiquetado como
andamio y remite a la partitura del alumno, que es la regla del proyecto.

Esa tercera medición destapó un **error ya impreso en el cuaderno de José
María**: allí se decía que la mano izquierda del c. 12 bajaba con los dedos
5 · 3 · 2 · 1, y sube (Fa · La · Do · Re). Corregido en los dos álbumes.

## Verificación pasada antes de entregar

- `python3 cuaderno/auditar_josep.py` → **TODO OK** en las 19 piezas (compases,
  margen derecho, material repetido entre hojas, altura final de cada hoja y
  texto que no cabe en su caja) **más la variedad**: 19 hojas, 10 esqueletos
  distintos, **21 tipos**, y el reparto cumplido una a una.
- `python3 cuaderno/cruzar_josep.py` → **0 sistemas compartidos con José María**
  y 0 repetidos dentro del propio álbum.
- **Portada, índice y plan**: 0 desbordes de texto, 0 cajas desbordadas.
- **Píxeles del álbum montado** (147 páginas): de las 116 hojas nuestras,
  **0 desbordes por abajo y 0 por la derecha**.

## Salida

`output/Josep_Cuaderno_del_Pianista_2026.pdf` · **147 páginas**
(portada + índice + plan de curso de 44 semanas + las 19 piezas).
