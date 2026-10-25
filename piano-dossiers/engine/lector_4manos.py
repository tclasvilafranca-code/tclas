# -*- coding: utf-8 -*-
"""Lectura de una partitura a CUATRO MANOS: cuatro pentagramas por sistema.
   sistemas() empareja de dos en dos y aqui no vale, asi que se agrupan de
   cuatro: 0-1 son el Primo (las dos manos en clave de sol) y 2-3 el Secondo.
"""
import os
import sys
import glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score_reader as sr

CLAVES = ['treble', 'treble', 'treble', 'bass']


def leer4(pdf, out):
    pgs = sr.render(pdf, out)
    n = 0
    filas = []
    for path in pgs:
        a = sr.load(path)
        ps = sr.pentagramas(a)
        for i in range(0, len(ps) - 3, 4):
            grupo = ps[i:i + 4]
            top, bot = grupo[0][0], grupo[3][1]
            bs = sr._mas_regular(sr.barras(a, top, bot),
                                 sr._interseca(sr.barras(a, grupo[0][0], grupo[0][1]),
                                               sr.barras(a, grupo[3][0], grupo[3][1]), tol=6))
            if len(bs) < 2:
                continue
            for k in range(len(bs) - 1):
                n += 1
                xa, xb = bs[k] + 4, bs[k + 1] - 3
                voces = []
                for j, (t, b) in enumerate(grupo):
                    h = sr.cabezas(a, t, b, CLAVES[j], xa, xb)
                    voces.append(' '.join(x[1] for x in h))
                filas.append((n, voces))
    return filas


if __name__ == '__main__':
    for n, v in leer4(sys.argv[1], sys.argv[2]):
        print('c.%02d  P1a: %-30s P1b: %-30s P2a: %-22s P2b: %s' % (n, v[0], v[1], v[2], v[3]))
