# -*- coding: utf-8 -*-
"""Taller de practica - I Have a Dream (Merce, cancion 6, Abba,
   Do mayor, 4/4). Mismo arreglo compartido con Julia, pero con
   enfoque propio y distinto: el ritmo con puntillo -- negra con
   puntillo y corchea, la proporcion larga-corta exacta. Nivel
   basico pero solido, tono adulto."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · I HAVE A DREAM'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'I Have a Dream, de Abba, en Do mayor. Hoy: la proporción exacta del ritmo con puntillo.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Localiza el Do central como punto de referencia.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El ritmo con puntillo: largo-corto exacto', 2,
                          'Lo que trabajamos hoy. La negra con puntillo dura tres corcheas y la corchea que la sigue solo una: hay que sentir esa proporción 3 a 1, sin igualarlas.')
    y -= 9
    ev2a = [{'pitch': 'C4', 'dur': 'q.'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'h'},
            {'pitch': 'D4', 'dur': 'q.'}, {'pitch': 'C4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'a) Negra con puntillo y corchea, dos veces seguidas', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'C4', 'D4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma melodía, en negras iguales: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': 'C4', 'dur': 'q.'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'h'}]
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El ritmo con puntillo sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el acorde sostenido no debe alterar la proporción larga-corta de la melodía.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el ritmo con puntillo sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha mantiene la proporción larga-corta exacta.')
    y -= 7
    treb1 = [{'pitch': 'F4', 'dur': 'q.'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'h'}]
    bass1 = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El ritmo con puntillo sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, en negras iguales: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el puntillo no descoloca el acorde', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha marca el puntillo sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': 'G4', 'dur': 'q.'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'B4', 'dur': 'h'}]
    bass3 = [{'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El ritmo con puntillo sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, en negras iguales', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · I Have a Dream casi entera', 3,
                          'Con la partitura al lado: mantén la proporción exacta 3 a 1 entre la nota larga y la corta.')
    y -= 7
    treb5 = ([{'pitch': 'C4', 'dur': 'q.'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'h'}] +
             [{'pitch': 'D4', 'dur': 'q.'}, {'pitch': 'C4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'h'}])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'I Have a Dream casi completa · con el ritmo con puntillo exacto', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
