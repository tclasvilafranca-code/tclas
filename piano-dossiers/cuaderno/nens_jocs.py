# -*- coding: utf-8 -*-
"""Peces reutilitzables dels fulls de JOCS del Quadern PEKES: panell de joc, sopa de lletres,
   crucigrama, unir, veritat/fals, laberint, caselles per dibuixar i línies per escriure."""
import random

from nens_tclas import (M, W, CW, NAVY, NAVY_SOFT, WARM, WARM2, RULE, SOMBRA, INK, MUTED, OCRE, white,
                        SANS, SANSB, SERIFB, ETQ, Y, txt, par, alt_par, trac, rr, panell, consigna,
                        caseta, stringWidth)


class Pila:
    """Reparteix l'alçada d'una pàgina en files de panells."""

    def __init__(self, ytop, ybottom=40 + 16, gap=18):
        self.y, self.fons, self.gap = ytop, ybottom, gap

    def pren(self, h):
        yt = self.y
        self.y -= h + self.gap
        assert yt - h >= self.fons - 1, 'la pàgina no hi cap: queden %.0f pt' % (yt - h - self.fons)
        return yt

    def sobra(self):
        return self.y + self.gap - self.fons


def joc(c, x, yt, w, h, n, titol, text=None):
    """Panell d'un joc amb número i la consigna; retorna la y on comença el contingut."""
    panell(c, x, yt, w, h, titol, n=n)
    y = yt - 40
    if text:
        y = consigna(c, x + 14, y, text, w - 28)
        return y - 6
    return y


def meitats(pw_total=CW, gap=18):
    pw = (pw_total - gap) / 2.0
    return pw, M + pw + gap


# ------------------------------------------------------------------ sopa de lletres
def sopa(paraules, n=8, seed=3, pool='AEIOTRNLCSMPD'):
    rnd = random.Random(seed)
    for intent in range(400):
        g = [[None] * n for _ in range(n)]
        ok = True
        for p in sorted(paraules, key=lambda s: -len(s)):
            placed = False
            for _ in range(200):
                dr, dk = rnd.choice([(0, 1), (1, 0)])
                r = rnd.randrange(0, n - (len(p) - 1) * dr)
                k = rnd.randrange(0, n - (len(p) - 1) * dk)
                if all(g[r + i * dr][k + i * dk] in (None, ch) for i, ch in enumerate(p)):
                    for i, ch in enumerate(p):
                        g[r + i * dr][k + i * dk] = ch
                    placed = True
                    break
            if not placed:
                ok = False
                break
        if ok:
            for r in range(n):
                for k in range(n):
                    if g[r][k] is None:
                        g[r][k] = rnd.choice(pool)
            return g
    raise ValueError('no es pot col·locar ' + str(paraules))


def dibuixa_sopa(c, x, ytop, g, cs=20.5, fs=14):
    n = len(g)
    trac(c, 1.3, NAVY)
    c.setFillColor(white)
    c.roundRect(x - 3, ytop - n * cs - 3, n * cs + 6, n * cs + 6, 4, stroke=1, fill=1)
    for r in range(n):
        for k in range(n):
            txt(c, x + k * cs + cs / 2, ytop - r * cs - cs + (cs - fs * 0.72) / 2, g[r][k], fs, SANSB, INK, 'c')
    return n * cs + 6


def llista_paraules(c, x, ytop, paraules, size=12, lead=22):
    for i, p in enumerate(paraules):
        txt(c, x, ytop - i * lead, p, size, SANSB, NAVY)


# ------------------------------------------------------------------ crucigrama
def crucigrama(c, x, ytop, spec, cs=21):
    """spec: llista de (paraula, fila, col, 'h'|'v', número). Dibuixa les caselles amb el número."""
    cel = {}
    nums = {}
    for (p, r, k, d, nm) in spec:
        nums[(r, k)] = (nums[(r, k)] + '/' + str(nm)) if (r, k) in nums else str(nm)
        for i, ch in enumerate(p):
            cel[(r + (i if d == 'v' else 0), k + (i if d == 'h' else 0))] = ch
    for (r, k) in cel:
        rr(c, x + k * cs, ytop - (r + 1) * cs, cs, cs, 0, fill=white, lw=1.5, col=NAVY)
        if (r, k) in nums:
            txt(c, x + k * cs + 2.5, ytop - r * cs - 9, nums[(r, k)], 8, SANSB, OCRE)
    return cel


def pistes(c, x, ytop, ample, llista, size=11.5, lead=14):
    y = ytop
    for (a, b) in llista:
        txt(c, x, y, a, size, SANSB, OCRE)
        y = par(c, x + 26, y, b, size, ample - 26, lead, SANS, INK) - lead * 0.8
    return y


# ------------------------------------------------------------------ unir
def uneix(c, x, ytop, w, esq, dre, fila=34, ampl_esq=70, ampl_dre=None, fs=13, dibuix_dre=None, serif=True):
    """Dues columnes d'elements amb un punt a cada banda. `dibuix_dre(c, x, ycentre, k)` pinta cada element
       de la dreta (si no, text). Retorna la y final."""
    ampl_dre = ampl_dre or (w - ampl_esq - 50)
    for k, t in enumerate(esq):
        yy = ytop - k * fila
        rr(c, x, yy - 14, ampl_esq, 28, 14, fill=white, lw=1.5, col=NAVY)
        txt(c, x + ampl_esq / 2, yy - 5, t, fs, SERIFB if serif else SANSB, INK, 'c')
        c.setFillColor(NAVY)
        c.circle(x + ampl_esq + 12, yy, 4, stroke=0, fill=1)
    xr = x + w - ampl_dre
    for k, t in enumerate(dre):
        yy = ytop - k * fila
        c.setFillColor(NAVY)
        c.circle(xr - 12, yy, 4, stroke=0, fill=1)
        if dibuix_dre:
            dibuix_dre(c, xr, yy, k)
        else:
            rr(c, xr, yy - 14, ampl_dre, 28, 14, fill=white, lw=1.5, col=NAVY)
            txt(c, xr + ampl_dre / 2, yy - 5, t, fs - 1, SANSB, INK, 'c')
    return ytop - len(esq) * fila


# ------------------------------------------------------------------ veritat / fals
def veritat_fals(c, x, ytop, w, frases, size=12, lead=15):
    y = ytop
    for f in frases:
        h = alt_par(f, size, w - 84, lead)
        par(c, x, y, f, size, w - 84, lead, SANS, INK)
        for k, l in enumerate(('V', 'F')):
            cx = x + w - 54 + k * 32
            cy = y - h / 2 + lead / 2 - 5
            rr(c, cx - 12, cy - 12, 24, 24, 12, fill=white, lw=1.6, col=NAVY)
            txt(c, cx, cy - 4.6, l, 12.5, SANSB, NAVY_SOFT, 'c')
        y -= h + 10
    return y


def capcalera_vf(c, x, ytop, w):
    for k, l in enumerate(('veritat', 'fals')):
        txt(c, x + w - 54 + k * 32, ytop, l, 8.8, ETQ, MUTED, 'c')


# ------------------------------------------------------------------ caselles
def casella_dibuix(c, x, y, w, h, text=None):
    rr(c, x, y, w, h, 6, fill=white, lw=1.3, col=MUTED, dash=(3, 3))
    if text:
        txt(c, x + w / 2, y + 6, text, 9.5, SANS, MUTED, 'c')


def linia(c, x, y, w):
    trac(c, 1.2, NAVY_SOFT, (1, 3))
    c.line(x, y, x + w, y)
    c.setDash()


def quadres(c, x, ytop, n, mida=20, sep=6, ple=None):
    """n quadradets per escriure (una lletra cada un)."""
    for i in range(n):
        rr(c, x + i * (mida + sep), ytop - mida, mida, mida, 3, fill=white, lw=1.5, col=NAVY)
    return x + n * (mida + sep)


# ------------------------------------------------------------------ laberint
def laberint(c, x, ytop, cols, rows, cs, seed=5, lw=2.0):
    rnd = random.Random(seed)
    mur_h = [[True] * cols for _ in range(rows + 1)]     # parets horitzontals (sobre la fila r)
    mur_v = [[True] * (cols + 1) for _ in range(rows)]
    vist = [[False] * cols for _ in range(rows)]
    pila = [(0, 0)]
    vist[0][0] = True
    while pila:
        r, k = pila[-1]
        veins = [(r + dr, k + dk) for dr, dk in ((1, 0), (-1, 0), (0, 1), (0, -1))
                 if 0 <= r + dr < rows and 0 <= k + dk < cols and not vist[r + dr][k + dk]]
        if not veins:
            pila.pop()
            continue
        r2, k2 = rnd.choice(veins)
        vist[r2][k2] = True
        if r2 == r + 1:
            mur_h[r + 1][k] = False
        elif r2 == r - 1:
            mur_h[r][k] = False
        elif k2 == k + 1:
            mur_v[r][k + 1] = False
        else:
            mur_v[r][k] = False
        pila.append((r2, k2))
    mur_h[0][0] = False                  # entrada (a dalt, a l'esquerra)
    mur_h[rows][cols - 1] = False        # sortida (a baix, a la dreta)
    trac(c, lw, NAVY)
    for r in range(rows + 1):
        for k in range(cols):
            if mur_h[r][k]:
                c.line(x + k * cs, ytop - r * cs, x + (k + 1) * cs, ytop - r * cs)
    for r in range(rows):
        for k in range(cols + 1):
            if mur_v[r][k]:
                c.line(x + k * cs, ytop - r * cs, x + k * cs, ytop - (r + 1) * cs)
    return cols * cs, rows * cs
