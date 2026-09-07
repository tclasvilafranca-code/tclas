# -*- coding: utf-8 -*-
"""Taller de practica - Christmas Songs for Four Little Hands
   (Luisa, cancion 4, Mindy Liang, Do mayor, 4/4, a 4 manos).
   Nivel hobby, sin complicaciones: tocar en pareja, sin agobios
   -- solo hay que disfrutar juntas."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · CHRISTMAS SONGS (A 4 MANOS)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un popurrí navideño a 4 manos, en Do mayor. Hoy: disfrutar de tocar en pareja, sin agobios.')
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

    y = exercise_heading(c, y, 2, 'Tocar en pareja, sin agobios', 2,
                          'Lo de hoy. Cuando toques con otra persona, no hace falta que salga perfecto: lo importante es disfrutar juntas y volver a encontraros si os despistáis.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'E4', 'E4', 'E4', 'E4', 'A4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Tu melodía, tranquila y repetida', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'C5', 'C5', 'B4', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Lo que viene después, sin prisa por juntarlo todo a la vez', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'E4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Tu melodía sobre el acorde de Do, tranquilo', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: disfruta, sin agobiarte si algo no sale perfecto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · tu melodía sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, tranquila; la derecha repite su nota, sin prisa.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'A4', 'A4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La nota repetida sobre Fa, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'A4', 'A4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · sin agobios, cada mano tranquila', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha entra en la nueva melodía sin prisa.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'C5', 'C5', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El inicio de "We Wish You" sobre Sol, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, más despacio', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · el popurrí casi entero', 3,
                          'Con la partitura al lado: sin agobios, disfruta de tocar en pareja hasta el final.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'E4', 'E4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'C5', 'C5', 'B4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El popurrí casi completo · disfrutando sin agobios', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
