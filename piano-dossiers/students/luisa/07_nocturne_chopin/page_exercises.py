# -*- coding: utf-8 -*-
"""Taller de practica - Nocturne Op.9, easy (Luisa, cancion 7,
   Chopin, Do mayor, 3/4). Nivel hobby, sin complicaciones: las
   notas largas que se quedan sonando -- relajate y escucha."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · NOCTURNE OP.9 (CHOPIN)'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El Nocturno de Chopin, simplificado, en Do mayor. Hoy: notas largas que se quedan sonando.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Las notas largas: relájate y escucha', 2,
                          'Lo de hoy. Cada nota larga dura todo el compás: no hay que hacer nada más que dejarla sonar y escuchar, relajada.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h.'} for p in ['E4', 'D4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) Una nota, un compás entero: escucha cómo suena', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, en notas cortas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': 'E4', 'dur': 'h.'}]
    bass2c = [{'pitches': DO, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La nota larga sobre el acorde de Do, tranquilo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes, sin más complicación.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: deja que las notas largas suenen tranquilas.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la nota larga sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, tranquila; la derecha deja sonar su nota larga.')
    y -= 7
    treb1 = [{'pitch': 'A4', 'dur': 'h.'}]
    bass1 = [{'pitches': FA, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La nota larga sobre Fa, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, en notas cortas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la nota larga no descoloca el acorde', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha deja sonar su nota, tranquila.')
    y -= 7
    treb3 = [{'pitch': 'B4', 'dur': 'h.'}]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La nota larga sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en notas cortas', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Nocturne Op.9 casi entero', 3,
                          'Con la partitura al lado: deja sonar cada nota larga, relajada, sin prisa.')
    y -= 7
    treb5 = [{'pitch': 'E4', 'dur': 'h.'}, {'pitch': 'G4', 'dur': 'h.'}]
    bass5 = [{'pitches': DO, 'dur': 'h.'}, {'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Nocturne Op.9 casi completo · relajada, sin prisa', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
