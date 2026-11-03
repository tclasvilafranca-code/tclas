# -*- coding: utf-8 -*-
"""Taller de practica - Silent Night, solo (Merce, cancion 26,
   Gruber/Mohr, Do mayor, 3/4, con acordes con bajo distinto tipo
   G/B, Am/C, C7/Bb). Nivel basico pero solido: los acordes con
   bajo distinto -- leer las barras."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · SILENT NIGHT (SOLO)'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
SOLdB = ['B2', 'D3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Silent Night, en versión solo, en Do mayor. Hoy: los acordes con bajo distinto, como G/B.')
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

    y = exercise_heading(c, y, 2, 'Los acordes con bajo distinto: leer las barras', 2,
                          'Lo que trabajamos hoy. "G/B" significa: acorde de Sol, pero con el Si en el bajo, no el Sol. La letra después de la barra manda en el bajo.')
    y -= 9
    ev2a = [{'pitches': SOL, 'dur': 'h.', 'label': 'Sol'}]
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Sol en posición normal: el bajo es Sol', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': SOLdB, 'dur': 'h.', 'label': 'G/B'}]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo acorde como "G/B": el bajo ahora es Si', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'G4', 'B4']]
    bass2c = [{'pitches': SOLdB, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre "G/B": el acorde de Sol con el Si en el bajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, en posición normal.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: el bajo distinto no cambia el acorde, solo su nota más grave.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre "G/B"', 2,
                          'La izquierda toca el acorde de Sol con el Si en el bajo; la derecha canta la melodía encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5']]
    bass1 = [{'pitches': SOLdB, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre "G/B", el Sol con el Si en el bajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el bajo distinto no descoloca el acorde', 3,
                          'La izquierda sostiene el acorde de Sol en posición normal; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'G4', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre el acorde de Sol, en posición normal', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'D5', 'G5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Silent Night casi entera', 3,
                          'Con la partitura al lado: fíjate en cada barra ("/") y coloca la nota correcta en el bajo.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['D4', 'G4', 'B4']])
    bass5 = [{'pitches': DO, 'dur': 'h.'}, {'pitches': SOLdB, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Silent Night casi completa · con los acordes con bajo distinto', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
