# -*- coding: utf-8 -*-
"""Taller de practica - Perfect (Julia, cancion 23, Ed Sheeran,
   Do mayor, 12/8). Nivel inicial con toque extra: el compas de
   doce por ocho -- cuatro pasos grandes, cada uno con tres
   corcheas dentro."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · PERFECT (ED SHEERAN)'
TS = (12, 8)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La famosa balada de Ed Sheeran, en Do mayor. Hoy: ¡un compás con cuatro pasos grandes de tres!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). ¡Busca tu nota casa, el Do!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4', 'C4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El compás de doce por ocho: cuatro pasos grandes de tres', 2,
                          'Lo que vamos a practicar hoy. Cada compás tiene cuatro pasos grandes, y cada paso grande esconde tres corcheas dentro: como una balanceo suave y continuo.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['C4', 'D4', 'E4', 'E4', 'D4', 'C4', 'C4', 'D4', 'E4', 'E4', 'D4', 'C4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Cuatro pasos grandes, tres corcheas en cada uno', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, sintiendo solo el paso grande (negra con puntillo)', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'E4', 'D4']]
    bass2c = [{'pitches': DO, 'dur': 'q.'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Los pasos grandes sobre el acorde de Do, repetido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
    y -= 11
    eva = ([{'pitches': DO, 'dur': 'q.', 'label': 'Do'}] * 2 + [{'pitches': FA, 'dur': 'q.', 'label': 'Fa'}] * 2 +
           [{'pitches': SOL, 'dur': 'q.', 'label': 'Sol'}] * 2 + [{'pitches': DO, 'dur': 'q.', 'label': 'Do'}] * 2)
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, dos pasos grandes por acorde', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la izquierda repite su acorde en pasos grandes mientras la derecha canta.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · los pasos grandes sobre el acorde de Fa', 2,
                          'La izquierda repite su acorde de Fa en cada paso grande; la derecha canta la melodía encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'G4', 'A4', 'G4']]
    bass1 = [{'pitches': FA, 'dur': 'q.'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Los pasos grandes sobre Fa, repetido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
             enumerate(['F4', 'G4', 'A4', 'A4', 'G4', 'F4', 'F4', 'G4', 'A4', 'A4', 'G4', 'F4'])]
    y = system_block(c, x0, w0, y, gap, 'b) La misma melodía, con las tres corcheas de cada paso: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el paso grande no mueve el acorde', 3,
                          'La izquierda queda repitiendo su acorde en pasos grandes; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q.'} for p in ['G4', 'A4', 'B4', 'A4']]
    bass3 = [{'pitches': SOL, 'dur': 'q.'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Los pasos grandes sobre Sol, repetido', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q.'} for p in ['B4', 'C5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Perfect casi entera', 3,
                          'Con la partitura al lado: ¡siente los cuatro pasos grandes de cada compás, uno tras otro!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'E4', 'D4']] +
             [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'G4', 'A4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'q.'} for p in [DO, DO, DO, DO, FA, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Perfect casi completa · con los pasos grandes del compás de doce por ocho', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
