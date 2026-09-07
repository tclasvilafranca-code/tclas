# -*- coding: utf-8 -*-
"""LA CONTRASEÑA DE LA PUERTA — fichas para recortar, UNA figura por
   recuadro, sin pentagrama, sin nombre, sin color (pensada para imprimir en
   blanco y negro). La profesora compone la contraseña de la semana
   pegando varias fichas seguidas en la puerta y quien la lee bien en voz
   alta —o la toca— entra. Es MATERIAL SUELTO: cuantas más fichas y más
   variadas, más contraseñas distintas salen sin repetirse semana a semana.

   UNA COSA POR RECUADRO, SIEMPRE. Nada de sumar valores distintos en una
   misma ficha (una negra pegada a dos corcheas, por ejemplo): cada ficha es
   UNA figura, UN silencio, UN grupo de notas del MISMO valor (dos, tres o
   cuatro corcheas bajo su barra, semicorcheas, un tresillo) o UN símbolo
   suelto (calderón, ligadura) — que es justo cómo se lee de un vistazo en
   una partitura de verdad, y no una frase rítmica inventada.

   SIN PENTAGRAMA: ni las figuras sueltas ni los grupos llevan las cinco
   líneas detrás. Las sueltas nunca las llevaron
   (`juegos_comun.figura_en_caja`); los grupos las llevaban porque se
   dibujan con `notation.draw_system`, que siempre pinta un pentagrama — se
   le quita con el mismo truco que ya se usa para quitarle la barra de
   compás (`_sin_pentagrama`, más abajo).

   TRES FAMILIAS DE FICHA:
     - SUELTAS: sobre las 13 de siempre (`juegos_comun.FIGURAS`) se añaden
       tres silencios CON PUNTILLO (de blanca, negra y corchea), que el
       motor ya sabe dibujar (`notation.draw_rest` acepta el puntillo en
       cualquier silencio) pero no estaban en el catálogo de cartas.
     - GRUPOS DEL MISMO VALOR: dos/tres/cuatro corcheas, dos/cuatro
       semicorcheas, tresillo de corcheas, tresillo de semicorcheas.
     - SÍMBOLOS: calderón y ligadura, sacados de
       `juegos_comun.simbolo()` (el mismo vocabulario que ya usan el UNO y
       la Oca) — aquí sueltos, sin la casilla ni la carta alrededor.

   SIN COLOR NI NOMBRE: se imprime en blanco y negro, así que el color de
   nivel de la primera versión no servía para nada — todo va en tinta
   negra. Y sin etiqueta debajo caben muchas más fichas por hoja.

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
from page_layout_common import before_staff, after_system                    # noqa: E402
from juegos_comun import (W, H, NAVY, CREAM, RULE, INK, MUTED,                # noqa: E402
                          figura_en_caja, simbolo,
                          JUEGO_DISPLAY_BLACK, JUEGO_BODY, JUEGO_DISPLAY_ITALIC,
                          _con_tracking)
from notation import BLEED_SAFE                                              # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# --------------------------------------------------------------------------
# Cuántas veces se repite cada figura — sin color de nivel ya no hace falta
# elegir "fácil/difícil", pero se sigue repartiendo por lo simple que es de
# LEER: las figuras de toda la vida (blanca, negra, corchea...) dan para
# mezclar contraseñas largas de sobra; las más raras (tresillo de
# semicorcheas, ligadura) bastan con unas pocas para condimentar la mezcla.
# --------------------------------------------------------------------------
REPETIR = {'comun': 8, 'media': 6, 'rara': 4}

# Las 13 figuras/silencios de siempre + tres silencios con puntillo, que el
# motor ya sabe dibujar pero no estaban en el catálogo de cartas de
# `juegos_comun.FIGURAS`. 'Rq.' etc. no son claves de FIGURAS: se dibujan
# aparte, con `_silencio_en_caja`.
SUELTAS = [
    ('w', 'comun'), ('h', 'comun'), ('q', 'comun'), ('e', 'comun'),
    ('Rw', 'comun'), ('Rh', 'comun'), ('Rq', 'comun'), ('Re', 'media'),
    ('h.', 'media'), ('q.', 'media'), ('e.', 'rara'), ('s', 'rara'),
    ('Rs', 'rara'),
]
SUELTAS_PUNTILLO = [('h.', 'media'), ('q.', 'rara'), ('e.', 'rara')]  # silencios


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
    ('media', [_ev('e', 1), _ev('e', 1)]),                               # dos corcheas
    ('media', [_ev('e', 1)] * 3),                                        # tres corcheas
    ('media', [_ev('e', 1)] * 4),                                        # cuatro corcheas
    ('media', [_ev('s', 1), _ev('s', 1)]),                               # dos semicorcheas
    ('rara',  [_ev('s', 1)] * 4),                                        # cuatro semicorcheas
    ('rara',  [_ev('e', tresillo=1)] * 3),                               # tresillo de corcheas
    ('rara',  [_ev('s', tresillo=1)] * 3),                               # tresillo de semicorcheas
]

# Símbolos sueltos, del mismo vocabulario que ya usan el UNO y la Oca.
SIMBOLOS = [
    ('calderon', 'media'),
    ('ligadura', 'media'),
]


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


def _grupo_en_caja(c, cx, cy, ancho, alto, eventos):
    """Dibuja un grupo de notas (en Si4, sin clave, sin compás y sin
       pentagrama) centrado en (cx, cy) y a la escala que llene la caja —
       mismo principio que `juegos_comun.figura_en_caja`, para varias
       notas en vez de una."""
    def total(gap):
        return (before_staff(gap, eventos, 'treble') + 4 * gap
                + after_system(gap, eventos, 'treble'))
    k = total(1.0)
    gap = alto / k
    top_y = (cy + alto / 2.0) - before_staff(gap, eventos, 'treble')
    x = cx - ancho / 2.0
    c.saveState()
    with _sin_barras(), _sin_pentagrama():
        nt.draw_system(c, x, top_y, ancho, gap, eventos, clef='treble',
                       show_clef=False, show_time=False, spacing='engraved')
    c.restoreState()


def _silencio_en_caja(c, cx, cy, ancho, alto, dur):
    """Un silencio CON PUNTILLO ('h.', 'q.', 'e.'): no está en el catálogo
       de `juegos_comun.FIGURAS` (que solo trae los silencios lisos), así
       que se dibuja con el mismo truco de pentagrama imaginario que usa
       `juegos_comun.figura()` por dentro, llamando a `draw_rest`
       directamente — el motor ya sabe poner el puntillo, aquí solo hace
       falta darle el hueco."""
    # un silencio con puntillo es un poco más ancho que uno liso por el
    # punto; 2.3 x 1.9 (alto x ancho, en espacios de pentagrama) es lo que
    # mide de verdad dibujándolo, con margen de sobra.
    gap = min(alto / 2.3, ancho / 1.9)
    sb, st = cy - 2 * gap, cy + 2 * gap
    nt.draw_rest(c, cx, sb, st, gap, dur)


def _simbolo_en_caja(c, cx, cy, ancho, alto, cual):
    r = min(ancho, alto) * 0.42
    simbolo(c, cx, cy, r, cual, INK)


# --------------------------------------------------------------------------
# El mazo: se baraja con semilla fija, para que la hoja sea siempre la misma.
# --------------------------------------------------------------------------
def construir_mazo():
    mazo = []
    for clave, peso in SUELTAS:
        for _ in range(REPETIR[peso]):
            mazo.append(('suelta', clave))
    for dur, peso in SUELTAS_PUNTILLO:
        for _ in range(REPETIR[peso]):
            mazo.append(('silencio_puntillo', dur))
    for peso, eventos in GRUPOS:
        for _ in range(REPETIR[peso]):
            mazo.append(('grupo', eventos))
    for cual, peso in SIMBOLOS:
        for _ in range(REPETIR[peso]):
            mazo.append(('simbolo', cual))
    random.Random(77).shuffle(mazo)
    return mazo


# --------------------------------------------------------------------------
# La hoja: cuadrícula densa y fichas pequeñas — sin pentagrama, sin nombre y
# sin color, cada ficha ocupa poco, así que caben muchas más por hoja.
# --------------------------------------------------------------------------
MARGIN = 32
CONTENT_W = W - 2 * MARGIN
COLS, FILAS = 8, 10
POR_HOJA = COLS * FILAS
FICHA_W = CONTENT_W / COLS
CABECERA_H = 70
FICHA_H = (H - CABECERA_H - 40) / FILAS


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
    """Una ficha: SOLO la figura, centrada, en tinta negra — sin nombre, sin
       color, sin pentagrama."""
    tipo, dato = item
    cx, cy = x + w / 2.0, y + h / 2.0
    if tipo == 'suelta':
        figura_en_caja(c, cx, cy, w * 0.72, h * 0.78, dato, INK)
    elif tipo == 'silencio_puntillo':
        _silencio_en_caja(c, cx, cy, w * 0.72, h * 0.78, dato)
    elif tipo == 'grupo':
        _grupo_en_caja(c, cx, cy, w * 0.88, h * 0.78, dato)
    else:
        _simbolo_en_caja(c, cx, cy, w * 0.88, h * 0.86, dato)


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
