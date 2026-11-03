# Luisa — las 19 partituras, comprobadas una a una

Luisa es la **abuela de Arnau**. Empezó hace poco, es mayor y le gusta el
piano. El encargo del cliente, literal: *"poquito pero bien, que se entienda
todo, sencillo"*. Eso no cambia el esquema del dosier —es el mismo de todos los
adultos— sino el nivel: **nivel de iniciación, el más bajo del proyecto**.

Bajadas de su carpeta de Drive con `gdown --folder` el 18 de agosto de 2026. De
cada una se ha comprobado **el título impreso dentro del archivo** (no el
nombre), y la armadura y el compás se han leído a **230 dpi**, no a ojo: en el
álbum de Josep dos lecturas a baja resolución salieron mal y hubo que
corregirlas.

## Avisos sobre los archivos

- **Los 19 son PDF de verdad**, aunque seis vienen sin extensión o con la
  extensión en medio del nombre (`bela-ciao.easy`, `LA PRIMAVERA.pdf easy`,
  `nocturne-op9-chopin. easy`, `piano-man-easy.`, `puff-the-magic-dragon.`,
  `Silent-Night.easy`). Se abren igual.
- **Ninguna pasa de dos páginas.** Es la carpeta más corta del proyecto, y
  encaja exactamente con lo que se pidió.
- **Dos son el mismo archivo que las de otro alumno**, byte a byte:
  *Heart and Soul* (Josep) y *Rasputin* (José María y Josep). Las citas
  literales pueden coincidir; el material inventado no. Lo comprueba
  `cruzar_luisa.py`.
- `Silent-Night.easy` tiene el texto codificado con un desplazamiento (el
  extractor devuelve `4IFFUNVTJDGSFFDPN` por `sheetmusicfree.com`), así que su
  título se comprobó **mirando la página**, no extrayendo texto.

## La tabla

| # | pieza | edición | ton. | compás | tempo/carácter | págs |
|---|---|---|---|---|---|---|
| 1 | Sonatina per bambini | M. Bazzoni · **a 4 manos** · parte *Children 1* | La menor | 4/4 | — | 2 |
| 2 | The Beginner, Le Début | C. Gurlitt · op. 211 nº 3 · **a 4 manos** · Primo | Do | 3/4 | Allegretto | 1 |
| 3 | Sonatina nº 2 | M. Bazzoni · **a 4 manos** · Pianoforte 1 | **Sol (1♯)** | 4/4 | — | 2 |
| 4 | You've Got a Friend in Me | arr. Megan Harper · *Easy* | Do | 4/4 | — | 1 |
| 5 | Puff the Magic Dragon | arr. Eric Moore | Do | 4/4 | — | 1 |
| 6 | I Have a Dream · Abba | INeVENT Music Academy | Do | 4/4 | ♩ = 120 | 2 |
| 7 | Christmas Songs for Four Little Hands | Mindy Liang · **a 4 manos** · *Beginner* | Do | 4/4 | ♩ = 100 | 2 |
| 8 | Silent Night | F. X. Gruber · con letra y digitación | Do | 3/4 | Gently | 2 |
| 9 | Spring (*Las cuatro estaciones*) | Vivaldi · *(easy)* | Do | 4/4 | — | 1 |
| 10 | Titanic | James Horner · arr. A. C. Escobés | Do | **2/4** | Adagio | 1 |
| 11 | Piano Man | Billy Joel · arr. JuanM04 · *SimplyPiano* | Do | 3/4 | ♩ = 178 | 2 |
| 12 | La Panthère rose | *Première année* · con digitación impresa | Do · con ♯ escritos | 4/4 | — | 1 |
| 13 | Bela Ciao (*La Casa de Papel*) | — | **Mi menor (1♯)** | **2/4** | — | 1 |
| 14 | Heart and Soul | Hoagy Carmichael · *Easy Piano Version* | Do | 4/4 | ♩ = 110 **Swing** | 1 |
| 15 | Greensleeves | tradicional inglesa · con cifrado y pedal | La menor | 3/4 | Moderato | 2 |
| 16 | Chim Chim Cher-ee (*Mary Poppins*) | R. M. Sherman · arr. A. C. Escobés | La menor | 3/4 | Allegro | 1 |
| 17 | Rasputin · Boney M | Musescore · *Easy piano* | **Si menor (2♯)** | 4/4 | ♩ = 124 | 2 |
| 18 | Für Elise | Beethoven · *Easy Ver.* | La menor | 3/4 | — | 1 |
| 19 | Nocturne op. 9 | Chopin · arr. Benny Chaw | Do | 3/4 | *mp* | 1 |

## Lo que trae cada pieza, medido

Esto es lo que decide el orden, y sale de mirar la partitura.

| # | por qué está donde está |
|---|---|
| 1 | dueto: **las dos manos tocan lo mismo**, los dos pentagramas en clave de sol, y **solo negras** |
| 2 | igual de mecánica, con negras y blancas y compás de tres |
| 3 | igual, y aparece **la primera armadura** — que con las dos manos al unísono no cuesta nada |
| 4 | la izquierda hace **una redonda de una sola nota** por compás |
| 5 | lo mismo, pero la redonda es de **dos notas** |
| 6 | lo mismo con letra debajo, y la derecha ya tiene puntillos |
| 7 | dueto: la izquierda pasa a **blancas** y hay que llevar el pulso con otra persona |
| 8 | negra + blanca en la izquierda, y **digitación impresa** |
| 9 | **anacrusa** y barra de repetición |
| 10 | **compás de 2/4**, el primero del cuaderno, y corchea con puntillo |
| 11 | 3/4 a **♩ = 178**: rápido de reloj y fácil de manos |
| 12 | entra **tras tres compases callados** y trae muchos sostenidos escritos |
| 13 | **tono menor** y 2/4, con corcheas seguidas |
| 14 | primer **swing**, y la izquierda pasa a bajo + acorde |
| 15 | cifrado impreso, **pedal** y la izquierda en tres negras por compás |
| 16 | **dobles notas** en la derecha, con silencio en cada primer tiempo |
| 17 | dos sostenidos y ♩ = 124 |
| 18 | **corcheas seguidas** de principio a fin: la más difícil de dedos |
| 19 | de notas es de las más fáciles y **de sonido es la más difícil**: va al final por eso, para la audición |

## Cómo se leyeron las armaduras

Render a 230 dpi del comienzo de cada pieza y lectura del hueco entre la clave
y la primera nota. Merece la pena decir lo que se encontró:

- **Ocho de las diecinueve no llevan armadura pero sí alteraciones escritas
  delante de las notas** (Chim Chim Cher-ee, Für Elise, Greensleeves, la
  Sonatina per bambini y La Panthère rose son las más cargadas). En el cuaderno
  se dicen así: *"la tecla negra no está al principio, está escrita delante de
  la nota"*.
- Solo **tres piezas tienen armadura de verdad**: Sonatina nº 2 (1♯), Bela Ciao
  (1♯) y Rasputin (2♯).
- **Dos compases nuevos** respecto a los otros cuadernos de adulto: el 2/4 de
  Titanic y de Bela Ciao.

## Lo que NO está medido, y por qué se dice

Ninguna pieza está transcrita nota a nota. Todo el material generado va
etiquetado como **andamio**: conserva el compás y la tonalidad medidos y remite
a la partitura de Luisa para las notas exactas. Es la regla del proyecto, y con
un alumno de iniciación importa más que con nadie: una nota inventada en una
hoja suya no la va a detectar ella.
