# Chopsticks (arr. Gilbert DeBenedetti) — transcripción verificada

Método: render del PDF original a 150 dpi, detección de las 5 líneas de cada
pentagrama, medición de la posición vertical de cada cabeza de nota respecto a
esas líneas, y comprobación visual a zoom ×7-9 de todos los compases dudosos.

Escritura: **las dos manos en clave de Sol sobre UN solo pentagrama**. La nota
de abajo es la mano izquierda, la de arriba la derecha. Indicación impresa:
*"Only use finger 2, both hands. These are your chopsticks."*
Do mayor, 3/4, 32 compases, sin matices escritos.

## Parte A (cc. 1–16) — todo negras, tres por compás

| compás | mano izq. | mano der. | intervalo |
|---|---|---|---|
| 1–2   | Fa4 | Sol4 | 2ª |
| 3–4   | Mi4 | Sol4 | 3ª |
| 5–6   | Re4 | Si4  | 6ª |
| 7     | Do4 | Do5  | 8ª |
| 8¹    | Do4 | Do5  | 8ª |
| 8²    | Re4 | Si4  | 6ª |
| 8³    | Mi4 | La4  | 4ª |
| 9–10  | Fa4 | Sol4 | 2ª |
| 11–12 | Mi4 | Sol4 | 3ª |
| 13–14 | Re4 | Si4  | 6ª |
| 15¹   | Do4 | Do5  | 8ª |
| 15²   | —   | —    | silencio de negra en las dos manos |
| 15³   | Fa4 | Sol4 | 2ª |
| 16¹   | Mi4 | Do5  | 6ª |
| 16²   | —   | —    | silencio |
| 16³   | Do5 | Mi5  | 3ª (arranque de la parte B) |

**El movimiento es contrario y por grados.** La izquierda baja Fa-Mi-Re-Do y la
derecha sube Sol-Si-Do; al volver, la izquierda sube Do-Re-Mi-Fa mientras la
derecha baja Do-Si-La-Sol. En los cc. 1–4 la derecha NO se mueve (siempre Sol):
solo anda la izquierda.

## Parte B (cc. 17–32) — blanca + negra, las dos manos en terceras paralelas

| compás | contenido |
|---|---|
| 17 | Si4+Re5 (blanca) · La4+Do5 (negra) |
| 18 | Sol4+Si4 (blanca) · Fa4+La4 (negra) |
| 19 | Mi4+Sol4 (blanca) · Mi4+Sol4 (negra) |
| 20 | Mi4+Sol4 · Fa4+La4 · Mi4+Sol4 (tres negras) |
| 21 | Re4+Fa4 (blanca) · Re4+Fa4 (negra) |
| 22 | Re4+Fa4 · Mi4+Sol4 · Re4+Fa4 (tres negras) |
| 23 | Do4+Mi4 (blanca) · Fa4+La4 (negra) |
| 24 | Mi4+Sol4 (negra) · silencio · Do5+Mi5 (negra) |
| 25–28 | igual que 17–20 |
| 29–30 | igual que 21–22 |
| 31 | Do4+Do5 (negra) · silencio · Fa4+Sol4 (negra) |
| 32 | Mi4+Do5 (negra) · silencio · silencio ‖ |

Los cc. 24 y 32 son el mismo gesto con final distinto: el 24 acaba en Do5+Mi5 y
relanza la parte B, el 32 acaba en silencio y cierra la pieza.

## Corrección respecto a lo entregado antes

En la ficha de la partitura y en la hoja de calentamiento se dijo que la apertura
era **2ª → 3ª → 5ª (Mi–Si) en los cc. 5–8**. Es incorrecto: los cc. 5–6 son una
**6ª (Re–Si)** y los cc. 7–8 una **8ª (Do–Do)**. La 5ª no aparece en toda la
pieza. Corregido en `build_ficha_01.py` y en `build_calentamiento_01.py`.
