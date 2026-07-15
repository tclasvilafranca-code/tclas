# -*- coding: utf-8 -*-
"""Taller de practica - When I Was Your Man (Dilan, cancion 14, Do mayor,
   4/4). Estructura DISTINTA otra vez: es una balada de piano solo, casi
   toda en acordes en bloque -- el foco es memorizar la FORMA de cada
   acorde en la mano, para poder tocarla sin mirar la partitura ni las
   manos, como haria un pianista de verdad en una balada asi."""
from page_layout_common import *

SONG_KICKER = 'DILAN · ABRIL · WHEN I WAS YOUR MAN (BRUNO MARS)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de piano solo en Do mayor. Casi todo son acordes en bloque.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 5), ('E4', 3), ('F4', 4), ('D4', 2), ('E4', 3), ('C4', 1)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Baja a saltos hasta Do', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 3), ('C4', 1), ('G4', 5), ('C4', 1)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desde el Mi', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Tocar de memoria: la forma del acorde en la mano', 2,
                          'En una balada de piano solo no hay tiempo de leer cada acorde: la mano tiene que "saber" su forma. Mira el acorde, tócalo, y a la tercera vez ya no mires la partitura.')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa')] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Mirando: Do y Fa, sintiendo la forma de cada uno', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa')] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora tapa la partitura: los mismos dos acordes, de memoria', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'C4', 'C4', 'C4']]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa')] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, sin mirar: solo la forma', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Fa–Sol–Do–Sol: memoriza el orden antes de memorizar las notas.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sol-Do-Sol, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, memoriza 4 compases enteros, y la canción casi completa.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · melodía sobre acordes en bloque', 2,
                          'La izquierda toca acordes largos; la derecha canta la melodía por encima.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('G4', 5), ('E4', 3), ('F4', 4), ('D4', 2), ('E4', 3), ('C4', 1), ('D4', 2), ('E4', 3)]]
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La melodía sobre los acordes', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El reto de memoria: 4 compases enteros', 3,
                          'Estudia estos 4 compases mirando, luego tapa la partitura entera y tócalos solo de memoria. Si te pierdes, no mires: para y vuelve a empezar el compás.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 3), ('C4', 1), ('G4', 5), ('C4', 1), ('D4', 2), ('C4', 1), ('E4', 3), ('D4', 2)]]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (DO, 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Cuatro compases para memorizar de verdad', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · When I Was Your Man casi entera', 3,
                          'Con la partitura al lado la primera vez; luego intenta un fragmento de memoria.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('G4', 5), ('E4', 3), ('F4', 4), ('D4', 2), ('E4', 3), ('C4', 1), ('D4', 2), ('E4', 3)]]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['E4', 'C4', 'G4', 'C4', 'D4', 'C4', 'E4', 'D4']]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do'), (DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (DO, 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La balada casi completa · ♩≈72, con sentimiento', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
