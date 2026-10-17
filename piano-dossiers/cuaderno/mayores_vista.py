# -*- coding: utf-8 -*-
"""Uso: python3 mayores_vista.py <pdf> <desde> <hasta> [dpi] -> /tmp/vista_<pdf>/vista.png (paginas en fila)"""
import sys, subprocess, glob, os
from PIL import Image
pdf, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
TAG = os.path.splitext(os.path.basename(pdf))[0][:24]
D = '/tmp/vista_' + TAG
os.makedirs(D, exist_ok=True)
dpi = sys.argv[4] if len(sys.argv) > 4 else '70'
for f in glob.glob(D + '/vv-*.png'):
    os.remove(f)
subprocess.run(['pdftoppm', '-r', dpi, '-png', '-f', str(a), '-l', str(b), pdf, D + '/vv'], check=True)
fs = sorted(glob.glob(D + '/vv-*.png'))
ims = [Image.open(f) for f in fs]
w, h = ims[0].size
cols = min(len(ims), 4)
rows = (len(ims) + cols - 1) // cols
m = Image.new('RGB', (w * cols, h * rows), 'white')
for i, im in enumerate(ims):
    m.paste(im, ((i % cols) * w, (i // cols) * h))
m.save(D + '/vista.png')
print(D + '/vista.png', m.size)
