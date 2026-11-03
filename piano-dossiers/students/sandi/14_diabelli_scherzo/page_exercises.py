# -*- coding: utf-8 -*-
"""Taller de practica - Scherzo (Sandi, cancion 14, Anton Diabelli,
   28 Melodic Studies Op.149 No.6, Do mayor -- armadura sin
   alteraciones confirmada por render directo, 3/4, Allegro, a 4
   manos, forma Scherzo-Trio en Mib mayor-D.C. al Fine). Nivel
   avanzado: el picado con acento -- corto, pero marcado."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · SCHERZO (DIABELLI, A 4 MANOS)'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Scherzo, de Anton Diabelli, a 4 manos, en Do mayor. Hoy: el picado con acento.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). El Primo se mueve en esta posición durante todo el Scherzo.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El picado con acento: corto, pero marcado', 3,
                          'La dificultad de hoy. Cada nota lleva staccato Y acento a la vez: corta como un picado normal, pero con más peso y decisión, sin convertirse en un golpe seco ni en un picado suave.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5', 'C5', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'a) Picado acentuado: corto, con peso, sin dureza', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'B4', 'A4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Bajando, con la misma marca exacta en cada nota', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5']]
    bass2c = [{'rest': True, 'dur': 'q'}, {'pitches': DO, 'dur': 'q'}, {'pitches': DO, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El picado acentuado sobre el acompañamiento en tresillo del Secondo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes principales de esta tonalidad.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el picado acentuado del Primo debe destacar sobre el acompañamiento del Secondo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el picado acentuado sobre el acorde de Fa', 3,
                          'La izquierda marca el acompañamiento en silencio-acorde-acorde; la derecha pica con acento, corta y decidida.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5']]
    bass1 = [{'rest': True, 'dur': 'q'}, {'pitches': FA, 'dur': 'q'}, {'pitches': FA, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El picado acentuado sobre el acompañamiento de Fa', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: comprueba que cada nota es corta pero pesada', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acompañamiento de Sol no ablanda el picado', 3,
                          'La izquierda marca el acompañamiento sobre Sol; la derecha mantiene su picado acentuado sin dejarse arrastrar por el silencio de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5']]
    bass3 = [{'rest': True, 'dur': 'q'}, {'pitches': SOL, 'dur': 'q'}, {'pitches': SOL, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El picado acentuado sobre el acompañamiento de Sol', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'B4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando con el mismo picado', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Scherzo casi entero', 3,
                          'Con la partitura al lado: mantén el picado corto pero marcado en cada nota, del principio al final.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5']])
    bass5 = ([{'rest': True, 'dur': 'q'}, {'pitches': DO, 'dur': 'q'}, {'pitches': DO, 'dur': 'q'}] +
             [{'rest': True, 'dur': 'q'}, {'pitches': FA, 'dur': 'q'}, {'pitches': FA, 'dur': 'q'}])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Scherzo casi completo · picado con acento, del principio al final', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
