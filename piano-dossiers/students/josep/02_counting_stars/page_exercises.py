# -*- coding: utf-8 -*-
"""Taller de practica - Counting Stars (Josep, cancion 2, Do mayor,
   4/4). Angulo: la SINCOPA -- entrar justo antes o despues del
   tiempo, no encima de el, tal como hace la version real de la
   cancion con sus corcheas y silencios de anacrusa."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · SEPTIEMBRE · COUNTING STARS (ONEREPUBLIC)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de OneRepublic en Do mayor. El reto: entrar justo antes o después del tiempo, no encima.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('D4', 2), ('G4', 5), ('F4', 4), ('E4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La síncopa: entrar antes o después del tiempo', 2,
                          'La dificultad exacta de esta canción. Un silencio de corchea justo antes de la nota hace que "entres" un poquito antes de lo que esperas — cuenta el silencio con la misma firmeza que la nota.')
    y -= 9
    ev2a = ([{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'q'},
             {'rest': True, 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'q'}] * 2)
    y = system_block(c, x0, w0, y, gap, 'a) Silencio-nota-nota larga: la entrada llega un pelín tarde', ev2a, clef='treble', time_sig=TS)

    ev2b = ([{'pitch': 'C4', 'dur': 'e', 'beam': 0}, {'rest': True, 'dur': 'e'},
             {'pitch': 'E4', 'dur': 'e', 'beam': 0}, {'rest': True, 'dur': 'e'},
             {'pitch': 'G4', 'dur': 'e', 'beam': 1}, {'rest': True, 'dur': 'e'},
             {'pitch': 'E4', 'dur': 'e', 'beam': 1}, {'rest': True, 'dur': 'e'}] * 2)
    y = system_block(c, x0, w0, y, gap, 'b) Nota-silencio: la entrada llega un pelín pronto', ev2b, clef='treble', time_sig=TS)

    treb2c = ([{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'q'},
               {'rest': True, 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'q'}] * 2)
    bass2c = [{'pitches': p, 'dur': 'w'} for p in [DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La síncopa sobre un acorde firme y quieto debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (FA, 'Fa')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la síncopa se apoya en un acorde que no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la síncopa sobre el acorde quieto', 2,
                          'La izquierda sostiene el acorde entero; la derecha entra siempre un pelín antes o después del tiempo, nunca encima.')
    y -= 7
    treb1 = ([{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'q'},
              {'rest': True, 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'q'}] * 2)
    bass1 = [{'pitches': p, 'dur': 'w'} for p in [DO, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La síncopa, con el acorde firme debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'D4', 'G4', 'F4', 'E4', 'D4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin síncopas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la síncopa no contagia al acorde', 3,
                          'La izquierda se queda perfectamente quieta mientras la derecha entra y sale de tiempo — que no se le pegue el "tropiezo" a la mano de abajo.')
    y -= 7
    treb3 = ([{'pitch': 'C4', 'dur': 'e', 'beam': 0}, {'rest': True, 'dur': 'e'},
              {'pitch': 'E4', 'dur': 'e', 'beam': 0}, {'rest': True, 'dur': 'e'},
              {'pitch': 'G4', 'dur': 'e', 'beam': 1}, {'rest': True, 'dur': 'e'},
              {'pitch': 'E4', 'dur': 'e', 'beam': 1}, {'rest': True, 'dur': 'e'}] * 2)
    bass3 = [{'pitches': p, 'dur': 'w'} for p in [SOL, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Nota-silencio arriba; acorde quieto abajo', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'E4', 'D4', 'C4', 'E4', 'D4', 'C4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase al revés, tranquila', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Counting Stars casi entera', 3,
                          'Con la partitura al lado: cuenta cada silencio con la misma firmeza que cada nota — así la síncopa suena decidida, no dudosa.')
    y -= 7
    treb5 = ([{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'q'},
              {'rest': True, 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'q'}] * 2 +
             [{'pitch': 'C4', 'dur': 'e', 'beam': 2}, {'rest': True, 'dur': 'e'},
              {'pitch': 'E4', 'dur': 'e', 'beam': 2}, {'rest': True, 'dur': 'e'},
              {'pitch': 'G4', 'dur': 'e', 'beam': 3}, {'rest': True, 'dur': 'e'},
              {'pitch': 'E4', 'dur': 'e', 'beam': 3}, {'rest': True, 'dur': 'e'}] * 2)
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, FA, SOL, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈120, con la síncopa decidida', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
