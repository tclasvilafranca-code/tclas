# Josep — las 19 partituras, comprobadas una a una

Bajadas de su carpeta de Drive con `gdown --folder` el 17 de agosto de 2026.
De cada una se ha comprobado **el título impreso dentro del archivo** (no el
nombre del archivo), el número de páginas, la armadura, el compás y el tempo o
carácter impreso. Lo que no está en esta tabla no está medido, y por lo tanto
no se escribe en ninguna hoja.

## Avisos sobre los archivos

- **Los 19 son PDF de verdad.** Cuatro vienen sin extensión (`-PEACHES.`,
  `A COMME AMOUR _ Richard Clayderman.`, `Petite chanson.(4 MANOS)`,
  `cant-help-falling-in-love-elvis-presley.`) y se abren igual.
- **Ocho son el MISMO archivo que tiene José María**, byte a byte (comprobado
  con `md5sum`): Romance de Diabelli, Peaches, Counting Stars, Deck the Halls,
  Jailhouse Rock, Can't Help Falling in Love, Rasputin y A comme amour. Las
  citas literales de esas piezas pueden coincidir entre los dos cuadernos —eso
  es la partitura, y es la misma—, pero **el material inventado no puede**. Lo
  comprueba `cruzar_josep.py`.
- Las carpetas vacías que quedaban en el repositorio de una lista antigua de
  Josep (Boig per tu, Kiss the Rain, Nuovo Cinema Paradiso, Y si fuera ella,
  Your Song, Bob Esponja, Despacito, Bohemian Rhapsody…) **ya no están en su
  Drive**. El álbum se monta con lo que hay hoy en la carpeta.

## La tabla

| # | pieza | edición | ton. | compás | tempo/carácter impreso | págs |
|---|---|---|---|---|---|---|
| 1 | Romance, op. 163 nº 1, mvt. 2 | Diabelli · **Primo a 4 manos** | Do (nada) | ¢ | Andantino | 2 |
| 2 | Petite Chanson | Riccardo Collu · **a 4 manos** | Do (nada) | 4/4 | ♩ = 80 andante | 2 |
| 3 | Peaches (Super Mario Bros. Movie) · Jack Black | — | Do (nada) | 4/4 | — | 2 |
| 4 | Counting Stars · OneRepublic | arr. Becky Messer · **Easy Version** | Do (nada) | 4/4 | — | 2 |
| 5 | What Was I Made For? · Billie Eilish | Musescore · con cifrado y letra | Do (nada) | 4/4 | ♩ = 78 | 2 |
| 6 | Heart and Soul · Hoagy Carmichael | **Easy Piano Version** · guestinpiano.fr | Do (nada) | 4/4 | ♩ = 110 **Swing** | 1 |
| 7 | Hit the Road Jack | Musescore · sin arreglista impreso | Fa (1♭) | 4/4 | — | 1 |
| 8 | Deck the Halls | arr. Jim Paterson · mfiles.co.uk | Fa (1♭) | 4/4 | — | 1 |
| 9 | Jailhouse Rock · Elvis Presley | arr. Sadie King · Musescore | Do (nada) | 4/4 | ♩ = 150 **Swing** | 1 |
| 10 | Bella Ciao | **a 4 manos** (*4 mains*) | Sol menor (2♭) | 4/4 | — | 1 |
| 11 | Can't Help Falling in Love · Elvis Presley | arr. Seb Alejandro · Musescore | Re (2♯) | 3/4 | — | 2 |
| 12 | Lovely · Billie Eilish con Khalid | arr. Amy Kieran | Mi menor (1♯) | 4/4 | ♩ = 115 | 2 |
| 13 | Rasputin · Boney M | Musescore · **Easy piano** | Si menor (2♯) | 4/4 | ♩ = 124 | 2 |
| 14 | It's Beginning to Look a Lot Like Christmas | **Piano Duet** · arr. Rachel Chytelman | Do (nada) | **6/8** | — | 2 |
| 15 | My Favourite Things (*The Sound of Music*) | Rodgers y Hammerstein · arr. Kaitlin | Sol (1♯) | 3/4 | ♩ = 160 | 1 |
| 16 | Sweet Child O' Mine · Guns N' Roses | arr. Sadie King · **easy piano** | Sib (2♭) | 4/4 | — | 1 |
| 17 | Un Beso y una Flor · Nino Bravo | Musicaymaestro.com | Fa (1♭) | ¢ (C) | Allegro | 2 |
| 18 | Merry Go Round of Life · Joe Hisaishi | *for Piano Solo* | Sib (2♭) | 3/4 | ♩ = 120 → **♩ = 152** | 2 |
| 19 | A comme amour · Richard Clayderman | musicaparadisfrutar.com | Mi menor (1♯) → La menor | 4/4 | ♩ = 69 | 1 |

### Cómo se comprobaron las armaduras y los compases

Render a 250–300 dpi del comienzo de cada pieza y lectura a zoom del hueco
entre la clave y la primera nota. **No es una formalidad**: a 105 dpi leí mal
dos de ellas y las dos se corrigieron al ampliar.

- **Bella Ciao** parecía 3/4 y es **4/4**.
- **Hit the Road Jack** parecía empezar sin armadura y cambiar a un bemol en el
  compás 7; el bemol **está desde el compás 1**.

## Lo que trae cada pieza, medido

Esto es lo que decide el orden del álbum, y sale de mirar la partitura, no de
lo conocida que sea la canción.

| # | lo que la hace estar donde está |
|---|---|
| 1 | Primo de cuatro manos: **posición fija de cinco dedos** y las dos manos al unísono; la edición lo dice en el subtítulo |
| 2 | Primo de cuatro manos con **las dos manos en clave de sol**; negras y blancas, y un salto de octava en el primer compás |
| 3 | izquierda en **redondas** todo el rato; la derecha se repite |
| 4 | izquierda en redondas y **digitación impresa** nota a nota |
| 5 | notas fáciles y **entradas a contratiempo**: la mitad de los compases empiezan con silencio |
| 6 | primer **swing** del cuaderno, y la izquierda pasa de blancas a **bajo + acorde** |
| 7 | primer bemol, y **acordes en bloque** en la mano derecha |
| 8 | un bemol y **dobles notas** (dos teclas a la vez) en la derecha, compás tras compás |
| 9 | swing otra vez, pero a **♩ = 150**, y empieza con casi un compás de silencio |
| 10 | primer **tono menor**, a cuatro manos, con el Fa sostenido escrito nota a nota |
| 11 | dos sostenidos, **3/4**, y la izquierda ya no descansa |
| 12 | **corcheas seguidas de principio a fin** en la derecha: resistencia, no dificultad |
| 13 | dos sostenidos y ♩ = 124 con letra debajo |
| 14 | **6/8**: la única pieza del cuaderno que no se cuenta en dos o en cuatro |
| 15 | ♩ = 160 y **55 compases** en una sola página; cifrado impreso encima |
| 16 | el riff en corcheas continuas y el **pedal marcado** en la partitura |
| 17 | **semicorcheas** desde el primer compás, Allegro, y tresillos al final |
| 18 | terceras en corcheas, **dos tempos** (120 y 152) y 45 compases |
| 19 | semicorcheas de principio a fin **y cambio de armadura** en el compás 10 |

## Lo medido nota a nota

Método: render a 300 dpi, detección de las cinco líneas del pentagrama por
densidad de tinta, borrado de las líneas y medición del centro de cada cabeza
de nota contra ellas (`cabezas.py`). Solo se apunta aquí lo que ha salido
limpio y coherente consigo mismo; el resto de cada pieza va como **andamio** en
las hojas, y remite a la partitura del alumno.

### 6 · Heart and Soul — los dos primeros compases, medidos

Pentagrama de sol, líneas medidas en y = 530,5 · 551,5 · 572,5 · 593,5 · 614,5
(300 dpi), medio espacio = 10,5 px.

```
c. 1   Do · Do · Do          (negra · negra · blanca)   — todo do central
c. 2   (silencio de corchea) Do · Si · La · Si · Do · Re
```

Alturas medidas, en índices de medio espacio desde la línea superior:
9,90 · 9,90 · 10,15 | 9,90 · 10,64 · 11,90 · 10,65 · 9,89 · 8,97. Un índice de
10,0 es el do central; los tres primeros dan 9,90 tres veces seguidas, así que
la lectura es firme. La última nota del c. 2 (el Re) va sin barra: es más larga
que las anteriores.

### 2 · Petite Chanson — la anacrusa y el primer compás, medidos

Primo, mano derecha. Líneas en y = 472 · 492,5 · 513,5 · 534,5 · 555,5.

```
anacrusa   Mi · Fa                    (dos corcheas)
c. 1       Sol · Sol · Sol            (tres negras)
```

El primer Sol es el de la segunda línea; **el segundo está una octava más
arriba** (índices medidos 7,87 y 0,90: siete grados justos). Ese salto de
octava en el primer compás es lo que se trabaja en su hoja de dedos. Las dos
corcheas que cierran el compás quedan por encima del pentagrama con líneas
adicionales y no se dan por medidas: van como andamio.

### 9 · Jailhouse Rock — el compás 12, medido (y una corrección)

Pentagrama de fa, líneas medidas en y = 1244 · 1258 · 1272 · 1285,5 · 1299
(200 dpi).

```
c. 12   Fa · La · Do · Re      (cuatro negras, ASCENDENTES)
        índices medidos: 1,96 · -0,06 · -2,08 · -2,78
        digitación impresa debajo: 5 · 3 · 2 · 1
```

Esta medición corrigió un error que ya estaba impreso en el cuaderno de José
María, que tiene la misma partitura: allí se decía que la izquierda **bajaba**.
En la mano izquierda el 5 es el meñique y el 1 el pulgar, así que 5 · 3 · 2 · 1
solo puede subir. Corregido en los dos cuadernos.

## Lo que NO está medido, y por qué se dice

Las otras 17 piezas no están transcritas nota a nota. Todo el material generado
para ellas —calentamientos, ejercicios de lectura, ejemplos de las fichas— sale
etiquetado como **andamio**: conserva el dibujo, el compás y la tonalidad
medidos de la pieza, y la hoja remite al alumno a su propia partitura para las
notas exactas. Es la regla del proyecto, y es preferible a inventar un compás
concreto y equivocarse.
