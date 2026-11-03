# -*- coding: utf-8 -*-
"""El recuadro de MUSOL MISOL, el buho del curso de Pekes.

   Es un recuadro mas del cuaderno, de la misma familia que "La clave de todo"
   de las hojas al piano (fondo calido, filete ocre a la izquierda), con el
   buho dentro. Se usa como un bloque normal en `hoja_piano` y `hoja_deberes`
   (tipo 'misol') y en `hoja_teoria`.

   El buho es el del Canva original del cliente, recortado de la portada de
   su dosier "NIVEL PEKES" (ver `assets/pekes_owl/`): lo pidio asi, porque
   ya se veia bien y es el personaje que los ninos conocen.
"""
import os

from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader

from portada import MARGIN, CONTENT_W, NAVY, ACCENT, _wrap
from hoja_deberes import _lineas_que_ocupa

WARM = HexColor('#F4EFE3')
_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'pekes_owl')
_IMG = {}


def _img(pose):
    if pose not in _IMG:
        _IMG[pose] = ImageReader(os.path.join(_DIR, 'owl_%s_color.png' % pose))
    return _IMG[pose]


def dibujar_buho(c, x, y, alto, pose='normal'):
    """El buho con la esquina inferior izquierda en (x, y). Devuelve su ancho."""
    img = _img(pose)
    iw, ih = img.getSize()
    ancho = alto * iw / float(ih)
    c.drawImage(img, x, y, ancho, alto, mask='auto')
    return ancho


def caja_misol(c, y, texto, etiqueta='MUSOL MISOL DICE', pose='normal',
               alto_buho=66.0, size=9.4):
    leading = size * 1.32
    iw, ih = _img(pose).getSize()
    ancho_buho = alto_buho * iw / float(ih)
    tx = MARGIN + 16 + ancho_buho + 14
    inner = MARGIN + CONTENT_W - 14 - tx
    h_texto = 30 + leading * _lineas_que_ocupa(texto, size, inner)
    h = max(alto_buho + 14, h_texto)

    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    dibujar_buho(c, MARGIN + 14, y - h + (h - alto_buho) / 2.0, alto_buho, pose)

    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(ACCENT)
    ty = y - (h - h_texto) / 2.0
    c.drawString(tx, ty - 15, etiqueta)
    _wrap(c, texto, tx, ty - 29, 'DejaVuSans', size, inner, leading, NAVY)
    return y - h - 10
