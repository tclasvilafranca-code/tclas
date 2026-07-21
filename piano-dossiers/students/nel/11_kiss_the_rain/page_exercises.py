# -*- coding: utf-8 -*-
"""Taller de practica - Kiss the Rain (Nel, cancion 11, Do mayor,
   4/4). Enfoque: el arpegio que sube y baja por todo el teclado,
   sin perder el pulso constante de fondo -- el reto real de esta
   pieza de Yiruma."""
from page_layout_common import *

SONG_KICKER = 'NEL · JUNIO · KISS THE RAIN (YIRUMA)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
Am = ['A2', 'C3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una pieza instrumental de Yiruma en Do mayor. El reto: el arpegio que recorre el teclado sin perder el pulso.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, en arpegio de octava', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El arpegio que sube y baja, sin perder el pulso', 2,
                          'La dificultad exacta de esta canción. El arpegio recorre una octava entera de un vuelo, pero el pulso de fondo no puede tambalearse nunca.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C4', 'E4', 'G4', 'C5', 'G4', 'E4', 'C4', 'E4'])] + \
           [{'pitch': p, 'dur': 'h'} for p in ['G4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'a) El arpegio de octava entera, subiendo y bajando', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5', 'G4', 'E4', 'C4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, en negras: para sentir el pulso', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C4', 'E4', 'G4', 'C5', 'G4', 'E4', 'C4', 'E4'])] + \
             [{'pitch': p, 'dur': 'h'} for p in ['G4', 'C4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El arpegio sobre el acorde de Do, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Do–Sol–Lam–Fa: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(DO, 'Do'), (SOL, 'Sol'), (Am, 'Lam'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Sol-Lam-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el arpegio recorre el teclado mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el arpegio sobre el acorde quieto', 2,
                          'La izquierda sostiene el acorde entero, sin moverse; la derecha recorre su arpegio de octava, con el pulso siempre firme.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['G4', 'B4', 'D5', 'G5', 'D5', 'B4', 'G4', 'B4'])] + \
            [{'pitch': p, 'dur': 'h'} for p in ['D5', 'G4']]
    bass1 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El arpegio sobre Sol, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G5', 'D5', 'B4', 'G4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo el pulso, sin el arpegio: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del arpegio', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha vuela por el arpegio, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'C5', 'E5', 'A5', 'E5', 'C5', 'A4', 'C5'])] + \
            [{'pitch': p, 'dur': 'h'} for p in ['E5', 'A4']]
    bass3 = [{'pitches': Am, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El arpegio vuela; el acorde de Lam no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5', 'A5', 'E5', 'C5', 'A4', 'E5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: el mismo arpegio, un acorde distinto', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Kiss the Rain casi entera', 3,
                          'Con la partitura al lado: deja que el arpegio recorra el teclado entero sin que el pulso tiemble.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C4', 'E4', 'G4', 'C5', 'G4', 'E4', 'C4', 'E4'])] +
             [{'pitch': p, 'dur': 'h'} for p in ['G4', 'C4']] +
             [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['G4', 'B4', 'D5', 'G5', 'D5', 'B4', 'G4', 'B4'])] +
             [{'pitch': p, 'dur': 'h'} for p in ['D5', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, SOL, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con el arpegio recorriendo el teclado', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
