# -*- coding: utf-8 -*-
"""Taller de practica - Despacito (Nel, cancion 19, Do mayor, 4/4).
   Mismo arreglo que el de Dilan (ostinato sincopado 3+3+2) y el de
   Eva (contraste verso-estribillo), pero enfoque DISTINTO para
   Nel: el ORNAMENTO -- un pasaje rapido de corcheas que decora la
   melodia sobre acordes largos y sostenidos, tal como la partitura
   real (que usa semicorcheas; aqui se trabaja el mismo gesto con
   corcheas, la subdivision mas rapida del motor)."""
from page_layout_common import *

SONG_KICKER = 'NEL · MAYO · DESPACITO (LUIS FONSI & DADDY YANKEE)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
Am = ['A2', 'C3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Luis Fonsi y Daddy Yankee en Do mayor. El reto: adornos rápidos sobre acordes sostenidos.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('D4', 2), ('F4', 4), ('E4', 3), ('G4', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El ornamento: corcheas rápidas sobre el acorde sostenido', 2,
                          'La dificultad exacta de esta canción. Un pasaje corto de corcheas rápidas decora la melodía mientras el acorde de abajo se mantiene quieto, sin moverse.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C4', 'D4', 'E4', 'D4'] * 2)] + \
           [{'pitch': p, 'dur': 'h'} for p in ['E4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'a) El adorno rápido, resolviendo en notas largas', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4', 'C4', 'E4', 'G4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, en negras tranquilas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C4', 'D4', 'E4', 'D4'] * 2)] + \
             [{'pitch': p, 'dur': 'h'} for p in ['E4', 'C4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El adorno sobre el acorde de Do, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Do–Fa–Sol–Lam: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (Am, 'Lam')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Lam, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el ornamento decora la melodía mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el ornamento sobre el acorde quieto', 2,
                          'La izquierda sostiene el acorde entero, sin moverse; la derecha decora la melodía con su pasaje rápido de corcheas.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'F4', 'G4', 'F4'] * 2)] + \
            [{'pitch': p, 'dur': 'h'} for p in ['G4', 'E4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El adorno sobre Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F4', 'E4', 'D4', 'C4', 'D4', 'E4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin el adorno: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del adorno', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha vuela con su pasaje rápido, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['G4', 'A4', 'B4', 'A4'] * 2)] + \
            [{'pitch': p, 'dur': 'h'} for p in ['B4', 'G4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El adorno vuela; el acorde de Sol no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'B4', 'A4', 'G4', 'F4', 'G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Despacito casi entera', 3,
                          'Con la partitura al lado: deja que el adorno rápido resbale sin prisa, siempre sobre un acorde que no se mueve.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C4', 'D4', 'E4', 'D4'] * 2)] +
             [{'pitch': p, 'dur': 'h'} for p in ['E4', 'C4']] +
             [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'F4', 'G4', 'F4'] * 2)] +
             [{'pitch': p, 'dur': 'h'} for p in ['G4', 'E4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈76, con el ornamento decorando', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
