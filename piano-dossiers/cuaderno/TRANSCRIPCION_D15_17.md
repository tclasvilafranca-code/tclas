# My Favourite Things · Adagio de Albinoni · Arabesque (4 manos)

---

## 15 · My Favourite Things (Rodgers y Hammerstein, arr. Kaitlin)

| | |
|---|---|
| Tonalidad | **Sol mayor** · la pieza se mueve en **Mi menor** casi todo el rato |
| Compás | **3/4** · **♩=160** |
| Extras | **cifrados impresos**: Em, C, Am, D, G, B |

Es un **vals rápido**. La izquierda hace el vals clásico: la fundamental y
después el acorde, tres notas por compás.

**Los acordes medidos de la izquierda**:

| cifrado | notas medidas |
|---|---|
| Em | Mi3 · Sol3 · Si3 |
| C | Do3 · Mi3 · Sol3 |
| D | Re3 · Fa♯3 · La3 |
| Em (grave) | Si2 · Mi3 · Sol3 |

Hay **casillas 1.ª y 2.ª** hacia el c. 38 y una **barra de repetición** en el
c. 15.

**Lo que NO está verificado**: el total exacto de compases (los números
impresos van 14, 27, 40, 52, así que rondan los 55, pero el recuento del
lector da 46 y no coinciden), ni el ritmo de la melodía.

---

## 16 · Adagio en Sol menor (Albinoni, arr. A. C. Escobés)

| | |
|---|---|
| Tonalidad | **Sol menor** (dos bemoles) |
| Compás | **3/4** · **Adagio** · dinámica **p** |

**El hallazgo de esta pieza**: la mano izquierda hace en todos los compases
el mismo gesto de **tres negras — fundamental · octava · fundamental** —, y
las notas graves dibujan el bajo descendente que es la identidad del Adagio:

> **Sol · Fa · Mi♭ · Re · Do · Re · Sol** — y después
> **Sol · La · Si♭ · Si♭ · Do · La · Si♭ · La · Do**

Medido compás a compás en quince compases seguidos, sin una sola excepción.

**Lo que NO está verificado**

- El ritmo de la mano derecha: lleva puntillos, fusas y tresillos, y el
  motor no escribe fusas.
- Las alteraciones accidentales. Hay Fa♯ escritos a mano (la sensible de Sol
  menor) y algún Mi♮, y el lector no los ve.
- El total de compases: la página tiene 28, pero la pieza puede seguir.

---

## 17 · Arabesque (Burgmüller op. 100 nº 2, arr. a cuatro manos por MB)

| | |
|---|---|
| Tonalidad | **La menor** (sin armadura) |
| Compás | **2/4** · **Allegro scherzando** |
| Formato | **cuatro manos**: cuatro pentagramas por sistema |

Esta partitura se lee con `arab.py`, no con `sistemas()`: hay que agrupar
los pentagramas de cuatro en cuatro, porque el emparejado normal los junta
de dos en dos y mezcla al Primo con el Secondo.

**Primo** (los dos pentagramas de arriba, los dos en clave de sol): las dos
manos tocan **lo mismo**, unas veces en octava y otras al unísono. Medido:

| compases | qué hace |
|---|---|
| 3, 9, 31 | `La · Si · Do · Si · La` — la célula que da nombre a la pieza |
| 4, 25, 30 | `Re · Mi · Fa · Sol · La` — la escala que sube |
| 5, 11 | `La · Si · Do · Do · Do` |
| 33 | escala entera bajando: `Mi · Re · Do · Si · La` |

**Secondo** (los dos de abajo): acordes staccato repetidos dos veces por
compás, y octavas en el bajo. Medido: `La·Do·Mi` (Am), `La·Re·Fa` (Re menor),
`Do·Mi·Sol` (Do), `Si·Fa·Sol` (la dominante). El bajo va en octavas: La2–La3.

**Los cc. 1 y 2 los toca solo el Secondo**: el Primo entra en el c. 3. Y en
el c. 5 hay un **8va** sobre el Primo.

**Lo que NO está verificado**: el ritmo exacto (semicorcheas con silencio de
semicorchea y notas picadas) y el total de compases de las cuatro páginas.
