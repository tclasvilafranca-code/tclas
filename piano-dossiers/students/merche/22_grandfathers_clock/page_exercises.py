# -*- coding: utf-8 -*-
"""Taller de practica - My Grandfather's Clock (Merce, cancion 22,
   Henry Clay Work, arr. Gilbert DeBenedetti, Sol mayor, 4/4).
   Compartida con Jose Maria, pero con enfoque propio y distinto:
   el cambio de posicion -- mover la mano con suavidad cuando
   cambia el dedo guia. Nivel basico pero solido."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · MY GRANDFATHER\'S CLOCK'
TS = (4, 4)

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D2', 'F#2', 'A2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'My Grandfather\'s Clock, en Sol mayor. Hoy: cambiar de posición con suavidad, sin mirar el teclado.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5). El Fa# es la única alteración de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El cambio de posición: cuando cambia el dedo guía', 2,
                          'Lo que trabajamos hoy. A veces el dedo 1 aparece en una tecla nueva: la mano entera se mueve a una posición distinta, con suavidad y sin mirar.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('B4', 1), ('C5', 2), ('D5', 3), ('C5', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) La mano se desliza del Sol(1) al Si(1): un nuevo punto de apoyo', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D5', 1), ('E5', 2), ('F#5', 3), ('E5', 2), ('D5', 1), ('C5', 5), ('B4', 4), ('A4', 3)]]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora del Re(1) de vuelta a una posición más grave', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('G4', 1), ('A4', 2), ('B4', 1), ('C5', 2)]]
    bass2c = [{'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Dos cambios de posición seguidos, sobre el acorde de Sol, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Re-Sol, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: desliza la mano a la nueva posición sin perder el acompañamiento.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el cambio de posición sobre el acorde de Do', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha cambia de posición con suavidad.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 1), ('F#4', 2), ('G4', 1), ('A4', 2)]]
    bass1 = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El cambio de posición sobre Do, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F#4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el cambio de posición no descoloca el acorde', 3,
                          'La izquierda sostiene el acorde de Re, sin moverse; la derecha cambia de posición sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('F#4', 1), ('G4', 2), ('A4', 1), ('B4', 2)]]
    bass3 = [{'pitches': RE, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El cambio de posición sobre Re; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sin cambio de posición', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · My Grandfather\'s Clock casi entera', 3,
                          'Con la partitura al lado: desliza la mano a cada nueva posición con suavidad, sin mirar el teclado.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2)]] +
             [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('B4', 1), ('C5', 2), ('D5', 3), ('C5', 2)]])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [SOL, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'My Grandfather\'s Clock casi completa · con los cambios de posición', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
