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


def marca(c, x, y, w, h, col, n, tipo='caja'):
    """Marca fina alrededor de lo importante; (x, y) es el centro, y desde arriba.
       Solo contorno: no tapa nada. El numero va en la esquina, fuera de la musica."""
    c.setStrokeColor(Color(col.red, col.green, col.blue, alpha=0.9))
    c.setLineWidth(1.0)
    x0, y0 = x - w / 2, PAGE_H - y - h / 2
    if tipo == 'ovalo':
        c.ellipse(x0, y0, x0 + w, y0 + h, stroke=1, fill=0)
    else:
        c.roundRect(x0, y0, w, h, 3, stroke=1, fill=0)
    cx, cy = x0 + w, y0 + h
    c.setFillColor(col)
    c.circle(cx, cy, 4.4, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont('DejaVuSans-Bold', 6)
    c.drawCentredString(cx, cy - 2.1, str(n))


def margen(c, bloque, top, bot, primero):
    """Parentesis fino en el margen izquierdo + ficha con el numero del bloque."""
    num, c1, c2, nombre, col = bloque
    t, b = PAGE_H - top, PAGE_H - bot
    c.setStrokeColor(col)
    c.setLineWidth(1.3)
    c.line(28, b, 28, t)
    c.line(28, t, 32, t)
    c.line(28, b, 32, b)
    c.setFillColor(col)
    c.circle(19.5, t - 9, 7, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont('DejaVuSerif-Bold', 9)
    c.drawCentredString(19.5, t - 12.1, str(num))
    c.saveState()
    c.setFillColor(col)
    c.setFont('DejaVuSans-Bold', 6.2)
    etq = 'cc. %d-%d' % (c1, c2) if primero else 'sigue'
    c.translate(22.5, t - 20)
    c.rotate(-90)
    c.drawString(0, 0, etq)
    c.restoreState()


def capa(pag, marcas):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(595.276, PAGE_H))
    segmentos = []                      # (bloque, top, bot, primero)
    for (t, b_), (c1, c2) in zip(SIST[pag], COMPASES[pag]):
        b = bloque_de(c1)
        top = t - (34 if (pag, c1) in ((3, 23), (3, 25)) else 24)
        bot = b_ + 8
        if segmentos and segmentos[-1][0] is b:
            segmentos[-1][2] = bot
        else:
            segmentos.append([b, top, bot, c1 == b[1]])
    for b, top, bot, primero in segmentos:
        col = b[4]
        c.setFillColor(Color(col.red, col.green, col.blue, alpha=0.055))
        c.roundRect(31, PAGE_H - bot, 543, bot - top, 4, fill=1, stroke=0)
        margen(c, b, top, bot, primero)
    for (x, y, w, h, bn, n, tipo) in marcas.get(pag, []):
        marca(c, x, y, w, h, [b for b in BLOQUES if b[0] == bn][0][4], n, tipo)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


# marcas: (x, y, ancho, alto, bloque, numero, tipo): centro en pt desde arriba
MARCAS = {
    1: [(139, 171, 66, 14, 1, 1, 'caja'), (122, 257, 26, 16, 1, 2, 'ovalo'),
        (131, 336, 120, 14, 2, 1, 'caja'), (70, 414, 20, 17, 2, 2, 'ovalo'),
        (76, 517, 17, 26, 3, 1, 'caja'), (351, 516, 17, 26, 3, 2, 'caja'),
        (545, 516, 19, 26, 3, 3, 'caja'),
        (111, 639, 80, 14, 4, 1, 'caja')],
    2: [(344, 93, 17, 26, 4, 2, 'caja'), (72, 227, 17, 26, 4, 3, 'caja'),
        (252, 227, 19, 26, 4, 4, 'caja'),
        (50, 564, 12, 76, 6, 1, 'caja'), (76, 621, 24, 14, 6, 2, 'ovalo')],
    3: [(72, 359, 15, 14, 7, 1, 'caja'), (75, 507, 15, 14, 7, 2, 'caja'),
        (555, 715, 14, 82, 7, 3, 'caja')],
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
