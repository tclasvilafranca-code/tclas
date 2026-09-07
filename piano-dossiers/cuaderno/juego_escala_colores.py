# -*- coding: utf-8 -*-
"""LA ESCALA DE COLORES — un pentagrama ancho, en A3 apaisada, con las siete
   notas de Do a Si pintadas cada una de su color: el sistema de colorines que
   se usa para que un niño pequeño empiece a leer antes de saber solfeo de
   verdad — la nota se reconoce por el color antes que por la posición.

   Pedido explícito del cliente: Do rojo, Re naranja, Mi amarillo, Fa verde,
   Sol azul, La lila, Si gris. Esos siete colores y no otros.

   Va en A3 apaisada (el mismo truco de `juego_oca.py`: `setPageSize` solo en
   esta página) porque un pentagrama "ancho" de verdad — las siete notas
   respirando, no apretadas en un A4 — es la gracia de la hoja: se cuelga en
   la pared o se pone sobre la mesa entre el alumno y el teclado.

   Tres piezas, de arriba abajo: el pentagrama con las cabezas de color (lo
   que se PIDIÓ), la leyenda de colores (para confirmar el código sin tener
   que leer el pentagrama) y una tira de teclado con las mismas siete teclas
   pintadas (para que el niño pase del papel a las teclas sin traducir nada).

   Uso:  python3 juego_escala_colores.py
"""
import os
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from juegos_comun import (NAVY, CREAM, INK, MUTED, RULE,                     # noqa: E402
                          JUEGO_DISPLAY_BLACK, JUEGO_DISPLAY_ITALIC,
                          JUEGO_BODY, JUEGO_BODY_BOLD, JUEGO_BODY_BLACK,
                          _con_tracking)
from notation import (draw_staff, draw_clef, note_y, draw_ledger,            # noqa: E402
                      ledger_lines_needed, BLEED_SAFE)

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

BW, BH = landscape(A3)          # 1190.55 x 841.89 — apaisada de verdad
MARGIN = 54
CONTENT_W = BW - 2 * MARGIN

# Las siete notas, en el orden pedido, con SU color y su nombre en solfeo.
# El gris de Si se sube un punto de saturación (no un gris de "desactivado")
# para que no lea como una nota "apagada" al lado de las otras seis vivas.
ESCALA = [
    ('C4', 'DO',  HexColor('#D2483C')),
    ('D4', 'RE',  HexColor('#E8862B')),
    ('E4', 'MI',  HexColor('#E5C230')),
    ('F4', 'FA',  HexColor('#4E9B4E')),
    ('G4', 'SOL', HexColor('#3B72B4')),
    ('A4', 'LA',  HexColor('#8C6BC1')),
    ('B4', 'SI',  HexColor('#7D7D7D')),
]


def _cabeza_color(c, cx, cy, r, color):
    """Una cabeza de nota grande y de color, con un filete oscuro fino — el
       gesto de un "botón" de color, no el de una cabeza de partitura al uso:
       aquí lo que hay que leer primero es el color, y la forma de nota real
       (ovalada, con plica) se aprende después."""
    c.setFillColor(color)
    c.setStrokeColor(INK)
    c.setLineWidth(1.4)
    c.circle(cx, cy, r, fill=1, stroke=1)
    c.setStrokeColor(white)
    c.setLineWidth(1.0)
    c.circle(cx, cy, r * 0.68, fill=0, stroke=1)


def _cabecera(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, BW, BH, fill=1, stroke=0)
    b = BLEED_SAFE
    c.setFillColor(NAVY)
    c.rect(b, BH - 118 - b, BW - 2 * b, 118, fill=1, stroke=0)
    c.setFont(JUEGO_BODY_BOLD, 8.6)
    c.setFillColor(HexColor('#9FB0C4'))
    _con_tracking(c, MARGIN, BH - 38, 'MATERIAL DE CLASE · EL CUADERNO DEL PIANISTA', 1.1)
    c.setFont(JUEGO_DISPLAY_BLACK, 38)
    c.setFillColor(white)
    c.drawString(MARGIN, BH - 78, 'La escala de colores')
    c.setFont(JUEGO_DISPLAY_ITALIC, 13.5)
    c.setFillColor(HexColor('#C3CEDB'))
    c.drawString(MARGIN, BH - 100,
                'Do-Re-Mi-Fa-Sol-La-Si, cada nota con su color · para leer antes de leer')


def _pentagrama(c, y_top):
    """El pentagrama ancho con las siete cabezas de color, repartidas a lo
       ANCHO de toda la A3 — la gracia de la hoja, y lo que se pidió."""
    gap = 30.0
    ys = draw_staff(c, MARGIN, y_top, CONTENT_W, gap=gap)
    top, bot = ys[0], ys[-1]
    draw_clef(c, MARGIN + 6, bot, gap, clef='treble')

    r = gap * 0.78
    x0 = MARGIN + gap * 6.4          # deja sitio a la clave
    x1 = BW - MARGIN - r * 1.2
    n = len(ESCALA)
    paso = (x1 - x0) / (n - 1)

    for i, (pitch, nombre, color) in enumerate(ESCALA):
        cx = x0 + i * paso
        cy = note_y(bot, gap, pitch, clef='treble')
        for ly in ledger_lines_needed(bot, top, cy, gap):
            draw_ledger(c, cx, ly, gap)
        _cabeza_color(c, cx, cy, r, color)
        c.setFont(JUEGO_BODY_BLACK, 15)
        c.setFillColor(NAVY)
        c.drawCentredString(cx, bot - gap * 3.35, nombre)

    return bot - gap * 4.4


def _leyenda(c, y_top):
    """La tira de colores de abajo: confirma el código sin tener que saber
       leer el pentagrama todavía — para el primer día, antes de la primera
       clase de lectura."""
    c.setFont(JUEGO_BODY_BOLD, 10.5)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y_top, 'LEYENDA DE COLORES')
    y = y_top - 30

    n = len(ESCALA)
    chip = 34
    hueco = (CONTENT_W - n * chip) / (n - 1)
    x = MARGIN
    for pitch, nombre, color in ESCALA:
        c.setFillColor(color)
        c.setStrokeColor(INK)
        c.setLineWidth(1.1)
        c.roundRect(x, y - chip, chip, chip, 8, fill=1, stroke=1)
        c.setFont(JUEGO_BODY_BLACK, 12)
        c.setFillColor(NAVY)
        c.drawCentredString(x + chip / 2.0, y - chip - 20, nombre)
        x += chip + hueco
    return y - chip - 38


def _teclado(c, y_top):
    """Siete teclas blancas, pintadas del mismo color que su nota — para que
       el salto del papel al piano de verdad sea directo: el color que se ve
       en la hoja es el color que se toca."""
    c.setFont(JUEGO_BODY_BOLD, 10.5)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y_top, 'Y EN EL TECLADO')
    y = y_top - 16

    n = len(ESCALA)
    alto = 92
    ancho = CONTENT_W / n
    x = MARGIN
    for pitch, nombre, color in ESCALA:
        c.setFillColor(color)
        c.setStrokeColor(INK)
        c.setLineWidth(1.1)
        c.roundRect(x + 2, y - alto, ancho - 4, alto, 7, fill=1, stroke=1)
        c.setFont(JUEGO_BODY_BLACK, 14)
        c.setFillColor(white)
        c.drawCentredString(x + ancho / 2.0, y - alto + 14, nombre)
        x += ancho
    return y - alto


def _pie(c):
    c.setFont(JUEGO_DISPLAY_ITALIC, 9)
    c.setFillColor(MUTED)
    c.drawCentredString(BW / 2.0, 24, 'El Cuaderno del Pianista · T-Clas')


def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Escala_de_colores.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(BW, BH))
    c.setTitle('La escala de colores')

    _cabecera(c)
    y = BH - 118 - 56
    y = _pentagrama(c, y)
    y -= 34
    y = _leyenda(c, y)
    y -= 20
    y = _teclado(c, y)
    _pie(c)
    c.showPage()
    c.save()
    return ruta


def main(argv):
    ruta = construir()
    print('Escala de colores · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
