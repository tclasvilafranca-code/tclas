# -*- coding: utf-8 -*-
"""Hojas de TRABAJO AL PIANO: la partitura desmontada y vuelta a montar.

   Las tres hojas anteriores preparan; esta es la única que trabaja la pieza:

   - El CALENTAMIENTO entrena la mano con secuencias inventadas a partir de
     la pieza. La AGUDEZA VISUAL entrena el ojo sin tocar. Ninguna de las dos
     toca la partitura de verdad.
   - Aquí el material NO se inventa: cada ejercicio es un trozo literal de la
     partitura, aislado. El método es el de cualquier profesor con oficio:

         AISLAR   -> sacar el trozo que falla, solo
         REDUCIR  -> quitarle el relleno y dejar la dificultad desnuda
         REINSERTAR -> devolverlo a su sitio y comprobar que ya está resuelto

   El error clásico de un cuaderno de ejercicios es quedarse en 'aislar'. Sin
   el paso de reinsertar, el alumno acaba tocando ejercicios muy bien y la
   pieza igual de mal. Por eso cada bloque acaba volviendo a la partitura.

   La velocidad no se trabaja tocando rápido, sino subiendo escalones con una
   regla: solo subes cuando sale dos veces seguidas sin parar. De ahí el
   bloque de la escalera de tempo, que es papel, no pentagrama, y es lo que
   de verdad se usa en casa entre semana.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_system
from page_layout_common import before_staff, after_system
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM,
                     INK, MUTED, ACCENT, _fit, _wrap)

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')
WARM = HexColor('#F4EFE3')

# Pentagrama mas alto que en las hojas de lectura: aqui el alumno esta al
# piano, mirando de lejos y con las manos ocupadas, no con la hoja en la mano.
GAP = 7.4
BARS_PER_LINE = 4
DUR = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 'q.': 1.5, 'h.': 3.0}


def _ej_heading(c, y, num, titulo, pista):
    c.setFillColor(ACCENT)
    c.roundRect(MARGIN, y - 13, 16, 16, 3, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 9)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 8, y - 9.5, str(num))
    c.setFont('DejaVuSans-Bold', 9.6)
    c.setFillColor(INK)
    c.drawString(MARGIN + 23, y - 9, titulo)
    tw = stringWidth(titulo, 'DejaVuSans-Bold', 9.6)
    psize = _fit(pista, 'DejaVuSans', 8.2, CONTENT_W - 23 - tw - 12, floor=6.2)
    c.setFont('DejaVuSans', psize)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 23 + tw + 12, y - 9, pista)
    return y - 21


def _lineas(c, y, events, time_sig, bars_per_line, gap=GAP, show_time=True):
    bpb = time_sig[0] * (4.0 / time_sig[1])
    line_beats = bpb * bars_per_line
    lines, cur, acc = [], [], 0.0
    for e in events:
        cur.append(e)
        acc += DUR[e['dur']]
        if acc >= line_beats - 1e-6:
            lines.append(cur); cur, acc = [], 0.0
    if cur:
        lines.append(cur)
    for i, ln in enumerate(lines):
        y -= before_staff(gap, ln, 'treble')
        top, bot = draw_system(c, MARGIN, y, CONTENT_W, gap, ln, clef='treble',
                               time_sig=time_sig, show_time=(i == 0 and show_time),
                               spacing='engraved')
        last = i == len(lines) - 1
        y = bot - (after_system(gap, ln, 'treble') if last else gap * 2.0)
    return y


def _caption(c, y, texto):
    """Rotulo de un sistema concreto dentro de un ejercicio (a, b, c...)."""
    if not texto:
        return y
    size = _fit(texto, 'DejaVuSans-Bold', 7.8, CONTENT_W, floor=6.4)
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y - 7, texto)
    return y - 12


def nota_clave(c, y, texto, etiqueta='LA CLAVE DE TODO'):
    """Caja destacada: la idea que hace que el ejercicio funcione. Va aparte
       de la 'pista' porque no es una instrucción, es el porqué."""
    size = 8.0
    inner = CONTENT_W - 26
    # medir cuantas lineas ocupa para dimensionar la caja antes de pintarla
    words, ln, count = texto.split(), '', 1
    for wd in words:
        t = (ln + ' ' + wd).strip()
        if stringWidth(t, 'DejaVuSans', size) > inner:
            count += 1; ln = wd
        else:
            ln = t
    h = 20 + count * 10.6
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 7.2)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + 13, y - 12, etiqueta)
    _wrap(c, texto, MARGIN + 13, y - 24, 'DejaVuSans', size, inner, 10.6, NAVY)
    return y - h - 10


def escalera_tempo(c, y, valores, regla, titulo='LA ESCALERA DE TEMPO'):
    """Los escalones de velocidad, con dos casillas por escalón. Subir de
       escalón solo cuando salga DOS veces seguidas sin parar: sin esa regla
       escrita, el alumno sube en cuanto le sale una vez y se atasca."""
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, titulo)
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.3)
    c.line(MARGIN, y - 5, MARGIN + 22, y - 5)
    y -= 14

    n = len(valores)
    rise, bh, sep = 8.5, 32, 5
    bw = (CONTENT_W - sep * (n - 1)) / n
    base = y - bh - (n - 1) * rise
    for i, v in enumerate(valores):
        bx = MARGIN + i * (bw + sep)
        by = base + i * rise
        c.setFillColor(PANEL)
        c.roundRect(bx, by, bw, bh, 3, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.rect(bx, by + bh - 2.6, bw, 2.6, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 9.2)
        c.setFillColor(NAVY)
        c.drawCentredString(bx + bw / 2, by + 19, '♩=%d' % v)
        for k in range(2):
            sx = bx + bw / 2 - 10.5 + k * 13
            c.setStrokeColor(NAVY_SOFT)
            c.setLineWidth(0.9)
            c.setFillColor(white)
            c.rect(sx, by + 6, 8, 8, fill=1, stroke=1)
    y = base - 13
    size = _fit(regla, 'DejaVuSans-Bold', 8.0, CONTENT_W, floor=6.4)
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN, y, regla)
    return y - 12


def tracker(c, y, titulo, pie, dias=('L', 'M', 'X', 'J', 'V', 'S', 'D')):
    """Registro de la semana: una casilla por día. Es lo que convierte la hoja
       en algo que se usa en casa y no solo en clase."""
    h = 46
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 13, y - 14, titulo.upper())
    c.setFont('DejaVuSans', 7.2)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 13, y - 39, pie)

    bx = W - MARGIN - 13 - (len(dias) * 26 - 8)
    for d in dias:
        c.setFont('DejaVuSans-Bold', 6.8)
        c.setFillColor(MUTED)
        c.drawCentredString(bx + 9, y - 13, d)
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.9)
        c.setFillColor(white)
        c.rect(bx, y - 33, 18, 16, fill=1, stroke=1)
        bx += 26
    return y - h - 10


def build_piano(c, cfg):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, cfg['kicker'].upper())
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, cfg['esquina'])
    y -= 28

    c.setFont('DejaVuSerif-Bold', 24)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, cfg['titulo'])
    y -= 16
    y = _wrap(c, cfg['intro'], MARGIN, y, 'DejaVuSans', 9, CONTENT_W, 11.6, MUTED)
    y -= 8

    bh = 24
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - bh, CONTENT_W, bh, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - bh, 3, bh, fill=1, stroke=0)
    reglas = cfg['reglas']
    size = 8.2
    while size > 6.0 and (sum(stringWidth(r, 'DejaVuSans-Bold', size) for r in reglas)
                          + 24 * (len(reglas) - 1)) > CONTENT_W - 26:
        size -= 0.2
    rx = MARGIN + 13
    for i, r in enumerate(reglas):
        c.setFont('DejaVuSans-Bold', size)
        c.setFillColor(NAVY)
        c.drawString(rx, y - 15, r)
        rx += stringWidth(r, 'DejaVuSans-Bold', size)
        if i < len(reglas) - 1:
            c.setFillColor(ACCENT)
            c.circle(rx + 12, y - 12, 1.8, fill=1, stroke=0)
            rx += 24
    y -= bh + 14

    for blq in cfg['bloques']:
        tipo = blq.get('tipo', 'ej')
        if tipo == 'ej':
            y = _ej_heading(c, y, blq['num'], blq['titulo'], blq['pista'])
            for s in blq['sistemas']:
                y = _caption(c, y, s.get('cap'))
                y = _lineas(c, y, s['events'], cfg['time_sig'],
                            s.get('bars', BARS_PER_LINE),
                            gap=s.get('gap', cfg.get('gap', GAP)),
                            show_time=s.get('show_time', True))
            y -= blq.get('extra_gap', 3)
        elif tipo == 'nota':
            y = nota_clave(c, y, blq['texto'], blq.get('etiqueta', 'LA CLAVE DE TODO'))
        elif tipo == 'escalera':
            y = escalera_tempo(c, y, blq['valores'], blq['regla'])
        elif tipo == 'tracker':
            y = tracker(c, y, blq['titulo'], blq['pie'])

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
    return y
