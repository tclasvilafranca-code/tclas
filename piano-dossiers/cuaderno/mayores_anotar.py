# -*- coding: utf-8 -*-
"""Anota ENCIMA de la partitura original los bloques de aprendizaje.

   La partitura (PDF de Drive, con copyright) no se toca: se le superpone una
   capa transparente con bandas de color por bloque, una etiqueta por bloque y
   anillos sobre lo importante. El resultado va a `entrega/` (no se versiona).
"""
import io
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from pypdf import PdfReader, PdfWriter
from portada import W, H                                       # noqa: F401  (registra fuentes)
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(__file__)
SRC = os.path.join(HERE, '..', 'students', 'demo', 'source', 'Heart-Asks-Pleasure-First.pdf')
PAGE_H = 841.89

# (alto_arriba, alto_abajo) de cada sistema en pt DESDE ARRIBA, medidos sobre el PDF a 144 dpi
SIST = {
    1: [(215.5, 293.5), (370.0, 450.5), (509.0, 590.0), (652.5, 736.5)],
    2: [(85.5, 163.5), (219.5, 303.0), (375.5, 453.0), (528.5, 598.5), (672.0, 749.5)],
    3: [(85.5, 163.5), (224.0, 305.0), (390.0, 467.5), (536.0, 614.0), (676.0, 754.0)],
}
# compases por sistema, en orden de lectura
COMPASES = {1: [(1, 2), (3, 4), (5, 6), (7, 8)],
            2: [(9, 10), (11, 12), (13, 14), (15, 16), (17, 18)],
            3: [(19, 20), (21, 22), (23, 24), (25, 26), (27, 28)]}

BLOQUES = [
    (1, 1, 2, 'Entrada', HexColor('#3E6E8F')),
    (2, 3, 4, 'El dibujo de Più mosso', HexColor('#8C6A3F')),
    (3, 5, 6, 'Cambia el compás', HexColor('#A0453A')),
    (4, 7, 12, 'La cadencia y la vuelta', HexColor('#4F7A5A')),
    (5, 13, 14, 'Vuelve la entrada', HexColor('#3E6E8F')),
    (6, 15, 22, 'Repetición y octavas', HexColor('#6B5B95')),
    (7, 23, 28, 'Casillas y final', HexColor('#8C6A3F')),
]


def bloque_de(compas):
    for b in BLOQUES:
        if b[1] <= compas <= b[2]:
            return b


def pill(c, x, y, txt, col, size=7.6):
    w = stringWidth(txt, 'DejaVuSans-Bold', size) + 14
    c.setFillColor(col)
    c.roundRect(x, y, w, 13.5, 6.7, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont('DejaVuSans-Bold', size)
    c.drawString(x + 7, y + 3.9, txt)
    return w


def anillo(c, x, y, rx, ry, col, n=None):
    """Anillo a lapiz alrededor de algo importante (coordenadas desde arriba)."""
    c.setStrokeColor(col)
    c.setLineWidth(1.5)
    c.ellipse(x - rx, PAGE_H - y - ry, x + rx, PAGE_H - y + ry, stroke=1, fill=0)
    if n is not None:
        c.setFillColor(col)
        c.circle(x + rx, PAGE_H - y + ry, 5.2, fill=1, stroke=0)
        c.setFillColor(HexColor('#FFFFFF'))
        c.setFont('DejaVuSans-Bold', 6.6)
        c.drawCentredString(x + rx, PAGE_H - y + ry - 2.3, str(n))


def capa(pag, marcas):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(595.276, PAGE_H))
    visto = set()
    for (t, b_), (c1, c2) in zip(SIST[pag], COMPASES[pag]):
        b = bloque_de(c1)
        col = b[4]
        top, bot = t - (34 if (pag, c1) in ((3, 23), (3, 25)) else 26), b_ + 8
        c.setFillColor(Color(col.red, col.green, col.blue, alpha=0.10))
        c.roundRect(22, PAGE_H - bot, 551, bot - top, 5, fill=1, stroke=0)
        c.setFillColor(col)
        c.rect(14, PAGE_H - bot, 4.5, bot - top, fill=1, stroke=0)
        if b[0] not in visto:
            visto.add(b[0])
            etq = 'BLOQUE %d · cc. %d-%d · %s' % (b[0], b[1], b[2], b[3])
            if c1 != b[1]:
                etq = 'BLOQUE %d (sigue) · %s' % (b[0], b[3])
            w = stringWidth(etq, 'DejaVuSans-Bold', 7.6) + 14
            pill(c, 90 if (pag, c1) == (3, 23) else 573 - w, PAGE_H - bot - 6.5, etq, col)
    for (x, y, rx, ry, bn, n) in marcas.get(pag, []):
        anillo(c, x, y, rx, ry, [b for b in BLOQUES if b[0] == bn][0][4], n)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


# anillos: (x, y_desde_arriba, rx, ry, bloque, numero)
MARCAS = {
    1: [(139, 171, 36, 8, 1, 1), (122, 257, 12, 9, 1, 2),
        (125, 337, 55, 9, 2, 1), (70, 414, 10, 9, 2, 2),
        (76, 518, 15, 22, 3, 1), (351, 515, 15, 22, 3, 2), (545, 515, 15, 22, 3, 3),
        (122, 639, 32, 8, 4, 1)],
    2: [(344, 90, 15, 22, 4, 2), (72, 216, 15, 22, 4, 3), (252, 216, 15, 22, 4, 4),
        (47, 533, 9, 30, 6, 1), (76, 620, 13, 8, 6, 2)],
    3: [(75, 361, 12, 9, 7, 1), (80, 500, 12, 9, 7, 2), (557, 711, 7, 40, 7, 3)],
}


def main(salida):
    rd = PdfReader(SRC)
    wr = PdfWriter()
    for i, p in enumerate(rd.pages, 1):
        p.merge_page(capa(i, MARCAS))
        wr.add_page(p)
    with open(salida, 'wb') as f:
        wr.write(f)


if __name__ == '__main__':
    out = os.path.join(HERE, 'entrega', 'DEMO_Partitura_por_bloques.pdf')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(out)
    print(out)
