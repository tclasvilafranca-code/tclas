# -*- coding: utf-8 -*-
"""Taller de practica - Heart and Soul (Oriol, cancion 4, Hoagy
   Carmichael, Do mayor, 4/4, swing, mismo archivo que Luisa). Nivel
   medio, sin agobiar: la mano izquierda constante -- un compañero
   fiel que no cambia."""
from page_layout_common import *

SONG_KICKER = 'ORIOL · NIVEL MEDIO · HEART AND SOUL'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Heart and Soul, de Hoagy Carmichael, en Do mayor. Hoy: la mano izquierda constante.')
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

    y = exercise_heading(c, y, 2, 'La mano izquierda constante: un compañero fiel', 2,
                          'Lo de hoy. La izquierda repite el mismo acorde compás tras compás, siempre igual: es tu compañero fiel, mientras la derecha se mueve libremente encima con el swing.')
    y -= 9
    ev2a = [{'pitches': DO, 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Do, sostenido, sin cambiar', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': DO, 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo acorde otra vez: exactamente igual, sin variar', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El balanceo tranquilo sobre el acorde constante de Do', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: la izquierda se queda fiel mientras la derecha se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el balanceo sobre el acorde constante de Fa', 2,
                          'La izquierda sostiene el acorde de Fa sin moverse; la derecha se balancea encima con el swing.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El balanceo sobre Fa, constante', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Sol no se contagia del swing', 3,
                          'La izquierda sostiene su acorde de Sol sin moverse; la derecha se balancea sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El balanceo sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Heart and Soul casi entera', 3,
                          'Con la partitura al lado: la izquierda se mantiene fiel mientras la derecha disfruta del swing.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Heart and Soul casi completa · la mano izquierda constante y fiel', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
