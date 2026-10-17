# -*- coding: utf-8 -*-
"""Pàgines inicials del Quadern PEKES: portada, en Mussol Misol, com s'usa el llibre, índex."""
import math
import os

from nens_tclas import *                                         # noqa: F401,F403
from nens_tclas import (W, H, M, CW, NAVY, NAVY_SOFT, CREMA, WARM, WARM2, RULE, SOMBRA, INK, MUTED, OCRE, COL,
                        COLNOM, SANS, SANSB, SERIFB, ETQ, Y, txt, par, alt_par, trac, rr, pagina, mapa, panell,
                        caixa_t, franja, guia, quadrat, etiqueta_sec, teclat, pauta, cap, nota, xip, white,
                        HexColor, stringWidth, mussol, ICONES, SYM)
from nens_jocs import linia
import nens_pla as pla

LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'asset_logo_tclas.png')
COLORS7 = [COL[n] for n in ('DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI')]


def arc_iris(c, cx, cy, r_out, gruix):
    """Arc de Sant Martí amb els 7 colors de les notes (de fora cap a dins: DO ... SI)."""
    c.saveState()
    for k, col in enumerate(COLORS7):
        r = r_out - k * gruix
        c.setFillColor(HexColor(col))
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.4)
        c.wedge(cx - r, cy - r, cx + r, cy + r, 0, 180, stroke=1, fill=1)
    c.setFillColor(CREMA)
    c.setStrokeColor(NAVY)
    r = r_out - 7 * gruix
    c.wedge(cx - r, cy - r, cx + r, cy + r, 0, 180, stroke=1, fill=1)
    c.restoreState()


# ======================================================================== 1 · portada
def portada(c):
    c.setFillColor(CREMA)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    trac(c, 1.1, RULE)
    c.rect(32, 32, W - 64, H - 64, stroke=1, fill=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 9, W, 9, stroke=0, fill=1)
    c.saveState()
    cp = c.beginPath()
    cp.circle(W / 2, H - 104, 45)
    c.clipPath(cp, stroke=0, fill=0)
    c.drawImage(LOGO, W / 2 - 50, H - 154, 100, 100, mask='auto', preserveAspectRatio=True)
    c.restoreState()
    txt(c, W / 2, Y(168), 'T-CLAS  ·  DESPERTA EL TEU SO INTERIOR', 9, ETQ, OCRE, 'c')
    # arc de Sant Martí amb en Mussol al mig
    cx = W / 2
    arc_iris(c, cx, Y(420), 190, 14)
    mussol(c, cx, Y(354), 0.98, color=True, lw=3.0)
    # títol
    txt(c, W / 2, Y(532), 'El Quadern', 44, SERIFB, NAVY, 'c')
    txt(c, W / 2, Y(580), 'del Pianista', 44, SERIFB, NAVY, 'c')
    trac(c, 3, OCRE)
    c.line(W / 2 - 34, Y(596), W / 2 + 34, Y(596))
    rr(c, W / 2 - 70, Y(640), 140, 32, 16, fill=NAVY, lw=0)
    txt(c, W / 2, Y(630), 'PEKES', 20, ETQ, white, 'c')
    txt(c, W / 2, Y(666), 'Teoria i jocs per començar a tocar el piano', 13.5, SANS, NAVY_SOFT, 'c')
    txt(c, W / 2, Y(684), 'per a nens i nenes de 6 a 10 anys', 11.5, SANS, MUTED, 'c')
    # teclat de colors
    teclat(c, W / 2 - 150, 86, 300, 46, nb=7, resalta={i: n for i, n in enumerate(('DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI'))},
           noms='resalta', color=True)
    txt(c, M + 4, 62, 'AQUEST QUADERN ÉS DE', 8.6, ETQ, OCRE)
    linia(c, M + 126, 62, 300)
    c.showPage()


# ======================================================================== 2 · en Mussol Misol
def presentacio(c):
    pagina(c, 'PEKES  ·  BENVINGUDA', 'Hola, sóc en Mussol!', 'Presentació',
           'Seré el teu guia durant tot el quadern. Vols conèixer-me?', 2)
    # esquerra: Mussol + globus
    arc_iris(c, M + 70, Y(262), 78, 6.5)
    mussol(c, M + 70, Y(204), 0.62, color=True, lw=2.8)
    bx, by, bw, bh = M + 156, Y(262), CW - 156, 130
    rr(c, bx + 3.4, by - 3.4, bw, bh, 11, fill=SOMBRA, lw=0)
    rr(c, bx, by, bw, bh, 11, fill=white, lw=1.7, col=NAVY)
    c.setFillColor(white)
    trac(c, 1.7, NAVY)
    c.poly([(bx + 1, by + bh / 2 + 10), (bx - 14, by + bh / 2), (bx + 1, by + bh / 2 - 10)], 1, 1)
    c.setStrokeColor(white)
    c.setLineWidth(3)
    c.line(bx + 1, by + bh / 2 + 8, bx + 1, by + bh / 2 - 8)
    par(c, bx + 18, by + bh - 30, 'Em dic Mussol Misol. Sóc mussol, i m’agrada molt la música! '
        'El meu nom amaga un secret: si el mires bé, hi veuràs dues notes.', 13.5, bw - 36, 19)
    # secret MI + SOL
    yt = Y(296)
    panell(c, M, yt, CW, 108, 'EL SECRET DEL MEU NOM')
    xs = M + 34
    for k, nm in enumerate(('MI', 'SOL')):
        hexc = HexColor(COL[nm])
        bxk = xs + k * 150
        rr(c, bxk, yt - 88, 92, 52, 10, fill=hexc, lw=1.7, col=NAVY)
        txt(c, bxk + 46, yt - 72, nm, 24, SERIFB, INK if nm == 'MI' else white, 'c')
        txt(c, bxk + 46, yt - 102, 'groc' if nm == 'MI' else 'blau', 10.5, SANS, MUTED, 'c')
    txt(c, xs + 118, yt - 70, '+', 28, SANSB, OCRE, 'c')
    txt(c, xs + 302, yt - 66, '=', 28, SANSB, OCRE, 'c')
    txt(c, xs + 330, yt - 64, 'MISOL', 26, SERIFB, NAVY)
    txt(c, xs + 330, yt - 84, 'Mi + Sol: dues notes!', 11, SANS, NAVY_SOFT)
    # ruta musical (un camí de serp amb vuit parades)
    yt = Y(430)
    panell(c, M, yt, CW, 250, 'LA RUTA MUSICAL')
    txt(c, M + 14, yt - 40, 'El camí que farem junts: vuit parades amb una mica de música a cada una.', 11.5, SANS, NAVY_SOFT)
    xs_ = [M + 62 + k * 122 for k in range(4)]
    y1, y2 = yt - 100, yt - 182
    pts = [(xs_[k], y1) for k in range(4)] + [(xs_[3 - k], y2) for k in range(4)]
    trac(c, 9, SOMBRA)
    p = c.beginPath()
    p.moveTo(*pts[0])
    for q in pts[1:4]:
        p.lineTo(*q)
    p.curveTo(pts[3][0] + 44, pts[3][1], pts[4][0] + 44, pts[4][1], pts[4][0], pts[4][1])
    for q in pts[5:]:
        p.lineTo(*q)
    c.setLineJoin(1)
    c.drawPath(p, stroke=1, fill=0)
    trac(c, 1.8, NAVY, (7, 6))
    c.drawPath(p, stroke=1, fill=0)
    c.setDash()
    curts = ['Abans de tocar', 'El pentagrama', 'Les notes', 'El ritme', 'Els silencis', 'Les plicas', 'Toquem!', 'Expressem']
    for k, (px, py) in enumerate(pts):
        c.setFillColor(HexColor(COLORS7[k % 7]))
        trac(c, 1.8, NAVY)
        c.circle(px, py, 19, stroke=1, fill=1)
        txt(c, px, py - 6.5, str(k + 1), 19, SANSB, INK if k % 7 == 2 else white, 'c')
        txt(c, px, py - 33, curts[k], 11, SANSB, NAVY, 'c')
    caixa_t(c, M, Y(702), CW, 78, 'ET CAL',
            'Un llapis, una goma i colors; i un piano o un teclat per provar el que aprenguis. '
            'La resta la poses tu: ganes de passar-ho bé!', 12)
    c.showPage()



# ======================================================================== 3 · com s'usa el llibre
def com_sus(c):
    pagina(c, 'PEKES  ·  BENVINGUDA', 'Com s’usa el quadern', 'Guia ràpida',
           'Cada tema té dues pàgines. Una per aprendre i una per jugar.', 3)

    def mini(x, ytop, w, h, titol, jocs):
        rr(c, x + 3.4, ytop - h - 3.4, w, h, 6, fill=SOMBRA, lw=0)
        rr(c, x, ytop - h, w, h, 6, fill=CREMA, lw=1.7, col=NAVY)
        c.setFillColor(NAVY)
        c.rect(x + 1, ytop - 6, w - 2, 5, stroke=0, fill=1)
        txt(c, x + 10, ytop - 22, titol, 8.6, SERIFB, NAVY)
        if not jocs:
            for k in range(4):
                rr(c, x + 10 + k * 25, ytop - 40, 21, 8, 4, fill=NAVY if k == 1 else white, lw=0.8, col=NAVY_SOFT)
            rr(c, x + 10, ytop - 78, w - 20, 30, 5, fill=white, lw=1.1, col=NAVY)
            mussol(c, x + 24, ytop - 62, 0.13, color=False, lw=1.4)
            for k in range(3):
                nm = ('DO', 'RE', 'MI')[k]
                rr(c, x + 10 + k * ((w - 28) / 3 + 4), ytop - 140, (w - 28) / 3, 52, 4, fill=HexColor(COL[nm]), lw=1.1, col=NAVY)
            rr(c, x + 10, ytop - 178, w - 20, 26, 4, fill=WARM, lw=1.1, col=OCRE)
            rr(c, x + 10, ytop - 210, w - 20, 24, 4, fill=WARM, lw=1.1, col=OCRE)
        else:
            rr(c, x + 10, ytop - 66, w - 20, 36, 4, fill=white, lw=1.1, col=NAVY)
            for k in range(14):
                c.setStrokeColor(NAVY_SOFT)
                c.setLineWidth(0.5)
                c.line(x + 16 + k * ((w - 32) / 14.0), ytop - 66, x + 16 + k * ((w - 32) / 14.0), ytop - 38)
            rr(c, x + 10, ytop - 140, (w - 24) / 2, 66, 4, fill=white, lw=1.1, col=NAVY)
            rr(c, x + 14 + (w - 24) / 2, ytop - 140, (w - 24) / 2, 66, 4, fill=white, lw=1.1, col=NAVY)
            rr(c, x + 10, ytop - 210, (w - 24) / 2, 62, 4, fill=white, lw=1.1, col=NAVY)
            rr(c, x + 14 + (w - 24) / 2, ytop - 210, (w - 24) / 2, 62, 4, fill=white, lw=1.1, col=NAVY)
    yt = Y(130)
    mw = 150
    mini(M + 10, yt, mw, 230, 'Do, Re i Mi', False)
    txt(c, M + 10 + mw / 2, yt - 250, 'APRENC', 15, ETQ, NAVY, 'c')
    par(c, M + 10, yt - 268, 'Una idea per pàgina, amb dibuixos i colors. En Mussol t’ho explica.', 11.5, mw, 15, SANS, INK)
    mini(M + 190, yt, mw, 230, 'a jugar!', True)
    txt(c, M + 190 + mw / 2, yt - 250, 'JUGUEM', 15, ETQ, NAVY, 'c')
    par(c, M + 190, yt - 268, 'Jocs per practicar el que has après: pintar, unir, sopes de lletres…', 11.5, mw, 15, SANS, INK)
    # llegenda de caixes
    lx = M + 372
    txt(c, lx, yt - 4, 'LES CAIXES', 9.6, ETQ, OCRE)
    entries = [('RECORDA', 'El més important del tema, per no oblidar-ho.'),
               ('SABIES QUE?', 'Una curiositat de la música.'),
               ('ESCOLTO', 'Un moment per escoltar o tocar.')]
    yy = yt - 26
    for (e, t) in entries:
        c.setFillColor(OCRE)
        c.circle(lx + 14, yy - 6, 13, stroke=0, fill=1)
        txt(c, lx + 14, yy - 11, ICONES[e], 13, SYM, white, 'c')
        txt(c, lx + 36, yy - 3, e, 11.5, ETQ, OCRE)
        yy = par(c, lx + 36, yy - 18, t, 10.8, 126, 13.5, SANS, INK) - 14
    yy -= 6
    txt(c, lx, yy, 'EL MAPA', 9.6, ETQ, OCRE)
    xip_w = 70
    rr(c, lx, yy - 30, xip_w, 22, 11, fill=NAVY, lw=0)
    txt(c, lx + xip_w / 2, yy - 23, 'EL TEMA', 9.2, ETQ, white, 'c')
    par(c, lx, yy - 48, 'Et diu en quin tema ets, i què ve després.', 10.8, 140, 13.5, SANS, INK)
    # regles d'or
    yt2 = Y(470)
    panell(c, M, yt2, CW, 210, 'LES TRES REGLES D’OR DEL PIANISTA')
    regles = [('1', 'ESQUENA DRETA', 'Seu a la vora de la banqueta, amb els peus a terra.'),
              ('2', 'MANS ARRODONIDES', 'Com si sostinguessis una pilota petita.'),
              ('3', 'ESCOLTA SEMPRE', 'Les orelles són la meitat del pianista.')]
    cw = (CW - 28 - 24) / 3.0
    for k, (n, t, d) in enumerate(regles):
        x = M + 14 + k * (cw + 12)
        rr(c, x, yt2 - 190, cw, 142, 8, fill=WARM, lw=1.4, col=OCRE)
        c.setFillColor(OCRE)
        c.circle(x + cw / 2, yt2 - 76, 20, stroke=0, fill=1)
        txt(c, x + cw / 2, yt2 - 84, n, 24, SERIFB, white, 'c')
        txt(c, x + cw / 2, yt2 - 116, t, 11.5, ETQ, NAVY, 'c')
        par(c, x + 10, yt2 - 136, d, 11.5, cw - 20, 14.5, SANS, INK)
    caixa_t(c, M, Y(702), CW, 76, 'RECORDA',
            'No cal córrer. Aprendre música és com pujar escales: un esglaó cada vegada!', 12)
    c.showPage()


# ======================================================================== 4 · índex
def index(c):
    pagina(c, 'PEKES  ·  BENVINGUDA', 'Què hi ha aquí dins', 'Índex', 'Vuit capítols, trenta-quatre temes i un munt de jocs.', 4)
    colw = (CW - 24) / 2.0
    cols = [[1, 2, 3, 4], [5, 6, 7, 8]]
    for ci, caps in enumerate(cols):
        x = M + ci * (colw + 24)
        y = Y(128)
        for cap_ in caps:
            hexc = HexColor(COLORS7[(cap_ - 1) % 7])
            rr(c, x, y - 22, colw, 26, 7, fill=NAVY, lw=0)
            c.setFillColor(HexColor(COLORS7[(cap_ - 1) % 7]))
            c.circle(x + 15, y - 9, 10, stroke=0, fill=1)
            txt(c, x + 15, y - 13.4, str(cap_), 12, SANSB, INK if (cap_ - 1) % 7 == 2 else white, 'c')
            txt(c, x + 34, y - 13, pla.CAPITOLS[cap_].upper(), 10.3, ETQ, white)
            y -= 36
            for t in pla.temes_del_cap(cap_):
                txt(c, x + 8, y, str(t['n']), 10, SANSB, OCRE)
                txt(c, x + 30, y, t['titol'], 11.2, SANS, INK)
                txt(c, x + colw - 4, y, str(t['pag']), 11.2, SANSB, NAVY, 'r')
                tw = stringWidth(t['titol'], SANS, 11.2)
                trac(c, 0.8, RULE, (1, 3))
                c.line(x + 34 + tw, y + 3, x + colw - 24, y + 3)
                c.setDash()
                y -= 19
            y -= 12
        if ci == 1:
            rr(c, x, y - 22, colw, 26, 7, fill=OCRE, lw=0)
            txt(c, x + 34, y - 13, 'ANNEXOS', 10.3, ETQ, white)
            y -= 36
            for (t, p_, k) in pla.ANNEX_PAG:
                txt(c, x + 30, y, t, 11.2, SANS, INK)
                txt(c, x + colw - 4, y, str(p_), 11.2, SANSB, NAVY, 'r')
                y -= 19
    c.showPage()
