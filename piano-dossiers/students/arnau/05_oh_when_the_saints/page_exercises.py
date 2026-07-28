# -*- coding: utf-8 -*-
"""Taller de practica - Oh, When the Saints (Arnau, cancion 5, Do
   mayor, 4/4). Nivel iniciacion: el compas que marcha, firme y
   decidido, como un desfile."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · OH WHEN THE SAINTS'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción alegre en Do mayor. Hoy marchamos con paso firme, ¡como en un desfile!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: acento en cada paso', 1,
                          'Marca bien el primer tiempo de cada compás, como el bombo de una banda.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3), ('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)]]
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Do, desgranado con acento', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El compás que marcha, firme y decidido', 2,
                          'Lo que vamos a practicar hoy. Cada nota cae con un paso firme y decidido, como en un desfile.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'G4', 'C5', 'E5', 'E5', 'C5', 'G4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) El paso firme, un peldaño más arriba', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'C5', 'B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, con más pasos: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'G4', 'C5', 'E5', 'E5', 'C5', 'G4', 'G4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La marcha sobre el acorde de Do, quieto', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: la marcha avanza mientras el acorde se queda quieto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la marcha sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha marcha con paso firme encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'A4', 'C5', 'F5', 'F5', 'C5', 'A4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La marcha sobre Fa, quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'C5', 'C5', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, con más pasos: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no marcha con la melodía', 3,
                          'La izquierda queda quieta con su acorde; la derecha marcha con firmeza, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'B4', 'D5', 'G5', 'G5', 'D5', 'B4', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La marcha vuela; el acorde de Sol no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'D5', 'D5', 'B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un acorde distinto', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Oh, When the Saints casi entera', 3,
                          'Con la partitura al lado: ¡marcha con paso firme, como en un desfile alegre!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['G4', 'G4', 'C5', 'E5', 'E5', 'C5', 'G4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['A4', 'A4', 'C5', 'F5', 'F5', 'C5', 'A4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · marchando con firmeza', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
