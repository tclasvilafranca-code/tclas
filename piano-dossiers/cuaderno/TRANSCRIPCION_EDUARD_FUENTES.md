# Eduard — mismo repertorio que José María

El cliente pidió un álbum "al nivel de José María" con "el mismo repertorio":
las 19 partituras de `students/jose_maria/source/` se han copiado tal cual a
`students/eduard/source/` (mismas ediciones, mismos archivos byte a byte). No
hace falta remedir nada: las 19 fichas musicales (tonalidad, compás, tempo,
reparto de manos, la dificultad concreta) ya están transcritas y verificadas
en los `jm_*.py` correspondientes, y se reutilizan sin cambios.

Lo que sí es nuevo, pieza a pieza, es el **andamio** (los ejercicios
inventados de las hojas de calentamiento y "cómo se estudia"): la norma del
proyecto es que las citas literales de la partitura pueden coincidir entre
alumnos que comparten fuente, pero el material inventado no. Con Eduard esto
es más estricto que con ningún otro álbum — comparte el 100% del repertorio
con un único alumno — así que cada `ed_*.py` se ha escrito con su propio
andamio, verificado sin coincidencias con `cruzar_eduard.py`.

## Las 19 piezas, y de dónde sale la ficha

| pieza | ton. · compás | de dónde sale la ficha |
|---|---|---|
| Romance (Diabelli, 4 manos) | Do · partido (¢) | jm_01_romance.py |
| America | Do · 3/4 | jm_02_america.py |
| The Star-Spangled Banner | Do · 3/4 | jm_03_banner.py |
| Counting Stars | Do · 4/4 | jm_04_counting.py |
| Peaches | Do · 4/4 | jm_05_peaches.py |
| Someone You Loved | — | jm_06_someone.py |
| Deck the Halls | Fa (1♭) · 4/4 | jm_07_deck.py |
| Jailhouse Rock | Do, blues · 4/4 · ♩=150 swing | jm_08_jailhouse.py |
| My Grandfather's Clock | Sol (1♯) · 4/4 | jm_09_clock.py |
| Shallow | — | jm_10_shallow.py |
| Can't Help Falling in Love | Re (2♯) · 3/4 | jm_11_canthelp.py |
| Carol of the Bells | — | jm_12_carol.py |
| Adagio (Albinoni) | — | jm_13_adagio.py (fuente JPEG, normalizada) |
| Rasputin | Si menor (2♯) · 4/4 · ♩=124 | jm_14_rasputin.py |
| Toreador · Carmen | Fa mayor (1♭) · 4/4 · Nivel 4 | jm_15_toreador.py |
| Trouble (Coldplay) | — | jm_16_trouble.py (PDF corrupto, normalizado con pdftocairo) |
| A comme amour | Mi m → La m · 4/4 · cambio de armadura | jm_17_acomme.py |
| Interstellar | — | jm_18_interstellar.py |
| Flying Theme (Cómo entrenar a tu dragón) | Do → Re · 4/4 · cambia de tono | jm_19_flying.py |

## Lo que NO está medido, y por qué se dice

Todo el material generado va etiquetado como **andamio** y remite a la
partitura de Eduard para las notas exactas — la regla de siempre.
