# -*- coding: utf-8 -*-
"""Taller de practica - The Beginner, Le Debut (Luisa, cancion 6,
   Cornelius Gurlitt Op.211 No.3, Do mayor, 3/4, a 4 manos). Nivel
   hobby, sin complicaciones: el sube y baja del volumen, como una
   ola tranquila."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · THE BEGINNER (A 4 MANOS)'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'The Beginner, de Gurlitt, en Do mayor, a 4 manos. Hoy: una ola tranquila de volumen.')
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

    y = exercise_heading(c, y, 2, 'El sube y baja del volumen: una ola tranquila', 2,
                          'Lo de hoy. El sonido crece un poquito y luego se relaja, como una ola pequeña: sin esfuerzo, sin prisa.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'E4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'a) La ola que sube, poquito a poco', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'E4', 'D4', 'E4', 'D4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Y la ola que baja, igual de tranquila', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La ola sobre el acorde de Do, tranquilo', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: la ola de volumen crece y se relaja tranquila.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la ola sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, tranquila; la derecha hace su ola de volumen encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La ola sobre Fa, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la ola no descoloca el acorde', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha hace su ola sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La ola sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · The Beginner casi entera', 3,
                          'Con la partitura al lado: deja que la ola de volumen crezca y se relaje, sin prisa.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'E4', 'D4']])
    bass5 = [{'pitches': DO, 'dur': 'h.'}, {'pitches': DO, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'The Beginner casi completa · con la ola tranquila', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
