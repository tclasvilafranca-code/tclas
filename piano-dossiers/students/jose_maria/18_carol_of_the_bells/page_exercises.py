# -*- coding: utf-8 -*-
"""Taller de practica - Carol of the Bells (Jose Maria, cancion 18,
   Sol menor, 3/4). Enfoque relajado: el dibujo que se repite -- la
   misma frase de cuatro notas, una y otra vez, sin cansarse ni
   apretar."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · MAYO · CAROL OF THE BELLS'
TS = (3, 4)

Gm = ['G2', 'Bb2', 'D3']
Cm = ['C3', 'Eb3', 'G3']
D = ['D3', 'F#3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico tradicional en Sol menor. Sin prisa: el mismo dibujo, sin cansarse.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol menor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Sib(3) Do(4) Re(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('Bb4', 3), ('A4', 2), ('G4', 1), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Bb4', 'D5'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol menor, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El dibujo que se repite, sin cansarse', 2,
                          'Lo que vamos a cuidar en esta pieza. La misma frase corta de cuatro notas se repite una y otra vez — sin apretar la mano ni acelerarse por la repetición.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'A4', 'Bb4'] * 3]
    y = system_block(c, x0, w0, y, gap, 'a) El dibujo repetido, con la mano relajada', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'b) Las mismas notas, en valores largos: para sentir la calma', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'A4', 'Bb4'] * 3]
    bass2c = [{'pitches': Gm, 'dur': 'h.'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El dibujo repetido sobre el acorde de Solm, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en Sol menor', 2,
                          'Solm–Dom–Re: los acordes reales de esta pieza.')
    y -= 11
    pattern_a = [(Gm, 'Solm'), (Cm, 'Dom'), (D, 'Re'), (Gm, 'Solm')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Solm-Dom-Re-Solm, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el dibujo se repite mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el dibujo repetido sobre el acorde de Dom', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha repite su dibujo, sin cansarse ni apretar.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'D5', 'Eb5'] * 3]
    bass1 = [{'pitches': Cm, 'dur': 'h.'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El dibujo repetido sobre Dom, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'h.'} for p in ['C5', 'Eb5']]
    y = system_block(c, x0, w0, y, gap, 'b) Las mismas notas, en valores largos: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del dibujo', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha repite, sin arrastrar a la de abajo ni acelerarse.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'E5', 'F#5'] * 3]
    bass3 = [{'pitches': D, 'dur': 'h.'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El dibujo repetido sobre Re; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'h.'} for p in ['D5', 'F#5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: las mismas notas, en valores largos', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Carol of the Bells casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que el dibujo se repita sin cansarse, sobre un acorde que no se mueve.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'A4', 'Bb4'] * 3] +
             [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'D5', 'Eb5'] * 3])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [Gm, Gm, Gm, Gm, Cm, Cm, Cm, Cm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · con el dibujo repitiéndose, sin prisa', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
