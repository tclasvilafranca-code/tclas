# -*- coding: utf-8 -*-
"""Prepara les partitures de Lola: pinta les notes (colorear_notas) i deixa els PDF amb noms
   normalitzats a students/lola/source/. Les partitures NO es versionen.
   Us: python3 lola_preparar.py <carpeta_amb_els_PDF_de_Drive_de_Lola>"""
import glob
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from colorear_notas import colorear

# (fragment del nom a Drive, nom final, tapar imatges decoratives)
FONTS = [('pTwinkle', 'twinkle', False), ('pAlouette', 'alouette', True), ('pSaints', 'saints', True),
         ('pOde', 'ode', True), ('clementine', 'clementine', False), ('MyBonnie', 'bonnie', False),
         ('puff-the-magic', 'puff', False), ('youve-got-a-friend', 'friend', False),
         ('panthere', 'panthere', True), ('PRIMAVERA', 'primavera', False),
         ('i-have-a-dream', 'dream', False), ('gladiator', 'gladiator', False),
         ('perfect-ed', 'perfect', False), ('spring-easy', 'spring', False),
         ('nocturne', 'nocturne', False), ('piano-man', 'pianoman', False)]


def main(origen, bn=False):
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'students', 'lola', 'source_bn' if bn else 'source')
    os.makedirs(dst, exist_ok=True)
    arx = sorted(glob.glob(os.path.join(origen, '*.pdf')))
    for frag, nom, sin in FONTS:
        f = [a for a in arx if frag in os.path.basename(a)]
        if not f:
            print('FALTA', frag)
            continue
        r = colorear(f[-1], os.path.join(dst, nom + '.pdf'), sin, pintar=not bn)
        print(nom, sum(x[2] for x in r), 'notes')


if __name__ == '__main__':
    main(sys.argv[1], '--bn' in sys.argv)
