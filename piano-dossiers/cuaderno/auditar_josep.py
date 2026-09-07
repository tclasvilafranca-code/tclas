# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las piezas de Josep.

   Además de lo de siempre (compases, márgenes, material repetido entre hojas
   y altura final de cada hoja), comprueba la norma de variedad sobre sus hojas
   de trabajo semanales y que cada una cumple el reparto de `jp_recetas`.

   Dos diferencias con el auditor de José María:

     - `plan` y `escucha` van los dos como **estructurales**. En este cuaderno
       el recuadro de "para la próxima clase" sale las 19 semanas a propósito,
       igual que el plan de minutos: el hilo entre la semana en casa y la clase
       siguiente no se corta ninguna semana.
     - `distancia=8`, no 6. El reparto de Josep está atado a propiedades de las
       partituras (`cifrado` solo donde el cifrado está impreso, `cuatro_manos`
       solo en los duetos), así que las parejas de recetas no pueden estar a
       diez hojas como en José María; ocho es lo que da el reparto y se audita
       en ocho, no en seis.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar
from auditar_variedad import revisar_variedad
from jp_recetas import revisar_reparto

MODULOS = ['jp_01_romance', 'jp_02_petite', 'jp_03_peaches', 'jp_04_counting',
           'jp_05_what', 'jp_06_heart', 'jp_07_hittheroad', 'jp_08_deck',
           'jp_09_jailhouse', 'jp_10_bellaciao', 'jp_11_canthelp', 'jp_12_lovely',
           'jp_13_rasputin', 'jp_14_beginning', 'jp_15_favourite',
           'jp_16_sweetchild', 'jp_17_unbeso', 'jp_18_merry', 'jp_19_acomme']

ESTRUCTURALES = {'rutina', 'plan', 'escucha'}


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
    fallos += len(revisar_variedad(hojas_de_trabajo(MODULOS), 'Josep',
                                   distancia=8, min_tipos=15,
                                   estructurales=ESTRUCTURALES))
    fallos += len(revisar_reparto(MODULOS))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
