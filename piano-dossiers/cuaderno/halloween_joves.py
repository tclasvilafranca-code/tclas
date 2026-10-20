# -*- coding: utf-8 -*-
"""HALLOWEEN · fitxes per pintar, cantar i tocar · versio JOVES (12-20 anys) · en catala.

   Portada + 6 fitxes A4 verticals. Cada fitxa: 01 PINTA (un mandala per acolorir, que alhora
   ensenya alguna cosa), 02 CANTA, 03 TOCA (pentagrama gravat amb el motor de notacio). Tot el
   material musical és propi o és teoria (escales, intervals, acords): res amb drets d'autor.

   1 L'escala embruixada (La menor harmònica)   4 Riff de la nit (ostinato i matisos)
   2 El tritó (l'interval del diable)           5 Improvisa amb la lluna (pentatònica)
   3 Acords que fan por (cadència andalusa)     6 Missatges secrets (notes = lletres)

   python3 halloween_joves.py  ->  ../output/Halloween_Joves.pdf
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
sys.path.insert(0, HERE)
import notation as nt                                           # noqa: E402
from page_layout_common import before_staff, after_system       # noqa: E402
from reportlab.lib.colors import HexColor, white, black        # noqa: E402
from reportlab.pdfbase.pdfmetrics import stringWidth           # noqa: E402

from dibujo_mano import ManoCanvas, trazo, lineas_texto         # noqa: E402
import halloween_dib as hd                                      # noqa: E402

OUT = os.path.join(HERE, '..', 'output', 'Halloween_Joves.pdf')
W, H = 595.276, 841.89
M = 40
CW = W - 2 * M
PLUM = HexColor('#2A1740')
PURPLE = HexColor('#6B3FA0')
ORANGE = HexColor('#E8742C')
CREAM = HexColor('#FBF7EE')
INK = HexColor('#241B2F')
MUTED = HexColor('#7A6F8A')
LAV = HexColor('#EDE6F5')
GOLD = HexColor('#C9A227')
SANS, SANSB, SERIFB = 'DejaVuSans', 'DejaVuSans-Bold', 'DejaVuSerif-Bold'


# ------------------------------------------------------------------ text
def t(c, x, y, s, size=10, font=SANS, col=INK, align='l'):
    c.setFillColor(col)
    c.setFont(font, size)
    {'l': c.drawString, 'c': c.drawCentredString, 'r': c.drawRightString}[align](x, y, s)


def par(c, x, y, s, size=9.4, w=CW, lead=None, font=SANS, col=INK, align='l'):
    lead = lead or size * 1.45
    for ln in lineas_texto(s, font, size, w):
        t(c, x if align == 'l' else x + w / 2.0, y, ln, size, font, col, align)
        y -= lead
    return y


def alt(s, size, w, lead=None, font=SANS):
    return len(lineas_texto(s, font, size, w)) * (lead or size * 1.45)


# ------------------------------------------------------------------ pàgina
def pagina(c, n, kicker, titol, sub, deco=0):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(PLUM)
    c.rect(0, H - 128, W, 128, stroke=0, fill=1)
    c.setFillColor(ORANGE)
    c.rect(0, H - 132, W, 4, stroke=0, fill=1)
    # ratpenats i lluna decoratius dins la franja
    c.saveState()
    trazo(c, 1.4, col=HexColor('#9A7BC4'))
    c.setFillColor(HexColor('#3A2358'))
    hd.murcielago(c, W - 70, H - 62, 0.55, lw=1.3)
    hd.murcielago(c, W - 150, H - 98, 0.32, lw=1.1)
    c.restoreState()
    t(c, M, H - 36, kicker, 8.6, SANSB, ORANGE)
    t(c, W - M, H - 36, 'T-Clas · Nit de Halloween', 8.2, SANS, HexColor('#B9A5D6'), 'r')
    size = 27
    while stringWidth(titol, SERIFB, size) > CW - 120 and size > 18:
        size -= 1
    t(c, M, H - 76, titol, size, SERIFB, white)
    t(c, M, H - 100, sub, 10.4, SANS, HexColor('#D9CCEE'))
    # peu
    trazo(c, 0.8, col=HexColor('#D7CDE6'))
    c.line(M, 46, W - M, 46)
    t(c, M, 30, 'Nom: ____________________________', 9, SANS, MUTED)
    t(c, W - M, 30, 'Fitxa %d de 6' % n, 9, SANSB, PURPLE, 'r')


def seccio(c, y, num, titol, nota=''):
    """Cinta de secció: 01 PINTA... Torna la y de sota."""
    c.setFillColor(ORANGE)
    c.circle(M + 11, y + 4, 11, stroke=0, fill=1)
    t(c, M + 11, y, num, 10, SANSB, white, 'c')
    t(c, M + 30, y, titol, 12.5, SERIFB, PLUM)
    if nota:
        t(c, M + 32 + stringWidth(titol, SERIFB, 12.5) + 8, y, nota, 8.6, SANS, MUTED)
    trazo(c, 0.9, col=HexColor('#CFC3E2'))
    c.line(M + 32 + stringWidth(titol, SERIFB, 12.5) + (14 + stringWidth(nota, SANS, 8.6) if nota else 6),
           y + 4, W - M, y + 4)
    return y - 18


def caixa(c, x, y, w, h, titol=None, fons=LAV, vora=None):
    """(x, y) = cantonada inferior esquerra."""
    c.setFillColor(fons)
    c.setStrokeColor(vora or fons)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, 7, stroke=1 if vora else 0, fill=1)
    if titol:
        t(c, x + 10, y + h - 15, titol, 7.8, SANSB, PURPLE)


def cap_pent(c, x, y, s):
    t(c, x, y, s, 8, SANSB, PURPLE)


def sistema(c, x, y, w, gap, ev, clau='treble', ts=(4, 4), caption=None, show_time=True):
    """Pentagrama amb caption; torna la y de sota (llesta per al següent)."""
    if caption:
        cap_pent(c, x, y, caption)
    y -= before_staff(gap, ev, clau)
    top, bot = nt.draw_system(c, x, y, w, gap, ev, clef=clau, time_sig=ts, show_time=show_time)
    return bot - after_system(gap, ev, clau)


def gran(c, x, y, w, gap, ev_t, ev_b, ts=(4, 4), caption=None, sep=7.6):
    if caption:
        cap_pent(c, x, y, caption)
    yy = y - before_staff(gap, ev_t, 'treble')
    t_top, t_bot = nt.draw_system(c, x, yy, w, gap, ev_t, clef='treble', time_sig=ts)
    yy2 = t_bot - gap * sep
    b_top, b_bot = nt.draw_system(c, x, yy2, w, gap, ev_b, clef='bass', time_sig=ts)
    trazo(c, 1.2, col=black)
    c.line(x, t_top, x, b_bot)
    return b_bot - after_system(gap, ev_b, 'bass')


def nota(p, d='q', n=None, **k):
    e = dict(pitch=p, dur=d)
    if n:
        e['number'] = n
    e.update(k)
    return e


def acord(ps, d='w', **k):
    e = dict(pitches=ps, dur=d)
    e.update(k)
    return e


def silenci(d='q'):
    return dict(rest=True, dur=d)


# ------------------------------------------------------------------ mandales
def _poli(c, pts, fill=white, lw=1.3, col=PLUM, closed=True):
    trazo(c, lw, col=col)
    c.setFillColor(fill)
    c.poly(pts, 1, 1 if closed else 0, closed=closed)


def _roda(c, cx, cy, ang, f):
    """Transforma un punt local (x, y) girat `ang` graus."""
    a = math.radians(ang)
    return lambda x, y: (cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a))


def _fulla(c, cx, cy, ang, r0, r1, w, fill=white, lw=1.3, col=PLUM):
    T = _roda(c, cx, cy, ang, None)
    pts = []
    n = 14
    for i in range(n + 1):
        u = i / float(n)
        x = r0 + (r1 - r0) * u
        pts.append(T(x, w * math.sin(math.pi * u) ** 0.8))
    for i in range(n, -1, -1):
        u = i / float(n)
        x = r0 + (r1 - r0) * u
        pts.append(T(x, -w * math.sin(math.pi * u) ** 0.8))
    _poli(c, pts, fill, lw, col)
    return T


def _cercle(c, cx, cy, r, fill=white, lw=1.3, col=PLUM):
    trazo(c, lw, col=col)
    c.setFillColor(fill)
    c.circle(cx, cy, r, stroke=1, fill=1)


def _estrella(c, cx, cy, R, r, n, giro=90, fill=white, lw=1.2, col=PLUM):
    pts = []
    for i in range(2 * n):
        a = math.radians(giro + i * 180.0 / n)
        rr = R if i % 2 == 0 else r
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    _poli(c, pts, fill, lw, col)


def _corona(c, cx, cy, R, n, rl, lw=1.2, col=PLUM):
    """Corona de lòbuls (festons) de radi rl sobre la circumferència R."""
    for k in range(n):
        a = math.radians(90 + k * 360.0 / n)
        _cercle(c, cx + R * math.cos(a), cy + R * math.sin(a), rl, white, lw, col)


def mandala_rosassa(c, cx, cy, R, etiquetes):
    n = len(etiquetes)
    _corona(c, cx, cy, R * 0.86, 24, R * 0.095)
    _cercle(c, cx, cy, R * 0.86, white, 1.5)
    _cercle(c, cx, cy, R * 0.80, white, 0.8)
    for k in range(n):
        ang = 90 - k * 360.0 / n
        _fulla(c, cx, cy, ang, R * 0.28, R * 0.78, R * 0.15)
    _estrella(c, cx, cy, R * 0.3, R * 0.14, n, 90)
    _cercle(c, cx, cy, R * 0.07, PLUM)
    for k, et in enumerate(etiquetes):
        a = math.radians(90 - k * 360.0 / n)
        px, py = cx + R * 0.56 * math.cos(a), cy + R * 0.56 * math.sin(a)
        t(c, px, py - 3, et, 8.6, SANSB, PLUM, 'c')
    for k in range(n):
        a = math.radians(90 - (k + 0.5) * 360.0 / n)
        _estrella(c, cx + R * 0.72 * math.cos(a), cy + R * 0.72 * math.sin(a), R * 0.05, R * 0.02, 4, 90, PLUM, 0.6)


def mandala_rellotge(c, cx, cy, R, noms):
    n = 12
    r0, r1 = R * 0.34, R * 0.86
    for k in range(n):
        a0 = math.radians(90 - k * 30 + 15)
        a1 = math.radians(90 - k * 30 - 15)
        pts = []
        for i in range(7):
            a = a0 + (a1 - a0) * i / 6.0
            pts.append((cx + r1 * math.cos(a), cy + r1 * math.sin(a)))
        for i in range(6, -1, -1):
            a = a0 + (a1 - a0) * i / 6.0
            pts.append((cx + r0 * math.cos(a), cy + r0 * math.sin(a)))
        _poli(c, pts, white, 1.3)
        am = math.radians(90 - k * 30)
        t(c, cx + (r0 + r1) / 2 * math.cos(am), cy + (r0 + r1) / 2 * math.sin(am) - 3, noms[k], 8, SANSB, PLUM, 'c')
    _corona(c, cx, cy, R * 0.93, 36, R * 0.035)
    # diàmetres: cada tritó és un diàmetre
    trazo(c, 0.9, col=PURPLE)
    for k in range(6):
        a = math.radians(90 - k * 30)
        c.line(cx + r0 * 0.96 * math.cos(a), cy + r0 * 0.96 * math.sin(a),
               cx - r0 * 0.96 * math.cos(a), cy - r0 * 0.96 * math.sin(a))
    _cercle(c, cx, cy, R * 0.07, PLUM)


def mandala_vitralls(c, x, y, w, h, acords):
    """Quatre finestres gòtiques en fila (x, y = cantonada inferior esquerra)."""
    n = len(acords)
    gw = w / float(n)
    for k, (nom, notes) in enumerate(acords):
        x0 = x + k * gw + gw * 0.2
        ww = gw * 0.6
        top = y + h * 0.78
        pts = [(x0, y), (x0 + ww, y), (x0 + ww, top)]
        for i in range(1, 12):
            a = math.pi * i / 12.0
            pts.append((x0 + ww / 2 + ww / 2 * math.cos(a), top + ww * 0.62 * math.sin(a)))
        pts.append((x0, top))
        _poli(c, pts, white, 1.6)
        cxm = x0 + ww / 2
        trazo(c, 1.0, col=PLUM)
        c.line(cxm, y, cxm, top + ww * 0.62)
        c.line(x0, y + (top - y) * 0.35, x0 + ww, y + (top - y) * 0.35)
        c.line(x0, y + (top - y) * 0.68, x0 + ww, y + (top - y) * 0.68)
        _cercle(c, cxm, top + ww * 0.2, ww * 0.2, white, 1.0)
        _estrella(c, cxm, top + ww * 0.2, ww * 0.15, ww * 0.07, 6, 90, white, 0.8)
        t(c, cxm, y - 12, nom, 8.6, SANSB, PLUM, 'c')
        t(c, cxm, y - 23, notes, 7.6, SANS, MUTED, 'c')


def mandala_ratpenats(c, cx, cy, R):
    _cercle(c, cx, cy, R * 0.98, white, 1.5)
    _cercle(c, cx, cy, R * 0.9, white, 0.7)
    # teranyina central
    for k in range(8):
        a = math.radians(k * 45)
        trazo(c, 0.9, col=PLUM)
        c.line(cx, cy, cx + R * 0.52 * math.cos(a), cy + R * 0.52 * math.sin(a))
    for r_ in (0.16, 0.30, 0.44, 0.56):
        pts = [(cx + R * r_ * math.cos(math.radians(k * 45)), cy + R * r_ * math.sin(math.radians(k * 45)))
               for k in range(8)]
        trazo(c, 0.9, col=PLUM)
        c.poly(pts, 1, 0, closed=True)
    for k in range(8):
        a = math.radians(90 - k * 45)
        hd.murcielago(c, cx + R * 0.74 * math.cos(a), cy + R * 0.74 * math.sin(a), R / 230.0 * 1.3, lw=1.2)
    _corona(c, cx, cy, R * 0.98, 32, R * 0.03, 0.8)


def fase_lluna(c, cx, cy, r, fase):
    """Fase 0..7: 0 nova, 1 creixent, 2 quart creixent, 3 gibosa creixent, 4 plena..."""
    _cercle(c, cx, cy, r, white, 1.4)
    trazo(c, 1.2, col=PLUM)
    if fase == 4:
        return
    if fase == 0:
        c.setFillColor(PLUM)
        c.circle(cx, cy, r * 0.96, stroke=0, fill=1)
        return
    # terminador: elipse de semieix |cos|·r
    k = {1: 0.55, 2: 0.0, 3: -0.55, 5: -0.55, 6: 0.0, 7: 0.55}[fase]
    creix = fase < 4
    pts = []
    for i in range(0, 181, 12):
        a = math.radians(90 - i) if creix else math.radians(90 + i)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    for i in range(180, -1, -12):
        a = math.radians(90 - i)
        x = k * r * math.cos(a) * (1 if creix else -1)
        pts.append((cx + x, cy + r * math.sin(a)))
    c.setFillColor(HexColor('#D9CCEE'))
    c.poly(pts, 1, 1, closed=True)


def mandala_lluna(c, cx, cy, R):
    _cercle(c, cx, cy, R * 0.98, white, 1.5)
    _corona(c, cx, cy, R * 0.98, 40, R * 0.03, 0.8)
    for k in range(8):
        a = math.radians(90 - k * 45)
        fase_lluna(c, cx + R * 0.66 * math.cos(a), cy + R * 0.66 * math.sin(a), R * 0.2, k)
        t(c, cx + R * 0.66 * math.cos(a), cy + R * 0.66 * math.sin(a) - R * 0.31, str(k + 1), 7.5, SANSB, PURPLE, 'c')
    _estrella(c, cx, cy, R * 0.36, R * 0.15, 8, 90)
    _cercle(c, cx, cy, R * 0.06, PLUM)


def mandala_calavera(c, cx, cy, R):
    _corona(c, cx, cy, R * 0.88, 18, R * 0.1)
    _cercle(c, cx, cy, R * 0.88, white, 1.5)
    for k in range(9):
        ang = 90 - k * 40
        _fulla(c, cx, cy, ang, R * 0.5, R * 0.8, R * 0.1)
    for k in range(9):
        a = math.radians(90 - (k + 0.5) * 40)
        _estrella(c, cx + R * 0.66 * math.cos(a), cy + R * 0.66 * math.sin(a), R * 0.07, R * 0.03, 5, 90)
    _cercle(c, cx, cy, R * 0.47, white, 1.2)
    hd.calavera(c, cx, cy + R * 0.02, R / 110.0 * 1.1, lw=1.5)


# ------------------------------------------------------------------ utilitats de fitxa
def bloc_pinta(c, y, mandala, text, nota_titol=None, nota=None, R=86):
    """01 PINTA: mandala a l'esquerra, instruccions i caixa d'informació a la dreta."""
    y = seccio(c, y, '01', 'PINTA', 'color, relaxa i aprèn')
    cx, cy = M + R + 4, y - R - 6
    mandala(c, cx, cy, R)
    xt = M + 2 * R + 28
    wt = W - M - xt
    yy = par(c, xt, y - 8, text, 9.6, wt, 14)
    if nota:
        h = alt(nota, 8.8, wt - 20, 12.8) + 36
        caixa(c, xt, yy - h - 4, wt, h, nota_titol, LAV)
        par(c, xt + 10, yy - 32, nota, 8.8, wt - 20, 12.8)
    return y - 2 * R - 22


def bloc_canta(c, y, text, h=None):
    y = seccio(c, y, '02', 'CANTA', 'abans de tocar, la veu ja ho sap')
    h = h or alt(text, 9.6, CW - 24, 14) + 18
    caixa(c, M, y - h + 8, CW, h, None, LAV)
    par(c, M + 12, y - 8, text, 9.6, CW - 24, 14)
    return y - h - 6


def caixa_nota(c, x, y, w, titol, text, size=8.8):
    h = alt(text, size, w - 20, size * 1.45) + 36
    caixa(c, x, y - h, w, h, titol, LAV)
    par(c, x + 10, y - 32, text, size, w - 20, size * 1.45)
    return h


# ------------------------------------------------------------------ fitxa 1
def f1(c):
    pagina(c, 1, 'HALLOWEEN · ESCALES', "L'escala embruixada", "La menor harmònica: l'escala que fa por")
    y = 690
    y = bloc_pinta(c, y, lambda cc, cx, cy, R: mandala_rosassa(cc, cx, cy, R,
                                                               ['LA', 'SI', 'DO', 'RE', 'MI', 'FA', 'SOL♯', 'LA']),
                   'Pinta cada pètal amb el color que vulguis, un per a cada nota. Quan acabis, fixa\'t en els '
                   'pètals FA i SOL♯: són els que sonen més «espantosos».',
                   'PER QUÈ FA POR?',
                   "Entre FA i SOL♯ hi ha tres semitons (una segona augmentada). L'escala menor natural "
                   "no té aquest salt: només la harmònica.")
    y = bloc_canta(c, y, "Canta l'escala amunt i avall amb els noms: la – si – do – re – mi – fa – sol♯ – la. "
                         "En el salt fa–sol♯ fes un crescendo, com si s'obrís una porta. Repeteix-ho dues vegades, "
                         "cada cop més suau.")
    y = seccio(c, y, '03', 'TOCA', 'dues mans i una idea per inventar')
    g = 7.4
    asc = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G#5', 'A5']
    ev = [nota(p, 'q', n) for p, n in zip(asc + asc[::-1], [1, 2, 3, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 3, 2, 1])]
    y = sistema(c, M, y - 6, CW, g, ev, 'treble', (4, 4), 'MÀ DRETA · La menor harmònica, una octava amunt i avall')
    asc_b = ['A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G#3', 'A3']
    ev = [nota(p, 'q', n) for p, n in zip(asc_b + asc_b[::-1], [5, 4, 3, 2, 1, 3, 2, 1, 1, 2, 3, 1, 2, 3, 4, 5])]
    y = sistema(c, M, y - 4, CW, g, ev, 'bass', (4, 4), 'MÀ ESQUERRA · el mateix, dues octaves més greu')
    y -= 6
    et = [nota('F5', 'q'), nota('G#5', 'q'), nota('A5', 'h'), nota('G#5', 'q'), nota('F5', 'q'), nota('E5', 'h')]
    eb = [acord(['A2', 'E3'], 'w'), acord(['A2', 'E3'], 'w')]
    y = gran(c, M, y, CW, g, et, eb, (4, 4), "IMPROVISA · mini-motiu sobre LA + MI a la mà esquerra (quinta buida)")
    caixa_nota(c, M, y + 4, CW, 'REPTE',
               "Toca l'escala de tres maneres: lligada (legato), picada (staccato) i cada cop més ràpida. "
               "Després, ajunta mans en moviment paral·lel. Inventa un motiu de dos compassos amb el salt "
               "FA–SOL♯ i toca'l sobre la quinta buida de la mà esquerra.")
    c.showPage()


# ------------------------------------------------------------------ fitxa 2
def f2(c):
    pagina(c, 2, 'HALLOWEEN · INTERVALS', 'El tritó', "L'interval del diable · diabolus in musica")
    y = 690
    noms = ['DO', 'DO♯', 'RE', 'RE♯', 'MI', 'FA', 'FA♯', 'SOL', 'SOL♯', 'LA', 'LA♯', 'SI']
    y = bloc_pinta(c, y, lambda cc, cx, cy, R: mandala_rellotge(cc, cx, cy, R, noms),
                   "Aquest és el rellotge de les 12 notes. Els sectors oposats formen un tritó (sis semitons): "
                   "DO–FA♯, DO♯–SOL, RE–SOL♯, RE♯–LA, MI–LA♯, FA–SI. Pinta cada parella del mateix color!",
                   'SABIES QUE…?',
                   "A la Dansa macabra (1874), Saint-Saëns fa que el violí de la Mort afini la corda de Mi mig to "
                   "més baixa i sona un tritó (La–Mi♭). A l'edat mitjana se l'anomenava «diabolus in musica».")
    y = bloc_canta(c, y, "Canta un DO i aguanta'l. Ara salta a FA♯: aquest salt de tres tons enters és el tritó, el "
                         "més inquietant. Resol-lo pujant un semitò (FA♯ → SOL) i nota com es calma la tensió.")
    y = seccio(c, y, '03', 'TOCA', 'del so inquietant al so de pau')
    g = 7.4
    et = [nota('A4', 'q'), nota('Eb5', 'q'), nota('A4', 'q'), nota('Eb5', 'q'),
          nota('A4', 'q'), nota('Eb5', 'q'), nota('A4', 'q'), nota('Eb5', 'q'),
          nota('Eb5', 'q'), nota('Eb5', 'q'), nota('E5', 'h'), nota('A4', 'w')]
    eb = [acord(['A2', 'Eb3'], 'h'), acord(['A2', 'Eb3'], 'h'), acord(['A2', 'Eb3'], 'h'),
          acord(['A2', 'Eb3'], 'h'), acord(['A2', 'Eb3'], 'h'), acord(['A2', 'E3'], 'h'),
          acord(['A2', 'E3'], 'w')]
    y = gran(c, M, y - 6, CW, g, et, eb, (4, 4),
             'LA + MI♭ = tritó (compassos 1-3) · el MI♭ puja un semitò i arriba la quinta LA + MI (compàs 4)')
    y -= 8
    h1 = caixa_nota(c, M, y, 250, 'ON ÉS EL TRITÓ AL PIANO?',
                    "Compta sis semitons (sis tecles, blanques i negres) des de DO: arribes a FA♯. "
                    "Prova-ho des de RE, MI, FA...")
    caixa_nota(c, M + 265, y, CW - 265, 'REPTE',
               "Toca els compassos 1-3 molt fluix (pp) amb pedal de silenci mental: només escolta. "
               "Al compàs 4 fes un diminuendo: sents com el misteri es calma?")
    c.showPage()


# ------------------------------------------------------------------ fitxa 3
def f3(c):
    pagina(c, 3, 'HALLOWEEN · ACORDS', 'Acords que fan por', 'La cadència andalusa: La menor – Sol – Fa – Mi')
    y = 690
    acords = [('La menor', 'la · do · mi'), ('Sol major', 'sol · si · re'),
              ('Fa major', 'fa · la · do'), ('Mi major', 'mi · sol♯ · si')]
    y = seccio(c, y, '01', 'PINTA', 'vitralls de la casa embruixada')
    mandala_vitralls(c, M + 8, y - 118, CW - 16, 74, acords)
    yy = y - 118 - 32
    h = caixa_nota(c, M, yy, CW, 'COM ES PINTA',
                   "Pinta cada vitrall amb una família de colors (per exemple: La menor, morats; Sol, blaus; "
                   "Fa, verds; Mi, vermells). El Mi major és el més brillant: té el SOL♯ que «demana» tornar "
                   "a La menor (dominant → tònica).")
    y = yy - h - 12
    y = bloc_canta(c, y, "Canta l'arpegi de cada acord de baix a dalt: la-do-mi · sol-si-re · fa-la-do · "
                         "mi-sol♯-si. Després canta només la nota més greu de cada acord: LA – SOL – FA – MI, "
                         "una escala que baixa.")
    y = seccio(c, y, '03', 'TOCA', 'acords i arpegis')
    g = 7.0
    sets = [('La menor', ['A4', 'C5', 'E5'], 'A2'), ('Sol major', ['G4', 'B4', 'D5'], 'G2'),
            ('Fa major', ['F4', 'A4', 'C5'], 'F2'), ('Mi major', ['E4', 'G#4', 'B4'], 'E2')]
    et = [acord(ps, 'w', label=nom) for nom, ps, _ in sets]
    eb = [nota(r, 'w') for _, _, r in sets]
    y = gran(c, M, y - 4, CW, g, et, eb, (4, 4), 'ACORDS · mà dreta 1-3-5, mà esquerra la nota més greu', sep=5.8)
    y -= 4
    et = []
    eb = []
    quinta = {'A2': 'E3', 'G2': 'D3', 'F2': 'C3', 'E2': 'B2'}
    for k, (nom, ps, r) in enumerate(sets):
        arp = [ps[0], ps[1], ps[2], ps[1]] * 2
        for i, p in enumerate(arp):
            et.append(nota(p, 'e', beam=k * 2 + i // 4))
        eb += [nota(r, 'h'), nota(quinta[r], 'h')]
    y = gran(c, M, y - 18, CW, g, et, eb, (4, 4), 'ARPEGIS · els mateixos acords repartits en corxeres', sep=5.8)
    caixa_nota(c, M, y + 6, CW, 'REPTE',
               "Toca la progressió amb la mà dreta en acords i la mà esquerra en octaves (LA, SOL, FA, MI). "
               "Després inventa un ritme propi de dos compassos i repeteix-lo sobre els quatre acords.")
    c.showPage()


# ------------------------------------------------------------------ fitxa 4
def f4(c):
    pagina(c, 4, 'HALLOWEEN · RITME', 'Riff de la nit', "Ostinato, silencis i matisos: p i f")
    y = 690
    y = bloc_pinta(c, y, mandala_ratpenats,
                   "Pinta els ratpenats: els de dalt, ben foscos (piano); els de baix, més brillants (forte). "
                   "Quan toquis el riff, torna a mirar el mandala i recorda quin és quin.",
                   'EL RIFF EN BREU',
                   "Mà esquerra: un ostinato de corxeres LA–MI (quinta buida). Mà dreta: LA, SI♭, LA, SOL♯, LA, "
                   "un motiu cromàtic que gira al voltant del LA.")
    y = bloc_canta(c, y, "Diu el ritme amb sílabes: «ti-ti ti-ti ta (sh)», dues vegades; després «ti-ti ti-ti ta-a». "
                         "Cada «ti» és una corxera; «ta» és una negra; «sh» és el silenci. Taral·leja el motiu amb "
                         "els noms: la – si♭ – la – sol♯ – la.")
    y = seccio(c, y, '03', 'TOCA', 'un riff de quatre compassos')
    g = 7.4
    et = [nota('A4', 'e', beam=0, matiz='p'), nota('Bb4', 'e', beam=0), nota('A4', 'e', beam=0), nota('G#4', 'e', beam=0),
          nota('A4', 'q'), silenci('q'),
          nota('A4', 'e', beam=1), nota('Bb4', 'e', beam=1), nota('A4', 'e', beam=1), nota('G#4', 'e', beam=1),
          nota('A4', 'q'), silenci('q'),
          nota('C5', 'e', beam=2, matiz='f'), nota('B4', 'e', beam=2), nota('Bb4', 'e', beam=2), nota('A4', 'e', beam=2),
          nota('E4', 'q'), silenci('q'),
          nota('A4', 'e', beam=3, matiz='p'), nota('Bb4', 'e', beam=3), nota('A4', 'e', beam=3),
          nota('G#4', 'e', beam=3), nota('A4', 'h')]
    eb = []
    for b in range(3):
        for gr in range(2):
            for i, p in enumerate(['A2', 'E3', 'A2', 'E3']):
                eb.append(nota(p, 'e', beam=10 + b * 2 + gr))
    for i, p in enumerate(['A2', 'E3', 'A2', 'E3']):
        eb.append(nota(p, 'e', beam=20))
    eb.append(nota('A2', 'h'))
    y = gran(c, M, y - 16, CW, g, et, eb, (4, 4), 'RIFF · p (suau) als compassos 1, 2 i 4 · f (fort) al compàs 3')
    y -= 6
    h1 = caixa_nota(c, M, y, 250, 'PAS A PAS',
                    "1) Mà esquerra sola, ♩ = 70. 2) Mà dreta sola. 3) Juntes, a poc a poc. "
                    "4) Puja a ♩ = 90 i després a ♩ = 110.")
    caixa_nota(c, M + 265, y, CW - 265, 'CREA',
               "Canvia el compàs 3: inventa quatre corxeres noves amb notes de LA menor harmònica i "
               "ensenya-les. Mantén sempre el silenci de negra del final.")
    c.showPage()


# ------------------------------------------------------------------ fitxa 5
def f5(c):
    pagina(c, 5, 'HALLOWEEN · IMPROVISACIÓ', 'Improvisa amb la lluna', 'La pentatònica menor i un bucle de quatre acords')
    y = 690
    y = bloc_pinta(c, y, mandala_lluna,
                   "Les vuit fases de la lluna, de lluna nova a lluna plena i de nou a nova. Pinta la part "
                   "il·luminada de cada fase i fixa't en l'ordre: 1 → 8.",
                   'LA PENTATÒNICA MENOR',
                   "Cinc notes que sempre «quadren»: LA – DO – RE – MI – SOL. Si hi afegeixes el MI♭ "
                   "(la «nota blava») obtens el color del blues.")
    y = bloc_canta(c, y, "Improvisa cantant amb només cinc notes (la – do – re – mi – sol) mentre algú toca, o "
                         "tu mateix, el bucle de la mà esquerra. Quatre compassos, un acord a cada compàs. "
                         "No hi ha notes dolentes: repeteix el que t'agradi!")
    y = seccio(c, y, '03', 'TOCA', 'bucle, notes i cartes de ritme')
    g = 7.4
    eb = [acord(['A2', 'E3'], 'w'), acord(['G2', 'D3'], 'w'), acord(['F2', 'C3'], 'w'), acord(['E2', 'B2'], 'w')]
    et = [nota('A4', 'q'), nota('C5', 'q'), nota('D5', 'q'), nota('E5', 'q'),
          nota('G5', 'q'), nota('E5', 'q'), nota('D5', 'q'), nota('C5', 'q'),
          nota('A4', 'h'), nota('Eb5', 'q'), nota('E5', 'q'), nota('A4', 'w')]
    y = gran(c, M, y - 6, CW, g, et, eb, (4, 4),
             "BUCLE · mà esquerra: La m – Sol – Fa – Mi · mà dreta: un exemple d'improvisació (el MI♭ és la nota blava)")
    y -= 4
    cap_pent(c, M, y, 'CARTES DE RITME · tria una carta i repeteix-la amb notes de la pentatònica')
    y -= 8
    cards = [[nota('A4', 'q'), nota('A4', 'q'), nota('A4', 'h')],
             [nota('A4', 'e', beam=0), nota('A4', 'e', beam=0), nota('A4', 'e', beam=1), nota('A4', 'e', beam=1),
              nota('A4', 'q'), nota('A4', 'q')],
             [nota('A4', 'q.'), nota('A4', 'e'), nota('A4', 'q'), nota('A4', 'q')]]
    cw = (CW - 2 * 14) / 3.0
    ybot = y
    for i, ev in enumerate(cards):
        yy = y - before_staff(g, ev, 'treble')
        top, bot = nt.draw_system(c, M + i * (cw + 14), yy, cw, g, ev, clef='treble', time_sig=(4, 4),
                                  show_clef=False, show_time=False)
        t(c, M + i * (cw + 14), bot - 12, 'CARTA %s' % 'ABC'[i], 7.8, SANSB, PURPLE)
        ybot = min(ybot, bot - 18)
    y = ybot - 4
    caixa_nota(c, M, y, CW, 'REPTE',
               "Tira un dau (o tria una carta): toca aquell ritme sobre el bucle, quatre compassos. Canvia de "
               "carta i repeteix. Quan et sentis segur, afegeix el MI♭ una sola vegada per compàs.")
    c.showPage()


# ------------------------------------------------------------------ fitxa 6
def f6(c):
    pagina(c, 6, 'HALLOWEEN · REPTE FINAL', 'Missatges secrets', 'Les notes són lletres: descodifica i toca')
    y = 690
    y = bloc_pinta(c, y, mandala_calavera,
                   "Pinta la calavera amb els colors que vulguis mentre penses en el primer missatge. "
                   "A continuació, descodifica'l!",
                   'LA CLAU',
                   "Les notes tenen nom de lletra: LA = A · SI = B · DO = C · RE = D · MI = E · FA = F · "
                   "SOL = G. Amb aquestes set lletres es poden escriure paraules!")
    y = bloc_canta(c, y, "Digues en veu alta el nom de cada nota, a ritme de negra: «do, la, sol, mi». Quina "
                         "paraula formen? Canta-la a poc a poc i, després, toca-la al piano.")
    y = seccio(c, y, '03', 'TOCA', 'quatre missatges per descodificar')
    g = 7.4
    msgs = [['C5', 'A4', 'G4', 'E4'], ['F4', 'A4', 'C5', 'E5'], ['D5', 'E5', 'A4', 'D5'],
            ['F4', 'A4', 'D5', 'E5']]
    cw = (CW - 14) / 2.0
    yy0 = y - 6
    ys = []
    for i, ps in enumerate(msgs):
        x = M + (i % 2) * (cw + 14)
        yy = yy0 - (i // 2) * 84
        ev = [nota(p, 'q') for p in ps]
        yb = yy - before_staff(g, ev, 'treble')
        top, bot = nt.draw_system(c, x, yb, cw, g, ev, clef='treble', time_sig=(4, 4))
        t(c, x, yy + 6, 'MISSATGE %d' % (i + 1), 7.8, SANSB, PURPLE)
        t(c, x, bot - 14, 'Resposta:  ___  ___  ___  ___', 9, SANS, INK)
        ys.append(bot - 22)
    y = min(ys) - 2
    y -= 14
    # diploma
    caixa(c, M, y - 142, CW, 140, None, white, PLUM)
    trazo(c, 0.8, col=GOLD)
    c.roundRect(M + 6, y - 136, CW - 12, 128, 5, stroke=1, fill=0)
    t(c, W / 2, y - 30, 'CERTIFICAT DE NIGROMANT PIANISTA', 14, SERIFB, PLUM, 'c')
    t(c, W / 2, y - 50, 'Aquest certificat acredita que', 9, SANS, MUTED, 'c')
    trazo(c, 0.8, col=INK)
    c.line(M + 90, y - 74, W - M - 90, y - 74)
    par(c, M + 40, y - 92, "ha pintat, cantat i tocat les sis fitxes de la Nit de Halloween: l'escala embruixada, el "
                           "tritó, els acords, el riff, la improvisació i els missatges secrets.", 8.8, CW - 80, 12.6, align='c')
    t(c, M + 70, y - 126, 'Signatura del professor/a', 7.6, SANS, MUTED)
    c.line(M + 60, y - 118, M + 200, y - 118)
    t(c, W - M - 70, y - 126, 'Data', 7.6, SANS, MUTED, 'r')
    c.line(W - M - 160, y - 118, W - M - 70, y - 118)
    hd.estrellitas(c, [(M + 22, y - 22, 1.0), (W - M - 22, y - 22, 1.0)])
    t(c, W / 2, 56, 'Solucions (professor/a): 1 CAGE · 2 FACE · 3 DEAD · 4 FADE', 6.8, SANS, MUTED, 'c')
    c.showPage()


def portada(c):
    c.setFillColor(PLUM)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(ORANGE)
    c.rect(0, H - 14, W, 14, stroke=0, fill=1)
    t(c, M, H - 60, 'T-CLAS · EL QUADERN DEL PIANISTA', 9, SANSB, ORANGE)
    t(c, M, H - 130, 'Nit de', 40, SERIFB, white)
    t(c, M, H - 180, 'nigromants', 40, SERIFB, white)
    t(c, M, H - 224, 'Fitxes de Halloween per pintar, cantar i tocar', 12, SANS, HexColor('#D9CCEE'))
    t(c, M, H - 242, 'Per a joves de 12 a 20 anys', 10, SANS, HexColor('#B9A5D6'))
    # mandala gran en blanc sobre fons fosc: es dibuixa amb traços clars
    c.saveState()
    c.setFillColor(HexColor('#3A2358'))
    c.circle(W / 2, 400, 170, stroke=0, fill=1)
    c.restoreState()
    mandala_rosassa(c, W / 2, 400, 160, ['LA', 'SI', 'DO', 'RE', 'MI', 'FA', 'SOL♯', 'LA'])
    items = ["1 · L'escala embruixada", '2 · El tritó', '3 · Acords que fan por', '4 · Riff de la nit',
             '5 · Improvisa amb la lluna', '6 · Missatges secrets']
    for i, s_ in enumerate(items):
        x = M + (i % 2) * 260
        yy = 150 - (i // 2) * 30
        t(c, x, yy, s_, 11, SANSB, white)
    t(c, M, 40, 'Material musical propi i teoria: sense drets d\'autor.', 8, SANS, HexColor('#B9A5D6'))
    c.showPage()


def main(solo=None):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    c = ManoCanvas(OUT, pagesize=(W, H), amp=0)
    if not solo or 0 in solo:
        portada(c)
    for n, f in enumerate([f1, f2, f3, f4, f5, f6], 1):
        if solo and n not in solo:
            continue
        f(c)
    c.save()
    print(OUT)


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or None)
