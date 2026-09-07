# -*- coding: utf-8 -*-
"""Taller de practica - Peaches (Jose Maria, cancion 11, Do mayor,
   4/4). Enfoque relajado: las frases cortas, con una pequena
   respiracion entre cada una, sin lanzarse enseguida a la
   siguiente."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · ENERO · PEACHES (SUPER MARIO BROS MOVIE)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
Am = ['A2', 'C3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La canción de "Peaches" (Super Mario Bros Movie) en Do mayor. Sin prisa: frases cortas, con su respiro.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas, sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Las frases cortas: una respiración entre cada una', 2,
                          'Lo que vamos a cuidar en esta pieza. Cada frase es corta y luego hay un pequeño respiro antes de la siguiente — sin lanzarse enseguida.')
    y -= 9
    ev2a = [{'pitch': 'C4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
            {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}, {'pitch': 'F4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    y = system_block(c, x0, w0, y, gap, 'a) La frase corta, con su respiro detrás', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'E4', 'F4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, sin respiro: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': 'C4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}, {'pitch': 'F4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase corta sobre el acorde de Do, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Do–Lam–Fa–Sol: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(DO, 'Do'), (Am, 'Lam'), (FA, 'Fa'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Lam-Fa-Sol, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: cada frase corta respira mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase corta sobre el acorde de Lam', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta su frase corta y respira antes de la siguiente.')
    y -= 7
    treb1 = [{'pitch': 'A4', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'B4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'D5', 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    bass1 = [{'pitches': Am, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase corta sobre Lam, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'B4', 'C5', 'D5', 'E5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia de las frases', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha respira entre frases, sin que ninguna se apresure.')
    y -= 7
    treb3 = [{'pitch': 'F4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    bass3 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase corta sobre Fa; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'A4', 'B4', 'C5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sin respiro', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Peaches casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que cada frase corta respire antes de la siguiente.')
    y -= 7
    treb5 = ([{'pitch': 'C4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}, {'pitch': 'F4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}] +
             [{'pitch': 'A4', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'B4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'D5', 'dur': 'q'}, {'rest': True, 'dur': 'q'}])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, Am, Am]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con las frases cortas respirando', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
