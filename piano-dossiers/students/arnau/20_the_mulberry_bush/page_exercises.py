# -*- coding: utf-8 -*-
"""Taller de practica - The Mulberry Bush (Arnau, cancion 20, Do
   mayor, 6/8, a 4 manos). Nivel iniciacion: el balanceo de seis
   corcheas, como un corro -- gran final del cuaderno, a duo con el
   profesor."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · THE MULBERRY BUSH (A 4 MANOS)'
TS = (6, 8)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de corro en Do mayor, a 4 manos: el gran final de tu cuaderno, ¡a dúo con el profesor!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: dos grupos de tres corcheas', 1,
                          'Cuenta "uno-dos-tres, uno-dos-tres" con calma, como si giraras en corro.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['C4', 'D4', 'E4', 'D4', 'C4', 'D4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Seis corcheas, en dos grupos de tres', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El balanceo de seis corcheas, como un corro', 2,
                          'La melodía gira suave en grupos de tres, como niños dando vueltas alrededor de la morera.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['E4', 'D4', 'C4', 'D4', 'E4', 'D4'])]
    y = system_block(c, x0, w0, y, gap, 'a) El corro, girando de un lado a otro', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q.'} for p in ['E4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo compás, sin corcheas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
              enumerate(['C4', 'D4', 'E4', 'D4', 'C4', 'D4'])]
    bass2c = [{'pitches': DO, 'dur': 'q.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El corro sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, en compás de 6/8.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa')] + [(SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, dos acordes por compás', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Truco de estudio: primero tu parte sola, muy despacio; luego a dúo con el profesor.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el corro sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha gira encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
             enumerate(['F4', 'G4', 'A4', 'G4', 'F4', 'G4'])]
    bass1 = [{'pitches': FA, 'dur': 'q.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El corro sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo compás, sin corcheas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no gira con la melodía', 3,
                          'La izquierda queda quieta con su acorde; la derecha gira, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
             enumerate(['G4', 'A4', 'G4', 'F4', 'G4', 'A4'])]
    bass3 = [{'pitches': SOL, 'dur': 'q.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El corro sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q.'} for p in ['G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación, sin corcheas', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · The Mulberry Bush casi entera', 3,
                          'Con la partitura al lado: gira con el corro, ¡y disfruta este cierre de cuaderno a dúo!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
              enumerate(['C4', 'D4', 'E4', 'D4', 'C4', 'D4'])] +
             [{'pitch': p, 'dur': 'e', 'beam': (i // 3) + 2} for i, p in
              enumerate(['F4', 'G4', 'A4', 'G4', 'F4', 'G4'])])
    bass5 = [{'pitches': p, 'dur': 'q.'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · girando en corro, a dúo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
