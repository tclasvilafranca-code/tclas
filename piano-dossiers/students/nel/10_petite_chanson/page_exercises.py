# -*- coding: utf-8 -*-
"""Taller de practica - Petite Chanson (Nel, cancion 10, Do mayor,
   4/4, a 4 manos). Angulo: MOVIMIENTO PERPETUO -- la segunda parte
   fluye en corcheas continuas de principio a fin, sin parar nunca,
   tal como el acompanamiento real de la pieza."""
from page_layout_common import *

SONG_KICKER = 'NEL · FEBRERO · PETITE CHANSON (RICCARDO COLLU, A 4 MANOS)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una pieza de Riccardo Collu en Do mayor, a 4 manos. El reto: corcheas fluidas que no paran nunca.')
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

    y = exercise_heading(c, y, 2, 'Movimiento perpetuo: corcheas que no paran nunca', 2,
                          'La dificultad exacta de esta pieza. La segunda parte fluye en corcheas continuas, sin ningún hueco ni respiro, de principio a fin.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C4', 'E4', 'G4', 'E4'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'a) El flujo continuo sobre Do, sin parar', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['F3', 'A3', 'C4', 'A3'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo flujo, ahora sobre Fa: ni una interrupción', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'E4', 'C5', 'G4']]
    bass2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C4', 'E4', 'G4', 'E4'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía larga sobre el flujo continuo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, la base del flujo continuo.')
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: el flujo continuo sostiene una melodía tranquila encima.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía flota sobre el flujo', 2,
                          'La izquierda fluye en corcheas sin ningún hueco; la derecha canta notas largas encima, tranquila.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'G4', 'C5', 'G4']]
    bass1 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C4', 'E4', 'G4', 'E4'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre el flujo continuo de Do', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'E4', 'C5', 'G4', 'A4', 'G4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando su forma', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el flujo no se detiene aunque la melodía se mueva', 3,
                          'La derecha se mueve más rápido; la izquierda sigue fluyendo en corcheas, sin ningún hueco, pase lo que pase arriba.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['G4', 'E4', 'F4', 'D4', 'E4', 'C5', 'G4', 'E4'] * 2)]
    bass3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['G3', 'B3', 'D4', 'B3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La derecha vuela; el flujo de abajo no se detiene', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'G4', 'E4', 'C4', 'D4', 'E4', 'F4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía, un poco más viva', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Petite Chanson casi entera', 3,
                          'Con la partitura al lado: no dejes que el flujo continuo se pare ni un instante, de principio a fin.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'G4', 'C5', 'G4', 'A4', 'G4', 'E4', 'D4']]
    bass5 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(
             ['C4', 'E4', 'G4', 'E4'] * 4 + ['F3', 'A3', 'C4', 'A3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · Andante ♩≈80, sin parar', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
