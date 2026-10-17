# -*- coding: utf-8 -*-
"""El Quadern del Pianista · PEKES — muntatge del llibre.

   python3 nens_llibre.py            -> ../output/Quadern_Pekes.pdf  (tot el que hi ha fet: tanda 1 = portada + capítols 1-3)
   python3 nens_llibre.py --prova    -> només una prova ràpida de les 4 primeres pàgines

   Cada tema ocupa 2 pàgines: `tN_teoria` i `tN_jocs` (ho dicta nens_pla.py).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nens_pla as pla                                           # noqa: E402
from nens_tclas import ManoCanvas, W, H                          # noqa: E402
import nens_front as front                                       # noqa: E402
import nens_t01 as c1                                            # noqa: E402
import nens_t02 as c2                                            # noqa: E402
import nens_t03 as c3                                            # noqa: E402

OUT = os.path.join(HERE, '..', 'output', 'Quadern_Pekes.pdf')

PAGINES = [front.portada, front.presentacio, front.com_sus, front.index]
for n in range(1, 14):
    mod = c1 if n <= 4 else (c2 if n <= 7 else c3)
    PAGINES += [getattr(mod, 't%d_teoria' % n), getattr(mod, 't%d_jocs' % n)]


def main(sortida=OUT, prova=False):
    os.makedirs(os.path.dirname(sortida), exist_ok=True)
    c = ManoCanvas(sortida, pagesize=(W, H), seed=5, amp=0.0)
    c.setTitle('El Quadern del Pianista · PEKES')
    c.setAuthor('T-Clas')
    llista = PAGINES[:4] if prova else PAGINES
    for f in llista:
        f(c)
    c.save()
    print('generat', sortida, len(llista), 'pàgines')


if __name__ == '__main__':
    main(prova='--prova' in sys.argv)
