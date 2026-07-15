# -*- coding: utf-8 -*-
"""Generador de la PORTADA de album: una pagina de indice con el logo T-Clas,
   el nombre del alumno y el listado del repertorio agrupado por mes.
   Parametrizado, igual que page_theory_generic y page_worksheet_generic."""
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import *

W, H = 595.276, 841.89
MARGIN = 46
CONTENT_W = W - 2 * MARGIN
STAR_FULL, STAR_EMPTY = '★', '☆'


def _stars(level, total=4):
    return STAR_FULL * level + STAR_EMPTY * (total - level)


def build_portada(c, logo_path, alumno, subtitle, months):
    """months: list of (month_label, [song_row, ...]) in the order they should
       appear, where song_row is a dict with keys:
         num, title, subtitle (compositor/arreglista), tonalidad, dificultad (1-4)
    """
    c.setFillColor(DARKGREEN)
    c.rect(0, H - 5, W, 5, fill=1, stroke=0)

    logo_size = 92
    logo_x = (W - logo_size) / 2
    y = H - 40
    try:
        c.drawImage(logo_path, logo_x, y - logo_size, logo_size, logo_size, mask='auto')
    except Exception:
        pass
    y -= logo_size + 24

    c.setFont('DejaVuSerif-Bold', 25)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, y, 'El Cuaderno del Pianista')
    y -= 22
    c.setFont('DejaVuSans-Bold', 12.5)
    c.setFillColor(DARKGREEN)
    c.drawCentredString(W / 2, y, alumno.upper())
    y -= 16
    c.setFont('DejaVuSans', 10)
    c.setFillColor(GRAY)
    c.drawCentredString(W / 2, y, subtitle)
    y -= 22

    c.setStrokeColor(LIGHTLINE)
    c.setLineWidth(0.8)
    c.line(MARGIN, y, W - MARGIN, y)
    y -= 26

    c.setFont('DejaVuSans-Bold', 11)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Repertorio de este cuaderno')
    y -= 20

    row_h = 30
    month_h = 20

    for month_label, rows in months:
        c.setFillColor(DARKGREEN)
        c.roundRect(MARGIN, y - 15, CONTENT_W, 15, 3, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(white)
        c.drawString(MARGIN + 8, y - 11, month_label.upper())
        y -= month_h

        for row in rows:
            c.setFillColor(HexColor('#F6F3EA'))
            c.roundRect(MARGIN, y - row_h + 6, CONTENT_W, row_h - 8, 4, fill=1, stroke=0)

            c.setFillColor(DARKGREEN)
            c.setFont('DejaVuSans-Bold', 10)
            c.drawString(MARGIN + 10, y - 13, str(row['num']))

            c.setFont('DejaVuSans-Bold', 10.3)
            c.setFillColor(INK)
            title = row['title']
            max_title_w = CONTENT_W - 190
            while stringWidth(title, 'DejaVuSans-Bold', 10.3) > max_title_w and len(title) > 3:
                title = title[:-2]
            if title != row['title']:
                title += '…'
            c.drawString(MARGIN + 28, y - 12, title)
            c.setFont('DejaVuSans', 7.8)
            c.setFillColor(GRAY)
            c.drawString(MARGIN + 28, y - 22, row['subtitle'])

            c.setFont('DejaVuSans', 8.4)
            c.setFillColor(GRAY)
            c.drawRightString(MARGIN + CONTENT_W - 66, y - 12, row['tonalidad'])
            c.setFont('DejaVuSans', 10.5)
            c.setFillColor(GOLD)
            c.drawRightString(MARGIN + CONTENT_W - 8, y - 12.5, _stars(row['dificultad']))

            y -= row_h

    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(HexColor('#8A8A8A'))
    c.drawCentredString(W / 2, 22, 'El Cuaderno del Pianista · T-Clas')
