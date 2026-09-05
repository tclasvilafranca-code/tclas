# -*- coding: utf-8 -*-
"""PREVIEW del nuevo formato de dosier (v2): en vez de un dosier de 5
   paginas con 6 bloques identicos por cancion, ahora son 3 paginas:
      1. Partitura fuente (la real, sin tocar)
      2. Ficha de clase: EL problema real de esta cancion (uno, no seis),
         identificado leyendo la partitura, con un pentagrama doble (sol+fa)
         repartido en varias lineas -- como una pagina de partitura de
         verdad, con notas suficientes para que se sienta como musica y
         no como fichas sueltas -- y un hueco en blanco para que la
         profesora anote lo que vea en la clase real.
      3. Tarjeta de practica en casa: pasos concretos, solo sobre ese
         mismo problema, con casillas para marcar los dias de la semana.
   Ejemplo: Chopsticks (Do mayor, 3/4). El problema real de esta pieza es
   el turno de las dos manos, que se pasan la melodia sin chocar -- asi
   que TODO el material de hoy gira en torno a eso, nada mas."""
from reportlab.lib.colors import HexColor, white
from notation import *
from page_layout_common import (W, H, MARGIN, CONTENT_W, wrap_text_common,
                                 multi_grand_staff_block, grand_staff_block)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
DO_TREB = ['C4', 'E4', 'G4']
FA_TREB = ['F4', 'A4', 'C5']
SOL_TREB = ['G4', 'B4', 'D5']

KICKER = 'ARNAU · CANCIÓN 1 · CHOPSTICKS'
TS = (3, 4)


def _header(c, subtitle_right, titulo):
    c.setFillColor(DARKGREEN)
    c.rect(0, H - 5, W, 5, fill=1, stroke=0)
    y = H - 32
    c.setFont('DejaVuSans-Bold', 8.8)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN, y, KICKER)
    c.setFont('DejaVuSans', 8.8)
    c.setFillColor(GRAY)
    c.drawRightString(W - MARGIN, y, subtitle_right)
    y -= 22
    c.setFont('DejaVuSerif-Bold', 19)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, titulo)
    return y - 20


def _footer(c, page_num):
    c.setFont('DejaVuSans', 7.6)
    c.setFillColor(HexColor('#8A8A8A'))
    c.drawCentredString(W / 2, 22, 'El Cuaderno del Pianista · T-Clas')
    c.drawRightString(W - MARGIN, 22, str(page_num))


def _problema_box(c, y, problema, explicacion):
    """La caja central: EL problema real de esta cancion, uno solo,
       tal y como se lee en la partitura -- no una lista de bloques."""
    height = 52
    c.setFillColor(HexColor('#EFF3ED'))
    c.roundRect(MARGIN, y - height, CONTENT_W, height, 6, fill=1, stroke=0)
    c.setFillColor(DARKGREEN)
    c.rect(MARGIN, y - height, 4, height, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN + 14, y - 15, 'EL PROBLEMA REAL DE ESTA PARTITURA')
    c.setFont('DejaVuSerif-Bold', 13.5)
    c.setFillColor(INK)
    c.drawString(MARGIN + 14, y - 32, problema)
    wrap_text_common(c, explicacion, MARGIN + 14, y - 44, 'DejaVuSans', 8.3, CONTENT_W - 28, 11.2, color=GRAY)
    return y - height - 14


def page_fuente_partitura_placeholder():
    """La pagina 1 real es la partitura fuente (PDF externo, con copyright);
       no se genera aqui. Ver build_preview.py."""
    pass


def page_clase(c):
    y = _header(c, 'Ficha de clase', 'Ficha de clase')
    c.setFont('DejaVuSans', 9.1)
    c.setFillColor(GRAY)
    y = wrap_text_common(c, 'El juego de piano más famoso del mundo, en Do mayor. Vale para trabajar HOY una sola cosa de verdad.',
                          MARGIN, y, 'DejaVuSans', 9.1, CONTENT_W, 12.4, color=GRAY)
    y -= 6

    y = _problema_box(c, y,
                       'El turno de las dos manos, sin chocar',
                       'En toda la pieza, una mano toca su frase y la otra espera quieta — y luego al revés. '
                       'Eso es lo único que trabajamos hoy: que cada mano espere su turno con calma.')
    y -= 4

    gap = 6.6
    x0, w0 = MARGIN, CONTENT_W

    # Pieza de estudio completa, a piano real (sol+fa), en 3 lineas de 4
    # compases -- primero canta la derecha (la izquierda espera con su
    # acorde), luego se cambian los papeles (la izquierda canta y la
    # derecha espera), y al final las dos manos van juntas.
    treb = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4', 'D4', 'E4', 'F4']] +
            [{'pitches': p, 'dur': 'h.'} for p in [DO_TREB, FA_TREB, SOL_TREB, DO_TREB]] +
            [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F4', 'E4', 'D4', 'C4', 'D4', 'E4', 'F4', 'G4', 'E4', 'D4', 'C4']])
    bass = ([{'pitches': p, 'dur': 'h.'} for p in [DO, FA, SOL, DO]] +
            [{'pitch': p, 'dur': 'q'} for p in ['C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3', 'C3', 'D3', 'E3', 'F3']] +
            [{'pitch': p, 'dur': 'q'} for p in ['C3', 'C3', 'C3', 'F2', 'F2', 'F2', 'G2', 'G2', 'G2', 'C3', 'C3', 'C3']])
    y = multi_grand_staff_block(c, x0, w0, y, gap, treb, bass,
                                 'Estudio: primero canta la derecha, luego la izquierda, al final las dos juntas',
                                 time_sig=TS, bars_per_line=4, grand_gap_mult=6.2, line_gap_mult=1.7)
    y -= 8

    # El momento exacto del "turno", aislado (categoria E: aislar el patron).
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'El momento del turno, aislado y muy despacio:')
    y -= 12
    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4']] + [{'rest': True, 'dur': 'h.'}]
    bass2 = [{'rest': True, 'dur': 'h.'}] + [{'pitch': p, 'dur': 'q'} for p in ['C3', 'D3', 'E3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2, bass2, 'a) La derecha toca y calla; la izquierda responde',
                           grand_gap_mult=6.2, time_sig=TS)
    y -= 10

    # Hueco para la profesora.
    box_h = 74
    c.setStrokeColor(LIGHTLINE)
    c.setLineWidth(0.8)
    c.roundRect(MARGIN, y - box_h, CONTENT_W, box_h, 5, fill=0, stroke=1)
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(DARKGREEN)
    c.drawString(MARGIN + 10, y - 14, 'NOTAS DE LA PROFESORA DESPUÉS DE ESTA CLASE')
    c.setStrokeColor(HexColor('#D9D9D9'))
    c.setLineWidth(0.6)
    for i in range(3):
        ly = y - 30 - i * 16
        c.line(MARGIN + 10, ly, MARGIN + CONTENT_W - 10, ly)

    _footer(c, 2)
    c.showPage()


def page_tarjeta_casa(c):
    y = _header(c, 'Tarjeta de práctica en casa', 'Práctica en casa')
    c.setFont('DejaVuSans', 9.1)
    c.setFillColor(GRAY)
    y = wrap_text_common(c, 'Esta semana practicamos solo UNA cosa: el turno de las dos manos, sin chocar.',
                          MARGIN, y, 'DejaVuSans', 9.1, CONTENT_W, 12.4, color=GRAY)
    y -= 10

    steps = [
        'Manos separadas, muy despacio: toca solo la línea 1 (la derecha) del estudio de la ficha de clase.',
        'Ahora solo la izquierda: toca la línea 2, donde ella tiene la melodía.',
        'Junta las manos solo en la línea 3, el final, donde las dos tocáis juntas.',
        'Con la partitura de Chopsticks delante: toca la canción entera una vez, sin parar aunque falles.',
    ]
    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Los 4 pasos de esta semana')
    y -= 20
    for i, step in enumerate(steps, 1):
        c.setFillColor(DARKGREEN)
        c.roundRect(MARGIN, y - 16, 18, 18, 3, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 9.5)
        c.setFillColor(white)
        c.drawCentredString(MARGIN + 9, y - 11.5, str(i))
        c.setFont('DejaVuSans', 9.3)
        c.setFillColor(INK)
        y = wrap_text_common(c, step, MARGIN + 26, y - 11.5, 'DejaVuSans', 9.3, CONTENT_W - 26, 12.6, color=INK)
        y -= 10

    y -= 8
    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, '¿Qué días has practicado esta semana?')
    y -= 22
    dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
    box = 30
    total_w = 7 * box + 6 * 8
    x = MARGIN
    for d in dias:
        c.setStrokeColor(LIGHTLINE)
        c.setLineWidth(0.9)
        c.roundRect(x, y - box, box, box, 5, fill=0, stroke=1)
        c.setFont('DejaVuSans-Bold', 9.5)
        c.setFillColor(GRAY)
        c.drawCentredString(x + box / 2, y - box / 2 - 3.5, d)
        x += box + 8
    y -= box + 20

    c.setFillColor(HexColor('#F4EFE3'))
    c.roundRect(MARGIN, y - 34, CONTENT_W, 34, 5, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(MARGIN, y - 34, 3, 34, fill=1, stroke=0)
    wrap_text_common(c, 'Truco: practica siempre con las dos manos separadas primero. Solo júntalas cuando cada una vaya sola sin dudar.',
                      MARGIN + 12, y - 14, 'DejaVuSans', 8.4, CONTENT_W - 24, 11.4, color=HexColor('#5A4A20'))

    _footer(c, 3)
    c.showPage()
