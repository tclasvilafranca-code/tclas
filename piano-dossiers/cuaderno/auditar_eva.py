# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las canciones de Eva."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar

MODULOS = ['eva_01_canthelp', 'eva_02_sky', 'eva_03_poema',
           'eva_04_what', 'eva_05_thinking', 'eva_06_cisne',
           'eva_07_bruno', 'eva_08_promesa', 'eva_09_amiga',
           'eva_10_young', 'eva_11_soldadito', 'eva_12_favourite',
           'eva_13_merry', 'eva_14_santa', 'eva_15_beginning',
           'eva_16_arabesque', 'eva_17_bohemian']


def main():
    fallos = 0
    for nombre in MODULOS:
        fallos += len(auditar(__import__(nombre).CANCION))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
