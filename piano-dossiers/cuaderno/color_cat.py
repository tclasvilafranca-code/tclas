# -*- coding: utf-8 -*-
"""Fulls A4 apaïsats A TOT COLOR, en català, per a nens: el teclat de les notes (com el
   cartell original), les figures musicals i el pentagrama, amb en Mussol Misol.

   Es genera amb:  python3 color_cat.py  ->  ../output/Color_Catala.pdf
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
sys.path.insert(0, HERE)
import notation as nt                                           # noqa: E402
from reportlab.lib.colors import HexColor, white               # noqa: E402
from reportlab.pdfbase.pdfmetrics import stringWidth           # noqa: E402

from dibujo_mano import W, H, ManoCanvas, texto, lineas_texto, _bezier   # noqa: E402
from mussol import mussol                                      # noqa: E402

OUT = os.path.join(HERE, '..', 'output', 'Color_Catala.pdf')
FAT, HA = 'Fat', 'Hand'

PAPER = HexColor('#FBF1D5')
INK = HexColor('#35302F')
COL = dict(vermell='#E4392B', taronja='#F28C0E', groc='#F9C80E', verd='#76B82A', blau='#2E86C8',
           morat='#A58AC9', gris='#A7A397', rosa='#F277A5')
# (nom, altura, color de la tecla)
NOTES = [('DO', 'C4', 'vermell'), ('RE', 'D4', 'taronja'), ('MI', 'E4', 'groc'),
         ('FA', 'F4', 'verd'), ('SOL', 'G4', 'blau'), ('LA', 'A4', 'morat'),
         ('SI', 'B4', 'gris'), ('DO', 'C5', 'vermell')]
COLOR_NOTA = {n[0]: n[2] for n in NOTES}


def hx(nom):
    return HexColor(COL[nom])


def fons(c):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setStrokeColor(INK)
    c.setLineWidth(3.0)
    c.setFillColor(PAPER)
    c.roundRect(12, 12, W - 24, H - 24, 18, stroke=1, fill=0)
    c.setLineWidth(1.0)
    c.setDash(1, 4)
    c.roundRect(19, 19, W - 38, H - 38, 13, stroke=1, fill=0)
    c.setDash()


def forma(c, tipus, *a, fill, lw=2.6, **k):
    c.setStrokeColor(INK)
    c.setLineWidth(lw)
    c.setLineJoin(1)
    c.setLineCap(1)
    c.setFillColor(fill)
    getattr(c, tipus)(*a, stroke=1, fill=1, **k)


def lletres_color(c, cx, y, text, mida, colors, semilla=1, sep=2.0):
    """Lletres grosses de colors amb vora fosca; `colors` és una llista de noms de color,
       una per lletra (es repeteix si cal)."""
    import random
    rnd = random.Random(semilla)
    ws = [stringWidth(ch, FAT, mida) for ch in text]
    total = sum(ws) + sep * (len(text) - 1)
    x = cx - total / 2
    c.saveState()
    k = 0
    for ch, w in zip(text, ws):
        if ch != ' ':
            c.saveState()
            c.translate(x + w / 2, y + rnd.uniform(-2, 2))
            c.rotate(rnd.uniform(-3, 3))
            for mode, lw, col in ((1, 9, INK), (2, 3.2, hx(colors[k % len(colors)]))):
                t = c.beginText(-w / 2, 0)
                t.setFont(FAT, mida)
                t.setTextRenderMode(mode)
                c.setLineWidth(lw)
                c.setLineJoin(1)
                c.setStrokeColor(col)
                c.setFillColor(col)
                t.textOut(ch)
                c.drawText(t)
            c.restoreState()
            k += 1
        x += w + sep
    c.restoreState()


def lletres_blanques(c, cx, y, text, mida):
    """Lletres blanques amb vora fosca (els noms de les notes)."""
    ws = [stringWidth(ch, FAT, mida) for ch in text]
    total = sum(ws) + 1.5 * (len(text) - 1)
    x = cx - total / 2
    c.saveState()
    for ch, w in zip(text, ws):
        for mode, lw, col in ((1, 7, INK), (2, 2.4, white)):
            t = c.beginText(x, y)
            t.setFont(FAT, mida)
            t.setTextRenderMode(mode)
            c.setLineWidth(lw)
            c.setLineJoin(1)
            c.setStrokeColor(col)
            c.setFillColor(col)
            t.textOut(ch)
            c.drawText(t)
        x += w + 1.5
    c.restoreState()


def estrella(c, cx, cy, r, color, giro=0):
    pts = []
    for i in range(10):
        a = math.pi / 2 + giro + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.46
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    c.setStrokeColor(INK)
    c.setLineWidth(2.0)
    c.setFillColor(hx(color))
    c.poly(pts, 1, 1)


def nota_color(c, x, y, s, color, corxera=False):
    """Una nota de colors per decorar (cap pintat, plica i, si cal, corxet)."""
    c.saveState()
    c.translate(x, y)
    c.rotate(-20)
    forma(c, 'ellipse', -9 * s, -6.5 * s, 9 * s, 6.5 * s, fill=hx(color), lw=2.0)
    c.restoreState()
    c.setStrokeColor(INK)
    c.setLineWidth(2.4 * s)
    c.line(x + 8.2 * s, y + 2 * s, x + 8.2 * s, y + 38 * s)
    if corxera:
        px, py = x + 8.2 * s, y + 38 * s
        pts = (_bezier((px, py), (px + 8 * s, py - 7 * s), (px + 16 * s, py - 12 * s),
                       (px + 9 * s, py - 25 * s), 8) +
               _bezier((px + 9 * s, py - 25 * s), (px + 11 * s, py - 14 * s), (px + 5 * s, py - 9 * s),
                       (px, py - 8 * s), 8))
        c.setFillColor(hx(color))
        c.setLineWidth(2.0)
        c.poly(pts, 1, 1)


def sol(c, cx, cy, r):
    c.setStrokeColor(HexColor('#F4A100'))
    c.setLineWidth(3.6)
    c.setLineCap(1)
    for i in range(12):
        a = i * math.pi / 6 + 0.08
        c.line(cx + (r + 7) * math.cos(a), cy + (r + 7) * math.sin(a),
               cx + (r + 18 + 6 * (i % 2)) * math.cos(a), cy + (r + 18 + 6 * (i % 2)) * math.sin(a))
    forma(c, 'circle', cx, cy, r, fill=HexColor('#FFD23F'), lw=2.8)
    c.setFillColor(INK)
    for dx in (-0.36, 0.36):
        c.circle(cx + dx * r, cy + 0.14 * r, r * 0.09, stroke=0, fill=1)
    c.setStrokeColor(INK)
    c.setLineWidth(2.0)
    c.arc(cx - r * 0.3, cy - r * 0.34, cx + r * 0.3, cy + r * 0.04, 200, 140)
    c.setFillColor(HexColor('#F7A08C'))
    for dx in (-0.58, 0.58):
        c.circle(cx + dx * r, cy - 0.12 * r, r * 0.13, stroke=0, fill=1)


def nuvol(c, cx, cy, s=1.0):
    circ = [(-46, -6, 22), (-20, 12, 28), (14, 16, 31), (44, -2, 24), (0, -10, 26)]
    c.setStrokeColor(HexColor('#7DB5DA'))
    c.setLineWidth(2.8)
    for dx, dy, r in circ:
        c.circle(cx + dx * s, cy + dy * s, r * s, stroke=1, fill=0)
    c.roundRect(cx - 60 * s, cy - 36 * s, 120 * s, 26 * s, 13 * s, stroke=1, fill=0)
    c.setFillColor(HexColor('#EAF5FC'))
    for dx, dy, r in circ:
        c.circle(cx + dx * s, cy + dy * s, r * s - 2.2, stroke=0, fill=1)
    c.roundRect(cx - 60 * s + 2.2, cy - 36 * s + 2.2, 120 * s - 4.4, 26 * s - 4.4, 13 * s, stroke=0, fill=1)
    c.rect(cx - 46 * s, cy - 30 * s, 90 * s, 30 * s, stroke=0, fill=1)
    c.setFillColor(INK)
    for dx in (-0.36, 0.36):
        c.circle(cx + dx * 24 * s, cy + 4 * s + 0.14 * 24 * s, 24 * s * 0.09, stroke=0, fill=1)
    c.setStrokeColor(INK)
    c.setLineWidth(1.8)
    c.arc(cx - 7 * s, cy + 4 * s - 8 * s, cx + 7 * s, cy + 4 * s + 1 * s, 200, 140)
    c.setFillColor(HexColor('#F7B6C2'))
    for dx in (-0.58, 0.58):
        c.circle(cx + dx * 24 * s, cy + 4 * s - 3 * s, 3.4 * s, stroke=0, fill=1)


def arc_iris(c, cx, base, rx, ry, paso=17):
    cols = ['#F6A7A0', '#F9C98B', '#FBE58C', '#BFE0A0', '#A9D3EC', '#CDB8E4']
    for i, col in enumerate(cols):
        a1, b1 = rx - i * paso, ry - i * paso * ry / rx
        a2, b2 = rx - (i + 1) * paso, ry - (i + 1) * paso * ry / rx
        n = 40
        pts = [(cx + a1 * math.cos(math.pi * (1 - t / n)), base + b1 * math.sin(math.pi * (1 - t / n)))
               for t in range(n + 1)]
        pts += [(cx + a2 * math.cos(math.pi * t / n), base + b2 * math.sin(math.pi * t / n))
                for t in range(n + 1)]
        p = c.beginPath()
        p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        p.close()
        c.setFillColor(HexColor(col))
        c.drawPath(p, stroke=0, fill=1)


def pentagrama(c, x, ytop, w, gap, lw=1.8):
    c.setStrokeColor(INK)
    c.setLineWidth(lw)
    c.setLineCap(0)
    a = c.amp
    c.amp = 0.3
    for i in range(5):
        c.line(x, ytop - i * gap, x + w, ytop - i * gap)
    c.amp = a
    return ytop - 4 * gap


def cap_rodona(c, cx, cy, gap, color):
    c.saveState()
    c.translate(cx, cy)
    forma(c, 'ellipse', -gap * 0.85, -gap * 0.56, gap * 0.85, gap * 0.56, fill=hx(color) if color else white,
          lw=2.0)
    c.rotate(-30)
    c.setStrokeColor(INK)
    c.setLineWidth(1.2)
    c.ellipse(-gap * 0.24, -gap * 0.46, gap * 0.24, gap * 0.46, stroke=1, fill=0)
    c.restoreState()


def globus(c, x, y, w, h, linies, cua_x=None, mida=13.5, lead=16):
    forma(c, 'roundRect', x, y, w, h, 18, fill=white, lw=2.4)
    if cua_x is not None:
        c.setFillColor(white)
        c.setStrokeColor(INK)
        c.setLineWidth(2.4)
        c.poly([(cua_x - 12, y + 2), (cua_x + 14, y + 2), (cua_x + 20, y - 26)], 1, 1)
        c.setStrokeColor(white)
        c.setLineWidth(3.4)
        c.line(cua_x - 9, y + 2, cua_x + 11, y + 2)
    yy = y + h - 22
    for ln in linies:
        texto(c, x + 16, yy, ln, mida, HA)
        yy -= lead


def peu(c):
    texto(c, 40, 30, 'Nom:', 15, HA, col=INK)
    c.setStrokeColor(INK)
    c.setLineWidth(1.2)
    c.setDash(1, 3)
    c.line(80, 28, 250, 28)
    c.setDash()


# ============================================================ full 1: el teclat
def full_teclat(c):
    fons(c)
    lletres_color(c, W / 2, 506, 'EL TECLAT DE', 54, ['vermell'] * 2 + ['blau'] * 6 + ['verd'] * 4, 3)
    lletres_color(c, W / 2, 458, 'LES NOTES', 54, ['morat'] * 3 + ['vermell'] * 6, 5)
    sol(c, 98, 498, 36)
    nuvol(c, 752, 494, 1.05)
    estrella(c, 190, 446, 16, 'groc')
    estrella(c, 668, 452, 13, 'blau', 0.3)
    nota_color(c, 62, 396, 1.0, 'vermell', True)
    nota_color(c, 118, 410, 0.85, 'blau', True)
    nota_color(c, 735, 398, 1.0, 'morat')
    nota_color(c, 785, 404, 0.9, 'verd', True)

    arc_iris(c, W / 2, 296, 372, 128)
    kw, gp = 88, 8.7
    x0 = (W - (8 * kw + 7 * gp)) / 2
    ytop, ybot = 292, 128
    for i, (nom, alt, color) in enumerate(NOTES):
        x = x0 + i * (kw + gp)
        forma(c, 'roundRect', x, ybot - 9, kw, ytop - ybot, 11, fill=HexColor('#3B3433'), lw=2.6)
        forma(c, 'roundRect', x, ybot, kw, ytop - ybot, 11, fill=hx(color), lw=2.8)
        c.setFillColor(white)
        lletres_blanques(c, x + kw / 2, ytop - 56, nom, 33 if len(nom) < 3 else 28)
        gap = 7.4
        yb = pentagrama(c, x + 10, ybot + 58, kw - 20, gap, lw=1.4)
        nt.draw_clef(c, x + 11, yb, gap)
        ny = nt.note_y(yb, gap, alt)
        nx = x + kw - 27
        if alt == 'C4':
            c.setStrokeColor(INK)
            c.setLineWidth(1.5)
            c.line(nx - gap * 1.2, ny, nx + gap * 1.2, ny)
        cap_rodona(c, nx, ny, gap * 1.15, None)
    estrella(c, 48, 66, 13, 'taronja')
    estrella(c, W - 50, 62, 15, 'rosa', 0.2)
    nota_color(c, 130, 40, 0.8, 'groc', True)
    nota_color(c, W - 150, 40, 0.8, 'verd')
    texto(c, W / 2, 60, 'Cada nota té el seu color: busca-les al piano!', 17, HA, 'c', col=INK)
    peu(c)
    c.showPage()


# ==================================================== full 2: les figures musicals
def figura_color(c, tipus, cx, cy, s, color):
    if tipus == 'w':
        cap_rodona(c, cx, cy, 15 * s, color)
        return
    c.saveState()
    c.translate(cx, cy)
    c.rotate(-20)
    farcit = hx(color) if tipus in ('q', 'e') else white
    forma(c, 'ellipse', -12 * s, -8.5 * s, 12 * s, 8.5 * s, fill=farcit, lw=2.4)
    c.restoreState()
    c.setStrokeColor(INK)
    c.setLineWidth(3.0)
    c.line(cx + 11 * s, cy + 2 * s, cx + 11 * s, cy + 50 * s)
    if tipus == 'e':
        px, py = cx + 11 * s, cy + 50 * s
        pts = (_bezier((px, py), (px + 10 * s, py - 8 * s), (px + 20 * s, py - 14 * s),
                       (px + 12 * s, py - 30 * s), 8) +
               _bezier((px + 12 * s, py - 30 * s), (px + 14 * s, py - 16 * s), (px + 6 * s, py - 11 * s),
                       (px, py - 10 * s), 8))
        c.setFillColor(hx(color))
        c.setLineWidth(2.2)
        c.poly(pts, 1, 1)


def full_figures(c):
    fons(c)
    lletres_color(c, W / 2, 522, 'LES FIGURES MUSICALS', 42,
                  ['blau', 'verd', 'taronja', 'rosa', 'morat', 'vermell'], 7)
    estrella(c, 70, 520, 14, 'groc')
    estrella(c, W - 70, 522, 12, 'blau', 0.3)

    cartes = [('w', 'RODONA', '4 temps', 4, 'blau', 'Fes 4 palmes!'),
              ('h', 'BLANCA', '2 temps', 2, 'verd', 'Fes 2 palmes!'),
              ('q', 'NEGRA', '1 temps', 1, 'taronja', 'Fes 1 palma!'),
              ('e', 'CORXERA', 'mig temps', 1, 'rosa', 'Dues per temps!')]
    cw, cg = 182, 14
    cx0 = (W - (4 * cw + 3 * cg)) / 2
    for i, (tp, nom, gl, nb, colr, frase) in enumerate(cartes):
        x = cx0 + i * (cw + cg)
        forma(c, 'roundRect', x, 352, cw, 132, 14, fill=white, lw=2.6)
        forma(c, 'roundRect', x, 446, cw, 38, 14, fill=hx(colr), lw=2.6)
        c.setFillColor(hx(colr))
        c.rect(x + 3, 446, cw - 6, 14, stroke=0, fill=1)
        lletres_blanques(c, x + cw / 2, 457, nom, 22)
        figura_color(c, tp, x + 40, 382, 1.1, colr)
        texto(c, x + 82, 420, gl, 17, HA, col=INK)
        for k in range(nb if tp != 'e' else 1):
            forma(c, 'circle', x + 90 + k * 17, 396, 6.5, fill=hx(colr), lw=1.8)
        texto(c, x + 82, 366, frase, 12.5, HA, col=INK)

    texto(c, 40, 320, 'Quantes en caben en un compàs de 4 temps?', 20, HA, col=INK)
    files = [('RODONA', 1, 'blau'), ('BLANCA', 2, 'verd'), ('NEGRA', 4, 'taronja'), ('CORXERA', 8, 'rosa')]
    bx0, bw = 150, 500
    yy = 270
    for nom, n, colr in files:
        texto(c, 40, yy + 10, nom, 15, HA, col=INK)
        w1 = bw / float(n)
        for k in range(n):
            forma(c, 'roundRect', bx0 + k * w1 + 1.5, yy, w1 - 3, 34, 8 if n < 8 else 5,
                  fill=hx(colr), lw=2.0)
            if n == 8:
                c.setFillColor(white)
                c.setStrokeColor(INK)
                c.setLineWidth(1.2)
                c.circle(bx0 + k * w1 + w1 / 2, yy + 17, 3.6, stroke=1, fill=1)
            if n <= 4:
                c.setFillColor(white)
                c.setStrokeColor(INK)
                c.setLineWidth(1.6)
                c.circle(bx0 + k * w1 + w1 / 2, yy + 17, 6, stroke=1, fill=1)
        yy -= 52
    mussol(c, 745, 160, 0.78, color=True)
    globus(c, 648, 262, 172, 62, ['Una rodona val 2 blanques,', '4 negres o 8 corxeres!'], cua_x=740,
           mida=12, lead=16)
    nota_color(c, 690, 60, 0.7, 'vermell', True)
    nota_color(c, 790, 62, 0.7, 'morat')
    peu(c)
    c.showPage()


# ======================================================= full 3: el pentagrama
def full_pentagrama(c):
    fons(c)
    lletres_color(c, W / 2, 522, 'EL PENTAGRAMA', 44, ['vermell', 'taronja', 'groc', 'verd', 'blau', 'morat'], 4)
    estrella(c, 70, 520, 14, 'rosa')
    estrella(c, W - 70, 522, 12, 'groc', 0.3)

    gap = 18
    # ---- les cinc línies
    texto(c, 50, 470, 'Les 5 línies es compten de baix a dalt:', 19, HA, col=INK)
    ytop = 440
    yb = pentagrama(c, 110, ytop, 440, gap)
    nt.draw_clef(c, 118, yb, gap)
    for k in range(5):
        forma(c, 'circle', 580, yb + k * gap, 9, fill=white, lw=1.8)
        texto(c, 580, yb + k * gap - 4.5, str(k + 1), 14, HA, 'c', col=INK)
    linies = [('MI', 'E4'), ('SOL', 'G4'), ('SI', 'B4'), ('RE', 'D5'), ('FA', 'F5')]
    for k, (nom, alt) in enumerate(linies):
        nx = 215 + k * 68
        cap_rodona(c, nx, nt.note_y(yb, gap, alt), gap * 0.95, COLOR_NOTA[nom])
        forma(c, 'roundRect', nx - 26, yb - 50, 52, 28, 9, fill=hx(COLOR_NOTA[nom]), lw=2.0)
        lletres_blanques(c, nx, yb - 42, nom, 17)

    # ---- els quatre espais
    texto(c, 50, 288, 'I els 4 espais, també de baix a dalt:', 19, HA, col=INK)
    ytop2 = 258
    yb2 = pentagrama(c, 110, ytop2, 440, gap)
    nt.draw_clef(c, 118, yb2, gap)
    espais = [('FA', 'F4'), ('LA', 'A4'), ('DO', 'C5'), ('MI', 'E5')]
    for k, (nom, alt) in enumerate(espais):
        nx = 235 + k * 78
        cap_rodona(c, nx, nt.note_y(yb2, gap, alt), gap * 0.95, COLOR_NOTA[nom])
        forma(c, 'roundRect', nx - 26, yb2 - 50, 52, 28, 9, fill=hx(COLOR_NOTA[nom]), lw=2.0)
        lletres_blanques(c, nx, yb2 - 42, nom, 17)

    # ---- en Mussol Misol
    mussol(c, 712, 235, 0.95, color=True)
    globus(c, 622, 372, 198, 96, ['El meu nom són les', 'dues primeres línies:', 'MI i SOL!'], cua_x=700,
           mida=14, lead=19)
    forma(c, 'roundRect', 40, 52, 560, 54, 12, fill=white, lw=2.2)
    texto(c, 56, 86, 'La clau de sol dóna voltes just a la 2a línia: la del SOL.', 15.5, HA, col=INK)
    texto(c, 56, 64, 'Així sempre saps on és el SOL i pots comptar la resta!', 15.5, HA, col=INK)
    nota_color(c, 640, 40, 0.8, 'vermell', True)
    nota_color(c, 790, 44, 0.8, 'blau')
    peu(c)
    c.showPage()


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    c = ManoCanvas(OUT, pagesize=(W, H), seed=23, amp=0.8)
    c.setTitle('Fulls de color · El teclat de les notes')
    for f in (full_teclat, full_figures, full_pentagrama):
        f(c)
    c.save()
    print('generat', OUT)


if __name__ == '__main__':
    main()
