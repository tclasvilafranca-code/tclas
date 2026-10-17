# José María — las 19 partituras, comprobadas una a una

Bajadas de su carpeta de Drive con `gdown --folder` el 17 de agosto de 2026.
De cada una se ha comprobado **el título impreso dentro del archivo** (no el
nombre del archivo), el número de páginas, la armadura, el compás y el tempo o
carácter impreso. Lo que no está en esta tabla no está medido, y por lo tanto
no se escribe en ninguna hoja.

## Aviso sobre los archivos

- **`ADAGIO.` no es un PDF: es un JPEG** (736 × 1041). Para montarlo en el
  álbum hay que convertirlo a PDF.
- Cuatro archivos vienen **sin extensión** (`SHALLOW.`, `Trouble.`,
  `-PEACHES.`, `Toreador. Bizet`…). Son PDF válidos; solo les falta el `.pdf`.
- Dos de los que había en la carpeta antes (Jingle Bells y Leise rieselt) **ya
  no están**, y en su lugar hay dos nuevos (Adagio y Flying Theme). El álbum se
  monta con lo que hay hoy en la carpeta.

## La tabla

| # | pieza | edición | ton. | compás | tempo/carácter impreso | págs |
|---|---|---|---|---|---|---|
| 1 | Romance, op. 163 nº 1, mvt. 2 | Diabelli · free-scores · **Primo a 4 manos** | Do (nada) | ¢ | Andantino | 2 |
| 2 | America (My Country, 'Tis of Thee) | arr. Gilbert DeBenedetti · Level Two | Do (nada) | 3/4 | With Reverence | 1 |
| 3 | The Star-Spangled Banner | arr. Gilbert DeBenedetti · Level 2 | Do (nada) | 3/4 | With pride | 2 |
| 4 | Counting Stars · OneRepublic | arr. Becky Messer · **Easy Version** | Do (nada) | 4/4 | — | 2 |
| 5 | Peaches (Super Mario Bros. Movie) · Jack Black | — | Do (nada) | 4/4 | — | 2 |
| 6 | Someone You Loved · Lewis Capaldi | Campamento Bye Bye Beethoven | Do (nada) | 4/4 | — | 3 |
| 7 | Deck the Halls | arr. Jim Paterson · mfiles.co.uk | Fa (1♭) | 4/4 | — | 1 |
| 8 | Jailhouse Rock · Elvis Presley | arr. Sadie King · Musescore | Do (nada) | 4/4 | ♩ = 150 Swing | 1 |
| 9 | My Grandfather's Clock · H. C. Work | arr. Gilbert DeBenedetti · Level Three | Sol (1♯) | C | With precision | 2 |
| 10 | Shallow · Lady Gaga y Bradley Cooper | Campamento Bye Bye Beethoven | Sol (1♯) | 4/4 | ♩ = 96 | 3 |
| 11 | Can't Help Falling in Love · Elvis Presley | arr. Seb Alejandro · Musescore | Re (2♯) | 3/4 | — | 2 |
| 12 | Carol of the Bells · Leontovych | arr. Jim Paterson · mfiles.co.uk | Sol menor (2♭) | 3/4 | — | 1 |
| 13 | Adagio · Albinoni | arr. A. L. Christopherson · music-scores.com | sin armadura | 3/4 | Adagio ♩ = 60 | 1 (JPEG) |
| 14 | Rasputin · Boney M | Musescore · **Easy piano** | Si menor (2♯) | 4/4 | ♩ = 124 | 2 |
| 15 | Toreador, de *Carmen* · Bizet | arr. Gilbert DeBenedetti · **Level Four** | Fa (1♭) | C | March time | 1 |
| 16 | Trouble · Coldplay | arr. Unai Karam | Sol (1♯) | 4/4 | ♩ = 138 | 4 |
| 17 | A comme amour · Richard Clayderman | musicaparadisfrutar.com | Mi menor (1♯) | 4/4 | ♩ = 69 | 1 |
| 18 | Interstellar · Hans Zimmer | Campamento Bye Bye Beethoven | sin armadura | 3/4 | ♩ = 96 | 6 |
| 19 | Flying Theme (*Cómo entrenar a tu dragón*) | Perfect Harmony | Do → Re (2♯) | 4/4 | — | 3 |

## Corrección posterior a la entrega

**Jailhouse Rock, compás 12.** La primera versión de esta ficha decía que la
mano izquierda **bajaba** con los dedos 5 · 3 · 2 · 1. Es falso: **sube**. Se
detectó al preparar el cuaderno de Josep, que tiene esta misma partitura, y se
comprobó midiendo (render a 200 dpi, `cabezas.py`, contra las líneas del
pentagrama de fa):

```
c. 12   Fa · La · Do · Re      (cuatro negras, ascendentes)
        índices medidos: 1,96 · -0,06 · -2,08 · -2,78
```

En la digitación de la mano izquierda el 5 es el meñique y el 1 el pulgar, así
que una digitación 5 · 3 · 2 · 1 solo puede ir de grave a agudo. El error
estaba impreso en la ficha y en la hoja "cómo se estudia" de la pieza 8 de José
María; las dos están corregidas y el álbum, regenerado. **Si el álbum ya está
impreso en papel, hay que reimprimir esas dos hojas.**

## Lo medido nota a nota

Método: render a 150 dpi, detección de las cinco líneas del pentagrama, y
medición del centro de cada cabeza de nota contra ellas (`cabezas.py`). Solo se
apunta aquí lo que ha salido limpio; el resto de cada pieza va como **andamio**
en las hojas, y remite a la partitura.

### 2 · America — los cuatro primeros compases, medidos

```
c. 1   Do · Do · Re          (tres negras)
c. 2   Si · Do · Re          (negra con puntillo · corchea · negra)
c. 3   Mi · Mi · Fa          (tres negras)
c. 4   Mi · Re · Do          (negra con puntillo · corchea · negra)
```

Alturas medidas: C4 C4 D4 | B3 C4 D4 | E4 E4 F4 | E4 D4 C4. Coinciden con la
melodía conocida de *God Save the King* transportada a Do, así que la medición
está contrastada por dos caminos. La digitación viene impresa en las dos manos
(2 · 3 · 1 · 4 · 3 en la derecha; 3/5 · 1 · 2 · 5 en la izquierda).

### 1 · Romance (Diabelli) — lo que dice la edición

No se citan alturas: el Primo lleva **8va** sobre el pentagrama de arriba y la
detección de cabezas se ensucia con las ligaduras y el corchete de la octava.
Lo que sí está impreso, y es lo que de verdad importa aquí:

- *"Primo part for 5 fingers with stationary hand position"* — la mano **no se
  mueve de sitio** en toda la pieza. Es lo más fácil que hay para empezar.
- Las **dos manos del Primo tocan lo mismo**, en dos pentagramas de clave de
  sol, a distancia de octava.
- Compás partido (¢), *Andantino*, *p dolce*, *sempre legato*.
- Es a cuatro manos: el Secondo lo toca la profesora.

Sus ejercicios van rotulados como andamio en Do mayor y remiten a la partitura.
