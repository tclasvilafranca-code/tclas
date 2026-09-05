# -*- coding: utf-8 -*-
"""Taller de practica - Christmas Songs for Four Little Hands
   (Merce, cancion 2, Mindy Liang, Do mayor, 4/4, a 4 manos:
   popurri de Jingle Bells + We Wish You a Merry Christmas).
   Nivel basico: el popurri -- dos canciones que se enlazan sin
   parar el pulso."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · CHRISTMAS SONGS (A 4 MANOS)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un popurrí navideño a 4 manos, en Do mayor: Jingle Bells enlaza con We Wish You a Merry Christmas.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Localiza el Do central como punto de referencia.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El popurrí: dos canciones que se enlazan sin parar', 2,
                          'Lo que trabajamos hoy. La pieza pasa de "Jingle Bells" a "We Wish You a Merry Christmas" sin ninguna pausa: el pulso debe seguir exactamente igual en el cambio.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'E4', 'E4', 'E4', 'E4', 'E4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) El final de "Jingle Bells"', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'C5', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) El inicio de "We Wish You a Merry Christmas", justo después', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'E4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El final de Jingle Bells sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: el pulso no debe titubear justo en el cambio de canción.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el final de Jingle Bells, sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha repite su nota, camino del cambio de canción.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'A4', 'A4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La nota repetida sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'A4', 'A4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el cambio de canción no descoloca el pulso', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha entra en la nueva canción exactamente a tiempo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'C5', 'C5', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El inicio de "We Wish You" sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, más despacio', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · el popurrí casi entero', 3,
                          'Con la partitura al lado: mantén el pulso firme justo en el cambio de una canción a la otra.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'E4', 'E4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'C5', 'C5', 'B4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El popurrí casi completo · con el cambio de canción sin pausas', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
