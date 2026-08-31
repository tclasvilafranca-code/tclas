# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las 20 piezas de Eduard.

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

MODULOS = ['ed_01_clementine', 'ed_02_aristogatos', 'ed_03_eso',
           'ed_04_america', 'ed_05_banner', 'ed_06_pantera', 'ed_07_nocturno',
           'ed_08_beginner', 'ed_09_puff', 'ed_10_heart', 'ed_11_dream',
           'ed_12_navidad', 'ed_13_greensleeves', 'ed_14_honor',
           'ed_15_rasputin', 'ed_16_jinglerock', 'ed_17_pianoman',
           'ed_18_clock', 'ed_19_toreador']


def revisar_nivel(modulos):
    """Eduard es un adulto de unos 65 anos que empieza de cero, y su cuaderno
       se rehizo entero sobre SU carpeta de Drive. Aqui solo se comprueba lo
       que es norma fija: formato adulto y el esquema minimo del dosier
       presente en las 20 piezas."""
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
