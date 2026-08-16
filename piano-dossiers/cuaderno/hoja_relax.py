# -*- coding: utf-8 -*-
"""Ultima hoja del dosier: SOLTANDO DEDOS.

   Rediseno pedido por el cliente. Antes eran cuatro gestos sueltos con su
   explicacion al lado; ahora es la hoja entera de pentagramas, como el
   calentamiento, pero con el material pensado para lo contrario: alli se
   despierta la mano, aqui se suelta.

   El esquema de relajacion no es un adorno del texto, esta metido en las
   notas y es lo unico que hace que esta hoja no sea otro calentamiento:

     1. FIGURAS LARGAS. Redondas, blancas y negras, nada mas corto. En cuanto
        aparecen corcheas la mano se pone a correr y se agarrota.
     2. UN SILENCIO EN CASI TODOS LOS COMPASES. Ese hueco es el ejercicio:
        es donde se suelta la mano encima de las teclas.
     3. SALTOS MINIMOS (segundas y terceras). Un salto grande obliga a estirar
        la mano, y estirar es justo lo contrario de soltar.
     4. LA LINEA BAJA MAS QUE SUBE. Bajar es dejar caer el brazo; subir pide
        fuerza precisamente cuando se busca lo contrario.
     5. UNA MANO POR LINEA, ALTERNANDO. Mientras una toca, la otra se queda
        muerta encima del teclado, que es donde de verdad descansa.

   Y abajo, pequeno, el sitio donde la profesora escribe los deberes de ESA
   semana. Sin casillas de comprobacion: es una nota, no un examen.
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

GAP = 6.8
ALTO_DEBERES = 74          # lo que se reserva abajo para los deberes


def deberes(c, y, titulo='ESTA SEMANA, EN CASA', lineas=3, sub=None):
    """El recuadro de deberes, al pie. Pequeno a proposito: es para UNA
       semana, no un registro del curso. Sin casillas de hecho / no hecho."""
    h = ALTO_DEBERES
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)

    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + 14, y - 15, titulo)
    tw = stringWidth(titulo, 'DejaVuSans-Bold', 8.6)
    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 14 + tw + 10, y - 15, sub or 'lo escribe la profesora al final de la clase')

    yy = y - 30
    paso = (h - 34) / lineas
    for _ in range(lineas):
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.line(MARGIN + 14, yy, MARGIN + CONTENT_W - 14, yy)
        yy -= paso
    return y - h - 8


def build_relax(c, cfg):
    ton = cfg.get('key_sig')
    nombre_ton = ton if ton else 'Do mayor'
    intro = ('Lo último de la clase, con el brazo ya cansado. No es un ejercicio: es dejar de hacer '
             'fuerza. Todo son figuras largas y silencios, y en cada silencio hay que soltar la mano '
             'encima de las teclas hasta notarla pesada. Una línea cada mano, alternando: mientras una '
             'toca, la otra descansa. Está en %s, como la pieza.' % nombre_ton)
    reglas = cfg.get('reglas_relax') or ['EL BRAZO CAE, NO EMPUJA',
                                         'EN CADA SILENCIO, SUELTA LA MANO',
                                         'SI SUENA FUERTE, ES QUE APRIETAS']

    y = cabecera(c, cfg, 'Soltando dedos', 'Relajación · para terminar', intro, reglas)

    lineas = generar_hoja(nombre_ton, semilla=2000 + cfg.get('semilla', 1),
                          n_lineas=20, nivel=0, relax=True,
                          compases_extra=cfg.get('compases_relax') or [(4, 4), (4, 4), (3, 4)])
    y_caja = 48 + ALTO_DEBERES
    y, _ = rellenar(c, y, lineas, gap=cfg.get('gap', GAP), key_sig=ton,
                    suelo=y_caja + 12)

    deberes(c, y_caja, lineas=cfg.get('lineas_deberes', 3),
            sub=cfg.get('sub_deberes'))
    y = y_caja - ALTO_DEBERES
    pie(c, cfg)
    return y
