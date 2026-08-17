# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las canciones de Arnau."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar

MODULOS = ['arnau_01_chopsticks', 'arnau_02_clementine', 'arnau_03_jolly',
           'arnau_04_ears', 'arnau_05_wheels', 'arnau_06_saints',
           'arnau_07_wewish', 'arnau_08_baabaa', 'arnau_09_polly',
           'arnau_10_muffet']


def main():
    fallos = 0
    for nombre in MODULOS:
        fallos += len(auditar(__import__(nombre).CANCION))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
