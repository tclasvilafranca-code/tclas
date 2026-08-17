# Álbum de José María — adulto que empieza · 19 piezas · formato de seis hojas

José María tiene unos 60 años, empezó hace poco, **viene a clase** y se ha
comprado un teclado para practicar en casa. El encargo: **material para
trabajar de verdad, pero a un nivel que no agobie**. Eso decide dos cosas.

1. **Los seis días que hay entre clase y clase se decide la semana.** No es
   que estudie por su cuenta: tiene profesora. Lo que hay que resolver es qué
   se lleva de la clase para el resto de la semana, y por eso su hoja semanal
   lleva **plan de minutos por día**, **tabla de metrónomo** y un recuadro
   **"para la próxima clase"**, que no existen en ningún otro cuaderno del
   proyecto.
2. **No es un niño.** Nada de sopas de letras, adivinanzas, crucigramas ni
   ritmos de palabras: eso es de Arnau. Los ejercicios son los mismos de
   siempre (nombres, figuras, contar, diferencias, teclado, inventar…) con
   redacción de adulto.

## Las seis hojas

| hoja | qué es | módulo |
|---|---|---|
| — | la partitura original | el PDF de su carpeta, sin tocar |
| 1 | **Ficha de la partitura** | `ficha_info.py` |
| 2 | **Dedos** — calentamiento, hoja llena y generada | `hoja_calentamiento.py` |
| 3 | **Leer** — agudeza visual, hoja llena y generada | `hoja_lectura.py` |
| 4 | **Cómo se estudia** — el orden de trabajo al piano (dos hojas si la pieza lo pide) | `hoja_piano.py` |
| 5 | **El trabajo de esta semana** — plan, metrónomo y ejercicios escritos | `hoja_deberes.py` |
| 6 | **Para escribir** — papel pautado | `hoja_pauta.py` |

Decisión del cliente: **dedos y lectura en hojas separadas**, no fundidas en
una como en el formato corto de Arnau.

El reparto de las 19 hojas de trabajo está en `jm_recetas.py`: diez recetas,
cada una usada dos veces y con diez hojas de distancia. Lo comprueban
`auditar_variedad.py` y `jm_recetas.revisar_reparto`, igual que en Arnau. El
`plan` es el único bloque que sale las 19 semanas, y cuenta como estructural.

El bloque que en el cuaderno de Arnau es *"un juego con alguien de casa"* aquí
es **"para la próxima clase"** (`jm_comun.para_clase`): a José María no le hace
falta un juego, le hace falta llegar el día de la clase con el trabajo hecho
por donde tocaba y sabiendo qué preguntar.

## De dónde salen las partituras

Carpeta de Drive de José María, bajada con `gdown --folder` y verificada una a
una por el **título impreso dentro del archivo**. La tabla completa —edición,
armadura, compás, tempo impreso y páginas— está en
`TRANSCRIPCION_JM_FUENTES.md`, junto con lo medido nota a nota.

Dos avisos que salieron de esa comprobación:

- **`ADAGIO.` no es un PDF, es un JPEG.** Hay que convertirlo antes de montar
  el álbum.
- Los dos villancicos que había antes en la carpeta (Jingle Bells y Leise
  rieselt) **ya no están**; en su lugar hay Adagio y Flying Theme. El álbum se
  monta con lo que hay hoy.

## El orden: de menos a más difícil

Criterio del cliente. Las cuatro o cinco duras van al final del curso, que es
lo que se acordó: **las 19, ordenadas**, y las difíciles cuando ya esté listo.

### 1 · La mano quieta
La mano se coloca una vez y no se mueve. Es donde hay que empezar a los 60 y a
los 10.

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 1 | Romance · Diabelli (Primo, a 4 manos) | Do · ¢ | la edición lo dice: posición fija de cinco dedos, y las dos manos al unísono |
| 2 | America (My Country, 'Tis of Thee) | Do · 3/4 | Level Two, letra y digitación impresas; melodía de siete notas |
| 3 | The Star-Spangled Banner | Do · 3/4 | Level 2, letra y digitación; empieza con silencio |

### 2 · La izquierda aguanta, la derecha se mueve
La izquierda toca redondas y ya está. Todo el trabajo es de la derecha.

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 4 | Counting Stars · OneRepublic | Do · 4/4 | *Easy Version*: izquierda en redondas y digitación impresa |
| 5 | Peaches (Super Mario Bros. Movie) | Do · 4/4 | igual, y la melodía es corta y se repite |
| 6 | Someone You Loved · Lewis Capaldi | Do · 4/4 | izquierda en redondas, pero la derecha ya va en corcheas seguidas |

### 3 · La primera armadura
Aparece la primera tecla negra fija, y con ella la costumbre de mirar el
principio del pentagrama antes de tocar.

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 7 | Deck the Halls | Fa (1♭) · 4/4 | un bemol: todos los Si van a la tecla negra |
| 8 | Jailhouse Rock · Elvis | Do · 4/4 | una página, ♩=150 con swing: la primera pieza rápida |
| 9 | My Grandfather's Clock | Sol (1♯) · 4/4 | Level Three, un sostenido, y "with precision" |
| 10 | Shallow · Lady Gaga | Sol (1♯) · 4/4 | la misma armadura, y una melodía que ya conoce |

### 4 · Más tonalidades, y las dos manos de verdad

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 11 | Can't Help Falling in Love · Elvis | Re (2♯) · 3/4 | dos sostenidos, y la izquierda en corcheas |
| 12 | Carol of the Bells | Sol menor (2♭) · 3/4 | la primera en tono menor |
| 13 | Adagio · Albinoni | 3/4 · Adagio ♩=60 | lento de verdad: aquí lo difícil es el sonido, no las notas |
| 14 | Rasputin · Boney M | Si menor (2♯) · 4/4 | *easy piano*, pero a ♩=124 |
| 15 | Toreador, de *Carmen* | Fa (1♭) · 4/4 | Level Four: el salto de nivel de la edición |

### 5 · Los retos del final
Aquí es donde el cuaderno deja de ser cómodo, y a propósito: llegan en junio y
julio, no en octubre.

| nº | pieza | ton. · compás | por qué al final |
|---|---|---|---|
| 16 | Trouble · Coldplay | Sol (1♯) · 4/4 | cuatro páginas a ♩=138 |
| 17 | A comme amour · Clayderman | Mi menor (1♯) · 4/4 | semicorcheas seguidas de principio a fin |
| 18 | Interstellar · Hans Zimmer | 3/4 · ♩=96 | seis páginas: la más larga del cuaderno |
| 19 | Flying Theme (*Cómo entrenar a tu dragón*) | Do → Re (2♯) · 4/4 | tres páginas, corcheas en las dos manos y cambio de tonalidad a mitad |

## Dos cosas que había que arreglar en las fuentes

Las partituras las sube el cliente a Drive y llegan como llegan. En este álbum
salieron dos casos que rompían el montaje, y los dos los resuelve ahora
`cuaderno/fuente.py` al vuelo, sin tocar los originales:

- **El Adagio no era un PDF**, era un JPEG. Se convierte.
- **Trouble (Coldplay) tiene dentro un objeto mal formado.** `pypdf` lo abre y
  cuenta bien las páginas, pero al copiarlas revienta con `LimitReachedError`.
  Se reescribe con `pdftocairo`.

Está hecho así, y no como un apaño a mano, porque las partituras no se
versionan: el álbum tiene que poder montarse de cero en una máquina limpia
bajando la carpeta de Drive otra vez.

## Verificación pasada antes de entregar

- `python3 cuaderno/auditar_josemaria.py` → **TODO OK** en las 19 piezas
  (compases, margen derecho, material repetido entre hojas, altura final de
  cada hoja y texto que no cabe en su caja) **más la variedad**: 19 hojas de
  trabajo, 10 esqueletos distintos, 18 tipos, y el reparto cumplido una a una.
- **Portada, índice y plan**: 0 desbordes de texto, 0 cajas desbordadas.
- **Píxeles del álbum montado** (157 páginas): de las 116 hojas nuestras,
  **0 desbordes por abajo y 0 por la derecha**.

## Salida

`output/JoseMaria_Cuaderno_del_Pianista_2026.pdf` · **157 páginas**
(portada + índice + plan de curso + las 19 piezas).
