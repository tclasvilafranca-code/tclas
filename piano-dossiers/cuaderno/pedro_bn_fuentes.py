# -*- coding: utf-8 -*-
"""Genera students/pedro/source_bn/: las partituras con color (clipart de Gradimi...) pasadas a grises a 200 ppi.
   Las que ya son en blanco y negro se copian tal cual (siguen siendo vectoriales)."""
import os, shutil, sys
import pymupdf
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'students', 'pedro', 'source')
DST = os.path.join(HERE, '..', 'students', 'pedro', 'source_bn')


def tiene_color(page):
    pm = page.get_pixmap(dpi=40)
    s = pm.samples
    n = pm.n
    for i in range(0, len(s) - n, n * 3):
        r, g, b = s[i], s[i + 1], s[i + 2]
        if max(r, g, b) - min(r, g, b) > 28:
            return True
    return False


os.makedirs(DST, exist_ok=True)
for f in sorted(os.listdir(SRC)):
    if not f.endswith('.pdf'):
        continue
    d = pymupdf.open(os.path.join(SRC, f))
    if not any(tiene_color(p) for p in d):
        shutil.copy(os.path.join(SRC, f), os.path.join(DST, f))
        print(f, 'ya en B/N')
        continue
    out = pymupdf.open()
    for p in d:
        pm = p.get_pixmap(dpi=200, colorspace=pymupdf.csGRAY)
        np_ = out.new_page(width=p.rect.width, height=p.rect.height)
        np_.insert_image(np_.rect, pixmap=pm)
    out.save(os.path.join(DST, f), deflate=True)
    print(f, 'pasada a grises')
