# -*- coding: utf-8 -*-
"""Hoja de TEORIA del curso de Pekes.

   No es un diseno nuevo: es la misma hoja de los albumes de alumno (la
   cabecera de `hoja_piano`, los recuadros y la tira de datos de
   `ficha_info`, el teclado dibujado, el pentagrama del motor) montada para
   explicar UN concepto en vez de presentar una partitura. Peticion del
   cliente tras descartar un diseno propio: "coge el motor de diseno de los
   albumes y siguelos igual, solo que mas infantil, resumido y didactico".

   Se compone por bloques, como las hojas al piano y los deberes:

     misol       el recuadro del buho (ver `misol.py`)
     teclado     un teclado dibujado con teclas marcadas
     pentagrama  notas sueltas con su nombre debajo
     tarjetas    la fila de tarjetas de la ficha
     puntos      lista de cosas que hay que saber
     nota        el recuadro "la clave de todo"
     sabias      el "¿Sabias que...?"
"""
import io
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.pdfgen.canvas import Canvas

from notation import draw_staff, draw_clef, draw_note, note_y
from portada import W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, ACCENT, MUTED, _wrap
from ficha_info import draw_keyboard, tarjetas, _section_title, _bullets, _note_box, BLUE
from hoja_piano import _cabecera, _pie, nota_clave
from misol import caja_misol

OBJETIVO = 88.0
AIRE_MAX = 26.0


def _teclado(c, y, b):
    y = _section_title(c, MARGIN, y, b['titulo'])
    n = b.get('teclas', 10)
    kh = b.get('alto', 74)
    kw = CONTENT_W / float(n)
    marcas = {gi: (BLUE, etq, 0) for gi, etq in b.get('marcas', {}).items()}
    # los rotulos de las teclas marcadas van ENCIMA del teclado
    y -= 18 if marcas else 0
    bot = draw_keyboard(c, MARGIN, y, n, kw, kh, marks=marcas, start_idx=b.get('inicio', 0))
    y = bot - 14
    if b.get('pie'):
        y = _wrap(c, b['pie'], MARGIN, y, 'DejaVuSans', 8.6, CONTENT_W, 11.4, MUTED)
    return y - 4


def _pentagrama(c, y, b):
    y = _section_title(c, MARGIN, y, b['titulo'])
    gap = b.get('gap', 10.0)
    y -= gap * 1.8
    ys = draw_staff(c, MARGIN, y, CONTENT_W, gap=gap)
    top, bot = ys[0], ys[-1]
    draw_clef(c, MARGIN + 6, bot, gap, clef='treble')
    notas = b['notas']
    x0 = MARGIN + gap * 9
    paso = (CONTENT_W - gap * 12) / max(1, len(notas) - 1)
    # todos los nombres en la MISMA linea, por debajo de la nota mas baja:
    # cada uno debajo de su nota quedaban a tres alturas y el del Do se
    # pegaba al texto de debajo
    base = min([bot] + [note_y(bot, gap, p) for p, _ in notas]) - gap * 2.4
    for i, (pitch, nombre) in enumerate(notas):
        cx = x0 + i * paso
        draw_note(c, cx, bot, top, gap, pitch, dur='w', clef='treble')
        c.setFont('DejaVuSans-Bold', 11)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, base, nombre)
    y = base - gap * 1.8
    if b.get('pie'):
        y = _wrap(c, b['pie'], MARGIN, y, 'DejaVuSans', 8.6, CONTENT_W, 11.4, MUTED)
    return y - 4


def _tarjetas(c, y, b):
    y = _section_title(c, MARGIN, y, b['titulo'])
    return tarjetas(c, y, b['items']) - 14


def _puntos(c, y, b):
    y = _section_title(c, MARGIN, y, b['titulo'])
    return _bullets(c, MARGIN, y, CONTENT_W, b['items'], size=9.2, leading=12.4) - 6


def _sabias(c, y, b):
    return _note_box(c, MARGIN, y, CONTENT_W, '¿Sabías que…?', b['texto'], NAVY_SOFT) - 10


def _bloque(c, y, b):
    tipo = b['tipo']
    if tipo == 'misol':
        return caja_misol(c, y, b['texto'], b.get('etiqueta', 'MUSOL MISOL DICE'),
                          b.get('pose', 'normal'))
    if tipo == 'nota':
        return nota_clave(c, y, b['texto'], b.get('etiqueta', 'PARA RECORDAR'))
    return {'teclado': _teclado, 'pentagrama': _pentagrama, 'tarjetas': _tarjetas,
            'puntos': _puntos, 'sabias': _sabias}[tipo](c, y, b)


def _aire(cfg, y0):
    """Igual que `hoja_piano._aire`: lo que sobra de hoja se reparte entre los
       bloques, con tope, en vez de quedarse todo junto al final."""
    prueba = Canvas(io.BytesIO(), pagesize=(W, H))
    y = y0
    for b in cfg['bloques']:
        y = _bloque(prueba, y, b)
    sobra = y - OBJETIVO
    huecos = max(1, len(cfg['bloques']) - 1)
    return max(0.0, min(AIRE_MAX, sobra / huecos))


def build_teoria(c, cfg):
    y = _cabecera(c, cfg)
    aire = _aire(cfg, y)
    for b in cfg['bloques']:
        y = _bloque(c, y, b) - aire
    _pie(c, cfg)
    return y + aire
