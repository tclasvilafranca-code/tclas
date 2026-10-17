# -*- coding: utf-8 -*-
"""Taller de practica - Mary Mary Quite Contrary (Julia, cancion 9,
   Fa mayor, 2/4). Nivel inicial: el compas cortito -- solo dos
   tiempos por compas, sin perder ninguno."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · MARY MARY QUITE CONTRARY'
TS = (2, 4)

FA = ['F2', 'A2', 'C3']
SIb = ['Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción tradicional en Fa mayor. Hoy el compás es cortito: ¡solo dos tiempos!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). ¡Busca tu nota casa, el Fa!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El compás cortito: solo dos tiempos', 2,
                          'Lo que vamos a practicar hoy. Cada compás dura solo dos tiempos, muy cortito — hay que contar rápido "1-2, 1-2" sin perder ninguno.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'A4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) El compás cortito, contando "1-2"', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h'} for p in ['F4', 'G4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Las mismas notas, más despacio: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'A4', 'A4', 'G4']]
    bass2c = [{'pitches': FA, 'dur': 'h'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El compás cortito sobre el acorde de Fa', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SIb, 'Sib'), (DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el compás cortito avanza mientras el acorde se queda quieto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el compás cortito sobre el acorde de Sib', 2,
                          'La izquierda marca negras firmes; la derecha canta su melodía cortita encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'C5', 'Bb4', 'D5', 'D5', 'C5']]
    bass1 = [{'pitches': SIb, 'dur': 'h'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Sib, con negras firmes', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'h'} for p in ['Bb4', 'C5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Las mismas notas, más despacio: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se acelera', 3,
                          'La izquierda mantiene su negra firme; la derecha canta rápido, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'D5', 'C5', 'E5', 'E5', 'D5']]
    bass3 = [{'pitches': DO, 'dur': 'h'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre Do; el acorde no se acelera', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'h'} for p in ['C5', 'D5', 'E5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más despacio', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Mary Mary Quite Contrary casi entera', 3,
                          'Con la partitura al lado: ¡cuenta rápido "1-2" en cada compás cortito!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'A4', 'A4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'C5', 'Bb4', 'D5', 'D5', 'C5']])
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [FA, FA, FA, FA, SIb, SIb, SIb, SIb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con el compás cortito', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
