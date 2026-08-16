# -*- coding: utf-8 -*-
"""Hoja de CALENTAMIENTO DE DEDOS: la hoja entera de pentagramas.

   Rediseno pedido por el cliente. Antes eran cuatro o cinco ejercicios con
   su titulo y su explicacion; ahora es lo que pidio literalmente: "toda la
   hoja de pentagrama arriba abajo derecha izquierda con notas", con
   silencios, con todas las figuras y jugando con distintos compases y con
   las dos claves del piano.

   Las lineas se generan (engine/generador_lectura.py) a partir de la
   tonalidad de la pieza y del numero de cancion, que hace de semilla: la
   hoja de la cancion 7 es siempre la misma hoja, pero no se parece a la de
   la 6. Y el nivel sube con el numero, asi que en septiembre hay negras y
   blancas y en junio hay corcheas, puntillos y silencios.

   Cada linea va numerada. No es decorativo: en clase se dice "hoy del 1 al
   6" y la semana siguiente "del 7 al 12".
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_system
from page_layout_common import before_staff, after_system
from generador_lectura import hoja as generar_hoja
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)  # noqa

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')

GAP = 6.6
NUM_W = 17          # ancho de la columna de numeros, a la izquierda
SUELO = 48          # por debajo de esto empieza el pie de pagina


def cabecera(c, cfg, titulo, esquina, intro, reglas):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, cfg['kicker'].upper())
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, esquina)
    y -= 27

    c.setFont('DejaVuSerif-Bold', 23)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, titulo)
    y -= 14
    y = _wrap(c, intro, MARGIN, y, 'DejaVuSans', 8.8, CONTENT_W, 11.0, MUTED)
    y -= 7

    bh = 21
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - bh, CONTENT_W, bh, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - bh, 3, bh, fill=1, stroke=0)
    size = 8.0
    while size > 6.0 and (sum(stringWidth(r, 'DejaVuSans-Bold', size) for r in reglas)
                          + 24 * (len(reglas) - 1)) > CONTENT_W - 26:
        size -= 0.2
    rx = MARGIN + 13
    for i, r in enumerate(reglas):
        c.setFont('DejaVuSans-Bold', size)
        c.setFillColor(NAVY)
        c.drawString(rx, y - 13.5, r)
        rx += stringWidth(r, 'DejaVuSans-Bold', size)
        if i < len(reglas) - 1:
            c.setFillColor(ACCENT)
            c.circle(rx + 12, y - 10.5, 1.7, fill=1, stroke=0)
            rx += 24
    return y - bh - 12


def rellenar(c, y, lineas, gap=GAP, key_sig=None, desde=1, suelo=SUELO):
    """Dibuja lineas numeradas hasta abajo. Devuelve (y, cuantas).

       Dos pasadas. La primera cuenta cuantas caben; la segunda reparte el
       hueco que sobra entre ellas, igual que hace una partitura publicada
       cuando justifica los sistemas de una pagina. Sin esto, la hoja acaba
       con un palmo de papel en blanco al pie por muy llena que este arriba."""
    x = MARGIN + NUM_W
    ancho = CONTENT_W - NUM_W

    def alto(ln):
        return (before_staff(gap, ln['events'], ln['clef']) + 4 * gap
                + after_system(gap, ln['events'], ln['clef']))

    caben, usado = [], 0.0
    for ln in lineas:
        if y - usado - alto(ln) < suelo:
            break
        caben.append(ln)
        usado += alto(ln)
    if not caben:
        return y, 0
    extra = max(0.0, (y - usado - suelo) / len(caben))
    extra = min(extra, 16.0)

    num = desde
    for ln in caben:
        ev = ln['events']
        y -= before_staff(gap, ev, ln['clef']) + extra / 2.0
        c.setFont('DejaVuSans-Bold', 8.2)
        c.setFillColor(ACCENT)
        c.drawRightString(MARGIN + NUM_W - 7, y - 2 * gap - 3, str(num))
        top, bot = draw_system(c, x, y, ancho, gap, ev, clef=ln['clef'],
                               time_sig=ln['time_sig'], show_time=True,
                               key_sig=key_sig, spacing='engraved')
        y = bot - after_system(gap, ev, ln['clef']) - extra / 2.0
        num += 1
    return y, num - desde


def pie(c, cfg):
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()


def build_calentamiento(c, cfg):
    ton = cfg.get('key_sig')
    nombre_ton = ton if ton else 'Do mayor'
    intro = ('Cinco minutos antes de abrir la partitura. Se lee y se toca de arriba abajo, sin pararse '
             'en los fallos: esto no se estudia, se recorre. Cada línea lleva su número, su clave y su '
             'compás, y todo está en %s, la tonalidad de la pieza.' % nombre_ton)
    reglas = cfg.get('reglas') or ['MANOS SEPARADAS', 'MUY LENTO AL PRINCIPIO',
                                   'NO PARES EN LOS FALLOS']

    y = cabecera(c, cfg, 'Calentamiento de dedos',
                 'Calentamiento · antes de la partitura', intro, reglas)

    lineas = generar_hoja(nombre_ton, semilla=cfg.get('semilla', 1),
                          n_lineas=22, nivel=cfg.get('nivel_lectura', 1),
                          compases=cfg.get('compases_linea', 5),
                          compases_extra=cfg.get('compases_extra',
                                                 [(4, 4), (3, 4), (4, 4), (6, 8)]),
                          salto_max=cfg.get('salto_max', 3))
    y, _ = rellenar(c, y, lineas, gap=cfg.get('gap', GAP), key_sig=ton)
    pie(c, cfg)
    return y
