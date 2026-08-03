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
   duplicados entre hojas y altura de página (por abajo **y por arriba**).
7. Chequeo de píxeles con `pdftoppm`, que es lo único que ve la ficha
   completa y las páginas de la partitura.

## Cuánto material lleva una hoja

Una hoja que acaba a media página está a medio hacer. El listón es el álbum
de Arnau, que llena el 97-99 % de las cinco hojas. `auditar()` lo comprueba:
la `y` final de cada hoja tiene que quedar **entre 44 y 132**.

- por debajo de 44 la hoja pisa el pie de página;
- por encima de 132 sobra papel y falta trabajo.

En la práctica eso son **6-7 ejercicios en el calentamiento** y **4-6 bloques
en cada hoja al piano**, contando las cajas de texto. Cuando no se puede
citar más música porque no está medida, el hueco se llena con cajas de texto
que expliquen algo real de la pieza, nunca con relleno.

## Reglas que no se negocian

- **Calentamiento DERIVA, al piano CITA.** Si lleva número de compás va en
  "al piano"; si está transportado o ampliado va en el calentamiento. Nada
  en las dos hojas. Lo comprueba `audit_duplicados`.
- Nunca afirmar un dato musical sin medirlo. Ha fallado dos veces (la 5ª de
  Chopsticks, la reexposición de El Cisne) y las dos se detectaron tarde.
- Si el nº de compases no es fiable, **se omite el mapa de la pieza**.

## Orden del álbum

Se construyen en este orden y se **renumeran al final**, cuando esté
decidido el orden definitivo del álbum.

| nº | canción | archivo | estado |
|---|---|---|---|
| 1 | El Cisne (Saint-Saëns) | `build_*_d01.py` | ✅ |
| 2 | Can't Help Falling in Love | `build_*_d02.py` | ✅ |
| 3 | Your Song | `dilan_03_your_song.py` | ✅ |
| 4 | Thinking Out Loud | `dilan_04_thinking.py` | ✅ |
| 5 | Lucía | `dilan_05_lucia.py` | ✅ |
| 6 | Poema de Amor | `dilan_06_poema.py` | ✅ |
| 7 | Amiga Mía | `dilan_07_amiga.py` | ✅ |
| 8 | La Promesa | `dilan_08_promesa.py` | ✅ |
| 9 | When I Was Your Man | `dilan_09_bruno.py` | ✅ |
| 10 | Al Calor del Amor en un Bar | `dilan_10_calor.py` | ✅ |
| 11 | Soldadito de Hierro | `dilan_11_soldadito.py` | ✅ |
| 12 | A Sky Full of Stars | `dilan_12_sky.py` | ✅ |
| 13 | What Was I Made For | `dilan_13_what.py` | ✅ |
| 14 | Writing's on the Wall | `dilan_14_writings.py` | ✅ |
| 15 | My Favourite Things | `dilan_15_favourite.py` | ✅ |
| 16 | Adagio en Sol menor (Albinoni) | `dilan_16_adagio.py` | ✅ |
| 17 | Arabesque (Burgmüller, 4 manos) | `dilan_17_arabesque.py` | ✅ |
| 18 | Have Yourself a Merry Little Christmas | `dilan_18_merry.py` | ✅ |
| 19 | Santa Tell Me | `dilan_19_santa.py` | ✅ |
| 20 | It's Beginning to Look a Lot Like Christmas (4 manos) | `dilan_20_beginning.py` | ✅ |

Las dos primeras se montaron con los `build_*_d0N.py` antes de que existiera
`cancion.py`; se auditan igual, pasándole las cinco hojas a
`cancion.auditar_hojas()`.

`cuaderno/auditar_dilan.py` pasa las cuatro comprobaciones a las veinte de
una vez. Tiene que salir TODO OK antes de tocar nada más.

Al terminar: generar portada + índice con `cuaderno/portada.py` y unir el
álbum completo.

## Avisos por partitura

- Las de **4 manos** (17, 20) llevan cuatro pentagramas por sistema: el
  emparejado por defecto de `sistemas()` no vale. Se leen con
  `engine/lector_4manos.py`, que agrupa de cuatro en cuatro (0-1 = Primo,
  2-3 = Secondo). **Y las claves cambian de una a otra**: en la Arabesque
  el Secondo lleva sol y fa, y en It's Beginning lleva fa y fa. Hay que
  poner `lector_4manos.CLAVES` a mano antes de leer. El dosier se escribe para el **Primo**, que es la parte
  del alumno, y la hoja de montar habla de tocar en pareja.
- Las cabezas **huecas** (blancas y redondas) se leen con
  `engine/lector_huecas.py`, que rellena huecos antes de abrir. Solo vale
  en manos izquierdas sin ligaduras, y hay que mirar que las posiciones
  caigan cerca de un entero antes de fiarse.
- Las ediciones de MuseScore con letra traen **cifrados impresos**: son
  armonía dada por el editor y valen más que cualquier análisis propio.
- Las cabezas huecas no las ve el lector: en piezas de melodía en notas
  largas, la línea de la derecha se lee a zoom.
