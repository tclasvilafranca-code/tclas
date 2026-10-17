# -*- coding: utf-8 -*-
"""El Quadern del Pianista · PEKES (6-10 anys) — sistema de disseny TCLAS adaptat a nens.

   Base: l'estil de tots els àlbums T-Clas (A4 vertical, barra blau nit a dalt, titol en serif,
   caixes crema amb filet ocre, lletra DejaVu). Sobre aquesta base, els afegits infantils:

     · en Mussol Misol com a guia a cada pàgina (global de conversa)
     · "ET TROBES AQUÍ": un mapa de píndoles amb el tema actual
     · fitxes de nota (teclat + pentagrama + color) en lloc de paràgrafs
     · esquemes amb fletxes, escales de colors, números grans de pas
     · les pàgines de notes poden anar A COLOR; la resta, en blanc i negre

   Les pàgines es dibuixen amb un ManoCanvas d'amplitud 0 (traç net, sense tremolor).
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
sys.path.insert(0, HERE)
import notation as nt                                           # noqa: E402
from reportlab.lib.colors import HexColor, white, black        # noqa: E402
from reportlab.pdfbase.pdfmetrics import stringWidth           # noqa: E402

from dibujo_mano import ManoCanvas, lineas_texto               # noqa: E402
from mussol import mussol                                       # noqa: E402

W, H = 595.276, 841.89
M = 40
CW = W - 2 * M

NAVY = HexColor('#1A2332')
NAVY_SOFT = HexColor('#3C4A5E')
CREMA = HexColor('#FDFBF6')
WARM = HexColor('#F4EFE3')
RULE = HexColor('#C9CFD8')
INK = HexColor('#232323')
MUTED = HexColor('#7C838F')
OCRE = HexColor('#8C6A3F')

# colors de les notes (els de tota la vida del cartell)
COL = dict(DO='#E4392B', RE='#F28C0E', MI='#F9C80E', FA='#76B82A', SOL='#2E86C8', LA='#A58AC9',
           SI='#A7A397')
COLNOM = dict(DO='vermell', RE='taronja', MI='groc', FA='verd', SOL='blau', LA='lila', SI='gris')
SANS, SANSB, SERIFB = 'DejaVuSans', 'DejaVuSans-Bold', 'DejaVuSerif-Bold'


def Y(t):
    """Coordenada y a partir d'una distància des de dalt de la pàgina."""
    return H - t


# ------------------------------------------------------------------ text
def txt(c, x, y, s, size=10.5, font=SANS, col=INK, align='l'):
    c.setFillColor(col)
    c.setFont(font, size)
    if align == 'c':
        c.drawCentredString(x, y, s)
    elif align == 'r':
        c.drawRightString(x, y, s)
    else:
        c.drawString(x, y, s)


def par(c, x, y, s, size=10.5, ample=300, lead=None, font=SANS, col=INK):
    lead = lead or size * 1.38
    for ln in lineas_texto(s, font, size, ample):
        txt(c, x, y, ln, size, font, col)
        y -= lead
    return y


def alt_par(s, size, ample, lead=None, font=SANS):
    return len(lineas_texto(s, font, size, ample)) * (lead or size * 1.38)


def trac(c, w=1.0, col=NAVY, dash=None):
    c.setStrokeColor(col)
    c.setLineWidth(w)
    c.setLineJoin(1)
    c.setLineCap(1)
    c.setDash(*dash) if dash else c.setDash()


def rr(c, x, y, w, h, r=4, fill=white, lw=1.0, col=NAVY, dash=None):
    trac(c, lw, col, dash)
    c.setFillColor(fill)
    c.roundRect(x, y, w, h, r, stroke=1 if lw else 0, fill=1)
    c.setDash()


# ------------------------------------------------------------------ pàgina
def pagina(c, kicker, titol, dreta, intro, num, color=False):
    c.setFillColor(CREMA)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(NAVY)
    c.rect(0, H - 7, W, 7, stroke=0, fill=1)
    txt(c, M, Y(30), kicker, 7.2, SANSB, NAVY_SOFT)
    txt(c, W - M, Y(30), dreta, 8, SANS, MUTED, 'r')
    txt(c, M, Y(62), titol, 27, SERIFB, NAVY)
    par(c, M, Y(80), intro, 10, CW, 13.2, SANS, NAVY_SOFT)
    # peu
    trac(c, 0.6, RULE)
    c.line(M, 40, W - M, 40)
    txt(c, W / 2, 24, 'El Quadern del Pianista  ·  T-Clas', 7.5, SANS, MUTED, 'c')
    txt(c, W - M, 24, str(num), 8, SANS, MUTED, 'r')
    txt(c, M, 24, 'PEKES', 7.5, SANSB, OCRE)


def mapa(c, y, items, actiu):
    """ET TROBES AQUÍ: píndoles amb els temes del capítol."""
    txt(c, M, y + 3, 'ET TROBES AQUÍ', 6.8, SANSB, OCRE)
    x = M + 70
    for k, t in enumerate(items):
        w = stringWidth(t, SANSB, 7.5) + 18
        on = (k == actiu)
        rr(c, x, y - 4, w, 17, 8.5, fill=NAVY if on else white, lw=0.9, col=NAVY if on else RULE)
        txt(c, x + w / 2, y + 1, t, 7.5, SANSB, white if on else MUTED, 'c')
        if k < len(items) - 1:
            trac(c, 1.0, RULE)
            c.line(x + w + 2, y + 4.5, x + w + 8, y + 4.5)
        x += w + 10


def caixa(c, x, y, w, h, etiqueta, text, size=10, fons=WARM, filet=OCRE):
    """Caixa crema amb filet ocre a l'esquerra (la de tota la vida)."""
    rr(c, x, y, w, h, 3, fill=fons, lw=0)
    c.setFillColor(filet)
    c.rect(x, y, 3, h, stroke=0, fill=1)
    txt(c, x + 14, y + h - 15, etiqueta, 7.2, SANSB, filet)
    par(c, x + 14, y + h - 30, text, size, w - 28, size * 1.38)


def guia(c, x, y, ample, text, color=False, s=0.5, size=10.5, alt=None):
    """En Mussol Misol fent de guia: la seva figura a l'esquerra i el globus de conversa."""
    h = alt or (alt_par(text, size, ample - 70) + 34)
    mussol(c, x + 34, y + h / 2 - 4, s, color=color, lw=2.6)
    bx = x + 78
    rr(c, bx, y, ample - 78, h, 8, fill=white, lw=1.1, col=NAVY)
    c.setFillColor(white)
    trac(c, 1.1, NAVY)
    c.poly([(bx + 1, y + h / 2 + 8), (bx - 10, y + h / 2), (bx + 1, y + h / 2 - 8)], 1, 1)
    c.setStrokeColor(white)
    c.setLineWidth(2)
    c.line(bx + 1, y + h / 2 + 6, bx + 1, y + h / 2 - 6)
    txt(c, bx + 14, y + h - 16, 'EN MUSSOL MISOL DIU', 6.8, SANSB, OCRE)
    par(c, bx + 14, y + h - 31, text, size, ample - 78 - 28, size * 1.38)
    return h


def quadrat(c, x, y, n, mida=17):
    """El número de pas (quadrat ocre)."""
    rr(c, x, y, mida, mida, 3, fill=OCRE, lw=0)
    txt(c, x + mida / 2, y + mida * 0.3, str(n), 10.5, SANSB, white, 'c')


def bloc(c, y, n, titol, pista=None, x=M):
    quadrat(c, x, y - 4)
    txt(c, x + 25, y, titol, 12.5, SANSB, NAVY)
    if pista:
        txt(c, x + 25, y - 13, pista, 8.2, SANS, MUTED)


def etiqueta_sec(c, x, y, text):
    txt(c, x, y, text, 7.6, SANSB, NAVY)
    trac(c, 1.4, OCRE)
    c.line(x, y - 4, x + 26, y - 4)


# ------------------------------------------------------------------ teclat
ORDRE = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']


def teclat(c, x, y, w, h, nb=7, resalta=None, noms=None, color=False, dits=None, lw=1.1):
    """Teclat de `nb` blanques des del DO. `resalta`: {índex: nom}. `noms`: 'resalta' o 'totes'."""
    resalta = resalta or {}
    dits = dits or {}
    kw = w / float(nb)
    for i in range(nb):
        nm = resalta.get(i)
        fill = HexColor(COL[nm]) if (nm and color) else (HexColor('#E7E2D5') if nm else white)
        rr(c, x + i * kw, y, kw, h, 2.5, fill=fill, lw=lw, col=NAVY)
    for i in range(nb - 1):
        if i % 7 in (0, 1, 3, 4, 5):
            rr(c, x + (i + 1) * kw - 0.3 * kw, y + h * 0.4, 0.6 * kw, h * 0.6, 2, fill=NAVY, lw=0)
    for i in range(nb):
        nm = ORDRE[i % 7]
        if (noms == 'totes') or (noms == 'resalta' and i in resalta):
            on = i in resalta
            txt(c, x + i * kw + kw / 2, y + 5, nm, 8.5 if on else 7.5, SANSB if on else SANS,
                INK if on else MUTED, 'c')
        if i in dits:
            cx, cy = x + i * kw + kw / 2, y + h * 0.3 + 12
            c.setFillColor(NAVY)
            c.circle(cx, cy, 6.6, stroke=0, fill=1)
            txt(c, cx, cy - 3.3, str(dits[i]), 9, SANSB, white, 'c')


# ------------------------------------------------------------------ pentagrama
def pauta(c, x, ytop, w, gap, clau='treble', final=True, lw=0.85):
    trac(c, lw, NAVY_SOFT)
    for i in range(5):
        c.line(x, ytop - i * gap, x + w, ytop - i * gap)
    yb = ytop - 4 * gap
    nt.draw_clef(c, x + 3, yb, gap, clau)
    if final:
        trac(c, 1.1, NAVY)
        c.line(x + w, ytop, x + w, yb)
    return yb


def cap(c, cx, cy, gap, dur, fill=white):
    """Cap de nota net: negra plena, blanca buida, rodona buida i inclinada."""
    trac(c, 1.2, NAVY)
    if dur == 'w':
        c.saveState()
        c.translate(cx, cy)
        c.setFillColor(fill)
        c.ellipse(-gap * 0.82, -gap * 0.56, gap * 0.82, gap * 0.56, stroke=1, fill=1)
        c.rotate(-30)
        c.ellipse(-gap * 0.24, -gap * 0.46, gap * 0.24, gap * 0.46, stroke=1, fill=0)
        c.restoreState()
        return
    c.saveState()
    c.translate(cx, cy)
    c.rotate(-20)
    c.setFillColor(NAVY if (dur == 'q' and fill == white) else fill)
    c.ellipse(-gap * 0.78, -gap * 0.55, gap * 0.78, gap * 0.55, stroke=1, fill=1)
    c.restoreState()
    trac(c, 1.3, NAVY)
    c.line(cx + gap * 0.74, cy + gap * 0.1, cx + gap * 0.74, cy + gap * 3.3)


def nota(c, x0, yb, gap, alt, cx, dur='w', fill=white):
    cy = nt.note_y(yb, gap, alt)
    if alt in ('C4',):
        trac(c, 0.9, NAVY)
        c.line(cx - gap * 1.25, cy, cx + gap * 1.25, cy)
    cap(c, cx, cy, gap, dur, fill)
    return cy


def caseta(c, x, y, w, h, r=4, dash=(2, 2)):
    rr(c, x, y, w, h, r, fill=white, lw=0.8, col=MUTED, dash=dash)


# ------------------------------------------------------------------ mans
def ma(c, cx, cy, s=1.0, esq=False, dits=True, fill=white):
    """Una mà, vista de dalt. `esq` la gira (el polze queda a la dreta)."""
    sg = -1 if esq else 1
    fin = [(-52, 8, 9, 28, 38, 1), (-28, 62, 9.5, 31, 0, 2), (-8, 72, 9.5, 36, 0, 3),
           (12, 65, 9.5, 32, 0, 4), (31, 48, 8.5, 25, 0, 5)]
    trac(c, 1.2, NAVY)
    c.setFillColor(fill)
    for (dx, dy, rx, ry, gir, n) in fin:
        c.saveState()
        c.translate(cx + sg * dx * s, cy + dy * s)
        c.rotate(-sg * gir)
        c.ellipse(-rx * s, -ry * s, rx * s, ry * s, stroke=1, fill=1)
        c.restoreState()
    c.roundRect(cx - 44 * s, cy - 56 * s, 90 * s, 84 * s, 26 * s, stroke=1, fill=1)
    if dits:
        for (dx, dy, rx, ry, gir, n) in fin:
            tx = cx + sg * (dx - math.sin(math.radians(gir)) * ry * 0.45) * s
            ty = cy + (dy + ry * 0.55 + 12) * s
            c.setFillColor(NAVY)
            c.circle(tx, ty, 7 * s, stroke=0, fill=1)
            txt(c, tx, ty - 3 * s, str(n), 9 * s, SANSB, white, 'c')


def xip(c, x, y, w, text, fill=white, col=INK, h=17, size=8):
    rr(c, x, y, w, h, 8, fill=fill, lw=0.8, col=NAVY_SOFT)
    txt(c, x + w / 2, y + h * 0.3, text, size, SANSB, col, 'c')
