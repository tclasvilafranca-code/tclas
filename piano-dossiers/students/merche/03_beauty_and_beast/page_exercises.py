# -*- coding: utf-8 -*-
"""Taller de practica - Beauty and Beast (Merce, cancion 3, arr.
   Naf, Fa mayor, 4/4). Mismo arreglo que el de Julia, pero con
   enfoque propio y distinto: el acompanamiento en bloque -- el
   mismo acorde repetido con firmeza, igual de solido en cada
   tiempo. Nivel basico pero solido, tono adulto."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · BEAUTY AND BEAST'
TS = (4, 4)

FA = ['F2', 'A2', 'C3']
SIb = ['Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de La Bella y la Bestia, en Fa mayor. Hoy trabajamos la firmeza del acorde repetido.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El Sib es la única tecla negra de esta posición.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El acompañamiento en bloque: firmeza constante', 2,
                          'Lo que trabajamos hoy. La izquierda repite el mismo acorde en cada tiempo: debe sonar igual de firme la primera vez que la última, sin perder fuerza.')
    y -= 9
    ev2a = [{'pitches': FA, 'dur': 'q'}] * 4
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Fa, repetido cuatro veces, con firmeza pareja', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': SIb, 'dur': 'q'}] * 4
    y = system_block(c, x0, w0, y, gap, 'b) Lo mismo sobre Sib: cada golpe, igual de firme', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'G4']]
    bass2c = [{'pitches': FA, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde repetido, sin perder firmeza', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SIb, 'Sib'), (DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el acorde repetido mantiene su firmeza mientras la melodía canta encima.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde repetido de Fa', 2,
                          'La izquierda repite su acorde de Fa con firmeza constante; la derecha canta la melodía encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre el acorde de Fa, repetido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la firmeza no depende de la melodía', 3,
                          'La izquierda mantiene su acorde repetido, igual de firme; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'D5']]
    bass3 = [{'pitches': SIb, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre el acorde de Sib, repetido; la firmeza no cambia', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sobre Sib', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Beauty and Beast casi entera', 3,
                          'Con la partitura al lado: mantén el acorde repetido igual de firme del principio al final.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'A4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'D5']])
    bass5 = [{'pitches': p, 'dur': 'q'} for p in [FA, FA, FA, FA, SIb, SIb, SIb, SIb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Beauty and Beast casi completa · con el acompañamiento en bloque firme', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
