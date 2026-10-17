# -*- coding: utf-8 -*-
"""El meu llibre de piano, amb en Mussol Misol — sistema de disseny i lliçó de prova.

   Un mateix codi genera la lliçó en dues versions:
       COLOR  (fons crema, peces de colors)       ->  Llibre_Prova_Color.pdf
       BN     (blanc i negre, per pintar)         ->  Llibre_Prova_BN.pdf

   Els tipus de pàgina tenen la seva pestanya: APRENC (teoria), PRACTICO (exercicis),
   TOCO (al piano), JUGUEM (jocs i repte).

   Es genera amb:  python3 llibre.py
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
sys.path.insert(0, HERE)
import notation as nt                                           # noqa: E402
from reportlab.lib.colors import HexColor, black, white        # noqa: E402
from reportlab.pdfbase.pdfmetrics import stringWidth           # noqa: E402

from dibujo_mano import (W, H, ManoCanvas, texto, lineas_texto, letras_huecas,   # noqa: E402
                         subrayado_ondulado, flecha, _bezier)
from mussol import mussol                                       # noqa: E402

HA, FAT, SK = 'Hand', 'Fat', 'Sketch'
INK = HexColor('#35302F')
COL = dict(vermell='#E4392B', taronja='#F28C0E', groc='#F9C80E', verd='#76B82A', blau='#2E86C8',
           morat='#A58AC9', gris='#A7A397', rosa='#F277A5', pell='#F6CFA6')
NOTA_COLOR = {'DO': 'vermell', 'RE': 'taronja', 'MI': 'groc', 'FA': 'verd', 'SOL': 'blau',
              'LA': 'morat', 'SI': 'gris'}
TIPUS = {'APRENC': ('blau', 'bombeta'), 'PRACTICO': ('verd', 'llapis'),
         'TOCO': ('vermell', 'teclat'), 'JUGUEM': ('taronja', 'estrella')}


class Estil:
    """Color o blanc i negre. `f(nom)` dóna el color de farciment (blanc en BN)."""
    def __init__(self, color):
        self.color = color

    def f(self, nom):
        return HexColor(COL[nom]) if self.color else white

    @property
    def paper(self):
        return HexColor('#FBF1D5') if self.color else white


# ------------------------------------------------------------------ elements bàsics
def traç(c, w=2.4, col=INK):
    c.setStrokeColor(col)
    c.setLineWidth(w)
    c.setLineJoin(1)
    c.setLineCap(1)


def forma(c, tipus, *a, fill=white, lw=2.4, dash=None, **k):
    traç(c, lw)
    c.setFillColor(fill)
    if dash:
        c.setDash(*dash)
    getattr(c, tipus)(*a, stroke=1, fill=1, **k)
    c.setDash()


def fons(c, st):
    c.setFillColor(st.paper)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    forma(c, 'roundRect', 12, 12, W - 24, H - 24, 18, fill=st.paper, lw=3.0)
    traç(c, 1.0)
    c.setDash(1, 4)
    c.roundRect(19, 19, W - 38, H - 38, 13, stroke=1, fill=0)
    c.setDash()


def titol(c, st, text, y=500, mida=38):
    if st.color:
        from color_cat import lletres_color
        cols = ['vermell', 'taronja', 'groc', 'verd', 'blau', 'morat']
        lletres_color(c, W / 2, y, text, mida, cols, semilla=len(text))
    else:
        letras_huecas(c, W / 2, y, text, mida, semilla=len(text))


def pestanya(c, st, tipus, tema):
    nom, icona = TIPUS[tipus]
    w = stringWidth(tipus, FAT, 17) + 52
    forma(c, 'roundRect', 34, 536, w, 32, 12, fill=st.f(nom), lw=2.4)
    # icona
    ix, iy = 52, 552
    traç(c, 1.8)
    c.setFillColor(white)
    if icona == 'bombeta':
        c.circle(ix, iy + 1, 7, stroke=1, fill=1)
        c.line(ix - 3, iy - 9, ix + 3, iy - 9)
    elif icona == 'llapis':
        c.poly([(ix - 8, iy - 5), (ix + 5, iy + 8), (ix + 8, iy + 5), (ix - 5, iy - 8)], 1, 1)
    elif icona == 'teclat':
        c.rect(ix - 8, iy - 6, 16, 12, stroke=1, fill=1)
        c.line(ix - 3, iy - 6, ix - 3, iy + 6)
        c.line(ix + 3, iy - 6, ix + 3, iy + 6)
    else:
        from color_cat import estrella
        c.setFillColor(white)
        c.poly([(ix + 9 * math.cos(math.pi / 2 + i * math.pi / 5) * (1 if i % 2 == 0 else 0.46),
                 iy + 9 * math.sin(math.pi / 2 + i * math.pi / 5) * (1 if i % 2 == 0 else 0.46))
                for i in range(10)], 1, 1)
    c.setFillColor(white if st.color else INK)
    texto(c, 66, 546, tipus, 17, FAT, col=white if st.color else INK)
    texto(c, W - 36, 548, tema, 14, HA, 'r')


def peu(c, st, pagina, tema='El meu llibre de piano · amb en Mussol Misol'):
    traç(c, 1.2)
    c.line(40, 44, W - 40, 44)
    texto(c, 40, 28, tema, 12, HA)
    forma(c, 'circle', W - 52, 32, 12, fill=st.f('groc'), lw=2.0)
    texto(c, W - 52, 28, str(pagina), 14, HA, 'c')
    mussol(c, W - 92, 20, 0.15, color=st.color)


def targeta(c, st, x, y, w, h, tit, nom='blau', r=14):
    forma(c, 'roundRect', x, y, w, h, r, fill=white, lw=2.4)
    forma(c, 'roundRect', x, y + h - 30, w, 30, r, fill=st.f(nom), lw=2.4)
    if st.color:
        c.setFillColor(st.f(nom))
        c.rect(x + 3, y + h - 30, w - 6, 12, stroke=0, fill=1)
    texto(c, x + 14, y + h - 21, tit, 15, FAT if st.color else HA, col=white if st.color else INK)


def globus(c, x, y, w, h, linies, cua=None, mida=13.5, lead=16):
    forma(c, 'roundRect', x, y, w, h, 18, fill=white, lw=2.4)
    if cua is not None:
        cx, cy = cua
        c.setFillColor(white)
        traç(c, 2.4)
        c.poly([(cx - 14, y + 2), (cx + 14, y + 2), (cx + 4, cy)], 1, 1)
        c.setStrokeColor(white)
        c.setLineWidth(3.6)
        c.line(cx - 11, y + 2, cx + 11, y + 2)
    yy = y + h - 22
    for ln in linies:
        texto(c, x + 14, yy, ln, mida, HA)
        yy -= lead


def caseta(c, x, y, w, h, r=7):
    forma(c, 'roundRect', x, y, w, h, r, fill=white, lw=1.4, dash=(3, 2))


def numero(c, st, cx, cy, n, nom='blau', r=11):
    forma(c, 'circle', cx, cy, r, fill=st.f(nom), lw=2.0)
    texto(c, cx, cy - 5, str(n), 15, FAT if st.color else HA, 'c', col=white if st.color else INK)


def par_text(c, x, y, text, mida=13, ample=300, lead=16):
    for ln in lineas_texto(text, HA, mida, ample):
        texto(c, x, y, ln, mida, HA)
        y -= lead
    return y


# ------------------------------------------------------------------ teclat i notes
def teclat(c, st, x, y, w, h, nb=7, resalta=None, noms=False, dits=None):
    """Teclat de `nb` tecles blanques començant en DO. `resalta`: {índex: nom_de_color}."""
    resalta = resalta or {}
    dits = dits or {}
    kw = w / float(nb)
    ordre = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']
    for i in range(nb):
        nom_n = ordre[i % 7]
        col = resalta.get(i)
        forma(c, 'roundRect', x + i * kw, y, kw, h, 4, fill=st.f(col) if col else white, lw=2.0)
    for i in range(nb):
        if i % 7 in (0, 1, 3, 4, 5) and i + 1 < nb + 0:
            bx = x + (i + 1) * kw - 0.31 * kw
            forma(c, 'roundRect', bx, y + h * 0.38, 0.62 * kw, h * 0.62, 3, fill=HexColor('#3B3433') if st.color else white,
                  lw=2.0)
    for i in range(nb):
        nom_n = ordre[i % 7]
        if noms and i in resalta:
            texto(c, x + i * kw + kw / 2, y + 7, nom_n, 14 if len(nom_n) < 3 else 11.5, FAT if st.color else HA, 'c',
                  col=INK)
        if i in dits:
            numero(c, st, x + i * kw + kw / 2, y + h * 0.2 + 22, dits[i], 'blau', 9)


def cap_nota(c, st, cx, cy, gap, dur, nom):
    """Cap d'una nota: negra plena, blanca buida, rodona buida i inclinada."""
    col = st.f(NOTA_COLOR.get(nom, 'blau')) if st.color else white
    if dur == 'w':
        c.saveState()
        c.translate(cx, cy)
        forma(c, 'ellipse', -gap * 0.9, -gap * 0.6, gap * 0.9, gap * 0.6, fill=col, lw=2.0)
        c.rotate(-30)
        traç(c, 1.4)
        c.ellipse(-gap * 0.26, -gap * 0.5, gap * 0.26, gap * 0.5, stroke=1, fill=0)
        c.restoreState()
        return
    c.saveState()
    c.translate(cx, cy)
    c.rotate(-20)
    forma(c, 'ellipse', -gap * 0.78, -gap * 0.56, gap * 0.78, gap * 0.56, fill=col, lw=2.0)
    if dur == 'h' and st.color:
        c.setFillColor(white)
        c.ellipse(-gap * 0.42, -gap * 0.26, gap * 0.42, gap * 0.26, stroke=0, fill=1)
    if dur == 'q' and not st.color:
        p = c.beginPath()
        p.ellipse(-gap * 0.78, -gap * 0.56, gap * 0.78, gap * 0.56)
        c.clipPath(p, stroke=0, fill=0)
        traç(c, 1.0)
        k = -gap * 0.78
        while k < gap * 1.4:
            c.line(k, -gap * 0.56, k + gap * 0.8, gap * 0.56)
            k += gap * 0.32
    c.restoreState()
    if dur in ('h', 'q'):
        traç(c, 2.2)
        c.line(cx + gap * 0.74, cy + gap * 0.1, cx + gap * 0.74, cy + gap * 3.4)


def pent_notes(c, st, x, ytop, w, gap, notes, clau=True, compas=False, caselles=None, barres=()):
    """Pentagrama amb notes. `notes` = [(altura, durada, nom), ...]. Les notes es reparteixen
       pel pentagrama; `barres` = índexs després dels quals va una barra de compàs."""
    traç(c, 1.7)
    a = c.amp
    c.amp = 0.3
    for i in range(5):
        c.line(x, ytop - i * gap, x + w, ytop - i * gap)
    c.amp = a
    yb = ytop - 4 * gap
    x0 = x + 6
    if clau:
        nt.draw_clef(c, x0, yb, gap)
        x0 += gap * 2.6
    if compas:
        nt.draw_time_sig(c, x0, yb, gap)
        x0 += gap * 2.2
    n = len(notes)
    pas = (x + w - x0 - 8) / float(max(n, 1))
    pos = []
    for i, (alt, dur, nom) in enumerate(notes):
        cx = x0 + pas * (i + 0.5)
        cy = nt.note_y(yb, gap, alt)
        if alt == 'C4':
            traç(c, 1.6)
            c.line(cx - gap * 1.3, cy, cx + gap * 1.3, cy)
        cap_nota(c, st, cx, cy, gap, dur, nom)
        pos.append((cx, cy))
        if i in barres and i < n - 1:
            traç(c, 1.6)
            bx = x0 + pas * (i + 1)
            c.line(bx, ytop, bx, yb)
    traç(c, 1.8)
    c.line(x + w - 2, ytop, x + w - 2, yb)
    traç(c, 3.2)
    c.line(x + w + 2, ytop, x + w + 2, yb)
    return pos, yb


def ma_dreta(c, st, cx, cy, s=1.0, nums=True):
    pell = st.f('pell')
    # dits
    dits = [(-52, 8, 9, 28, 38, '1'), (-28, 62, 9.5, 31, 0, '2'), (-8, 72, 9.5, 36, 0, '3'),
            (12, 65, 9.5, 32, 0, '4'), (31, 48, 8.5, 25, 0, '5')]
    for (dx, dy, rx, ry, gir, n) in dits:
        c.saveState()
        c.translate(cx + dx * s, cy + dy * s)
        c.rotate(-gir)
        forma(c, 'ellipse', -rx * s, -ry * s, rx * s, ry * s, fill=pell, lw=2.2)
        c.restoreState()
    forma(c, 'roundRect', cx - 44 * s, cy - 56 * s, 90 * s, 84 * s, 26 * s, fill=pell, lw=2.4)
    if nums:
        for (dx, dy, rx, ry, gir, n) in dits:
            top = dy + ry * 0.55
            ang = math.radians(gir)
            tx = cx + (dx - math.sin(ang) * ry * 0.45) * s
            ty = cy + (top + 2) * s
            numero(c, st, tx, ty + 6 * s, n, 'blau', 8.5)
