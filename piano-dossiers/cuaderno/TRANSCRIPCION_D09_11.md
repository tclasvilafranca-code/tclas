# When I Was Your Man · Al Calor del Amor en un Bar · Soldadito de Hierro

Método: `engine/score_reader.py` a 200 dpi, `huecas.py` para las cabezas
huecas de la izquierda, y lectura visual a zoom de todo lo que se imprime.

---

## 9 · When I Was Your Man (Bruno Mars)

| | |
|---|---|
| Tonalidad | **Do mayor** (sin armadura; las alteraciones van escritas una a una) |
| Compás | **4/4** |
| Compases | el lector cuenta **45**; la edición no los numera, así que no se afirma un total |
| Mano izquierda | arpegios de tres notas en corcheas, alternando con notas largas |
| Mano derecha | melodía muy densa, en semicorcheas y con muchas ligaduras |

**Los acordes de la izquierda que el lector aísla limpios** (grupos de tres
notas seguidas en un mismo compás):

| notas medidas | acorde |
|---|---|
| Re3 · Fa3 · La3 | Re menor |
| Do3 · Mi3 · Sol3 | Do mayor |
| Fa3 · La3 · Do4 | Fa mayor |
| Sol2 · Si2 · Re3 | Sol mayor |
| Si2 · Re3 · Fa3 | la dominante, sin su fundamental |

Son los cinco acordes de Do mayor que usa la canción. El cuaderno los trabaja
como acordes, **sin citar números de compás**: la edición no los numera y la
detección de barras de esta partitura no es fiable del todo.

**Lo que NO está verificado**

- El total de compases y, por tanto, la forma.
- El ritmo de la mano derecha. Va en semicorcheas con ligaduras y silencios
  que el motor no sabe escribir.
- Las alteraciones accidentales del acorde de entrada (hay un ♯ y un ♮
  escritos a mano en el c. 1).

---

## 10 · Al Calor del Amor en un Bar (Gabinete Caligari)

| | |
|---|---|
| Tonalidad | **Mi menor** (armadura de un sostenido) |
| Compás | **C** = 4/4 · **Allegretto** |
| Extras | **cifrados impresos en español** y, además, **los nombres de las notas del bajo escritos debajo del pentagrama** |

**Lo que imprime la edición y por tanto es de fiar**

- Cifrados: `Mim · Fa♯7 · Si7 · Lam · Solm · Sol`.
- Nombres del bajo, escritos por el editor debajo de la clave de fa:
  `MI` · `FA♯ MI DO♯ FA♯` · `MI SOL SI` · `MI SOL SI DO♯ RE♯` ·
  `MI FA♯ SOL LA SI`.
- Hay **segno**, casillas **1.ª** y **2.ª**, y más adelante un **cambio de
  armadura a cuatro sostenidos**.

**El molde de la mano izquierda**, medido en cinco compases distintos:

| cifrado | notas medidas | patrón |
|---|---|---|
| Mim | Mi2 · Mi3 · Si2 · Mi3 | fundamental · 8ª · 5ª · 8ª |
| Fa♯7 | Fa♯2 · Fa♯3 · Do♯3 · Fa♯3 | igual, sobre Fa♯ |
| Lam | La2 · La3 · Mi3 · La3 | igual, sobre La |
| Sol | Sol2 · Sol3 · Si2 · Sol3 | igual, sobre Sol |

Es **el mismo molde que Poema de Amor**, pero en Mi menor y a otra velocidad.

**La mano derecha**, medida: la frase que más se repite es un descenso
`Do5 · Si4 · La4 · Sol4 · Fa♯4 · Mi4` — la escala de Mi menor bajando hasta
la tónica. Aparece dos veces (el lector la encuentra idéntica en dos sitios).
Y hay otra célula que sale **cinco veces**: `Do5 · La4 · La4 · Si4 · La4`.

**Lo que NO está verificado**

- **Los números de compás.** El recuento del lector no cuadra con los números
  impresos de la edición (el segno y las casillas le añaden barras), así que
  en el cuaderno **no se cita ni un número de compás**: se cita por cifrado,
  que es lo que la edición imprime y no admite duda.
- Qué pasa exactamente en el cambio de armadura a cuatro sostenidos. Se dice
  que existe y que hay que mirarlo, no lo que hace.
- El ritmo de los tresillos (marcados con un 3 en la mano derecha).

---

## 11 · Soldadito de Hierro (Nil Moliner, arr. Bye Bye Beethoven)

| | |
|---|---|
| Tonalidad | **Do mayor** (sin armadura) |
| Compás | **4/4** · **♩=84** · con **letra** |
| Compases | **30** impresos, más una anacrusa ("Me") |
| Mano izquierda | **una quinta vacía en redonda por compás**. Nada más. |
| Mano derecha | la melodía cantada, llena de **tresillos** |

**La mano izquierda, medida** (cabezas huecas, con `huecas.py`, y todas las
posiciones caen a menos de 0,15 de paso de una línea o un espacio, así que la
lectura es firme):

| compás impreso | notas | acorde |
|---|---|---|
| 1 | Do3 · Sol3 | Do |
| 2 | Re3 · La3 | Re menor (sin tercera) |
| 3 | Sol2 · Re3 | Sol |
| 4 | Do3 · Sol3 | Do |
| 5 | Fa2 · Do3 | Fa |
| 6 | Sol2 · Re3 | Sol |
| 7 | Fa2 · Do3 | Fa |

**Siempre dos notas y siempre a distancia de quinta: nunca hay tercera.** Por
eso el acompañamiento suena hueco y abierto, y por eso es tan fácil de tocar.

**La forma**: los **cc. 15–24 son literalmente los cc. 4–13**. Comprobado con
`repeticiones()` en siete parejas de compases idénticos seguidos. Media
canción está aprendida en cuanto se monta la primera mitad.

**Lo que NO está verificado**

- El ritmo de la mano derecha. Está lleno de tresillos y de silencios de
  semicorchea; se citan las alturas y se dice que el ritmo va simplificado.
- Los acordes de la izquierda a partir del c. 8, donde baja de registro y la
  medición se vuelve ruidosa. Se citan solo los siete primeros.
