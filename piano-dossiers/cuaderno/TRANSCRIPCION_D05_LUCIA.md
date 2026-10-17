# Lucía (Joan Manuel Serrat) — transcripción verificada

Fuente: edición de MuseScore. Método: `score_reader` a 200 dpi (36 compases,
3 páginas) + lectura visual de la página 1.

## Datos globales (verificados)

| | |
|---|---|
| Tonalidad | **La menor** (sin armadura; los cifrados lo confirman: Am, Dm, E7) |
| Compás | **4/4** |
| Tempo | **♩ = 75** |
| Compases | **36** |
| Mano izquierda | **Acordes en bloque, cuatro negras por compás.** Tres o cuatro sonidos cada uno. |
| Mano derecha | Melodía con **anacrusa** y **tresillos** marcados con un 3. |
| Extras | Cifrados impresos entre los dos pentagramas. Barra de repetición en el c. 6. |

## Los cifrados impresos, y lo que esconden

```
Am/E · Dm/F · E7 · Am/E · F · G/F · C/E · B°/F · E7
```

**Casi todos llevan barra.** Y si se miran solo los bajos:

| cifrado | bajo |
|---|---|
| Am/E | **Mi** |
| Dm/F | **Fa** |
| E7 | **Mi** |
| Am/E | **Mi** |
| F | **Fa** |
| G/F | **Fa** |
| C/E | **Mi** |
| B°/F | **Fa** |
| E7 | **Mi** |

El bajo hace **Mi–Fa–Mi–Fa**: un semitono que va y viene mientras los acordes
cambian por encima. Esa oscilación es la firma armónica de la canción.

## Los acordes medidos (lector), que coinciden con el cifrado

| compás | cifrado | notas medidas |
|---|---|---|
| 4 (y 7, idéntico) | **Am/E** | Mi3 · La3 · Do4 |
| 5 | **Dm/F** | Fa3 · La3 · Re4 |

`repeticiones()` confirma que los cc. 4 y 7 son idénticos nota por nota.

## Lo que NO está verificado

- La melodía nota a nota: lleva tresillos y semicorcheas, y el lector no
  distingue duraciones. En el cuaderno no se cita ninguna nota de la derecha.
- Los acordes a partir del c. 9 (F, G/F, C/E, B°/F): se citan **por su
  cifrado impreso y por su bajo**, que es lo que la edición afirma, pero no
  se escribe su disposición exacta porque no está medida.
