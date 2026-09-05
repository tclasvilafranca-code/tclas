# -*- coding: utf-8 -*-
"""Taller de practica - What Was I Made For? (Valentina, cancion 2, Do
   mayor, 4/4, mismo archivo que Dilan). Nivel medio, un poco mas
   exigente: acordes con septima -- un color mas denso bajo la
   melodia."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · WHAT WAS I MADE FOR?'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
DO7 = ['C3', 'E3', 'G3', 'B3']
FA7 = ['F2', 'A2', 'C3', 'E3']
SOL7 = ['G2', 'B2', 'D3', 'F3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Billie Eilish en Do mayor. Hoy: acordes con séptima, un color más denso.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Acordes con séptima: un color más denso bajo la melodía', 2,
                          'Lo de hoy. Añade la 4ª nota al acorde: Do se convierte en Domaj7, un color más rico y algo melancólico.')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(DO, 'Do'), (DO7, 'Domaj7')]]
    y = system_block(c, x0, w0, y, gap, 'a) Do y su séptima: escucha la diferencia', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(FA, 'Fa'), (FA7, 'Famaj7')]]
    y = system_block(c, x0, w0, y, gap, 'b) Fa y su séptima, el mismo color', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'C4']]
    bass2c = [{'pitches': DO7, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía flota sobre el Domaj7', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes, en su forma simple, sin más complicación.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: escucha el color denso de la séptima bajo cada frase.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el Famaj7', 2,
                          'La izquierda sostiene el Famaj7 entero; la derecha canta encima, dejando sonar el color.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'F4']]
    bass1 = [{'pitches': FA7, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase sobre Famaj7, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · el Sol7 no se contagia', 3,
                          'La izquierda sostiene su Sol7 sin moverse; la derecha canta sin arrastrar a la de abajo.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'G4']]
    bass3 = [{'pitches': SOL7, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase sobre Sol7; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · con el color de las séptimas', 3,
                          'Con la partitura al lado: deja sonar cada acorde entero, sin cortarlo antes de tiempo.')
    y -= 11
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'C4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'F4']])
    bass5 = [{'pitches': DO7, 'dur': 'w'}, {'pitches': FA7, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con acordes de séptima', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
