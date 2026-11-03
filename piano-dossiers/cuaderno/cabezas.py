# -*- coding: utf-8 -*-
"""Mide la altura de cada cabeza de nota de un pentagrama y dice su nombre.

   Herramienta de medicion, no de dibujo: es la que convierte "me parece que
   esa nota esta en el segundo espacio" en un numero. Se uso para transcribir
   las partituras de Jose Maria (ver TRANSCRIPCION_JM_FUENTES.md).

   Detecta las cinco lineas, borra las lineas y las plicas (columnas finas) y
   busca los ovalos: son las manchas anchas de cada nota. Devuelve la lista
   ordenada por x con su altura calculada contra las lineas.
"""
import sys
from PIL import Image
import numpy as np
from scipy import ndimage

TREBLE = ['F5','E5','D5','C5','B4','A4','G4','F4','E4','D4','C4','B3','A3','G3','F3']
BASS = ['A3','G3','F3','E3','D3','C3','B2','A2','G2','F2','E2','D2','C2','B1','A1']


def medir(img, x0, x1, y0, y1, clave='sol', ancho_min=5, verbose=True):
    im = Image.open(img).convert('L').crop((x0, y0, x1, y1))
    arr = np.array(im)
    m = arr < 140
    tinta = m.sum(axis=1)
    umbral = tinta.max() * 0.55
    filas = [i for i, v in enumerate(tinta) if v >= umbral]
    grupos, act = [], [filas[0]]
    for f in filas[1:]:
        if f - act[-1] <= 2:
            act.append(f)
        else:
            grupos.append(sum(act) / len(act)); act = [f]
    grupos.append(sum(act) / len(act))
    paso = (grupos[-1] - grupos[0]) / 8.0        # medio espacio en pixeles

    # fuera las lineas del pentagrama: se borran las filas que son casi todo negro
    limpio = m.copy()
    for g in grupos:
        for r in range(int(g) - 1, int(g) + 2):
            if 0 <= r < limpio.shape[0]:
                # solo se borra donde NO hay nada grueso encima o debajo
                vecino = limpio[max(0, r - 3):r + 4].sum(axis=0)
                limpio[r] &= vecino > 5
    # las cabezas son mas anchas que las plicas: erosion horizontal
    est = np.ones((1, 4), bool)
    cabezas = ndimage.binary_erosion(limpio, structure=est)
    lab, n = ndimage.label(cabezas)
    out = []
    for i in range(1, n + 1):
        ys, xs = np.where(lab == i)
        if len(ys) < 12:
            continue
        if xs.max() - xs.min() < ancho_min:
            continue
        cy = ys.mean()
        idx = (cy - grupos[0]) / paso
        nombres = TREBLE if clave == 'sol' else BASS
        j = int(round(idx))
        nom = nombres[j] if 0 <= j < len(nombres) else '?%.1f' % idx
        out.append((xs.mean(), nom, round(idx, 2), len(ys)))
    out.sort()
    if verbose:
        print('lineas %s · medio espacio %.2f px · %d cabezas'
              % ([round(g, 1) for g in grupos], paso, len(out)))
        print('  ' + '  '.join('%s' % o[1] for o in out))
        for o in out:
            print('    x=%6.1f  %-4s  idx=%5.2f  px=%d' % o)
    return out


if __name__ == '__main__':
    a = sys.argv
    medir(a[1], int(a[2]), int(a[3]), int(a[4]), int(a[5]), a[6] if len(a) > 6 else 'sol')
