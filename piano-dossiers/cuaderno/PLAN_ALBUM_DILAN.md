# Álbum de Dilan — plan y estado

Nivel: **avanzado**. Estructura fija de 6 páginas por canción
(partitura · ficha · calentamiento · agudeza · al piano ×2).

## Flujo por canción (no saltarse ningún paso)

1. `score_reader.leer()` sobre el PDF → nº de compases, mano izquierda,
   `repeticiones()` para la forma.
2. **Mirar la página 1 a zoom**: armadura, compás, tempo, cifrados impresos,
   disposición de las manos, dinámicas. El lector no lee nada de eso.
3. Verificar a zoom **cada pasaje que se vaya a imprimir**. Lo que no se
   mida, no se cita: ni tonalidad, ni total de compases, ni acordes.
4. Escribir `TRANSCRIPCION_D<nn>_<TITULO>.md` con lo medido **y una sección
   "Lo que NO está verificado"**.
5. Escribir `dilan_<nn>_<slug>.py` con el diccionario `CANCION` y llamar a
   `cancion.construir()`.
6. `cancion.auditar()` tiene que salir OK: compases, margen derecho,
   duplicados entre hojas y altura de página.

## Reglas que no se negocian

- **Calentamiento DERIVA, al piano CITA.** Si lleva número de compás va en
  "al piano"; si está transportado o ampliado va en el calentamiento. Nada
  en las dos hojas. Lo comprueba `audit_duplicados`.
- Nunca afirmar un dato musical sin medirlo. Ha fallado dos veces (la 5ª de
  Chopsticks, la reexposición de El Cisne) y las dos se detectaron tarde.
- Si el nº de compases no es fiable, **se omite el mapa de la pieza**.

## Orden del álbum

| nº | canción | estado |
|---|---|---|
| 1 | Can't Help Falling in Love | ✅ hecha |
| 2 | Your Song | ✅ hecha |
| 3 | Thinking Out Loud | ✅ hecha |
| 4 | When I Was Your Man | |
| 5 | Lucía | |
| 6 | Poema de Amor | |
| 7 | Amiga Mía | |
| 8 | La Promesa | |
| 9 | Al Calor del Amor en un Bar | |
| 10 | Soldadito de Hierro | |
| 11 | A Sky Full of Stars | |
| 12 | What Was I Made For | |
| 13 | Writing's on the Wall | |
| 14 | My Favourite Things | |
| 15 | El Cisne | ✅ hecha |
| 16 | Adagio en Sol menor (Albinoni) | |
| 17 | Arabesque (Burgmüller, 4 manos) | |
| 18 | Have Yourself a Merry Little Christmas | |
| 19 | Santa Tell Me | |
| 20 | It's Beginning to Look a Lot Like Christmas (4 manos) | |

Al terminar: renumerar los kickers, generar portada + índice con
`cuaderno/portada.py` y unir el álbum completo.

## Avisos por partitura

- Las de **4 manos** (17, 20) llevan cuatro pentagramas por sistema: el
  emparejado por defecto de `sistemas()` no vale, hay que tratarlas aparte.
- Las ediciones de MuseScore con letra traen **cifrados impresos**: son
  armonía dada por el editor y valen más que cualquier análisis propio.
- Las cabezas huecas no las ve el lector: en piezas de melodía en notas
  largas, la línea de la derecha se lee a zoom.
