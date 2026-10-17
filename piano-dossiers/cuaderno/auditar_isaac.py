# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las 20 piezas de Isaac.

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

MODULOS = ['is_01_petite', 'is_02_saints', 'is_03_puff', 'is_04_beginner',
           'is_05_wewishyou', 'is_06_christmas', 'is_07_silentnight', 'is_08_silentnight4h',
           'is_09_panthere', 'is_10_pianoman', 'is_11_greensleeves', 'is_12_grandfather',
           'is_13_doremi', 'is_14_dream', 'is_15_gladiator', 'is_16_rasputin',
           'is_17_jailhouse', 'is_18_toreador', 'is_19_furelise', 'is_20_diabelli']


def revisar_nivel(modulos):
    """Isaac sube por la curva de nivel medio (cancion.CURVA['isaac']), mas
       rapido que Jose Maria o Merce pero sin llegar al techo de los
       avanzados. Aqui solo se comprueba lo que es norma fija: formato
       adulto y el esquema minimo del dosier presente en las 20 piezas."""
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
