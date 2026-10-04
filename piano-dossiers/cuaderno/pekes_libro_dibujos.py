# -*- coding: utf-8 -*-
"""Diagramas en blanco y negro para EL LIBRO DE PEKES (v2).

   `pekes_dibujos.py` es la libreria de la primera version (con color:
   NAVY, ACCENT, los colores Kodaly de las notas...) y sigue viva para el
   `build_pekes.py` antiguo. Esta es la version "solo tinta negra" que pide
   el cliente para el libro nuevo: trazo grueso, relleno blanco, estilo
   libro ilustrado -- nunca un bloque de color solido.
"""
from reportlab.lib.colors import HexColor, white

INK = HexColor('#1A1A1A')
PAPER = white


def _teclado_bn(c, x, y, w, h, n_blancas=13, resaltar=None):
    ww = w / n_blancas
    c.setStrokeColor(INK)
    c.setLineWidth(1.6)
    for i in range(n_blancas):
        c.setFillColor(PAPER)
        c.rect(x + i * ww, y, ww, h, fill=1, stroke=1)
        if resaltar == i:
            c.setFillColor(INK)
            c.circle(x + (i + 0.5) * ww, y + h * 0.16, ww * 0.26, fill=1, stroke=0)
    c.setFillColor(INK)
    for i in range(n_blancas - 1):
        if i % 7 in (0, 1, 3, 4, 5):
            bx = x + (i + 1) * ww - ww * 0.19
            c.rect(bx, y + h * 0.42, ww * 0.38, h * 0.58, fill=1, stroke=0)
    return ww


def _etiqueta(c, px, py, num, radio=11.0):
    c.setFillColor(INK)
    c.circle(px, py, radio, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', radio * 1.05)
    c.setFillColor(PAPER)
    c.drawCentredString(px, py - radio * 0.36, str(num))


def piano_partes(c, x, y, w, h, **_k):
    cx = x + w / 2.0
    body_w, body_h = w * 0.80, h * 0.42
    bx, by = x + (w - body_w) / 2.0, y + h * 0.30

    c.setLineWidth(2.4)
    c.setStrokeColor(INK)
    c.setFillColor(PAPER)
    c.roundRect(bx, by, body_w, body_h, 9, fill=1, stroke=1)

    lid_w, lid_h = body_w * 0.88, h * 0.12
    lx, ly = bx + body_w * 0.06, by + body_h
    c.roundRect(lx, ly, lid_w, lid_h, 5, fill=1, stroke=1)

    atril_w, atril_h = w * 0.15, h * 0.09
    ax, ay = cx - atril_w / 2.0, ly + lid_h
    c.rect(ax, ay, atril_w, atril_h, fill=1, stroke=1)

    kb_h = h * 0.17
    kb_w = body_w * 0.90
    kx, ky = bx + body_w * 0.05, by - kb_h * 0.55
    _teclado_bn(c, kx, ky, kb_w, kb_h, n_blancas=13)

    leg_w = w * 0.028
    c.setFillColor(INK)
    for lx2 in (bx + body_w * 0.08, bx + body_w * 0.5 - leg_w / 2.0,
                bx + body_w * 0.92 - leg_w):
        c.rect(lx2, y, leg_w, by - y, fill=1, stroke=0)

    pw, ph = w * 0.045, h * 0.025
    c.setFillColor(PAPER)
    c.setStrokeColor(INK)
    c.setLineWidth(1.6)
    c.rect(cx - pw / 2.0, y, pw, ph, fill=1, stroke=1)

    for num, px, py in (
        (1, kx + kb_w * 0.22, ky + kb_h * 0.22),
        (2, kx + kb_w * 0.40, ky + kb_h * 0.80),
        (3, lx + lid_w * 0.5, ly + lid_h * 0.55),
        (4, ax + atril_w * 0.5, ay + atril_h * 0.5),
        (5, cx, y + ph * 0.5 + 12),
        (6, bx + body_w * 0.08 + leg_w / 2.0, y + (by - y) * 0.45),
        (7, bx + body_w * 0.5, by + body_h * 0.5),
    ):
        _etiqueta(c, px, py, num, radio=12.5)


_FUNCIONES = {
    'piano_partes': piano_partes,
}


def dibujar(c, clave, x, y, w, h, params=None):
    if clave is None:
        return
    _FUNCIONES[clave](c, x, y, w, h, **(params or {}))
