# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las 27 piezas de Mercè.

   Compases, márgenes, material repetido entre hojas, altura final de cada
   hoja y texto que no cabe en su caja: lo de siempre, y todo tiene que decir
   OK.

   Aquí NO hay auditoría de variedad de recetas, igual que en Luisa: el
   esquema de adulto son seis hojas fijas, no una hoja de deberes con bloques
   rotatorios. La variedad de este cuaderno la ponen las hojas generadas
   (calentamiento, agudeza, relajación, distintas cada semana por la semilla)
   y la hoja de "cómo se estudia", escrita pieza a pieza.

   A diferencia de Luisa, Mercè NO tiene tope de una sola hoja de estudio:
   su clase de hora y media (la más larga del proyecto) permite dos hojas
   cuando la pieza lo pide, así que ese límite no se comprueba aquí.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar

MODULOS = ['me_01_bambini', 'me_02_saints', 'me_03_friend', 'me_04_puff',
           'me_05_sonatina2', 'me_06_avignon', 'me_07_doremi', 'me_08_christmas',
           'me_09_silentnight', 'me_10_wewishyou', 'me_11_silentnight4h', 'me_12_panthere',
           'me_13_pianoman', 'me_14_belaciao', 'me_15_spring', 'me_16_greensleeves',
           'me_17_countingstars', 'me_18_largodvorak', 'me_19_grandfather', 'me_20_dream',
           'me_21_beauty', 'me_22_gladiator', 'me_23_rasputin', 'me_24_jailhouse',
           'me_25_toreador', 'me_26_furelise', 'me_27_nocturne']


def revisar_nivel(modulos):
    """Mercè está por encima de Luisa en la curva de niveles (cancion.CURVA),
       pero sigue siendo adulto sin tope de hojas de estudio. Aquí solo se
       comprueba lo que es una norma fija del cliente: formato adulto y el
       esquema mínimo del dosier presente en las 27 piezas."""
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
