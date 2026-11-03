# -*- coding: utf-8 -*-
"""Taller de practica - Have Yourself a Merry Little Christmas (Eva,
   cancion 6, Do mayor, 4/4). Mismo arreglo que el de Dilan (que trabaja la
   melodia en acordes con un eco dinamico), pero enfoque DISTINTO para Eva:
   el DIALOGO ENTRE LAS DOS MANOS, como un coro que se responde a si mismo."""
from page_layout_common import *

SONG_KICKER = 'EVA · DICIEMBRE · HAVE YOURSELF A MERRY LITTLE CHRISTMAS'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico clásico en Do mayor. El reto: un diálogo entre las dos manos, como un coro que se responde.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Escala completa, ida y vuelta', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 3), ('C4', 1), ('G4', 5), ('C4', 1)] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desde el Mi', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El diálogo: una mano pregunta, la otra responde', 2,
                          'La dificultad exacta de esta canción. Una mano toca una frase corta; la otra la repite como un eco, como un coro respondiéndose a sí mismo.')
    y -= 9
    treb2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4']] + [{'rest': True, 'dur': 'q'}]
    bass2a = [{'rest': True, 'dur': 'q'}] * 3 + [{'pitch': 'C3', 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2a, bass2a, 'a) La derecha pregunta, la izquierda entra al final', grand_gap_mult=7.3, time_sig=TS)

    treb2b = [{'rest': True, 'dur': 'q'}] * 3 + [{'pitch': 'G4', 'dur': 'q'}]
    bass2b = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'D3', 'E3']] + [{'rest': True, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2b, bass2b, 'b) Ahora empieza la izquierda; la derecha responde', grand_gap_mult=7.3, time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes básicos de esta tonalidad.')
    y -= 9
    pattern_a = [(DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (SOL, 'Sol')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Sol-Fa-Sol, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas tranquilas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la melodía y el acorde se turnan el protagonismo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre los acordes', 2,
                          'La izquierda sostiene el acorde; la derecha canta la melodía del villancico encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'E4', 'C4', 'D4', 'E4', 'D4']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [DO, SOL, FA, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase entera, con su acorde debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4', 'D4', 'F4', 'A4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando el dibujo', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'El diálogo con acordes reales', 3,
                          'Ahora el diálogo entre manos ocurre con acordes de verdad debajo, no solo notas sueltas.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4']] + [{'rest': True, 'dur': 'q'}]
    bass3 = [{'rest': True, 'dur': 'q'}] * 3 + [{'pitches': DO, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La derecha pregunta; el acorde de la izquierda responde', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['C4', 'E4', 'D4', 'F4'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía en corcheas, más viva', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · el villancico casi entero', 3,
                          'Con la partitura al lado: deja que las manos se turnen el protagonismo, como un coro entero.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['E4', 'F4', 'G4', 'E4', 'C4', 'D4', 'E4', 'D4', 'C4', 'E4', 'G4', 'E4', 'D4', 'F4', 'A4', 'F4']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [DO, SOL, FA, SOL, DO, SOL, FA, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Tranquilo ♩≈92, con calidez', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
