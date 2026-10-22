# -*- coding: utf-8 -*-
"""Clona una peça ja mesurada (ms_/ab_/mp_) per a un altre alumne quan la partitura és byte a byte la mateixa.
   Us: python3 clonar_spec.py <origen.py> <prefix_nou> <num> <Nom> [mes]
   Canvia num, el nom i el numero del kicker, el mes i el titol de la docstring; la resta (cortes, burbujas,
   textos) es conserva perque descriu la mateixa partitura."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lo_comun import MESES


def clonar(origen, prefix, num, nom, mes=None):
    s = open(origen, encoding='utf-8').read()
    s = re.sub(r'num=\d+,', 'num=%d,' % num, s, count=1)
    s = re.sub(r"kicker=(['\"])[A-Za-zÀ-ÿ]+ · peça \d+ ·", lambda m: "kicker=%s%s · peça %d ·" % (m.group(1), nom, num), s, count=1)
    s = re.sub(r"mes=(['\"])[^'\"]*\1", "mes='%s'" % (mes or MESES[num]), s, count=1)
    s = re.sub(r'"""Peça \d+ ·', '"""Peça %d ·' % num, s, count=1)
    s = s.replace("TEST_", "TEST_%s_" % prefix)
    base = os.path.basename(origen)
    resto = re.sub(r'^[a-z]+_\d+_', '', base)
    dst = os.path.join(os.path.dirname(origen), '%s_%02d_%s' % (prefix, num, resto))
    open(dst, 'w', encoding='utf-8').write(s)
    return dst


if __name__ == '__main__':
    print(clonar(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else None))
