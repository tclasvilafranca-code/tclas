# -*- coding: utf-8 -*-
"""Taller de practica - The Wheels on the Bus (Arnau, cancion 10, Fa
   mayor, 4/4). Nivel iniciacion: primera tonalidad con un bemol.
   La nota repetida gira, sin miedo -- y ahora la armadura de Fa
   mayor se indica una vez, al principio de cada pentagrama."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · THE WHEELS ON THE BUS'
TS = (4, 4)
KEY = 'Fa mayor'

FA = ['F2', 'A2', 'C3']
SIb = ['Bb1', 'D2', 'F2']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Primera canción en Fa mayor: un solo bemol (Sib), que se escribe una vez, al principio.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: posición de 5 dedos en Fa mayor', 1,
                          'Dedo 1 en Fa: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca una tecla negra.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja la posición de Fa mayor', ev1a, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 2, 'Las ruedas que giran: la misma nota, sin miedo', 2,
                          'La melodía repite la misma nota varias veces, como las ruedas del autobús: "round and round".')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'C5', 'C5', 'C5', 'Bb4', 'Bb4', 'A4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) La rueda que gira: nota repetida', ev2a, clef='treble', time_sig=TS, key_sig=KEY)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'Bb4', 'A4', 'G4', 'F4', 'G4', 'A4', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo camino, ahora sin repetir: para comparar', ev2b, clef='treble', time_sig=TS, key_sig=KEY)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'C5', 'C5', 'C5', 'Bb4', 'Bb4', 'A4', 'A4']]
    bass2c = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La rueda que gira, sobre el acorde de Fa', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SIb, 'Sib'), (DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS, key_sig=KEY)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El Sib ya no se repite en cada nota: se toca todo el rato, como recuerda la armadura.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la rueda sobre el acorde de Sib', 2,
                          'La izquierda sostiene el acorde de Sib entero, quieta; la derecha gira encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'D5', 'D5', 'C5', 'C5', 'Bb4', 'Bb4']]
    bass1 = [{'pitches': SIb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La rueda sobre Sib, quieto', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'C5', 'Bb4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin repetir: para comparar', treb2, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no gira con la melodía', 3,
                          'La izquierda queda quieta con su acorde; la derecha gira, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'E5', 'E5', 'E5', 'D5', 'D5', 'C5', 'C5']]
    bass3 = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La rueda gira; el acorde de Do no se mueve', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación de la melodía, un poco más arriba', treb4, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · The Wheels on the Bus casi entera', 3,
                          'Con la partitura al lado: ¡deja que las ruedas giren "round and round"!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C5', 'C5', 'C5', 'C5', 'Bb4', 'Bb4', 'A4', 'A4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'D5', 'D5', 'C5', 'C5', 'Bb4', 'Bb4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [FA, FA, SIb, SIb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · las ruedas girando', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    exercises_footer(c, 4)
    c.showPage()
