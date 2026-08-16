# Bohemian Rhapsody (Queen) — medición

**Archivo**: `students/eva/source/EVA/bohemian-rhapsody.pdf` · 2 páginas ·
descarga de Musescore (lleva marca de agua en la primera línea de cada página,
que hay que saltar al leer el texto). **No está en el álbum de Dilan**: es la
segunda de las dos piezas nuevas de Eva.

## Método

Como la de Adele, esta edición **imprime el cifrado encima de cada compás**,
con el bajo escrito cuando el acorde va invertido (B♭/D, Cm/B, Cm/B♭, F/A,
Fm/A♭, E♭/D, Fm/E♭, Fm/D, E♭/G, F7sus4/C). Eso se extrae como texto con
`pdftotext -layout` y se contrasta sistema a sistema con las dos páginas
rasterizadas a 110 dpi.

**No se citan alturas de la melodía ni el voicing exacto de la izquierda.** Lo
que sí es dato duro es el CIFRADO, y con él la línea del bajo entera.

## Datos comprobados

| dato | valor | dónde se ve |
|---|---|---|
| Tonalidad | Si♭ mayor (dos bemoles) | armadura |
| Tempo | ♩ = 66 | impreso sobre el c. 1 |
| Compás | 4/4, con **5/4 en el c. 3** y **2/4 en el penúltimo** | los tres cambios están impresos |
| Páginas | 2 | |
| Recorrido | Segno en el último compás de la pág. 1 · **Fine** en el primero de la pág. 2 · **D.S. al Fine** al final | |
| Textura MI | pág. 1 acordes en bloque · pág. 2 corcheas corriendo | se ve de un vistazo comparando las dos páginas |

## El mapa armónico

**Página 1** (16 compases: 3 + 3 + 3 + 3 + 4)

```
 1-3    | B♭ | C7 | F7 (5/4) |        ← el c. 3 tiene cinco tiempos
 4-6    | B♭ | Gm | B♭7 |
 7-9    | E♭ | Cm | F7 |
10-12   | C♭  B♭  A  B♭ | C♭  B♭  A  B♭ | E♭   B♭/D |
13-16   | C♯dim | F7sus4/C | F7 | ‖: 𝄋 B♭ |
```

**Página 2**

```
        | Fine (compás de espera) | B♭ | Gm |
        | Cm | Cm   F | B♭ |
        | Gm | Cm  Cm/B  Cm/B♭ | F/A   Fm/A♭ |
        | E♭  E♭/D | Cm | Fm  Fm/E♭  Fm/D |
        | B♭ | E♭ | B♭ |
        | Cm | A♭m | E♭  A♭  E♭/G | F♯dim  Fm (2/4) :‖   D.S. al Fine
```

## Lo que se deduce, y que es lo que enseña el cuaderno

1. **El bajo baja cromáticamente, y eso es la canción.** En la sección de
   «Mama»: Do → Si → Si♭ → La → La♭ (Cm · Cm/B · Cm/B♭ · F/A · Fm/A♭). Las
   barras del cifrado no son adorno: son una línea que desciende medio tono
   cada vez. El mismo gesto vuelve dos veces más: E♭ → E♭/D → Cm (Mi♭ · Re ·
   Do) y Fm → Fm/E♭ → Fm/D (Fa · Mi♭ · Re).
2. **Los cc. 10 y 11 son el otro cromatismo**: Do♭ · Si♭ · La · Si♭, cuatro
   acordes en un compás, uno por tiempo, y el Do♭ y el La son vecinos del
   Si♭ por arriba y por abajo.
3. **Tres compases irregulares**: el c. 3 en 5/4 y el penúltimo en 2/4. Son
   dos, y están señalados; lo que no se puede es tocarlos de oído.
4. **La izquierda cambia de textura entera al pasar de página**: bloques en la
   primera, corcheas corriendo en la segunda. Es la misma armonía con otra
   ropa.
5. **El recorrido**: se toca todo, y al llegar al «D.S. al Fine» se vuelve al
   segno (último compás de la pág. 1) y se acaba en el «Fine» (primer compás
   de la pág. 2).
