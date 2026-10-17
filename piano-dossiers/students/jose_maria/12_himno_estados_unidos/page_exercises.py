# -*- coding: utf-8 -*-
"""Taller de practica - Himno de Estados Unidos, The Star-Spangled
   Banner (Jose Maria, cancion 12, Do mayor, 3/4). Enfoque
   relajado: los saltos grandes, sin tensarse -- la melodia salta
   mas de una octava, pero la mano llega suelta, no de un golpe."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · ENERO · HIMNO DE ESTADOS UNIDOS'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El himno de Estados Unidos en Do mayor. Sin prisa: los saltos grandes llegan sueltos.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas, sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los saltos grandes, sin tensarse', 2,
                          'Lo que vamos a cuidar en esta pieza. La melodía salta más de una octava de golpe — la mano llega suelta, sin apretar ni tensarse por el camino.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'C5', 'B4', 'A4', 'G4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'a) El salto de octava, con la mano suelta', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo camino, paso a paso: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'C5', 'B4', 'A4', 'G4', 'C5']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El salto sobre el acorde de Do, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, sin prisa.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el salto llega suelto mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el salto sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha salta una octava y llega suelta, sin tensarse.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F5', 'E5', 'D5', 'C5', 'F5']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El salto sobre Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'C5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo camino, paso a paso: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del salto', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha salta con calma, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'G5', 'F5', 'E5', 'D5', 'G5']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El salto vuela; el acorde de Sol no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'D5', 'E5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: el mismo camino, un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · el himno casi entero', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que el salto llegue suelto, sobre un acorde que no se mueve.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'C5', 'B4', 'A4', 'G4', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F5', 'E5', 'D5', 'C5', 'F5']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El himno casi completo · con el salto llegando suelto', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
