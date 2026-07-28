# -*- coding: utf-8 -*-
"""Hoja de CALENTAMIENTO: va delante de la partitura.

   Principios aplicados (ver ANALISIS_ESCRITURA_MUSICAL.md):
   - Densidad real: 6 compases por línea, ~21 pt por tiempo, que es el rango
     de una partitura publicada (12-32). Nada de 6 notas flotando.
   - Principio de SECUENCIA: cada ejercicio es una célula corta transportada
     grado a grado, no un puñado de notas sueltas. Así llena la línea con
     lógica musical y entrena la mano en todas las posiciones.
   - Todo sale de la pieza: mismo compás, misma clave (las dos manos en Sol
     sobre un solo pentagrama, como la edición), mismo dedo 2, y los mismos
     intervalos que la pieza abre (2ª, 3ª, 5ª).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_system
from page_layout_common import before_staff, after_system
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM,
                     INK, MUTED, ACCENT, _fit, _wrap)  # noqa

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')

GAP = 6.7
BARS_PER_LINE = 6


def _ej_heading(c, y, num, titulo, pista):
    """Cabecera compacta de ejercicio: badge + titulo + pista en una linea."""
    c.setFillColor(NAVY)
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


def _lineas(c, y, events, time_sig, bars_per_line=BARS_PER_LINE, gap=GAP):
    """Reparte los eventos en lineas densas de N compases, como una partitura
       real. Clave y compas al principio de cada linea (el compas solo en la
       primera)."""
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


def _rep(dyad, n, dur='q'):
    """Una célula repetida n veces (el gesto de 'picoteo' de la pieza)."""
    return [{'pitches': list(dyad), 'dur': dur} for _ in range(n)]


def _rep1(pitch, n, dur='q'):
    return [{'pitch': pitch, 'dur': dur} for _ in range(n)]


def build_calentamiento(c, cfg):
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
    c.drawRightString(W - MARGIN, y, 'Calentamiento · antes de la partitura')
    y -= 28

    c.setFont('DejaVuSerif-Bold', 24)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, 'Calentamiento')
    y -= 16
    c.setFont('DejaVuSans', 9)
    c.setFillColor(MUTED)
    y = _wrap(c, cfg['intro'], MARGIN, y, 'DejaVuSans', 9, CONTENT_W, 11.6, MUTED)
    y -= 8

    # tira de reglas fijas, en etiquetas separadas (una sola linea larga no
    # cabe en el ancho de la caja y se sale por la derecha)
    bh = 24
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - bh, CONTENT_W, bh, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
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
            c.setFillColor(ACCENT)
            c.circle(rx + 13, y - 12, 1.8, fill=1, stroke=0)
            rx += 26
    y -= bh + 16

    for ej in cfg['ejercicios']:
        y = _ej_heading(c, y, ej['num'], ej['titulo'], ej['pista'])
        y = _lineas(c, y, ej['events'], cfg['time_sig'],
                    bars_per_line=ej.get('bars_per_line', BARS_PER_LINE))
        y -= ej.get('extra_gap', 4)

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
    return y
