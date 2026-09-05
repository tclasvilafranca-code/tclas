# -*- coding: utf-8 -*-
"""Taller de practica - We Wish You a Merry Christmas (Merce,
   cancion 19, arr. Gilbert DeBenedetti, Sol mayor -- armadura de
   1 sostenido, confirmada por los simbolos G-C-A7-D-B7-Am-D7,
   3/4). Nivel basico pero solido: los acordes de septima que
   resuelven -- tension y descanso."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · WE WISH YOU A MERRY CHRISTMAS'
TS = (3, 4)

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D2', 'F#2', 'A2']
RE7 = ['D2', 'F#2', 'A2', 'C3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'We Wish You a Merry Christmas, en Sol mayor. Hoy: los acordes de séptima que resuelven.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5). El Fa# es la única alteración de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los acordes de séptima que resuelven: tensión y descanso', 2,
                          'Lo que trabajamos hoy. Un acorde con séptima (como Re7) suena en tensión y "pide" resolver al acorde siguiente: siente ese momento en que la tensión se relaja.')
    y -= 9
    ev2a = [{'pitches': RE7, 'dur': 'h.'}]
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Re7, en tensión: escucha cómo "pide" resolver', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': RE7, 'dur': 'h'}, {'pitches': SOL, 'dur': 'q'}]
    y = system_block(c, x0, w0, y, gap, 'b) Re7 resolviendo a Sol: la tensión se relaja', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4']]
    bass2c = [{'pitches': RE7, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde de Re7, en tensión', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Re-Sol, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: siente la tensión de Re7 y su resolución en Sol.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre la resolución de Re7 a Sol', 2,
                          'La izquierda toca Re7 y resuelve a Sol; la derecha canta la melodía sin detenerse.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4']] + [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5']]
    bass1 = [{'pitches': RE7, 'dur': 'h.'}, {'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) De Re7 a Sol: tensión y descanso', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía sobre la tensión: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Do no se tensa', 3,
                          'La izquierda sostiene el acorde de Do, quieta; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4']]
    bass3 = [{'pitches': DO, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre el acorde de Do; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · We Wish You a Merry Christmas casi entera', 3,
                          'Con la partitura al lado: siente la tensión de cada acorde de séptima y disfruta su resolución.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5']])
    bass5 = [{'pitches': RE7, 'dur': 'h.'}, {'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'We Wish You a Merry Christmas casi completa · con la tensión que resuelve', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
