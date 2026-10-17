# -*- coding: utf-8 -*-
"""Mostra del Quadern del Pianista · PEKES (estil TCLAS adaptat a nens, en català) — versió 2.

   3 pàgines:
     1  Tema 8 · Do, Re i Mi — TEORIA, a color (les notes i els seus colors)
     2  Tema 8 · Do, Re i Mi — JOCS, en blanc i negre (pinta, sopa de lletres, crucigrama…)
     3  Tema 15 · La corxera — TEORIA, en blanc i negre

   v2 (per a nens petits): lletra Andika de 11,5-13 pt, panells amb vora i ombra, caixes amb icona,
   en Mussol Misol més gran.

   Es genera amb:  python3 nens_prova.py  ->  ../output/Prova_Pekes_TCLAS.pdf
"""
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from reportlab.lib.colors import HexColor, white               # noqa: E402

from nens_tclas import (W, H, M, CW, NAVY, NAVY_SOFT, CREMA, WARM, WARM2, RULE, SOMBRA, INK, MUTED, OCRE,   # noqa: E402
                        COL, COLNOM, SANS, SANSB, SERIFB, ETQ, Y, txt, par, alt_par, trac, rr, pagina,
                        mapa, panell, caixa_t, franja, guia, consigna, pill_dit, etiqueta_sec, teclat,
                        pauta, cap, nota, caseta, xip, figura, ManoCanvas)
from mussol import mussol                                       # noqa: E402
import notation as nt                                           # noqa: E402

OUT = os.path.join(HERE, '..', 'output', 'Prova_Pekes_TCLAS.pdf')
KICK = 'PEKES  ·  CAPÍTOL 3  ·  LES NOTES I ELS SEUS COLORS'


# ======================================================================== pàg. 1 · teoria a color
def fitxa_nota(c, x, yt, w, h, nom, alt_d, alt_e, dit_d, dit_e, pos_tecla, peu_tecla, pent_peu):
    hexc = HexColor(COL[nom])
    rr(c, x + 3.4, yt - h - 3.4, w, h, 8, fill=SOMBRA, lw=0)
    rr(c, x, yt - h, w, h, 8, fill=white, lw=1.7, col=NAVY)
    # banda de color amb el nom
    rr(c, x, yt - 58, w, 58, 8, fill=hexc, lw=1.7, col=NAVY)
    c.setFillColor(hexc)
    c.rect(x + 1.5, yt - 58, w - 3, 14, stroke=0, fill=1)
    trac(c, 1.7, NAVY)
    c.line(x, yt - 58, x + w, yt - 58)
    ink = INK if nom == 'MI' else white
    txt(c, x + w / 2, yt - 39, nom, 36, SERIFB, ink, 'c')
    txt(c, x + w / 2, yt - 53, COLNOM[nom].upper(), 9.2, ETQ, ink, 'c')
    # al teclat
    etiqueta_sec(c, x + 12, yt - 79, 'AL TECLAT')
    teclat(c, x + 12, yt - 128, w - 24, 40, nb=5, resalta={pos_tecla: nom}, noms='resalta', color=True)
    par(c, x + 12, yt - 147, peu_tecla, 11, w - 24, 13.5, SANS, INK)
    # al pentagrama
    etiqueta_sec(c, x + 12, yt - 192, 'AL PENTAGRAMA')
    gap = 7.2
    txt(c, x + 12, yt - 209, 'mà dreta · clau de sol', 9.6, SANS, MUTED)
    yb = pauta(c, x + 12, yt - 218, w - 24, gap, 'treble', final=False)
    nota(c, x, yb, gap, alt_d, x + w - 40, 'w', hexc)
    txt(c, x + 12, yt - 272, 'mà esquerra · clau de fa', 9.6, SANS, MUTED)
    yb2 = pauta(c, x + 12, yt - 281, w - 24, gap, 'bass', final=False)
    cap(c, x + w - 40, nt.note_y(yb2, gap, alt_e, 'bass'), gap, 'w', hexc)
    par(c, x + 12, yt - 322, pent_peu, 11, w - 24, 13.5, SANS, INK)
    # dits
    yy = yt - h + 11
    hw = (w - 30) / 2.0
    pill_dit(c, x + 10, yy, hw, 'dreta', dit_d)
    pill_dit(c, x + 20 + hw, yy, hw, 'esq.', dit_e)


def pag1(c):
    pagina(c, KICK, 'Do, Re i Mi', 'Tema 8  ·  teoria',
           'Tres notes que sempre van juntes, com tres esglaons d’una escala.', 45)
    mapa(c, Y(124), ['DO · RE · MI', 'FA · SOL', 'LA · SI', 'LES 7 NOTES'], 0)
    guia(c, M, Y(142), CW,
         'Hola! Avui coneixerem tres amigues que sempre van juntes: el Do, el Re i el Mi. Cada una té el seu color, '
         'la seva tecla i la seva casa al pentagrama.', color=True, size=12.5, h=86)
    cw = (CW - 28) / 3.0
    yt = Y(246)
    h = 386
    fitxa_nota(c, M, yt, cw, h, 'DO', 'C4', 'C3', 1, 3, 0, 'La blanca de l’esquerra de les DUES tecles negres.',
               'Just sota el pentagrama, amb una ratlleta.')
    fitxa_nota(c, M + cw + 14, yt, cw, h, 'RE', 'D4', 'D3', 2, 2, 1, 'La blanca del mig, entre les dues tecles negres.',
               'Penja just sota la primera línia, sense ratlleta.')
    fitxa_nota(c, M + 2 * (cw + 14), yt, cw, h, 'MI', 'E4', 'E3', 3, 1, 2, 'La blanca de la dreta de les dues tecles negres.',
               'Viu a la primera línia del pentagrama.')

    # pugen com esglaons
    yt2 = Y(650)
    h2 = 100
    panell(c, M, yt2, 236, h2, 'PUGEN COM ESGLAONS')
    base = yt2 - h2 + 28
    for k, nom in enumerate(('DO', 'RE', 'MI')):
        hh = 16 + k * 14
        bx = M + 14 + k * 69
        rr(c, bx, base, 69, hh, 2, fill=HexColor(COL[nom]), lw=1.5, col=NAVY)
        txt(c, bx + 34.5, base + hh / 2 - 5, nom, 13, SERIFB, INK if nom == 'MI' else white, 'c')
    txt(c, M + 14, base - 17, '← més GREU', 10.5, SANSB, NAVY_SOFT)
    txt(c, M + 14 + 207, base - 17, 'més AGUT →', 10.5, SANSB, NAVY_SOFT, 'r')
    caixa_t(c, M + 236 + 22, yt2, CW - 236 - 22, h2, 'RECORDA',
            'El DO és sempre a l’esquerra de les DUES tecles negres. Troba’l i el RE i el MI són al costat!', 11.5)
    franja(c, M, Y(762), CW, 40, 'ESCOLTO', 'Toca DO, RE, MI: el so puja. Ara MI, RE, DO: baixa!')
    c.showPage()


# ======================================================================== pàg. 2 · jocs
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
    pagina(c, KICK, 'Do, Re i Mi · a jugar!', 'Tema 8  ·  jocs',
           'Agafa els llapis i fes-ho sense pressa. Cada joc fa servir el que acabes d’aprendre.', 46)
    guia(c, M, Y(122), CW, 'Un joc darrere l’altre! Si t’encalles, torna a mirar la pàgina de les notes: allà hi ha les pistes.',
         color=False, size=12.5, h=66)

    # 1 · pinta
    yt = Y(204)
    h = 114
    panell(c, M, yt, CW, h, 'PINTA LES TECLES', n=1)
    consigna(c, M + 14, yt - 40, 'Pinta de vermell les DO, de taronja les RE i de groc les MI.')
    teclat(c, M + 14, yt - 102, 340, 52, nb=14, resalta={0: 'DO'}, noms='resalta', color=False)
    for k, nm in enumerate(('DO', 'RE', 'MI')):
        yy = yt - 56 - k * 22
        rr(c, M + 384, yy - 8, 18, 18, 9, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 410, yy - 3, nm, 13, SERIFB, INK)
        txt(c, M + 442, yy - 3, '= ' + {'DO': 'vermell', 'RE': 'taronja', 'MI': 'groc'}[nm], 11.5, SANS, NAVY_SOFT)

    # 2 · sopa de lletres  /  3 · crucigrama
    pw = (CW - 18) / 2.0
    yt = Y(336)
    h = 224
    panell(c, M, yt, pw, h, 'SOPA DE LLETRES', n=2)
    consigna(c, M + 14, yt - 40, 'Troba les 7 paraules (→ i ↓).', pw - 24)
    g = sopa()
    cs = 20.5
    gx, gy = M + 12, yt - 52
    trac(c, 1.3, NAVY)
    c.setFillColor(white)
    c.roundRect(gx - 3, gy - 8 * cs - 3, 8 * cs + 6, 8 * cs + 6, 4, stroke=1, fill=1)
    for r in range(8):
        for k in range(8):
            txt(c, gx + k * cs + cs / 2, gy - r * cs - cs + 6, g[r][k], 14, SANSB, INK, 'c')
    for i, p in enumerate(['PIANO', 'TECLA', 'COLOR', 'NOTA', 'DO', 'RE', 'MI']):
        txt(c, M + 12 + 8 * cs + 16, gy - 14 - i * 22, p, 12, SANSB, NAVY)

    x3 = M + pw + 18
    panell(c, x3, yt, pw, h, 'CRUCIGRAMA', n=3)
    consigna(c, x3 + 14, yt - 40, 'Una lletra a cada quadret.', pw - 24)
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
    cs2 = 21
    cx0, cy0 = x3 + 12, yt - 52
    for (r, k) in cells:
        rr(c, cx0 + k * cs2, cy0 - (r + 1) * cs2, cs2, cs2, 0, fill=white, lw=1.5, col=NAVY)
        if (r, k) in ns:
            txt(c, cx0 + k * cs2 + 2.5, cy0 - r * cs2 - 9, str(ns[(r, k)]), 8.5, SANSB, OCRE)
    pistes = [('1 ↓', 'El Do és una…'), ('2 →', 'Premem una… del piano.'), ('3 ↓', 'El vermell és un…'),
              ('4 ↓', 'El contrari de GREU.')]
    yy = yt - 66
    for (a, b) in pistes:
        txt(c, x3 + 124, yy, a, 11.5, SANSB, OCRE)
        yy = par(c, x3 + 150, yy, b, 11.5, pw - 150 - 8, 14, SANS, INK) - 14

    # 4 · uneix  /  5 · dibuixa
    yt = Y(578)
    h = 200
    panell(c, M, yt, pw, h, 'UNEIX AMB UNA LÍNIA', n=4)
    consigna(c, M + 14, yt - 40, 'Cada nom amb la seva nota.', pw - 24)
    ordre = ['MI', 'DO', 'RE']
    alts = {'DO': 'C4', 'RE': 'D4', 'MI': 'E4'}
    for k, nm in enumerate(('DO', 'RE', 'MI')):
        yy = yt - 78 - k * 46
        rr(c, M + 14, yy - 9, 58, 28, 14, fill=white, lw=1.5, col=NAVY)
        txt(c, M + 43, yy - 1, nm, 14, SERIFB, INK, 'c')
        c.setFillColor(NAVY)
        c.circle(M + 84, yy + 5, 4, stroke=0, fill=1)
    for k, nm in enumerate(ordre):
        yy = yt - 78 - k * 46
        yb = pauta(c, M + 124, yy + 15, 108, 7, 'treble', final=False)
        nota(c, M + 124, yb, 7, alts[nm], M + 206, 'w', white)
        c.setFillColor(NAVY)
        c.circle(M + 112, yy + 3, 4, stroke=0, fill=1)

    x5 = M + pw + 18
    panell(c, x5, yt, pw, h, 'DIBUIXA LES NOTES', n=5)
    consigna(c, x5 + 14, yt - 40, 'Dibuixa cada nota a la seva casa.', pw - 24)
    for k, (clau, nomc) in enumerate((('treble', 'clau de sol'), ('bass', 'clau de fa'))):
        yy = yt - 70 - k * 60
        txt(c, x5 + 14, yy + 2, nomc, 10, SANS, MUTED)
        yb = pauta(c, x5 + 14, yy - 13, pw - 28, 6.5, clau, final=True)
        for j, nm in enumerate(('DO', 'RE', 'MI')):
            xx = x5 + 112 + j * 52
            caseta(c, xx - 20, yb - 26, 40, 17, 4)
            txt(c, xx, yb - 21.5, nm, 11, SANSB, NAVY_SOFT, 'c')
    c.showPage()


# ======================================================================== pàg. 3 · la corxera (BN)
def pag3(c):
    pagina(c, 'PEKES  ·  CAPÍTOL 4  ·  EL RITME', 'La corxera', 'Tema 15  ·  teoria',
           'Fins ara hem comptat notes que duren 4, 2 i 1 temps. Avui arriba la més ràpida: la corxera!', 75)
    mapa(c, Y(124), ['EL POLS', 'RODONA · BLANCA · NEGRA', 'LA CORXERA', 'ELS TEMPS'], 2)
    guia(c, M, Y(142), CW,
         'Dues corxeres juntes tarden el mateix que una sola negra. Per això són tan ràpides: en caben moltes en un compàs!',
         color=False, size=12.5, h=78)
    pw = (CW - 18) / 2.0

    # com es veu / quant dura
    yt = Y(238)
    h = 140
    panell(c, M, yt, pw, h, 'COM ES VEU')
    figura(c, 'e', M + 56, yt - 80, 11)
    txt(c, M + 56, yt - 108, 'SOLA', 11.5, SANSB, NAVY, 'c')
    txt(c, M + 56, yt - 122, 'amb banderola', 10.5, SANS, MUTED, 'c')
    figura(c, 'ee', M + 140, yt - 80, 11)
    txt(c, M + 180, yt - 108, 'JUNTES', 11.5, SANSB, NAVY, 'c')
    txt(c, M + 180, yt - 122, 'amb barra', 10.5, SANS, MUTED, 'c')
    x2 = M + pw + 18
    panell(c, x2, yt, pw, h, 'QUANT DURA?')
    files = [('RODONA', 1), ('BLANCA', 2), ('NEGRA', 4), ('CORXERA', 8)]
    for k, (nm, n) in enumerate(files):
        yy = yt - 42 - k * 21
        txt(c, x2 + 12, yy - 4, nm, 10.5, SANSB, NAVY)
        bw = (pw - 100) / float(n)
        for j in range(n):
            rr(c, x2 + 84 + j * bw, yy - 10, bw - 2.5, 20, 2, fill=WARM2, lw=1.2, col=NAVY)
            if n <= 4:
                c.setFillColor(NAVY)
                c.circle(x2 + 84 + j * bw + (bw - 2.5) / 2, yy, 3, stroke=0, fill=1)
    txt(c, x2 + 12, yt - h + 10, 'Cada fila omple els mateixos 4 temps.', 9.8, SANS, MUTED)

    # com es diu
    yt = Y(396)
    h = 110
    panell(c, M, yt, CW, h, 'COM ES DIU: TA I TI-TI')
    for fg, sil, xx in [('q', 'ta', 56), ('q', 'ta', 160), ('ee', 'ti-ti', 262), ('q', 'ta', 400)]:
        figura(c, fg, M + xx, yt - 66, 10)
        txt(c, M + xx + (18 if fg == 'ee' else 0), yt - 98, sil, 20, SERIFB, NAVY, 'c')
    txt(c, M + CW - 14, yt - 24, 'Diguem-ho i piquem de mans!', 11.5, SANS, NAVY_SOFT, 'r')

    # compta amb les mans
    yt = Y(524)
    h = 118
    panell(c, M, yt, CW, h, 'COMPTA AMB LES MANS')
    bw = (CW - 28) / 8.0
    for k in range(8):
        bx = M + 14 + k * bw
        num = (k % 2 == 0)
        rr(c, bx, yt - 72, bw - 3, 34, 4, fill=NAVY if num else WARM, lw=1.5, col=NAVY)
        txt(c, bx + (bw - 3) / 2, yt - 62, str(k // 2 + 1) if num else 'i', 19 if num else 17, SANSB if num else SANS,
            white if num else NAVY_SOFT, 'c')
    par(c, M + 14, yt - 90, 'Cada número és un temps. Cada «i» és la segona corxera. Pica una palma a cada número '
        'i una palmeta suau a cada «i».', 11.8, CW - 28, 15.5, SANS, INK)

    # recorda / sabies que
    yt = Y(666)
    h = 112
    caixa_t(c, M, yt, pw, h, 'RECORDA', '', 12.5)
    for k, t in enumerate(['2 corxeres  =  1 negra', '4 corxeres  =  1 blanca', '8 corxeres  =  1 rodona']):
        txt(c, M + 16, yt - 56 - k * 18, t, 13, SANSB, NAVY)
    caixa_t(c, M + pw + 18, yt, pw, h, 'SABIES QUE?',
            'En italià, la corxera es diu «croma», que vol dir colorida!', 12.5)
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
