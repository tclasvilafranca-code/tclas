# El Cuaderno del Pianista — Motor de Dosieres · guía para Claude Code

> ## ⚠️ FORMATO VIGENTE: el cuaderno de 6 páginas (`cuaderno/`)
>
> El formato **actual y definitivo** son **6 páginas por canción**, generadas por
> `cuaderno/build_cancion_<n>.py`:
>
> | Pág. | Hoja | Módulo |
> |---|---|---|
> | 1 | La partitura original | (PDF fuente, sin tocar) |
> | 2 | Ficha de la partitura | `ficha_info.py` |
> | 3 | Calentamiento | `hoja_calentamiento.py` |
> | 4 | Agudeza visual y auditiva | `hoja_lectura.py` |
> | 5 | Al piano · por partes | `hoja_piano.py` |
> | 6 | Al piano · montarla | `hoja_piano.py` |
>
> Más `cuaderno/portada.py` para portada + índice del álbum de cada alumno.
>
> ### Las tres reglas que sostienen el formato
>
> 1. **Todo sale de la partitura.** Ningún ejercicio se inventa: cada uno indica
>    de qué compases procede. Antes de escribir nada hay que **transcribir la
>    pieza midiendo el PDF fuente** (render a 150 dpi, detectar las 5 líneas de
>    cada pentagrama, medir la posición vertical de cada cabeza de nota, y
>    comprobar visualmente a zoom todo lo dudoso). El resultado se guarda en
>    `cuaderno/TRANSCRIPCION_<nn>_<TITULO>.md`. Ver ese archivo como plantilla.
>    **Nunca afirmes en papel un dato musical que no hayas medido** — pasó una
>    vez (se dio por buena una 5ª que no existía en la pieza) y hubo que
>    corregir material ya entregado.
> 2. **Cada hoja tiene una lógica propia, y son opuestas entre sí.**
>    El calentamiento usa **secuencias** (una célula transportada grado a grado)
>    porque busca memoria muscular. La hoja de lectura usa **anti-secuencia**
>    (orden deliberadamente irregular) porque un patrón deja que el alumno
>    adivine en vez de leer. Las hojas al piano usan **aislar → reducir →
>    reinsertar**: la última siempre devuelve el material a la partitura, o el
>    alumno acaba tocando ejercicios bien y la pieza mal.
> 3. **Densidad real de partitura publicada:** 12–32 pt por tiempo, 4–8 compases
>    por línea. Usa `spacing='engraved'` en `draw_system`. Ver
>    `ANALISIS_ESCRITURA_MUSICAL.md`.
>
> ### Correspondencia con el dosier de ejercicios por niveles del cliente
>
> | Bloque del documento | Dónde vive |
> |---|---|
> | 2. Técnica al piano | Calentamiento + hojas al piano |
> | 3. Lectura, ritmo e interpretación | Agudeza visual (parte 1) |
> | 4. Entrenamiento auditivo | Agudeza auditiva (parte 2) |
> | 6. Teoría escrita | Ficha de la partitura |
> | E. Estrategias de estudio | Hojas al piano (es su núcleo) |
>
> Los bloques 1 (calentamiento físico), 5 (juegos) y 7 (creatividad) quedan
> **fuera del cuaderno por decisión del cliente**: mejor menos y mejor.
>
> ### Verificación obligatoria antes de entregar
> `run_full_audit` (compases) + `audit_text_bounds` (margen derecho) +
> comprobación de píxeles del borde inferior. Las tres, en las 5 hojas.
> Los avisos de *sparse* son aceptables solo en sistemas de blancas/silencios.
>
> Lo que sigue documenta el **formato antiguo de 5 páginas** (`engine/`,
> `examples/`), que ya no se usa para material nuevo pero sigue en producción
> para los álbumes ya entregados. El motor de notación (`notation.py`,
> `audit_suite.py`) es común a los dos y sí se sigue usando.

---

Este proyecto generaba **dosieres de piano de 5 páginas** (partitura + teoría + 2 páginas
de ejercicios + ficha de lenguaje musical sin piano) para alumnos de piano infantil,
en PDF, con calidad profesional de imprenta.

Todo lo que hay en `engine/` es el motor ya construido, probado y verificado a lo
largo de un proyecto real de 20 canciones. **No lo reescribas desde cero.** Impórtalo
y reutilízalo. Este documento te dice exactamente cómo.

## Antes de nada: instala dependencias

```bash
pip install reportlab pypdf pdf2image --break-system-packages
# Necesitas también poppler-utils para pdftoppm/pdftotext/pdfseparate/pdfimages:
apt-get install -y poppler-utils   # si no está ya
# Fuentes necesarias (normalmente ya presentes en Ubuntu):
#   /usr/share/fonts/truetype/dejavu/DejaVuSans*.ttf
#   /usr/share/fonts/truetype/freefont/FreeSerif.ttf   <- ¡imprescindible! (claves, silencios)
```

Si `FreeSerif.ttf` no existe: `apt-get install -y fonts-freefont-ttf`.

## Estructura de carpetas

```
engine/
  notation.py                 Motor de notación: pentagramas, claves, notas, acordes,
                               plicas, barras de corcheas, silencios, alteraciones,
                               puntillos, teclado, keyboard, colores del tema.
  page_layout_common.py       Layout compartido de las 2 páginas de EJERCICIOS
                               (cabecera, pie, exercise_heading, system_block,
                               grand_staff_block).
  page_theory_generic.py      Generador de la página de TEORÍA (ficha de lenguaje
                               musical), parametrizado por un diccionario `song`.
  page_worksheet_generic.py   Generador de la FICHA SIN PIANO (escribir notas,
                               colorear, quiz), parametrizado por un diccionario `cfg`.
  audit_suite.py              Auditor automático — ver más abajo. ÚSALO SIEMPRE.
  transpose_util.py           Transposición diatónica simple nota a nota.
  ast_transpose.py            Transposición automática de un archivo de ejercicios
                               completo (para cambiar de tonalidad sin reescribir a mano).
examples/
  build_song4.py + page_exercises_song4.py    Ejemplo simple: Do mayor, 4/4.
  build_song7.py + page_exercises_song7.py    Ejemplo: compás 3/4 (vals).
  build_song14.py + page_exercises_song14.py  Ejemplo: Fa mayor (con Sib).
  build_song17.py + page_exercises_song17.py  Ejemplo: La menor + silencios.
  build_song20.py + page_exercises_song20.py  Ejemplo: compás 6/8 + negra con puntillo.
assets/
  asset_qr_real.png           QR de ejemplo — sustitúyelo por el QR real de cada
                               canción/alumno si lo hay, o usa un placeholder.
  asset_logo_tclas.png        Logo T-Clas para portadas de álbum (opcional).
```

## El flujo de trabajo completo para UN dosier nuevo

1. **Reúne los datos de la canción**: título, compositor/arreglista, tonalidad real
   (¡verificada, no asumida — ver sección "Tonalidad" más abajo!), compás, tempo,
   forma, dificultad, la dificultad técnica concreta (con su "reto" y su "truco"),
   y una curiosidad ("¿sabías que...?").
2. **Consigue la partitura** como página de PDF independiente (una sola página,
   imagen o vectorial, con la música real). Si viene de un PDF más grande:
   ```bash
   pdfseparate -f <pagina> -l <pagina> origen.pdf partitura_nombre.pdf
   ```
3. **Compón los ejercicios** (`page_exercises_<nombre>.py`) usando
   `page_layout_common`. Sigue el patrón de los ejemplos en `examples/`. Ver
   "Estructura de las 2 páginas de ejercicios" más abajo.
4. **Construye la teoría y la ficha** (`build_<nombre>.py`) usando
   `page_theory_generic.build_theory_page` y `page_worksheet_generic.build_worksheet`.
5. **Audita ANTES de generar ningún PDF visual.** Ver sección de auditoría.
   No se entrega nada sin pasar el auditor con 0 errores de compás y 0 desbordes
   de texto.
6. **Genera y une las 5 páginas** con `pypdf` (partitura + teoría + ejercicios×2 +
   ficha), en ese orden.
7. **Verificación final por píxeles**: renderiza a JPEG con `pdftoppm` y comprueba
   que ninguna página se desborda por abajo ni por la derecha (código de ejemplo
   en la sección correspondiente).

## La API del motor de notación (`notation.py`)

Todas las coordenadas son en puntos PDF (72pt = 1 pulgada), origen abajo-izquierda.

- `draw_staff(c, x, top_y, w, gap, lines=5)` → lista de 5 coordenadas Y (arriba→abajo).
- `draw_clef(c, x, staff_bottom_y, gap, clef='treble'|'bass'|'alto')` — las 3 claves
  están calibradas matemáticamente para que caigan exactamente en su línea de
  referencia. **No cambies las constantes de calibración** (`5.038*gap`, `5.426*gap`,
  `7.23*gap`, etc.) — están verificadas con precisión sub-píxel.
- `draw_time_sig(c, x, staff_bottom_y, gap)` — usa siempre `(4,4)` salvo que pases
  `time_sig` explícito a `draw_system`.
- `note_y(staff_bottom_y, gap, pitch, clef)` — calcula la posición Y de una nota.
- `draw_note(...)`, `draw_chord(...)`, `draw_rest(...)` — dibujan elementos
  individuales. **Normalmente NO los llames directamente**: usa `draw_system`, que
  se encarga de plicas, barras de corcheas, alteraciones y puntillos por ti.
- `draw_system(c, x, top_y, width, gap, events, clef='treble', time_sig=(4,4))` →
  `(top, bot)`. Es la función principal. `events` es una lista de diccionarios:
  ```python
  {'pitch': 'C4', 'dur': 'q', 'number': 1}        # nota sola, con dedo opcional
  {'pitches': ['C3','E3','G3'], 'dur': 'q', 'label': 'Do'}   # acorde, con etiqueta opcional
  {'rest': True, 'dur': 'q'}                       # silencio
  {'pitch': 'Bb4', 'dur': 'q'}                      # alteración: 'b' o '#' tras la letra
  {'pitch': 'C4', 'dur': 'q.'}                      # nota con puntillo (1.5×)
  {'pitch': 'C4', 'dur': 'e', 'beam': 0}            # corchea con id de grupo para la barra
  ```
  Duraciones válidas: `'w'`(redonda,4) `'h'`(blanca,2) `'q'`(negra,1) `'e'`(corchea,0.5)
  `'q.'`(1.5) `'h.'`(3) `'e.'`(0.75).

## Estructura de las 2 páginas de EJERCICIOS (`page_layout_common`)

Cada página de ejercicios sigue SIEMPRE este patrón (no lo cambies, es el que el
alumno ya reconoce):

```python
from page_layout_common import *

SONG_KICKER = 'NIVEL X · ETIQUETA · TÍTULO DE LA CANCIÓN'

def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    # ... breve intro en prosa (una línea) ...
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    # Ejercicio 1: posición de 5 dedos (calentamiento, 3 sistemas de una sola clave)
    y = exercise_heading(c, y, 1, 'Título', nivel_dificultad_1_a_3, 'descripción')
    y -= 12
    ev = [...]
    y = system_block(c, x0, w0, y, gap, 'a) subtítulo', ev, clef='treble')
    # ... b) y c) ...
    y -= 6

    # Ejercicio 2: LA DIFICULTAD ESPECÍFICA de esta canción (siempre dedicado a
    # ella, con 3 variantes que la trabajan desde distintos ángulos)
    y = exercise_heading(c, y, 2, ...)
    ...

    # Ejercicio 3: acordes I-IV-V de la tonalidad, en clave de FA (2 sistemas)
    y = exercise_heading(c, y, 3, ...)
    ...

    exercises_footer(c, 3)
    c.showPage()

def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    ...
    # Ejercicio 4: manos juntas (grand_staff_block ×2, o ×1 + system_block)
    # Ejercicio 5: independencia rítmica (grand_staff_block + system_block)
    # Ejercicio 6: reto final — la canción casi completa (grand_staff_block)
    exercises_footer(c, 4)
    c.showPage()
```

`system_block(c, x0, w0, y, gap, caption, events, clef, time_sig=(4,4))` dibuja un
sistema con su título y devuelve la `y` ya lista para el siguiente elemento.

`grand_staff_block(c, x0, w0, y, gap, treble_events, bass_events, caption,
grand_gap_mult=7.3, time_sig=(4,4))` dibuja un sistema de piano completo (sol+fa).
**El total de tiempos (beats) de `treble_events` y `bass_events` debe coincidir
siempre** — si no, las dos claves quedan desincronizadas visualmente.

### Presupuesto de página (para que no se desborde)
- Página de ejercicios completa (cabecera+3 ejercicios con 3 sistemas sencillos
  cada uno, o cabecera+3 ejercicios variados) ≈ cabe justo en una A4. Si añades
  un ejercicio de más o un `grand_staff_block` extra, **compruébalo con el
  auditor de texto** (no hay presupuesto de sobra).
- Cada `system_block` de una sola clave cuesta ≈ 78pt de alto (con `gap≈7.3-7.6`).
- Cada `grand_staff_block` cuesta ≈ 158pt de alto.

## Estructura de la página de TEORÍA (`page_theory_generic.build_theory_page`)

```python
from page_theory_generic import build_theory_page

song = dict(
  num=21, title='Título de la canción', subtitle='Compositor · arr. Quien sea',
  tonalidad='Do mayor', compas='4/4', tempo='Alegre ♩≈100', forma='Estrofa',
  dificultad='Fácil', manos='Melodía + acordes',
  la_cancion='Una frase o dos describiendo la canción para un niño.',
  difficult_cc='cc. 1–4', difficult_title='Nombre corto de LA dificultad concreta',
  reto='qué hay que superar, en una frase.',
  truco='cómo practicarlo, en una frase.',
  sabias_que='Una curiosidad real y verificable sobre la canción/compositor.',
  mini_staff_events=[...],   # 8 tiempos de ejemplo en la posición de 5 dedos
  # Solo si la tonalidad NO es Do mayor, añade además:
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa','Sol','La','Sib','Do','Re','Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA...',
  estudiar_steps=[...],       # 4 pasos
  checklist_items=[...],      # 4 casillas
)
build_theory_page(c, 'assets/asset_qr_real.png', song)
```

## Estructura de la FICHA SIN PIANO (`page_worksheet_generic.build_worksheet`)

```python
from page_worksheet_generic import build_worksheet

cfg = {
 'kicker': 'NIVEL X · ETIQUETA · TÍTULO',
 'sec1_treble': [8 nombres de nota, en solfeo, ej. 'Do','Re','Mi'...],
 'sec1_bass':   [8 nombres de nota — DISTINTOS de sec1_treble idealmente],
 'sec2_title': 'Título de la sección temática (ligada a la dificultad de la canción)',
 'sec2_desc': 'Instrucción para el alumno.',
 'sec2_pitches': [12 alturas reales, ej. 'C4','D4'...],   # notas sin plica que el
                                                            # alumno completa
 'sec3_title': 'Colorea solo las notas X',
 'sec3_desc': 'Instrucción.',
 'sec3_treble': [12 alturas], 'sec3_bass': [12 alturas],
 'pista_text': 've "Tonalidad y pistas" más abajo — ¡NUNCA la inventes a ojo!',
 'quiz_pitches': [7 alturas],
}
build_worksheet(c, cfg)
```

**Solo lleva claves de Sol y de Fa** (la clave de Do se quitó del proyecto por
decisión del cliente — no la reintroduzcas).

## Tonalidad — cómo NO equivocarse (esto costó una corrección grande)

**Nunca asumas la tonalidad por el texto de una fuente sin verificar la partitura
real.** En este proyecto, dos canciones (de 20) tenían la tonalidad mal etiquetada
porque el texto descriptivo decía "Do mayor" pero la partitura real llevaba
armadura de Fa mayor (un bemol). Antes de dar por buena una tonalidad:
1. Mira la armadura de la partitura real (¿hay sostenidos o bemoles justo después
   de la clave, antes del compás?).
2. Si hay un bemol en Si → Fa mayor. Si hay un sostenido en Fa → Sol mayor.
   Si no hay nada y sí hay indicios de tono menor (acordes menores, sonido
   "triste"/"misterioso" en la descripción) → probablemente La menor (relativo
   de Do mayor).
3. Si tienes dudas y no puedes verificarlo de forma fiable, dilo explícitamente
   al usuario en vez de asumir.

### Si la canción NO está en Do mayor

- **Posición de 5 dedos**: el dedo 1 va siempre en la tónica. Fa mayor → Fa(1)
  Sol(2) La(3) Sib(4) Do(5). Sol mayor → Sol(1) La(2) Si(3) Do(4) Re(5). Todas
  las digitaciones del resto del dosier deben ser coherentes con esto.
- **Acordes I-IV-V**: se construyen sobre la tónica real, no sobre Do. Fa mayor →
  Fa-Sib-Do. Sol mayor → Sol-Do-Re.
- **Alteraciones**: usa `'Bb4'`, `'F#4'`, etc. en los pitches — el motor ya
  calcula la posición en el pentagrama ignorando la alteración (mismo lugar que
  la nota natural) y dibuja el símbolo (♭ o ♯) automáticamente.
- **Transposición automática**: si ya tienes una versión en Do mayor y quieres
  pasarla a Fa mayor sin reescribir todo a mano, usa `ast_transpose.py`:
  ```bash
  python3 engine/ast_transpose.py entrada_do_mayor.py salida_fa_mayor.py
  ```
  Esto transpone una 4ª justa hacia arriba TODOS los `'pitch'`, `'pitches'` y
  `'label'` del archivo (Do→Fa, Re→Sol, Mi→La, Fa→Sib, Sol→Do, La→Re, Si→Mi),
  preservando los números de dedo (que ya cuadran solos porque el patrón de
  digitación es diatónico). Después de transponer, revisa a mano el texto en
  prosa (títulos, captions) que mencione notas — el transpositor NO toca texto
  narrativo, solo estructuras de datos.
- Para La menor: los acordes naturales son i (menor), iv (menor), v (menor) —
  no uses V mayor (con sensible alterada) salvo que la pieza real lo pida.

## Las "pistas" de la ficha — cómo no equivocarse (otro fallo real corregido)

La sección "Colorea" de la ficha usa la MISMA nota en clave de Sol Y en clave de
Fa — y la posición en el pentagrama es DISTINTA en cada clave. Una pista que solo
describe la posición en Sol es errónea para la mitad del ejercicio. Tabla
verificada (posición en clave de Sol / posición en clave de Fa):

| Nota | Clave de Sol | Clave de Fa |
|---|---|---|
| DO  | 1ª línea adicional bajo el pentagrama (con rayita) | 2º espacio |
| RE  | justo debajo de la 1ª línea (sin rayita) | 3ª línea (la del medio) |
| MI  | 1ª línea (la de abajo) | 3er espacio |
| FA  | 1er espacio | 4ª línea |
| SOL | 2ª línea | 1ª línea (la de abajo) |
| LA  | 2º espacio | 1er espacio |
| SI  | 3ª línea (la del medio) | 2ª línea |

Escribe siempre la pista mencionando **ambas claves**, ej.: *"en clave de Sol,
MI está en la primera línea; en clave de Fa, MI está en el tercer espacio."*
El cuadro de la pista envuelve el texto en varias líneas automáticamente
(`wrap_text`), así que no hace falta acortarlo artificialmente — pero comprueba
igualmente con el auditor de texto.

## El auditor — úsalo SIEMPRE antes de entregar nada

`audit_suite.py` expone:

```python
from audit_suite import run_full_audit, audit_text_bounds

# 1) Compases: comprueba que cada pentagrama tenga un número de tiempos
#    múltiplo exacto del compás, y avisa si un pentagrama queda muy disperso
#    (pocos elementos repartidos en todo el ancho).
run_full_audit('nombre descriptivo', modulo.page1)
run_full_audit('nombre descriptivo', modulo.page2)

# 2) Texto: comprueba que ningún drawString/drawCentredString se salga del
#    margen derecho de la página (549.28pt).
overflow = audit_text_bounds(build_fn, 595.276, 841.89, 549.28)
```

**Regla de oro: 0 errores de compás y 0 desbordes de texto antes de generar
ningún PDF visual.** Los avisos de "sparse" (disperso) son aceptables SOLO
cuando son pedagógicamente intencionados (ej. un ejercicio específico de notas
largas, silencios, o "solo dos pulsos por compás" en 6/8) — no los ignores sin
pensarlo, pero tampoco fuerces densidad artificial que rompa el sentido del
ejercicio.

### Duplicados entre canciones/alumnos

Si generas varios dosieres en la misma sesión (varios alumnos, o varias
canciones), comprueba que no repites la MISMA secuencia de notas nota-por-nota
entre ejercicios de dosieres distintos (aunque el texto de alrededor cambie).
Patrón de escaneo (adapta la lista de módulos):

```python
import notation as nt
orig = nt.draw_system
seqs = []
def patched(c, x, top_y, width, gap, events, clef='treble', time_sig=(4,4),
            show_clef=True, show_time=True):
    key = tuple((e.get('pitch') or tuple(e.get('pitches',[])) or 'REST', e['dur'])
                for e in events)
    seqs.append((key, clef))
    return orig(c, x, top_y, width, gap, events, clef, time_sig, show_clef, show_time)
nt.draw_system = patched
# ... generar cada page1()/page2() de cada dosier, anotando a qué dosier
#     pertenece cada seqs[] añadida ...
# luego agrupar por (key, clef) y listar los grupos con más de un dosier distinto.
```

Si encuentras coincidencias, cambia el ORDEN de las notas o la duración de una
de las dos versiones (no hace falta rehacer el ejercicio entero).

### Verificación final por píxeles (después de generar el PDF)

```python
from PIL import Image
import numpy as np, subprocess

subprocess.run(['pdftoppm', '-jpeg', '-r', '120', 'dosier.pdf', '/tmp/pg'])
for f in sorted(glob.glob('/tmp/pg-*.jpg')):
    img = Image.open(f).convert('L')
    arr = np.array(img)
    mask = arr < 130
    dark = mask.sum(axis=1)
    rows = np.where(dark > 2)[0]
    last_row = rows.max()
    footer_expected = arr.shape[0] - 22 * (120/72.0)
    assert last_row <= footer_expected + 18, f'{f}: posible desborde inferior'
```

## Fallos ya corregidos — NO los repitas

Estos son bugs reales que aparecieron durante la construcción del motor y ya
están arreglados en el código de `engine/`. Si tocas el motor, no reintroduzcas
estos problemas:

1. **Plicas de corcheas emparejadas**: cuando dos corcheas de una misma barra
   están a distinta altura, TODAS las notas del grupo deben compartir una única
   dirección de plica (arriba/abajo) calculada sobre el grupo entero, y cada
   plica debe alargarse hasta tocar exactamente la altura de la barra (no una
   longitud fija por nota). Esto ya está resuelto en `draw_system` — no vuelvas
   a una lógica "una plica por nota calculada de forma independiente".
2. **Alteraciones**: el símbolo (♭/♯) no cambia la posición en el pentagrama,
   solo se dibuja al lado. `_abs_idx` ya ignora la alteración al calcular la
   línea/espacio — no dupliques esa lógica en otro sitio.
3. **Silencios**: usa los glifos de `FreeSerif` (`\U0001D13B`-`\U0001D13E`), NO
   existen en DejaVuSans. Ya están en `draw_rest`.
4. **Negra con puntillo (6/8 etc.)**: añade el `.` a la duración (`'q.'`) y usa
   el diccionario de duraciones extendido — no inventes una duración nueva sin
   añadirla también en `audit_suite.py`, o el auditor contará mal los tiempos.
5. **Presupuesto vertical**: antes de añadir un ejercicio extra "porque hay
   sitio", compruébalo con `build_fn` + contar la `y` final — el margen
   disponible en las páginas de ejercicios es ajustado (unas pocas decenas de
   puntos), no hay hueco de sobra.
6. **Texto largo en cajas de una sola línea**: cualquier texto que pueda variar
   en longitud (pistas, subtítulos con nombre de tonalidad, etc.) debe usar
   `wrap_text` con una caja de altura dinámica, nunca `drawString` a pelo — un
   texto más largo de lo previsto se sale del margen sin avisar.
7. **Nombres de acordes en prosa**: cuando transpongas o cambies contenido, los
   textos descriptivos ("a) Do se aleja y vuelve: Do-Sol-Do-Fa") NO se
   actualizan solos — revísalos a mano tras cualquier transposición.

## Convenciones de diseño (no las cambies sin que te lo pidan)

- Colores: `DARKGREEN` (marca/cabeceras), `MAROON` (clave de Fa / alertas),
  `GOLD` (estrellas de dificultad), `INK` (texto principal), `GRAY` (texto
  secundario), `LIGHTLINE` (separadores) — todos definidos en `notation.py`.
- Fuentes: `DejaVuSans`/`DejaVuSans-Bold` (texto), `DejaVuSerif-Bold` (títulos
  grandes), `FreeSerif` (claves musicales y silencios — nunca sustituir).
  Todas ya registradas al importar `notation`.
- Tamaño de página: A4 (`595.276 × 841.89` pt), márgenes `46pt`.
- Cada canción/alumno tiene un color de "nivel" si agrupas varios dosieres
  (verde=nivel 1, ocre=nivel 2, granate=nivel 3) — ajusta si tu sistema de
  niveles es distinto.

## Para 15 dosieres de alumnos nuevos

Cada alumno probablemente necesita una selección propia de canciones/ejercicios
según su nivel, no las mismas 20 de este álbum. El flujo recomendado por alumno:

1. Sesión corta y aislada por alumno (no arrastres el historial de otros).
2. Pide al principio: nombre del alumno, canción(es) o pieza(s) que vas a
   trabajar con él, y su nivel/dificultades específicas si las conoces.
3. Reutiliza `engine/` tal cual — es el motor genérico, no depende del álbum
   de Arnau.
4. Sigue el flujo de la sección "El flujo de trabajo completo" de arriba.
5. Antes de entregar: auditor de compases + auditor de texto + verificación de
   píxeles. Sin excepciones.
6. Si dos alumnos comparten alguna canción, comprueba duplicados de ejercicios
   entre sus dosieres (mismo escáner de la sección correspondiente) para que
   cada alumno reciba contenido realmente propio si eso importa en tu caso de
   uso; si no importa (dosieres para alumnos distintos, sin relación entre
   ellos), puedes omitir este paso.
