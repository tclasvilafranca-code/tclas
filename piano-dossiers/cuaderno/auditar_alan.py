# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las piezas de Alan.

   Lo de siempre (compases, márgenes, material repetido entre hojas, altura
   final de cada hoja), la norma de variedad sobre sus hojas de trabajo y que
   cada una cumple el reparto de `al_recetas`. Mismas reglas que Josep:
   `plan` y `escucha` son estructurales y la distancia mínima entre dos usos
   de una receta es 8.
"""
import glob
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from cancion import auditar
from auditar_variedad import revisar_variedad
from al_recetas import revisar_reparto

MODULOS = sorted(os.path.basename(f)[:-3]
                 for f in glob.glob(os.path.join(HERE, 'al_[0-9]*.py')))

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
    fallos += len(revisar_variedad(hojas_de_trabajo(MODULOS), 'Alan',
                                   distancia=8, min_tipos=15,
                                   estructurales=ESTRUCTURALES))
    fallos += len(revisar_reparto(MODULOS))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
