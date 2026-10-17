# -*- coding: utf-8 -*-
"""Pasa las comprobaciones obligatorias a las 19 piezas de Luisa.

   Compases, márgenes, material repetido entre hojas, altura final de cada hoja
   y texto que no cabe en su caja: lo de siempre, y todo tiene que decir OK.

   Aquí NO hay auditoría de variedad de recetas, y no es un olvido. La variedad
   de este cuaderno la ponen las hojas generadas —calentamiento, agudeza visual
   y relajación, distintas cada semana por la semilla— y la hoja de "cómo se
   estudia", que se escribe pieza a pieza. Luisa no lleva hoja de deberes con
   bloques rotatorios: el esquema de adulto que decidió el cliente son seis
   hojas, y ninguna de ellas es esa.

   Lo que sí se comprueba aparte, y es obligatorio antes de montar el álbum, es
   `cruzar_luisa.py`: dos de sus partituras son el mismo archivo que las de
   otros alumnos.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))

from cancion import auditar

MODULOS = ['lu_01_bambini', 'lu_02_beginner', 'lu_03_sonatina2', 'lu_04_friend',
           'lu_05_puff', 'lu_06_dream', 'lu_07_christmas', 'lu_08_silent',
           'lu_09_spring', 'lu_10_titanic', 'lu_11_pianoman', 'lu_12_panthere',
           'lu_13_belaciao', 'lu_14_heart', 'lu_15_greensleeves', 'lu_16_chimchim',
           'lu_17_rasputin', 'lu_18_furelise', 'lu_19_nocturne']


def revisar_nivel(modulos):
    """El nivel de Luisa es el más bajo del proyecto y tiene que seguir siéndolo.

       Dos cosas que se han decidido y que un descuido puede deshacer sin que
       ningún otro auditor se entere: que todas las piezas vayan de iniciación,
       y que ninguna lleve DOS hojas de "cómo se estudia". Una sola por pieza es
       parte del encargo —*"poquito pero bien"*—, no una casualidad."""
    fallos = []
    for mod in modulos:
        cfg = __import__(mod).CANCION
        if cfg.get('nivel') != 'iniciación':
            fallos.append('%s: nivel %r, tendría que ser iniciación' % (mod, cfg.get('nivel')))
        if cfg.get('piano2'):
            fallos.append('%s: lleva dos hojas de "cómo se estudia"; Luisa lleva una' % mod)
        if cfg.get('formato') != 'adulto':
            fallos.append('%s: formato %r, tendría que ser adulto' % (mod, cfg.get('formato')))
        pasos = [b for b in cfg['piano1']['bloques'] if b.get('num')]
        if len(pasos) > 3:
            fallos.append('%s: %d pasos al piano; el tope de Luisa son 3' % (mod, len(pasos)))
    print('\n  nivel · %d piezas · iniciación, una hoja de estudio, tres pasos · %s'
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
