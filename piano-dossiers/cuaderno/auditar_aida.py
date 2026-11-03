# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las piezas de Aida.

   Ademas de lo de siempre (compases, margenes, material repetido entre hojas y
   altura final de cada hoja), comprueba la norma de variedad sobre sus hojas de
   trabajo semanales y que cada una cumple el reparto de `ai_recetas`.

   Dos cosas propias, y las dos estan razonadas en `ai_recetas`:

     - `plan` y `escucha` van los dos como **estructurales**, igual que en
       Josep: en este cuaderno el recuadro de "para la proxima clase" sale las
       19 semanas a proposito.
     - `distancia=7`. El reparto esta atado a propiedades de las partituras
       (`cifrado` solo donde el cifrado esta impreso, `cuatro_manos` solo en
       los duetos) y las piezas con cifrado se concentran al principio del
       album, asi que ocho no da: siete es lo que deja el reparto y en siete se
       audita.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar
from auditar_variedad import revisar_variedad
from ai_recetas import revisar_reparto

MODULOS = ['ai_01_romance', 'ai_02_scherzo', 'ai_03_wewishyou', 'ai_04_canthelp',
           'ai_05_what', 'ai_06_counting', 'ai_07_perfect', 'ai_08_boig',
           'ai_09_kiss', 'ai_10_beginning', 'ai_11_titanic', 'ai_12_hijoluna',
           'ai_13_carol', 'ai_14_silence', 'ai_15_gladiator', 'ai_16_unbeso',
           'ai_17_pachelbel', 'ai_18_preludio', 'ai_19_acomme']

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
    fallos += len(revisar_variedad(hojas_de_trabajo(MODULOS), 'Aída',
                                   distancia=7, min_tipos=15,
                                   estructurales=ESTRUCTURALES))
    fallos += len(revisar_reparto(MODULOS))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
