# -*- coding: utf-8 -*-
"""El Quadern del Pianista · PEKES — muntatge del llibre.

   python3 nens_llibre.py            -> ../output/Quadern_Pekes.pdf  (el llibre sencer: 34 temes + annexos)
   python3 nens_llibre.py --prova    -> només una prova ràpida de les 4 primeres pàgines

   Cada tema ocupa 2 pàgines: `tN_teoria` i `tN_jocs` (ho dicta nens_pla.py).
"""
import os
import sys
if os.environ.get('BN') == '1':          # versio per imprimir en blanc i negre
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import bn
    bn.instalar()

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nens_pla as pla                                           # noqa: E402
from nens_tclas import ManoCanvas, W, H                          # noqa: E402
import nens_front as front                                       # noqa: E402
import nens_t01 as c1                                            # noqa: E402
import nens_t02 as c2                                            # noqa: E402
import nens_t03 as c3                                            # noqa: E402
import nens_t04 as c4                                            # noqa: E402
import nens_t05 as c5                                            # noqa: E402
import nens_t06 as c6                                            # noqa: E402
import nens_t07 as c7                                            # noqa: E402
import nens_annex as an                                          # noqa: E402
import nens_x01 as x1                                            # noqa: E402

OUT = os.path.join(HERE, '..', 'output', 'Quadern_Pekes_BN.pdf' if os.environ.get('BN') == '1' else 'Quadern_Pekes.pdf')

MODULS = {range(1, 5): c1, range(5, 8): c2, range(8, 14): c3, range(14, 20): c4, range(20, 24): c5, range(24, 31): c6,
          range(31, 35): c7}


def _mod(n):
    for r, m in MODULS.items():
        if n in r:
            return m


PAGINES = [front.portada, front.presentacio, front.com_sus, front.index]
for kind, key in pla.SEQ:
    if kind == 'tema':
        PAGINES += [getattr(_mod(key), 't%d_teoria' % key), getattr(_mod(key), 't%d_jocs' % key)]
    elif kind == 'extra':
        PAGINES += [getattr(x1, 'x_' + key)]
    else:
        PAGINES += [getattr(x1, 'repas%d' % key)]
PAGINES += [an.pautes_1, an.pautes_2]


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
