# -*- coding: utf-8 -*-
"""La libreria de dibujos del CURSO PEKES. Un dibujo por concepto, no por
   semana: muchas semanas comparten el mismo tipo de diagrama (una nota de
   color sobre un pentagrama, una figura sola, un silencio...), asi que aqui
   vive una funcion por concepto y `pekes_datos.py` dice cual usar y con que
   parametros.

   Todo se dibuja con el motor real del proyecto (notation.py para
   pentagramas/claves/notas, juegos_comun.py para figuras/silencios/simbolos
   sueltos) -- nada de clipart. Cada funcion recibe la caja donde tiene que
   caber: (x, y) es la esquina inferior izquierda, (w, h) el ancho y alto
   disponibles. Ninguna dibuja fuera de esa caja.
"""
import os
import sys

from reportlab.lib.colors import HexColor, white

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import notation as nt                                                # noqa: E402
from notation import (draw_staff, draw_clef, note_y, draw_ledger,     # noqa: E402
                      ledger_lines_needed, draw_barline)
from portada import NAVY, NAVY_SOFT, INK, MUTED, RULE, ACCENT          # noqa: E402
from juegos_comun import figura_en_caja, simbolo                       # noqa: E402
from pekes_datos import NOTAS_COLOR, ORDEN_NOTAS                       # noqa: E402

MADERA = HexColor('#C9A15A')
MADERA_OSC = HexColor('#8C6A34')
TECLA_SOMBRA = HexColor('#D8D2C2')


# --------------------------------------------------------------------------
# piezas sueltas, reutilizadas por varios dibujos
# --------------------------------------------------------------------------
def _etiqueta(c, px, py, num, radio=8.0):
    """Un numero en circulo navy -- el callout de un diagrama etiquetado."""
    c.setFillColor(NAVY)
    c.circle(px, py, radio, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', radio)
    c.setFillColor(white)
    c.drawCentredString(px, py - radio * 0.36, str(num))


def _teclado(c, x, y, w, h, n_blancas=14, resaltar=None):
    """Un teclado horizontal de piano, blancas + negras en su patron real.
       `resaltar` es un indice de tecla blanca (0-based) que se pinta de
       color para marcarla (el Do central, p.ej.)."""
    ww = w / n_blancas
    c.setStrokeColor(INK)
    c.setLineWidth(0.8)
    for i in range(n_blancas):
        c.setFillColor(HexColor('#FBEFD0') if resaltar == i else white)
        c.rect(x + i * ww, y, ww, h, fill=1, stroke=1)
    c.setFillColor(INK)
    for i in range(n_blancas - 1):
        if i % 7 in (0, 1, 3, 4, 5):
            bx = x + (i + 1) * ww - ww * 0.19
            c.rect(bx, y + h * 0.42, ww * 0.38, h * 0.58, fill=1, stroke=0)
    return ww


def _pentagrama(c, x, y, w, h, gap=None, clef='treble', frac_y=0.55):
    """Un pentagrama centrado en la caja, con su clave. Devuelve
       (staff_bottom_y, staff_top_y, gap, x0) para que quien llama coloque
       notas encima con `note_y`."""
    if gap is None:
        gap = min(h / 10.0, 15.0)
    top_y = y + h * frac_y + gap * 2
    x0 = x + w * 0.14
    ys = draw_staff(c, x0, top_y, w * 0.82, gap=gap)
    draw_clef(c, x0 + gap * 0.3, ys[-1], gap, clef=clef)
    return ys[-1], ys[0], gap, x0 + gap * 4.4


# --------------------------------------------------------------------------
# BLOQUE 1 · el piano y las manos
# --------------------------------------------------------------------------
def piano_partes(c, x, y, w, h, **_k):
    cx = x + w / 2.0
    body_w, body_h = w * 0.80, h * 0.42
    bx, by = x + (w - body_w) / 2.0, y + h * 0.30
    c.setFillColor(HexColor('#EDE6D6'))
    c.setStrokeColor(INK)
    c.setLineWidth(1.1)
    c.roundRect(bx, by, body_w, body_h, 9, fill=1, stroke=1)

    lid_w, lid_h = body_w * 0.88, h * 0.12
    lx, ly = bx + body_w * 0.06, by + body_h
    c.setFillColor(HexColor('#F7F2E7'))
    c.roundRect(lx, ly, lid_w, lid_h, 5, fill=1, stroke=1)

    atril_w, atril_h = w * 0.15, h * 0.09
    ax, ay = cx - atril_w / 2.0, ly + lid_h
    c.setFillColor(MADERA)
    c.rect(ax, ay, atril_w, atril_h, fill=1, stroke=1)

    kb_h = h * 0.17
    kb_w = body_w * 0.90
    kx, ky = bx + body_w * 0.05, by - kb_h * 0.55
    _teclado(c, kx, ky, kb_w, kb_h, n_blancas=13)

    leg_w = w * 0.028
    for lx2 in (bx + body_w * 0.08, bx + body_w * 0.5 - leg_w / 2.0,
                bx + body_w * 0.92 - leg_w):
        c.setFillColor(MADERA_OSC)
        c.rect(lx2, y, leg_w, by - y, fill=1, stroke=0)

    pw, ph = w * 0.045, h * 0.025
    c.setFillColor(HexColor('#8C8C8C'))
    c.rect(cx - pw / 2.0, y, pw, ph, fill=1, stroke=0)

    for num, px, py in (
        (1, kx + kb_w * 0.22, ky + kb_h * 0.22),
        (2, kx + kb_w * 0.40, ky + kb_h * 0.80),
        (3, lx + lid_w * 0.5, ly + lid_h * 0.55),
        (4, ax + atril_w * 0.5, ay + atril_h * 0.5),
        (5, cx, y + ph * 0.5 + 9),
        (6, bx + body_w * 0.08 + leg_w / 2.0, y + (by - y) * 0.45),
        (7, bx + body_w * 0.5, by + body_h * 0.5),
    ):
        _etiqueta(c, px, py, num, radio=9.5)


def manos_dedos(c, x, y, w, h, **_k):
    r = min(w, h) * 0.40
    for sgn, cx, nombre in ((-1, x + w * 0.27, 'MANO IZQUIERDA'),
                            (1, x + w * 0.73, 'MANO DERECHA')):
        cy = y + h * 0.56
        c.setFillColor(HexColor('#F3E9D4'))
        c.setStrokeColor(INK)
        c.setLineWidth(1.0)
        c.ellipse(cx - r * 0.9, cy - r * 0.62, cx + r * 0.9, cy + r * 0.62, fill=1, stroke=1)
        orden = range(1, 6) if sgn < 0 else range(5, 0, -1)
        n = 5
        for i, dedo in enumerate(orden):
            dx = cx + (i - (n - 1) / 2.0) * r * 0.42
            fy = cy + r * (0.55 + 0.12 * (1 - abs(i - (n - 1) / 2.0) / (n / 2.0)))
            c.setFillColor(white)
            c.setStrokeColor(INK)
            c.ellipse(dx - r * 0.15, cy - r * 0.1, dx + r * 0.15, fy, fill=1, stroke=1)
            c.setFillColor(NAVY)
            c.circle(dx, fy - r * 0.03, r * 0.16, fill=1, stroke=0)
            c.setFont('DejaVuSans-Bold', r * 0.22)
            c.setFillColor(white)
            c.drawCentredString(dx, fy - r * 0.03 - r * 0.08, str(dedo))
        c.setFont('DejaVuSans-Bold', 9)
        c.setFillColor(NAVY_SOFT)
        c.drawCentredString(cx, y + h * 0.08, nombre)


def grave_agudo(c, x, y, w, h, **_k):
    ww = _teclado(c, x + w * 0.08, y + h * 0.10, w * 0.84, h * 0.22, n_blancas=14)
    cx = x + w * 0.08 + (w * 0.84) / 2.0
    for sgn, nombre, cual in ((-1, 'GRAVE', 'mano izquierda'), (1, 'AGUDO', 'mano derecha')):
        tx = cx + sgn * w * 0.21
        c.setFillColor(ACCENT if sgn < 0 else NAVY)
        c.roundRect(tx - 46, y + h * 0.42, 92, 26, 6, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 11)
        c.setFillColor(white)
        c.drawCentredString(tx, y + h * 0.42 + 8.5, nombre)
        c.setFont('DejaVuSans', 8.4)
        c.setFillColor(MUTED)
        c.drawCentredString(tx, y + h * 0.42 - 12, cual)
        # flecha hacia el extremo correspondiente del teclado
        c.setStrokeColor(ACCENT if sgn < 0 else NAVY)
        c.setLineWidth(1.6)
        tex = x + w * 0.08 + (0.5 * ww if sgn < 0 else 13.5 * ww)
        c.line(tx, y + h * 0.42, tex, y + h * 0.32)


def do_central(c, x, y, w, h, **_k):
    n = 11
    kb_w, kb_h = w * 0.88, h * 0.34
    kx, ky = x + (w - kb_w) / 2.0, y + h * 0.22
    resaltar = n // 2
    _teclado(c, kx, ky, kb_w, kb_h, n_blancas=n, resaltar=resaltar)
    ww = kb_w / n
    cx_do = kx + (resaltar + 0.5) * ww
    c.setFont('DejaVuSans-Bold', 20)
    c.setFillColor(ACCENT)
    c.drawCentredString(cx_do, ky + kb_h + 26, '★')
    c.setFont('DejaVuSans-Bold', 12)
    c.setFillColor(NAVY)
    c.drawCentredString(cx_do, ky + kb_h + 6, 'DO')
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawCentredString(cx_do, ky - 16,
                        'el Do siempre está a la izquierda de las 2 teclas negras juntas')


# --------------------------------------------------------------------------
# BLOQUE 2 · el pentagrama
# --------------------------------------------------------------------------
def pentagrama_lineas(c, x, y, w, h, **_k):
    gap = min(h * 0.16, 24.0)
    bot, top, gap, _x0 = _pentagrama(c, x, y, w, h, gap=gap, frac_y=0.5)
    for i in range(5):
        ly = bot + i * gap
        c.setFont('DejaVuSans-Bold', 9)
        c.setFillColor(NAVY)
        c.drawRightString(x + w * 0.09, ly - 3.2, str(i + 1))
    for i in range(4):
        sy = bot + gap * (i + 0.5)
        c.setFillColor(HexColor('#E3DCC8'))
        c.rect(x + w * 0.12, sy - gap * 0.46, w * 0.80, gap * 0.92, fill=1, stroke=0)
    draw_staff(c, x + w * 0.12, top, w * 0.80, gap=gap)
    draw_clef(c, x + w * 0.14, bot, gap, clef='treble')


def linea_espacio(c, x, y, w, h, **_k):
    bot, top, gap, x0 = _pentagrama(c, x, y, w, h, frac_y=0.5)
    notas = [('línea', bot), ('espacio', bot + gap * 0.5),
             ('línea', bot + gap), ('espacio', bot + gap * 1.5)]
    paso = (w * 0.6) / (len(notas) - 1)
    for i, (tipo, ny) in enumerate(notas):
        cx = x0 + i * paso
        c.setFillColor(ACCENT)
        c.circle(cx, ny, gap * 0.42, fill=1, stroke=0)
        c.setFont('DejaVuSans', 8)
        c.setFillColor(MUTED)
        c.drawCentredString(cx, bot - gap * 1.6, tipo.upper()[0])


def agudo_grave_pentagrama(c, x, y, w, h, **_k):
    bot, top, gap, x0 = _pentagrama(c, x, y, w, h, frac_y=0.55)
    c.setFont('DejaVuSans-Bold', 9)
    c.setFillColor(NAVY)
    c.drawString(x0 - gap * 2, top + gap * 1.3, 'AGUDO')
    c.drawString(x0 - gap * 2, bot - gap * 1.8, 'GRAVE')
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.6)
    c.line(x0 - gap * 2.4, bot - gap * 0.5, x0 - gap * 2.4, top + gap * 0.5)
    _flecha_arriba(c, x0 - gap * 2.4, top + gap * 0.5)


def _flecha_arriba(c, px, py, r=4.2):
    c.setFillColor(ACCENT)
    p = c.beginPath()
    p.moveTo(px, py + r); p.lineTo(px - r, py - r); p.lineTo(px + r, py - r)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def repaso_pentagrama1(c, x, y, w, h, **_k):
    pentagrama_lineas(c, x, y, w, h * 0.78)
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(NAVY_SOFT)
    c.drawCentredString(x + w / 2.0, y + h * 0.92, 'AGUDO arriba · GRAVE abajo · 5 líneas, 4 espacios')


repaso_pentagrama2 = repaso_pentagrama1


def clave_sol_pasos(c, x, y, w, h, **_k):
    paso_w = w / 3.0
    gap = min(h * 0.11, 15.0)
    for i in range(3):
        px = x + i * paso_w
        bot, top, g, x0 = _pentagrama(c, px, y, paso_w, h, gap=gap, frac_y=0.5)
        if i >= 1:
            simbolo(c, x0 + g * 2, (bot + top) / 2.0, g * 1.5, 'clave_sol', NAVY)
        if i == 2:
            pass
        c.setFont('DejaVuSans-Bold', 9)
        c.setFillColor(ACCENT)
        c.drawCentredString(px + paso_w / 2.0, y + h * 0.08, 'PASO %d' % (i + 1))
    textos = ['rodea la línea del Sol', 'sube girando por el medio', 'cierra la clave al final']
    for i, t in enumerate(textos):
        c.setFont('DejaVuSans', 7.6)
        c.setFillColor(MUTED)
        c.drawCentredString(x + i * paso_w + paso_w / 2.0, y + h * 0.02, t)


def clave_guardiana(c, x, y, w, h, **_k):
    bot, top, gap, x0 = _pentagrama(c, x, y, w, h, frac_y=0.55)
    simbolo(c, x0 + gap * 0.3, (bot + top) / 2.0, gap * 1.6, 'clave_sol', NAVY)
    c.setFont('DejaVuSans', 9)
    c.setFillColor(MUTED)
    c.drawCentredString(x + w / 2.0, bot - gap * 1.8, 'sin clave, no sabemos qué nota es ninguna')


def pentagrama_completo(c, x, y, w, h, **_k):
    bot, top, gap, x0 = _pentagrama(c, x, y, w, h, frac_y=0.55)
    simbolo(c, x0 + gap * 0.3, (bot + top) / 2.0, gap * 1.6, 'clave_sol', NAVY)
    _nota_simple(c, x0 + gap * 7, bot, gap, 'C4', ACCENT)


def _nota_simple(c, cx, bot, gap, pitch, color):
    cy = note_y(bot, gap, pitch, clef='treble')
    for ly in ledger_lines_needed(bot, bot + gap * 4, cy, gap):
        draw_ledger(c, cx, ly, gap)
    c.setFillColor(color)
    c.setStrokeColor(INK)
    c.setLineWidth(1.1)
    c.circle(cx, cy, gap * 0.52, fill=1, stroke=1)


# --------------------------------------------------------------------------
# BLOQUE 3 · las siete notas
# --------------------------------------------------------------------------
def nota_color(c, x, y, w, h, nombre=None, **_k):
    pitch, color = NOTAS_COLOR[nombre]
    pent_h = h * 0.56
    pent_y = y + h - pent_h
    bot, top, gap, x0 = _pentagrama(c, x, pent_y, w, pent_h, frac_y=0.78)
    simbolo(c, x0 - gap * 2.3, (bot + top) / 2.0, gap * 1.5, 'clave_sol', NAVY)
    cx = x0 + (w * 0.6) / 2.0
    _nota_simple(c, cx, bot, gap, pitch, color)

    c.setFont('DejaVuSerif-Bold', 21)
    c.setFillColor(color)
    c.drawCentredString(x + w / 2.0, y + h * 0.30, nombre.capitalize())

    kb_w, kb_h = w * 0.7, h * 0.15
    kx = x + (w - kb_w) / 2.0
    ww = _teclado(c, kx, y, kb_w, kb_h, n_blancas=8)
    idx = ORDEN_NOTAS.index(nombre)
    c.setFillColor(color)
    c.circle(kx + (idx + 0.5) * ww, y + kb_h * 0.20, ww * 0.22, fill=1, stroke=0)


def mapa_notas(c, x, y, w, h, hasta='SI', **_k):
    bot, top, gap, x0 = _pentagrama(c, x, y, w, h, frac_y=0.5)
    simbolo(c, x0 - gap * 2.3, (bot + top) / 2.0, gap * 1.5, 'clave_sol', NAVY)
    idx_hasta = ORDEN_NOTAS.index(hasta)
    activas = ORDEN_NOTAS[:idx_hasta + 1]
    x1 = x0 + w * 0.06
    x2 = x + w * 0.96
    paso = (x2 - x1) / 6.0
    for i, nombre in enumerate(ORDEN_NOTAS):
        pitch, color = NOTAS_COLOR[nombre]
        cx = x1 + i * paso
        if nombre in activas:
            _nota_simple(c, cx, bot, gap, pitch, color)
            c.setFont('DejaVuSans-Bold', 8.6)
            c.setFillColor(color)
        else:
            cy = note_y(bot, gap, pitch, clef='treble')
            c.setStrokeColor(RULE)
            c.setLineWidth(1.1)
            c.circle(cx, cy, gap * 0.52, fill=0, stroke=1)
            c.setFont('DejaVuSans', 8.6)
            c.setFillColor(MUTED)
        c.drawCentredString(cx, bot - gap * 1.8, nombre.capitalize())


# --------------------------------------------------------------------------
# BLOQUE 4 · las figuras y el compas
# --------------------------------------------------------------------------
def figura_intro(c, x, y, w, h, clave='q', **_k):
    cx, cy = x + w / 2.0, y + h * 0.56
    lado = min(w * 0.5, h * 0.62)
    figura_en_caja(c, cx, cy, lado * 0.7, lado, clave, NAVY)
    from juegos_comun import FIGURAS
    nombre, beats, _ = FIGURAS[clave]
    c.setFont('DejaVuSans-Bold', 13)
    c.setFillColor(ACCENT)
    c.drawCentredString(cx, y + h * 0.10, '%s · %s tiempo%s' %
                        (nombre, str(beats).rstrip('0').rstrip('.') or '0',
                         '' if beats == 1 else 's'))


def tres_figuras(c, x, y, w, h, **_k):
    from juegos_comun import FIGURAS
    claves = ['w', 'h', 'q']
    paso = w / 3.0
    for i, clave in enumerate(claves):
        cx = x + i * paso + paso / 2.0
        cy = y + h * 0.56
        lado = min(paso * 0.55, h * 0.58)
        figura_en_caja(c, cx, cy, lado * 0.7, lado, clave, NAVY)
        nombre, beats, _ = FIGURAS[clave]
        c.setFont('DejaVuSans-Bold', 10.5)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, y + h * 0.08, '%s · %d' % (nombre, int(beats)))


def compas(c, x, y, w, h, **_k):
    gap = min(h * 0.22, 15.0)
    top_y = y + h * 0.62
    x0 = x + w * 0.08
    ys = draw_staff(c, x0, top_y, w * 0.86, gap=gap)
    draw_clef(c, x0 + gap * 0.3, ys[-1], gap, clef='treble')
    n_compases = 3
    paso = (w * 0.86 - gap * 5) / n_compases
    for i in range(n_compases + 1):
        bx = x0 + gap * 5 + i * paso
        draw_barline(c, bx, ys[0], ys[-1], final=(i == n_compases))
    for i in range(n_compases):
        cx = x0 + gap * 5 + (i + 0.5) * paso
        c.setFont('DejaVuSans-Bold', 9)
        c.setFillColor(MUTED)
        c.drawCentredString(cx, ys[-1] - gap * 1.8, 'compás %d' % (i + 1))


def repaso_figuras(c, x, y, w, h, **_k):
    tres_figuras(c, x, y, w, h * 0.62)
    compas(c, x, y + h * 0.60, w, h * 0.38)


def compositor(c, x, y, w, h, **_k):
    gap = min(h * 0.3, 14.0)
    top_y = y + h * 0.7
    x0 = x + w * 0.1
    draw_staff(c, x0, top_y, w * 0.8, gap=gap)
    draw_clef(c, x0 + gap * 0.3, top_y - gap * 4, gap, clef='treble')
    c.setFont('DejaVuSans', 9)
    c.setFillColor(MUTED)
    c.drawCentredString(x + w / 2.0, y + h * 0.18, '¿qué notas vas a usar en tu melodía?')


# --------------------------------------------------------------------------
# BLOQUE 5 · los silencios
# --------------------------------------------------------------------------
def silencio_intro(c, x, y, w, h, clave='Rq', **_k):
    cx, cy = x + w / 2.0, y + h * 0.56
    lado = min(w * 0.45, h * 0.6)
    figura_en_caja(c, cx, cy, lado * 0.7, lado, clave, NAVY)
    from juegos_comun import FIGURAS
    nombre, beats, _ = FIGURAS[clave]
    c.setFont('DejaVuSans-Bold', 12.5)
    c.setFillColor(ACCENT)
    c.drawCentredString(cx, y + h * 0.10, '%s · dura %d' %
                        (nombre.replace('silencio de ', 'SILENCIO DE ').upper(), int(beats)))


def silencio_repaso(c, x, y, w, h, **_k):
    claves = ['Rw', 'Rh', 'Rq']
    paso = w / 3.0
    from juegos_comun import FIGURAS
    for i, clave in enumerate(claves):
        cx = x + i * paso + paso / 2.0
        cy = y + h * 0.56
        lado = min(paso * 0.55, h * 0.56)
        figura_en_caja(c, cx, cy, lado * 0.6, lado, clave, NAVY)
        nombre, beats, _ = FIGURAS[clave]
        c.setFont('DejaVuSans-Bold', 9.5)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, y + h * 0.08, '%s · %d' % (nombre.replace('silencio de ', ''), int(beats)))


# --------------------------------------------------------------------------
# BLOQUE 6 · las plicas
# --------------------------------------------------------------------------
def plica_cola(c, x, y, w, h, **_k):
    claves = ['w', 'h', 'q']
    paso = w / 3.0
    for i, clave in enumerate(claves):
        cx = x + i * paso + paso / 2.0
        cy = y + h * 0.56
        lado = min(paso * 0.5, h * 0.58)
        figura_en_caja(c, cx, cy, lado * 0.65, lado, clave, NAVY)
        c.setFont('DejaVuSans-Bold', 9.5)
        c.setFillColor(ACCENT if clave == 'w' else NAVY_SOFT)
        c.drawCentredString(cx, y + h * 0.08, 'SIN plica' if clave == 'w' else 'CON plica')


def plica_arriba_abajo(c, x, y, w, h, **_k):
    bot, top, gap, x0 = _pentagrama(c, x, y, w, h, frac_y=0.55)
    mid = bot + gap * 2
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.0)
    c.setDash(3, 2)
    c.line(x0 - gap, mid, x0 + w * 0.6, mid)
    c.setDash()
    c.setFont('DejaVuSans', 8)
    c.setFillColor(ACCENT)
    c.drawString(x0 + w * 0.6 + 4, mid + 4, '3ª línea')

    from notation import draw_note
    # D4 queda claramente POR DEBAJO de la 3a linea (plica arriba) y B4 cae
    # EN la 3a linea misma (plica abajo) -- se fija la plica a mano, sin
    # comparar note_y contra `mid` por flotantes: en ese punto exacto el
    # redondeo puede ir a cualquiera de los dos lados.
    for i, (pitch, stem) in enumerate((('D4', 'up'), ('B4', 'down'))):
        cx = x0 + gap * 6 + i * gap * 10
        draw_note(c, cx, bot, top, gap, pitch, 'q', stem_dir=stem, clef='treble')
        c.setFont('DejaVuSans', 8)
        c.setFillColor(MUTED)
        c.drawCentredString(cx, bot - gap * 1.8, 'plica %s' % ('arriba' if stem == 'up' else 'abajo'))


def plica_dibujo_pasos(c, x, y, w, h, **_k):
    paso_w = w / 3.0
    textos = ['1· la cabeza en su sitio', '2· decide arriba o abajo', '3· dibuja la plica']
    for i in range(3):
        px = x + i * paso_w
        bot, top, gap, x0 = _pentagrama(c, px, y, paso_w, h, frac_y=0.5)
        from notation import draw_note
        if i >= 1:
            stem = 'up'
            draw_note(c, x0 + gap * 4, bot, top, gap, 'D4', 'q' if i == 2 else 'w',
                     stem_dir=stem, clef='treble')
        else:
            _nota_simple(c, x0 + gap * 4, bot, gap, 'D4', ACCENT)
        c.setFont('DejaVuSans', 7.6)
        c.setFillColor(MUTED)
        c.drawCentredString(px + paso_w / 2.0, y + h * 0.04, textos[i])


# --------------------------------------------------------------------------
# BLOQUE 7 · el gran repaso y el concierto
# --------------------------------------------------------------------------
def repaso_total(c, x, y, w, h, **_k):
    mapa_notas(c, x, y + h * 0.55, w, h * 0.45)
    tres_figuras(c, x, y, w * 0.5, h * 0.5)
    silencio_repaso(c, x + w * 0.5, y, w * 0.5, h * 0.5)


def concierto(c, x, y, w, h, **_k):
    top = y + h
    c.setStrokeColor(ACCENT)
    c.setLineWidth(2.2)
    c.roundRect(x + 8, y + 8, w - 16, h - 16, 10, fill=0, stroke=1)
    simbolo(c, x + w / 2.0, top - 18, min(w, h) * 0.072, 'clave_sol', ACCENT)
    c.setFont('DejaVuSerif-Bold', 15)
    c.setFillColor(NAVY)
    c.drawCentredString(x + w / 2.0, top - 44, 'MI PRIMER CONCIERTO')
    row_y = top - 64
    for campo in ('Pianista', 'Fecha', 'Partitura', 'Dedicado a'):
        c.setFont('DejaVuSans-Bold', 8.6)
        c.setFillColor(NAVY_SOFT)
        c.drawString(x + w * 0.12, row_y, campo.upper())
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.line(x + w * 0.32, row_y - 2, x + w * 0.88, row_y - 2)
        row_y -= 15.5


def diploma(c, x, y, w, h, **_k):
    c.setStrokeColor(ACCENT)
    c.setLineWidth(2.6)
    c.roundRect(x + 6, y + 6, w - 12, h - 12, 12, fill=0, stroke=1)
    c.setStrokeColor(RULE)
    c.setLineWidth(1.0)
    c.roundRect(x + 16, y + 16, w - 32, h - 32, 8, fill=0, stroke=1)
    simbolo(c, x + w / 2.0, y + h * 0.90, min(w, h) * 0.10, 'clave_sol', ACCENT)
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawCentredString(x + w / 2.0, y + h * 0.60, 'DIPLOMA MUSICAL')
    c.setFont('DejaVuSans', 10.5)
    c.setFillColor(MUTED)
    c.drawCentredString(x + w / 2.0, y + h * 0.50, '¡Felicidades, gran pianista!')
    for i, campo in enumerate(['Nombre', 'Curso']):
        ly = y + h * 0.36 - i * h * 0.12
        c.setFont('DejaVuSans-Bold', 9.5)
        c.setFillColor(NAVY_SOFT)
        c.drawCentredString(x + w / 2.0, ly, campo.upper())
        c.setStrokeColor(RULE)
        c.line(x + w * 0.2, ly - 14, x + w * 0.8, ly - 14)


# --------------------------------------------------------------------------
# el despachador
# --------------------------------------------------------------------------
_FUNCIONES = {
    'piano_partes': piano_partes, 'manos_dedos': manos_dedos,
    'grave_agudo': grave_agudo, 'do_central': do_central,
    'pentagrama_lineas': pentagrama_lineas, 'linea_espacio': linea_espacio,
    'agudo_grave_pentagrama': agudo_grave_pentagrama,
    'repaso_pentagrama1': repaso_pentagrama1, 'repaso_pentagrama2': repaso_pentagrama2,
    'clave_sol_pasos': clave_sol_pasos, 'clave_guardiana': clave_guardiana,
    'pentagrama_completo': pentagrama_completo,
    'nota_color': nota_color, 'mapa_notas': mapa_notas,
    'figura_intro': figura_intro, 'tres_figuras': tres_figuras, 'compas': compas,
    'repaso_figuras': repaso_figuras, 'compositor': compositor,
    'silencio_intro': silencio_intro, 'silencio_repaso': silencio_repaso,
    'plica_cola': plica_cola, 'plica_arriba_abajo': plica_arriba_abajo,
    'plica_dibujo_pasos': plica_dibujo_pasos,
    'repaso_total': repaso_total, 'concierto': concierto, 'diploma': diploma,
}


def dibujar(c, clave, x, y, w, h, params=None):
    if clave is None:
        return
    fn = _FUNCIONES[clave]
    fn(c, x, y, w, h, **(params or {}))
