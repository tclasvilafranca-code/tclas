# -*- coding: utf-8 -*-
"""Més tipus de joc per al Quadern PEKES: crucigrama de panell, camí de notes, intrús, mosaic i laberint."""
import random

from nens_tclas import (M, CW, NAVY, NAVY_SOFT, WARM, WARM2, OCRE, INK, MUTED, SANS, SANSB, SERIFB, ETQ, txt, par, trac, rr,
                        panell, consigna, white, HexColor, COL, stringWidth)
from nens_jocs import crucigrama, pistes, laberint, linia
import nens_pla as pla

NOTES7 = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']


def p_cruci(c, x, yt, w, h, n, spec, pistes_l, cs=17, titol='CRUCIGRAMA'):
    panell(c, x, yt, w, h, titol, n=n)
    consigna(c, x + 14, yt - 40, 'Una lletra a cada quadret.', w - 28)
    cel = crucigrama(c, x + 12, yt - 54, spec, cs)
    ncol = max(k for (_, k) in cel) + 1
    pistes(c, x + 12 + ncol * cs + 14, yt - 70, w - (ncol * cs + 38), pistes_l, 11, 13.5)


def p_cami(c, x, yt, w, h, n, cami, grid=(4, 4), titol='EL CAMÍ DE LES NOTES', seed=3, consigna_t=None):
    """cami: llista de (fila, col, nom) en ordre; la resta de cel·les s'omplen amb notes que no continuen el camí."""
    panell(c, x, yt, w, h, titol, n=n)
    seq = ' → '.join(t for (_, _, t) in cami)
    consigna(c, x + 14, yt - 40, consigna_t or ('Pinta el camí: ' + seq), w - 28)
    rows, cols = grid
    rnd = random.Random(seed)
    cell = {(r, k): t for (r, k, t) in cami}
    for r in range(rows):
        for k in range(cols):
            if (r, k) not in cell:
                cell[(r, k)] = rnd.choice([t for t in NOTES7 if t != cami[0][2]])
    cw_ = (w - 40) / cols
    ch = min(40, (h - 100) / rows)
    gx, gy = x + 20, yt - 80
    for (r, k), t in cell.items():
        on = any((r, k) == (a, b) for (a, b, _) in cami)
        rr(c, gx + k * cw_ + 2, gy - (r + 1) * ch + 2, cw_ - 4, ch - 4, 8, fill=white, lw=1.5, col=NAVY)
        txt(c, gx + k * cw_ + cw_ / 2, gy - r * ch - ch / 2 - 5, t, 13, SERIFB, NAVY, 'c')
    # inici i final
    a = cami[0]
    z = cami[-1]
    txt(c, gx + a[1] * cw_ + 8, gy - a[0] * ch - 12, '▶', 8, 'DejaVuSans', OCRE) if False else None


def p_intrus(c, x, yt, w, h, n, files, titol='TROBA L’INTRÚS', consigna_t='En cada fila hi ha una cosa que no té res a veure. Encercla-la.'):
    panell(c, x, yt, w, h, titol, n=n)
    consigna(c, x + 14, yt - 40, consigna_t, w - 28)
    for k, items in enumerate(files):
        yy = yt - 92 - k * 34
        iw = (w - 28 - 6 * (len(items) - 1)) / len(items)
        for j, t in enumerate(items):
            rr(c, x + 14 + j * (iw + 6), yy - 12, iw, 26, 13, fill=white, lw=1.4, col=NAVY)
            tam = 11
            while stringWidth(t, SANSB, tam) > iw - 8 and tam > 7:
                tam -= 0.5
            txt(c, x + 14 + j * (iw + 6) + iw / 2, yy - 4, t, tam, SANSB, INK, 'c')


HEART = ['..XX..XX..', '.XXXXXXXX.', 'XXXXXXXXXX', 'XXXXXXXXXX', '.XXXXXXXX.', '..XXXXXX..', '...XXXX...', '....XX....']
HOUSE = ['....XX....', '...XXXX...', '..XXXXXX..', '.XXXXXXXX.', 'XXXXXXXXXX', '.XXXXXXXX.', '.XXXXXXXX.', '.XXXXXXXX.']


def p_mosaic(c, x, yt, w, h, n, mask, titol='PINTA PER NOTES', pag_colors=True):
    panell(c, x, yt, w, h, titol, n=n)
    consigna(c, x + 14, yt - 40, 'Pinta cada quadret del color de la seva nota (mira la pàgina %d).' % pla.TEMES[11]['pag'], w - 28)
    cs = min(17, (w - 28) / len(mask[0]))
    gx, gy = x + (w - cs * len(mask[0])) / 2, yt - 62
    for r, fila in enumerate(mask):
        for k, ch in enumerate(fila):
            if ch == 'X':
                rr(c, gx + k * cs, gy - (r + 1) * cs, cs, cs, 0, fill=white, lw=1.1, col=NAVY)
                txt(c, gx + k * cs + cs / 2, gy - r * cs - cs + 5.2, NOTES7[r % 7], 6.8, SANSB, NAVY_SOFT, 'c')


def p_laberint(c, x, yt, w, h, n, titol='EL LABERINT', consigna_t='Ajuda en Mussol a arribar fins al final.', seed=11):
    panell(c, x, yt, w, h, titol, n=n)
    consigna(c, x + 14, yt - 40, consigna_t, w - 28)
    cs = 20
    cols = int((w - 40) // cs)
    rows = int((h - 76) // cs)
    laberint(c, x + 20, yt - 58, cols, rows, cs, seed=seed, lw=2.0)
