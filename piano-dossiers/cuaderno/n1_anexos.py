# -*- coding: utf-8 -*-
"""Portada, paginas iniciales y anexos (chuleta, glosario, diario de practica, soluciones, pautas)."""
import os
from n1_base import *
from n1_base import _abs_idx
from reportlab.lib.colors import HexColor
from notation import draw_staff, draw_clef, draw_note
from n1_comun import fig_celda
from n1_feb import GRADOS

ASSETS = os.path.join(HERE, '..', 'assets')

MESES = [('Noviembre', 'Etapa 1', 'Fundamentos del piano', 'Postura, numeración de los dedos, teclado, pentagrama y lectura desde el Do y el Fa.'),
         ('Diciembre', 'Etapa 1', 'Figuras, silencios y compás', 'Valor de las figuras y silencios, puntillo, compases 2/4, 3/4 y 4/4.'),
         ('Enero', 'Etapa 1', 'Notas adicionales', 'Leer fuera del pentagrama, el Do central y la velocidad de lectura en las dos claves.'),
         ('Febrero', 'Etapa 2', 'Escala de Do mayor', 'Tonos, semitonos y alteraciones; escala con digitación; grados e intervalos.'),
         ('Marzo', 'Etapa 2', 'Ritmo y subdivisión', 'Lectura rítmica, ligadura de prolongación, puntillo y compás de 6/8.'),
         ('Abril', 'Etapa 2', 'Clave de fa y manos juntas', 'Leer el registro grave y coordinar las dos manos sobre el sistema de piano.'),
         ('Mayo', 'Etapa 3', 'Armaduras: Sol y Fa mayor', 'Construir escalas con alteraciones y reconocer tonalidades; Minueto en Sol.'),
         ('Junio', 'Etapa 3', 'Acordes y acompañamiento', 'Tríadas mayores y menores, cifrado y la cadencia I – IV – V – I.'),
         ('Julio', 'Etapa 3', 'Expresión y repaso final', 'Dinámica, tempo y articulación; revisión del curso y recital.')]


# ------------------------------------------------------------------ portada
def portada(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.rect(MARGIN * 0.62, MARGIN * 0.62, W - MARGIN * 1.24, H - MARGIN * 1.24, fill=0, stroke=1)
    c.setFillColor(NAVY)
    c.rect(18, H - 24, W - 36, 6, fill=1, stroke=0)
    try:
        c.drawImage(os.path.join(ASSETS, 'asset_logo_tclas_v2.png'), W / 2 - 55, H - 190, 110, 110, mask='auto', preserveAspectRatio=True)
    except Exception:
        pass
    c.setFillColor(OCRE)
    c.setFont('DejaVuSans-Bold', 10)
    c.drawCentredString(W / 2, H - 214, 'CURSO 2026 / 27')
    c.setFillColor(NAVY)
    c.setFont('DejaVuSerif-Bold', 38)
    c.drawCentredString(W / 2, H - 275, 'Mi cuaderno')
    c.setFont('DejaVuSerif-Bold', 38)
    c.drawCentredString(W / 2, H - 322, 'de piano')
    c.setStrokeColor(OCRE)
    c.setLineWidth(1.4)
    c.line(W / 2 - 40, H - 340, W / 2 + 40, H - 340)
    # pentagrama con la escala de Do
    g = 9.0
    xs, ws = MARGIN + 20, W - 2 * MARGIN - 40
    ys = draw_staff(c, xs, H - 400, ws, g)
    draw_clef(c, xs + 4, ys[-1], g, 'treble')
    esc = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    paso = (ws - 60) / 8.0
    for k, p in enumerate(esc):
        draw_note(c, xs + 56 + paso * (k + 0.5), ys[-1], ys[0], g, p, 'q', clef='treble')
    # teclado
    teclado(c, MARGIN, 190, W - 2 * MARGIN, 120, desde=('C', 4), n_blancas=15, do_central=False)
    c.setFillColor(NAVY)
    c.setFont('DejaVuSerif-Bold', 16)
    c.drawCentredString(W / 2, 148, 'Curso de piano · noviembre – julio')
    c.setFillColor(OCRE)
    c.setFont('DejaVuSans-Bold', 9.4)
    c.drawCentredString(W / 2, 130, 'NIVEL 1  ·  ADULTOS')
    c.setFillColor(INK)
    c.setFont('DejaVuSans', 10.4)
    c.drawString(MARGIN + 20, 88, 'Alumn@:')
    c.setFont('DejaVuSerif-Bold', 15)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 80, 91, os.environ.get('N1_ALUMNO', ''))
    c.setStrokeColor(NAVY_SOFT)
    c.setLineWidth(0.7)
    c.line(MARGIN + 74, 86, W - MARGIN - 20, 86)
    c.showPage()


# ------------------------------------------------------------------ paginas iniciales
def inicio(d):
    d.nuevo('Cómo usar este cuaderno')
    d.add(banda_mes('Presentación', 'Curso 2026/27', 'Cómo usar este cuaderno',
                    'Un curso de nueve meses, de noviembre a julio, que lleva de cero a leer partituras sencillas en las dos claves y tocarlas con las dos manos.'))
    d.add(caja('dato', 'Estructura de cada mes', [
        'Cada mes desarrolla un tema siguiendo el mismo orden: primero el **concepto** (lo imprescindible, explicado con precisión), después los **ejercicios** escritos '
        '(que fijan lo aprendido y se corrigen con el solucionario) y, por último, la parte **al piano**, donde el concepto se lleva a las manos. '
        'El ritmo está pensado para un adulto que aprende con rapidez: el profesor indicará en clase qué ejercicios se hacen en casa.']))
    d.add(h2('Elementos de cada página'))
    d.add(tabla([130, 361], [
        ['**Concepto**', 'La idea principal del tema, expuesta con las definiciones exactas. Conviene leerla antes de hacer los ejercicios.'],
        ['**Consejo de estudio**', 'Una recomendación práctica de método o de técnica.'],
        ['**Ampliación**', 'Un dato complementario que enriquece el tema sin ser imprescindible para seguir.'],
        ['**Al piano**', 'Práctica en el teclado: ejercicios técnicos y piezas. La teoría se consolida cuando pasa por las manos.'],
        ['**Ejercicio**', 'Numerado, con lo que hay que hacer y su **objetivo**. Las soluciones están al final, con el criterio cuando hay varias respuestas válidas.'],
    ], ['Elemento', 'Función'], alto=32, alin=['l', 'l'], size=9))
    d.add(h2('Recomendaciones de estudio'))
    d.add(lista([
        '**Regularidad.** Diez a veinte minutos diarios rinden más que una sesión larga una vez por semana. El **diario de práctica** del final sirve para llevar el control.',
        '**Lápiz.** Los ejercicios se repiten; borra y rehaz hasta que salgan sin dudar.',
        '**Voz y pulso.** Nombra las notas en voz alta al leer y cuenta el pulso al tocar: es el hábito que más acelera el aprendizaje de la lectura.',
        '**Corrección posterior.** Intenta cada ejercicio antes de mirar la solución; un error detectado por uno mismo se fija mejor.',
        '**Lo difícil, en pequeño.** Si un pasaje no sale, redúcelo (una mano, un compás, más lento) y amplíalo después: el método completo está en julio.',
    ], marca='▸', size=9.4, sep=4))


def calendario(d):
    d.nuevo('Calendario del curso')
    d.add(banda_mes('Calendario', '2026/27', 'Los nueve temas del curso',
                    'Qué se trabaja cada mes. Marca la casilla cuando lo domines.'))
    filas = []
    for mes, tri, tema, sabras in MESES:
        pg = d.prev.get(mes, '–')
        filas.append([mes + '\n' + tri, '**%s**\n%s' % (tema, sabras), lambda c, cx, cy, w, h: (c.setStrokeColor(NAVY), c.setLineWidth(0.9),
                                                                                  c.roundRect(cx - 5, cy - 5, 10, 10, 2, fill=0, stroke=1)), str(pg)])
    d.add(tabla([80, 320, 45, 46], filas, ['Mes', 'Tema y contenidos', '¿Lo domino?', 'Pág.'], alto=44, alin=['l', 'l', 'c', 'c'], size=8.4))
    d.add(h2('Mi punto de partida y mis objetivos'))
    d.add(par('Escribe aquí con qué ganas empiezas, qué esperas conseguir al acabar el curso y qué pieza te gustaría tocar:', 9.2),
          lineas_escribir(4, None, 21))


# ------------------------------------------------------------------ chuleta
def chuleta(d):
    d.nuevo('Anexo · Chuleta de consulta')
    d.add(banda_mes('Anexo', 'Consulta rápida', 'Chuleta de notas y teclado',
                    'Para tener a mano cuando dudes: dónde está cada nota en el pentagrama y en el teclado.'))
    tr = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
    bs = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4']
    nm = lambda ps: [nombre(p) for p in ps]
    d.add(fila_notas('treble', tr, 'w', bajo=nm(tr), titulo='CLAVE DE SOL · del Do central al Do agudo (mano derecha)'),
          bloque_teclado(h=64, desde=('C', 4), n_blancas=15, etiqueta_blancas=True, do_central=True),
          fila_notas('bass', bs, 'w', bajo=nm(bs), titulo='CLAVE DE FA · del Do grave al Do central (mano izquierda)'),
          bloque_teclado(h=64, desde=('C', 2), n_blancas=15, etiqueta_blancas=True))
    d.add(caja('tip', 'Claves para recordar', [
        '**Sol:** líneas Mi – Sol – Si – Re – Fa · espacios Fa – La – Do – Mi.   **Fa:** líneas Sol – Si – Re – Fa – La · espacios La – Do – Mi – Sol.',
        'El **Do central** es la nota que comparten las dos claves, la tecla blanca a la izquierda del grupo de dos negras del medio del teclado.']))
    d.nuevo()
    d.add(banda_mes('Anexo', 'Consulta rápida', 'Chuleta de figuras y compases', 'Valores, silencios, puntillo y cómo se cuenta cada compás.'))
    d.add(tabla([80, 110, 80, 110, 111], [[fig_celda(x), NOM_FIG[x], FIG[x][4], fig_celda(x, True), NOM_SIL[x].replace('Silencio de ', '')] for x in ['w', 'h', 'q', 'e', 's', 'f', 'g']],
                ['Figura', 'Nombre', 'Dura', 'Silencio', 'del/de la'], alto=32, size=8.6))
    d.add(tabla([100, 90, 301], [
        ['2/4', 'dos negras', '1–2 · primer tiempo fuerte, segundo débil'],
        ['3/4', 'tres negras', '1–2–3 · fuerte, débil, débil (vals)'],
        ['4/4 o C', 'cuatro negras', '1–2–3–4 · fuerte, débil, semifuerte, débil'],
    ], ['Compás', 'Cabe', 'Cómo se cuenta'], alto=19, alin=['c', 'c', 'l'], size=8.8))
    d.add(tabla([120, 371], [
        ['Puntillo', 'Suma la mitad de la figura: blanca con puntillo = 3 tiempos; negra con puntillo = 1 ½.'],
        ['Ligadura de prolongación', 'Une dos notas del mismo sonido y suma sus tiempos.'],
        ['Ligadura de expresión', 'Une notas distintas: se tocan ligadas (legato), sin sumar tiempos.'],
        ['Silencio de redonda', 'Cuelga de la 4.ª línea; también vale para un compás entero de silencio.'],
        ['Silencio de blanca', 'Se apoya en la 3.ª línea.'],
    ], ['Signo', 'Qué hace'], alto=19, alin=['c', 'l'], size=8.8))
    d.add(h2('Escala de Do mayor, grados e intervalos'))
    d.add(par('Receta de la escala mayor: **T T S T T T S** (tono, tono, semitono…). Semitonos naturales: **Mi–Fa** y **Si–Do**. '
              'Grados: **I** tónica · **IV** subdominante · **V** dominante · **VII** sensible. '
              'Intervalos: se cuentan **incluyendo las dos notas** (Do–Mi = 3.ª; Do–Sol = 5.ª). '
              'Alteraciones: **♯ sube** un semitono · **♭ baja** un semitono · **♮ anula** la alteración.', 9.2))


GLOSARIO = [
    ('Acorde', 'Conjunto de tres o más sonidos simultáneos; el más sencillo es la tríada.'),
    ('Alteración', 'Signo (♯, ♭, ♮) que sube, baja o devuelve una nota a su sonido natural.'),
    ('Armadura', 'Alteraciones escritas tras la clave que afectan a toda la pieza y definen la tonalidad.'),
    ('Barra de compás', 'Línea vertical que separa un compás del siguiente.'),
    ('Becuadro (♮)', 'Anula una alteración anterior.'),
    ('Bemol (♭)', 'Baja la nota un semitono.'),
    ('Clave', 'Signo del principio del pentagrama que dice qué nota es cada línea (sol, fa).'),
    ('Cadencia', 'Fórmula de acordes que da sensación de pausa o de final (por ejemplo, I – IV – V – I).'),
    ('Cifrado', 'Sistema de letras (C, Dm, G…) para indicar los acordes.'),
    ('Compás', 'Unidad de medida del tiempo; contiene un número fijo de tiempos.'),
    ('Corchea', 'Figura que dura medio tiempo (en un compás con negra = 1).'),
    ('Digitación', 'Los números de dedo con los que se toca (1 = pulgar … 5 = meñique).'),
    ('Dinámica', 'Grados de intensidad del sonido (pp, p, mf, f, ff) y sus cambios (crescendo, diminuendo).'),
    ('Escala', 'Sucesión de notas ordenadas por grados (por ejemplo, Do–Re–Mi–Fa–Sol–La–Si–Do).'),
    ('Figura', 'Signo que indica la duración de un sonido.'),
    ('Grado', 'Lugar que ocupa una nota dentro de la escala (I, II, III…).'),
    ('Intervalo', 'Distancia entre dos notas, contando las dos (3.ª, 5.ª…).'),
    ('Legato', 'Tocar ligado, sin cortar el sonido entre las notas.'),
    ('Ligadura', 'Arco que une notas: de prolongación (mismo sonido) o de expresión (distintos).'),
    ('Línea adicional', 'Trazo corto que prolonga el pentagrama hacia arriba o abajo.'),
    ('Octava', 'Distancia de ocho notas: de un Do al siguiente Do.'),
    ('Staccato', 'Articulación que separa las notas, tocándolas cortas.'),
    ('Pentagrama', 'Cinco líneas y cuatro espacios sobre los que se escribe la música.'),
    ('Plica', 'Rayita vertical que sale de la cabeza de una nota.'),
    ('Pulso', 'Latido constante de la música.'),
    ('Puntillo', 'Punto que alarga una figura la mitad de su valor.'),
    ('Ritmo', 'Combinación de duraciones sobre el pulso.'),
    ('Semitono', 'La distancia más pequeña entre dos teclas vecinas del piano.'),
    ('Silencio', 'Signo que indica una pausa con una duración determinada.'),
    ('Sostenido (♯)', 'Sube la nota un semitono.'),
    ('Subdivisión', 'Partir un tiempo en partes iguales (dos corcheas, cuatro semicorcheas…).'),
    ('Tempo', 'La velocidad de la música (por ejemplo, ♩ = 60 pulsos por minuto).'),
    ('Tiempo', 'Cada uno de los golpes de pulso de un compás.'),
    ('Tónica', 'Primera nota de una escala y centro de la tonalidad.'),
    ('Tonalidad', 'Conjunto de notas y relaciones organizadas en torno a una tónica (Do mayor, Sol mayor…).'),
    ('Tríada', 'Acorde de tres notas superpuestas por terceras: fundamental, tercera y quinta.'),
    ('Tono', 'Distancia de dos semitonos.'),
]


def glosario(d):
    d.nuevo('Anexo · Glosario')
    d.add(banda_mes('Anexo', 'Consulta rápida', 'Glosario', 'Las palabras del curso, por orden alfabético.'))
    mitad = (len(GLOSARIO) + 1) // 2
    d.add(tabla([130, 361], [[a, b] for a, b in GLOSARIO[:mitad]], None, alto=21, alin=['l', 'l'], size=8.4))
    d.add(tabla([130, 361], [[a, b] for a, b in GLOSARIO[mitad:]], None, alto=21, alin=['l', 'l'], size=8.4))


# ------------------------------------------------------------------ diario de practica
def diario(d):
    for k, (tri, meses) in enumerate([('Etapa 1', 'Noviembre – Enero'), ('Etapa 2', 'Febrero – Abril'), ('Etapa 3', 'Mayo – Julio')]):
        d.nuevo('Anexo · Diario de práctica')
        d.add(banda_mes('Diario', tri, 'Diario de práctica',
                        meses + '. Marca con ✓ cada día que practiques, anota los minutos de la semana y una cosa que hayas mejorado o que te haya costado.'))

        def tab(c, x, y, w):
            filas = 13
            rh = 40
            cw = [34] + [20] * 7 + [40, 277]
            c.setFillColor(NAVY)
            c.roundRect(x, y - 18, w, 18, 3, fill=1, stroke=0)
            xx = x
            for t, wc in zip(['Sem.', 'L', 'M', 'X', 'J', 'V', 'S', 'D', 'Min.', 'Lo que he mejorado / lo que me ha costado'], cw):
                c.setFillColor(BLANCO)
                c.setFont('DejaVuSans-Bold', 7.4)
                c.drawCentredString(xx + wc / 2, y - 12.4, t)
                xx += wc
            for r in range(filas):
                yy = y - 18 - (r + 1) * rh + rh
                if r % 2 == 0:
                    c.setFillColor(PANEL)
                    c.rect(x, yy - rh, w, rh, fill=1, stroke=0)
                c.setStrokeColor(RULE)
                c.setLineWidth(0.5)
                c.line(x, yy - rh, x + w, yy - rh)
                c.setFillColor(NAVY)
                c.setFont('DejaVuSans-Bold', 8.4)
                c.drawCentredString(x + 17, yy - rh / 2 - 3, str(r + 1))
                xx = x + 34
                for j in range(7):
                    c.setStrokeColor(NAVY_SOFT)
                    c.setLineWidth(0.7)
                    c.roundRect(xx + 4, yy - rh / 2 - 6, 12, 12, 2, fill=0, stroke=1)
                    xx += 20
                c.setStrokeColor(RULE)
                c.line(xx + 6, yy - rh / 2 - 6, xx + 34, yy - rh / 2 - 6)
                c.line(xx + 46, yy - rh + 12, x + w - 8, yy - rh + 12)
                c.line(xx + 46, yy - rh + 26, x + w - 8, yy - rh + 26)
        d.add(Blk(18 + 13 * 40 + 6, tab))


# ------------------------------------------------------------------ soluciones
def soluciones(d):
    d.nuevo('Anexo · Soluciones')
    d.add(banda_mes('Anexo', 'Solucionario', 'Soluciones de los ejercicios',
                    'Compara después de haberlo intentado. En los ejercicios con varias respuestas válidas se da una posibilidad o el criterio.'))
    actual = None
    for mes, num, titulo, ls in SOLUCIONES:
        if mes != actual:
            actual = mes
            d.add(h2(mes))
        d.add(par('**%s · %s**' % (num if isinstance(num, str) else 'Ej. %s' % num, titulo), 8.8, NAVY, despues=1))
        for t in ls:
            d.add(par(t, 8.3, INK, despues=2, sangria=8))


# ------------------------------------------------------------------ pautas
def pautas(d):
    d.nuevo('Anexo · Papel pautado')
    d.add(banda_mes('Anexo', 'Para escribir', 'Papel pautado', 'Pentagramas vacíos para copiar, componer y hacer dictados.'))
    for k in range(6):
        d.add(pauta_vacia('treble', 4, None))
    d.nuevo()
    for k in range(3):
        d.add(pauta_piano_vacia(4, None))
    d.nuevo()
    for k in range(4):
        d.add(pauta_vacia('bass', 4, None), pauta_vacia('treble', 4, None))
