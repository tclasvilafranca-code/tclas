# -*- coding: utf-8 -*-
"""Hoja de AGUDEZA VISUAL: leer las notas en voz alta, sin tocar.

   Finalidad distinta a la del calentamiento, y eso cambia las reglas de
   diseño:

   - El calentamiento usa SECUENCIAS (una célula transportada) porque busca
     memoria muscular: la repetición es lo que entrena la mano.
   - La lectura necesita justo lo contrario: ANTI-SECUENCIA. Si las notas
     siguen un patrón, el alumno lo adivina y deja de leer. Aquí el orden es
     deliberadamente irregular y ninguna célula se repite.

   - Espaciado más generoso que en el calentamiento (5 compases por línea en
     vez de 6): leer en voz alta a primera vista pide más aire entre notas
     que repetir un patrón que ya conoces.
   - Sin digitaciones y sin acordes: una nota cada vez, para poder nombrarla.
   - Solo las figuras y el registro que aparecen en la partitura.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_system, draw_staff, draw_clef, note_y, draw_notehead
from page_layout_common import before_staff, after_system
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM,
                     INK, MUTED, ACCENT, _fit, _wrap)

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')

GAP = 6.3
BARS_PER_LINE = 5


def _ej_heading(c, y, num, titulo, pista):
    c.setFillColor(BLUE)
    c.roundRect(MARGIN, y - 13, 16, 16, 3, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 9)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 8, y - 9.5, str(num))
    c.setFont('DejaVuSans-Bold', 9.6)
    c.setFillColor(INK)
    c.drawString(MARGIN + 23, y - 9, titulo)
    tw = stringWidth(titulo, 'DejaVuSans-Bold', 9.6)
    psize = _fit(pista, 'DejaVuSans', 8.2, CONTENT_W - 23 - tw - 12, floor=6.4)
    c.setFont('DejaVuSans', psize)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 23 + tw + 12, y - 9, pista)
    return y - 22


def chuleta(c, y, pitches, nombres, gap=6.6):
    """Referencia: cada nota del registro de la pieza, con su nombre debajo.
       Sirve de apoyo las primeras semanas; luego se tapa con la mano."""
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, 'LAS NOTAS DE ESTA PARTITURA')
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.3)
    c.line(MARGIN, y - 5, MARGIN + 22, y - 5)
    y -= 20

    # la caja se dimensiona a partir de la nota mas grave: si se fija a ojo,
    # los nombres se montan encima de las notas de linea adicional
    staff_top = y - 11
    sx, sw = MARGIN + 16, CONTENT_W - 32
    bot = staff_top - gap * 4
    low = min(note_y(bot, gap, p, clef='treble') for p in pitches)
    label_y = min(low, bot) - gap * 1.9
    box_h = (y - label_y) + 9

    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - box_h, CONTENT_W, box_h, 4, fill=1, stroke=0)
    draw_staff(c, sx, staff_top, sw, gap=gap)
    draw_clef(c, sx + 3, bot, gap, clef='treble')
    # la clave de Sol ocupa mas de lo que parece: si las notas empiezan antes
    # de ~9 espacios, los nombres de debajo se montan encima del dibujo
    x0 = sx + gap * 9.4
    step = (sw - gap * 10.6) / max(len(pitches) - 1, 1)
    for i, (p, nm) in enumerate(zip(pitches, nombres)):
        cx = x0 + i * step
        cy = note_y(bot, gap, p, clef='treble')
        draw_notehead(c, cx, cy, gap, filled=True)
        if cy < bot:   # nota bajo el pentagrama: linea adicional
            c.setStrokeColor(NAVY)
            c.setLineWidth(1.0)
            c.line(cx - gap * 0.95, cy, cx + gap * 0.95, cy)
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(NAVY)
        c.drawCentredString(cx, label_y, nm)
    return y - box_h - 12


def _lineas(c, y, events, time_sig, bars_per_line=BARS_PER_LINE, gap=GAP):
    dur_beats = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 'q.': 1.5, 'h.': 3.0}
    bpb = time_sig[0] * (4.0 / time_sig[1])
    line_beats = bpb * bars_per_line
    lines, cur, acc = [], [], 0.0
    for e in events:
        cur.append(e)
        acc += dur_beats[e['dur']]
        if acc >= line_beats - 1e-6:
            lines.append(cur); cur, acc = [], 0.0
    if cur:
        lines.append(cur)
    for i, ln in enumerate(lines):
        y -= before_staff(gap, ln, 'treble')
        top, bot = draw_system(c, MARGIN, y, CONTENT_W, gap, ln, clef='treble',
                               time_sig=time_sig, show_time=(i == 0),
                               spacing='engraved')
        last = i == len(lines) - 1
        y = bot - (after_system(gap, ln, 'treble') if last else gap * 2.0)
    return y


def crono(c, y, titulo, intentos=3, w=None):
    """Casillas de tiempo: leer la misma línea varias veces y ver que cada
       vez se tarda menos es lo que de verdad engancha y mide la soltura."""
    w = w or CONTENT_W
    h = 40
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, w, h, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 13, y - 15, titulo.upper())
    bx = MARGIN + 13
    for i in range(1, intentos + 1):
        c.setFont('DejaVuSans', 7.6)
        c.setFillColor(MUTED)
        c.drawString(bx, y - 30, f'{i}ª vez')
        lw = 46
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.8)
        c.line(bx + 30, y - 31, bx + 30 + lw, y - 31)
        bx += 30 + lw + 26
    return y - h


def build_lectura(c, cfg):
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
    c.drawRightString(W - MARGIN, y, 'Agudeza visual · sin tocar el piano')
    y -= 28

    c.setFont('DejaVuSerif-Bold', 24)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, 'Agudeza visual')
    y -= 16
    y = _wrap(c, cfg['intro'], MARGIN, y, 'DejaVuSans', 9, CONTENT_W, 11.6, MUTED)
    y -= 8

    bh = 24
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - bh, CONTENT_W, bh, 4, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.rect(MARGIN, y - bh, 3, bh, fill=1, stroke=0)
    reglas = cfg['reglas']
    size = 8.2
    while size > 6.2 and (sum(stringWidth(r, 'DejaVuSans-Bold', size) for r in reglas)
                          + 26 * (len(reglas) - 1)) > CONTENT_W - 26:
        size -= 0.2
    rx = MARGIN + 13
    for i, r in enumerate(reglas):
        c.setFont('DejaVuSans-Bold', size)
        c.setFillColor(NAVY)
        c.drawString(rx, y - 15, r)
        rx += stringWidth(r, 'DejaVuSans-Bold', size)
        if i < len(reglas) - 1:
            c.setFillColor(BLUE)
            c.circle(rx + 13, y - 12, 1.8, fill=1, stroke=0)
            rx += 26
    y -= bh + 16

    y = chuleta(c, y, cfg['chuleta_pitches'], cfg['chuleta_nombres'])

    for ej in cfg['ejercicios']:
        y = _ej_heading(c, y, ej['num'], ej['titulo'], ej['pista'])
        y = _lineas(c, y, ej['events'], cfg['time_sig'],
                    bars_per_line=ej.get('bars_per_line', BARS_PER_LINE))
        y -= ej.get('extra_gap', 2)

    if cfg.get('crono'):
        y = crono(c, y, cfg['crono'])

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
    return y
