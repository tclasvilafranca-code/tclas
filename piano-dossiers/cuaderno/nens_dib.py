# -*- coding: utf-8 -*-
"""Dibuixos vectorials nets (traç net, sense tremolor) per al Quadern PEKES: piano, mecanisme,
   nen assegut, ós, ocell, mà en arc, fletxes i ones. Tot a la paleta TCLAS."""
import math

from reportlab.lib.colors import HexColor, white
from nens_tclas import (NAVY, NAVY_SOFT, WARM, WARM2, SOMBRA, MUTED, OCRE, INK, trac, rr, txt, SANSB, SANS,
                        teclat)

FUSTA = HexColor('#E9DBBF')
FUSTA_FOSCA = HexColor('#C9B48A')
ROSA = HexColor('#F6D9C4')


def _path(c, pts, closed=True, fill=1, stroke=1, curves=None):
    p = c.beginPath()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    if closed:
        p.close()
    c.drawPath(p, stroke=stroke, fill=fill)


def corba(c, segs, fill=1, stroke=1, closed=True):
    """segs: [(x0,y0), (c1x,c1y,c2x,c2y,x,y), ...] — camí amb Béziers."""
    p = c.beginPath()
    p.moveTo(*segs[0])
    for s in segs[1:]:
        if len(s) == 2:
            p.lineTo(*s)
        else:
            p.curveTo(*s)
    if closed:
        p.close()
    c.drawPath(p, stroke=stroke, fill=fill)


def fletxa(c, x1, y1, x2, y2, lw=1.8, col=NAVY, cap=8, doble=False):
    trac(c, lw, col)
    a = math.atan2(y2 - y1, x2 - x1)
    c.line(x1, y1, x2 - math.cos(a) * cap * 0.6, y2 - math.sin(a) * cap * 0.6)
    c.setFillColor(col)

    def cap_(x, y, ang):
        _path(c, [(x, y), (x - cap * math.cos(ang - 0.45), y - cap * math.sin(ang - 0.45)),
                  (x - cap * math.cos(ang + 0.45), y - cap * math.sin(ang + 0.45))], True, 1, 0)
    cap_(x2, y2, a)
    if doble:
        cap_(x1, y1, a + math.pi)


# ------------------------------------------------------------------ piano vertical
def _grad(c, path, x0, y0, x1, y1, a, b):
    c.saveState()
    c.clipPath(path, stroke=0, fill=0)
    c.linearGradient(x0, y0, x1, y1, (a, b), extend=False)
    c.restoreState()


def _rrpath(c, x, y, w, h, r):
    p = c.beginPath()
    p.roundRect(x, y, w, h, r)
    return p


def peça(c, x, y, w, h, r, a, b, lw=1.8, vertical=False):
    """Peça de fusta amb degradat suau i contorn."""
    c.setFillColor(a)
    c.drawPath(_rrpath(c, x, y, w, h, r), stroke=0, fill=1)
    if vertical:
        _grad(c, _rrpath(c, x, y, w, h, r), x, y + h, x, y, a, b)
    else:
        _grad(c, _rrpath(c, x, y, w, h, r), x, y, x + w, y, a, b)
    trac(c, lw, NAVY)
    c.drawPath(_rrpath(c, x, y, w, h, r), stroke=1, fill=0)


def piano(c, cx, yb, s=1.0, color=True):
    """Piano vertical vist de cara: tapa, atril amb partitura, teclat de 88 tecles, pedals i potes.
       Ample 256·s, alt 222·s (des del terra). Retorna els punts de les parts per a les etiquetes."""
    def X(v):
        return cx + v * s

    def Yy(v):
        return yb + v * s
    if color:
        f1, f2, f3 = HexColor('#C98B57'), HexColor('#9B5E34'), HexColor('#7E4A28')
        daurat = (HexColor('#F3D77C'), HexColor('#B88B1E'))
    else:
        f1, f2, f3 = HexColor('#EDE9DE'), HexColor('#D2CCBB'), HexColor('#B8B19E')
        daurat = (HexColor('#F2F0EA'), HexColor('#A9A596'))
    # ombra al terra
    c.setFillColor(SOMBRA)
    c.ellipse(X(-132), Yy(-5), X(132), Yy(7), stroke=0, fill=1)
    # peus + sòcol
    for sg in (-1, 1):
        peça(c, X(sg * 96 - 17), Yy(2), 34 * s, 24 * s, 3, f2, f3, 1.6)
    peça(c, X(-124), Yy(18), 248 * s, 14 * s, 3, f2, f3, 1.6)
    # cos principal (panell de sota)
    peça(c, X(-120), Yy(30), 240 * s, 40 * s, 4, f1, f2, 1.8)
    trac(c, 1.3, NAVY_SOFT)                       # filet del panell
    c.roundRect(X(-100), Yy(35), 200 * s, 29 * s, 4, stroke=1, fill=0)
    # pedals daurats
    for dx in (-26, 0, 26):
        c.setFillColor(daurat[0])
        pth = c.beginPath()
        pth.moveTo(X(dx - 9), Yy(8))
        pth.lineTo(X(dx + 9), Yy(8))
        pth.lineTo(X(dx + 7), Yy(1))
        pth.lineTo(X(dx - 7), Yy(1))
        pth.close()
        c.drawPath(pth, stroke=0, fill=1)
        _grad(c, pth, X(dx - 9), Yy(8), X(dx + 9), Yy(1), daurat[0], daurat[1])
        trac(c, 1.4, NAVY)
        c.drawPath(pth, stroke=1, fill=0)
        c.line(X(dx), Yy(8), X(dx), Yy(30))
    # vores laterals del teclat (galtes) i teclat
    for sg in (-1, 1):
        peça(c, X(sg * 109 - 6), Yy(66), 12 * s, 38 * s, 2, f1, f2, 1.6)
    c.setFillColor(HexColor('#EFEBDF'))
    nb = 52
    kx0, kw = X(-103), 206 * s / nb
    c.setFillColor(white)
    c.rect(kx0, Yy(68), 206 * s, 34 * s, stroke=0, fill=1)
    _grad(c, _rrpath(c, kx0, Yy(68), 206 * s, 34 * s, 0.1), kx0, Yy(86), kx0, Yy(68), white, HexColor('#E2DCCB'))
    trac(c, 0.45, NAVY_SOFT)
    for i in range(1, nb):
        c.line(kx0 + i * kw, Yy(68), kx0 + i * kw, Yy(101))
    trac(c, 1.4, NAVY)
    c.rect(kx0, Yy(68), 206 * s, 34 * s, stroke=1, fill=0)
    # tecles negres (88 tecles: comença en LA0; hi ha negra després de LA, DO, RE, FA i SOL)
    lletres = 'ABCDEFG'
    c.setFillColor(NAVY)
    for i in range(nb - 1):
        if lletres[i % 7] in 'ACDFG':
            c.rect(kx0 + (i + 1) * kw - kw * 0.3, Yy(81), kw * 0.6, 21 * s, stroke=0, fill=1)
    # tapa del teclat (feltre vermell) i taulell
    c.setFillColor(HexColor('#8C2F39'))
    c.rect(kx0, Yy(100), 206 * s, 2.4, stroke=0, fill=1)
    peça(c, X(-120), Yy(104), 240 * s, 12 * s, 3, f1, f2, 1.8)
    # placa amb el nom
    c.setFillColor(daurat[0])
    c.roundRect(X(-22), Yy(106), 44 * s, 8 * s, 2, stroke=0, fill=1)
    _grad(c, _rrpath(c, X(-22), Yy(106), 44 * s, 8 * s, 2), X(-22), Yy(114), X(22), Yy(106), daurat[0], daurat[1])
    trac(c, 1.0, NAVY)
    c.roundRect(X(-22), Yy(106), 44 * s, 8 * s, 2, stroke=1, fill=0)
    # panell superior amb l'atril
    peça(c, X(-120), Yy(116), 240 * s, 82 * s, 4, f1, f2, 1.8)
    trac(c, 1.3, NAVY_SOFT)
    c.roundRect(X(-108), Yy(150), 216 * s, 42 * s, 4, stroke=1, fill=0)
    # atril i partitura
    peça(c, X(-70), Yy(118), 140 * s, 7 * s, 2, f2, f3, 1.6)
    c.setFillColor(white)
    trac(c, 1.6, NAVY)
    pg = c.beginPath()
    pg.moveTo(X(-62), Yy(125))
    pg.lineTo(X(62), Yy(125))
    pg.lineTo(X(56), Yy(184))
    pg.lineTo(X(-56), Yy(184))
    pg.close()
    c.drawPath(pg, stroke=1, fill=1)
    trac(c, 0.8, NAVY_SOFT)
    for k, yy in enumerate((150, 172)):
        for r in range(5):
            c.line(X(-50), Yy(yy - r * 3.8 + (-1 if k == 0 else 0)), X(50), Yy(yy - r * 3.8 + (-1 if k == 0 else 0)))
    c.setFillColor(NAVY)
    for (nx, yy) in ((-36, 146), (-22, 150), (-8, 142), (8, 154), (24, 146), (38, 150), (-30, 168), (-12, 172), (6, 164),
                     (22, 170), (36, 166)):
        c.ellipse(X(nx - 2.6), Yy(yy - 1.8), X(nx + 2.6), Yy(yy + 1.8), stroke=0, fill=1)
        c.setLineWidth(0.9)
        trac(c, 0.9, NAVY)
        c.line(X(nx + 2.5), Yy(yy), X(nx + 2.5), Yy(yy + 9))
    # tapa superior
    peça(c, X(-128), Yy(198), 256 * s, 16 * s, 5, f1, f2, 1.8)
    trac(c, 1.0, white if color else NAVY_SOFT)
    c.line(X(-118), Yy(210), X(110), Yy(210))
    return dict(tapa=(X(0), Yy(214)), atril=(X(0), Yy(150)), teclat=(X(0), Yy(86)), pedals=(X(26), Yy(4)),
                pota=(X(96), Yy(8)), cos=(X(118), Yy(150)), martells=(X(0), Yy(130)))


def mecanisme(c, x, y, s=1.0, color=True):
    """Tecla -> martellet -> corda, en secció (de costat). (x,y) = cantonada inferior esquerra; 190×120·s.
       Retorna punts: tecla, martell, corda."""
    def X(v):
        return x + v * s

    def Yy(v):
        return y + v * s
    fusta, fusta2 = (HexColor('#C98B57'), HexColor('#9B5E34')) if color else (HexColor('#EDE9DE'), HexColor('#CFC9B7'))
    feltre = HexColor('#9A8F86') if color else HexColor('#BDB7A8')
    daurat = HexColor('#E7BE46') if color else HexColor('#8F8A7C')
    # marc de la caixa (fons)
    # tecla: palanca de fusta amb la cara blanca a l'esquerra
    pth = c.beginPath()
    pth.moveTo(X(0), Yy(10))
    pth.lineTo(X(130), Yy(12))
    pth.lineTo(X(130), Yy(32))
    pth.lineTo(X(0), Yy(30))
    pth.close()
    c.setFillColor(white)
    c.drawPath(pth, stroke=0, fill=1)
    _grad(c, pth, X(0), Yy(30), X(0), Yy(10), white, HexColor('#E6E0CF'))
    trac(c, 1.9, NAVY)
    c.drawPath(pth, stroke=1, fill=0)
    # punt de gir (balancí)
    peça(c, X(80), Yy(0), 10 * s, 12 * s, 2, fusta, fusta2, 1.6)
    c.setFillColor(NAVY)
    c.circle(X(85), Yy(21), 2.6 * s, stroke=0, fill=1)
    # varetes del mecanisme
    trac(c, 3.0, NAVY)
    c.line(X(112), Yy(32), X(112), Yy(66))
    trac(c, 1.6, fusta)
    c.line(X(112), Yy(32), X(112), Yy(66))
    # martellet: mànec + cap de feltre
    trac(c, 3.0, NAVY)
    c.line(X(112), Yy(60), X(138), Yy(84))
    trac(c, 1.6, fusta)
    c.line(X(112), Yy(60), X(138), Yy(84))
    c.setFillColor(feltre)
    trac(c, 1.9, NAVY)
    c.ellipse(X(130), Yy(80), X(152), Yy(100), stroke=1, fill=1)
    c.setFillColor(HexColor('#6F655D') if color else white)
    c.ellipse(X(136), Yy(86), X(146), Yy(95), stroke=0, fill=1)
    # corda
    c.setLineCap(0)
    trac(c, 3.2, NAVY)
    c.line(X(100), Yy(108), X(190), Yy(108))
    trac(c, 1.8, daurat)
    c.line(X(100), Yy(108), X(190), Yy(108))
    return dict(tecla=(X(10), Yy(36)), martell=(X(141), Yy(76)), corda=(X(170), Yy(112)))


# ------------------------------------------------------------------ nen assegut (vist de costat)
def _membre(c, pts, w, fill, lw=2.0):
    """Braç o cama: polilínia gruixuda amb contorn (traç fosc a sota, color a sobre)."""
    p = c.beginPath()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    c.setLineJoin(1)
    c.setLineCap(1)
    c.setStrokeColor(NAVY)
    c.setLineWidth(w + 2 * lw)
    c.drawPath(p, stroke=1, fill=0)
    c.setStrokeColor(fill)
    c.setLineWidth(w)
    c.drawPath(p, stroke=1, fill=0)


def nen_assegut(c, x, y, s=1.0, color=True):
    """Nen assegut davant del piano, de perfil. (x,y) = terra, sota la banqueta. Retorna punts d'interès.
       Ample total ~ 190·s, alt ~ 165·s."""
    if color:
        samarreta, pantalo, sabata, cabell, fusta1, fusta2 = (HexColor('#6FB1E0'), HexColor('#45557A'), HexColor('#8A5A3C'),
                                                             HexColor('#5A3B28'), HexColor('#C98B57'), HexColor('#9B5E34'))
        pell = PELL
    else:
        samarreta, pantalo, sabata, cabell, fusta1, fusta2 = (white, HexColor('#C9C4B6'), HexColor('#8F8A7C'),
                                                             HexColor('#6F6A5E'), HexColor('#EDE9DE'), HexColor('#D2CCBB'))
        pell = white

    def X(v):
        return x + v * s

    def Yy(v):
        return y + v * s
    lw = 2.0
    # terra
    trac(c, 1.2, SOMBRA)
    c.line(X(-60), Yy(0), X(170), Yy(0))
    # piano (només la part de davant)
    peça(c, X(100), Yy(8), 64 * s, 150 * s, 4, fusta1, fusta2, 1.9)
    peça(c, X(94), Yy(156), 76 * s, 12 * s, 4, fusta1, fusta2, 1.9)
    trac(c, 1.2, NAVY_SOFT)
    c.roundRect(X(110), Yy(16), 44 * s, 30 * s, 3, stroke=1, fill=0)
    # atril amb partitura
    c.setFillColor(white)
    trac(c, 1.7, NAVY)
    pg = c.beginPath()
    pg.moveTo(X(100), Yy(88))
    pg.lineTo(X(88), Yy(84))
    pg.lineTo(X(88), Yy(138))
    pg.lineTo(X(100), Yy(142))
    pg.close()
    c.drawPath(pg, stroke=1, fill=1)
    # teclat
    peça(c, X(70), Yy(54), 36 * s, 8 * s, 2, fusta1, fusta2, 1.8)
    c.setFillColor(white)
    trac(c, 1.5, NAVY)
    c.rect(X(66), Yy(62), 40 * s, 6 * s, stroke=1, fill=1)
    c.setFillColor(NAVY)
    for kx in (72, 82, 92):
        c.rect(X(kx), Yy(64), 4 * s, 4 * s, stroke=0, fill=1)
    # banqueta
    peça(c, X(-42), Yy(38), 56 * s, 9 * s, 3, fusta1, fusta2, 1.8)
    for dx in (-36, 8):
        trac(c, 2.2, NAVY)
        c.line(X(dx), Yy(38), X(dx - 3 if dx < 0 else dx + 3), Yy(0))
    # cames
    _membre(c, [(X(-6), Yy(55)), (X(40), Yy(56)), (X(40), Yy(14))], 15 * s, pantalo, lw)
    # peu
    c.setFillColor(sabata)
    trac(c, lw, NAVY)
    sh = c.beginPath()
    sh.moveTo(X(32), Yy(14))
    sh.lineTo(X(48), Yy(14))
    sh.lineTo(X(50), Yy(8))
    sh.curveTo(X(60), Yy(8), X(68), Yy(5), X(68), Yy(2))
    sh.lineTo(X(68), Yy(0))
    sh.lineTo(X(32), Yy(0))
    sh.close()
    c.drawPath(sh, stroke=1, fill=1)
    # tronc
    c.setFillColor(samarreta)
    trac(c, lw, NAVY)
    c.roundRect(X(-26), Yy(48), 30 * s, 56 * s, 12 * s, stroke=1, fill=1)
    trac(c, 1.2, NAVY_SOFT)
    c.line(X(-5), Yy(100), X(-5), Yy(88))
    # coll + cap
    trac(c, 1.0, NAVY)
    _membre(c, [(X(-7), Yy(102)), (X(-7), Yy(110))], 9 * s, pell, lw)
    c.setFillColor(pell)
    trac(c, lw, NAVY)
    c.circle(X(-6), Yy(126), 17 * s, stroke=1, fill=1)
    # nas
    c.drawPath(_nas(c, X(10.5), Yy(124), s), stroke=1, fill=1)
    # cabell
    c.setFillColor(cabell)
    hp = c.beginPath()
    hp.moveTo(X(10), Yy(133))
    hp.curveTo(X(8), Yy(147), X(-8), Yy(150), X(-18), Yy(146))
    hp.curveTo(X(-28), Yy(142), X(-26), Yy(124), X(-20), Yy(118))
    hp.curveTo(X(-18), Yy(130), X(-6), Yy(137), X(10), Yy(133))
    hp.close()
    c.drawPath(hp, stroke=1, fill=1)
    # orella, ull, boca
    c.setFillColor(pell)
    trac(c, 1.4, NAVY)
    c.circle(X(-14), Yy(122), 4.4 * s, stroke=1, fill=1)
    c.setFillColor(NAVY)
    c.circle(X(3), Yy(128), 2.0 * s, stroke=0, fill=1)
    trac(c, 1.5, NAVY)
    c.arc(X(1), Yy(113), X(9), Yy(119), 200, 140)
    c.setFillColor(HexColor('#F4A9A0') if color else HexColor('#E3DED0'))
    c.circle(X(-3), Yy(119), 3.0 * s, stroke=0, fill=1)
    # braç: espatlla -> colze -> mà
    _membre(c, [(X(-8), Yy(94)), (X(14), Yy(72)), (X(50), Yy(71))], 10 * s, samarreta, lw)
    # mà arquejada
    c.setFillColor(pell)
    trac(c, lw, NAVY)
    mp = c.beginPath()
    mp.moveTo(X(46), Yy(66))
    mp.curveTo(X(48), Yy(80), X(68), Yy(80), X(74), Yy(70))
    mp.curveTo(X(76), Yy(66), X(74), Yy(65), X(70), Yy(66))
    mp.curveTo(X(64), Yy(72), X(56), Yy(72), X(52), Yy(66))
    mp.close()
    c.drawPath(mp, stroke=1, fill=1)
    return dict(esquena=(X(-26), Yy(80)), cap=(X(-6), Yy(144)), colze=(X(14), Yy(72)), ma=(X(62), Yy(78)),
                peu=(X(52), Yy(6)), seient=(X(-14), Yy(42)), cuixa=(X(20), Yy(52)), genoll=(X(40), Yy(40)))


def _nas(c, x, y, s):
    p = c.beginPath()
    p.moveTo(x - 1 * s, y + 5 * s)
    p.curveTo(x + 3 * s, y + 4 * s, x + 5 * s, y + 1 * s, x + 4 * s, y - 1 * s)
    p.curveTo(x + 3 * s, y - 3 * s, x, y - 2 * s, x - 1 * s, y - 3 * s)
    p.close()
    return p


# ------------------------------------------------------------------ animals
def os_(c, cx, cy, s=1.0, color=True):
    """Ós (cap). Radi total ~ 44·s."""
    pel, pel2, musell = ((HexColor('#B97C4B'), HexColor('#8F5A33'), HexColor('#F0D9B5')) if color
                         else (HexColor('#D9D3C3'), HexColor('#B5AE9B'), white))
    trac(c, 2.0, NAVY)
    for dx in (-27, 27):
        c.setFillColor(pel)
        c.circle(cx + dx * s, cy + 28 * s, 13 * s, stroke=1, fill=1)
        c.setFillColor(musell)
        c.circle(cx + dx * s, cy + 28 * s, 6.5 * s, stroke=1, fill=1)
    c.setFillColor(pel)
    c.drawPath(_rrpath(c, cx - 36 * s, cy - 32 * s, 72 * s, 66 * s, 30 * s), stroke=1, fill=1)
    _grad(c, _rrpath(c, cx - 36 * s, cy - 32 * s, 72 * s, 66 * s, 30 * s), cx - 36 * s, cy, cx + 36 * s, cy, pel, pel2)
    trac(c, 2.0, NAVY)
    c.drawPath(_rrpath(c, cx - 36 * s, cy - 32 * s, 72 * s, 66 * s, 30 * s), stroke=1, fill=0)
    c.setFillColor(musell)
    c.ellipse(cx - 18 * s, cy - 24 * s, cx + 18 * s, cy + 0 * s, stroke=1, fill=1)
    c.setFillColor(NAVY)
    c.ellipse(cx - 7 * s, cy - 8 * s, cx + 7 * s, cy - 0.5 * s, stroke=0, fill=1)
    for dx in (-15, 15):
        c.circle(cx + dx * s, cy + 12 * s, 3.6 * s, stroke=0, fill=1)
        c.setFillColor(white)
        c.circle(cx + (dx + 1.1) * s, cy + 13.2 * s, 1.1 * s, stroke=0, fill=1)
        c.setFillColor(NAVY)
    trac(c, 1.7, NAVY)
    c.line(cx, cy - 8 * s, cx, cy - 13 * s)
    c.arc(cx - 9 * s, cy - 20 * s, cx, cy - 9 * s, 270, 90)
    c.arc(cx, cy - 20 * s, cx + 9 * s, cy - 9 * s, 180, 90)


def ocell(c, cx, cy, s=1.0, color=True):
    """Ocell petit, de costat, cap a la dreta. Ample ~ 80·s."""
    blau, blau2, panxa, bec = ((HexColor('#4FA3E0'), HexColor('#2E7DB8'), HexColor('#FBE7A8'), HexColor('#F2A03C'))
                               if color else (HexColor('#D9D3C3'), HexColor('#B5AE9B'), white, HexColor('#B5AE9B')))
    trac(c, 2.0, NAVY)
    # cua (3 plomes)
    c.setFillColor(blau2)
    for ang in (14, 0, -14):
        c.saveState()
        c.translate(cx - 22 * s, cy - 2 * s)
        c.rotate(180 + ang)
        c.roundRect(0, -4.5 * s, 34 * s, 9 * s, 4.5 * s, stroke=1, fill=1)
        c.restoreState()
    # cos
    c.setFillColor(blau)
    body = c.beginPath()
    body.moveTo(cx - 28 * s, cy + 2 * s)
    body.curveTo(cx - 24 * s, cy + 26 * s, cx + 14 * s, cy + 32 * s, cx + 26 * s, cy + 16 * s)
    body.curveTo(cx + 36 * s, cy + 2 * s, cx + 20 * s, cy - 26 * s, cx - 4 * s, cy - 24 * s)
    body.curveTo(cx - 20 * s, cy - 22 * s, cx - 30 * s, cy - 12 * s, cx - 28 * s, cy + 2 * s)
    body.close()
    c.drawPath(body, stroke=1, fill=1)
    # panxa
    c.setFillColor(panxa)
    pan = c.beginPath()
    pan.moveTo(cx + 24 * s, cy + 2 * s)
    pan.curveTo(cx + 30 * s, cy - 14 * s, cx + 10 * s, cy - 22 * s, cx - 4 * s, cy - 20 * s)
    pan.curveTo(cx + 6 * s, cy - 12 * s, cx + 12 * s, cy - 4 * s, cx + 24 * s, cy + 2 * s)
    pan.close()
    c.drawPath(pan, stroke=1, fill=1)
    # bec
    c.setFillColor(bec)
    bk = c.beginPath()
    bk.moveTo(cx + 30 * s, cy + 22 * s)
    bk.lineTo(cx + 48 * s, cy + 15 * s)
    bk.lineTo(cx + 30 * s, cy + 9 * s)
    bk.close()
    c.drawPath(bk, stroke=1, fill=1)
    # ull
    c.setFillColor(NAVY)
    c.circle(cx + 18 * s, cy + 20 * s, 3.4 * s, stroke=0, fill=1)
    c.setFillColor(white)
    c.circle(cx + 19 * s, cy + 21.2 * s, 1.1 * s, stroke=0, fill=1)
    # ala
    c.setFillColor(blau2)
    trac(c, 1.9, NAVY)
    wing = c.beginPath()
    wing.moveTo(cx - 14 * s, cy + 12 * s)
    wing.curveTo(cx - 2 * s, cy + 20 * s, cx + 12 * s, cy + 8 * s, cx + 10 * s, cy - 6 * s)
    wing.curveTo(cx + 6 * s, cy - 18 * s, cx - 10 * s, cy - 16 * s, cx - 20 * s, cy - 4 * s)
    wing.curveTo(cx - 22 * s, cy + 2 * s, cx - 20 * s, cy + 8 * s, cx - 14 * s, cy + 12 * s)
    wing.close()
    c.drawPath(wing, stroke=1, fill=1)
    trac(c, 1.4, NAVY)
    for k in range(3):
        c.line(cx - 12 * s + k * 6 * s, cy + 6 * s - k * 4 * s, cx - 4 * s + k * 5 * s, cy - 4 * s - k * 3 * s)
    # potetes
    trac(c, 2.0, bec if color else NAVY)
    for dx in (-2, 8):
        c.line(cx + dx * s, cy - 24 * s, cx + dx * s, cy - 36 * s)
        c.line(cx + dx * s, cy - 36 * s, cx + (dx + 6) * s, cy - 36 * s)


def ona(c, x, y, w, amp, cicles, lw=2.4, col=NAVY):
    """Ona sinusoïdal des de (x,y) amb `cicles` cicles dins de l'ample `w`."""
    trac(c, lw, col)
    n = 60
    pts = [(x + w * i / n, y + amp * math.sin(2 * math.pi * cicles * i / n)) for i in range(n + 1)]
    _path(c, pts, closed=False, fill=0, stroke=1)


# ------------------------------------------------------------------ mà en arc (de costat)
def ma_costat(c, x, y, correcta=True, s=1.0):
    """Una mà vista de costat sobre una tecla. (x,y) = canell. Ample ~ 100·s."""
    def X(v):
        return x + v * s

    def Yy(v):
        return y + v * s
    # tecla
    trac(c, 1.6, NAVY)
    c.setFillColor(white)
    c.roundRect(X(20), Yy(-10), 90 * s, 14 * s, 3, stroke=1, fill=1)
    trac(c, 2.0, NAVY)
    c.setFillColor(ROSA)
    if correcta:
        corba(c, [(X(0), Yy(4)), (X(10), Yy(26), X(30), Yy(46), X(54), Yy(44)),
                  (X(78), Yy(42), X(92), Yy(30), X(98), Yy(8)),
                  (X(96), Yy(2), X(88), Yy(2), X(86), Yy(6)),
                  (X(80), Yy(24), X(66), Yy(28), X(54), Yy(28)),
                  (X(40), Yy(28), X(26), Yy(18), X(16), Yy(2)),
                  (X(12), Yy(-2), X(4), Yy(-2), X(0), Yy(4))])
    else:
        corba(c, [(X(0), Yy(4)), (X(20), Yy(12), X(50), Yy(10), X(72), Yy(8)),
                  (X(88), Yy(6), X(98), Yy(8), X(102), Yy(4)),
                  (X(104), Yy(-2), X(98), Yy(-2), X(94), Yy(0)),
                  (X(70), Yy(-2), X(30), Yy(-4), X(4), Yy(-6)),
                  (X(0), Yy(-4), X(-2), Yy(0), X(0), Yy(4))])


# ------------------------------------------------------------------ mà (vista de dalt, dits amunt)
PELL = HexColor('#F5CDAF')
PELL_FOSC = HexColor('#E3A985')


def _capsula(c, cx, cy, w, h, ang, dx=0.0, dy=0.0):
    """Cantonada: capsula de base (cx,cy), amplada w, llargada h, girada `ang` graus (0 = amunt)."""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(ang)
    c.roundRect(-w / 2.0 + dx, dy, w, h, w / 2.0, stroke=_capsula.stroke, fill=_capsula.fill)
    c.restoreState()


_capsula.stroke = 1
_capsula.fill = 1


_DITS_DEF = {2: (-31, 42, 21, 76, 5), 3: (-10, 46, 22, 86, 0.5), 4: (11, 43, 21, 77, -4),
             5: (31, 34, 18.5, 60, -10), 1: (-40, 6, 24, 62, 52)}


def punts_dits(cx, cy, s=1.0, esq=False):
    """Posició (x, y) on van els números de cada dit d'`ma_real`: {dit: (x, y)}."""
    sg = -1 if esq else 1
    out = {}
    for n, (bx, by, w, l, ang) in _DITS_DEF.items():
        a = math.radians(ang)
        out[n] = (sg * (bx - math.sin(a) * (l + 15)) * s + cx, (by + math.cos(a) * (l + 15)) * s + cy)
    return out


def ma_real(c, cx, cy, s=1.0, esq=False, dits=True, color=True, lw=2.2, numeros=(1, 2, 3, 4, 5), marca=None):
    """Mà vista pel dors, dits amunt. (cx,cy) = centre del palmell. Alt ~ 200·s. `esq` la mirall.
       `marca`: {dit: color} pinta aquell dit (per als jocs)."""
    sg = -1 if esq else 1
    fill = PELL if color else white
    fosc = PELL_FOSC if color else HexColor('#D9D3C3')
    marca = marca or {}
    # (x base, y base, ample, llarg, angle) — dits 2,3,4,5 i polze
    dits_def = _DITS_DEF

    def dib(stroke):
        c.saveState()
        c.translate(cx, cy)
        c.scale(sg * s, s)
        # palmell + canell
        c.roundRect(-46, -30, 92, 94, 30, stroke=stroke, fill=1)
        c.roundRect(-28, -62, 56, 50, 10, stroke=stroke, fill=1)
        for n, (bx, by, w, l, ang) in dits_def.items():
            c.saveState()
            c.translate(bx, by)
            c.rotate(ang)
            c.roundRect(-w / 2.0, 0, w, l, w / 2.0, stroke=stroke, fill=1)
            c.restoreState()
        c.restoreState()
    # 1) contorn gruixut sota, 2) emplenat per damunt = només queda la silueta
    trac(c, lw * 2 / 1.0, NAVY)
    c.setFillColor(NAVY)
    c.saveState()
    c.setLineWidth(lw * 2)
    dib(1)
    c.restoreState()
    c.setFillColor(fill)
    dib(0)
    # dits marcats
    for n, colr in marca.items():
        bx, by, w, l, ang = dits_def[n]
        c.saveState()
        c.translate(cx, cy)
        c.scale(sg * s, s)
        c.translate(bx, by)
        c.rotate(ang)
        c.setFillColor(HexColor(colr))
        c.roundRect(-w / 2.0, 0, w, l, w / 2.0, stroke=0, fill=1)
        c.restoreState()
    # detalls: ungles, artelles, osset
    c.saveState()
    c.translate(cx, cy)
    c.scale(sg * s, s)
    trac(c, max(1.0, lw * 0.55), NAVY_SOFT)
    for n, (bx, by, w, l, ang) in dits_def.items():
        c.saveState()
        c.translate(bx, by)
        c.rotate(ang)
        # ungla
        c.setFillColor(HexColor('#FBE9DC') if color else WARM)
        c.roundRect(-w * 0.34, l - w * 0.95, w * 0.68, w * 0.72, w * 0.32, stroke=1, fill=1)
        # artelles dels dits (dues rugositats curtes)
        if n != 1:
            for fr in (0.38, 0.66):
                ym = l * fr
                c.line(-w * 0.28, ym, -w * 0.06, ym - 1.4)
                c.line(w * 0.06, ym - 1.4, w * 0.28, ym)
        else:
            ym = l * 0.45
            c.line(-w * 0.28, ym, -w * 0.06, ym - 1.4)
            c.line(w * 0.06, ym - 1.4, w * 0.28, ym)
        c.restoreState()
    # os del dors de la mà (tendons suggerits)
    trac(c, max(0.8, lw * 0.4), fosc)
    for bx in (-31, -10, 11, 31):
        c.line(bx * 0.9, 14, bx * 1.0, 40)
    c.restoreState()
    if dits:
        for n, (bx, by, w, l, ang) in dits_def.items():
            a = math.radians(ang)
            tx = sg * (bx - math.sin(a) * (l + 15)) * s + cx
            ty = (by + math.cos(a) * (l + 15)) * s + cy
            c.setFillColor(NAVY)
            rr_ = max(7.2, 9.2 * s)
            c.circle(tx, ty, rr_, stroke=0, fill=1)
            txt(c, tx, ty - rr_ * 0.46, str(n), rr_ * 1.36, SANSB, white, 'c')


def bola(c, x, y, n, r=11, fill=OCRE, size=None):
    """Cercle amb un número (per assenyalar parts d'un dibuix)."""
    c.setFillColor(fill)
    trac(c, 1.6, white)
    c.circle(x, y, r, stroke=1, fill=1)
    txt(c, x, y - (size or r * 1.05) * 0.36, str(n), size or r * 1.05, SANSB, white, 'c')


def clau_llarga(c, x1, y1, x2, y2):
    """Línia d'assenyalament fina amb un punt a l'extrem (x2,y2)."""
    trac(c, 1.3, NAVY)
    c.line(x1, y1, x2, y2)
    c.setFillColor(NAVY)
    c.circle(x2, y2, 2.6, stroke=0, fill=1)


# ------------------------------------------------------------------ icones per al ritme i la música
def cor(c, cx, cy, s=1.0, color=True):
    """Cor (el pols del cos)."""
    fil = HexColor('#E4392B') if color else HexColor('#E3DED0')
    trac(c, 2.0, NAVY)
    c.setFillColor(fil)
    p = c.beginPath()
    p.moveTo(cx, cy - 26 * s)
    p.curveTo(cx - 48 * s, cy + 2 * s, cx - 30 * s, cy + 34 * s, cx, cy + 14 * s)
    p.curveTo(cx + 30 * s, cy + 34 * s, cx + 48 * s, cy + 2 * s, cx, cy - 26 * s)
    p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(white)
    c.ellipse(cx - 24 * s, cy + 8 * s, cx - 14 * s, cy + 20 * s, stroke=0, fill=1)


def rellotge(c, cx, cy, s=1.0, color=True):
    trac(c, 2.0, NAVY)
    c.setFillColor(HexColor('#F6D9A0') if color else HexColor('#EDE9DE'))
    c.circle(cx, cy, 30 * s, stroke=1, fill=1)
    c.setFillColor(white)
    c.circle(cx, cy, 25 * s, stroke=1, fill=1)
    trac(c, 1.2, NAVY)
    for k in range(12):
        a = math.radians(k * 30)
        r1, r2 = (21 if k % 3 == 0 else 22.5) * s, 25 * s
        c.line(cx + r1 * math.sin(a), cy + r1 * math.cos(a), cx + r2 * math.sin(a), cy + r2 * math.cos(a))
    trac(c, 2.4, NAVY)
    c.line(cx, cy, cx + 12 * s * math.sin(math.radians(60)), cy + 12 * s * math.cos(math.radians(60)))
    trac(c, 1.6, NAVY)
    c.line(cx, cy, cx, cy + 19 * s)
    c.setFillColor(NAVY)
    c.circle(cx, cy, 2.4 * s, stroke=0, fill=1)


def petjades(c, cx, cy, s=1.0, color=True):
    """Dues petjades de sabata (caminar al ritme del pols)."""
    trac(c, 1.8, NAVY)
    c.setFillColor(HexColor('#8A5A3C') if color else HexColor('#CFC9B7'))
    for (dx, dy, ang) in ((-13, -14, 10), (13, 12, -10)):
        c.saveState()
        c.translate(cx + dx * s, cy + dy * s)
        c.rotate(ang)
        sol = c.beginPath()
        sol.moveTo(0, 20 * s)
        sol.curveTo(9 * s, 20 * s, 11 * s, 8 * s, 8 * s, 0)
        sol.curveTo(6 * s, -6 * s, 6 * s, -8 * s, 6 * s, -10 * s)
        sol.lineTo(-6 * s, -10 * s)
        sol.curveTo(-6 * s, -8 * s, -6 * s, -6 * s, -8 * s, 0)
        sol.curveTo(-11 * s, 8 * s, -9 * s, 20 * s, 0, 20 * s)
        sol.close()
        c.drawPath(sol, stroke=1, fill=1)
        c.ellipse(-6 * s, -22 * s, 6 * s, -13 * s, stroke=1, fill=1)
        c.restoreState()


def metronom(c, cx, yb, s=1.0, color=True):
    """Metrònom de piràmide amb el pèndol. Alt ~ 118·s, ample ~ 60·s (la base)."""
    fusta, fusta2 = (HexColor('#C98B57'), HexColor('#9B5E34')) if color else (HexColor('#EDE9DE'), HexColor('#CFC9B7'))
    p = c.beginPath()
    p.moveTo(cx - 30 * s, yb)
    p.lineTo(cx + 30 * s, yb)
    p.lineTo(cx + 12 * s, yb + 108 * s)
    p.lineTo(cx - 12 * s, yb + 108 * s)
    p.close()
    c.setFillColor(fusta)
    c.drawPath(p, stroke=0, fill=1)
    _grad(c, p, cx - 30 * s, yb, cx + 30 * s, yb, fusta, fusta2)
    trac(c, 2.0, NAVY)
    c.drawPath(p, stroke=1, fill=0)
    # escala
    c.setFillColor(white)
    c.roundRect(cx - 8 * s, yb + 20 * s, 16 * s, 70 * s, 3, stroke=1, fill=1)
    trac(c, 0.9, NAVY_SOFT)
    for k in range(8):
        c.line(cx - 6 * s, yb + 26 * s + k * 8 * s, cx - 1 * s, yb + 26 * s + k * 8 * s)
    # pèndol (inclinat)
    trac(c, 2.4, NAVY)
    c.line(cx, yb + 6 * s, cx + 20 * s, yb + 112 * s)
    c.setFillColor(HexColor('#E7BE46') if color else HexColor('#BDB7A8'))
    c.roundRect(cx + 8 * s, yb + 70 * s, 11 * s, 12 * s, 2, stroke=1, fill=1)
    c.setFillColor(NAVY)
    c.circle(cx, yb + 6 * s, 3 * s, stroke=0, fill=1)


def tortuga(c, cx, cy, s=1.0, color=True):
    """Tortuga de costat, cap a la dreta. Ample ~ 100·s."""
    verd, verd2, pell = ((HexColor('#7DB84A'), HexColor('#4F8A2E'), HexColor('#B9D98F')) if color
                         else (HexColor('#DDD8C8'), HexColor('#B5AE9B'), HexColor('#EFEBDF')))
    trac(c, 2.0, NAVY)
    c.setFillColor(pell)
    for dx in (-26, 18):
        c.roundRect(cx + dx * s - 8 * s, cy - 32 * s, 16 * s, 20 * s, 6 * s, stroke=1, fill=1)
    c.ellipse(cx + 34 * s, cy - 2 * s, cx + 62 * s, cy + 18 * s, stroke=1, fill=1)
    c.circle(cx + 56 * s, cy + 8 * s, 1.8 * s, stroke=0, fill=0)
    c.setFillColor(NAVY)
    c.circle(cx + 54 * s, cy + 11 * s, 2.0 * s, stroke=0, fill=1)
    c.setFillColor(pell)
    trac(c, 2.0, NAVY)
    c.ellipse(cx - 56 * s, cy - 14 * s, cx - 38 * s, cy - 2 * s, stroke=1, fill=1)
    # closca
    cl = c.beginPath()
    cl.moveTo(cx - 44 * s, cy - 10 * s)
    cl.curveTo(cx - 44 * s, cy + 44 * s, cx + 40 * s, cy + 44 * s, cx + 40 * s, cy - 10 * s)
    cl.close()
    c.setFillColor(verd)
    c.drawPath(cl, stroke=0, fill=1)
    _grad(c, cl, cx - 44 * s, cy + 40 * s, cx + 40 * s, cy - 10 * s, verd, verd2)
    trac(c, 2.0, NAVY)
    c.drawPath(cl, stroke=1, fill=0)
    trac(c, 1.5, NAVY)
    for (a, b, c2, d) in ((-8, 0, -10, 34), (-30, 0, -26, 24), (14, 0, 12, 28)):
        c.line(cx + a * s, cy - 10 * s + 2, cx + c2 * s, cy - 10 * s + d * s)
    c.line(cx - 36 * s, cy + 12 * s, cx + 34 * s, cy + 12 * s)
    c.setFillColor(pell)
    trac(c, 2.0, NAVY)
    c.roundRect(cx - 46 * s, cy - 14 * s, 90 * s, 7 * s, 3, stroke=1, fill=1)


def coet(c, cx, cy, s=1.0, color=True, ang=-30):
    """Coet (per a «ràpid»). Alt ~ 110·s."""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(ang)
    cos, tap, finest, flama = ((white, HexColor('#E4392B'), HexColor('#6FB1E0'), HexColor('#F28C0E')) if color
                               else (white, HexColor('#B5AE9B'), HexColor('#D9D3C3'), HexColor('#BDB7A8')))
    trac(c, 2.0, NAVY)
    c.setFillColor(flama)
    fl = c.beginPath()
    fl.moveTo(-8 * s, -34 * s)
    fl.curveTo(-10 * s, -56 * s, 0, -66 * s, 0, -72 * s)
    fl.curveTo(0, -66 * s, 10 * s, -56 * s, 8 * s, -34 * s)
    fl.close()
    c.drawPath(fl, stroke=1, fill=1)
    c.setFillColor(tap)
    for sg in (-1, 1):
        fn = c.beginPath()
        fn.moveTo(sg * 14 * s, -18 * s)
        fn.lineTo(sg * 30 * s, -42 * s)
        fn.lineTo(sg * 14 * s, -32 * s)
        fn.close()
        c.drawPath(fn, stroke=1, fill=1)
    body = c.beginPath()
    body.moveTo(-16 * s, -34 * s)
    body.curveTo(-22 * s, 10 * s, -12 * s, 40 * s, 0, 54 * s)
    body.curveTo(12 * s, 40 * s, 22 * s, 10 * s, 16 * s, -34 * s)
    body.close()
    c.setFillColor(cos)
    c.drawPath(body, stroke=0, fill=1)
    _grad(c, body, -20 * s, 0, 20 * s, 0, white, HexColor('#DCD5C2'))
    trac(c, 2.0, NAVY)
    c.drawPath(body, stroke=1, fill=0)
    c.setFillColor(tap)
    cap = c.beginPath()
    cap.moveTo(-12 * s, 28 * s)
    cap.curveTo(-8 * s, 42 * s, -4 * s, 48 * s, 0, 54 * s)
    cap.curveTo(4 * s, 48 * s, 8 * s, 42 * s, 12 * s, 28 * s)
    cap.close()
    c.drawPath(cap, stroke=1, fill=1)
    c.setFillColor(finest)
    c.circle(0, 8 * s, 8 * s, stroke=1, fill=1)
    c.restoreState()
