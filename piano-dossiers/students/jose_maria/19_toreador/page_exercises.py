# -*- coding: utf-8 -*-
"""Taller de practica - Toreador, de Carmen (Jose Maria, cancion 19,
   Fa mayor, 4/4). Enfoque relajado: lo fuerte, sin apretar -- la
   energia del caracter marcial viene del gesto, no de tensar la
   mano."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · MAYO · TOREADOR (CARMEN, BIZET)'
TS = (4, 4)

FA = ['F2', 'A2', 'C3']
SIb = ['Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La marcha del Toreador, de "Carmen" (Bizet), en Fa mayor. Sin prisa: fuerte, sin apretar.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Lo fuerte, sin apretar', 2,
                          'Lo que vamos a cuidar en esta pieza. El carácter marcial pide energía y decisión, pero esa energía viene del gesto del brazo, no de apretar los dedos contra las teclas.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F4', 'A4', 'C5', 'C5', 'A4', 'F4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'a) El gesto marcial, con energía pero sin tensión', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'C5', 'Bb4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, más suave: para sentir la diferencia', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F4', 'A4', 'C5', 'C5', 'A4', 'F4', 'F4']]
    bass2c = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El gesto marcial sobre el acorde de Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad, sin prisa.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SIb, 'Sib'), (DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: la energía llega sin apretar, sobre el acorde quieto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el gesto marcial sobre el acorde de Sib', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha marca su gesto con energía, sin apretar.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'Bb4', 'D5', 'F5', 'F5', 'D5', 'Bb4', 'Bb4']]
    bass1 = [{'pitches': SIb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El gesto marcial sobre Sib, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'Eb5', 'F5', 'Eb5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia de la energía', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha marca su gesto, sin que ninguna se tense.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'C5', 'E5', 'G5', 'G5', 'E5', 'C5', 'C5']]
    bass3 = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El gesto vuela; el acorde de Do no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'F5', 'G5', 'F5', 'E5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un acorde distinto', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · el Toreador casi entero', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que la energía llegue sin apretar, sobre un acorde que no se mueve.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['F4', 'F4', 'A4', 'C5', 'C5', 'A4', 'F4', 'F4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'Bb4', 'D5', 'F5', 'F5', 'D5', 'Bb4', 'Bb4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [FA, FA, SIb, SIb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El Toreador casi completo · con energía, sin apretar', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
