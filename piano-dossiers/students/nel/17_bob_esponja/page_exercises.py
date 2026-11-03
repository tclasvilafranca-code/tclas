# -*- coding: utf-8 -*-
"""Taller de practica - Bob Esponja, cancion inicial (Nel, cancion
   17, Mi mayor, 4/4). Enfoque: el staccato que salta -- notas
   cortas y decididas, separadas por pequenos silencios, para el
   caracter saltarin de esta melodia."""
from page_layout_common import *

SONG_KICKER = 'NEL · MAYO · BOB ESPONJA (CANCIÓN INICIAL)'
TS = (4, 4)

E = ['E2', 'G#2', 'B2']
A = ['A2', 'C#3', 'E3']
B = ['B2', 'D#3', 'F#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La canción inicial de Bob Esponja, en Mi mayor. El reto: el staccato que salta, corto y decidido.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi mayor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol#(3) La(4) Si(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('F#4', 2), ('G#4', 3), ('A4', 4), ('B4', 5), ('A4', 4), ('G#4', 3), ('F#4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G#4', 'B4', 'G#4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El staccato que salta: corto y decidido', 2,
                          'La dificultad exacta de esta canción. Cada nota es corta y suelta, como un saltito, con un pequeño silencio detrás antes de la siguiente.')
    y -= 9
    ev2a = [{'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
            {'pitch': 'F#4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
            {'pitch': 'G#4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
            {'pitch': 'A4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    y = system_block(c, x0, w0, y, gap, 'a) Notas cortas, con su silencio detrás', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F#4', 'G#4', 'A4', 'G#4', 'F#4', 'E4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Las mismas notas, unidas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'F#4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'G#4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'A4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    bass2c = [{'pitches': E, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El staccato sobre el acorde de Mi, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Mi–La–Si–Mi: los acordes reales de esta canción.')
    y -= 11
    pattern_a = [(E, 'Mi'), (A, 'La'), (B, 'Si'), (E, 'Mi')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mi-La-Si-Mi, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el staccato salta mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el staccato sobre el acorde de La', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha salta con sus notas cortas y decididas.')
    y -= 7
    treb1 = [{'pitch': 'A4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'B4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'C#5', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'B4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    bass1 = [{'pitches': A, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El staccato sobre La, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C#5', 'B4', 'A4', 'G#4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Las mismas notas, unidas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del staccato', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha salta, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': 'B4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'C#5', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'D#5', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'C#5', 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    bass3 = [{'pitches': B, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El staccato salta; el acorde de Si no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C#5', 'D#5', 'C#5', 'B4', 'A4', 'B4', 'C#5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, unida', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Bob Esponja casi entera', 3,
                          'Con la partitura al lado: deja que cada nota salte, corta y decidida, sobre un acorde que no se mueve.')
    y -= 7
    treb5 = ([{'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'F#4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'G#4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'A4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}] +
             [{'pitch': 'A4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'B4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'C#5', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
              {'pitch': 'B4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [E, E, A, A]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con el staccato saltando', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
