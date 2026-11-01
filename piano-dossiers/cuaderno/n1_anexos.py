# -*- coding: utf-8 -*-
"""Portada, paginas iniciales y anexos (chuleta, glosario, diario de practica, soluciones, pautas)."""
import os
from n1_base import *
from n1_base import _abs_idx
from reportlab.lib.colors import HexColor
from notation import draw_staff, draw_clef, draw_note
import n1_sep
from n1_sep import fig_celda
from n1_dic import GRADOS

ASSETS = os.path.join(HERE, '..', 'assets')

MESES = [('Septiembre', '1.er trimestre', 'Notación musical y figuras',
          'Leer las notas en clave de sol, conocer las figuras y los silencios y colocar bien las plicas.'),
         ('Octubre', '1.er trimestre', 'Líneas adicionales', 'Leer notas fuera del pentagrama y encontrar el Do central en las dos claves.'),
         ('Noviembre', '1.er trimestre', 'El teclado y su organización',
          'Moverte por el teclado, distinguir sostenidos, bemoles y becuadros y tocar una primera melodía.'),
         ('Diciembre', '1.er trimestre', 'Escala de Do mayor', 'Tocar y escribir la escala con su digitación, medir intervalos y crear una melodía.'),
         ('Enero', '2.º trimestre', 'Introducción a los compases', 'Sumar tiempos, completar compases y colocar barras.'),
         ('Febrero', '2.º trimestre', 'Ritmo y subdivisión', 'Partir cada tiempo en dos y en cuatro y leer ritmos con palabras.'),
         ('Marzo', '2.º trimestre', 'Trabajando en clave de fa', 'Leer las notas graves y tocar con la mano izquierda.'),
         ('Abril', '3.er trimestre', 'Recordamos los silencios', 'Usar los silencios en un compás y leer con pausas.'),
         ('Mayo', '3.er trimestre', 'La ligadura y el puntillo', 'Sumar duraciones con ligadura y puntillo y distinguir la ligadura de expresión.'),
         ('Junio', '3.er trimestre', 'Repaso final y gran concierto', 'Preparar una pieza, repasar todo y tocar delante de otros.')]


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
        c.drawImage(os.path.join(ASSETS, 'asset_logo_tclas.png'), W / 2 - 55, H - 190, 110, 110, mask='auto', preserveAspectRatio=True)
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
    c.drawCentredString(W / 2, 148, 'Explorador Musical')
    c.setFillColor(OCRE)
    c.setFont('DejaVuSans-Bold', 9.4)
    c.drawCentredString(W / 2, 130, 'NIVEL 1  ·  ADULTOS')
    c.setFillColor(INK)
    c.setFont('DejaVuSans', 10.4)
    c.drawString(MARGIN + 20, 88, 'Alumn@:')
    c.setStrokeColor(NAVY_SOFT)
    c.setLineWidth(0.7)
    c.line(MARGIN + 74, 86, W - MARGIN - 20, 86)
    c.showPage()


# ------------------------------------------------------------------ paginas iniciales
def inicio(d):
    d.nuevo('Cómo usar este cuaderno')
    d.add(banda_mes('Bienvenida', 'Curso 2026/27', 'Cómo usar este cuaderno',
                    'Un año de teoría y práctica para leer, escribir y tocar música con seguridad. Diez meses, diez temas.'))
    d.add(caja('dato', 'Cada mes, el mismo recorrido', [
        'Cada mes trabaja **un tema** y sigue siempre el mismo orden: primero la **teoría** (lo que necesitas saber), después los **ejercicios** '
        'escritos (para fijarlo con papel y lápiz) y, al final, una parte **al piano** (para llevarlo a las manos). '
        'Tu profesor te dirá qué ejercicios hacer en clase y cuáles en casa.']))
    d.add(h2('Las cajas que encontrarás'))
    d.add(tabla([120, 371], [
        [lambda c, cx, cy, w, h: (c.setFillColor(OCRE), c.circle(cx - 36, cy, 7, fill=1, stroke=0), c.setFillColor(BLANCO),
                                  c.setFont('DejaVuSans-Bold', 9), c.drawCentredString(cx - 36, cy - 3.2, '!'), c.setFillColor(OCRE),
                                  c.setFont('DejaVuSans-Bold', 7.4), c.drawString(cx - 25, cy - 2.6, 'TECLA AL DATO')),
         'La idea principal del tema, explicada en pocas líneas y con dibujos. Léela despacio antes de empezar los ejercicios.'],
        [lambda c, cx, cy, w, h: (c.setFillColor(NAVY), c.circle(cx - 36, cy, 7, fill=1, stroke=0), c.setFillColor(BLANCO),
                                  c.setFont('DejaVuSans-Bold', 9), c.drawCentredString(cx - 36, cy - 3.2, '♪'), c.setFillColor(NAVY),
                                  c.setFont('DejaVuSans-Bold', 7.4), c.drawString(cx - 25, cy - 2.6, 'TIP MUSICAL')),
         'Un consejo práctico para estudiar mejor o leer más rápido.'],
        [lambda c, cx, cy, w, h: (c.setFillColor(AZUL), c.circle(cx - 36, cy, 7, fill=1, stroke=0), c.setFillColor(BLANCO),
                                  c.setFont('DejaVuSans-Bold', 9), c.drawCentredString(cx - 36, cy - 3.2, 'i'), c.setFillColor(AZUL),
                                  c.setFont('DejaVuSans-Bold', 6.6), c.drawString(cx - 25, cy - 2.6, 'PARA SABER MÁS')),
         'Un dato extra que amplía el tema sin ser imprescindible.'],
        [lambda c, cx, cy, w, h: (c.setFillColor(VERDE), c.circle(cx - 36, cy, 7, fill=1, stroke=0), c.setFillColor(BLANCO),
                                  c.setFont('DejaVuSans-Bold', 9), c.drawCentredString(cx - 36, cy - 3.2, '♫'), c.setFillColor(VERDE),
                                  c.setFont('DejaVuSans-Bold', 7.4), c.drawString(cx - 25, cy - 2.6, 'AL PIANO')),
         'Práctica en el teclado: lo que acabas de aprender, tocado. No te lo saltes: la teoría solo se queda cuando pasa por las manos.'],
        [lambda c, cx, cy, w, h: (c.setFillColor(NAVY), c.circle(cx - 36, cy, 8, fill=1, stroke=0), c.setFillColor(BLANCO),
                                  c.setFont('DejaVuSerif-Bold', 9), c.drawCentredString(cx - 36, cy - 3.2, '1'), c.setFillColor(NAVY),
                                  c.setFont('DejaVuSans-Bold', 7.4), c.drawString(cx - 25, cy - 2.6, 'EJERCICIO')),
         'Lo que tienes que hacer, y **para qué sirve**. Muchos tienen varias respuestas válidas; los que tienen una sola están en el solucionario del final.'],
    ], ['Caja', 'Qué es'], alto=34, alin=['c', 'l'], size=9))
    d.add(h2('Cómo sacarle partido'))
    d.add(lista([
        '**Poco y a menudo.** Es mejor practicar un rato cada día (15–20 minutos) que una hora un solo día. Usa el **diario de práctica** del final.',
        '**Lápiz, no bolígrafo.** Los ejercicios se repiten: borra y vuelve a hacerlos hasta que salgan sin pensar.',
        '**Di las notas en voz alta** mientras lees y **cuenta el pulso** mientras tocas: es lo que más ayuda al principio.',
        '**Corrige tú mismo** con el solucionario después de intentarlo, no antes. Un error corregido por ti se olvida menos.',
        '**Si algo no sale**, bájalo a lo más pequeño (una nota, un compás, una mano) y sube de nuevo. En la página de junio tienes el método completo.',
    ], marca='▸', size=9.4, sep=4))


def calendario(d):
    d.nuevo('Calendario del curso')
    d.add(banda_mes('Calendario', '2026/27', 'Los diez temas del curso',
                    'Qué se trabaja cada mes y qué sabrás hacer al terminarlo. Marca la casilla cuando lo consigas.'))
    filas = []
    for mes, tri, tema, sabras in MESES:
        pg = d.prev.get(mes, '–')
        filas.append([mes, '**%s**\n%s' % (tema, sabras), lambda c, cx, cy, w, h: (c.setStrokeColor(NAVY), c.setLineWidth(0.9),
                                                                                  c.roundRect(cx - 5, cy - 5, 10, 10, 2, fill=0, stroke=1)), str(pg)])
    d.add(tabla([80, 320, 45, 46], filas, ['Mes', 'Tema y lo que sabrás hacer', '¿Lo sé?', 'Pág.'], alto=40, alin=['l', 'l', 'c', 'c'], size=8.4))
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
    ], ['Compás', 'Cabe', 'Cómo se cuenta'], alto=22, alin=['c', 'c', 'l'], size=8.8))
    d.add(tabla([120, 371], [
        ['Puntillo', 'Suma la mitad de la figura: blanca con puntillo = 3 tiempos; negra con puntillo = 1 ½.'],
        ['Ligadura de prolongación', 'Une dos notas del mismo sonido y suma sus tiempos.'],
        ['Ligadura de expresión', 'Une notas distintas: se tocan ligadas (legato), sin sumar tiempos.'],
        ['Silencio de redonda', 'Cuelga de la 4.ª línea; también vale para un compás entero de silencio.'],
        ['Silencio de blanca', 'Se apoya en la 3.ª línea.'],
    ], ['Signo', 'Qué hace'], alto=21, alin=['c', 'l'], size=8.8))
    d.add(h2('Escala de Do mayor, grados e intervalos'))
    d.add(tabla([70, 70, 70, 70, 70, 70, 71], [[str(g[0]) for g in GRADOS], [g[1] for g in GRADOS], [g[2] for g in GRADOS]], None, alto=22, size=7.0))
    d.add(par('Receta de la escala mayor: **T T S T T T S** (tono, tono, semitono…). Semitonos naturales: **Mi–Fa** y **Si–Do**. '
              'Intervalos: se cuentan **incluyendo las dos notas** (Do–Mi = 3.ª; Do–Sol = 5.ª). '
              'Alteraciones: **♯ sube** un semitono · **♭ baja** un semitono · **♮ anula** la alteración.', 9.2))


GLOSARIO = [
    ('Alteración', 'Signo (♯, ♭, ♮) que sube, baja o devuelve una nota a su sonido natural.'),
    ('Barra de compás', 'Línea vertical que separa un compás del siguiente.'),
    ('Becuadro (♮)', 'Anula una alteración anterior.'),
    ('Bemol (♭)', 'Baja la nota un semitono.'),
    ('Clave', 'Signo del principio del pentagrama que dice qué nota es cada línea (sol, fa).'),
    ('Compás', 'Unidad de medida del tiempo; contiene un número fijo de tiempos.'),
    ('Corchea', 'Figura que dura medio tiempo (en un compás con negra = 1).'),
    ('Digitación', 'Los números de dedo con los que se toca (1 = pulgar … 5 = meñique).'),
    ('Escala', 'Sucesión de notas ordenadas por grados (por ejemplo, Do–Re–Mi–Fa–Sol–La–Si–Do).'),
    ('Figura', 'Signo que indica la duración de un sonido.'),
    ('Grado', 'Lugar que ocupa una nota dentro de la escala (I, II, III…).'),
    ('Intervalo', 'Distancia entre dos notas, contando las dos (3.ª, 5.ª…).'),
    ('Legato', 'Tocar ligado, sin cortar el sonido entre las notas.'),
    ('Ligadura', 'Arco que une notas: de prolongación (mismo sonido) o de expresión (distintos).'),
    ('Línea adicional', 'Trazo corto que prolonga el pentagrama hacia arriba o abajo.'),
    ('Octava', 'Distancia de ocho notas: de un Do al siguiente Do.'),
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
    ('Tónica', 'Primera nota de una escala; la nota «de casa».'),
    ('Tono', 'Distancia de dos semitonos.'),
]


def glosario(d):
    d.nuevo('Anexo · Glosario')
    d.add(banda_mes('Anexo', 'Consulta rápida', 'Glosario', 'Las palabras del curso, por orden alfabético.'))
    for i in range(0, len(GLOSARIO), 7):
        d.add(tabla([130, 361], [[a, b] for a, b in GLOSARIO[i:i + 7]], None, alto=24, alin=['l', 'l'], size=8.6, zebra=(i // 7) % 2 == 0 or True))


# ------------------------------------------------------------------ diario de practica
def diario(d):
    for k, (tri, meses) in enumerate([('1.er trimestre', 'Septiembre – Diciembre'), ('2.º trimestre', 'Enero – Marzo'), ('3.er trimestre', 'Abril – Junio')]):
        d.nuevo('Anexo · Diario de práctica')
        d.add(banda_mes('Diario', tri, 'Diario de práctica',
                        meses + '. Marca con ✓ cada día que practiques, apunta los minutos de la semana y una cosa que te haya costado o que hayas mejorado.'))

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
