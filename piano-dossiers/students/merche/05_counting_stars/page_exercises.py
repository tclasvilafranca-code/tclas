# -*- coding: utf-8 -*-
"""Taller de practica - Counting Stars (Merce, cancion 5,
   OneRepublic, arr. Becky Messer, Easy Version, Do mayor, 4/4).
   Mismo arreglo compartido con Jose Maria/Josep/Nel, pero con
   enfoque propio y distinto: el anacrusis -- la frase que empieza
   antes del tiempo fuerte. Nivel basico pero solido."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · COUNTING STARS'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Counting Stars, de OneRepublic, en Do mayor. Hoy: frases que empiezan justo antes del tiempo fuerte.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Localiza el Do central como punto de referencia.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El anacrusis: empezar antes del tiempo fuerte', 2,
                          'Lo que trabajamos hoy. Varias frases de esta canción empiezan con un silencio de corchea y arrancan justo antes del tiempo fuerte: hay que entrar sin adelantarse.')
    y -= 9
    ev2a = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4']])
    y = system_block(c, x0, w0, y, gap, 'a) El silencio de corchea, y la frase que arranca justo después', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, empezando justo en el tiempo: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4']])
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El anacrusis sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el acorde sostenido espera mientras la melodía entra en su anacrusis.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el anacrusis sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha entra en su anacrusis justo antes del tiempo fuerte.')
    y -= 7
    treb1 = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['C5', 'D5', 'E5', 'F5', 'E5', 'D5', 'C5']])
    bass1 = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El anacrusis sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['C5', 'D5', 'E5', 'F5', 'E5', 'D5', 'C5']])
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el anacrusis no descoloca el acorde', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha entra en su anacrusis sin arrastrar a la de abajo.')
    y -= 7
    treb3 = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['D5', 'E5', 'F#5', 'G5', 'F#5', 'E5', 'D5']])
    bass3 = [{'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El anacrusis sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['D5', 'E5', 'F#5', 'G5', 'F#5', 'E5', 'D5']])
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sobre Sol', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Counting Stars casi entera', 3,
                          'Con la partitura al lado: entra en cada anacrusis justo antes del tiempo fuerte, sin adelantarte.')
    y -= 7
    treb5 = (([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4']]) +
             ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['C5', 'D5', 'E5', 'F5', 'E5', 'D5', 'C5']]))
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Counting Stars casi completa · con el anacrusis que entra a tiempo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
