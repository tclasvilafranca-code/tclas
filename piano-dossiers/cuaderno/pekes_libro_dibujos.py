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
LIGHT = HexColor('#E9E9E9')
MID = HexColor('#C9C9C9')
DARK = HexColor('#8A8A8A')


def _rr(c, x, y, w, h, r, fill, stroke=INK, lw=2.6):
    c.setLineWidth(lw)
    c.setStrokeColor(stroke)
    c.setFillColor(fill)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1)


def _teclado_bn(c, x, y, w, h, n_blancas=13, resaltar=None):
    ww = w / n_blancas
    c.setStrokeColor(INK)
    c.setLineWidth(1.8)
    for i in range(n_blancas):
        c.setFillColor(PAPER)
        c.roundRect(x + i * ww + 0.5, y, ww - 1, h, ww * 0.16, fill=1, stroke=1)
        if resaltar == i:
            c.setFillColor(INK)
            c.circle(x + (i + 0.5) * ww, y + h * 0.16, ww * 0.26, fill=1, stroke=0)
    c.setFillColor(INK)
    for i in range(n_blancas - 1):
        if i % 7 in (0, 1, 3, 4, 5):
            bx = x + (i + 1) * ww - ww * 0.19
            c.roundRect(bx, y + h * 0.42, ww * 0.38, h * 0.58, ww * 0.08, fill=1, stroke=0)
    return ww


def _etiqueta(c, px, py, num, radio=12.0):
    c.setFillColor(PAPER)
    c.circle(px, py, radio + 2.2, fill=1, stroke=0)
    c.setFillColor(INK)
    c.circle(px, py, radio, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', radio * 1.05)
    c.setFillColor(PAPER)
    c.drawCentredString(px, py - radio * 0.36, str(num))


def piano_partes(c, x, y, w, h, **_k):
    """Un piano "de cuento", con sombra y relleno gris suave en vez del
       estilo plano-de-plano anterior -- se acerca al look de las pegatinas
       de Canva (sombreado simple, esquinas muy redondeadas) sin perder la
       tinta negra pura que pide el cliente."""
    cx = x + w / 2.0
    body_w, body_h = w * 0.80, h * 0.42
    bx, by = x + (w - body_w) / 2.0, y + h * 0.30

    # sombra -- el mismo truco de las pegatinas: una silueta gris, un pelin
    # desplazada, detras de la forma principal
    sh = w * 0.012
    c.setFillColor(MID)
    c.roundRect(bx + sh, by - sh, body_w, body_h, 18, fill=1, stroke=0)

    _rr(c, bx, by, body_w, body_h, 18, LIGHT)

    lid_w, lid_h = body_w * 0.88, h * 0.12
    lx, ly = bx + body_w * 0.06, by + body_h
    c.setFillColor(MID)
    c.roundRect(lx + sh, ly - sh, lid_w, lid_h, 10, fill=1, stroke=0)
    _rr(c, lx, ly, lid_w, lid_h, 10, LIGHT)
    # brillo del "cristal" de la tapa
    c.setFillColor(PAPER)
    c.ellipse(lx + lid_w * 0.08, ly + lid_h * 0.30, lx + lid_w * 0.34, ly + lid_h * 0.85)

    atril_w, atril_h = w * 0.15, h * 0.09
    ax, ay = cx - atril_w / 2.0, ly + lid_h
    _rr(c, ax, ay, atril_w, atril_h, 7, DARK, lw=2.2)

    kb_h = h * 0.17
    kb_w = body_w * 0.90
    kx, ky = bx + body_w * 0.05, by - kb_h * 0.55
    c.setFillColor(MID)
    c.roundRect(kx + sh * 0.6, ky - sh * 0.6, kb_w, kb_h, 10, fill=1, stroke=0)
    c.setStrokeColor(INK)
    c.setLineWidth(2.6)
    c.setFillColor(INK)
    c.roundRect(kx, ky, kb_w, kb_h, 10, fill=1, stroke=1)
    _teclado_bn(c, kx + 4, ky + 4, kb_w - 8, kb_h - 8, n_blancas=13)

    leg_w = w * 0.034
    c.setFillColor(DARK)
    c.setStrokeColor(INK)
    c.setLineWidth(2.0)
    for lx2 in (bx + body_w * 0.08, bx + body_w * 0.5 - leg_w / 2.0,
                bx + body_w * 0.92 - leg_w):
        c.roundRect(lx2, y, leg_w, by - y, leg_w * 0.4, fill=1, stroke=1)

    pw, ph = w * 0.05, h * 0.03
    c.setFillColor(PAPER)
    c.setStrokeColor(INK)
    c.setLineWidth(1.8)
    c.roundRect(cx - pw / 2.0, y, pw, ph, ph * 0.4, fill=1, stroke=1)

    for num, px, py in (
        (1, kx + kb_w * 0.22, ky + kb_h * 0.22),
        (2, kx + kb_w * 0.40, ky + kb_h * 0.80),
        (3, lx + lid_w * 0.5, ly + lid_h * 0.55),
        (4, ax + atril_w * 0.5, ay + atril_h * 0.5),
        (5, cx, y + ph * 0.5 + 12),
        (6, bx + body_w * 0.08 + leg_w / 2.0, y + (by - y) * 0.45),
        (7, bx + body_w * 0.5, by + body_h * 0.5),
    ):
        _etiqueta(c, px, py, num, radio=13)


_FUNCIONES = {
    'piano_partes': piano_partes,
}


def dibujar(c, clave, x, y, w, h, params=None):
    if clave is None:
        return
    _FUNCIONES[clave](c, x, y, w, h, **(params or {}))
