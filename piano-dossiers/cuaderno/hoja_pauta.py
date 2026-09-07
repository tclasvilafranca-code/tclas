# -*- coding: utf-8 -*-
"""Ultima hoja del dosier: PAPEL PAUTADO.

   Pentagramas vacios, sin clave, sin armadura y sin compas. Nada mas.

   Es la hoja que en clase siempre acaba haciendo falta y que nadie tiene: la
   que se usa para copiar un compas que no sale, para escribir la escala de
   la semana, para apuntar de memoria el bajo de la pieza o para que el
   alumno invente algo. Al ir dentro del dosier de cada cancion, lo que se
   escriba ahi queda al lado de la partitura a la que pertenece, que es lo
   que no pasa cuando se usa un cuaderno pautado aparte.

   Va sin clave a proposito: la clave la pone quien escribe, y decidir si lo
   que va a escribir es de mano derecha o de izquierda ya es parte del
   ejercicio.

   Se meten los maximos que caben respetando el sitio de las lineas
   adicionales: un pentagrama pegado al de arriba no se puede usar, porque
   cualquier nota que se salga del pentagrama se mete en el de al lado.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_staff, BLEED_SAFE
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)

GAP = 8.6           # pentagrama grande: aqui se escribe a mano, con lapiz
SUELO = 46
AIRE = 3.15         # separacion entre pentagramas, en espacios de pentagrama


def build_pauta(c, cfg):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(BLEED_SAFE, H - 6 - BLEED_SAFE, W - 2 * BLEED_SAFE, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, cfg['kicker'].upper())
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, cfg.get('esquina', 'Papel pautado'))
    y -= 26

    c.setFont('DejaVuSerif-Bold', 21)
    c.setFillColor(NAVY)
    titulo = cfg.get('titulo_pauta', 'Para escribir')
    c.drawString(MARGIN, y, titulo)
    tw = stringWidth(titulo, 'DejaVuSerif-Bold', 21)
    sub = cfg.get('pie_pauta',
                  'la clave la pones tú · para copiar un compás, escribir la escala o inventarte algo')
    # se ajusta al hueco que queda a la derecha del titulo: escrito a pelo se
    # salia por el margen, que es el fallo numero seis de la lista del CLAUDE.md
    ssize = _fit(sub, 'DejaVuSans', 8.4, CONTENT_W - tw - 14, floor=6.6)
    c.setFont('DejaVuSans', ssize)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + tw + 14, y + 1, sub)
    y -= 16

    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.line(MARGIN, y, W - MARGIN, y)
    y -= 22

    gap = cfg.get('gap_pauta', GAP)
    paso = gap * (4 + AIRE)
    n = int((y - SUELO) // paso)
    # el sobrante se reparte entre todos, para que la hoja quede cuadrada por
    # arriba y por abajo en vez de dejar un hueco muerto al pie
    extra = (y - SUELO - n * paso) / n if n else 0

    for i in range(n):
        draw_staff(c, MARGIN, y, CONTENT_W, gap=gap)
        y -= paso + extra

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
    return y + extra
