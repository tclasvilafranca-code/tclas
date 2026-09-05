# Nel — las 17 partituras, comprobadas una a una

Nel tiene unos 12 años, lleva varios años viniendo a clase, es muy listo y le
gusta el piano, pero se desconcentra rápido. El encargo del cliente: subirle
el nivel y darle contenido para que se aplique, "dale caña".

Bajada de su carpeta de Drive con `gdown --folder` el 18 de agosto de 2026.
Traía 18 archivos; dos eran el mismo `Counting-stars` subido dos veces
(comprobado con `md5sum`), así que quedan **17 piezas distintas**.

## El dato más llamativo: 16 de las 17 son el mismo archivo que otro alumno

Comprobado con `md5sum` contra las carpetas de fuentes de todos los alumnos:

| archivo de Nel | idéntico a |
|---|---|
| Cant-Falling-in-love-elvis-presley. | jose_maria y josep (Can't Help Falling in Love) |
| A COMME AMOUR (Copia de Copia de) | jose_maria y josep |
| Como entrenar a tu dragon (Copia de Copia de) | jose_maria (Flying Theme) |
| Toreador. Bizet (Copia de Copia de) | jose_maria y merce |
| Counting-stars | jose_maria, josep y merce |
| Deck the Halls (NAVIDAD) | jose_maria y josep |
| LOVELY | josep |
| Merry-go-round-of-life | josep |
| Rasputin | jose_maria, luisa, josep y merce |
| bella-ciao (4 manos) | josep |
| heart-and-soul | luisa y josep |
| hit-the-road-jack | josep |
| jailhouse-rock | jose_maria, josep y merce |
| my-favourite-things | josep |
| petite chanson (4 manos) | josep |
| sweet-child-o-mine | josep |

Es decir: **el repertorio de Nel es, pieza a pieza, casi el mismo que el de
Josep** (14 de las 17 coinciden con su carpeta), con tres añadidas de José
María que Josep no tiene (A comme amour la comparten los dos, Toreador y
Flying Theme son solo de José María). La única pieza sin ningún duplicado en
el proyecto es **Rihanna - Diamond**.

Esto no es un problema — la norma del proyecto ya lo cubre: las citas
literales pueden coincidir entre alumnos, lo que no puede coincidir es el
andamio inventado, y eso lo comprobará `cruzar_nel.py`.

## La pieza propia: Rihanna - Diamond

Comprobada a 230 dpi: "Rihanna - Diamond, easy piano - short form". **Re
mayor** (dos sostenidos), 4/4, "♩ = 91". Empieza con una anacrusa (silencio y
una corchea de entrada) y la melodía lleva una nota larga ligada al final de
cada frase. La izquierda hace acordes de dos y tres notas: una redonda en el
primer compás y después notas dobles en negras. Trae letra completa y
digitación impresa en las dos manos.

## Lo que trae cada pieza (heredado de los álbumes ya medidos)

Con 16 de las 17 partituras ya transcritas nota a nota para otro alumno, no
hace falta remedirlas: se reutiliza la ficha musical (tonalidad, compás,
reparto de manos, dificultad concreta) tal como está documentada en
`jp_recetas.py` / `TRANSCRIPCION_JOSEP_FUENTES.md` y en los archivos
`jm_*.py` correspondientes, y se escribe un andamio **nuevo**, propio de Nel,
para que no coincida con el de nadie.

| pieza | ton. · compás | de dónde sale la ficha |
|---|---|---|
| Petite Chanson (4 manos) | Do · 4/4 | jp_02_petite.py |
| Heart and Soul | Do · 4/4, swing | jp_06_heart.py |
| Hit the Road Jack | Fa (1♭) · 4/4 | jp_07_hittheroad.py |
| Deck the Halls | Fa (1♭) · 4/4 | jm_07_deck.py |
| Jailhouse Rock | Do, blues · 4/4 · ♩=150 swing | jm_08_jailhouse.py |
| Bella Ciao (4 manos) | Sol menor (2♭) · 4/4 | jp_10_bellaciao.py |
| Can't Help Falling in Love | Re (2♯) · 3/4 | jm_11_canthelp.py |
| Lovely | Mi menor (1♯) · 4/4 · ♩=115 | jp_12_lovely.py |
| Rasputin | Si menor (2♯) · 4/4 · ♩=124 | jm_14_rasputin.py |
| Toreador · Carmen | Fa mayor (1♭) · 4/4 · Nivel 4 | jm_15_toreador.py |
| My Favourite Things | Sol (1♯) · 3/4 · ♩=160 | jp_15_favourite.py |
| Sweet Child O' Mine | Sib (2♭) · 4/4 · pedal escrito | jp_16_sweetchild.py |
| Merry Go Round of Life | Sib (2♭) · 3/4 · dos tempos | jp_18_merry.py |
| A comme amour | Mi m → La m · 4/4 · cambio de armadura | jp_19_acomme.py |
| Counting Stars | Do · 4/4 · digitación impresa | jm_04_counting.py |
| Flying Theme (Cómo entrenar a tu dragón) | Do → Re · 4/4 · cambia de tono | jm_19_flying.py |
| Rihanna - Diamond | Re (2♯) · 4/4 · ♩=91 | medida de cero, ver arriba |

## Lo que NO está medido, y por qué se dice

Todo el material generado va etiquetado como **andamio** y remite a la
partitura de Nel para las notas exactas — la regla de siempre.
