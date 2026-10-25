# -*- coding: utf-8 -*-
"""Hoja de AGUDEZA VISUAL: la hoja llena de notas para recitar en voz alta.

   Rediseno pedido por el cliente. Igual que el calentamiento, pero para el
   OJO y la BOCA, no para los dedos: el alumno recorre la hoja diciendo el
   nombre de cada nota en voz alta, sin tocar el piano.

   Diferencias con el calentamiento, que no son de forma sino de fondo:
     - los saltos son mas grandes (ahi se toca, aqui solo se lee);
     - el registro es mas ancho, con lineas adicionales;
     - se numeran las lineas igual, para poder mandar tramos.

   ANTI-SECUENCIA: si las notas siguen un patron, el alumno lo adivina y deja
   de leer. El generador elige saltos y ritmos al azar y comprueba que dos
   lineas seguidas no empiecen igual.

   Y abajo, un recuadro pequeno de ESCUCHA: lo dirige quien este al lado y el
   alumno responde sin mirar el teclado. Ocupa poco a proposito — el peso de
   la hoja esta en leer.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from generador_lectura import hoja as generar_hoja
from hoja_calentamiento import cabecera, rellenar, pie
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE,
                     INK, MUTED, ACCENT, _fit, _wrap)

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')
WARM = HexColor('#F4EFE3')

GAP = 6.6
ALTO_ESCUCHA = 104          # lo que se reserva abajo para el recuadro


def caja_escucha(c, y, preguntas, sub=None):
    """El recuadro de oido, al pie. Dos columnas: lo que toca quien acompana
       y las casillas que rodea el alumno."""
    h = ALTO_ESCUCHA
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)

    c.setFont('DejaVuSans-Bold', 9.2)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + 14, y - 15, 'ESCUCHA')
    tw = stringWidth('ESCUCHA', 'DejaVuSans-Bold', 9.2)
    c.setFont('DejaVuSans', 7.8)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 14 + tw + 10, y - 15,
                 sub or 'no mires el teclado · rodea con lápiz lo que oigas')

    yy = y - 30
    for letra, texto, opciones, n in preguntas:
        c.setFillColor(NAVY)
        c.circle(MARGIN + 19, yy - 3, 6.4, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 7.4)
        c.setFillColor(white)
        c.drawCentredString(MARGIN + 19, yy - 5.4, letra)

        # casillas a la derecha: n huecos, cada uno con las opciones dentro
        ancho_op = max(stringWidth(o, 'DejaVuSans', 7.2) for o in opciones) + 7
        celda = ancho_op * len(opciones) + 6
        bx = MARGIN + CONTENT_W - 14 - celda * n - 4 * (n - 1)

        ts = _fit(texto, 'DejaVuSans', 8.0, bx - (MARGIN + 31) - 12, floor=6.6)
        c.setFont('DejaVuSans', ts)
        c.setFillColor(INK)
        c.drawString(MARGIN + 31, yy - 6, texto)
        for _ in range(n):
            c.setStrokeColor(RULE)
            c.setLineWidth(0.7)
            c.setFillColor(white)
            c.roundRect(bx, yy - 13, celda, 15, 2, fill=1, stroke=1)
            ox = bx + 3
            for o in opciones:
                c.setFont('DejaVuSans', 7.2)
                c.setFillColor(NAVY_SOFT)
                c.drawCentredString(ox + ancho_op / 2, yy - 8.6, o)
                ox += ancho_op
            bx += celda + 4
        yy -= 21
    return y - h - 8


def build_lectura(c, cfg):
    ton = cfg.get('key_sig')
    nombre_ton = ton if ton else 'Do mayor'
    intro = ('Ni una nota al piano. Se recorre la hoja diciendo el nombre de cada nota EN VOZ ALTA, '
             'línea por línea y sin saltarse ninguna. Al principio despacio; cuando salga solo, con el '
             'metrónomo. Todo está en %s.' % nombre_ton)
    reglas = cfg.get('reglas_leer') or ['EN VOZ ALTA, SIEMPRE', 'SIN TOCAR EL PIANO',
                                        'NO ADIVINES: LEE']

    y = cabecera(c, cfg, 'Agudeza visual', 'Agudeza · leer sin tocar', intro, reglas)

    lineas = generar_hoja(nombre_ton, semilla=1000 + cfg.get('semilla', 1),
                          n_lineas=22, nivel=cfg.get('nivel_lectura', 1),
                          compases=cfg.get('compases_linea', 5),
                          compases_extra=cfg.get('compases_extra',
                                                 [(4, 4), (3, 4), (4, 4), (2, 4)]),
                          salto_max=cfg.get('salto_leer', 5))
    y_caja = 52 + ALTO_ESCUCHA
    y, _ = rellenar(c, y, lineas, gap=cfg.get('gap', GAP), key_sig=ton,
                    suelo=y_caja + 14)

    # 'preguntas_escucha', no 'escucha': las hojas antiguas ya traian una clave
    # 'escucha' con otra forma (la seccion de oido, que ocupaba media hoja) y
    # se colaba aqui.
    preguntas = cfg.get('preguntas_escucha') or [
        ('A', 'Toca dos notas seguidas. ¿La segunda SUBE o BAJA?', ['↑', '↓'], 6),
        ('B', 'Toca una tríada entera. ¿MAYOR o MENOR?', ['M', 'm'], 6),
        ('C', 'Toca una nota. ¿La has acertado al decirla?', ['sí', 'no'], 6),
    ]
    caja_escucha(c, y_caja, preguntas, cfg.get('sub_escucha'))
    y = y_caja - ALTO_ESCUCHA - 8
    pie(c, cfg)
    return y
