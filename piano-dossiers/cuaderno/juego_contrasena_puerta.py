# -*- coding: utf-8 -*-
"""LA CONTRASEÑA DE LA PUERTA — fichas para recortar, UNA figura por
   recuadro, sin pentagrama, sin nombre, sin color (para imprimir en blanco
   y negro). La profesora compone la contraseña de la semana pegando varias
   fichas seguidas en la puerta y quien la lee bien en voz alta —o la toca—
   entra. Es MATERIAL SUELTO: cuantas más fichas y más variadas, más
   contraseñas largas y distintas salen sin repetirse.

   ================= LAS TRES REGLAS DE ESTA HOJA =================

   1. NINGUNA FIGURA SE SALE DE SU RECUADRO. Y no de palabra: MEDIDO. Cada
      figura se dibuja una vez en una hoja de prueba, se rasteriza y se mide
      la tinta de verdad (arriba, abajo, izquierda, derecha) — eso es
      `MEDIDAS`, y se regenera con `python3 juego_contrasena_puerta.py
      --medir`. Con esa tabla, el programa (a) calcula el `GAP` más grande
      con el que la figura MÁS GRANDE de todas sigue cabiendo en su ficha, y
      (b) coloca cada figura centrada por SU PROPIA tinta. Antes el tresillo
      se salía por arriba porque el corchete y el "3" se dibujan por encima
      de la plica y nadie les había reservado sitio.

   2. TODAS LAS FIGURAS AL MISMO TAMAÑO DE VERDAD. Un único `GAP` (el
      espacio de pentagrama, la unidad de la que salen el tamaño de la
      cabeza y el largo de la plica) para TODA la colección: la cabeza de
      una negra mide exactamente lo mismo que la de una corchea o la de
      cualquier nota de un tresillo. Lo que cambia de una ficha a otra es el
      ANCHO —dos corcheas ocupan menos que cuatro semicorcheas—, nunca el
      tamaño de la nota.

   3. UNA COSA POR RECUADRO. Cada ficha es UNA figura, UN silencio, UN grupo
      de notas del MISMO valor (dos/tres/cuatro corcheas o semicorcheas bajo
      su barra, un tresillo) o UN símbolo (calderón, ligadura). Nunca la
      suma de valores distintos.

   ================= EL VOCABULARIO =================

   NOTAS: redonda, blanca, negra, corchea, semicorchea, fusa y semifusa,
   más las de puntillo (blanca, negra, corchea, semicorchea). La blanca y la
   redonda van con la CABEZA HUECA y la negra rellena, que es lo que las
   distingue — en una versión anterior la blanca salía rellena y por eso no
   se veía ninguna blanca en toda la hoja: eran todas negras.

   SILENCIOS: de redonda, blanca, negra, corchea, semicorchea, fusa y
   semifusa. SIN PUNTILLO (decisión del cliente). Los de REDONDA y BLANCA
   son el mismo rectangulito y solos no se distinguen, así que llevan su
   LÍNEA DE REFERENCIA dibujada: el de blanca SE APOYA encima de la línea y
   el de redonda CUELGA por debajo, exactamente como en una partitura.

   GRUPOS: dos, tres y cuatro corcheas; dos y cuatro semicorcheas; tresillo
   de corcheas y tresillo de semicorcheas.

   SÍMBOLOS: calderón y ligadura (`juegos_comun.simbolo`, el mismo
   vocabulario que ya usan el UNO y la Oca).

   Fusa y semifusa (tres y cuatro corchetes) NO existen en el motor
   compartido, que llega hasta la semicorchea porque ninguna partitura del
   cuaderno baja más: aquí se dibujan aparte, reutilizando el mismo trazo de
   corchete en curva de `notation.draw_note` y los glifos Unicode de
   silencio de fusa y semifusa (U+1D140, U+1D141), comprobados en FreeSerif
   antes de usarlos.

   Uso:  python3 juego_contrasena_puerta.py
         python3 juego_contrasena_puerta.py --medir     (rehace MEDIDAS)
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
# Dibujar una figura suelta, sin pentagrama
#
# Todas las funciones reciben (cx, ref_y, gap) y dibujan SIEMPRE al mismo
# `gap`: el que se le pase. Nada se reescala para llenar su hueco — de eso
# se encarga quien las llama, moviendo el punto de referencia.
#
#   - en una NOTA, `ref_y` es el centro de la cabeza;
#   - en un SILENCIO, la línea de en medio del pentagrama imaginario (que es
#     lo que `notation.draw_rest` usa de referencia);
#   - en un GRUPO, la fila de las cabezas (todas van en Si4);
#   - en un SÍMBOLO, su centro.
# --------------------------------------------------------------------------
def _flag_bezier(c, fx, fy, gap):
    """El mismo trazo curvo (bezier, no una cuña recta) con que
       `notation.draw_note` dibuja el corchete de una corchea o una
       semicorchea — copiado tal cual, porque el motor compartido no llega a
       fusa ni semifusa y un trazo nuevo no combinaría con el resto."""
    p = c.beginPath()
    p.moveTo(fx, fy)
    p.curveTo(fx + gap * 0.15, fy - gap * 0.25, fx + gap * 0.95, fy - gap * 0.05,
             fx + gap * 0.68, fy - gap * 1.25)
    p.curveTo(fx + gap * 0.62, fy - gap * 0.85, fx + gap * 0.22, fy - gap * 0.55,
             fx, fy - gap * 0.35)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def _dibuja_nota(c, cx, ref_y, gap, relleno, plica, corchetes, puntillo):
    """Una nota suelta. `relleno` decide cabeza rellena (negra y más cortas)
       o hueca (redonda y blanca) — que es LO ÚNICO que distingue una blanca
       de una negra, y por eso va como dato explícito y no deducido del
       número de corchetes."""
    nt.draw_notehead(c, cx, ref_y, gap, filled=relleno)
    if puntillo:
        c.setFillColor(nt.INK)
        c.circle(cx + gap * 1.05, ref_y + gap * 0.15, gap * 0.14, fill=1, stroke=0)
    if not plica:
        return
    stem_x = cx + gap * 0.6
    stem_top = ref_y + gap * 3.4
    c.setStrokeColor(nt.INK)
    c.setLineWidth(max(1.3, gap * 0.115))
    c.line(stem_x, ref_y, stem_x, stem_top)
    c.setFillColor(nt.INK)
    for k in range(corchetes):
        _flag_bezier(c, stem_x, stem_top - k * gap * 0.9, gap)


def _dibuja_silencio(c, cx, ref_y, gap, base):
    """Un silencio. Hasta semicorchea lo dibuja `notation.draw_rest` (con el
       mismo pentagrama imaginario que usa `juegos_comun.figura` por dentro);
       fusa y semifusa van con su glifo Unicode, que `draw_rest` no cablea.

       El de REDONDA y el de BLANCA son el mismo rectangulito y sueltos no
       hay quien los distinga, así que llevan dibujada la línea de la que
       penden: la blanca se apoya ENCIMA, la redonda cuelga DEBAJO."""
    if base in ('f', 'sf'):
        c.setFillColor(nt.INK)
        c.setFont('FreeSerif', gap * 2.6)
        c.drawCentredString(cx, ref_y - gap * 0.6,
                            '\U0001D140' if base == 'f' else '\U0001D141')
        return
    nt.draw_rest(c, cx, ref_y - 2 * gap, ref_y + 2 * gap, gap, base)
    if base in ('w', 'h'):
        # `draw_rest` apoya el de blanca EN `mid` y cuelga el de redonda de
        # `mid + gap`: la línea va justo donde toca en cada caso.
        y = ref_y if base == 'h' else ref_y + gap
        c.setStrokeColor(nt.INK)
        c.setLineWidth(max(0.7, gap * 0.075))
        c.line(cx - gap * 1.15, y, cx + gap * 1.15, y)


class _sin_barras(object):
    """`draw_system` remata siempre con una barra de compás a cada lado; en
       una ficha suelta no pinta nada. Se quita mientras dura el dibujo,
       igual que `juegos_comun._tinta` cambia la tinta, y se devuelve
       después sin excepciones."""

    def __enter__(self):
        self._orig = nt.draw_barline
        nt.draw_barline = lambda *a, **k: None
        return self

    def __exit__(self, *_e):
        nt.draw_barline = self._orig
        return False


class _sin_pentagrama(object):
    """Ídem con las cinco líneas: `draw_system` las pinta siempre detrás y
       aquí se pidió justo lo contrario. `draw_staff` no dibuja nada
       mientras dura el truco, pero sigue devolviendo las mismas cinco
       coordenadas Y que calcularía de verdad, así que el resto de
       `draw_system` (posición de las notas, plicas, barras) no se entera."""

    def __enter__(self):
        self._orig = nt.draw_staff

        def _fake(c, x, top_y, w, gap=9, lines=5):
            return [top_y - i * gap for i in range(lines)]
        nt.draw_staff = _fake
        return self

    def __exit__(self, *_e):
        nt.draw_staff = self._orig
        return False


# Cuánto separa a dos cabezas seguidas dentro de un grupo, en espacios de
# pentagrama. Cuantas más notas, más juntas — como en una edición de verdad,
# donde cuatro semicorcheas van más apretadas que dos corcheas. Y así el
# grupo de cuatro no obliga a encoger TODAS las figuras de la colección.
_PASO_GRUPO = {2: 1.35, 3: 1.15, 4: 0.95}
# Lo que `draw_system` se reserva a los lados pase lo que pase (4 pt a la
# izquierda y 8 a la derecha). Va aparte del ancho proporcional al `gap`
# para que el dibujo salga IGUAL a cualquier escala: si no, la medida en
# espacios de pentagrama dependería del gap con que se midió.
_ANCHO_FIJO = 12.0


def _ancho_grupo(n, gap):
    return n * _PASO_GRUPO.get(n, 1.15) * gap + _ANCHO_FIJO


def _dibuja_grupo(c, cx, ref_y, gap, eventos):
    """Un grupo de notas del mismo valor, dentro del pentagrama imaginario
       (ninguna pide línea adicional), sin clave, sin compás y sin
       pentagrama. `ref_y` es la fila de las cabezas, y `_ALTURA_GRUPO` dice
       a cuántos espacios queda de ahí la línea de arriba, que es lo que
       `draw_system` pide como `top_y`."""
    ancho = _ancho_grupo(len(eventos), gap)
    x = cx - ancho / 2.0
    c.saveState()
    with _sin_barras(), _sin_pentagrama():
        nt.draw_system(c, x, ref_y + _ALTURA_GRUPO * gap, ancho, gap, eventos,
                       clef='treble', show_clef=False, show_time=False,
                       spacing='engraved')
    c.restoreState()


def _dibuja_simbolo(c, cx, ref_y, gap, cual):
    simbolo(c, cx, ref_y, gap * 1.55, cual, INK)


# --------------------------------------------------------------------------
# EL CATÁLOGO. Cada entrada: (tipo, datos, peso).
#
# El peso es cuántas copias entran en el mazo. No es un nivel de dificultad
# (en blanco y negro no habría cómo marcarlo): es cómo de común es la figura.
# Negra, blanca, redonda, corchea y semicorchea —las que pidió el cliente—
# salen a montones para poder encadenar contraseñas largas; fusa, semifusa y
# los tresillos, unas pocas, para condimentar.
# --------------------------------------------------------------------------
# LA NOTA DE LOS GRUPOS ES UN LA4, NO UN SI4, Y NO ES CAPRICHO. `draw_system`
# decide hacia dónde va la plica de un grupo con `avg_cy > bot + 2*gap`, o
# sea comparando contra la línea de en medio del pentagrama. El Si4 CAE
# JUSTO en esa línea, así que la comparación queda en el filo: `avg_cy` sale
# de `sum(cys)/len(cys)` y ese promedio, con tres notas iguales, se va un ulp
# arriba o abajo según el número. Resultado real: a gap 24 el grupo salía con
# la plica hacia arriba y a gap 19,3 hacia abajo — con la barra por debajo de
# las cabezas y desbordando la ficha. Con el La4, medio espacio por debajo de
# la línea, la plica va hacia arriba SIEMPRE, sin depender del redondeo. Da
# igual qué nota sea: aquí no hay pentagrama, solo se lee la figura.
_PITCH_GRUPO = 'A4'
_ALTURA_GRUPO = 2.5      # espacios desde la cabeza hasta la línea de arriba


def _ev(dur, beam=None, tresillo=None):
    e = {'pitch': _PITCH_GRUPO, 'dur': dur}
    if beam is not None:
        e['beam'] = beam
    if tresillo is not None:
        e['tresillo'] = tresillo
    return e


def _nota(relleno, plica, corchetes, puntillo=False):
    return dict(relleno=relleno, plica=plica, corchetes=corchetes, puntillo=puntillo)


CATALOGO = [
    # ---- notas -----------------------------------------------------------
    ('redonda',          'nota', _nota(False, False, 0), 12),
    ('blanca',           'nota', _nota(False, True, 0), 12),
    ('blanca.',          'nota', _nota(False, True, 0, True), 6),
    ('negra',            'nota', _nota(True, True, 0), 12),
    ('negra.',           'nota', _nota(True, True, 0, True), 6),
    ('corchea',          'nota', _nota(True, True, 1), 12),
    ('corchea.',         'nota', _nota(True, True, 1, True), 6),
    ('semicorchea',      'nota', _nota(True, True, 2), 12),
    ('semicorchea.',     'nota', _nota(True, True, 2, True), 4),
    ('fusa',             'nota', _nota(True, True, 3), 4),
    ('semifusa',         'nota', _nota(True, True, 4), 4),
    # ---- silencios (sin puntillo, por decisión del cliente) ---------------
    ('sil-redonda',      'silencio', dict(base='w'), 10),
    ('sil-blanca',       'silencio', dict(base='h'), 10),
    ('sil-negra',        'silencio', dict(base='q'), 12),
    ('sil-corchea',      'silencio', dict(base='e'), 10),
    ('sil-semicorchea',  'silencio', dict(base='s'), 6),
    ('sil-fusa',         'silencio', dict(base='f'), 4),
    ('sil-semifusa',     'silencio', dict(base='sf'), 4),
    # ---- grupos del mismo valor -----------------------------------------
    ('2-corcheas',       'grupo', dict(eventos=[_ev('e', 1)] * 2), 8),
    ('3-corcheas',       'grupo', dict(eventos=[_ev('e', 1)] * 3), 6),
    ('4-corcheas',       'grupo', dict(eventos=[_ev('e', 1)] * 4), 6),
    ('2-semicorcheas',   'grupo', dict(eventos=[_ev('s', 1)] * 2), 6),
    ('4-semicorcheas',   'grupo', dict(eventos=[_ev('s', 1)] * 4), 6),
    ('tresillo-corcheas', 'grupo',
     dict(eventos=[_ev('e', beam=1, tresillo=1)] * 3), 6),
    ('tresillo-semis',   'grupo',
     dict(eventos=[_ev('s', beam=1, tresillo=1)] * 3), 4),
    # ---- símbolos --------------------------------------------------------
    ('calderon',         'simbolo', dict(cual='calderon'), 6),
    ('ligadura',         'simbolo', dict(cual='ligadura'), 6),
]

_POR_CLAVE = dict((clave, (tipo, datos)) for clave, tipo, datos, _p in CATALOGO)


def _dibuja(c, cx, ref_y, gap, clave):
    tipo, datos = _POR_CLAVE[clave]
    if tipo == 'nota':
        _dibuja_nota(c, cx, ref_y, gap, **datos)
    elif tipo == 'silencio':
        _dibuja_silencio(c, cx, ref_y, gap, datos['base'])
    elif tipo == 'grupo':
        _dibuja_grupo(c, cx, ref_y, gap, datos['eventos'])
    else:
        _dibuja_simbolo(c, cx, ref_y, gap, datos['cual'])


# --------------------------------------------------------------------------
# LAS MEDIDAS. Hasta dónde llega la TINTA de cada figura desde su punto de
# referencia, en espacios de pentagrama: (arriba, abajo, izquierda, derecha).
#
# No están estimadas: salen de dibujar cada figura, rasterizarla y mirar qué
# píxeles quedan pintados (`--medir`). Es la única forma de saber, por
# ejemplo, cuánto sube el "3" de un tresillo por encima de la plica, o dónde
# acaba de verdad el glifo del silencio de semifusa.
# --------------------------------------------------------------------------
MEDIDAS = {
    'redonda':               (0.57, 0.57, 0.72, 0.72),
    'blanca':                (3.46, 0.57, 0.72, 0.72),
    'blanca.':               (3.46, 0.57, 0.72, 1.24),
    'negra':                 (3.46, 0.51, 0.66, 0.70),
    'negra.':                (3.46, 0.51, 0.66, 1.24),
    'corchea':               (3.46, 0.51, 0.66, 1.38),
    'corchea.':              (3.46, 0.51, 0.66, 1.38),
    'semicorchea':           (3.46, 0.51, 0.66, 1.38),
    'semicorchea.':          (3.46, 0.51, 0.66, 1.38),
    'fusa':                  (3.46, 0.51, 0.66, 1.38),
    'semifusa':              (3.46, 0.59, 0.66, 1.38),
    # el silencio de redonda tiene la tinta ENTERA por encima de su linea de
    # referencia (cuelga de ella), de ahi el numero negativo hacia abajo
    'sil-redonda':           (1.09, -0.46, 1.21, 1.19),
    'sil-blanca':            (0.56, 0.08, 1.21, 1.19),
    'sil-negra':             (0.82, 0.83, 0.32, 0.33),
    'sil-corchea':           (0.84, 0.21, 0.36, 0.30),
    'sil-semicorchea':       (0.84, 0.70, 0.41, 0.39),
    'sil-fusa':              (1.34, 0.70, 0.49, 0.44),
    'sil-semifusa':          (1.32, 1.21, 0.54, 0.53),
    '2-corcheas':            (3.56, 0.51, 2.16, 0.62),
    '3-corcheas':            (3.56, 0.51, 2.52, 1.19),
    '4-corcheas':            (3.56, 0.51, 2.71, 1.57),
    '2-semicorcheas':        (3.56, 0.51, 2.16, 0.62),
    '4-semicorcheas':        (3.56, 0.51, 2.71, 1.57),
    'tresillo-corcheas':     (4.66, 0.51, 2.52, 1.19),
    'tresillo-semis':        (4.66, 0.51, 2.52, 1.19),
    'calderon':              (1.71, 0.43, 1.59, 1.57),
    'ligadura':              (1.01, 0.26, 1.62, 1.61),
}


def medir_todo(gap=24.0, dpi=300):
    """Dibuja cada figura sola en una hoja, la rasteriza y mide su tinta.
       Devuelve la tabla lista para pegar en `MEDIDAS`.

       Se comprueba a DOS escalas distintas: si una figura midiera distinto
       en espacios de pentagrama según el gap con que se dibuja, la tabla no
       valdría para nada (querría decir que algo de su dibujo NO es
       proporcional al gap, y entonces no se puede garantizar que quepa)."""
    import subprocess
    import tempfile
    from PIL import Image
    import numpy as np

    def _medir(clave, gap_test):
        lado = 460.0
        ref = lado / 2.0
        tmp = tempfile.mkdtemp()
        pdf = os.path.join(tmp, 'f.pdf')
        c = rl_canvas.Canvas(pdf, pagesize=(lado, lado))
        c.setFillColor(white)
        c.rect(0, 0, lado, lado, fill=1, stroke=0)
        _dibuja(c, ref, ref, gap_test, clave)
        c.save()
        subprocess.run(['pdftoppm', '-png', '-r', str(dpi), pdf,
                        os.path.join(tmp, 'p')], check=True)
        img = Image.open(os.path.join(tmp, 'p-1.png')).convert('L')
        arr = np.array(img) < 200
        ys, xs = np.where(arr)
        if len(ys) == 0:
            raise RuntimeError('la figura %s no ha pintado nada' % clave)
        esc = dpi / 72.0
        ref_px = ref * esc
        arriba = (ref_px - ys.min()) / esc / gap_test
        abajo = (ys.max() - ref_px) / esc / gap_test
        izq = (ref_px - xs.min()) / esc / gap_test
        der = (xs.max() - ref_px) / esc / gap_test
        return arriba, abajo, izq, der

    tabla, avisos = {}, []
    for clave, _t, _d, _p in CATALOGO:
        a1 = _medir(clave, gap)
        a2 = _medir(clave, gap * 0.6)
        if max(abs(x - y) for x, y in zip(a1, a2)) > 0.12:
            avisos.append('%s no escala igual: %s vs %s' % (clave, a1, a2))
        # se redondea hacia ARRIBA (a la centésima) y con un pelín de margen:
        # más vale sobrar dos décimas de milímetro que rozar el borde.
        tabla[clave] = tuple(round(max(x, y) + 0.05, 2) for x, y in zip(a1, a2))
    return tabla, avisos


# --------------------------------------------------------------------------
# La hoja. El GAP no se elige a ojo: es el más grande con el que la figura
# más alta y la más ancha SIGUEN cabiendo en su ficha, según `MEDIDAS`.
# --------------------------------------------------------------------------
MARGIN = 34
CONTENT_W = W - 2 * MARGIN
COLS, FILAS = 5, 6
POR_HOJA = COLS * FILAS
FICHA_W = CONTENT_W / COLS
CABECERA_H = 70
FICHA_H = (H - CABECERA_H - 40) / FILAS
AIRE = 11.0          # lo que se deja libre por dentro del filete de la ficha

_UTIL_W = FICHA_W - 2 * AIRE
_UTIL_H = FICHA_H - 2 * AIRE
GAP = min(min(_UTIL_H / (arr + aba), _UTIL_W / (izq + der))
          for arr, aba, izq, der in MEDIDAS.values())


def _tarjeta(c, x, y, w, h):
    """El filete de la ficha: fino y redondeado — bonito, y a la vez la guía
       de corte, sin necesitar una cuadrícula aparte."""
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.roundRect(x + 3, y + 3, w - 6, h - 6, 8, fill=0, stroke=1)


def _ficha(c, x, y, w, h, clave):
    """Una ficha: SOLO la figura, en tinta negra, al GAP común de toda la
       colección y CENTRADA POR SU PROPIA TINTA — no por su punto de
       referencia, que en una nota con plica está muy abajo y en un silencio
       de redonda muy arriba."""
    _tarjeta(c, x, y, w, h)
    arr, aba, izq, der = MEDIDAS[clave]
    ref_x = x + w / 2.0 + (izq - der) / 2.0 * GAP
    ref_y = y + h / 2.0 + (aba - arr) / 2.0 * GAP
    _dibuja(c, ref_x, ref_y, GAP, clave)


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


def construir_mazo():
    """El mazo entero, barajado con semilla fija para que la hoja salga
       siempre igual (se puede reimprimir una hoja suelta y encaja)."""
    mazo = []
    for clave, _tipo, _datos, veces in CATALOGO:
        mazo.extend([clave] * veces)
    random.Random(77).shuffle(mazo)
    return mazo


def construir(ruta=None, con_marco=True):
    os.makedirs(SALIDA, exist_ok=True)
    ruta = ruta or os.path.join(SALIDA, 'Contrasena_de_la_puerta.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('La contraseña de la puerta')

    mazo = construir_mazo()
    total_paginas = -(-len(mazo) // POR_HOJA)     # division hacia arriba
    x0 = MARGIN
    y0 = H - CABECERA_H - FILAS * FICHA_H - 10

    pagina = 1
    while mazo:
        lote, mazo = mazo[:POR_HOJA], mazo[POR_HOJA:]
        _cabecera_pagina(c, pagina, total_paginas)
        for k, clave in enumerate(lote):
            x = x0 + (k % COLS) * FICHA_W
            y = y0 + (FILAS - 1 - k // COLS) * FICHA_H
            if con_marco:
                _ficha(c, x, y, FICHA_W, FICHA_H, clave)
            else:
                arr, aba, izq, der = MEDIDAS[clave]
                _dibuja(c, x + FICHA_W / 2.0 + (izq - der) / 2.0 * GAP,
                        y + FICHA_H / 2.0 + (aba - arr) / 2.0 * GAP, GAP, clave)
        c.showPage()
        pagina += 1

    c.save()
    return ruta


def comprobar_fichas(dpi=200):
    """LA COMPROBACIÓN QUE IMPORTA: que NINGUNA figura se salga de su ficha.

       No se fía de la tabla ni de las cuentas: monta la hoja de verdad SIN
       el filete (para que en cada celda no haya más que la figura),
       rasteriza, y mira ficha por ficha que toda la tinta caiga dentro del
       recuadro. Devuelve (holgura_minima, lista_de_desbordes).

       Existe porque el fallo real fue justo del tipo que una cuenta no
       pilla: `draw_system` decide la plica de un grupo comparando contra la
       línea de en medio, y con las notas JUSTO en esa línea el resultado
       cambiaba según el redondeo del gap — la figura medía una cosa al
       medirla y otra al imprimirla."""
    import subprocess
    import tempfile
    from PIL import Image
    import numpy as np

    tmp = tempfile.mkdtemp()
    pdf = os.path.join(tmp, 'sin_marco.pdf')
    construir(ruta=pdf, con_marco=False)
    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), pdf,
                    os.path.join(tmp, 'p')], check=True)

    esc = dpi / 72.0
    mazo = construir_mazo()
    y0 = H - CABECERA_H - FILAS * FICHA_H - 10
    peor, malos = None, []
    for pi, fn in enumerate(sorted(f for f in os.listdir(tmp) if f.endswith('.png'))):
        arr = np.array(Image.open(os.path.join(tmp, fn)).convert('L')) < 200
        for k, clave in enumerate(mazo[pi * POR_HOJA:(pi + 1) * POR_HOJA]):
            x = MARGIN + (k % COLS) * FICHA_W
            y = y0 + (FILAS - 1 - k // COLS) * FICHA_H
            # se mira la celda ENTERA, no solo el recuadro: así se ve también
            # la tinta que se ha ido a invadir la ficha de al lado
            cx1, cx2 = int(x * esc), int((x + FICHA_W) * esc)
            cr1, cr2 = int((H - y - FICHA_H) * esc), int((H - y) * esc)
            ys, xs = np.where(arr[max(0, cr1):cr2, cx1:cx2])
            if len(ys) == 0:
                malos.append((pi + 1, clave, 'no ha pintado nada'))
                continue
            holgura = min((cr1 + ys.min()) - (H - y - FICHA_H + 3) * esc,
                          (H - y - 3) * esc - (cr1 + ys.max()),
                          (cx1 + xs.min()) - (x + 3) * esc,
                          (x + FICHA_W - 3) * esc - (cx1 + xs.max())) / esc
            if holgura < 0:
                malos.append((pi + 1, clave, 'se sale %.1f pt' % -holgura))
            if peor is None or holgura < peor[0]:
                peor = (holgura, clave)
    return peor, malos


def main(argv):
    if '--comprobar' in argv:
        peor, malos = comprobar_fichas()
        print('la ficha más justa: %.2f pt de holgura (%s)' % peor)
        print('fichas que se salen: %d' % len(malos))
        for m in malos[:20]:
            print('  ', m)
        return 1 if malos else 0
    if '--medir' in argv:
        tabla, avisos = medir_todo()
        print('MEDIDAS = {')
        for clave, _t, _d, _p in CATALOGO:
            print('    %-22s %s,' % ("'%s':" % clave, tabla[clave]))
        print('}')
        for a in avisos:
            print('AVISO:', a)
        return 0
    ruta = construir()
    print('La contraseña de la puerta · %s  (gap %.1f, %d fichas)'
          % (os.path.basename(ruta), GAP, len(construir_mazo())))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
