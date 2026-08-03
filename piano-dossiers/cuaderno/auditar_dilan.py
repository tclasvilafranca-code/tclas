# -*- coding: utf-8 -*-
"""Pasa las cuatro comprobaciones a las veinte canciones de Dilan de una vez.

   Las dos primeras se montaron antes de que existiera cancion.py y llevan
   sus propios build_*_d0N.py, asi que se auditan con auditar_hojas().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from ficha_info import build_ficha
from hoja_calentamiento import build_calentamiento
from hoja_lectura import build_lectura
from hoja_piano import build_piano
from cancion import auditar, auditar_hojas

ANTIGUAS = [('ElCisne', 'd01'), ('CantHelp', 'd02')]
MODULOS = ['dilan_03_your_song', 'dilan_04_thinking', 'dilan_05_lucia',
           'dilan_06_poema', 'dilan_07_amiga', 'dilan_08_promesa',
           'dilan_09_bruno', 'dilan_10_calor', 'dilan_11_soldadito',
           'dilan_12_sky', 'dilan_13_what', 'dilan_14_writings',
           'dilan_15_favourite', 'dilan_16_adagio', 'dilan_17_arabesque',
           'dilan_18_merry', 'dilan_19_santa', 'dilan_20_beginning']


def main():
    fallos = 0
    for etq, suf in ANTIGUAS:
        bf = __import__('build_ficha_' + suf)
        bc = __import__('build_calentamiento_' + suf)
        bl = __import__('build_lectura_' + suf)
        bp = __import__('build_piano_' + suf)
        hojas = [('ficha', lambda c, m=bf: build_ficha(c, m.CFG)),
                 ('calentamiento', lambda c, m=bc: build_calentamiento(c, m.CFG)),
                 ('agudeza', lambda c, m=bl: build_lectura(c, m.CFG)),
                 ('piano 1', lambda c, m=bp: build_piano(c, m.PAG1)),
                 ('piano 2', lambda c, m=bp: build_piano(c, m.PAG2))]
        fallos += len(auditar_hojas(hojas, etq))
    for nombre in MODULOS:
        fallos += len(auditar(__import__(nombre).CANCION))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
