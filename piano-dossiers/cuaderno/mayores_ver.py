# -*- coding: utf-8 -*-
"""Uso: python3 mayores_ver.py <pdf en eva_sc/source> [dpi]  -> /tmp/v_<n>.png con las y de los huecos."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import mayores_motor as m
from PIL import Image
pdf = os.path.join(m.SRCDIR, sys.argv[1])
r = m.huecos(pdf, '/tmp/v_%d.png')
print([(p, y, l) for (p, y, l) in r if l >= 4])
n = len(set(p for p, _, _ in r))
ims = [Image.open('/tmp/v_%d.png' % i) for i in range(1, n + 1)]
for g in range(0, n, 3):
    seg = ims[g:g + 3]
    w = sum(i.width for i in seg)
    h = max(i.height for i in seg)
    mm = Image.new('RGB', (w, h), 'white')
    x = 0
    for im in seg:
        mm.paste(im, (x, 0)); x += im.width
    mm.save('/tmp/v_m%d.png' % (g // 3))
print('montajes', (n + 2) // 3)
