# -*- coding: utf-8 -*-
"""Taller de practica - A comme Amour (Nel, cancion 12, Mi menor,
   4/4). Enfoque: la carrera que aterriza justo en el tiempo -- un
   arpegio rapido en corcheas que tiene que caer exactamente sobre
   el pulso, no antes ni despues (distinto del enfoque de relajacion
   de Jose Maria para la misma pieza)."""
from page_layout_common import *

SONG_KICKER = 'NEL · MARZO · A COMME AMOUR (RICHARD CLAYDERMAN)'
TS = (4, 4)

Em = ['E2', 'G2', 'B2']
Am = ['A2', 'C3', 'E3']
B = ['B2', 'D#3', 'F#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una pieza de Richard Clayderman en Mi menor. El reto: la carrera aterriza justo en el tiempo.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('G4', 3), ('F#4', 2), ('A4', 4), ('G4', 3), ('B4', 5), ('A4', 4), ('G4', 3)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'B4', 'G4', 'B4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La carrera que aterriza justo en el tiempo', 2,
                          'La dificultad exacta de esta canción. Un arpegio corto y rápido tiene que caer exactamente sobre el pulso — ni un pelo antes, ni un pelo después.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'G4', 'B4', 'G4'] * 2)] + \
           [{'pitch': p, 'dur': 'h'} for p in ['E4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'a) El arpegio, aterrizando sobre el pulso', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'E5', 'B4', 'G4', 'E4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo arpegio, en negras: para sentir el pulso', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'G4', 'B4', 'G4'] * 2)] + \
             [{'pitch': p, 'dur': 'h'} for p in ['E4', 'B4']]
    bass2c = [{'pitches': Em, 'dur': 'h.'}, {'pitches': Em, 'dur': 'q'}, {'pitches': Em, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La carrera sobre el acorde de Mim, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–V–iv en Mi menor', 2,
                          'Mim–Si–Lam–Mim: los acordes reales de esta pieza.')
    y -= 11
    pattern_a = [(Em, 'Mim'), (B, 'Si'), (Am, 'Lam'), (Em, 'Mim')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mim-Si-Lam-Mim, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la carrera aterriza sobre el pulso mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la carrera sobre el acorde de Lam', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha corre su arpegio, aterrizando siempre justo sobre el pulso.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'C5', 'E5', 'C5'] * 2)] + \
            [{'pitch': p, 'dur': 'h'} for p in ['A4', 'E5']]
    bass1 = [{'pitches': Am, 'dur': 'h.'}, {'pitches': Am, 'dur': 'q'}, {'pitches': Am, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La carrera sobre Lam, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5', 'A5', 'E5', 'C5', 'A4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo el pulso, sin la carrera: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia de la carrera', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha corre su arpegio, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['B4', 'D#5', 'F#5', 'D#5'] * 2)] + \
            [{'pitch': p, 'dur': 'h'} for p in ['B4', 'F#5']]
    bass3 = [{'pitches': B, 'dur': 'h.'}, {'pitches': B, 'dur': 'q'}, {'pitches': B, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La carrera vuela; el acorde de Si no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'D#5', 'F#5', 'B5', 'F#5', 'D#5', 'B4', 'D#5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma carrera, un acorde distinto', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · A comme Amour casi entera', 3,
                          'Con la partitura al lado: deja que la carrera aterrice siempre justo en el tiempo, sobre un acorde que no se mueve.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'G4', 'B4', 'G4'] * 2)] +
             [{'pitch': p, 'dur': 'h'} for p in ['E4', 'B4']] +
             [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'C5', 'E5', 'C5'] * 2)] +
             [{'pitch': p, 'dur': 'h'} for p in ['A4', 'E5']])
    bass5 = ([{'pitches': Em, 'dur': 'h.'}, {'pitches': Em, 'dur': 'q'}, {'pitches': Em, 'dur': 'w'}] +
             [{'pitches': Am, 'dur': 'h.'}, {'pitches': Am, 'dur': 'q'}, {'pitches': Am, 'dur': 'w'}])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · ♩≈69, con la carrera aterrizando en el pulso', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
