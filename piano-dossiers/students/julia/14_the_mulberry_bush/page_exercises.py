# -*- coding: utf-8 -*-
"""Taller de practica - The Mulberry Bush (Julia, cancion 14, Do
   mayor, 6/8, a 4 manos). Nivel inicial: el balanceo de seis
   corcheas -- como un columpio que se mece de un lado a otro."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · THE MULBERRY BUSH (A 4 MANOS)'
TS = (6, 8)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de corro en Do mayor, a 4 manos. Hoy nos balanceamos como en un columpio.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). ¡Busca tu nota casa, el Do!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
            enumerate(['C4', 'D4', 'E4', 'D4', 'C4', 'D4', 'E4', 'D4', 'C4', 'D4', 'E4', 'D4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición, en corcheas', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, en negras con puntillo', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El balanceo de seis corcheas, como un columpio', 2,
                          'Lo que vamos a practicar hoy. El compás de 6/8 se balancea en dos grandes impulsos, como un columpio que va y viene.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) Los dos impulsos grandes del columpio', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
            enumerate(['C4', 'D4', 'E4', 'E4', 'D4', 'C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4'])]
    y = system_block(c, x0, w0, y, gap, 'b) La misma duración, en seis corcheas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'E4', 'D4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El columpio sobre el acorde de Do, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol–Do: los acordes de esta tonalidad, uno por compás entero.')
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: el columpio se balancea mientras el acorde se queda quieto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el columpio sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha se balancea con sus dos impulsos.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'G4', 'A4', 'G4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El columpio sobre Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
             enumerate(['F4', 'G4', 'A4', 'A4', 'G4', 'F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4'])]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, en seis corcheas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se balancea', 3,
                          'La izquierda queda quieta con su acorde; la derecha se balancea, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q.'} for p in ['G4', 'A4', 'B4', 'A4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El columpio sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
             enumerate(['G4', 'A4', 'B4', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4'])]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en seis corcheas', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · The Mulberry Bush casi entera', 3,
                          'Con la partitura al lado: ¡balancéate como en un columpio, sin contar las seis corcheas por separado!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'E4', 'D4']] +
             [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'G4', 'A4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · balanceándose como un columpio', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
