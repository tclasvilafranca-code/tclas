# -*- coding: utf-8 -*-
"""Taller de practica - Jingle Bells (Jose Maria, cancion 8, Sol
   mayor, 4/4). Tono relajado: repetir la misma nota varias veces sin
   que la mano se canse ni se tense -- cada repeticion, igual de
   comoda que la anterior."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · DICIEMBRE · JINGLE BELLS'
TS = (4, 4)

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D3', 'F#3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico muy conocido en Sol mayor. Aquí cuidamos repetir la misma nota sin cansarnos.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5). Todo teclas blancas, sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('B4', 3), ('A4', 2), ('C5', 4), ('B4', 3), ('D5', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('B4', 3), ('D5', 5), ('B4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La misma nota, varias veces, sin cansarse', 2,
                          'Lo que vamos a cuidar en esta canción. Tocar la misma nota tres veces seguidas puede tensar la mano — deja que cada repetición sea igual de cómoda que la primera.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'B4', 'B4', 'B4', 'B4', 'B4', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) La misma nota, relajada cada vez', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h'} for p in [SOL, DO]]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: acordes tranquilos que acompañan', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'B4', 'B4', 'B4', 'B4', 'B4', 'B4', 'A4']]
    bass2c = [{'pitches': p, 'dur': 'h'} for p in [SOL, DO, SOL, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, cada una a su aire', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad, sin prisa.')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (DO, 'Do')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Re-Do, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: la nota repetida siempre relajada, con el acorde debajo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la nota repetida, siempre relajada', 2,
                          'La izquierda sostiene el acorde tranquilo; la derecha repite su nota sin tensarse, dejando caer el dedo con suavidad cada vez.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'G4', 'G4', 'G4', 'A4', 'A4', 'A4', 'A4']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [SOL, DO, SOL, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La nota repetida sobre el acorde tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'D5', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para irla conociendo', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la mano no se contagia de la repetición', 3,
                          'La izquierda queda quieta con su acorde; la derecha repite su nota relajada, sin que la tensión suba por el brazo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'D5', 'D5', 'C5', 'C5', 'C5', 'B4']]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [RE, SOL, RE, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda firme; la derecha repite libre', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la escala tranquila, sin repeticiones', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Jingle Bells casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que cada nota repetida caiga igual de suave que la anterior.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['B4', 'B4', 'B4', 'B4', 'B4', 'B4', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5', 'D5', 'D5', 'D5', 'C5']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [SOL, DO, SOL, DO, RE, SOL, RE, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · alegre, sin tensión', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
