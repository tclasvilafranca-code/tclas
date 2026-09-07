# -*- coding: utf-8 -*-
"""Taller de practica - Despacito (Eva, cancion 11, La menor, 4/4). Mismo
   arreglo que el de Dilan (que trabaja el ostinato sincopado 3+3+2), pero
   enfoque DISTINTO para Eva: el CONTRASTE verso-estribillo -- dos energias
   muy distintas dentro de la misma cancion, intimo y grande."""
from page_layout_common import *

SONG_KICKER = 'EVA · MARZO · DESPACITO (LUIS FONSI & DADDY YANKEE)'
TS = (4, 4)

AM = ['A2', 'C3', 'E3']
DM = ['D2', 'F2', 'A2']
EM = ['E2', 'G#2', 'B2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un reggaetón en La menor. El reto: dos energías distintas, verso íntimo y estribillo grande.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Misma armadura que Do mayor, centro tonal en La.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('B4', 2), ('E5', 5), ('D5', 4), ('C5', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('E5', 5), ('C5', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Verso y estribillo: dos energías en la misma canción', 2,
                          'La dificultad exacta de esta canción. El verso es contenido y hablado; el estribillo se abre grande — el mismo dibujo, pero con una energía completamente distinta.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'B3', 'A3']]
    y = system_block(c, x0, w0, y, gap, 'a) El verso: contenido, casi hablado', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5', 'C5', 'D5', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) El estribillo: abierto y grande, mismo dibujo rítmico', ev2b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en La menor', 2,
                          'Lam–Rem–Mim: los acordes naturales de la tonalidad, aquí más movidos que en la canción real.')
    y -= 9
    pattern_a = [(AM, 'Lam'), (EM, 'Mim'), (DM, 'Rem'), (EM, 'Mim')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Mim-Rem-Mim, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'e', 'beam': i // 2, 'label': l} for i, (p, l) in enumerate(
        [(AM, 'Lam'), (AM, None), (DM, 'Rem'), (DM, None), (EM, 'Mim'), (EM, None), (AM, 'Lam'), (AM, None)] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, repetidos en corcheas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: siente el contraste completo, del verso íntimo al estribillo grande.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el verso contenido', 2,
                          'La izquierda sostiene el acorde con calma; la derecha canta el verso, íntimo, casi susurrado.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'B3', 'A3']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [AM, DM, EM, AM]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El verso, contenido en las dos manos', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['A4', 'C5', 'B4', 'D5'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) El estribillo se mueve más rápido y más abierto', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el estribillo con toda su energía', 3,
                          'Ahora las dos manos suenan grandes: el acorde marcado, la melodía abierta, sin perder precisión.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['C5', 'E5', 'D5', 'C5'] * 4)]
    bass3 = [{'pitches': p, 'dur': 'q'} for p in [AM, AM, DM, DM, EM, EM, AM, AM]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Forte total: verso terminado, estribillo a plena energía', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: las mismas notas, tranquilas', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Despacito casi entera', 3,
                          'Con la partitura al lado: siente cómo cambia la energía entre el verso y el estribillo, sin perder el pulso.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'B3', 'A3', 'A4', 'C5', 'E5', 'C5', 'D5', 'C5', 'B4', 'A4']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [AM, DM, EM, AM, AM, DM, EM, AM]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Reggaetón ♩≈89, con contraste', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
