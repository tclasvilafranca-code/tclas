# -*- coding: utf-8 -*-
"""LA CONTRASEÑA DE LA PUERTA — fichas de figuras y silencios para recortar y
   pegar en la puerta del aula. La profesora compone la contraseña de la
   semana pegando varias fichas seguidas (una blanca, tres corcheas, un
   silencio, un tresillo...) y quien la lee bien en voz alta —o la toca—
   entra. No es un juego con reglas propias: es MATERIAL SUELTO, muchas
   fichas de golpe, para que dé para mezclar contraseñas distintas cada
   semana sin quedarse sin figuras.

   DOS FAMILIAS DE FICHA:
     - SUELTAS: una sola figura o silencio (`juegos_comun.figura_en_caja`,
       la misma pieza que ya dibuja los pips del UNO musical). Redonda,
       blanca, negra, corchea, sus puntillos y la semicorchea, con sus
       silencios — 13 figuras distintas en total.
     - GRUPOS: varias notas juntas (dos corcheas bajo una barra, cuatro
       semicorcheas, un tresillo...). No hay ninguna pieza ya hecha para
       esto, así que se reaprovecha el truco de `juegos_comun.figura()`
       llevado a `notation.draw_system`: todas las notas en Si4 (la línea
       de en medio, para que ninguna pida línea adicional), sin clave ni
       compás — el motor ya sabe barrar corcheas seguidas y dibujar un
       tresillo con su corchete, así que aquí no se repite nada de eso.

   CADA FICHA LLEVA EL COLOR DE SU NIVEL — verde/ocre/granate, el mismo
   código de `niveles.py` que usan los cinco juegos —para que, con solo
   mirar el color, la profesora sepa qué figuras puede mezclar para un
   alumno que va empezando y cuáles solo para uno que ya lee corcheas y
   puntillos. LA CANTIDAD ES A PROPÓSITO DESIGUAL: las figuras fáciles se
   repiten más veces (hacen falta muchas para una contraseña larga) y las
   difíciles menos (una o dos bastan para "subir el nivel" de una semana).

   Uso:  python3 juego_contrasena_puerta.py
"""
import os
import random
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import notation as nt                                                        # noqa: E402
from page_layout_common import before_staff, after_system                    # noqa: E402
from juegos_comun import (W, H, NAVY, NAVY_SOFT, CREAM, RULE, INK, MUTED,     # noqa: E402
                          ACCENT, NIVELES, FIGURAS, figura_en_caja, _tinta,
                          JUEGO_DISPLAY_BLACK, JUEGO_DISPLAY_ITALIC,
                          JUEGO_BODY, JUEGO_BODY_BOLD, JUEGO_BODY_BLACK,
                          _con_tracking)
from notation import BLEED_SAFE                                              # noqa: E402
from portada import _wrap                                                    # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# --------------------------------------------------------------------------
# Nivel de cada figura suelta — el mismo criterio que ya usan las barajas de
# los cinco juegos (`juegos_comun.NIVELES`): en qué escalón ENTRA la figura,
# no una clasificación nueva. 'Rw' y 'Rs' no aparecen en ninguna lista de
# NIVELES (esas listas son para repartir cartas de baraja, no un catálogo
# completo); se colocan junto a su pareja de duración — el silencio de
# redonda es tan simple de leer como la redonda, y el de semicorchea tan
# raro como la propia semicorchea.
# --------------------------------------------------------------------------
NIVEL_DE_FIGURA = {
    'w': 1, 'Rw': 1, 'h': 1, 'Rh': 1, 'q': 1, 'Rq': 1, 'e': 1,
    'h.': 2, 'q.': 2,
    'e.': 3, 's': 3, 'Re': 3, 'Rs': 3,
}

# Cuántas veces se repite cada figura suelta en el mazo — las fáciles dan
# para mezclar contraseñas de sobra; las difíciles, para condimentar.
REPETIR_SUELTA = {1: 4, 2: 3, 3: 2}

# --------------------------------------------------------------------------
# Los GRUPOS: varias notas juntas, todas en Si4 para que ninguna pida línea
# adicional (el mismo truco que usa `juegos_comun.figura`). 'beam' agrupa
# las corcheas/semicorcheas bajo una barra; 'tresillo' dibuja el corchete
# con el 3 — las dos cosas ya las sabe hacer `notation.draw_system`, aquí
# solo se listan los eventos.
# --------------------------------------------------------------------------
def _ev(dur, beam=None, tresillo=None):
    e = {'pitch': 'B4', 'dur': dur}
    if beam is not None:
        e['beam'] = beam
    if tresillo is not None:
        e['tresillo'] = tresillo
    return e


GRUPOS = [
    # (nombre, nivel, repeticiones, eventos)
    ('dos corcheas',              2, 3, [_ev('e', 1), _ev('e', 1)]),
    ('tres corcheas',             2, 2, [_ev('e', 1), _ev('e', 1), _ev('e', 1)]),
    ('cuatro corcheas',           2, 2, [_ev('e', 1)] * 4),
    ('negra y dos corcheas',      2, 2, [_ev('q'), _ev('e', 1), _ev('e', 1)]),
    ('dos corcheas y negra',      2, 2, [_ev('e', 1), _ev('e', 1), _ev('q')]),
    ('corchea, silencio, corchea', 2, 2, [_ev('e'), {'rest': True, 'dur': 'e'}, _ev('e')]),
    ('tresillo de corcheas',      3, 3, [_ev('e', tresillo=1), _ev('e', tresillo=1), _ev('e', tresillo=1)]),
    ('corchea con puntillo y semicorchea', 3, 2, [_ev('e.', 1), _ev('s', 1)]),
    ('semicorchea y corchea con puntillo', 3, 2, [_ev('s', 1), _ev('e.', 1)]),
    ('cuatro semicorcheas',       3, 2, [_ev('s', 1)] * 4),
    ('dos semicorcheas y corchea', 3, 2, [_ev('s', 1), _ev('s', 1), _ev('e', 1)]),
]


class _sin_barras(object):
    """`draw_system` siempre remata con una barra de compás a cada lado — en
       una partitura de verdad hace falta, pero en una ficha suelta de 100pt
       de ancho la barra de cierre queda pegada al borde redondeado de la
       tarjeta y lo atraviesa. Se quita igual que `_tinta` cambia la tinta:
       mientras dura el dibujo, y se devuelve después sin excepciones."""

    def __enter__(self):
        self._orig = nt.draw_barline
        nt.draw_barline = lambda *a, **k: None
        return self

    def __exit__(self, *_e):
        nt.draw_barline = self._orig
        return False


def _grupo_en_caja(c, cx, cy, ancho, alto, eventos, color=None):
    """Dibuja un grupo de notas (en Si4, sin clave ni compás) centrado en
       (cx, cy) y a la escala que llene la caja — mismo principio que
       `juegos_comun.figura_en_caja`, pero para varias notas en vez de una."""
    def total(gap):
        return (before_staff(gap, eventos, 'treble') + 4 * gap
                + after_system(gap, eventos, 'treble'))
    k = total(1.0)
    gap = alto / k
    top_y = (cy + alto / 2.0) - before_staff(gap, eventos, 'treble')
    x = cx - ancho / 2.0
    c.saveState()
    with _tinta(color), _sin_barras():
        nt.draw_system(c, x, top_y, ancho, gap, eventos, clef='treble',
                       show_clef=False, show_time=False, spacing='engraved')
    c.restoreState()
    return gap


# --------------------------------------------------------------------------
# El mazo: se baraja con semilla fija, para que la hoja sea siempre la misma.
# --------------------------------------------------------------------------
def construir_mazo():
    mazo = []
    for clave, (nombre, _beats, _sym) in FIGURAS.items():
        nivel = NIVEL_DE_FIGURA[clave]
        for _ in range(REPETIR_SUELTA[nivel]):
            mazo.append(('suelta', nombre, nivel, clave))
    for nombre, nivel, veces, eventos in GRUPOS:
        for _ in range(veces):
            mazo.append(('grupo', nombre, nivel, eventos))
    random.Random(77).shuffle(mazo)
    return mazo


# --------------------------------------------------------------------------
# La hoja: cuadrícula densa, con retícula de corte de punta a punta —a este
# tamaño de ficha una marca solo en las esquinas no basta para guiar un
# recorte interior recto.
# --------------------------------------------------------------------------
MARGIN = 40
CONTENT_W = W - 2 * MARGIN
COLS, FILAS = 5, 6
POR_HOJA = COLS * FILAS
FICHA_W = CONTENT_W / COLS
CABECERA_H = 172
FICHA_H = (H - CABECERA_H - 60) / FILAS


def _reticula(c, x0, y0, filas):
    """Solo dibuja la cuadrícula de las filas que de verdad llevan fichas —
       en la última hoja, que casi nunca sale justa, no tiene sentido
       imprimir cuadrícula vacía por debajo de la última ficha."""
    c.setStrokeColor(RULE)
    c.setLineWidth(0.4)
    c.setDash(2, 2)
    alto = filas * FICHA_H
    for i in range(COLS + 1):
        x = x0 + i * FICHA_W
        c.line(x, y0, x, y0 + alto)
    for j in range(filas + 1):
        y = y0 + j * FICHA_H
        c.line(x0, y, x0 + COLS * FICHA_W, y)
    c.setDash()


def _ficha(c, x, y, w, h, item):
    tipo, nombre, nivel, dato = item
    color = NIVELES[nivel]['color']
    c.setFillColor(white)
    c.setStrokeColor(color)
    c.setLineWidth(1.1)
    c.roundRect(x + 4, y + 4, w - 8, h - 8, 6, fill=1, stroke=1)

    cx = x + w / 2.0
    zona_h = h * 0.62
    zona_cy = y + h - 10 - zona_h / 2.0
    if tipo == 'suelta':
        figura_en_caja(c, cx, zona_cy, w * 0.6, zona_h, dato, color)
    else:
        _grupo_en_caja(c, cx, zona_cy, w * 0.82, zona_h, dato, color)

    c.setFont(JUEGO_BODY_BLACK, 7.4)
    c.setFillColor(color)
    etiqueta = nombre.upper()
    while stringWidth(etiqueta, JUEGO_BODY_BLACK, 7.4) > w - 12 and len(etiqueta) > 4:
        etiqueta = etiqueta[:-1]
        while etiqueta and etiqueta[-1] == ' ':
            etiqueta = etiqueta[:-1]
    if len(etiqueta) < len(nombre.upper()):
        etiqueta += '…'
    c.drawCentredString(cx, y + 9, etiqueta)


def _cabecera_pagina(c, pagina, total):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    b = BLEED_SAFE
    c.setFillColor(NAVY)
    c.rect(b, H - CABECERA_H - b, W - 2 * b, CABECERA_H, fill=1, stroke=0)

    c.setFont(JUEGO_BODY_BOLD, 8.2)
    c.setFillColor(HexColor('#9FB0C4'))
    _con_tracking(c, MARGIN, H - 40, 'MATERIAL DE CLASE · EL CUADERNO DEL PIANISTA', 1.1)
    c.setFont(JUEGO_DISPLAY_BLACK, 27)
    c.setFillColor(white)
    c.drawString(MARGIN, H - 74, 'La contraseña de la puerta')
    c.setFont(JUEGO_DISPLAY_ITALIC, 10.8)
    c.setFillColor(HexColor('#C3CEDB'))
    c.drawString(MARGIN, H - 92,
                'Recorta las fichas y pega en la puerta la contraseña de la semana')

    c.setFont(JUEGO_BODY, 8.4)
    c.setFillColor(HexColor('#C3CEDB'))
    instr = ('Se combinan varias fichas en fila (ej.: una blanca + tres corcheas + un silencio + '
            'un tresillo). Quien la lee bien en voz alta —o la toca— entra en clase.')
    _wrap(c, instr, MARGIN, H - 112, JUEGO_BODY, 8.4, CONTENT_W, 12.0, HexColor('#C3CEDB'))

    leyenda_x = W - MARGIN
    for nivel in (3, 2, 1):
        n = NIVELES[nivel]
        c.setFont(JUEGO_BODY_BOLD, 7.6)
        tw = stringWidth(n['nombre'], JUEGO_BODY_BOLD, 7.6)
        leyenda_x -= tw
        c.setFillColor(white)
        c.drawString(leyenda_x, H - 152, n['nombre'])
        leyenda_x -= 14
        c.setFillColor(n['color'])
        c.circle(leyenda_x, H - 148, 4.2, fill=1, stroke=0)
        leyenda_x -= 18

    c.setFont(JUEGO_BODY, 6.8)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, 24, 'El Cuaderno del Pianista · T-Clas')
    c.setFont(JUEGO_DISPLAY_ITALIC, 7.4)
    c.drawRightString(W - MARGIN, 24, 'Hoja %d de %d' % (pagina, total))


def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Contrasena_de_la_puerta.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('La contraseña de la puerta')

    mazo = construir_mazo()
    total_paginas = -(-len(mazo) // POR_HOJA)     # division hacia arriba
    x0, y0 = MARGIN, H - CABECERA_H - FILAS * FICHA_H - 12

    pagina = 1
    while mazo:
        lote, mazo = mazo[:POR_HOJA], mazo[POR_HOJA:]
        filas_usadas = -(-len(lote) // COLS)
        _cabecera_pagina(c, pagina, total_paginas)
        _reticula(c, x0, y0 + (FILAS - filas_usadas) * FICHA_H, filas_usadas)
        for k, item in enumerate(lote):
            col = k % COLS
            fil = k // COLS
            x = x0 + col * FICHA_W
            y = y0 + (FILAS - 1 - fil) * FICHA_H
            _ficha(c, x, y, FICHA_W, FICHA_H, item)
        c.showPage()
        pagina += 1

    c.save()
    return ruta


def main(argv):
    ruta = construir()
    print('La contraseña de la puerta · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
