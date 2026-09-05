# Mercè — las 27 partituras, comprobadas una a una

Mercè tiene unos 65 años y una peculiaridad respecto al resto: viene **hora y
media cada semana**, la clase más larga del proyecto. No tiene un nivel alto,
pero le gusta mucho el piano y aprender. Formato adulto, el mismo esquema que
José María, Josep y Luisa —partitura, ficha, calentamiento, agudeza visual,
cómo se estudia, relajación con el recuadro de la profesora, papel pautado—;
lo que cambia es el nivel y, por la clase más larga, cuánto material cabe por
semana.

Bajada de su carpeta de Drive con `gdown --folder` el 18 de agosto de 2026. De
cada archivo se ha comprobado el título impreso dentro del PDF, y la armadura
y el compás se han leído a 230 dpi.

## Aviso importante: 17 de las 27 son el mismo archivo que otro alumno

Comprobado con `md5sum` contra las carpetas de fuentes de todos los alumnos:

| archivo de Mercè | idéntico a |
|---|---|
| -Greensleeves.pdf | luisa (pieza 15) |
| Grandfather.pdf | jose_maria (Grandfather's Clock) |
| Hay un amigo en mi.pdf | luisa (pieza 4, You've Got a Friend in Me) |
| Jailhouse Elvis Presley.pdf | jose_maria y josep (Jailhouse Rock) |
| La Pantera Rosa.pdf | luisa (pieza 12) |
| Maurizio Bazzoni sonatina para 4 manos.pdf | luisa (pieza 1, Sonatina per bambini) |
| Piano Men.pdf | luisa (pieza 11, Piano Man) |
| Puff era un Drac Magic.pdf | luisa (pieza 5, Puff the Magic Dragon) |
| Rasputin.pdf | jose_maria, josep y luisa (pieza 17) |
| SILENT NINGT.easy | luisa (pieza 8, Silent Night) |
| TOREADOR-BIZET. Bizet | jose_maria (Toreador) |
| bazzoni-...-sol-maggiore-174724. | luisa (pieza 3, Sonatina nº2) |
| bela-ciao.pdf | luisa (pieza 13) |
| christmas-songs-for-four-little-...pdf | luisa (pieza 7, Christmas Songs) |
| counting-stars-.pdf | jose_maria y josep (Counting Stars) |
| i-have-a-dream-abba-.pdf | luisa (pieza 6) |
| nocturne-op9-chopin. | luisa (pieza 19, Nocturne) |

Esto no es un problema: la regla del proyecto es que las **citas literales**
pueden coincidir entre alumnos (es la misma partitura), y lo que no puede
coincidir es el **andamio inventado**. Lo comprobará `cruzar_merce.py`, igual
que con Josep y Luisa.

## Las 10 piezas propias de Mercè, comprobadas

| # | pieza | edición | ton. | compás | tempo/carácter | págs |
|---|---|---|---|---|---|---|
| A | Largo — Sinfonía nº5 (*sic*) Op. 95 | A. Dvorak · "del Nuevo Mundo" · arr. A. C. Escobés | Do mayor | 4/4 | Largo | 1 |
| B | Beauty and the Beast | arr. Naf | **Fa mayor (1♭)** | 4/4 | ♩ = 80 | 1 |
| C | Honor Him (Gladiator) | Hans Zimmer · *Easy Version* | **La mayor (3♯)** | 3/4 | ♩ = 70 | 1 |
| D | Spring, de Las cuatro estaciones | Vivaldi · edición distinta a la de Luisa | Do mayor | 4/4 | Allegro | 1 |
| E | Oh, When the Saints | *Primer Level* · arr. Gilbert DeBenedetti | Do mayor | 4/4 | Lively | 1 |
| F | Für Elise | Beethoven · edición REAL, no simplificada | **La menor** | 3/4 | — | 1 |
| G | Sur le Pont d'Avignon | *Deuxième Niveau* · arr. Gilbert DeBenedetti | Do mayor | 4/4 (c) | Pas trop vite | 1 |
| H | Do-Re-Mi (Sonrisas y Lágrimas) | R. Rodgers · arr. A. C. Escobés | Do mayor | 4/4 | Andantino | 1 |
| I | We Wish You a Merry Christmas | arr. Gilbert DeBenedetti · con letras de acorde | **Sol mayor (1♯)** | 3/4 | — | 2 |
| J | Silent Night, a cuatro manos | Piano 1 + Piano 2 | Do mayor | 3/4 | — | 1 |

## Aviso sobre la pieza F (Für Elise)

Es la edición REAL de la pieza, no una versión fácil: figuras rápidas, saltos
de octava en la mano izquierda y el ornamento característico del principio
escrito nota a nota. Es, con diferencia, la partitura más exigente de toda su
carpeta. Igual que ya pasó con Rasputin o Jailhouse Rock en otros álbumes, la
solución no es sustituir la partitura (es la que el cliente compartió) sino
que **el material generado —calentamiento, agudeza, cómo se estudia— se
queda en el nivel real de Mercè**, y la hoja "cómo se estudia" trabaja solo un
fragmento pequeño y muy reducido del arranque, dejando el resto para más
adelante o para tocar solo de oído con ayuda de la profesora en clase.

## Cómo se lee esto en conjunto

- **17 piezas ya están medidas** de otros álbumes (Greensleeves, Grandfather,
  You've Got a Friend, Jailhouse, La Panthère rose, dos sonatinas de Bazzoni,
  Piano Man, Puff, Rasputin, Silent Night con letra, Toreador, Bela Ciao,
  Christmas Songs, Counting Stars, I Have a Dream, Nocturne): se reutiliza la
  ficha musical (tonalidad, compás, reparto de manos) y se escribe andamio
  **nuevo**, propio de Mercè, para que no coincida con el de nadie más.
- **10 piezas son propias** y hay que transcribirlas desde cero (tabla de
  arriba).
- La clase de hora y media es la más larga del proyecto: eso no sube el nivel
  de las hojas generadas, pero sí permite que la hoja "cómo se estudia" tenga
  **dos páginas cuando la pieza lo pide** (el mismo margen que José María,
  Josep y Luisa niega por norma propia de "poquito pero bien" — a Mercè no le
  aplica esa restricción).

## Lo que NO está medido, y por qué se dice

Ninguna pieza está transcrita nota a nota más allá de lo indicado en la
tabla. Todo el material generado va etiquetado como **andamio** y remite a la
partitura de Mercè para las notas exactas — la regla de siempre.
