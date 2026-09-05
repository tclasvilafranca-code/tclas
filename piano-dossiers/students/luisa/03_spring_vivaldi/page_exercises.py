# -*- coding: utf-8 -*-
"""Taller de practica - Spring, easy (Luisa, cancion 3, Vivaldi,
   Do mayor, 4/4). Nivel hobby, sin complicaciones: los saltos
   alegres -- subir y bajar sin miedo, disfrutando la melodia."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · SPRING (VIVALDI)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, "'Spring' de Vivaldi, en Do mayor, versión fácil. Hoy: saltos alegres, sin miedo.")
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los saltos alegres: subir y bajar sin miedo', 2,
                          'Lo de hoy. La melodía sube y baja con saltitos alegres: no hay que tener miedo, solo disfrutar el vaivén.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4', 'C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Sube alegre, sin miedo', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'E4', 'C4', 'E4', 'G4', 'E4', 'C4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Y baja igual de contenta', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El salto alegre sobre el acorde de Do, tranquilo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes, sin más complicación.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: el salto alegre encima del acorde tranquilo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el salto alegre sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, tranquila; la derecha salta contenta encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El salto sobre Fa, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el salto no descoloca el acorde', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha salta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El salto sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'B4', 'G4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Spring casi entera', 3,
                          'Con la partitura al lado: disfruta cada salto, subiendo y bajando sin miedo.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Spring casi completa · con los saltos alegres', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
