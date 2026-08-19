# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las 19 piezas de Eduard.

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

MODULOS = ['ed_01_romance', 'ed_02_america', 'ed_03_banner', 'ed_04_counting',
           'ed_05_peaches', 'ed_06_someone', 'ed_07_deck', 'ed_08_jailhouse',
           'ed_09_clock', 'ed_10_shallow', 'ed_11_canthelp', 'ed_12_carol',
           'ed_13_adagio', 'ed_14_rasputin', 'ed_15_toreador', 'ed_16_trouble',
           'ed_17_acomme', 'ed_18_interstellar', 'ed_19_flying']


def revisar_nivel(modulos):
    """Eduard tiene el mismo nivel y el mismo repertorio que Jose Maria
       (cancion.CURVA['eduard'] = la misma curva). Aqui solo se comprueba lo
       que es norma fija: formato adulto y el esquema minimo del dosier
       presente en las 19 piezas."""
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
