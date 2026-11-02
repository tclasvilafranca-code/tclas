# -*- coding: utf-8 -*-
"""Piezas comunes del cuaderno KIDS: plan del mes, tablero de logros, diagramas y sopa de letras."""
from k1_base import *
import k1_base as KB
from k1_base import _alto

FIG_NOM = {'w': 'REDONDA', 'h': 'BLANCA', 'q': 'NEGRA', 'e': 'CORCHEA'}
FIG_TPO = {'w': 4, 'h': 2, 'q': 1, 'e': 0.5}


def K_plan(items, titulo='MI PLAN DEL MES'):
    """Lista visual de lo que se aprende este mes: numero, frase corta y un circulo que se colorea al terminarlo."""
    alts = [max(44, _alto(t, 13, CW - 140) + 18) for t in items]

    def f(c, x, y, w):
        yy = y
        for k, (t, hh) in enumerate(zip(items, alts)):
            rr(c, x, yy - hh + 6, w, hh - 6, 12, fill=white, lw=1.5, col=NAVY)
            K.quadrat(c, x + 12, yy - hh / 2 - 12 + 3, k + 1, 24)
            kpar(c, x + 50, yy - hh / 2 + 9, t, 13, w - 120, 13 * 1.38, SANS, INK)
            c.setFillColor(white)
            trac(c, 1.8, OCRE)
            c.circle(x + w - 28, yy - hh / 2 + 3, 14, stroke=1, fill=1)
            yy -= hh
    return Blk(sum(alts) + 6, f)


def K_tablero(mes, items):
    """Tablero de logros del mes: una casilla grande por tarea (el niño la colorea) y la medalla al final."""
    n = len(items)
    h = 40 + n * 46 + 90

    def f(c, x, y, w):
        txt(c, x, y - 14, 'MIS LOGROS DE %s' % mes.upper(), 12.5, ETQ, OCRE)
        yy = y - 26
        for k, t in enumerate(items):
            rr(c, x, yy - 38, w, 38, 10, fill=white, lw=1.5, col=NAVY)
            c.setFillColor(white)
            trac(c, 1.8, OCRE)
            c.rect(x + 10, yy - 31, 24, 24, stroke=1, fill=1)
            txt(c, x + 46, yy - 24, t, 13, SANS, INK)
            c.setDash()
            yy -= 46
        # medalla
        cx = x + w / 2.0
        trac(c, 1.8, NAVY)
        c.setFillColor(white)
        c.circle(cx, yy - 40, 30, stroke=1, fill=1)
        trac(c, 1.2, OCRE)
        c.circle(cx, yy - 40, 23, stroke=1, fill=0)
        txt(c, cx, yy - 46, '★', 26, 'DejaVuSans-Bold', OCRE, 'c')
        txt(c, cx + 48, yy - 36, 'Cuando termines, pinta la medalla.', 12, SANS, MUTED)
    return Blk(h, f)


def K_diag_pentagrama():
    """Pentagrama con las 5 lineas y los 4 espacios numerados de abajo hacia arriba."""
    h = 190

    def f(c, x, y, w):
        gap = 24.0
        top = y - 30
        ws = w - 230
        yb = K.pauta(c, x + 6, top, ws, gap, 'treble')
        for k in range(5):
            yy = yb + k * gap
            rr(c, x + 6 + ws + 14, yy - 10, 74, 20, 10, fill=white, lw=1.3, col=NAVY)
            txt(c, x + 6 + ws + 14 + 37, yy - 4.2, 'línea %d' % (k + 1), 11.5, SANSB, NAVY, 'c')
        for k in range(4):
            yy = yb + k * gap + gap / 2.0
            rr(c, x + 6 + ws + 100, yy - 9, 84, 18, 9, fill=WARM, lw=1.3, col=OCRE)
            txt(c, x + 6 + ws + 100 + 42, yy - 3.8, 'espacio %d' % (k + 1), 11, SANSB, OCRE, 'c')
        txt(c, x, y - 4, 'Se cuentan de abajo hacia arriba  ↑', 11.5, ETQ, OCRE)
    return Blk(h, f)


def K_notas_colores(titulo='LAS 7 NOTAS Y SUS COLORES'):
    """Siete circulos grandes: nombre de la nota y su color (siempre el mismo en todo el cuaderno)."""
    h = 92

    def f(c, x, y, w):
        txt(c, x, y - 12, titulo, 11, ETQ, OCRE)
        cw = w / 7.0
        for k, nm in enumerate(NOMBRES):
            cx = x + cw * (k + 0.5)
            c.setFillColor(HexColor(COL[nm]))
            trac(c, 1.8, NAVY)
            c.circle(cx, y - 44, 24, stroke=1, fill=1)
            txt(c, cx, y - 49, nm, 13.5, SANSB, INK, 'c')
            txt(c, cx, y - 82, COLNOM[nm], 11, SANS, NAVY_SOFT, 'c')
    return Blk(h, f)


def K_tabla_figuras(figs=('w', 'h', 'q', 'e')):
    """Figura, nombre y cuantos tiempos dura (los tiempos se ven como circulos)."""
    RH = 54
    h = 28 + len(figs) * RH

    def f(c, x, y, w):
        for j, t in enumerate(('FIGURA', 'NOMBRE', 'DURA')):
            txt(c, x + [30, 140, 300][j], y - 14, t, 10.5, ETQ, OCRE)
        yy = y - 22
        for k, d_ in enumerate(figs):
            rr(c, x, yy - RH + 6, w, RH - 6, 12, fill=white if k % 2 == 0 else WARM, lw=1.2, col=NAVY)
            K.figura(c, d_, x + 48, yy - 40, 9.0)
            txt(c, x + 140, yy - 32, FIG_NOM[d_], 15, SANSB, NAVY)
            n = FIG_TPO[d_]
            cx0 = x + 300
            full = int(n)
            for i in range(full):
                c.setFillColor(HexColor('#2E86C8'))
                trac(c, 1.4, NAVY)
                c.circle(cx0 + i * 26, yy - 28, 10, stroke=1, fill=1)
            if n != full:
                trac(c, 1.4, NAVY)
                c.setFillColor(white)
                c.circle(cx0, yy - 28, 10, stroke=1, fill=1)
                c.setFillColor(HexColor('#2E86C8'))
                p = c.beginPath()
                p.moveTo(cx0, yy - 28)
                p.arcTo(cx0 - 10, yy - 38, cx0 + 10, yy - 18, 90, 180)
                p.close()
                c.drawPath(p, stroke=0, fill=1)
                trac(c, 1.4, NAVY)
                c.circle(cx0, yy - 28, 10, stroke=1, fill=0)
            txt(c, cx0 + max(1, int(n) if n >= 1 else 1) * 26 + 6, yy - 33, ('%g tiempo%s' % (n, '' if n == 1 else 's')).replace('0.5', '½'), 12, SANS, MUTED)
            yy -= RH
    return Blk(h, f)


def sopa_letras(palabras, n=9, sem=3):
    """Sopa de letras SOLO en horizontal y vertical (hacia la derecha y hacia abajo)."""
    r = rnd(sem)
    g = [[None] * n for _ in range(n)]
    pos = {}
    for pal in sorted(palabras, key=len, reverse=True):
        for _ in range(500):
            dy, dx = r.choice([(0, 1), (1, 0)])
            L = len(pal)
            y0, x0 = r.randrange(n), r.randrange(n)
            if not (0 <= y0 + dy * (L - 1) < n and 0 <= x0 + dx * (L - 1) < n):
                continue
            if all(g[y0 + dy * k][x0 + dx * k] in (None, pal[k]) for k in range(L)):
                for k in range(L):
                    g[y0 + dy * k][x0 + dx * k] = pal[k]
                pos[pal] = (y0, x0, dy, dx)
                break
        else:
            raise RuntimeError(pal)
    pool = 'ABCDEFGHILMNOPQRSTUV'
    for yy in range(n):
        for xx in range(n):
            if g[yy][xx] is None:
                g[yy][xx] = r.choice(pool)
    return g, pos


def K_sopa(g, palabras, cell=36):
    n = len(g)
    h = n * cell + 12

    def f(c, x, y, w):
        x0 = x + 4
        rr(c, x0 - 4, y - n * cell - 6, n * cell + 8, n * cell + 8, 8, fill=white, lw=1.7, col=NAVY)
        for r_ in range(n):
            for k in range(n):
                txt(c, x0 + k * cell + cell / 2 - 2, y - r_ * cell - cell + 10, g[r_][k], 20, SANSB, INK, 'c')
        bx = x0 + n * cell + 22
        txt(c, bx, y - 12, 'BUSCA:', 12, ETQ, OCRE)
        for k, p in enumerate(palabras):
            yy = y - 36 - k * 38
            c.setFillColor(HexColor(COL[p]) if p in COL else white)
            trac(c, 1.6, NAVY)
            c.circle(bx + 14, yy, 13, stroke=1, fill=1)
            txt(c, bx + 36, yy - 5, p, 15, SANSB, INK)
            trac(c, 1.4, OCRE)
            c.setFillColor(white)
            c.rect(bx + 96, yy - 10, 20, 20, stroke=1, fill=1)
    return Blk(h, f)
