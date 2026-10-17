# -*- coding: utf-8 -*-
"""El Quadern del Pianista · PEKES (6-10 anys) — sistema de disseny TCLAS adaptat a nens.

   Base: l'estil de tots els àlbums T-Clas (A4 vertical, barra blau nit a dalt, títol en serif,
   caixes crema amb filet ocre, blau nit i ocre). Sobre aquesta base, els afegits infantils:

     · LLETRA GRAN I CLARA: Andika (dissenyada per aprendre a llegir) a 12-13 pt; res per sota de 9,5 pt
     · PANELLS amb vora gruixuda, ombra i pestanya de títol: es veuen de lluny
     · CAIXES AMB ICONA (RECORDA ★, SABIES QUE ?, ESCOLTO ♪): cada tipus de caixa es reconeix d'un cop d'ull
     · en Mussol Misol com a guia a cada pàgina (globus de conversa)
     · "ET TROBES AQUÍ": mapa de píndoles amb el tema actual
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
from reportlab.pdfbase import pdfmetrics                       # noqa: E402
from reportlab.pdfbase.pdfmetrics import stringWidth           # noqa: E402
from reportlab.pdfbase.ttfonts import TTFont                   # noqa: E402

from dibujo_mano import ManoCanvas, lineas_texto               # noqa: E402
from mussol import mussol                                       # noqa: E402

W, H = 595.276, 841.89
M = 40
CW = W - 2 * M

NAVY = HexColor('#1A2332')
NAVY_SOFT = HexColor('#3C4A5E')
CREMA = HexColor('#FDFBF6')
WARM = HexColor('#F4EFE3')
WARM2 = HexColor('#EADFC6')          # crema més fosca: capçaleres i fons de caixes
RULE = HexColor('#C9CFD8')
SOMBRA = HexColor('#B9C0CB')
INK = HexColor('#232323')
MUTED = HexColor('#6A7280')
OCRE = HexColor('#8C6A3F')

# colors de les notes (els de tota la vida del cartell)
COL = dict(DO='#E4392B', RE='#F28C0E', MI='#F9C80E', FA='#76B82A', SOL='#2E86C8', LA='#A58AC9',
           SI='#A7A397')
COLNOM = dict(DO='vermell', RE='taronja', MI='groc', FA='verd', SOL='blau', LA='lila', SI='gris')

# lletra: Andika per al cos (llegible per a nens), Quicksand per a etiquetes, DejaVu Serif per als títols
FD = os.path.join(HERE, '..', 'assets', 'fonts_nens')
pdfmetrics.registerFont(TTFont('Andika', os.path.join(FD, 'Andika-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Andika-Bold', os.path.join(FD, 'Andika-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Quicksand-Bold', os.path.join(FD, 'Quicksand-Bold.ttf')))
SANS, SANSB, SERIFB = 'Andika', 'Andika-Bold', 'DejaVuSerif-Bold'
ETQ = 'Quicksand-Bold'
SYM = 'DejaVuSans-Bold'


def Y(t):
    """Coordenada y a partir d'una distància des de dalt de la pàgina."""
    return H - t


# ------------------------------------------------------------------ text
def txt(c, x, y, s, size=12, font=SANS, col=INK, align='l'):
    c.setFillColor(col)
    c.setFont(font, size)
    if align == 'c':
        c.drawCentredString(x, y, s)
    elif align == 'r':
        c.drawRightString(x, y, s)
    else:
        c.drawString(x, y, s)


def par(c, x, y, s, size=12, ample=300, lead=None, font=SANS, col=INK):
    lead = lead or size * 1.36
    for ln in lineas_texto(s, font, size, ample):
        txt(c, x, y, ln, size, font, col)
        y -= lead
    return y


def alt_par(s, size, ample, lead=None, font=SANS):
    return len(lineas_texto(s, font, size, ample)) * (lead or size * 1.36)


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
    c.rect(0, H - 9, W, 9, stroke=0, fill=1)
    txt(c, M, Y(32), kicker, 9.2, ETQ, OCRE)
    txt(c, W - M, Y(32), dreta, 9.2, ETQ, MUTED, 'r')
    txt(c, M, Y(68), titol, 34, SERIFB, NAVY)
    trac(c, 3, OCRE)
    c.line(M, Y(77), M + 46, Y(77))
    par(c, M, Y(96), intro, 12, CW, 15.5, SANS, NAVY_SOFT)
    # peu
    trac(c, 0.8, RULE)
    c.line(M, 40, W - M, 40)
    txt(c, W / 2, 22, 'El Quadern del Pianista  ·  T-Clas', 9, SANS, MUTED, 'c')
    txt(c, W - M, 22, str(num), 10, SANSB, NAVY, 'r')
    txt(c, M, 22, 'PEKES', 9.5, ETQ, OCRE)


def mapa(c, y, items, actiu):
    """ET TROBES AQUÍ: píndoles amb els temes del capítol (s'encongeixen si no hi caben)."""
    txt(c, M, y + 3, 'ET TROBES AQUÍ', 8.6, ETQ, OCRE)
    x0 = M + 92
    avail = W - M - x0
    fs, pad, gap = 9.2, 20, 9
    while fs > 7.2:
        tot = sum(stringWidth(t, ETQ, fs) + pad for t in items) + gap * (len(items) - 1)
        if tot <= avail:
            break
        fs -= 0.4
        pad = max(12, pad - 1)
        gap = max(5, gap - 0.5)
    x = x0
    for k, t in enumerate(items):
        w = stringWidth(t, ETQ, fs) + pad
        on = (k == actiu)
        rr(c, x, y - 6, w, 22, 11, fill=NAVY if on else white, lw=1.3, col=NAVY if on else SOMBRA)
        txt(c, x + w / 2, y + 1, t, fs, ETQ, white if on else NAVY_SOFT, 'c')
        if k < len(items) - 1 and gap >= 8:
            trac(c, 1.3, SOMBRA)
            c.line(x + w + 2, y + 5, x + w + 7, y + 5)
        x += w + gap


# ------------------------------------------------------------------ panells i caixes
def panell(c, x, ytop, w, h, titol=None, n=None, fons=white, vora=NAVY, lw=1.7, ombra=True, tab=NAVY):
    """Panell gran de contingut: ombra, vora gruixuda i pestanya amb el títol (i número de pas).
       Retorna la y interior de dalt (a sota de la pestanya)."""
    y = ytop - h
    if ombra:
        rr(c, x + 3.4, y - 3.4, w, h, 7, fill=SOMBRA, lw=0)
    rr(c, x, y, w, h, 7, fill=fons, lw=lw, col=vora)
    if titol:
        tw = stringWidth(titol, ETQ, 11.5) + 22 + (22 if n else 0)
        trac(c, lw, vora)
        c.setFillColor(tab)
        c.roundRect(x + 12, ytop - 11, tw, 24, 12, stroke=1, fill=1)
        tx = x + 12 + 13
        if n:
            c.setFillColor(OCRE)
            c.circle(x + 12 + 13, ytop + 1, 9, stroke=0, fill=1)
            txt(c, x + 12 + 13, ytop - 3, str(n), 11.5, SANSB, white, 'c')
            tx = x + 12 + 28
        txt(c, tx, ytop - 3, titol, 11.5, ETQ, white)
    return ytop - 26


ICONES = {'RECORDA': '★', 'SABIES QUE?': '?', 'ESCOLTO': '♪', 'PROVA': '✋'}


def caixa_t(c, x, ytop, w, h, etiqueta, text, size=12, icona=None, fons=WARM, vora=OCRE):
    """Caixa crema amb vora gruixuda, cercle d'icona i etiqueta (RECORDA ★, SABIES QUE ?, ESCOLTO ♪)."""
    y = ytop - h
    rr(c, x + 3, y - 3, w, h, 7, fill=HexColor('#DCCFB0'), lw=0)
    rr(c, x, y, w, h, 7, fill=fons, lw=1.7, col=vora)
    ic = icona or ICONES.get(etiqueta, '★')
    c.setFillColor(vora)
    c.circle(x + 26, ytop - 24, 15, stroke=0, fill=1)
    txt(c, x + 26, ytop - 24 - 5.3, ic, 15, SYM, white, 'c')
    txt(c, x + 50, ytop - 28, etiqueta, 12.5, ETQ, vora)
    par(c, x + 14, ytop - 52, text, size, w - 28, size * 1.36)


def caixa(c, x, y, w, h, etiqueta, text, size=12, **kw):
    caixa_t(c, x, y + h, w, h, etiqueta, text, size, **kw)


def guia(c, x, ytop, ample, text, color=False, size=13, h=None):
    """En Mussol Misol fent de guia: figura a l'esquerra i globus de conversa. `ytop` = vora de dalt."""
    h = h or max(90, alt_par(text, size, ample - 126, size * 1.38) + 44)
    y = ytop - h
    mussol(c, x + 40, y + h / 2 - 2, 0.42, color=color, lw=2.8)
    bx = x + 86
    rr(c, bx + 3.4, y - 3.4, ample - 86, h, 11, fill=SOMBRA, lw=0)
    rr(c, bx, y, ample - 86, h, 11, fill=white, lw=1.7, col=NAVY)
    c.setFillColor(white)
    trac(c, 1.7, NAVY)
    c.poly([(bx + 1, y + h / 2 + 10), (bx - 13, y + h / 2), (bx + 1, y + h / 2 - 10)], 1, 1)
    c.setStrokeColor(white)
    c.setLineWidth(3)
    c.line(bx + 1, y + h / 2 + 8, bx + 1, y + h / 2 - 8)
    txt(c, bx + 16, y + h - 20, 'EN MUSSOL MISOL DIU', 9.2, ETQ, OCRE)
    par(c, bx + 16, y + h - 40, text, size, ample - 86 - 32, size * 1.38)
    return h


def quadrat(c, x, y, n, mida=24):
    """El número de pas (cercle ocre)."""
    c.setFillColor(OCRE)
    c.circle(x + mida / 2, y + mida / 2, mida / 2, stroke=0, fill=1)
    txt(c, x + mida / 2, y + mida * 0.3, str(n), 13, SANSB, white, 'c')


def etiqueta_sec(c, x, y, text, size=10.5):
    txt(c, x, y, text, size, ETQ, NAVY)
    trac(c, 2, OCRE)
    c.line(x, y - 5, x + 30, y - 5)


# ------------------------------------------------------------------ teclat
ORDRE = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']


def _tecla_path(c, x, y, w, h, r):
    """Rectangle amb les cantonades de BAIX arrodonides (com una tecla de debò)."""
    k = 0.5523 * r
    p = c.beginPath()
    p.moveTo(x, y + h)
    p.lineTo(x, y + r)
    p.curveTo(x, y + r - k, x + r - k, y, x + r, y)
    p.lineTo(x + w - r, y)
    p.curveTo(x + w - r + k, y, x + w, y + r - k, x + w, y + r)
    p.lineTo(x + w, y + h)
    p.close()
    return p


def degradat(c, path, x0, y0, x1, y1, col_a, col_b):
    c.saveState()
    c.clipPath(path, stroke=0, fill=0)
    c.linearGradient(x0, y0, x1, y1, (col_a, col_b), extend=False)
    c.restoreState()


def teclat(c, x, y, w, h, nb=7, resalta=None, noms=None, color=False, dits=None, lw=1.0, inici=0,
           tira=True, negres=True):
    """Teclat real de `nb` tecles blanques a partir de la nota `inici` (0 = DO). Les negres queden on toca
       (entre DO-RE, RE-MI, FA-SOL, SOL-LA i LA-SI). `resalta`: {índex: nom}. `noms`: 'resalta' o 'totes'."""
    resalta = resalta or {}
    dits = dits or {}
    kw = w / float(nb)
    r = min(3.0, kw * 0.14)
    # tira de feltre de dalt (la "vora" del teclat)
    if tira:
        rr(c, x - 3, y + h - 1.5, w + 6, 8, 2.5, fill=NAVY_SOFT, lw=0)
        c.setFillColor(HexColor('#8C2F39'))
        c.rect(x, y + h - 2.2, w, 2.4, stroke=0, fill=1)
    # sombra de sota
    rr(c, x + 2, y - 2.2, w, h, r, fill=SOMBRA, lw=0)
    for i in range(nb):
        nm = resalta.get(i)
        pth = _tecla_path(c, x + i * kw, y, kw, h, r)
        if nm and color:
            base = HexColor(COL[nm])
            c.setFillColor(base)
            c.drawPath(pth, stroke=0, fill=1)
            degradat(c, _tecla_path(c, x + i * kw, y, kw, h, r), 0, y + h, 0, y, base, base.clone(red=base.red * 0.86, green=base.green * 0.86, blue=base.blue * 0.86))
        else:
            c.setFillColor(white)
            c.drawPath(pth, stroke=0, fill=1)
            ton = HexColor('#DCD5C2') if nm else HexColor('#EFEBDF')
            degradat(c, _tecla_path(c, x + i * kw, y, kw, h, r), 0, y + h * 0.55, 0, y, white if not nm else HexColor('#EEE9DA'), ton)
        trac(c, lw, NAVY)
        c.drawPath(_tecla_path(c, x + i * kw, y, kw, h, r), stroke=1, fill=0)
        # el "llavi" de la tecla (la cara del davant)
        trac(c, 0.6, HexColor('#B9B29E'))
        c.line(x + i * kw + 1.4, y + h * 0.085, x + (i + 1) * kw - 1.4, y + h * 0.085)
    bw, bh = kw * 0.58, h * 0.62
    for i in range(nb - 1):
        if negres and (inici + i) % 7 in (0, 1, 3, 4, 5):
            bx = x + (i + 1) * kw - bw / 2.0
            by = y + h - bh
            c.setFillColor(NAVY)
            trac(c, 0.8, NAVY)
            c.drawPath(_tecla_path(c, bx, by, bw, bh, min(2.2, bw * 0.2)), stroke=1, fill=1)
            c.setFillColor(HexColor('#2C3647'))
            c.drawPath(_tecla_path(c, bx + bw * 0.14, by + bh * 0.18, bw * 0.72, bh * 0.78, min(1.6, bw * 0.15)), stroke=0, fill=1)
            c.setFillColor(HexColor('#566680'))
            c.rect(bx + bw * 0.2, by + bh * 0.3, bw * 0.08, bh * 0.5, stroke=0, fill=1)
    for i in range(nb):
        nm = ORDRE[(inici + i) % 7]
        if (noms == 'totes') or (noms == 'resalta' and i in resalta):
            on = i in resalta
            txt(c, x + i * kw + kw / 2, y + 5.5, nm, 11.5 if on else 9, SANSB if on else SANS,
                (INK if (on and (not color or nm == 'MI')) else (white if on else MUTED)), 'c')
        if i in dits:
            cx, cy = x + i * kw + kw / 2, y + h * 0.28 + 10
            c.setFillColor(NAVY)
            c.circle(cx, cy, 8.5, stroke=0, fill=1)
            txt(c, cx, cy - 4.2, str(dits[i]), 11.5, SANSB, white, 'c')


# ------------------------------------------------------------------ pentagrama
def pauta(c, x, ytop, w, gap, clau='treble', final=True, lw=1.0):
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


def xip(c, x, y, w, text, fill=white, col=INK, h=24, size=11):
    rr(c, x, y, w, h, 12, fill=fill, lw=1.4, col=NAVY)
    txt(c, x + w / 2, y + h * 0.3, text, size, SANSB, col, 'c')


# ------------------------------------------------------------------ figures de ritme
def banderola(c, x, y, s, fill=white):
    pts = []
    a, b, c2, d = (x, y), (x + 9 * s, y - 7 * s), (x + 17 * s, y - 12 * s), (x + 10 * s, y - 25 * s)
    for t in [i / 8.0 for i in range(9)]:
        u = 1 - t
        pts.append((u ** 3 * a[0] + 3 * u * u * t * b[0] + 3 * u * t * t * c2[0] + t ** 3 * d[0],
                    u ** 3 * a[1] + 3 * u * u * t * b[1] + 3 * u * t * t * c2[1] + t ** 3 * d[1]))
    a, b, c2, d = (x + 10 * s, y - 25 * s), (x + 12 * s, y - 14 * s), (x + 5 * s, y - 9 * s), (x, y - 8 * s)
    for t in [i / 8.0 for i in range(1, 9)]:
        u = 1 - t
        pts.append((u ** 3 * a[0] + 3 * u * u * t * b[0] + 3 * u * t * t * c2[0] + t ** 3 * d[0],
                    u ** 3 * a[1] + 3 * u * u * t * b[1] + 3 * u * t * t * c2[1] + t ** 3 * d[1]))
    trac(c, 1.0, NAVY)
    c.setFillColor(NAVY)
    c.poly(pts, 1, 1)


def figura(c, tipus, cx, cy, gap=6.0):
    """Figures soltes (cap + plica): 'w' rodona, 'h' blanca, 'q' negra, 'e' corxera."""
    if tipus == 'ee':
        cap(c, cx, cy, gap, 'q')
        cap(c, cx + gap * 3.6, cy, gap, 'q')
        trac(c, 1.3, NAVY)
        top = cy + gap * 3.3
        c.line(cx + gap * 3.6 + gap * 0.74, cy + gap * 0.1, cx + gap * 3.6 + gap * 0.74, top)
        c.setFillColor(NAVY)
        c.poly([(cx + gap * 0.74, top), (cx + gap * 3.6 + gap * 0.74, top), (cx + gap * 3.6 + gap * 0.74, top - gap * 0.75),
                (cx + gap * 0.74, top - gap * 0.75)], 1, 1)
        return
    cap(c, cx, cy, gap, 'w' if tipus == 'w' else ('h' if tipus == 'h' else 'q'))
    if tipus == 'e':
        banderola(c, cx + gap * 0.74, cy + gap * 3.3, gap / 6.0)


# ------------------------------------------------------------------ peces d'ús comú
def consigna(c, x, y, text, ample=480, size=11.5):
    """La instrucció d'un joc, sota la pestanya del panell."""
    return par(c, x, y, text, size, ample, size * 1.34, SANS, NAVY_SOFT)


def franja(c, x, ytop, w, h, etiqueta, text, size=12.5, vora=OCRE, fons=WARM):
    """Caixa baixa: icona + etiqueta + text (d'una o diverses línies, centrat en vertical)."""
    y = ytop - h
    rr(c, x + 3, y - 3, w, h, 7, fill=HexColor('#DCCFB0'), lw=0)
    rr(c, x, y, w, h, 7, fill=fons, lw=1.7, col=vora)
    c.setFillColor(vora)
    c.circle(x + 26, y + h / 2, 14, stroke=0, fill=1)
    txt(c, x + 26, y + h / 2 - 5, ICONES.get(etiqueta, '★'), 14, SYM, white, 'c')
    txt(c, x + 50, y + h / 2 - 4.5, etiqueta, 12.5, ETQ, vora)
    ex = x + 50 + stringWidth(etiqueta, ETQ, 12.5) + 12
    ample = w - (ex - x) - 12
    ll = lineas_texto(text, SANS, size, ample)
    lead = size * 1.3
    y0 = y + h / 2 + (len(ll) - 1) * lead / 2 - size * 0.34
    for k, ln in enumerate(ll):
        txt(c, ex, y0 - k * lead, ln, size, SANS, INK)


def pill_dit(c, x, y, w, ma_txt, n):
    """Pastilla amb el dit: cercle blau nit amb el número + 'mà dreta' / 'mà esq.'."""
    rr(c, x, y, w, 26, 13, fill=WARM, lw=1.4, col=NAVY)
    c.setFillColor(NAVY)
    c.circle(x + 14, y + 13, 10, stroke=0, fill=1)
    txt(c, x + 14, y + 8.6, str(n), 13, SANSB, white, 'c')
    txt(c, x + 30, y + 8.4, ma_txt, 11.5, SANSB, INK)


# ------------------------------------------------------------------ pàgina d'un tema del llibre
import nens_pla as pla                                           # noqa: E402


def pagina_tema(c, n, titol, intro, tipus, color=False, mapa_on=True):
    """Capçalera estàndard d'un tema: tipus 'teoria' (porta mapa) o 'jocs'. Retorna el número de pàgina."""
    t = pla.TEMES[n]
    num = t['pag'] + (0 if tipus == 'teoria' else t['pags'] - 1)
    pagina(c, pla.kicker(n), titol, 'Tema %d  ·  %s' % (n, 'teoria' if tipus == 'teoria' else 'jocs'), intro, num, color)
    if tipus == 'teoria' and mapa_on:
        items, act = pla.pagines_cap(n)
        mapa(c, Y(124), items, act)
    return num
