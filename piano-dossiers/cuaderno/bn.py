# -*- coding: utf-8 -*-
"""Mode blanc i negre per imprimir: BN=1 converteix tots els colors dibuixats amb reportlab a grisos (amb mes contrast)
   i els fons clars a blanc. S'activa amb `bn.instalar()` abans de crear cap Canvas (mayores_motor ho fa)."""
import os
from reportlab.lib.colors import Color
from reportlab.pdfgen import canvas as _cv

ACTIU = os.environ.get('BN', '') == '1'


def gris(col):
    r, g, b = col.red, col.green, col.blue
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    if lum > 0.965:
        v = 1.0                      # fons clars: blanc (estalvia tinta)
    elif lum > 0.86:
        v = 0.94                     # plafons lleugers
    else:
        v = lum * 0.82               # mes fosc perque el text blanc i els filets es llegeixin
    return Color(v, v, v, alpha=getattr(col, 'alpha', 1))


def _conv(arg):
    return gris(arg) if isinstance(arg, Color) else arg


def instalar():
    if not ACTIU or getattr(_cv.Canvas, '_bn_instalat', False):
        return
    for nom in ('setFillColor', 'setStrokeColor'):
        orig = getattr(_cv.Canvas, nom)

        def f(self, aColor, alpha=None, _o=orig):
            return _o(self, _conv(aColor), alpha) if alpha is not None else _o(self, _conv(aColor))
        setattr(_cv.Canvas, nom, f)
    for nom, base in (('setFillColorRGB', 'setFillColor'), ('setStrokeColorRGB', 'setStrokeColor')):
        orig = getattr(_cv.Canvas, base)

        def g(self, r, gg, b, alpha=None, _o=orig):
            return _o(self, Color(r, gg, b, alpha=1 if alpha is None else alpha))
        setattr(_cv.Canvas, nom, g)
    _cv.Canvas._bn_instalat = True
