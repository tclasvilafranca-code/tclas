# -*- coding: utf-8 -*-
"""Taller de practica - Nocturne Op.9 (Merce, cancion 7, Chopin,
   arr. Benny Chaw, Do mayor -- armadura sin alteraciones, con
   algunos cromatismos de paso en el bajo, 3/4). Nivel basico pero
   solido: el silencio expresivo -- contar los compases de
   descanso con precision."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · NOCTURNE OP.9 (CHOPIN)'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El Nocturno Op.9 de Chopin, simplificado en Do mayor. Hoy: contar los compases de silencio con precisión.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Localiza el Do central como punto de referencia.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El silencio expresivo: contar el compás de descanso', 2,
                          'Lo que trabajamos hoy. Esta pieza tiene compases enteros de silencio: hay que contarlos con la misma precisión que si estuvieras tocando, sin perder el pulso.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h.'} for p in ['E4']] + [{'rest': True, 'dur': 'h.'}] + \
           [{'pitch': p, 'dur': 'h.'} for p in ['G4']] + [{'rest': True, 'dur': 'h.'}]
    y = system_block(c, x0, w0, y, gap, 'a) Una nota, un compás entero de silencio, y otra nota', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.'} for p in ['E4', 'D4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, sin silencio: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': 'E4', 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}]
    bass2c = [{'pitches': DO, 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El silencio en las dos manos a la vez, contado con calma', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: el silencio se cuenta igual en las dos manos, sin adelantarse.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la nota y el silencio, sobre el acorde de Fa', 2,
                          'La izquierda toca su acorde y luego calla un compás entero; la derecha hace lo mismo con su nota.')
    y -= 7
    treb1 = [{'pitch': 'A4', 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}]
    bass1 = [{'pitches': FA, 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La nota y el silencio, sobre Fa', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'h.'} for p in ['A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, sin silencio: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el silencio no rompe el pulso', 3,
                          'La izquierda cuenta su silencio con calma; la derecha entra después, exactamente a tiempo.')
    y -= 7
    treb3 = [{'rest': True, 'dur': 'h.'}, {'pitch': 'B4', 'dur': 'h.'}]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El silencio cruzado: mientras una mano calla, la otra suena', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'h.'} for p in ['B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, sin silencio', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Nocturne Op.9 casi entero', 3,
                          'Con la partitura al lado: cuenta cada compás de silencio con la misma precisión que una nota.')
    y -= 7
    treb5 = ([{'pitch': 'E4', 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}] +
             [{'pitch': 'G4', 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}])
    bass5 = [{'pitches': DO, 'dur': 'h.'}, {'rest': True, 'dur': 'h.'},
             {'pitches': SOL, 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Nocturne Op.9 casi completo · con el silencio expresivo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
