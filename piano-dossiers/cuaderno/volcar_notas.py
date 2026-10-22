# -*- coding: utf-8 -*-
"""Vuelca las notas de una partitura (vectorial o de fuente musical) por sistema y compas:
   `python3 volcar_notas.py entrada.pdf` -> para cada sistema, cada compas con las notas de la
   mano derecha (clave de sol) e izquierda (clave de fa) en solfeo + octava (Do4 = Do central).
   Las alteraciones NO se leen (se ven en la imagen); sirve para medir compases y registros."""
import sys
import pymupdf
from colorear_notas import pentagramas, cabezas, glifos, LETRAS

SOL = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']


def nombre(clave, paso):
    """paso = medios-espacios sobre la linea de abajo. sol: Mi4; fa: Sol2."""
    base = (2 + 4 * 7) if clave == 'G' else (4 + 2 * 7)   # indice diatonico absoluto: Mi4 = 30, Sol2 = 18
    n = base + paso
    return '%s%d' % (SOL[n % 7], n // 7)


def barras(dr, sts):
    xs = []
    for p in dr:
        for it in p['items']:
            if it[0] == 'l' and abs(it[1].x - it[2].x) < 0.05:
                xs.append((it[1].x, min(it[1].y, it[2].y), max(it[1].y, it[2].y)))
    out = []
    for xl, xr, ys in sts:
        alto = ys[4] - ys[0]
        b = sorted(round(x, 0) for x, y0, y1 in xs
                   if y0 <= ys[0] + 1 and y1 >= ys[4] - 1 and (y1 - y0) > alto * 1.05 and y0 >= ys[0] - 130 and y1 <= ys[4] + 130
                   and xl - 3 <= x <= xr + 3)
        ded = []
        for x in b:
            if not ded or x - ded[-1] > 8:
                ded.append(x)
        out.append(ded)
    return out


def volcar(pdf):
    doc = pymupdf.open(pdf)
    for pn, pg in enumerate(doc, 1):
        dr = pg.get_drawings()
        sts = pentagramas(dr)
        if not sts:
            continue
        gap = sts[0][2][1] - sts[0][2][0]
        cab = cabezas(dr, gap)
        gl, claves = glifos(pg)
        cab += gl
        ded = []
        for h in sorted(cab):
            if not any(abs(h[0] - q[0]) < 1.6 and abs(h[1] - q[1]) < 1.6 for q in ded):
                ded.append(h)
        cab = ded
        bar = barras(dr, sts)
        tipo = []
        for k, (xl, xr, ys) in enumerate(sts):
            m = None
            for cx, cy, c in claves:
                if abs(cx - xl) < 40 and ys[0] - 2 * gap <= cy <= ys[4] + 2 * gap:
                    m = c
            tipo.append(m or ('G' if k % 2 == 0 else 'F'))
        por_staff = {k: [] for k in range(len(sts))}
        for cx, cy, w, tp in cab:
            mejor, dmin = None, 1e9
            for k, (xl, xr, ys) in enumerate(sts):
                cen = (ys[0] + ys[4]) / 2
                if xl - 5 <= cx <= xr + 5 and abs(cy - cen) < dmin:
                    mejor, dmin = k, abs(cy - cen)
            if mejor is None or dmin > 5.2 * gap:
                continue
            ys = sts[mejor][2]
            paso = round((ys[4] - cy) / ((ys[1] - ys[0]) / 2.0))
            por_staff[mejor].append((cx, nombre(tipo[mejor], paso), tp))
        print('=== pagina %d: %d pentagramas' % (pn, len(sts)))
        for k, (xl, xr, ys) in enumerate(sts):
            bs = bar[k]
            fin = [x for x in bs]
            lim = [xl] + [x for x in fin if x > xl + 12] + [xr + 6]
            if len(lim) > 2:
                lim = lim[:-1] if lim[-2] > xr - 8 else lim
            fila = []
            for a, b in zip(lim, lim[1:]):
                ns = sorted([(cx, n, tp) for cx, n, tp in por_staff[k] if a <= cx < b])
                grp, last = [], None
                for cx, n, tp in ns:
                    if last is not None and abs(cx - last) < 3.5:
                        grp[-1] += '+' + n
                    else:
                        grp.append(n + ('' if tp == 'n' else ('°' if tp == 'b' else '○')))
                    last = cx
                fila.append(' '.join(grp) if grp else '-')
            print('  [%d] %s y=%.0f: %s' % (k, 'sol' if tipo[k] == 'G' else 'fa ', ys[0], ' | '.join(fila)))


if __name__ == '__main__':
    volcar(sys.argv[1])
