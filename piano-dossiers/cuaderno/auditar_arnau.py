# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las canciones de Arnau."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar
from auditar_variedad import revisar_variedad, hojas_de_deberes
from arnau_recetas import revisar_reparto

MODULOS = ['arnau_01_chopsticks', 'arnau_02_clementine', 'arnau_03_jolly',
           'arnau_04_ears', 'arnau_05_wheels', 'arnau_06_saints',
           'arnau_07_wewish', 'arnau_08_baabaa', 'arnau_09_polly',
           'arnau_10_muffet', 'arnau_11_eso', 'arnau_12_puff',
           'arnau_13_pantera', 'arnau_14_bonnie', 'arnau_15_largo',
           'arnau_16_aloha', 'arnau_17_popeye', 'arnau_18_submarino',
           'arnau_19_rain', 'arnau_20_mulberry']


def main():
    fallos = 0
    for nombre in MODULOS:
        fallos += len(auditar(__import__(nombre).CANCION))
    print()
    fallos += len(revisar_variedad(hojas_de_deberes(MODULOS), 'Arnau'))
    fallos += len(revisar_reparto(MODULOS))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
