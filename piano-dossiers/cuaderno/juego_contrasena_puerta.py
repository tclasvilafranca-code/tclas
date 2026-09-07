# -*- coding: utf-8 -*-
"""LA CONTRASEÑA DE LA PUERTA — fichas para recortar, UNA figura por
   recuadro, sin pentagrama, sin nombre, sin color (pensada para imprimir en
   blanco y negro). La profesora compone la contraseña de la semana
   pegando varias fichas seguidas en la puerta y quien la lee bien en voz
   alta —o la toca— entra. Es MATERIAL SUELTO: cuantas más fichas y más
   variadas, más contraseñas largas y distintas salen sin repetirse.

   UNA COSA POR RECUADRO, SIEMPRE. Nada de sumar valores distintos en una
   misma ficha: cada ficha es UNA figura, UN silencio, UN grupo de notas del
   MISMO valor (dos/tres/cuatro corcheas bajo su barra, semicorcheas, un
   tresillo) o UN símbolo suelto (calderón, ligadura).

   TODAS LAS FIGURAS AL MISMO TAMAÑO DE VERDAD. La primera versión ajustaba
   cada ficha para llenar su recuadro, y eso hacía que una redonda (que es
   solo una cabeza) saliera enorme al lado de una negra (cabeza + plica) —
   mismo recuadro, tamaño de nota muy distinto. Aquí se dibuja TODO con el
   mismo `GAP` (el mismo espacio de pentagrama, la unidad de la que sale el
   tamaño real de una cabeza y una plica), calculado UNA vez para toda la
   hoja: la cabeza y la plica de cualquier ficha miden lo mismo en todas las
   demás. Lo que cambia de una ficha a otra es el ANCHO (una redonda ocupa
   poco; cuatro semicorcheas en barra, más), nunca el tamaño de la nota.

   VOCABULARIO, bien ancho a propósito (lo pidió el cliente: "dale caña"):
     - SUELTAS: las 13 de siempre —redonda, blanca, negra, corchea,
       semicorchea, sus puntillos y sus silencios— más DOS FIGURAS QUE EL
       MOTOR COMPARTIDO NO TENÍA: fusa y semifusa (tres y cuatro corchetes),
       nota y silencio de cada una. El motor de notación (`engine/
       notation.py`) llega hasta la semicorchea (dos corchetes) porque
       ninguna partitura del cuaderno necesita menos; aquí, para variedad de
       una ficha de cortar, se dibujan a mano reutilizando exactamente el
       mismo trazo de corchete en curva que usa `notation.draw_note`
       (`_nota_con_flags`, más abajo) y los glifos de silencio de fusa/
       semifusa de Unicode (U+1D140, U+1D141), que SÍ existen en
       `FreeSerif` — comprobado renderizando antes de usarlos.
     - CON PUNTILLO: notas Y silencios de blanca, negra y corchea.
     - GRUPOS DEL MISMO VALOR: dos/tres/cuatro corcheas, dos/cuatro
       semicorcheas, tresillo de corcheas, tresillo de semicorcheas.
     - SÍMBOLOS: calderón y ligadura, del mismo vocabulario que ya usan el
       UNO y la Oca (`juegos_comun.simbolo`).

   SIN PENTAGRAMA NI COLOR: los grupos se dibujan con `notation.draw_system`,
   que siempre pinta las cinco líneas — se le quitan con el mismo truco con
   que se le quita la barra de compás (ver `_sin_pentagrama`/`_sin_barras`).
   Todo en tinta negra: en blanco y negro un color de nivel no se ve.

   Uso:  python3 juego_contrasena_puerta.py
"""
import os
import random
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import notation as nt                                                        # noqa: E402
from juegos_comun import (W, H, NAVY, CREAM, RULE, INK, MUTED,                # noqa: E402
                          simbolo, JUEGO_DISPLAY_BLACK, JUEGO_BODY,
                          JUEGO_DISPLAY_ITALIC, _con_tracking)
from notation import BLEED_SAFE                                              # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# --------------------------------------------------------------------------
# Cuántas veces se repite cada figura. Sin color de nivel ya no hace falta
# marcar "fácil/difícil", pero se sigue repartiendo por lo COMÚN que es cada
# una: negra, blanca, redonda, corchea y semicorchea (lo que pidió el
# cliente explícitamente) dan para contraseñas largas de sobra; lo raro
# (fusa, tresillo de semicorcheas, ligadura) unas pocas para condimentar.
# --------------------------------------------------------------------------
REPETIR = {'comun': 10, 'media': 6, 'rara': 4}

# --------------------------------------------------------------------------
# SUELTAS de nota (con su propio dibujo, sin pentagrama): duración + cuántos
# corchetes lleva (0 = sin plica ni corchete: redonda; None = con plica sin
# corchete: blanca/negra). El motor ya sabe dibujar hasta 2 corchetes
# (semicorchea); 3 y 4 (fusa, semifusa) se dibujan aparte —`_nota_flags`.
# --------------------------------------------------------------------------
NOTAS = [
    # (nombre-dur para el motor si existe, corchetes, puntillo, peso)
    ('w',  0, False, 'comun'),   # redonda
    ('h',  None, False, 'comun'),   # blanca
    ('h',  None, True,  'media'),   # blanca con puntillo
    ('q',  None, False, 'comun'),   # negra
    ('q',  None, True,  'media'),   # negra con puntillo
    ('e',  1, False, 'comun'),   # corchea
    ('e',  1, True,  'media'),   # corchea con puntillo
    ('s',  2, False, 'comun'),   # semicorchea
    ('s',  2, True,  'rara'),    # semicorchea con puntillo
    ('f',  3, False, 'rara'),    # fusa
    ('sf', 4, False, 'rara'),    # semifusa
]

# SILENCIOS: base ('w','h','q','e','s','f','sf') + puntillo. 'f'/'sf' no los
# dibuja `draw_rest` (que llega hasta semicorchea); se dibujan con el glifo
# Unicode de fusa/semifusa, comprobado en `FreeSerif`.
SILENCIOS = [
    ('w', False, 'comun'), ('h', False, 'comun'), ('h', True, 'media'),
    ('q', False, 'comun'), ('q', True, 'media'),
    ('e', False, 'comun'), ('e', True, 'media'),
    ('s', False, 'comun'), ('s', True, 'rara'),
    ('f', False, 'rara'), ('sf', False, 'rara'),
]


def _ev(dur, beam=None, tresillo=None):
    e = {'pitch': 'B4', 'dur': dur}
    if beam is not None:
        e['beam'] = beam
    if tresillo is not None:
        e['tresillo'] = tresillo
    return e


# Grupos de notas del MISMO valor, todas en Si4 (línea de en medio, para que
# ninguna pida línea adicional) — el mismo truco que usa `juegos_comun.figura`.
GRUPOS = [
    ('media', [_ev('e', 1), _ev('e', 1)]),                # dos corcheas
    ('media', [_ev('e', 1)] * 3),                          # tres corcheas
    ('media', [_ev('e', 1)] * 4),                          # cuatro corcheas
    ('media', [_ev('s', 1), _ev('s', 1)]),                 # dos semicorcheas
    ('rara',  [_ev('s', 1)] * 4),                           # cuatro semicorcheas
    ('rara',  [_ev('e', beam=1, tresillo=1)] * 3),          # tresillo de corcheas
    ('rara',  [_ev('s', beam=1, tresillo=1)] * 3),          # tresillo de semicorcheas
]

# Símbolos sueltos, del mismo vocabulario que ya usan el UNO y la Oca.
SIMBOLOS = [
    ('calderon', 'media'),
    ('ligadura', 'media'),
]

# --------------------------------------------------------------------------
# EL TAMAÑO DE VERDAD: un único GAP para toda la hoja (ver docstring). Se
# calcula a partir de lo más alto que hay que dibujar — un TRESILLO, cuyo
# corchete y su "3" se dibujan por encima de la plica — para que nada se
# salga de su recuadro por arriba.
# --------------------------------------------------------------------------
NOTA_ALTO = 3.95     # cabeza + plica, en espacios de pentagrama (medido)
TRESILLO_ALTO = 5.4  # cabeza + plica + corchete del tresillo + el "3"


def _flag_bezier(c, fx, fy, gap):
    """El mismo trazo curvo (bezier, no una cuña recta) que usa
       `notation.draw_note` para el corchete de una corchea o una
       semicorchea — copiado tal cual, porque el motor compartido no llega
       a fusa/semifusa y no hay que inventarse un trazo nuevo para que
       combine con el resto."""
    p = c.beginPath()
    p.moveTo(fx, fy)
    p.curveTo(fx + gap * 0.15, fy - gap * 0.25, fx + gap * 0.95, fy - gap * 0.05,
             fx + gap * 0.68, fy - gap * 1.25)
    p.curveTo(fx + gap * 0.62, fy - gap * 0.85, fx + gap * 0.22, fy - gap * 0.55,
             fx, fy - gap * 0.35)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def _nota_en_caja(c, cx, cy, gap, corchetes, puntillo):
    """Una nota suelta: cabeza + plica (si no es redonda) + N corchetes
       (0, 1, 2 los dibuja ya `notation.draw_note`; 3 y 4 —fusa,
       semifusa— se dibujan aquí, reaprovechando el mismo trazo de
       corchete). `cabeza` se coloca 1.45*gap por debajo de `cy` — el mismo
       desplazamiento que usa `juegos_comun.figura()` para que la figura
       quede centrada de verdad (una plica hacia arriba pesa hacia arriba,
       y sin este ajuste la nota se ve descolgada hacia abajo en su caja)."""
    # la redonda no lleva plica, así que no pesa hacia arriba y no necesita
    # el desplazamiento óptico — igual que en `juegos_comun.figura()`.
    cabeza = cy if corchetes == 0 else cy - gap * 1.45
    filled = corchetes != 0 or corchetes is None  # todo menos la redonda va rellena
    nt.draw_notehead(c, cx, cabeza, gap, filled=filled)
    if puntillo:
        c.setFillColor(nt.INK)
        c.circle(cx + gap * 1.05, cabeza + gap * 0.15, gap * 0.14, fill=1, stroke=0)
    if corchetes == 0:
        return
    stem_x = cx + gap * 0.6
    stem_top = cabeza + gap * 3.4
    c.setStrokeColor(nt.INK)
    c.setLineWidth(max(1.3, gap * 0.115))
    c.line(stem_x, cabeza, stem_x, stem_top)
    if corchetes:
        c.setFillColor(nt.INK)
        for k in range(corchetes):
            _flag_bezier(c, stem_x, stem_top - k * gap * 0.9, gap)


def _silencio_en_caja(c, cx, cy, gap, base, puntillo):
    """Un silencio, con o sin puntillo. Hasta semicorchea lo dibuja
       `notation.draw_rest` (con el mismo truco de pentagrama imaginario
       que usa `juegos_comun.figura`); fusa y semifusa van con su propio
       glifo Unicode, que no está cableado en `draw_rest`."""
    if base in ('f', 'sf'):
        glifo = '\U0001D140' if base == 'f' else '\U0001D141'
        c.setFillColor(nt.INK)
        c.setFont('FreeSerif', gap * 2.6)
        c.drawCentredString(cx, cy - gap * 0.6, glifo)
        if puntillo:
            c.circle(cx + gap * 1.15, cy + gap * 0.5, gap * 0.14, fill=1, stroke=0)
        return
    dur = base + ('.' if puntillo else '')
    sb, st = cy - 2 * gap, cy + 2 * gap
    nt.draw_rest(c, cx, sb, st, gap, dur)


class _sin_barras(object):
    """`draw_system` siempre remata con una barra de compás a cada lado; en
       una ficha de un par de centímetros la barra de cierre queda pegada
       al borde y lo cruza. Se quita mientras dura el dibujo, igual que
       `_tinta` cambia la tinta, y se devuelve después sin excepciones."""

    def __enter__(self):
        self._orig = nt.draw_barline
        nt.draw_barline = lambda *a, **k: None
        return self

    def __exit__(self, *_e):
        nt.draw_barline = self._orig
        return False


class _sin_pentagrama(object):
    """Ídem, pero con las cinco líneas del pentagrama: para un GRUPO de
       notas (dos corcheas, un tresillo...) `draw_system` las pinta siempre
       detrás, y aquí se pidió justo lo contrario — solo la figura, sin
       ninguna línea. `draw_staff` no dibuja nada mientras dura el truco,
       pero sigue devolviendo las mismas cinco coordenadas Y que calcularía
       de verdad, así que el resto de `draw_system` (posición de las notas,
       líneas adicionales, plicas) no se entera del cambio."""

    def __enter__(self):
        self._orig = nt.draw_staff

        def _fake(c, x, top_y, w, gap=9, lines=5):
            return [top_y - i * gap for i in range(lines)]
        nt.draw_staff = _fake
        return self

    def __exit__(self, *_e):
        nt.draw_staff = self._orig
        return False


def _grupo_en_caja(c, cx, cy, gap, ancho, eventos):
    """Dibuja un grupo de notas (en Si4, sin clave, sin compás y sin
       pentagrama) centrado en (cx, cy), AL MISMO `gap` que toda la hoja —
       lo único que varía de un grupo a otro es cuánto ANCHO ocupa, según
       cuántas notas tenga. `top_y` se calcula para que la cabeza de las
       notas (que en Si4 cae en la línea de en medio del pentagrama
       imaginario) quede 1.45*gap por debajo de `cy` — el mismo
       desplazamiento óptico que usa `_nota_en_caja`/`figura()`, para que
       un grupo y una nota suelta queden a la misma altura visual."""
    top_y = cy + gap * 0.55
    x = cx - ancho / 2.0
    c.saveState()
    with _sin_barras(), _sin_pentagrama():
        nt.draw_system(c, x, top_y, ancho, gap, eventos, clef='treble',
                       show_clef=False, show_time=False, spacing='engraved')
    c.restoreState()


def _simbolo_en_caja(c, cx, cy, gap, cual):
    simbolo(c, cx, cy, gap * 1.55, cual, INK)


# --------------------------------------------------------------------------
# El mazo: se baraja con semilla fija, para que la hoja sea siempre la misma.
# --------------------------------------------------------------------------
def construir_mazo():
    mazo = []
    for dur, corchetes, puntillo, peso in NOTAS:
        for _ in range(REPETIR[peso]):
            mazo.append(('nota', corchetes, puntillo))
    for base, puntillo, peso in SILENCIOS:
        for _ in range(REPETIR[peso]):
            mazo.append(('silencio', base, puntillo))
    for peso, eventos in GRUPOS:
        for _ in range(REPETIR[peso]):
            mazo.append(('grupo', eventos))
    for cual, peso in SIMBOLOS:
        for _ in range(REPETIR[peso]):
            mazo.append(('simbolo', cual))
    random.Random(77).shuffle(mazo)
    return mazo


# --------------------------------------------------------------------------
# La hoja: fichas grandes de verdad (se pidió explícitamente que no
# quedaran pequeñas) en una cuadrícula de 6x7 — con la nota siempre al mismo
# tamaño, lo que cambia de una hoja apretada a una hoja amplia es cuánto
# aire le sobra alrededor a cada ficha, no el tamaño de la figura.
# --------------------------------------------------------------------------
MARGIN = 34
CONTENT_W = W - 2 * MARGIN
COLS, FILAS = 6, 7
POR_HOJA = COLS * FILAS
FICHA_W = CONTENT_W / COLS
CABECERA_H = 70
FICHA_H = (H - CABECERA_H - 40) / FILAS

# El GAP se fija UNA vez, a partir de lo más alto que hay que dibujar (el
# tresillo) y del alto real de una ficha, con un margen del 12% arriba y
# abajo para que nada roce el borde de la tarjeta.
GAP = (FICHA_H * 0.88) / TRESILLO_ALTO


def _tarjeta(c, x, y, w, h):
    """El marco de la ficha: un filete fino y redondeado — bonito y a la
       vez la guía de corte, sin necesitar una cuadrícula aparte."""
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.roundRect(x + 3, y + 3, w - 6, h - 6, 8, fill=0, stroke=1)


def _ficha(c, x, y, w, h, item):
    """Una ficha: SOLO la figura, centrada, en tinta negra, al `GAP` fijo
       de toda la hoja — sin nombre, sin color, sin pentagrama."""
    _tarjeta(c, x, y, w, h)
    tipo = item[0]
    cx, cy = x + w / 2.0, y + h / 2.0
    if tipo == 'nota':
        _, corchetes, puntillo = item
        _nota_en_caja(c, cx, cy, GAP, corchetes, puntillo)
    elif tipo == 'silencio':
        _, base, puntillo = item
        _silencio_en_caja(c, cx, cy, GAP, base, puntillo)
    elif tipo == 'grupo':
        _, eventos = item
        _grupo_en_caja(c, cx, cy, GAP, w - 20, eventos)
    else:
        _, cual = item
        _simbolo_en_caja(c, cx, cy, GAP, cual)


def _cabecera_pagina(c, pagina, total):
    """Cabecera mínima: kicker y título, nada más — la hoja es para
       recortar, no para leer."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    b = BLEED_SAFE
    c.setFillColor(NAVY)
    c.rect(b, H - CABECERA_H - b, W - 2 * b, CABECERA_H, fill=1, stroke=0)

    c.setFont(JUEGO_BODY, 7.2)
    c.setFillColor(HexColor('#9FB0C4'))
    _con_tracking(c, MARGIN, H - 30, 'MATERIAL DE CLASE · EL CUADERNO DEL PIANISTA', 1.0)
    c.setFont(JUEGO_DISPLAY_BLACK, 19)
    c.setFillColor(white)
    c.drawString(MARGIN, H - 54, 'La contraseña de la puerta')

    c.setFont(JUEGO_BODY, 6.6)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, 18, 'El Cuaderno del Pianista · T-Clas')
    c.setFont(JUEGO_DISPLAY_ITALIC, 7.2)
    c.drawRightString(W - MARGIN, 18, 'Hoja %d de %d' % (pagina, total))


def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Contrasena_de_la_puerta.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('La contraseña de la puerta')

    mazo = construir_mazo()
    total_paginas = -(-len(mazo) // POR_HOJA)     # division hacia arriba
    x0, y0 = MARGIN, H - CABECERA_H - FILAS * FICHA_H - 10

    pagina = 1
    while mazo:
        lote, mazo = mazo[:POR_HOJA], mazo[POR_HOJA:]
        _cabecera_pagina(c, pagina, total_paginas)
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
