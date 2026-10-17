# -*- coding: utf-8 -*-
"""Lee cabezas HUECAS en el pentagrama de la MANO IZQUIERDA.

   El truco de rellenar huecos falla en general (rellena lo que encierran las
   ligaduras), pero en una izquierda de acordes sin ligaduras es fiable.
   Aun asi: esto se contrasta a ojo antes de escribir nada.
"""
import os
import sys
import numpy as np
from scipy import ndimage
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score_reader as sr


def cabezas_huecas(a, top, bot, clef, x0, x1, pad_arriba=3.0, pad_abajo=3.0):
    step = (bot - top) / 8.0
    y0 = int(top - step * 2 * pad_arriba)
    y1 = int(bot + step * 2 * pad_abajo)
    y0, y1 = max(0, y0), min(a.shape[0], y1)
    win = a[y0:y1, int(x0):int(x1)]
    lleno = ndimage.binary_fill_holes(win)
    ev = max(3, int(round(step * 0.93)))
    eh = max(5, int(round(step * 1.67)))
    ab = ndimage.binary_opening(lleno, structure=np.ones((ev, eh)))
    lab, n = ndimage.label(ab)
    out = []
    for i in range(1, n + 1):
        ys, xs = np.where(lab == i)
        h, w = ys.max() - ys.min() + 1, xs.max() - xs.min() + 1
        if not (step * 1.10 <= h <= step * 2.85 and step * 1.45 <= w <= step * 4.55):
            continue
        cy = ys.mean() + y0
        cx = xs.mean() + int(x0)
        p = (cy - top) / step + sr.OFFSET
        idx = int(round(p))
        tabla = sr.TREBLE if clef == 'treble' else sr.BASS
        if 0 <= idx < len(tabla):
            out.append((cx, tabla[idx], cy))
    out.sort()
    return out


if __name__ == '__main__':
    a = sr.load('/tmp/claude-0/-home-user-tclas/34206757-a690-5241-b1bf-4ebbff352a1e/scratchpad/rd_prom/pg-1.jpg')
    sis = sr.sistemas(a)
    n = 0
    for si, (tt, tb, bt, bb) in enumerate(sis, 1):
        entero = sr.barras(a, tt, bb)
        cruce = sr._interseca(sr.barras(a, tt, tb), sr.barras(a, bt, bb), tol=5)
        bs = sr._mas_regular(entero, cruce)
        for k in range(len(bs) - 1):
            n += 1
            xa, xb = bs[k] + 4, bs[k + 1] - 3
            h = cabezas_huecas(a, bt, bb, 'bass', xa, xb)
            print('c.%02d  MI huecas: %s' % (n, ' '.join(t[1] for t in h)))
