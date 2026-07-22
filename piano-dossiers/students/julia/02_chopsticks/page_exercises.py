# -*- coding: utf-8 -*-
"""Taller de practica - Chopsticks (Julia, cancion 2, Do mayor,
   3/4). Nivel inicial: el juego de las dos manos que se turnan,
   como si jugaran a pasarse la pelota."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · CHOPSTICKS'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un juego de piano muy famoso, en Do mayor. Hoy las dos manos se turnan, ¡como pasarse la pelota!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). ¡Busca tu nota casa, el Do!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El juego de las dos manos que se turnan', 2,
                          'Lo que vamos a practicar hoy. Una mano toca, después la otra — como si se pasaran la pelota, sin chocar nunca.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) La derecha sola, con calma', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.'} for p in ['C3', 'D3', 'E3']]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora la izquierda, en el mismo sitio', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, cada una con su turno', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: se turnan mientras el acorde se queda quieto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el turno sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha juega su turno encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['F4', 'G4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El turno de la derecha sobre Fa, quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del turno', 3,
                          'La izquierda queda quieta con su acorde; la derecha juega, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'A4', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El turno de la derecha sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un poco más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Chopsticks casi entera', 3,
                          'Con la partitura al lado: ¡a jugar a pasarse la pelota entre las dos manos!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']] +
             [{'pitch': p, 'dur': 'h.'} for p in ['F4', 'G4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [DO, DO, DO, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · jugando con las dos manos', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
