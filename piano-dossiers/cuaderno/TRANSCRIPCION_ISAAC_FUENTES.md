# Isaac — las 20 partituras, comprobadas una a una

Isaac es de nivel medio. El encargo del cliente: subirle el nivel de verdad,
"dale caña", sin llegar al techo de los alumnos más avanzados del proyecto.

Bajada de su carpeta de Drive con `gdown --folder` el 18 de agosto de 2026.
Traía 20 archivos, todos distintos entre sí (comprobado con `md5sum`).

## El dato más llamativo: 19 de las 20 son el mismo archivo que Mercè

Comprobado con `md5sum` contra las carpetas de fuentes de todos los alumnos:

| archivo de Isaac | idéntico a |
|---|---|
| La Pantera Rosa.pdf | mercè (y arnau) |
| OH WHEN THE SAINT.pdf | mercè (y arnau) |
| petite chanson(4 manos).pdf | josep, nel |
| Piano Men.pdf | mercè, luisa |
| Puff era un Drac Magic.pdf | mercè, luisa |
| Rasputin.pdf | mercè, jose_maria, luisa, josep, nel |
| SILENT NINGT.pdf | mercè, luisa |
| TOREADOR-BIZET.pdf | mercè, jose_maria, nel |
| WE WISH YOU A MERRY CHRISTMAS.pdf | mercè |
| -Greensleeves. | mercè, luisa |
| Jailhouse Elvis Presley.pdf | mercè, jose_maria, josep, nel |
| Para Elisa.pdf | mercè |
| silent-night-(4 manos).pdf | mercè |
| Sonrisas y Lagrimas.pdf | mercè |
| Grandfather.pdf | mercè, jose_maria |
| christmas-songs-( 4 manos).pdf | mercè, luisa |
| i-have-a-dream-abba-.pdf | mercè, luisa |
| The Beginer le Debut(4 manos).pdf | luisa |
| DIABELLI ( cuatro manos).pdf | ninguno — pieza propia |

Es decir: **el repertorio de Isaac es, pieza a pieza, casi el mismo que el de
Mercè** (19 de las 20 coinciden con su carpeta), más una añadida de Luisa
(The Beginner, que Mercè no tiene) y una compartida con Josep/Nel (Petite
Chanson). La única pieza sin ningún duplicado en el proyecto es el estudio de
**Diabelli, Op. 149 nº 3**.

Esto no es un problema — la norma del proyecto ya lo cubre: las citas
literales pueden coincidir entre alumnos, lo que no puede coincidir es el
andamio inventado, y eso lo comprueba `cruzar_isaac.py`.

## La pieza propia: Diabelli, "28 melodische Übungsstücke" nº 3, Op. 149

Comprobada a 200 dpi, 3 páginas (edición Mutopia/MutopiaBSD, dominio
público). **Do mayor** (sin armadura), **2/4**, "Moderato." (sin metrónomo
impreso: la casilla de la ficha es "Carácter", no "Tempo"). Es un estudio a
cuatro manos, con las dos partes muy exigentes técnicamente:

- **Secondo** (páginas 1-2): arranca en clave de FA en las dos manos, con
  arpegios rápidos en corcheas y digitación completa impresa; termina con un
  compás en clave de SOL. Dinámicas: *p, f, sf, mf* y reguladores.
- **Primo** (páginas 2-3, la parte de Isaac, por convención del proyecto —
  el alumno toca siempre el Primo en los duetos): **las dos manos van en
  clave de SOL**, con un "8va" al principio (se toca una octava más alto de
  lo escrito). Corcheas con silencios (patrón "nota-silencio-nota-silencio"),
  ligaduras, staccatos, algún grupo de adorno (apoyatura) y acentos (>).
  Tiene una repetición hacia el compás 15 y termina con un acorde con
  calderón.

Es, con diferencia, la pieza más exigente de la carpeta de Isaac: por eso va
la última del álbum, como reto de cierre — igual que Für Elise en el álbum de
Mercè.

## Lo que trae cada pieza (heredado de los álbumes ya medidos)

Con 18 de las 20 partituras ya transcritas nota a nota para Mercè (o Luisa,
o Josep), no hace falta remedirlas: se reutiliza la ficha musical (tonalidad,
compás, reparto de manos, dificultad concreta) tal como está documentada en
los archivos `me_*.py` / `lu_*.py` / `jp_*.py` correspondientes, y se escribe
un andamio **nuevo**, propio de Isaac, para que no coincida con el de nadie.

| pieza | ton. · compás | de dónde sale la ficha |
|---|---|---|
| Petite Chanson (4 manos) | Do · 4/4 | jp_02_petite.py |
| Oh, When the Saints | Do · 4/4 | me_02_saints.py |
| Puff the Magic Dragon | Do · 4/4 | me_04_puff.py |
| The Beginner (Gurlitt, 4 manos) | Do · 3/4 | lu_02_beginner.py |
| We Wish You a Merry Christmas | Sol (1♯) · 3/4 | me_10_wewishyou.py |
| Christmas Songs (4 manos) | Do · 4/4 · ♩=100 | me_08_christmas.py |
| Silent Night | Do · 3/4 | me_09_silentnight.py |
| Silent Night (4 manos) | Do · 3/4 | me_11_silentnight4h.py |
| La Panthère rose | Do · 4/4 | me_12_panthere.py |
| Piano Man | Do · 3/4 · ♩=178 | me_13_pianoman.py |
| Greensleeves | La menor · 3/4 | me_16_greensleeves.py |
| My Grandfather's Clock | Sol (1♯) · 4/4 | me_19_grandfather.py |
| Do Re Mi | Do · 4/4 | me_07_doremi.py |
| I Have a Dream | Do · 4/4 · ♩=120 | me_20_dream.py |
| Honor Him · Gladiator | La mayor (3♯) · 3/4 · ♩=70 | me_22_gladiator.py |
| Rasputin | Si menor (2♯) · 4/4 · ♩=124 | me_23_rasputin.py |
| Jailhouse Rock | Do, blues · 4/4 · ♩=150 swing | me_24_jailhouse.py |
| Toreador · Carmen | Fa mayor (1♭) · 4/4 · Nivel 4 | me_25_toreador.py |
| Für Elise (edición real, arranque) | La menor · 3/4 | me_26_furelise.py |
| Diabelli, Op. 149 nº 3 (4 manos) | Do · 2/4 | medida de cero, ver arriba |

## Lo que NO está medido, y por qué se dice

Todo el material generado va etiquetado como **andamio** y remite a la
partitura de Isaac para las notas exactas — la regla de siempre.
