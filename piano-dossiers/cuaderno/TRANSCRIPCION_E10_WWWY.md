# When We Were Young (Adele) — medición

**Archivo**: `students/eva/source/EVA/WHEN WE WERE YOUNG _ Adele Dm .pdf`
**sha256**: `verificado en la carpeta de Drive de Eva` · 4 páginas ·
arreglo de musicaparadisfrutar.com. **No está en el álbum de Dilan**: es una
de las dos piezas nuevas de Eva.

## Método

Esta edición es un caso raro y afortunado: **imprime el cifrado encima de cada
compás y numera los compases cada sistema**. Eso significa que la línea del
bajo y la armonía entera se leen como TEXTO, no como notas, y se pueden
extraer con `pdftotext -layout` sin ninguna interpretación. Contrastado
sistema a sistema con las cuatro páginas rasterizadas a 110 y 200 dpi.

Lo que **no** se ha medido, y por tanto no se cita en el cuaderno:

- las alturas de la melodía (corcheas y semicorcheas muy densas, con
  ligaduras de unión y de fraseo cruzándose);
- el *voicing* exacto de la mano izquierda (cabezas huecas: el lector de
  partituras devuelve lecturas dispersas y no fiables en esta edición).

Donde un ejercicio necesita notas concretas de la izquierda, va rotulado
**ANDAMIO**. El BAJO no es andamio: lo dice el cifrado, nota por nota.

## Datos comprobados

| dato | valor | dónde se ve |
|---|---|---|
| Tonalidad | Re menor (un bemol) | armadura, pág. 1 |
| Tempo | ♩ = 72 | impreso sobre el c. 1 |
| Compás | 4/4 · **5/4 en el c. 62** | armadura de compás, y el cambio en la pág. 4 |
| Compases | 63 | numeración impresa + recuento del último sistema |
| 8vb | cc. 7–8 y cc. 15–16 | línea de puntos sobre la derecha, pág. 1 |
| Tresillos | cc. 21, 23 y 60 | el «3» sobre el grupo |
| Letra | sílaba a sílaba bajo el pentagrama | todas las páginas |

## El mapa armónico, compás a compás

Las barras separan compases. Dos acordes en un compás = dos tiempos cada uno.

```
Intro      1-4    | Dm  Fmaj7/A | Si♭  Fmaj7/A | Gm7 | F |
Estrofa    5-8    | Dm  Fmaj7/A | Si♭  F/A     | Gm7 | F |
           9-12   | Dm  Fmaj7/A | Si♭  F/A     | Gm7 | F |
          13-16   | Dm  Fmaj7/A | Si♭  F/A     | Gm7 | F |
          17-20   | Dm  Fmaj7/A | Si♭  F/A     | Gm7 | C |
Puente    21-24   | Si♭  C | Am7  Si♭ | Si♭  C | Am7  C |
Estribillo 25-27  | F  Am6 | Si♭  C | F  Am6 |
          28-30   | Si♭  C | Dm7  Am | Si♭maj7  Si♭m |
          31-34   | Gm7 | C  A/Do♯ | Dm  F/Do | Si♭  F/La |
          35-37   | Gm7 | C  A/Do♯ | Dm  F/Do |
          38-40   | Si♭  F/La | Gm7 | C |
          41-43   | Dm  F/Do | Si♭  F/La | Gm7 |
          44-46   | C | Si♭  C | Am7  Si♭ |
          47-50   | Si♭  C | Am7  C | F  Am7 | Si♭  C |
          51-53   | F  Am6 | Si♭  C | F  Am6 |
          54-56   | Si♭  C | F  Am6 | Si♭  C |
          57-59   | Dm7  Am | Si♭maj7  C | Dm7  Am |
Final     60-63   | Si♭maj7  Si♭m | Gm7 | C (5/4) | F |
```

## Lo que se deduce de ahí, y que es lo que enseña el cuaderno

1. **El ciclo de la estrofa son cuatro compases** y se repite **cuatro veces**
   seguidas (cc. 5–20). La cuarta vuelta solo cambia el último acorde: Do en
   el c. 20 en vez de Fa.
2. **El bajo de ese ciclo desciende**: Re · La · Si♭ · La · Sol · Fa. Leído
   solo por abajo, es una línea, no una lista de acordes.
3. **El Do♯ de los cc. 32 y 36** (A/Do♯) es la única nota de fuera de la
   tonalidad de toda la pieza. Es la tercera de La mayor, dominante de Re
   menor, y por eso el compás siguiente es Dm.
4. **El Si♭m del c. 60** es el otro acorde prestado: el Si♭ de siempre, menor.
5. De **63 compases hay menos de 20 de material distinto**: cc. 25–30 = cc.
   51–56, y los cc. 31–37 vuelven en los cc. 47–50.
6. **El c. 62 va en 5/4** y la izquierda lo reparte como blanca + blanca con
   puntillo (2 + 3). Es el único compás de cinco tiempos de la pieza.
