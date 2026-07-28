# -*- coding: utf-8 -*-
"""Ficha de información de una partitura: la hoja que va justo detrás de la
   partitura. Esquemática y visual — nada de prosa larga.

   Bloques:
     1. Cabecera + tira de datos (tonalidad, compás, nº de compases, carácter)
     2. MAPA DE LA PIEZA — barra segmentada con las secciones reales
     3. DÓNDE VAN LAS MANOS — teclado dibujado con las teclas de arranque
     4. LO ESPECIAL DE ESTA PARTITURA — los hechos concretos de ESTA edición
     5. EL RETO / EL TRUCO
     6. ¿SABÍAS QUE?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_system
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)

BLUE = HexColor('#3E6E8F')
WARM = HexColor('#F4EFE3')
PANEL = HexColor('#F3F1EA')

WHITE_SEQ = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
BLACK_AFTER = {0, 1, 3, 4, 5}   # hay tecla negra tras Do, Re, Fa, Sol, La


def draw_keyboard(c, x, y_top, n_white, kw, kh, marks=None, start_idx=0):
    """Teclado esquemático.
       marks: {indice_blanca_global: (color, etiqueta, nivel)} — el nivel
       (0, 1, ...) escalona la etiqueta hacia arriba para que dos teclas
       vecinas no solapen sus rótulos."""
    marks = marks or {}
    bw, bh = kw * 0.60, kh * 0.62

    for i in range(n_white):
        gi = start_idx + i
        kx = x + i * kw
        col = marks.get(gi, (None, None, 0))[0]
        c.setFillColor(col if col else white)
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.8)
        c.rect(kx, y_top - kh, kw, kh, fill=1, stroke=1)
        name = WHITE_SEQ[gi % 7]
        c.setFont('DejaVuSans-Bold' if col else 'DejaVuSans', 6.6)
        c.setFillColor(white if col else MUTED)
        c.drawCentredString(kx + kw / 2, y_top - kh + 6, name)

    for i in range(n_white):
        gi = start_idx + i
        if (gi % 7) in BLACK_AFTER and i < n_white - 1:
            bx = x + (i + 1) * kw - bw / 2
            c.setFillColor(NAVY)
            c.setStrokeColor(NAVY)
            c.setLineWidth(0.6)
            c.rect(bx, y_top - bh, bw, bh, fill=1, stroke=1)

    # Rotulos: se desplazan lateralmente (dx) para que dos teclas vecinas no
    # solapen, y la guia va en "V" desde la tecla hasta el rotulo.
    for gi, mk in marks.items():
        col, label = mk[0], mk[1]
        dx = mk[2] if len(mk) > 2 else 0
        if label is None:
            continue
        i = gi - start_idx
        kx = x + i * kw + kw / 2
        lx = kx + dx
        ly = y_top + 11
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(col)
        c.drawCentredString(lx, ly, label)
        c.setStrokeColor(col)
        c.setLineWidth(1.1)
        c.line(kx, y_top + 1, kx, y_top + 4)
        c.line(kx, y_top + 4, lx, ly - 3)
    return y_top - kh


def _section_title(c, x, y, text, w=None):
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(NAVY)
    c.drawString(x, y, text.upper())
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.3)
    c.line(x, y - 5, x + 22, y - 5)
    return y - 18


def _fact_strip(c, y, facts):
    """Tira de 4 datos duros, en cajas iguales."""
    n = len(facts)
    gapx = 8
    bw = (CONTENT_W - gapx * (n - 1)) / n
    bh = 48
    for i, (label, value) in enumerate(facts):
        bx = MARGIN + i * (bw + gapx)
        c.setFillColor(PANEL)
        c.roundRect(bx, y - bh, bw, bh, 4, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.rect(bx, y - bh, 2.6, bh, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 6.6)
        c.setFillColor(MUTED)
        c.drawString(bx + 10, y - 15, label.upper())
        size = _fit(value, 'DejaVuSerif-Bold', 13, bw - 18, floor=8)
        c.setFont('DejaVuSerif-Bold', size)
        c.setFillColor(NAVY)
        c.drawString(bx + 10, y - 34, value)
    return y - bh - 26


def _map_bar(c, y, secciones, total_compases):
    """Barra segmentada con la forma real de la pieza."""
    bh = 36
    x = MARGIN
    for (etq, desde, hasta, desc, col) in secciones:
        frac = (hasta - desde + 1) / total_compases
        sw = CONTENT_W * frac
        c.setFillColor(col)
        c.roundRect(x, y - bh, sw, bh, 3, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 10)
        c.setFillColor(white)
        c.drawString(x + 9, y - 15, etq)
        dsize = _fit(desc, 'DejaVuSans', 7.4, sw - 18, floor=5.6)
        c.setFont('DejaVuSans', dsize)
        c.drawString(x + 9, y - 27, desc)
        c.setFont('DejaVuSans', 6.8)
        c.setFillColor(MUTED)
        c.drawString(x, y - bh - 10, f'c. {desde}')
        x += sw + 3
    c.setFont('DejaVuSans', 6.8)
    c.setFillColor(MUTED)
    c.drawRightString(MARGIN + CONTENT_W, y - bh - 10, f'c. {total_compases}')
    return y - bh - 30


def _bullets(c, x, y, w, items, dot=NAVY, size=8.6, leading=11.6):
    for it in items:
        c.setFillColor(dot)
        c.circle(x + 2.4, y - 3.2, 1.7, fill=1, stroke=0)
        y = _wrap(c, it, x + 11, y, 'DejaVuSans', size, w - 11, leading, INK)
        y -= 3.5
    return y


def _rhythm_pair(c, y, bloques, time_sig):
    """Muestra, con notación real, el patrón de cada sección de la pieza,
       uno al lado del otro. Son un compás cada uno: ilustran el dibujo
       rítmico, no son un ejercicio."""
    col_w = (CONTENT_W - 26) / 2
    gap = 6.8
    ytop = y
    lowest = y
    for i, (etq, desc, events, color) in enumerate(bloques):
        bx = MARGIN + i * (col_w + 26)
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(color)
        c.drawString(bx, ytop, etq)
        c.setFont('DejaVuSans', 8.2)
        c.setFillColor(MUTED)
        c.drawString(bx + 16, ytop, desc)
        top, bot = draw_system(c, bx, ytop - 30, col_w, gap, events,
                               clef='treble', time_sig=time_sig)
        lowest = min(lowest, bot)
    return lowest - 24


def _note_box(c, x, y, w, titulo, texto, color, h=None):
    lines = 1
    tmp, cnt = '', 1
    for word in texto.split(' '):
        t = (tmp + ' ' + word).strip()
        if stringWidth(t, 'DejaVuSans', 8.4) <= w - 22:
            tmp = t
        else:
            cnt += 1
            tmp = word
    h = h or (24 + cnt * 11.4)
    c.setFillColor(PANEL)
    c.roundRect(x, y - h, w, h, 4, fill=1, stroke=0)
    c.setFillColor(color)
    c.rect(x, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 7.4)
    c.setFillColor(color)
    c.drawString(x + 12, y - 14, titulo.upper())
    _wrap(c, texto, x + 12, y - 26, 'DejaVuSans', 8.4, w - 22, 11.4, INK)
    return y - h


def build_ficha(c, cfg):
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
    c.drawRightString(W - MARGIN, y, 'Ficha de la partitura')
    y -= 30

    tsize = _fit(cfg['titulo'], 'DejaVuSerif-Bold', 26, CONTENT_W)
    c.setFont('DejaVuSerif-Bold', tsize)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, cfg['titulo'])
    y -= 15
    c.setFont('DejaVuSans', 9)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, y, cfg['autor'])
    y -= 20

    y = _fact_strip(c, y, cfg['datos'])

    y = _section_title(c, MARGIN, y, 'Mapa de la pieza')
    y = _map_bar(c, y, cfg['secciones'], cfg['total_compases'])
    y -= 4

    # --- dos columnas ---
    col_w = (CONTENT_W - 22) / 2
    right_x = MARGIN + col_w + 22
    y_col = y

    yl = _section_title(c, MARGIN, y_col, 'Dónde van las manos')
    kb = cfg['teclado']
    kw = col_w / kb['n_white']
    yl -= 24
    yl = draw_keyboard(c, MARGIN, yl, kb['n_white'], kw, 78,
                       marks=kb['marks'], start_idx=kb['start_idx'])
    yl -= 16
    c.setFont('DejaVuSans', 8.2)
    c.setFillColor(MUTED)
    yl = _wrap(c, kb['pie'], MARGIN, yl, 'DejaVuSans', 8.2, col_w, 11.2, MUTED)

    yr = _section_title(c, right_x, y_col, 'Lo especial de esta partitura')
    yr = _bullets(c, right_x, yr, col_w, cfg['especial'])

    y = min(yl, yr) - 20

    if cfg.get('ritmos'):
        y = _section_title(c, MARGIN, y, 'El dibujo de cada parte')
        y = _rhythm_pair(c, y, cfg['ritmos'], cfg['time_sig'])

    # --- reto / truco ---
    yb = _note_box(c, MARGIN, y, col_w, 'El reto', cfg['reto'], ACCENT)
    yb2 = _note_box(c, right_x, y, col_w, 'El truco', cfg['truco'], BLUE)
    y = min(yb, yb2) - 16

    y = _note_box(c, MARGIN, y, CONTENT_W, '¿Sabías que…?', cfg['sabias'], NAVY_SOFT)

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
