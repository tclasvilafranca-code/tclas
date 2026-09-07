# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las 17 piezas de Nel.

   Compases, márgenes, material repetido entre hojas, altura final de cada
   hoja y texto que no cabe en su caja: lo de siempre, y todo tiene que decir
   OK.

   Aquí NO hay auditoría de variedad de recetas: el esquema de adulto son
   seis hojas fijas, no una hoja de deberes con bloques rotatorios. La
   variedad la ponen las hojas generadas (calentamiento, agudeza,
   relajación) y la hoja de "cómo se estudia", escrita pieza a pieza.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar

MODULOS = ['nl_01_petite', 'nl_02_counting', 'nl_03_deck', 'nl_04_heart',
           'nl_05_hittheroad', 'nl_06_jailhouse', 'nl_07_bellaciao', 'nl_08_canthelp',
           'nl_09_toreador', 'nl_10_lovely', 'nl_11_rasputin', 'nl_12_diamonds',
           'nl_13_favourite', 'nl_14_sweetchild', 'nl_15_merry', 'nl_16_acomme',
           'nl_17_dragon']


def revisar_nivel(modulos):
    """Nel sube por la curva de los avanzados (cancion.CURVA['nel']), pero
       sigue siendo formato adulto estándar, sin los bloques de la versión
       exigente de Josep. Aquí solo se comprueba lo que es norma fija:
       formato adulto y el esquema mínimo del dosier presente en las 17
       piezas."""
    fallos = []
    for mod in modulos:
        cfg = __import__(mod).CANCION
        if cfg.get('formato') != 'adulto':
            fallos.append('%s: formato %r, tendría que ser adulto' % (mod, cfg.get('formato')))
        if not cfg.get('piano1', {}).get('bloques'):
            fallos.append('%s: no tiene bloques en la hoja de estudio' % mod)
    print('\n  nivel · %d piezas · formato adulto, hoja de estudio presente · %s'
          % (len(modulos), 'ok' if not fallos else '%d FALLOS' % len(fallos)))
    for f in fallos:
        print('     %s' % f)
    return fallos


def main():
    fallos = 0
    for nombre in MODULOS:
        fallos += len(auditar(__import__(nombre).CANCION))
    fallos += len(revisar_nivel(MODULOS))
    print('\n%s' % ('TODO OK' if not fallos else '%d FALLOS EN TOTAL' % fallos))
    return fallos


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
