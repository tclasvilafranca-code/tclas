# -*- coding: utf-8 -*-
"""Taller de practica - Have Yourself a Merry Little Christmas
   (Valentina, cancion 5, Do mayor, 4/4, mismo archivo que Dilan).
   Nivel medio, un poco mas exigente: las voces internas -- escuchar
   mas de una linea a la vez, dentro de una sola mano."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · HAVE YOURSELF A MERRY LITTLE CHRISTMAS'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico clásico en Do mayor. Hoy: dos voces dentro de una sola mano.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Campanas: nota repetida, cambiando de dedo', 1,
                          'Como un carillón de Navidad: la misma nota suena varias veces, cambiando el dedo cada vez (1-3-1-3).')
    y -= 12
    ev1a = [{'pitch': 'G4', 'dur': 'q', 'number': n} for n in [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]]
    y = system_block(c, x0, w0, y, gap, 'a) Campanita fija: Sol, alternando dedos 1 y 3', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('G4', 3), ('C4', 1), ('G4', 3)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) Carillón a dos voces: Do y Sol, cada vez más seguro', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Las voces internas: escuchar más de una línea a la vez', 2,
                          'Lo de hoy. En una sola mano viven dos voces: una se queda quieta arriba, la otra se mueve por debajo. Escucha las dos por separado.')
    y -= 12
    ev2a = [{'pitch': 'G4', 'dur': 'q'}] * 8
    y = system_block(c, x0, w0, y, gap, 'a) Primero, la voz de arriba: quieta, sostenida', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora, la voz de abajo: la que se mueve', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitches': p, 'dur': 'q'} for p in
            [['C4', 'G4'], ['D4', 'G4'], ['E4', 'G4'], ['D4', 'G4']] * 2]
    y = system_block(c, x0, w0, y, gap, 'c) Las dos voces juntas: una quieta, otra viva', ev2c, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los acordes que sostienen el villancico en la izquierda.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (FA, 'Fa')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora tres manos a la vez: las dos voces de la derecha, y el acorde de la izquierda.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · las dos voces sobre el acorde', 2,
                          'La izquierda sostiene su acorde; la derecha reparte sus dos voces, una quieta y otra viva.')
    y -= 11
    treb1 = [{'pitches': p, 'dur': 'q'} for p in [['C4', 'G4'], ['D4', 'G4'], ['E4', 'G4'], ['D4', 'G4']] * 2]
    bass1 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (SOL, 'Sol'), (DO, 'Do'), (SOL, 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Las dos voces sobre el acompañamiento', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · tres líneas que no se mezclan', 3,
                          'La voz de arriba no se mueve, la de abajo camina, y la izquierda marca su propio paso: tres líneas distintas.')
    y -= 11
    treb3 = [{'pitches': p, 'dur': 'q'} for p in [['E4', 'C5'], ['D4', 'C5'], ['C4', 'C5'], ['D4', 'C5']] * 2]
    bass3 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FA, 'Fa'), (SOL, 'Sol'), (FA, 'Fa'), (SOL, 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La voz de arriba, quieta; la de abajo, viva', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · el villancico a dos voces, casi entero', 3,
                          'Con la partitura al lado: deja que las dos voces canten sin mezclarse.')
    y -= 11
    treb6 = [{'pitches': p, 'dur': 'q'} for p in
             ([['C4', 'G4'], ['D4', 'G4'], ['E4', 'G4'], ['D4', 'G4']] +
              [['E4', 'C5'], ['D4', 'C5'], ['C4', 'C5'], ['D4', 'C5']])]
    bass6 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'El villancico casi completo · ♩≈66, dos voces con dulzura', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
