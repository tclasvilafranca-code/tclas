# Eduard · las 16 partituras de su carpeta de Drive

Medido el 26 de agosto de 2026 sobre los PDF **recién bajados de su carpeta**,
no sobre ninguna copia anterior. Están en `students/eduard/source_new/`.

## Por qué se rehace el álbum entero

El álbum que hay montado ahora **no es suyo**: se construyó copiando las
fuentes de José María (Romance de Diabelli, America, Star-Spangled Banner,
Counting Stars, Peaches, Someone You Loved, Shallow, Can't Help, Carol of the
Bells, Adagio de Albinoni, Trouble, A comme amour, Interstellar, Flying Theme).
De sus diecinueve piezas, **solo tres están de verdad en su carpeta**:
Toreador, Rasputin y Grandfather's Clock — y las tres son de las más difíciles
que él tiene.

Su repertorio real es bastante más suave y empieza mucho más abajo: hay tres
piezas de **un solo pentagrama con letra**, dos a **cuatro manos** y un
Nocturno de Chopin reducido a lo esencial. Eso es un alumno adulto que empieza,
que es lo que es.

## Una trampa del nombre de fichero

`Escalas y Arpegios Facil progresando.pdf` **no es un cuaderno de escalas**.
Dentro pone *Los aristogatos*, de Richard y Robert Sherman, arreglo de
A. C. Escobés: un solo pentagrama, Adagio. Si se hubiera creído el nombre del
fichero, el álbum habría tenido una hoja de técnica donde hay una canción.
Es exactamente el caso que obliga la norma: **leer el título impreso DENTRO del
PDF, no fiarse del nombre.**

## Lo medido, pieza a pieza

Compás y armadura leídos sobre el recorte del primer pentagrama a 300 ppp.
El tempo, de `pdftotext` cuando la edición lo imprime.

| # | pieza | edición | pág | compás | armadura | tempo | manos |
|---|---|---|---|---|---|---|---|
| 1 | Clementine (*…OR: Found a Peanut*) | arr. Gilbert DeBenedetti · **Primer Level** | 1 | 3/4 | — | — | 1 pentagrama + letra |
| 2 | Los Aristogatos | Sherman · arr. A. C. Escobés | 1 | 4/4 | — | Adagio | 1 pentagrama |
| 3 | Eso que tú me das | Jarabe de Palo · *Parte 1* | 1 | 4/4 | — | — | 1 pentagrama + cifrado |
| 4 | La Panthère Rose | *Première année* | 1 | 4/4 | — | — | 2 |
| 5 | Nocturne op. 9 | Chopin · arr. Benny Chaw | 1 | 3/4 | — | *mp* | 2 |
| 6 | The Beginner · Le Début | Gurlitt op. 211 nº 3 | 1 | 3/4 | — | Allegretto | **4 manos** |
| 7 | Heart and Soul | Hoagy Carmichael · *Easy Piano Version* | 1 | 4/4 | — | ♩=110 *Swing* | 2 |
| 8 | I Have a Dream | ABBA · *children song* | 2 | 4/4 | — | 120 | 2 |
| 9 | Greensleeves | tradicional inglesa | 2 | 3/4 | — | Moderato · *con pedale* | 2 + cifrado |
| 10 | Honor Him · Gladiator | Hans Zimmer · *Easy Version* | 1 | 3/4 | **3 ♯** | ♩=70 | 2 |
| 11 | Christmas Songs for Four Little Hands | Mindy Liang · *Beginner Version* | 2 | 4/4 | — | ♩=100 | **4 manos** |
| 12 | Jingle Bell Rock | arr. Sadie King | 1 | 4/4 | — | *Swing* | 2 |
| 13 | Piano Man | Billy Joel · *Simplified, SimplyPiano* | 2 | 3/4 | — | ♩=178 | 2 |
| 14 | Rasputin A | Boney M · *Easy piano* | 2 | 4/4 | **2 ♯** | ♩=124 | 2 + cifrado |
| 15 | My Grandfather's Clock | arr. Gilbert DeBenedetti · **Level Three** | 2 | **C** (4/4) | — | — | 2 |
| 16 | Toreador · Carmen | Bizet · arr. DeBenedetti · **Level Four** | 1 | **C** (4/4) | **1 ♭** | *March time* | 2 |

### Dos comprobaciones que estuvieron a punto de colarse

- **Grandfather's Clock parecía ir en 6/8.** En la miniatura, lo que hay
  después de la clave se lee como un 6 sobre un 8. Ampliado a 300 ppp es una
  **C de compasillo**, y el supuesto «8» son **dos redondas apiladas** del
  pentagrama de abajo. Va en 4/4, como decía el álbum viejo. *Si una
  comprobación visual va a decidir un cambio, hazla al tamaño en que no quepa
  duda.*
- **El Nocturno no lleva armadura.** El op. 9 nº 2 de Chopin está en Mi bemol
  mayor (tres bemoles) y va en 12/8; este arreglo de Benny Chaw lo pasa a **3/4
  y sin ninguna alteración**. Se comprobó ampliado porque el dato «Chopin op. 9
  sin armadura» es justo el que uno da por supuesto al revés.

### Resoluciones que no se pueden medir

Tres PDF son una **foto metida dentro**, no vectorial, y a esa resolución el
detector de figuras no distingue una semicorchea de un borrón:

| pieza | ppi |
|---|---|
| Clementine | 72 |
| Grandfather's Clock | 72 |
| Toreador | 76 |

Van miradas a ojo y anotadas en `auditar_figuras.MIRADAS`, como las otras 31
del proyecto. **Más vale no saberlo que creer que se sabe.**

## El orden propuesto

No es el orden de la carpeta: es un arco que va de un solo pentagrama a las dos
manos, de ahí a cuatro manos con la profesora, y solo al final a las dos piezas
que su propia edición marca como *Level Three* y *Level Four*.

1. Clementine · un pentagrama, 3/4
2. Los Aristogatos · un pentagrama, 4/4
3. Eso que tú me das · un pentagrama con cifrado
4. La Panthère Rose · **las dos manos por primera vez**
5. Nocturne op. 9 · 3/4, lento, todo el tiempo del mundo
6. The Beginner · **a cuatro manos con la profesora**
7. Heart and Soul · el swing
8. I Have a Dream · frases largas
9. Greensleeves · **la primera en menor**
10. Honor Him · **la primera armadura de verdad, tres sostenidos**
11. Christmas Songs · cuatro manos otra vez, ya con soltura
12. Jingle Bell Rock · swing con más notas
13. Piano Man · ♩=178, la rápida
14. Rasputin · Si menor y cifrado
15. My Grandfather's Clock · *Level Three*
16. Toreador · *Level Four*, el reto del final

## El nivel

Escalón **1 subiendo a 2** (`niveles.py`): hasta la corchea, con el puntillo
entrando a mitad de curso. Nada de semicorcheas salvo donde su propia partitura
las traiga — y ahí manda la partitura, con su excepción anotada.
