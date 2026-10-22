# -*- coding: utf-8 -*-
"""DOSIER DE AGUDEZA VISUAL EN A3 — diez hojas sueltas, nivel sencillo, para
   practicar la lectura de las dos claves del piano en papel grande.

   Es la misma lógica de `hoja_lectura.py` (la hoja de agudeza visual que ya
   lleva cada dosier de alumno: se recorre diciendo el nombre de cada nota EN
   VOZ ALTA, sin tocar el piano) pero suelta de cualquier canción, a tamaño
   A3 y en nivel 0 — el escalón más sencillo de `generador_lectura.py`: solo
   redondas, blancas, negras y algún silencio de negra, nunca corcheas ni
   puntillos. El tamaño grande y el nivel bajo van juntos a propósito: es
   material para los primeros pasos, antes de que la letra pequeña de un A4
   sea cómoda de seguir.

   Las diez hojas se reparten en dos bloques de cinco, una clave por bloque
   (CINCO EN CLAVE DE SOL, CINCO EN CLAVE DE FA) y no mezcladas dentro de la
   misma hoja: mezclar las dos claves en una sola línea es lo que hace
   `hoja_lectura.py` para un alumno que ya lee las dos, pero aquí el nivel es
   el de quien todavía está aprendiendo cada clave por separado.

   Reutiliza el motor de lectura tal cual (`generador_lectura.hoja`, con las
   reglas de anti-secuencia y de "cada línea cierra su compás" ya
   incorporadas) y el cálculo de espaciado de `page_layout_common`
   (`before_staff`/`after_system`), que no depende del tamaño de página — la
   única pieza propia de este archivo es la maquetación a A3.

   Uso:  python3 build_agudeza_a3.py
"""
import os
import sys

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from notation import draw_system, BLEED_SAFE                                 # noqa: E402
from page_layout_common import before_staff, after_system                    # noqa: E402
from generador_lectura import hoja as generar_hoja                           # noqa: E402
from portada import NAVY, NAVY_SOFT, CREAM, RULE, INK, MUTED, ACCENT, _wrap  # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output')

BW, BH = A3                     # 841.89 x 1190.55 — A3 vertical
MARGIN = 50
CONTENT_W = BW - 2 * MARGIN
NUM_W = 24
SUELO = 66
GAP = 10.4
PANEL = HexColor('#F3F1EA')

TITULO = 'Agudeza visual'
NOMBRE_CLAVE = {'treble': 'Clave de Sol', 'bass': 'Clave de Fa'}


def cabecera(c, clef, bloque_num, total_bloque, page_num, total_paginas):
    c.setFillColor(CREAM)
    c.rect(0, 0, BW, BH, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(BLEED_SAFE, BH - 7 - BLEED_SAFE, BW - 2 * BLEED_SAFE, 7, fill=1, stroke=0)

    y = BH - 52
    c.setFont('DejaVuSans-Bold', 10.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'AGUDEZA VISUAL · NIVEL SENCILLO'.upper())
    c.setFont('DejaVuSans', 10.4)
    c.setFillColor(MUTED)
    c.drawRightString(BW - MARGIN, y, 'Hoja %d de %d' % (page_num, total_paginas))
    y -= 34

    c.setFont('DejaVuSerif-Bold', 30)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, '%s — %s' % (TITULO, NOMBRE_CLAVE[clef]))
    y -= 19
    intro = ('Se recorre la hoja diciendo el nombre de cada nota EN VOZ ALTA, línea por línea y '
            'sin saltarse ninguna. Nada de tocar el piano todavía: primero se lee. %s de %d en %s.'
            % (bloque_num, total_bloque, NOMBRE_CLAVE[clef].lower()))
    y = _wrap(c, intro, MARGIN, y, 'DejaVuSans', 11.0, CONTENT_W, 14.5, MUTED)
    y -= 9

    reglas = ['EN VOZ ALTA, SIEMPRE', 'SIN TOCAR EL PIANO', 'NO ADIVINES: LEE']
    bh = 27
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - bh, CONTENT_W, bh, 5, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - bh, 4, bh, fill=1, stroke=0)
    rx = MARGIN + 17
    for i, r in enumerate(reglas):
        c.setFont('DejaVuSans-Bold', 10.2)
        c.setFillColor(NAVY)
        c.drawString(rx, y - bh / 2.0 - 3.6, r)
        rx += stringWidth(r, 'DejaVuSans-Bold', 10.2)
        if i < len(reglas) - 1:
            c.setFillColor(ACCENT)
            c.circle(rx + 15, y - bh / 2.0, 2.2, fill=1, stroke=0)
            rx += 30
    return y - bh - 20


def pie(c, page_num, total_paginas):
    c.setFont('DejaVuSans', 9.0)
    c.setFillColor(MUTED)
    c.drawCentredString(BW / 2.0, 30, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(BW - MARGIN, 30, '%d / %d' % (page_num, total_paginas))
    c.showPage()


def rellenar(c, y, lineas, clef):
    """Igual que `hoja_calentamiento.rellenar`, pero a la geometría de esta
       A3: dos pasadas, la segunda reparte el sobrante para que la hoja
       quede cuadrada por abajo y no se quede corta ni se desborde."""
    x = MARGIN + NUM_W
    ancho = CONTENT_W - NUM_W

    def alto(ln):
        return (before_staff(GAP, ln['events'], clef) + 4 * GAP
                + after_system(GAP, ln['events'], clef))

    caben, usado = [], 0.0
    for ln in lineas:
        if y - usado - alto(ln) < SUELO:
            break
        caben.append(ln)
        usado += alto(ln)
    if not caben:
        return y
    extra = min(20.0, max(0.0, (y - usado - SUELO) / len(caben)))

    num = 1
    for ln in caben:
        ev = ln['events']
        y -= before_staff(GAP, ev, clef) + extra / 2.0
        c.setFont('DejaVuSans-Bold', 11.0)
        c.setFillColor(ACCENT)
        c.drawRightString(MARGIN + NUM_W - 9, y - 2 * GAP - 4, str(num))
        top, bot = draw_system(c, x, y, ancho, GAP, ev, clef=clef,
                               time_sig=ln['time_sig'], show_time=True,
                               spacing='engraved')
        y = bot - after_system(GAP, ev, clef) - extra / 2.0
        num += 1
    return y


def hoja_a3(c, clef, bloque_num, total_bloque, page_num, total_paginas, semilla):
    y = cabecera(c, clef, bloque_num, total_bloque, page_num, total_paginas)
    lineas = generar_hoja('Do mayor', semilla=semilla, n_lineas=26, nivel=0,
                          compases=4, claves=(clef,), salto_max=3)
    y = rellenar(c, y, lineas, clef)
    pie(c, page_num, total_paginas)
    return y


def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Agudeza_visual_A3.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(BW, BH))
    c.setTitle('Agudeza visual · nivel sencillo')

    total_paginas = 10
    page_num = 1
    for i in range(5):
        hoja_a3(c, 'treble', i + 1, 5, page_num, total_paginas, semilla=2000 + i)
        page_num += 1
    for i in range(5):
        hoja_a3(c, 'bass', i + 1, 5, page_num, total_paginas, semilla=3000 + i)
        page_num += 1

    c.save()
    return ruta


def main(argv):
    ruta = construir()
    print('Agudeza visual A3 · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
