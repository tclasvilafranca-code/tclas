# -*- coding: utf-8 -*-
"""Taller de practica - Deck the Halls (Jose Maria, cancion 7, Fa
   mayor, 4/4). Tono relajado: saltos pequenos y alegres, sin tension
   en la muneca -- la mano se mueve lo justo, nunca se fuerza."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · DICIEMBRE · DECK THE HALLS'
TS = (4, 4)

FA = ['F2', 'A2', 'C3']
BB = ['Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico alegre en Fa mayor. Aquí cuidamos que la muñeca se quede suelta en cada salto.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca la tecla negra Sib, sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('G4', 2), ('Bb4', 4), ('A4', 3), ('C5', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('C5', 5), ('A4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Saltos pequeños, muñeca suelta', 2,
                          'Lo que vamos a cuidar en esta canción. Cada salto es corto — deja que la muñeca acompañe el movimiento sin ponerse rígida.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'F4', 'A4', 'G4', 'Bb4', 'G4', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'a) Saltitos cortos, con la muñeca relajada', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h'} for p in [FA, BB]]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: acordes tranquilos, sin prisa', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'F4', 'A4', 'G4', 'Bb4', 'G4', 'Bb4']]
    bass2c = [{'pitches': p, 'dur': 'h'} for p in [FA, BB, FA, BB]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, cada una a su aire', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad, sin prisa.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (BB, 'Sib'), (DO, 'Do'), (BB, 'Sib')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Sib, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: saltos pequeños y una muñeca siempre suelta.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · saltos alegres, muñeca suelta', 2,
                          'La izquierda sostiene el acorde tranquilo; la derecha da sus saltitos cortos, sin tensar nunca la muñeca.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'A4', 'C5', 'Bb4', 'D5', 'Bb4', 'D5']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [FA, BB, FA, BB]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Los saltos sobre el acorde tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4', 'F4', 'G4', 'A4', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para irla conociendo', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la muñeca no se contagia', 3,
                          'La izquierda queda quieta con su acorde; la derecha salta relajada, sin que la tensión suba por el brazo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'F4', 'C5', 'F4', 'Bb4', 'F4', 'Bb4', 'D5']]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [DO, BB, DO, BB]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda firme; la derecha salta libre', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'C5', 'Bb4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la escala tranquila, sin saltos', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Deck the Halls casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que la muñeca acompañe cada salto, relajada.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['F4', 'A4', 'F4', 'A4', 'G4', 'Bb4', 'G4', 'Bb4', 'A4', 'C5', 'A4', 'C5', 'Bb4', 'D5', 'Bb4', 'F4']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [FA, BB, FA, BB, BB, DO, BB, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · alegre, sin tensión', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
