# -*- coding: utf-8 -*-
"""HALLOWEEN · fitxes per pintar, cantar i tocar · versio PEKES (6-10 anys) · en catala.

   6 fitxes A4 apaisades, en blanc i negre (traç a mà, interior blanc per pintar), amb en
   Mussol Misol disfressat de bruixa. Les cançons són pròpies (cap dret d'autor), en posició de
   cinc dits de La menor (La Si Do Re Mi: totes tecles blanques) i les altures surten de
   `engine/notation.note_y`.

   1 El cementiri de les notes   4 El fantasma Bu!
   2 La bruixa vola              5 L'esquelet balla
   3 Carbassa per notes          6 La casa embruixada (jocs + diploma)

   python3 halloween_peques.py  ->  ../output/Halloween_Peques.pdf
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
sys.path.insert(0, HERE)
import notation as nt                                           # noqa: E402
from reportlab.lib.colors import black, white                  # noqa: E402

from dibujo_mano import texto as _texto
from dibujo_mano import (W, H, ManoCanvas, trazo, letras_huecas, caja, marco,  # noqa: E402
                         estrella, cabeza, cabeza_redonda, pentagrama, rayita, lineas_texto,
                         nube, negra_deco)
import halloween_dib as d                                       # noqa: E402
from mussol import mussol                                       # noqa: E402

OUT = os.path.join(HERE, '..', 'output', 'Halloween_Peques.pdf')
HA = 'Hand'
NOM = dict(C='DO', D='RE', E='MI', F='FA', G='SOL', A='LA', B='SI')
COLOR = dict(DO='VERMELL', RE='TARONJA', MI='GROC', FA='VERD', SOL='BLAU', LA='MORAT', SI='GRIS')


def texto(c, x, y, txt, size=11, font='Hand', align='l', col=black):
    """La lletra de mà no té el punt: es treu el punt final i els punts seguits d'espai."""
    txt = txt.rstrip('.').replace('. ', ' ')
    _texto(c, x, y, txt, size, font, align, col)


def par_h(c, x, y, txt, size=14, w=300, lead=None, align='l'):
    lead = lead or size + 4
    for ln in lineas_texto(txt, HA, size, w):
        texto(c, x, y, ln, size, HA, align)
        y -= lead
    return y


def nom_nota(p):
    return NOM[p[0]]


def peu(c, num):
    texto(c, 44, 32, 'Nom:', 15, HA)
    trazo(c, 1.2, cap=0)
    c.setDash(1, 3)
    c.line(84, 30, 270, 30)
    c.setDash()
    texto(c, W - 44, 32, 'Fitxa %d de 6 · Nit de Halloween · T-Clas' % num, 10.5, HA, 'r')


def capcalera(c, linies, size=40, y0=528, deco=True):
    marco(c)
    c.saveState()
    c.translate(W / 2, y0)
    c.rotate(0.8)
    if len(linies) == 1:
        letras_huecas(c, 0, 0, linies[0], size, semilla=5)
    else:
        letras_huecas(c, 0, 14, linies[0], size, semilla=5)
        letras_huecas(c, 0, -size + 6, linies[1], size, semilla=9)
    c.restoreState()


def etiqueta(c, x, y, n, text, size=17):
    c.setFillColor(black)
    trazo(c, 1.8)
    c.setFillColor(white)
    c.circle(x + 9, y + 5, 11, stroke=1, fill=1)
    texto(c, x + 9, y, str(n), 15, HA, 'c')
    texto(c, x + 31, y, text, size, HA)


def globus(c, x, y, w, text, size=12.5, cua='esq'):
    """Globus de conversa; (x, y) = cantonada inferior esquerra."""
    lin = lineas_texto(text, HA, size, w - 30)
    h = 16 + len(lin) * (size + 3)
    caja(c, x, y, w, h, r=10, lw=1.8)
    # cua
    c.setFillColor(white)
    trazo(c, 1.8)
    bx = x + 22 if cua == 'esq' else x + w - 22
    c.poly([(bx - 7, y + 1), (bx + 10, y + 1), (bx - 8 if cua == 'esq' else bx + 16, y - 14)], 0, 1)
    c.line(bx - 7, y, bx - 8 if cua == 'esq' else bx + 16, y - 14)
    c.line(bx + 10, y, bx - 8 if cua == 'esq' else bx + 16, y - 14)
    yy = y + h - 8 - size
    for ln in lin:
        texto(c, x + 10, yy, ln, size, HA)
        yy -= size + 3
    return h


# ------------------------------------------------------------------ notes sobre el pentagrama
def _tija(c, nx, ny, gap, amunt, lw=1.8):
    trazo(c, lw, cap=0)
    if amunt:
        c.line(nx + gap * 0.58, ny, nx + gap * 0.58, ny + gap * 3.3)
    else:
        c.line(nx - gap * 0.58, ny, nx - gap * 0.58, ny - gap * 3.3)


def dibuixa_nota(c, nx, ny, gap, dur, mitja):
    """mitja: pitch esta per sobre de la linia central (tija avall)."""
    if dur == 'w':
        cabeza_redonda(c, nx, ny, gap * 1.15)
        return
    cabeza(c, nx, ny, gap * 0.64, gap * 0.46, giro=-20, grosor=1.9, rayada=(dur == 'q'))
    _tija(c, nx, ny, gap, not mitja)


def silenci_negra(c, cx, cy, gap):
    trazo(c, 2.4)
    pts = [(cx - gap * 0.25, cy + gap * 1.5), (cx + gap * 0.35, cy + gap * 0.8),
           (cx - gap * 0.3, cy + gap * 0.1), (cx + gap * 0.3, cy - gap * 0.6),
           (cx - gap * 0.05, cy - gap * 1.0), (cx + gap * 0.3, cy - gap * 1.4)]
    c.poly(pts, 1, 0, closed=False)


def silenci_blanca(c, cx, yb, gap):
    trazo(c, 1.6)
    c.setFillColor(black)
    c.rect(cx - gap * 0.7, yb + gap * 2, gap * 1.4, gap * 0.5, stroke=1, fill=1)


def pauta_cancio(c, x, ytop, w, compassos, clau='treble', gap=11.0, lletra=True, dits=True,
                 mitja_linia='B4', bpm=4):
    """Dibuixa un pentagrama amb la clau, el compàs i `compassos` (llista de llistes de
       (pitch|None, durada en temps, síl·laba, dit)). Torna (yb, centres) per posar el
       que calgui a sota o a sobre."""
    yb = pentagrama(c, x, ytop, w, gap, lw=1.5)
    nt.draw_clef(c, x + 6, yb, gap, clau)
    nt.draw_time_sig(c, x + 38, yb, gap)
    x0 = x + 78
    ample = (x + w - 8 - x0) / float(len(compassos))
    trazo(c, 1.6)
    centres = []
    for k, comp in enumerate(compassos):
        bx = x0 + k * ample
        pas = ample / float(bpm)
        pos = 0.0
        for (pitch, dur, sil, dit) in comp:
            cx = bx + (pos + 0.5) * pas
            if dur >= 4:
                cx = bx + ample / 2.0
            if pitch is None:
                if dur >= 2:
                    silenci_blanca(c, cx, yb, gap)
                else:
                    silenci_negra(c, cx, yb + gap * 2, gap)
            else:
                ny = nt.note_y(yb, gap, pitch, clau)
                if pitch in ('C4', 'A5'):
                    rayita(c, cx, ny, gap)
                mitja_ = ny > yb + gap * 2 - 0.1
                dibuixa_nota(c, cx, ny, gap, 'w' if dur >= 4 else ('h' if dur >= 2 else 'q'), mitja_)
                centres.append((cx, ny, pitch, dit))
                if dits and dit:
                    c.setFillColor(black)
                    texto(c, cx, ytop + 14, str(dit), 13, HA, 'c')
            if lletra and sil:
                texto(c, cx, yb - 27, sil, 13 if len(sil) > 3 else 14, HA, 'c')
            pos += dur
        # barra
        trazo(c, 1.6, cap=0)
        xb = x0 + (k + 1) * ample - 4
        c.line(xb, yb, xb, ytop)
    # barra final doble
    trazo(c, 3.2, cap=0)
    c.line(x + w - 4, yb, x + w - 4, ytop)
    return yb, centres


def llegenda(c, x, y, notes, w=88, h=44, gap=8):
    """Caselles NOTA = COLOR: cada nota té el seu color per pintar-la."""
    for i, nm in enumerate(notes):
        bx = x + i * (w + gap)
        caja(c, bx, y, w, h, r=10, lw=1.8)
        texto(c, bx + w / 2, y + h - 20, nm, 18, HA, 'c')
        texto(c, bx + w / 2, y + 8, COLOR[nm], 11.5, HA, 'c')


def teclat_mini(c, x, y, w, h, primera, n, dits):
    """Teclat de n tecles blanques que comença a `primera` (p. ex. 'G4'); dits: {pitch: dit}."""
    lletres = 'CDEFGAB'
    L, o = primera[0], int(primera[1])
    ample = w / float(n)
    noms = []
    for i in range(n):
        noms.append('%s%d' % (lletres[(lletres.index(L) + i) % 7],
                              o + (lletres.index(L) + i) // 7))
    trazo(c, 1.6)
    for i, nm in enumerate(noms):
        c.setFillColor(white)
        c.rect(x + i * ample, y, ample, h, stroke=1, fill=1)
    # tecles negres
    for i, nm in enumerate(noms[:-1]):
        if nm[0] in 'CDFGA':
            trazo(c, 1.4)
            c.setFillColor(black)
            c.rect(x + (i + 1) * ample - ample * 0.3, y + h * 0.5, ample * 0.6, h * 0.5, stroke=1, fill=1)
    for i, nm in enumerate(noms):
        cx = x + i * ample + ample / 2
        if nm in dits:
            trazo(c, 1.8)
            c.setFillColor(white)
            c.circle(cx, y + 21, 8.5, stroke=1, fill=1)
            texto(c, cx, y + 16.5, str(dits[nm]), 13, HA, 'c')
        texto(c, cx, y + 4, NOM[nm[0]], 10, HA, 'c')


# ------------------------------------------------------------------ fitxa 1: cementiri
def fitxa_cementiri(c):
    import math
    capcalera(c, ['EL CEMENTIRI', 'DE LES NOTES'], size=40, y0=520)
    d.luna(c, 82, 500, 30)
    d.murcielago(c, 770, 512, 0.55)
    d.murcielago(c, 700, 462, 0.35)
    d.telarana(c, 22, 574, 78)
    estrella(c, 170, 556, 11)
    estrella(c, 690, 548, 9, 0.3)
    d.arana(c, 218, 482, 0.5, hilo=574)
    texto(c, W / 2, 452, "1 · Pinta cada làpida del color de la seva nota.", 16, HA, 'c')
    texto(c, W / 2, 432, "2 · Toca les notes al piano, de l'esquerra a la dreta. Sona una escala!", 16, HA, 'c')
    notes = [('DO', 'C4'), ('RE', 'D4'), ('MI', 'E4'), ('FA', 'F4'), ('SOL', 'G4'), ('LA', 'A4'),
             ('SI', 'B4'), ('DO', 'C5')]
    tw, tg, ybase = 80, 10, 168
    x0 = (W - (8 * tw + 7 * tg)) / 2
    top = ybase + 214
    for i, (nm, alt) in enumerate(notes):
        x = x0 + i * (tw + tg)
        trazo(c, 2.4)
        c.setFillColor(white)
        pts = [(x, ybase), (x + tw, ybase), (x + tw, top - 36)]
        for a_ in range(0, 181, 15):
            r_ = math.radians(a_)
            pts.append((x + tw / 2 + tw / 2 * math.cos(r_), top - 36 + 38 * math.sin(r_)))
        pts.append((x, top - 36))
        c.poly(pts, 1, 1)
        texto(c, x + tw / 2, top - 58, nm, 23, HA, 'c')
        gp = 7.0
        yb = pentagrama(c, x + 8, top - 84, tw - 16, gp, lw=1.1)
        ny = nt.note_y(yb, gp, alt, 'treble')
        if alt == 'C4':
            rayita(c, x + tw / 2 + 4, ny, gp)
        cabeza_redonda(c, x + tw / 2 + 4, ny, gp * 1.25)
        texto(c, x + tw / 2, ybase + 70, COLOR[nm], 11.5, HA, 'c')
        trazo(c, 1.6)
        c.line(x + tw / 2 - 9, ybase + 36, x + tw / 2 + 9, ybase + 36)
        c.line(x + tw / 2, ybase + 46, x + tw / 2, ybase + 20)
    trazo(c, 2.2)
    for gx in range(int(x0) - 20, int(x0 + 8 * tw + 7 * tg) + 20, 22):
        c.line(gx, ybase - 4, gx + 5, ybase + 6)
        c.line(gx + 5, ybase + 6, gx + 10, ybase - 4)
    d.fantasma(c, 52, 408, 0.36)
    d.fantasma(c, 792, 418, 0.34, expr='x')
    d.carbassa(c, 70, 90, 0.55)
    d.carbassa(c, 770, 94, 0.5)
    globus(c, 160, 62, 262, "Toca-les de dreta a esquerra i els fantasmes se'n van volant!", 13)
    mussol(c, 560, 96, 0.34, color=False, bruixa=True)
    peu(c, 1)
    c.showPage()


# ------------------------------------------------------------------ fitxes de cançó (mà dreta)
def fitxa_canco(c, num, titol, dibuix, lletra, aplaudeix, compassos, dits, notes_leg, tip,
                extra=None, escala_text=None):
    capcalera(c, titol, size=40, y0=528 if len(titol) == 1 else 520)
    d.murcielago(c, 770, 540, 0.45)
    d.luna(c, 80, 532, 22)
    d.telarana(c, 22, 574, 64)
    estrella(c, 180, 560, 9)
    estrella(c, 650, 556, 8, 0.4)
    dibuix(c)
    # 1 · CANTA
    caja(c, 292, 372, 400, 104, r=12, lw=2.0)
    etiqueta(c, 306, 452, 1, 'CANTA', 17)
    yy = 420
    for ln in lletra:
        texto(c, 498, yy, ln, 22, HA, 'c')
        yy -= 29
    # 2 · APLAUDEIX
    caja(c, 292, 326, 400, 38, r=10, lw=1.6, dash=(3, 2))
    etiqueta(c, 304, 338, 2, 'APLAUDEIX', 14)
    texto(c, 450, 338, aplaudeix, 13, HA)
    # mussol
    d.fantasma(c, 752, 410, 0.62)
    if extra:
        extra(c)
    # 3 · TOCA
    etiqueta(c, 44, 322, 3, 'TOCA', 17)
    gap = 11.0
    ytop = 300
    yb, centres = pauta_cancio(c, 44, ytop, 506, compassos, 'treble', gap)
    texto(c, 560, 276, 'Mà dreta · posició de LA', 14.5, HA)
    dd = {}
    for (_, _, pitch, dit) in centres:
        dd[pitch] = dit
    teclat_mini(c, 562, 190, 236, 72, 'G4', 8, dd)
    texto(c, 44, 178, 'Pinta cada nota del color del seu nom:', 14.5, HA)
    llegenda(c, 44, 122, notes_leg, w=92, h=44, gap=10)
    globus(c, 440, 56, 262, tip, 12.5, cua='dre')
    mussol(c, 752, 100, 0.38, color=False, bruixa=True)
    peu(c, num)
    c.showPage()


def dib_bruixa(c):
    d.bruja(c, 150, 400, 1.0)
    d.estrellitas(c, [(60, 372, 1.0), (250, 480, 0.9)])


def fitxa_bruixa(c):
    comp = [
        [('A4', 1, 'Bru', 1), ('A4', 1, 'xa', 1), ('C5', 1, 'bru', 3), ('C5', 1, 'xa', 3)],
        [('E5', 1, 'vo', 5), ('E5', 1, 'la', 5), ('D5', 1, 'vo', 4), ('D5', 1, 'la', 4)],
        [('C5', 1, 'vo', 3), ('C5', 1, 'la', 3), ('B4', 1, 'vo', 2), ('B4', 1, 'la', 2)],
        [('C5', 1, 'sen', 3), ('B4', 1, 'se', 2), ('A4', 2, 'por!', 1)],
    ]
    fitxa_canco(c, 2, ['LA BRUIXA VOLA'], dib_bruixa,
                ['Bruixa, bruixa, vola, vola,', 'vola, vola, sense por!'],
                'una palma per cada síl·laba',
                comp, None, ['LA', 'SI', 'DO', 'RE', 'MI'],
                "Els dits van 1-2-3-4-5, com si pugessis una escala. L'últim LA dura dos temps!")


# ------------------------------------------------------------------ fitxa 3: carbassa per notes
MOSAIC = [
    "..g.......vv.bb.",
    ".l.l.....vv.bbbb",
    "..l.....vv..bbb.",
    "....oooooooo....",
    "...oooooooooo...",
    "..oooggoooggooo.",
    "..ooggggoggggoo.",
    "..ooooooggooooo.",
    "..oggggggggggoo.",
    "...oogoggogoooo.",
    "....oooooooooo..",
    "vvvvvvvvvvvvvvvv",
]
MOS_NOTA = {'.': 'SOL', 'o': 'RE', 'g': 'MI', 'v': 'FA', 'l': 'LA', 'b': 'SI'}


def fitxa_carbassa(c):
    capcalera(c, ['CARBASSA PER NOTES'], size=36, y0=534)
    d.telarana(c, 22, 574, 56)
    d.murcielago(c, 790, 548, 0.4)
    cs = 27
    gx, gy = 40, 505
    assert all(len(r) == 16 for r in MOSAIC), [len(r) for r in MOSAIC]
    trazo(c, 1.4, cap=0)
    for r, fila in enumerate(MOSAIC):
        for k, ch in enumerate(fila):
            x, y = gx + k * cs, gy - (r + 1) * cs
            c.setFillColor(white)
            c.rect(x, y, cs, cs, stroke=1, fill=1)
            texto(c, x + cs / 2, y + 9.5, MOS_NOTA[ch], 8.6, HA, 'c')
    trazo(c, 2.6)
    c.setFillColor(white)
    c.rect(gx, gy - 12 * cs, 16 * cs, 12 * cs, stroke=1, fill=0)
    # panell dret
    etiqueta(c, 500, 478, 1, 'PINTA PER NOTES', 17)
    for i, (nm, col) in enumerate((('SOL', 'BLAU'), ('RE', 'TARONJA'), ('MI', 'GROC'),
                                   ('FA', 'VERD'), ('LA', 'MORAT'), ('SI', 'GRIS'))):
        y = 436 - i * 34
        caja(c, 502, y - 6, 34, 26, r=6, lw=1.8)
        texto(c, 548, y, '%s = %s' % (nm, col), 17, HA)
    etiqueta(c, 500, 232, 2, 'TOCA', 17)
    par_h(c, 534, 208, 'Toca al piano els sis colors: RE MI FA SOL LA SI. Quin so fan, de més greu a més agut?',
          13.5, 262, 16)
    etiqueta(c, 500, 138, 3, 'CONTA', 17)
    par_h(c, 534, 114, 'Quantes caselles de RE hi ha a la carbassa?', 13.5, 262, 16)
    caja(c, 534, 62, 70, 28, r=8, lw=1.6, dash=(3, 2))
    d.carbassa(c, 70, 100, 0.5)
    mussol(c, 160, 98, 0.36, color=False, bruixa=True)
    globus(c, 214, 62, 248, "Pista: les caselles de RE formen el cos de la carbassa!", 12.5, cua='esq')
    peu(c, 3)
    c.showPage()


# ------------------------------------------------------------------ fitxa 4: el fantasma Bu!
def dib_fantasma(c):
    d.fantasma(c, 150, 415, 1.3)
    d.estrellitas(c, [(50, 470, 1.0), (265, 330, 0.8), (260, 480, 0.9)])


def fitxa_fantasma(c):
    comp = [
        [('A4', 1, 'Fan', 1), ('A4', 1, 'tas', 1), ('A4', 1, 'ma', 1), (None, 1, 'xt!', None)],
        [('C5', 1, 'Fan', 3), ('C5', 1, 'tas', 3), ('C5', 1, 'ma', 3), (None, 1, 'xt!', None)],
        [('E5', 1, 'Fan', 5), ('E5', 1, 'tas', 5), ('E5', 1, 'ma', 5), (None, 1, 'xt!', None)],
        [('E5', 2, 'BU!', 5), ('A4', 2, 'uuu...', 1)],
    ]
    fitxa_canco(c, 4, ['EL FANTASMA BUUU'], dib_fantasma,
                ['Fantasma, fantasma, fantasma...', 'BUUUUU!'],
                'les notes sí, els silencis «xt!»',
                comp, None, ['LA', 'DO', 'MI'],
                "Cada fantasma és més agut que l'anterior. I l'últim, BU!, el cantes ben fort!")


# ------------------------------------------------------------------ fitxa 5: l'esquelet balla
def fitxa_esquelet(c):
    capcalera(c, ["L'ESQUELET BALLA"], size=40, y0=528)
    d.murcielago(c, 770, 540, 0.45)
    d.luna(c, 80, 532, 22)
    d.telarana(c, 22, 574, 64)
    estrella(c, 190, 556, 9)
    d.esqueleto(c, 112, 420, 0.7, baile=1)
    d.estrellitas(c, [(250, 470, 0.9), (50, 335, 0.9)])
    caja(c, 292, 372, 400, 104, r=12, lw=2.0)
    etiqueta(c, 306, 452, 1, 'CANTA', 17)
    texto(c, 498, 420, 'Cap, espatlles, genolls i peus,', 21, HA, 'c')
    texto(c, 498, 391, 'ossos, ossos, a ballar!', 21, HA, 'c')
    caja(c, 292, 332, 400, 32, r=10, lw=1.6, dash=(3, 2))
    etiqueta(c, 304, 341, 2, 'MOU-TE', 14)
    texto(c, 420, 341, 'toca-et cada os mentre el cantes', 14, HA)
    d.fantasma(c, 752, 410, 0.62)
    etiqueta(c, 44, 326, 3, 'TOCA', 17)
    texto(c, 134, 326, 'dues mans', 13.5, HA)
    gap = 11.0
    comp_d = [
        [('E5', 1, 'Cap', 5), ('D5', 1, 'es', 4), ('C5', 1, 'pat', 3), ('B4', 1, 'lles', 2)],
        [('A4', 1, 'ge', 1), ('B4', 1, 'nolls', 2), ('C5', 1, 'i', 3), ('A4', 1, 'peus', 1)],
        [('C5', 1, 'os', 3), ('C5', 1, 'sos', 3), ('E5', 1, 'os', 5), ('E5', 1, 'sos', 5)],
        [('D5', 1, 'a', 4), ('B4', 1, 'ba', 2), ('A4', 2, 'llar!', 1)],
    ]
    comp_e = [
        [('A2', 4, '', 5)], [('A2', 4, '', 5)], [('E3', 4, '', 1)], [('A2', 4, '', 5)],
    ]
    yb1, _ = pauta_cancio(c, 44, 296, 506, comp_d, 'treble', gap)
    yb2, cen = pauta_cancio(c, 44, 200, 506, comp_e, 'bass', gap, lletra=False, dits=False)
    trazo(c, 2.0, cap=0)
    c.line(44, 296, 44, yb2)
    for (cx, ny, pitch, dit) in cen:
        texto(c, cx, yb2 - 20, str(dit), 13, HA, 'c')
    texto(c, 566, 270, 'Mà dreta: LA = dit 1', 14, HA)
    texto(c, 566, 246, 'Mà esquerra:', 14, HA)
    texto(c, 566, 228, 'LA greu = dit 5', 14, HA)
    texto(c, 566, 210, 'MI = dit 1', 14, HA)
    texto(c, 566, 192, 'aguanta quatre temps', 12.5, HA)
    texto(c, 44, 112, 'Pinta cada nota del color del seu nom:', 14.5, HA)
    llegenda(c, 44, 58, ['LA', 'SI', 'DO', 'RE', 'MI'], w=92, h=44, gap=10)
    globus(c, 566, 138, 232, "La mà esquerra fa «tum-tum» llarg, com el cor de l'esquelet!", 12.5, cua='dre')
    mussol(c, 760, 76, 0.28, color=False, bruixa=True)
    peu(c, 5)
    c.showPage()


# ------------------------------------------------------------------ fitxa 6: jocs i diploma
def fitxa_jocs(c):
    from nens_jocs import sopa, laberint
    capcalera(c, ['LA CASA EMBRUIXADA'], size=36, y0=534)
    d.murcielago(c, 790, 548, 0.4)
    d.telarana(c, 22, 574, 56)
    # laberint
    etiqueta(c, 40, 482, 1, 'LABERINT', 17)
    laberint(c, 40, 456, 11, 10, 24, seed=7, lw=2.0)
    texto(c, 40, 460, 'ENTRADA', 10.5, HA)
    texto(c, 40, 180, 'ajuda la bruixa a arribar a casa', 13, HA)
    d.casa(c, 292, 178, 0.34)
    texto(c, 212, 208, 'SORTIDA', 10.5, HA)
    # sopa de lletres
    etiqueta(c, 340, 482, 2, 'SOPA DE LLETRES', 17)
    paraules = ['BRUIXA', 'FANTASMA', 'CARBASSA', 'ESQUELET', 'ARANYA']
    g = sopa(paraules, n=9, seed=4, pool='AEIOUCMNRSTLBQXFD')
    cs = 24
    gx, gy = 344, 456
    trazo(c, 1.6)
    c.setFillColor(white)
    c.roundRect(gx - 4, gy - 9 * cs - 4, 9 * cs + 8, 9 * cs + 8, 6, stroke=1, fill=1)
    for r in range(9):
        for k in range(9):
            texto(c, gx + k * cs + cs / 2, gy - r * cs - cs + 7, g[r][k], 17, HA, 'c')
    texto(c, 344, 224, 'Busca:', 14.5, HA)
    for i, w_ in enumerate(paraules):
        texto(c, 344 + (i % 2) * 110, 202 - (i // 2) * 22, w_, 15, HA)
    # diploma
    caja(c, 586, 120, 230, 356, r=16, lw=3.0)
    caja(c, 594, 128, 214, 340, r=12, lw=1.2, fill=False, dash=(2, 3))
    c.saveState()
    c.translate(701, 430)
    c.rotate(-2)
    letras_huecas(c, 0, 0, 'DIPLOMA', 28, semilla=2)
    c.restoreState()
    texto(c, 701, 394, 'de monstre pianista', 17, HA, 'c')
    estrella(c, 614, 440, 10)
    estrella(c, 790, 440, 10, 0.3)
    texto(c, 701, 364, 'Aquest diploma és per a', 13.5, HA, 'c')
    trazo(c, 1.4, cap=0)
    c.setDash(1, 3)
    c.line(612, 338, 790, 338)
    c.setDash()
    par_h(c, 701, 310, "perquè ha cantat i tocat les tres cançons de la nit de Halloween!", 13.5, 180, 16, 'c')
    d.fantasma(c, 640, 215, 0.42)
    d.carbassa(c, 765, 212, 0.38)
    mussol(c, 701, 184, 0.26, color=False, bruixa=True)
    texto(c, 701, 136, 'Signat: Mussol Misol', 12.5, HA, 'c')
    d.carbassa(c, 100, 120, 0.5)
    d.calavera(c, 190, 118, 0.5)
    globus(c, 250, 56, 270, "Has acabat! Ara toca ensenyar les tres cançons a casa!", 12.5, cua='dre')
    peu(c, 6)
    c.showPage()


def portada(c):
    marco(c)
    c.saveState()
    c.translate(W / 2, 505)
    c.rotate(1.0)
    letras_huecas(c, 0, 18, 'NIT DE MONSTRES', 46, semilla=4)
    letras_huecas(c, 0, -34, 'PIANISTES', 46, semilla=8)
    c.restoreState()
    d.telarana(c, 22, 574, 90)
    d.telarana(c, W - 22, 574, 90, esquina=1)
    d.luna(c, 110, 470, 34)
    d.murcielago(c, 730, 430, 0.7)
    d.murcielago(c, 790, 548, 0.4)
    estrella(c, 110, 545, 12)
    estrella(c, 700, 545, 10, 0.3)
    mussol(c, 160, 190, 1.0, color=False, bruixa=True)
    d.carbassa(c, 700, 150, 0.9)
    d.fantasma(c, 560, 140, 0.8)
    caja(c, 270, 90, 240, 250, r=14, lw=2.2)
    texto(c, 390, 318, 'Sis fitxes per', 17, HA, 'c')
    texto(c, 390, 296, 'pintar, cantar i tocar', 17, HA, 'c')
    for i, t in enumerate(["1 · El cementiri de les notes", "2 · La bruixa vola", "3 · Carbassa per notes",
                           "4 · El fantasma Buuu", "5 · L'esquelet balla", "6 · La casa embruixada"]):
        texto(c, 288, 262 - i * 24, t, 14.5, HA)
    texto(c, W / 2, 56, 'Per a nens i nenes de 6 a 10 anys · Amb en Mussol Misol · T-Clas', 13, HA, 'c')
    texto(c, 44, 32, 'Nom:', 15, HA)
    trazo(c, 1.2, cap=0)
    c.setDash(1, 3)
    c.line(84, 30, 270, 30)
    c.setDash()
    c.showPage()


def main(solo=None):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    c = ManoCanvas(OUT, pagesize=(W, H), seed=13)
    if not solo or 0 in solo:
        portada(c)
    for n, f in enumerate([fitxa_cementiri, fitxa_bruixa, fitxa_carbassa, fitxa_fantasma, fitxa_esquelet, fitxa_jocs], 1):
        if solo and n not in solo:
            continue
        f(c)
    c.save()
    print(OUT)


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or None)
