# -*- coding: utf-8 -*-
"""Taller de practica - Largo, Sinfonia n.5 (Julia, cancion 22,
   Dvorak, Do mayor, 4/4). Nivel inicial con toque extra: la frase
   larga que no se corta -- una sola respiracion para varios
   compases."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · LARGO (DVORÁK)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El Largo de la Sinfonía del Nuevo Mundo, en Do mayor. Hoy: ¡una frase larga que no se corta!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). ¡Busca tu nota casa, el Do!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La frase larga que no se corta', 2,
                          'Lo que vamos a practicar hoy. La melodía respira en frases largas que cruzan de un compás a otro sin cortarse: como una sola respiración muy larga.')
    y -= 9
    ev2a = ([{'pitch': p, 'dur': 'q.'} for p in ['G4']] + [{'pitch': 'A4', 'dur': 'e'}] +
            [{'pitch': 'G4', 'dur': 'h'}] +
            [{'pitch': p, 'dur': 'q.'} for p in ['E4']] + [{'pitch': 'D4', 'dur': 'e'}] +
            [{'pitch': 'C4', 'dur': 'h'}])
    y = system_block(c, x0, w0, y, gap, 'a) Una frase larga, de un compás al siguiente sin parar', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'G4', 'G4', 'E4', 'D4', 'C4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, pero cortada nota a nota: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = ([{'pitch': p, 'dur': 'q.'} for p in ['G4']] + [{'pitch': 'A4', 'dur': 'e'}] +
              [{'pitch': 'G4', 'dur': 'h'}])
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase larga sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: el acorde sostenido acompaña la respiración larga de la melodía.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase larga sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha respira una frase larga encima.')
    y -= 7
    treb1 = ([{'pitch': p, 'dur': 'q.'} for p in ['A4']] + [{'pitch': 'Bb4', 'dur': 'e'}] +
             [{'pitch': 'A4', 'dur': 'h'}])
    bass1 = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase larga sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'Bb4', 'A4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, cortada nota a nota: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la frase larga no mueve el acorde', 3,
                          'La izquierda queda quieta con su acorde; la derecha respira su frase larga sin arrastrar a la de abajo.')
    y -= 7
    treb3 = ([{'pitch': p, 'dur': 'q.'} for p in ['B4']] + [{'pitch': 'C5', 'dur': 'e'}] +
             [{'pitch': 'B4', 'dur': 'h'}])
    bass3 = [{'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase larga sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'B4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, cortada nota a nota', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · el Largo casi entero', 3,
                          'Con la partitura al lado: ¡mantén la respiración larga sin cortar entre un compás y otro!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q.'} for p in ['G4']] + [{'pitch': 'A4', 'dur': 'e'}] +
             [{'pitch': 'G4', 'dur': 'h'}] +
             [{'pitch': p, 'dur': 'q.'} for p in ['E4']] + [{'pitch': 'D4', 'dur': 'e'}] +
             [{'pitch': 'C4', 'dur': 'h'}])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El Largo casi completo · con la frase larga que no se corta', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
