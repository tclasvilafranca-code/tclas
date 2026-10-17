# -*- coding: utf-8 -*-
"""Mostra del Quadern del Pianista · PEKES (estil TCLAS adaptat a nens, en català).

   3 pàgines:
     1  Tema 8 · Do, Re i Mi — TEORIA, a color (les notes i els seus colors)
     2  Tema 8 · Do, Re i Mi — JOCS, en blanc i negre (pinta, sopa de lletres, crucigrama…)
     3  Tema 15 · La corxera — TEORIA, en blanc i negre

   Es genera amb:  python3 nens_prova.py  ->  ../output/Prova_Pekes_TCLAS.pdf
"""
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from reportlab.lib.colors import HexColor, white               # noqa: E402

from nens_tclas import *                                       # noqa: F401,F403,E402
from nens_tclas import (caixa_t, W, H, M, CW, NAVY, NAVY_SOFT, CREMA, WARM, RULE, INK, MUTED, OCRE, COL,   # noqa: E402
                        COLNOM, SANS, SANSB, SERIFB, Y, txt, par, alt_par, trac, rr, pagina, mapa,
                        caixa, guia, quadrat, bloc, etiqueta_sec, teclat, pauta, cap, nota, caseta, ma,
                        xip, figura, ManoCanvas)
import notation as nt                                           # noqa: E402

OUT = os.path.join(HERE, '..', 'output', 'Prova_Pekes_TCLAS.pdf')


# ======================================================================== pàg. 1 · teoria a color
def fitxa_nota(c, x, yt, w, h, nom, alt_d, alt_e, dit_d, dit_e, pos_tecla, peu_tecla, pent_peu):
    hexc = HexColor(COL[nom])
    rr(c, x, yt - h, w, h, 5, fill=white, lw=1.0, col=NAVY)
    rr(c, x, yt - 46, w, 46, 5, fill=hexc, lw=1.0, col=NAVY)
    c.setFillColor(hexc)
    c.rect(x + 1, yt - 46, w - 2, 12, stroke=0, fill=1)
    ink = INK if nom == 'MI' else white
    txt(c, x + w / 2, yt - 30, nom, 27, SERIFB, ink, 'c')
    txt(c, x + w / 2, yt - 41, COLNOM[nom].upper(), 6.8, SANSB, ink, 'c')
    # al teclat
    etiqueta_sec(c, x + 10, yt - 62, 'AL TECLAT')
    teclat(c, x + 10, yt - 116, w - 20, 44, nb=5, resalta={pos_tecla: nom}, noms='resalta', color=True)
    par(c, x + 10, yt - 127, peu_tecla, 8, w - 20, 10, SANS, NAVY_SOFT)
    # al pentagrama
    etiqueta_sec(c, x + 10, yt - 158, 'AL PENTAGRAMA')
    gap = 6.2
    txt(c, x + 10, yt - 172, 'MÀ DRETA · clau de sol', 6.6, SANS, MUTED)
    yb = pauta(c, x + 10, yt - 180, w - 20, gap, 'treble', final=False)
    nota(c, x, yb, gap, alt_d, x + w - 36, 'w', hexc)
    txt(c, x + 10, yt - 216, 'MÀ ESQUERRA · clau de fa', 6.6, SANS, MUTED)
    yb2 = pauta(c, x + 10, yt - 224, w - 20, gap, 'bass', final=False)
    cap(c, x + w - 36, nt.note_y(yb2, gap, alt_e, 'bass'), gap, 'w', hexc)
    par(c, x + 10, yt - 262, pent_peu, 8, w - 20, 10, SANS, NAVY_SOFT)
    # dits
    yy = yt - h + 9
    xip(c, x + 10, yy, 70, 'dreta · dit %d' % dit_d, WARM, INK, 17, 7.4)
    xip(c, x + w - 80, yy, 70, 'esq. · dit %d' % dit_e, WARM, INK, 17, 7.4)


def pag1(c):
    pagina(c, 'PEKES  ·  CAPÍTOL 3  ·  LES NOTES I ELS SEUS COLORS', 'Do, Re i Mi', 'Tema 8  ·  teoria',
           'Les nostres tres primeres notes. Viuen juntes al piano i juntes al pentagrama, com tres esglaons.', 45)
    mapa(c, Y(122), ['DO · RE · MI', 'FA · SOL', 'LA · SI', 'LES 7 NOTES'], 0)
    guia(c, M, Y(140), CW,
         'Hola! Avui coneixerem tres amigues que sempre van juntes: el Do, el Re i el Mi. Cada una té el seu color, '
         'la seva tecla i la seva casa al pentagrama.', color=True, size=10, h=80)
    cw = (CW - 24) / 3.0
    yt = Y(232)
    fitxa_nota(c, M, yt, cw, 304, 'DO', 'C4', 'C3', 1, 3, 0, 'La blanca de l’esquerra de les DUES tecles negres.',
               'El Do de la dreta, just sota el pentagrama: té una ratlleta.')
    fitxa_nota(c, M + cw + 12, yt, cw, 304, 'RE', 'D4', 'D3', 2, 2, 1, 'La blanca del mig, entre les dues tecles negres.',
               'Penja just sota de la primera línia, sense ratlleta.')
    fitxa_nota(c, M + 2 * (cw + 12), yt, cw, 304, 'MI', 'E4', 'E3', 3, 1, 2, 'La blanca de la dreta de les dues tecles negres.',
               'Viu a la primera línia del pentagrama.')

    # pugen com esglaons
    y0 = Y(554)
    etiqueta_sec(c, M, y0, 'PUGEN COM ESGLAONS')
    base = y0 - 84
    for k, nom in enumerate(('DO', 'RE', 'MI')):
        hh = 26 + k * 20
        bx = M + 4 + k * 64
        rr(c, bx, base, 64, hh, 2, fill=HexColor(COL[nom]), lw=1.0, col=NAVY)
        txt(c, bx + 32, base + 8, nom, 11, SERIFB, INK if nom == 'MI' else white, 'c')
    txt(c, M + 4, base - 13, '← més GREU', 8.2, SANSB, NAVY_SOFT)
    txt(c, M + 196, base - 13, 'més AGUT →', 8.2, SANSB, NAVY_SOFT, 'r')
    caixa_t(c, M + 214, y0 + 4, CW - 214, 100, 'SABIES QUE?',
            'Els noms Do, Re i Mi vénen d’una cançó de fa més de mil anys: cada nota començava una síl·laba d’una '
            'frase en llatí. I al principi el Do no es deia Do, sinó «Ut»!', 9)

    caixa_t(c, M, Y(660), CW, 50, 'RECORDA',
            'El Do sempre és a l’esquerra de les dues tecles negres juntes. Si trobes el Do, el Re i el Mi són just al costat!', 9.6)
    caixa_t(c, M, Y(722), CW, 50, 'ESCOLTO',
            'Toca el DO, el RE i el MI un darrere l’altre: sents com el so puja? Ara toca MI, RE, DO: ara baixa!', 9.6)
    c.showPage()


# ======================================================================== pàg. 2 · jocs
GRAELLA = None


def sopa():
    g = [[None] * 8 for _ in range(8)]

    def posa(par_, r, k, dr, dk):
        for i, ch in enumerate(par_):
            assert g[r + i * dr][k + i * dk] in (None, ch), par_
            g[r + i * dr][k + i * dk] = ch
    posa('PIANO', 0, 0, 0, 1)
    posa('TECLA', 3, 0, 0, 1)
    posa('COLOR', 0, 7, 1, 0)
    posa('NOTA', 4, 0, 1, 0)
    posa('DO', 5, 1, 0, 1)
    posa('RE', 5, 4, 1, 0)
    posa('MI', 7, 5, 0, 1)
    rnd = random.Random(12)
    for r in range(8):
        for k in range(8):
            if g[r][k] is None:
                g[r][k] = rnd.choice('AEIOTRNLCSMPD')
    return g


def pag2(c):
    pagina(c, 'PEKES  ·  CAPÍTOL 3  ·  LES NOTES I ELS SEUS COLORS', 'Do, Re i Mi · a jugar!', 'Tema 8  ·  jocs',
           'Fes-ho sense pressa i amb ganes de passar-t’ho bé. Cada joc fa servir el que acabes d’aprendre.', 46)
    # 1 · pinta
    y = Y(122)
    bloc(c, y, 1, 'Pinta i troba', 'Tria un color per a cada nota i pinta totes les seves tecles.')
    teclat(c, M + 25, y - 82, 330, 54, nb=14)
    for k, nm in enumerate(('DO', 'RE', 'MI')):
        cx = M + 395 + (k % 3) * 0
        yy = y - 30 - k * 24
        rr(c, M + 392, yy - 8, 20, 20, 10, fill=white, lw=1.2, col=NAVY)
        txt(c, M + 420, yy - 2, nm, 11, SERIFB, INK)
    # 2 · sopa de lletres
    y = Y(240)
    bloc(c, y, 2, 'Sopa de lletres', 'Troba aquestes paraules (→ i ↓).', x=M)
    g = sopa()
    cs = 19.5
    gx, gy = M + 4, y - 26
    trac(c, 0.8, NAVY_SOFT)
    c.setFillColor(white)
    c.roundRect(gx - 4, gy - 8 * cs - 4, 8 * cs + 8, 8 * cs + 8, 4, stroke=1, fill=1)
    for r in range(8):
        for k in range(8):
            txt(c, gx + k * cs + cs / 2, gy - r * cs - cs + 5.5, g[r][k], 11, SANSB, INK, 'c')
    paraules = ['PIANO', 'TECLA', 'COLOR', 'NOTA', 'DO', 'RE', 'MI']
    for i, p in enumerate(paraules):
        yy = y - 40 - (i // 2) * 18
        xx = M + 190 + (i % 2) * 58 if False else M + 175
    for i, p in enumerate(paraules):
        yy = y - 36 - i * 17
        rr(c, M + 182, yy - 2, 10, 10, 2, fill=white, lw=0.9, col=NAVY_SOFT)
        txt(c, M + 198, yy, p, 9.4, SANSB, INK)
    # 3 · crucigrama
    x3 = M + 262
    bloc(c, y, 3, 'Crucigrama', 'Escriu una lletra a cada quadret.', x=x3)
    cells = {}
    for i, ch in enumerate('NOTA'):
        cells[(i, 0)] = ch
    for i, ch in enumerate('TECLA'):
        cells[(2, i)] = ch
    for i, ch in enumerate('COLOR'):
        cells[(2 + i, 2)] = ch
    for i, ch in enumerate('AGUT'):
        cells[(2 + i, 4)] = ch
    ns = {(0, 0): 1, (2, 0): 2, (2, 2): 3, (2, 4): 4}
    cs2 = 19
    cx0, cy0 = x3 + 4, y - 28
    for (r, k) in cells:
        rr(c, cx0 + k * cs2, cy0 - (r + 1) * cs2, cs2, cs2, 0, fill=white, lw=1.0, col=NAVY)
        if (r, k) in ns:
            txt(c, cx0 + k * cs2 + 2, cy0 - r * cs2 - 8, str(ns[(r, k)]), 6.2, SANSB, OCRE)
    pistes = ['1 ↓  Cada una de les set amigues: Do, Re, Mi…', '2 →  El que premem amb el dit al piano.',
              '3 ↓  Cada nota té el seu…  (el vermell, el taronja…)', '4 ↓  El contrari de GREU.']
    yy = y - 28 - 7 * cs2 - 14 + 0
    yy = cy0 - 7 * cs2 - 14
    for p in pistes:
        yy = par(c, x3 + 2, yy, p, 8.2, 250, 10.5, SANS, INK) - 3

    # 4 · uneix
    y = Y(498)
    bloc(c, y, 4, 'Uneix amb una línia', 'Cada nom amb la seva nota.', x=M)
    ordre = ['MI', 'DO', 'RE']
    alts = {'DO': 'C4', 'RE': 'D4', 'MI': 'E4'}
    for k, nm in enumerate(('DO', 'RE', 'MI')):
        yy = y - 44 - k * 34
        rr(c, M + 4, yy - 8, 58, 22, 11, fill=white, lw=1.0, col=NAVY)
        txt(c, M + 33, yy - 1, nm, 11, SERIFB, INK, 'c')
        c.setFillColor(NAVY)
        c.circle(M + 74, yy + 3, 3, stroke=0, fill=1)
    for k, nm in enumerate(ordre):
        yy = y - 44 - k * 34
        yb = pauta(c, M + 150, yy + 12, 90, 5, 'treble', final=False)
        nota(c, M + 150, yb, 5, alts[nm], M + 214, 'w', white)
        c.setFillColor(NAVY)
        c.circle(M + 140, yy + 2, 3, stroke=0, fill=1)
    # 5 · dibuixa
    x5 = M + 262
    bloc(c, y, 5, 'Dibuixa les notes', 'Posa cada nota a la seva casa.', x=x5)
    for k, (clau, txtc) in enumerate((('treble', 'clau de sol'), ('bass', 'clau de fa'))):
        yy = y - 46 - k * 54
        txt(c, x5 + 4, yy + 6, txtc, 6.8, SANS, MUTED)
        yb = pauta(c, x5 + 4, yy - 4, 240, 5.6, clau, final=True)
        for j, nm in enumerate(('DO', 'RE', 'MI')):
            xx = x5 + 80 + j * 52
            caseta(c, xx - 12, yb - 22, 24, 15, 3)
            txt(c, xx, yb - 18, nm, 7.2, SANSB, MUTED, 'c')
    # 6 · l'error
    y = Y(684)
    bloc(c, y, 6, 'En Mussol s’ha equivocat!', 'Un nom està mal posat. Encercla’l i escriu el bo.', x=M)
    yb = pauta(c, M + 4, y - 36, 250, 6, 'treble', final=True)
    for j, (alt, nom) in enumerate((('C4', 'DO'), ('D4', 'MI'), ('E4', 'MI'))):
        xx = M + 90 + j * 52
        nota(c, M, yb, 6, alt, xx, 'w', white)
        txt(c, xx, yb - 26, nom, 9.5, SANSB, INK, 'c')
    mussol(c, M + 292, y - 34, 0.28, color=False, lw=2.2)
    # el joc de la profe
    caixa_t(c, M + 336, y + 14, CW - 336, 108, 'JOC AMB LA PROFE · EL SEMÀFOR MUSICAL',
            'Tres targetes grans: DO vermella, RE taronja i MI groga. Posa-les a terra. La profe toca una nota i tu '
            'corres a trepitjar la targeta que toca!', 8.6)
    c.showPage()


# ======================================================================== pàg. 3 · la corxera (BN)
def pag3(c):
    pagina(c, 'PEKES  ·  CAPÍTOL 4  ·  EL RITME', 'La corxera', 'Tema 15  ·  teoria',
           'Fins ara hem comptat notes que duren 4, 2 i 1 temps. Avui arriba la més ràpida: la corxera!', 75)
    mapa(c, Y(122), ['EL POLS', 'RODONA · BLANCA · NEGRA', 'LA CORXERA', 'ELS TEMPS', 'EL COMPÀS'], 2)
    guia(c, M, Y(140), CW,
         'Dues corxeres juntes tarden el mateix que una sola negra. Per això són tan ràpides: en caben moltes en un compàs!',
         color=False, size=10, h=80)

    # com es veu
    y = Y(246)
    etiqueta_sec(c, M, y, 'COM ES VEU')
    rr(c, M, y - 124, 247, 112, 5, fill=white, lw=1.0)
    figura(c, 'e', M + 62, y - 80, 9)
    txt(c, M + 62, y - 104, 'SOLA', 8, SANSB, NAVY, 'c')
    txt(c, M + 62, y - 114, 'amb banderola', 7.4, SANS, MUTED, 'c')
    figura(c, 'ee', M + 140, y - 80, 9)
    txt(c, M + 164, y - 104, 'JUNTES', 8, SANSB, NAVY, 'c')
    txt(c, M + 164, y - 114, 'amb barra', 7.4, SANS, MUTED, 'c')
    # quant dura
    x2 = M + 262
    etiqueta_sec(c, x2, y, 'QUANT DURA?')
    rr(c, x2, y - 124, CW - 262, 112, 5, fill=white, lw=1.0)
    files = [('RODONA', 1), ('BLANCA', 2), ('NEGRA', 4), ('CORXERA', 8)]
    for k, (nm, n) in enumerate(files):
        yy = y - 30 - k * 22
        txt(c, x2 + 8, yy - 2, nm, 7, SANSB, NAVY)
        bw = (CW - 262 - 80) / float(n)
        for j in range(n):
            rr(c, x2 + 66 + j * bw, yy - 8, bw - 2, 16, 2, fill=WARM, lw=0.8, col=NAVY_SOFT)
            if n <= 4:
                c.setFillColor(NAVY)
                c.circle(x2 + 66 + j * bw + (bw - 2) / 2, yy, 2.6, stroke=0, fill=1)
    txt(c, x2 + 8, y - 117, 'Cada fila omple els mateixos 4 temps.', 7.2, SANS, MUTED)

    # com es diu
    y = Y(392)
    etiqueta_sec(c, M, y, 'COM ES DIU: TA I TI-TI')
    rr(c, M, y - 100, CW, 90, 5, fill=white, lw=1.0)
    ritme = [('q', 'ta', 40), ('q', 'ta', 140), ('ee', 'ti-ti', 240), ('q', 'ta', 360)]
    for fg, sil, xx in ritme:
        figura(c, fg, M + xx, y - 52, 8)
        txt(c, M + xx + (14 if fg == 'ee' else 0), y - 88, sil, 12, SERIFB, NAVY, 'c')
    txt(c, M + CW - 12, y - 30, 'diguem-ho i piquem de mans!', 8, SANS, MUTED, 'r')

    # compta
    y = Y(506)
    etiqueta_sec(c, M, y, 'COMPTA AMB LES MANS')
    rr(c, M, y - 96, CW, 86, 5, fill=white, lw=1.0)
    for k in range(4):
        bx = M + 14 + k * 125
        rr(c, bx, y - 40, 112, 24, 4, fill=WARM, lw=0.8, col=NAVY_SOFT)
        txt(c, bx + 18, y - 33, str(k + 1), 11, SANSB, INK, 'c')
        txt(c, bx + 74, y - 33, 'i', 11, SANS, MUTED, 'c')
    txt(c, M + 14, y - 66, 'Cada número és un temps (una negra). Cada «i» és la segona corxera: «un i, dos i, tres i, quatre i».', 8.6, SANS, INK)
    txt(c, M + 14, y - 80, 'Pica una palma a cada número i una palmeta suau a cada «i».', 8.6, SANS, INK)

    caixa_t(c, M, Y(616), CW, 50, 'RECORDA',
            '2 corxeres = 1 negra  ·  4 corxeres = 1 blanca  ·  8 corxeres = 1 rodona.', 10)
    caixa_t(c, M, Y(674), CW, 62, 'SABIES QUE?',
            'En italià, la corxera es diu «croma» (colorida). Els músics de tot el món fan servir paraules italianes '
            'perquè la música escrita es va fer servir primer a Itàlia.', 9)
    caixa_t(c, M, Y(746), CW, 44, 'ESCOLTO',
            'Aplaudeix una negra i, després, dues corxeres seguides: sents que van el doble de ràpid?', 9.4)
    c.showPage()


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    c = ManoCanvas(OUT, pagesize=(W, H), seed=5, amp=0.0)
    c.setTitle('El Quadern del Pianista · PEKES · mostra')
    for f in (pag1, pag2, pag3):
        f(c)
    c.save()
    print('generat', OUT)


if __name__ == '__main__':
    main()
