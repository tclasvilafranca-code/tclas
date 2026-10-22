# -*- coding: utf-8 -*-
"""Taller de practica - Bela Ciao (Merce, cancion 4, arr. Anderson
   Miranda Fernandes, Mi menor -- armadura de 1 sostenido (Fa#),
   confirmada con el Re# que aparece como sensible cerca del final,
   2/4). Nivel basico pero solido: la nota que despierta, el
   sensible de Mi menor."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · BELA CIAO'
TS = (2, 4)

MI = ['E3', 'G3', 'B3']
LA = ['A2', 'C3', 'E3']
SI = ['B2', 'D#3', 'F#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La versión de Bela Ciao de La Casa de Papel, en Mi menor. Hoy: la nota que despierta al final.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El Fa# es la única tecla negra de esta posición.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('F#4', 2), ('G4', 3), ('F#4', 2), ('E4', 1), ('F#4', 2), ('G4', 3), ('F#4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'G4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La nota que despierta: el sensible de Mi menor', 2,
                          'Lo que trabajamos hoy. Cerca del final aparece un Re sostenido: es el "sensible", la nota que tira con fuerza hacia el Mi, como si despertara la melodía.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'D#4', 'E4', 'D#4', 'E4', 'D4', 'D#4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) El Re natural y el Re sostenido, para sentir la diferencia', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'D#4', 'E4', 'F#4', 'D#4', 'E4', 'D#4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) El sensible tirando hacia el Mi, como en la canción', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D#4', 'E4']]
    bass2c = [{'pitches': SI, 'dur': 'q'}, {'pitches': MI, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El sensible resolviendo, con el acorde de Si mayor hacia Mi menor', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en Mi menor', 2,
                          'Mi menor–La menor–Si mayor: los tres acordes de esta tonalidad (el V lleva el sensible Re#).')
    y -= 11
    pattern_a = [(MI, 'Mim'), (LA, 'Lam'), (SI, 'Si'), (MI, 'Mim')]
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mim-Lam-Si-Mim, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: siente cómo el sensible tira hacia la nota de reposo, el Mi.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde de Mi menor', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta la melodía sincopada encima.')
    y -= 7
    treb1 = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['B4', 'G4', 'B4']])
    bass1 = [{'pitches': MI, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sincopada sobre Mi menor, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['B4', 'G4', 'B4']])
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el sensible no descoloca el acorde', 3,
                          'La izquierda sostiene el acorde de Si mayor, quieta; la derecha toca el sensible sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D#4', 'E4']]
    bass3 = [{'pitches': SI, 'dur': 'q'}, {'pitches': SI, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El sensible sobre Si mayor; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'D#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Bela Ciao casi entera', 3,
                          'Con la partitura al lado: siente cómo el sensible tira hacia el Mi, la nota de reposo.')
    y -= 7
    treb5 = (([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['B4', 'G4', 'B4']]) +
             [{'pitch': p, 'dur': 'q'} for p in ['D#4', 'E4']])
    bass5 = [{'pitches': MI, 'dur': 'h'}, {'pitches': SI, 'dur': 'q'}, {'pitches': MI, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Bela Ciao casi completa · con el sensible que despierta', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
