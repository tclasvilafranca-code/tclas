# -*- coding: utf-8 -*-
"""Maquetacion compartida para las fichas de 10 minutos (calentamiento de
   dedos, agudeza visual, cierre/relajacion). Reutiliza el motor de
   notacion (notation.py) y los helpers de page_layout_common.py del
   proyecto de dosieres, pero con una cabecera y un pie propios: estas
   fichas no pertenecen a ninguna cancion ni alumno concreto."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from notation import *
from page_layout_common import (W, H, MARGIN, CONTENT_W, system_block,
                                 grand_staff_block, wrap_text_common,
                                 system_caption, before_staff, after_system)
from reportlab.lib.colors import white
from reportlab.pdfbase.pdfmetrics import stringWidth

NIVEL_COLOR = {1: DARKGREEN, 2: GOLD, 3: MAROON}
NIVEL_NOMBRE = {1: 'Nivel 1 · iniciación', 2: 'Nivel 2 · básico', 3: 'Nivel 3 · intermedio (para pasarlo bien)'}


def ficha_header(c, tipo, nivel, ficha_num, titulo, total_fichas=10):
    color = NIVEL_COLOR[nivel]
    c.setFillColor(color)
    c.rect(0, H - 5, W, 5, fill=1, stroke=0)
    y = H - 32
    kicker = f'{NIVEL_NOMBRE[nivel].upper()} · {tipo.upper()} · FICHA {ficha_num}/{total_fichas}'
    size = 8.8
    while size > 6.5 and stringWidth(kicker, 'DejaVuSans-Bold', size) > CONTENT_W - 140:
        size -= 0.2
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(color)
    c.drawString(MARGIN, y, kicker)
    c.setFont('DejaVuSans', 8.8)
    c.setFillColor(GRAY)
    c.drawRightString(W - MARGIN, y, '10 minutos')
    y -= 22
    size = 18
    while size > 13 and stringWidth(titulo, 'DejaVuSerif-Bold', size) > CONTENT_W:
        size -= 0.5
    c.setFont('DejaVuSerif-Bold', size)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, titulo)
    return y - 22


def ficha_intro(c, y, texto):
    return wrap_text_common(c, texto, MARGIN, y, 'DejaVuSans', 9.4, CONTENT_W, 13, color=GRAY) - 8


def ficha_footer(c, tipo_slug):
    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(HexColor('#8A8A8A'))
    c.drawCentredString(W / 2, 22, 'Fichas de práctica de 10 minutos · T-Clas')
    c.drawRightString(W - MARGIN, 22, tipo_slug)


def section_label(c, y, texto):
    c.setFont('DejaVuSans-Bold', 9.6)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, texto)
    return y - 16


def ruled_box(c, y_top, height, title):
    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN, y_top, title)
    y_top -= 16
    c.setStrokeColor(LIGHTLINE)
    c.setLineWidth(0.8)
    c.roundRect(MARGIN, y_top - height, CONTENT_W, height, 6, fill=0, stroke=1)
    n_lines = 4
    step = height / (n_lines + 1)
    yy = y_top - step
    for _ in range(n_lines):
        c.setStrokeColor(LIGHTLINE)
        c.line(MARGIN + 14, yy, MARGIN + CONTENT_W - 14, yy)
        yy -= step
    return y_top - height - 10
