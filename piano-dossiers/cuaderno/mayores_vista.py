# -*- coding: utf-8 -*-
"""Uso: python3 mayores_vista.py <pdf> <desde> <hasta> [dpi] -> /tmp/vista.png (paginas en fila)"""
import sys, subprocess, glob, os
from PIL import Image
pdf, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
dpi = sys.argv[4] if len(sys.argv) > 4 else '70'
for f in glob.glob('/tmp/vv-*.png'):
    os.remove(f)
subprocess.run(['pdftoppm', '-r', dpi, '-png', '-f', str(a), '-l', str(b), pdf, '/tmp/vv'], check=True)
fs = sorted(glob.glob('/tmp/vv-*.png'))
ims = [Image.open(f) for f in fs]
w, h = ims[0].size
cols = min(len(ims), 4)
rows = (len(ims) + cols - 1) // cols
m = Image.new('RGB', (w * cols, h * rows), 'white')
for i, im in enumerate(ims):
    m.paste(im, ((i % cols) * w, (i // cols) * h))
m.save('/tmp/vista.png')
print(m.size)
