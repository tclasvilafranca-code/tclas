# -*- coding: utf-8 -*-
"""Maquetacion para el nuevo formato de dosier de ejercicios, organizado
   en los 7 bloques pedagogicos (calentamiento fisico, tecnica, lectura,
   auditivo, juegos, teoria/dictado, creatividad). Reutiliza el motor de
   notacion y los helpers de page_layout_common, pero con pentagramas mas
   densos (mas notas por sistema) y una cabecera propia distinta de la de
   los dosieres por cancion."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from notation import *
from page_layout_common import (W, H, MARGIN, CONTENT_W, system_block, grand_staff_block,
                                 multi_system_block, wrap_text_common, exercise_heading,
                                 before_staff, after_system)
from reportlab.lib.colors import white
from reportlab.pdfbase.pdfmetrics import stringWidth

BLOQUE_COLOR = {
    1: HexColor('#6B7A8F'), 2: DARKGREEN, 3: HexColor('#3E6E8F'),
    4: GOLD, 5: HexColor('#8A5FA3'), 6: MAROON, 7: HexColor('#B8622E'),
}
BLOQUE_NOMBRE = {
    1: 'Calentamiento físico', 2: 'Técnica al piano', 3: 'Lectura, ritmo e interpretación',
    4: 'Entrenamiento auditivo', 5: 'Juegos pedagógicos', 6: 'Teoría y dictado', 7: 'Creatividad',
}


def page_header(c, kicker, subtitle_right):
    c.setFillColor(DARKGREEN)
    c.rect(0, H - 5, W, 5, fill=1, stroke=0)
    y = H - 32
    c.setFont('DejaVuSans-Bold', 8.8)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN, y, kicker.upper())
    c.setFont('DejaVuSans', 8.8)
    c.setFillColor(GRAY)
    c.drawRightString(W - MARGIN, y, subtitle_right)
    y -= 22
    titulo = 'Dosier de ejercicios · nuevo formato por bloques'
    size = 19
    while size > 13 and stringWidth(titulo, 'DejaVuSerif-Bold', size) > CONTENT_W:
        size -= 0.5
    c.setFont('DejaVuSerif-Bold', size)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, titulo)
    return y - 20


def page_footer(c, page_num):
    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(HexColor('#8A8A8A'))
    c.drawCentredString(W / 2, 22, 'El Cuaderno del Pianista · T-Clas · Ejemplo nuevo formato')
    c.drawRightString(W - MARGIN, 22, str(page_num))


def bloque_heading(c, y, num, desc):
    """Cabecera de bloque: badge de color propio + nombre fijo del bloque."""
    color = BLOQUE_COLOR[num]
    nombre = BLOQUE_NOMBRE[num]
    c.setFillColor(color)
    c.roundRect(MARGIN, y - 19, 23, 23, 4, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 11.5)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 11.5, y - 14, str(num))
    c.setFont('DejaVuSans-Bold', 12.8)
    c.setFillColor(INK)
    c.drawString(MARGIN + 31, y - 13.5, f'Bloque {num} · {nombre}')
    yy = wrap_text_common(c, desc, MARGIN + 31, y - 27, 'DejaVuSans', 8.7, CONTENT_W - 31, 11.5, color=GRAY)
    return yy - 4


def bullet_list(c, y, items, x0=MARGIN, w=CONTENT_W, font_size=8.9, leading=12.0, color=INK, dot_color=None):
    for item in items:
        c.setFillColor(dot_color or INK)
        c.circle(x0 + 2.3, y - 3.2, 1.5, fill=1, stroke=0)
        y = wrap_text_common(c, item, x0 + 11, y, 'DejaVuSans', font_size, w - 11, leading, color=color)
        y -= 3
    return y


def bullet_list_2col(c, y, items, x0=MARGIN, w=CONTENT_W, font_size=8.9, leading=12.0, dot_color=None):
    half = (len(items) + 1) // 2
    col_w = (w - 22) / 2
    y_left = bullet_list(c, y, items[:half], x0=x0, w=col_w, font_size=font_size, leading=leading, dot_color=dot_color)
    y_right = bullet_list(c, y, items[half:], x0=x0 + col_w + 22, w=col_w, font_size=font_size, leading=leading, dot_color=dot_color)
    return min(y_left, y_right)


def nota_estilo(c, y, texto, height=34):
    """Caja destacada para una nota de estilo/contexto (bloque F del dosier)."""
    c.setFillColor(HexColor('#F4EFE3'))
    c.roundRect(MARGIN, y - height, CONTENT_W, height, 5, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(MARGIN, y - height, 3, height, fill=1, stroke=0)
    wrap_text_common(c, texto, MARGIN + 12, y - 13, 'DejaVuSans', 8.4, CONTENT_W - 24, 11.2, color=HexColor('#5A4A20'))
    return y - height - 10


def blank_staff(c, x, top_y, width, gap, clef='treble', time_sig=(3, 4), n_bars=2):
    """Pentagrama vacio (clave + compas + compases marcados, sin notas) para
       un dictado ritmico: el alumno escribe encima lo que escucha."""
    ys = draw_staff(c, x, top_y, width, gap=gap)
    top, bot = ys[0], ys[-1]
    cursor_x = x + 4
    draw_clef(c, cursor_x, bot, gap, clef=clef)
    cursor_x += gap * (5.4 if clef == 'treble' else 4.6)
    draw_time_sig(c, cursor_x, bot, gap, top=str(time_sig[0]), bottom=str(time_sig[1]))
    cursor_x += gap * 3.0
    draw_barline(c, x, top, bot)
    avail_w = (x + width - 8) - cursor_x
    for i in range(1, n_bars):
        draw_barline(c, cursor_x + avail_w * i / n_bars, top, bot)
    draw_barline(c, x + width - 4, top, bot, final=True)
    return top, bot


def answer_box_row(c, x0, y, n_boxes, box_w, box_h=15, gap=6):
    """Fila de casillas en blanco (p.ej. para digitacion o grados I/IV/V)."""
    c.setStrokeColor(LIGHTLINE)
    c.setLineWidth(0.7)
    x = x0
    for _ in range(n_boxes):
        c.roundRect(x, y - box_h, box_w, box_h, 2, fill=0, stroke=1)
        x += box_w + gap
    return y - box_h
