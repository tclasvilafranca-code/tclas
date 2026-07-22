# -*- coding: utf-8 -*-
"""Taller de practica - Beauty and Beast (Julia, cancion 20, arr.
   Naf, Fa mayor, 4/4). Nivel inicial con toque extra: la mano
   derecha vuela una octava mas arriba de lo escrito."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · BEAUTY AND BEAST'
TS = (4, 4)

FA = ['F3', 'A3', 'C4']
SIb = ['Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La famosa canción de La Bella y la Bestia, en Fa mayor. Hoy: ¡la derecha vuela una octava más alta!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). ¡Cuidado con el Sib, la tecla negra!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La octava que vuela: la derecha toca más alto', 2,
                          'Lo que vamos a practicar hoy. En esta canción, la mano derecha toca una octava más arriba de lo que parece escrito: ¡vuela más alto de lo normal!')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'A4', 'G4', 'F4', 'A5', 'A5', 'G5', 'F5']]
    y = system_block(c, x0, w0, y, gap, 'a) La misma nota, abajo y luego una octava arriba', ev2a, clef='treble', time_sig=TS)

    ev2b = ([{'rest': True, 'dur': 'h'}] + [{'pitch': p, 'dur': 'e'} for p in ['A5', 'G5', 'F5', 'A5']] +
            [{'pitch': 'C6', 'dur': 'h'}, {'rest': True, 'dur': 'h'}])
    y = system_block(c, x0, w0, y, gap, 'b) El silencio que espera, y la melodía que despega arriba', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['A5', 'A5', 'G5', 'F5']]
    bass2c = [{'pitches': FA, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía arriba, con el acorde de Fa repetido abajo', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: la izquierda repite su acorde mientras la derecha vuela arriba.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía que vuela sobre el acorde repetido', 2,
                          'La izquierda repite su acorde de Fa en cada tiempo; la derecha canta una octava más arriba de lo esperado.')
    y -= 7
    treb1 = ([{'rest': True, 'dur': 'h'}] + [{'pitch': p, 'dur': 'e'} for p in ['A5', 'G5', 'F5', 'A5']] +
             [{'pitch': 'C6', 'dur': 'h'}, {'rest': True, 'dur': 'h'}])
    bass1 = [{'pitches': FA, 'dur': 'q'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El despegue sobre Fa repetido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A5', 'G5', 'F5', 'A5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía volando arriba: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde repetido no vuela con la melodía', 3,
                          'La izquierda repite su acorde de Sib, sin cambiar; la derecha vuela arriba sin arrastrar a la de abajo.')
    y -= 7
    treb3 = ([{'rest': True, 'dur': 'h'}] + [{'pitch': p, 'dur': 'e'} for p in ['D6', 'C6', 'Bb5', 'D6']] +
             [{'pitch': 'F6', 'dur': 'h'}, {'rest': True, 'dur': 'h'}])
    bass3 = [{'pitches': SIb, 'dur': 'q'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El despegue sobre Sib repetido; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D6', 'C6', 'Bb5', 'D6']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sobre Sib', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Beauty and Beast casi entera', 3,
                          'Con la partitura al lado: ¡recuerda que la derecha vuela una octava más arriba de lo escrito!')
    y -= 7
    treb5 = ([{'rest': True, 'dur': 'h'}] + [{'pitch': p, 'dur': 'e'} for p in ['A5', 'G5', 'F5', 'A5']] +
             [{'pitch': 'C6', 'dur': 'h'}] +
             [{'rest': True, 'dur': 'h'}] + [{'pitch': p, 'dur': 'e'} for p in ['A5', 'G5', 'F5', 'A5']] +
             [{'pitch': 'C6', 'dur': 'h'}])
    bass5 = [{'pitches': FA, 'dur': 'q'}] * 12
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Beauty and Beast casi completa · con la octava que vuela', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
