# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las piezas de José María.

   Además de lo de siempre (compases, márgenes, material repetido entre hojas
   y altura final de cada hoja), comprueba la norma de variedad sobre sus
   hojas de trabajo semanales y que cada una cumple el reparto de
   `jm_recetas`.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar
from auditar_variedad import revisar_variedad
from jm_recetas import revisar_reparto

MODULOS = ['jm_01_romance', 'jm_02_america', 'jm_03_banner', 'jm_04_counting',
           'jm_05_peaches', 'jm_06_someone', 'jm_07_deck', 'jm_08_jailhouse',
           'jm_09_clock', 'jm_10_shallow', 'jm_11_canthelp', 'jm_12_carol',
           'jm_13_adagio', 'jm_14_rasputin', 'jm_15_toreador', 'jm_16_trouble',
           'jm_17_acomme', 'jm_18_interstellar', 'jm_19_flying']


def hojas_de_trabajo(modulos):
    hojas = []
    for mod in modulos:
        cfg = __import__(mod).CANCION
        for hoja in cfg.get('trabajo') or []:
            hojas.append(('%02d' % cfg['num'], [b['tipo'] for b in hoja['bloques']]))
    return hojas


def main():
    fallos = 0
    for nombre in MODULOS:
        fallos += len(auditar(__import__(nombre).CANCION))
    print()
    # min_tipos baja mientras el album esta a medias: con cinco piezas todavia
    # no han salido las diez recetas.
    fallos += len(revisar_variedad(hojas_de_trabajo(MODULOS), 'José María',
                                   min_tipos=15))
    fallos += len(revisar_reparto(MODULOS))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
