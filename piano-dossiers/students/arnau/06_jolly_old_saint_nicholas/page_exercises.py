# -*- coding: utf-8 -*-
"""Taller de practica - Jolly Old Saint Nicholas (Arnau, cancion 6,
   Do mayor, 4/4). Nivel iniciacion: el paso a paso, la escalera de
   notas sin saltarse ningun escalon."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · JOLLY OLD SAINT NICHOLAS'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico en Do mayor. Hoy: subir y bajar la escalera de notas sin saltarse ningún escalón.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: dedos que caminan', 1,
                          'Un dedo por tecla, muy despacio, subiendo la posición entera.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) La escalera completa, subiendo y bajando', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El paso a paso: la escalera de notas', 2,
                          'Sube y baja escalón a escalón, sin saltarse ninguno — como subir una escalera con cuidado.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'B4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'a) La escalera, un peldaño más arriba', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5', 'G4', 'E4', 'C4', 'E4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora con saltos: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'B4', 'A4', 'G4', 'F4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La escalera sobre el acorde de Do, quieto', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: la escalera sube y baja mientras el acorde se queda quieto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la escalera sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha sube y baja su escalera.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'Bb4', 'C5', 'D5', 'E5', 'D5', 'C5', 'Bb4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La escalera sobre Fa, quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'F5', 'C5', 'A4', 'F4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora con saltos: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no sube la escalera', 3,
                          'La izquierda queda quieta con su acorde; la derecha sube y baja, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5', 'E5', 'F5', 'E5', 'D5', 'C5']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La escalera sube; el acorde de Sol no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G5', 'D5', 'B4', 'G4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, con saltos', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Jolly Old Saint Nicholas casi entera', 3,
                          'Con la partitura al lado: ¡sube y baja la escalera con cuidado, escalón a escalón!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'B4', 'A4', 'G4', 'F4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['A4', 'Bb4', 'C5', 'D5', 'E5', 'D5', 'C5', 'Bb4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · subiendo y bajando la escalera', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
