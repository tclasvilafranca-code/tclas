# Álbum de Arnau — iniciación · 20 piezas · formato corto

Arnau tiene unos 10 años y clase de **media hora**. Eso cambia dos cosas de
raíz, y el cuaderno está construido alrededor de ellas:

1. **No hay tiempo de leer un dosier largo en clase.** Cada canción son
   **cinco hojas**, no ocho.
2. **Casi todo el trabajo pasa en casa.** Por eso dos de las cinco hojas son
   **deberes escritos de verdad** (una por semana), no un recuadro en blanco
   para que el profesor apunte algo.

Y una norma que manda sobre la redacción entera: **sin tecnicismos**. Nada de
"anacrusa", "armadura", "subdivisión" ni "ligadura de prolongación". Se dice
*"entrar antes de que empiece el compás"*, *"la tecla negra que vale para toda
la canción"*, *"contar en dos"* y *"notas que se atan"*.

## De dónde salen las partituras

Carpeta de Drive de Arnau, bajada con `gdown --folder` y verificada una a una
por el **título impreso dentro del PDF**, no por el nombre del archivo. Las
ediciones son de tres sitios distintos y se nota en lo que imprimen:

| origen | qué imprime | qué se puede citar |
|---|---|---|
| Musescore (Pantera Rosa, Puff…) | marca de agua, título, tempo | tempo declarado |
| free-scores.com (Pratley: Aloha, los dos dúos) | autor, país, tempo | tempo y carácter |
| mfiles.co.uk (Paterson: Wheels, Polly, Muffet, Baa Baa) | letra encima del pentagrama | letra y digitación |

Cuando una edición **no imprime metrónomo**, la casilla de la ficha se llama
**"Carácter"** y se copia lo que sí pone (*Silly!*, *Lively*, *Brightly*,
*Slowly*, *Con moto*, *Allegretto*, *Allegro*) — no se le atribuye a la edición
un tempo que no trae.

Ninguna pieza de Arnau coincide con las de Dilan ni con las de Eva, así que
aquí no hay problema de fotocopia entre alumnos. Se comprobó igualmente:
**0 sistemas compartidos** de 8 eventos o más contra los 37 dosieres de los
otros dos álbumes, y **0 sistemas repetidos** entre las 20 canciones de Arnau.

## Las cinco hojas, y por qué son esas cinco

| hoja | qué es | módulo |
|---|---|---|
| — | la partitura original (1 o 2 páginas) | el PDF fuente, sin tocar |
| 1 | **Ficha de la partitura** — cinco datos y qué trae de nuevo | `ficha_info.py` |
| 2 | **Taller** — calentamiento de dedos + leer en voz alta, en una sola hoja | `hoja_taller.py` |
| 3 | **Cómo se aprende** — tres pasos al piano, con el material medido | `hoja_piano.py` |
| 4 | **Deberes · semana 1** — escritos, para hacer en casa | `hoja_deberes.py` |
| 5 | **Deberes · semana 2** — escritos, para hacer en casa | `hoja_deberes.py` |

El **taller** es la fusión de dos hojas del formato largo (calentamiento y
agudeza visual) en una: en media hora no caben las dos, y lo que se pierde al
juntarlas es menos que lo que se pierde si no se llega a hacer ninguna.

Los **deberes** se componen de bloques (`hoja_deberes.TIPOS`), y hay **21 tipos
distintos**:

| grupo | tipos |
|---|---|
| leer y escribir notas | `nombres` `dibuja` `figuras` `colorea` `rodea` `cuenta` `diferencias` |
| jugar | `sopa` `adivina` `crucigrama` `camino` `vf` `ordena` `palmas` |
| manos y teclado | `teclado` `inventa` `escribe` `une` |
| de casa | `rutina` `escucha` `nota` |

Cada hoja lleva cinco o seis bloques, y **qué bloques lleva cada semana está
decidido en `cuaderno/arnau_recetas.py`**: 20 recetas, cada una usada dos veces
en las 40 hojas y siempre con 10 hojas de distancia como mínimo. Así Arnau no
se encuentra nunca la misma forma de hoja dos semanas seguidas ni parecido.

Es la **norma de variedad** del cliente, y la comprueban dos auditores
distintos: `auditar_variedad.py` mira que el reparto cumpla la norma (dos
semanas seguidas no repiten esqueleto, cada hoja trae al menos dos tipos
nuevos, ningún tipo pasa del 60 % de las hojas) y `arnau_recetas.revisar_reparto`
mira que cada hoja cumpla el reparto.

Los números de ejercicio los pone `build_deberes` solo: con la variedad el
orden cambia cada semana y renumerarlos a mano era una fuente de fallos.

## El orden: de menos a más difícil

Criterio del cliente. La dificultad se mide por **cuántas cosas distintas tiene
que hacer a la vez**, no por la velocidad ni por el número de notas. Los dos
villancicos quedan repartidos por dificultad; el **plan de curso** ya se
encarga de adelantarlos a diciembre.

### 1 · Las dos manos, y la primera melodía
Empezar a tocar y a leer al mismo tiempo.

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 1 | Chopsticks | Do · 3/4 | un solo dedo por mano (el 2), y las manos se separan |
| 2 | Clementine | Do · 3/4 | la primera melodía de verdad: la derecha va sola |
| 3 | Jolly Old Saint Nicholas | Do · 4/4 | una mano se mueve y la otra aguanta dos notas largas |

### 2 · Los huecos, y la primera tecla negra
Contar lo que no suena, y mirar lo que hay al principio del pentagrama.

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 4 | Do Your Ears Hang Low? | Do · 4/4 | las dos manos se mueven, y aparecen los silencios |
| 5 | The Wheels on the Bus | Fa · 3/4 | la primera tecla negra: el Si bemol vale para toda la canción |
| 6 | Oh, When the Saints | Do · 4/4 | entrar antes de que empiece el compás |
| 7 | We Wish You a Merry Christmas | Do · 3/4 | las dos manos, con los dedos escritos en el papel |

### 3 · Leer más cosas a la vez
Cuando en el papel pasan dos cosas al mismo tiempo.

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 8 | Baa Baa Black Sheep | Do · 4/4 | una sola mano tocando dos notas a la vez |
| 9 | Polly Put the Kettle On | Fa · 2/4 | dos notas en cada golpe: un-y-dos-y |
| 10 | Little Miss Muffet | Fa · 6/8 | seis notas por compás, contadas en dos |
| 11 | Eso que tú me das | Do · 4/4 | una hoja de melodía con los acordes encima y la letra debajo |

### 4 · Acordes, saltos y puntillos
La mano se abre, viaja, y las notas cambian de duración.

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 12 | Puff the Magic Dragon | Do · 4/4 | acordes de tres notas a la vez, uno por compás |
| 13 | La Pantera Rosa | Do · 4/4 | teclas negras que aparecen de repente, y empieza con silencio |
| 14 | My Bonnie Lies Over the Ocean | Do · 3/4 | la mano cambia de sitio, y luego se cruzan |
| 15 | Largo · Sinfonía del Nuevo Mundo | Do · 4/4 | el puntillo, y las notas que se atan |
| 16 | Aloha Oe | Do · ¢ | saltos grandes, y por primera vez dos páginas |

### 5 · Deprisa, y tocando con otra persona
Lo último no es difícil de dedos: es coordinarse.

| nº | pieza | ton. · compás | por qué aquí |
|---|---|---|---|
| 17 | Popeye el marinerito | Sol · 3/4 | un sostenido al principio, y empieza con silencio |
| 18 | El submarino amarillo | Sol · 4/4 | Allegro: subir la velocidad con cabeza, sobre un molde que se repite |
| 19 | Rain Rain Go Away | Do · 4/4 | a cuatro manos: empezar los dos a la vez |
| 20 | The Mulberry Bush | Do · 4/4 | a cuatro manos: no pararse si te pierdes |

## El plan de curso

44 semanas, dos por pieza (la primera para leerla, la segunda para tocarla
entera), y **una hoja de deberes por semana** — de ahí que cada canción lleve
dos. Fechas que mandan sobre el reparto:

- **Halloween (semana 8)** → 13 · La Pantera Rosa, que es la pieza misteriosa
  del cuaderno. Esa semana solo se lee y se prueba; entera se estudia en su
  sitio, en marzo.
- **Navidad (semanas 15 y 16)** → 3 · Jolly Old Saint Nicholas y 7 · We Wish
  You a Merry Christmas.
- **Semanas 12, 21 y 30** → repaso, para no perder lo de atrás.
- **Semanas 42–44** → elegir programa, ensayo general y concierto.

## Verificación pasada antes de entregar

- `python3 cuaderno/auditar_arnau.py` → **TODO OK** en las 20 canciones
  (compases, margen derecho, material repetido entre hojas, altura final de
  cada hoja, y texto que no cabe en su caja) **más la variedad**: 40 hojas, 20
  esqueletos distintos, 21 tipos, y el reparto cumplido hoja por hoja.
- **Altura final de las 100 hojas generadas**: todas entre 44 y 132 (la más
  baja 44, la más alta 127,1).
- **Portada, índice y plan**: 0 desbordes de texto, 0 cajas desbordadas.
- **Píxeles del álbum montado** (128 páginas a 110 dpi): de las 102 hojas
  nuestras, **0 desbordes por abajo y 0 por la derecha**. Las 6 páginas que
  pisan el margen derecho son las **partituras originales**, cuyos márgenes no
  son nuestros.
- **Cruce entre alumnos** (`cruzar_arnau.py`): 0 coincidencias contra Dilan y
  Eva, 0 repeticiones entre las canciones de Arnau.

## Salida

`output/Arnau_Cuaderno_del_Pianista_2026.pdf` · **128 páginas**
(portada + índice + plan de curso + 20 dosieres).
