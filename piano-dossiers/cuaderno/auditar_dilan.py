# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las veinte canciones de Dilan.

   Desde el rediseno las veinte pasan por el mismo sitio: las dos primeras,
   que se escribieron antes de que existiera cancion.py, van envueltas en
   dilan_0N_cancion.py y se auditan igual que el resto.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar
from tareas_semana import revisar_variedad_tareas

MODULOS = ['dilan_01_cancion', 'dilan_02_cancion',
           'dilan_03_your_song', 'dilan_04_thinking', 'dilan_05_lucia',
           'dilan_06_poema', 'dilan_07_amiga', 'dilan_08_promesa',
           'dilan_09_bruno', 'dilan_10_calor', 'dilan_11_soldadito',
           'dilan_12_sky', 'dilan_13_what', 'dilan_14_writings',
           'dilan_15_favourite', 'dilan_16_adagio', 'dilan_17_arabesque',
           'dilan_18_merry', 'dilan_19_santa', 'dilan_20_beginning']


def main():
    fallos = 0
    for nombre in MODULOS:
        fallos += len(auditar(__import__(nombre).CANCION))
    print()
    fallos += len(revisar_variedad_tareas(
        'Dilan', [__import__(m).CANCION['num'] for m in MODULOS]))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
