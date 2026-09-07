# -*- coding: utf-8 -*-
"""Taller de practica - It's Beginning to Look a Lot Like Christmas
   (Nel, cancion 18, Do mayor, 6/8, a 4 manos). Angulo: contar en
   dos, no en seis -- sentir el pulso grande de 6/8 (dos negras con
   puntillo por compas), distinto del enfoque de "ensamble" usado
   con Dilan y Eva para la misma pieza."""
from page_layout_common import *

SONG_KICKER = 'NEL · MAYO · IT’S BEGINNING TO LOOK A LOT LIKE CHRISTMAS (A 4 MANOS)'
TS = (6, 8)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico a dúo en Do mayor y 6/8. El reto: contar en dos, no en seis.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
            enumerate(['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4', 'D4', 'E4', 'F4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición, en corcheas', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'G4', 'E4', 'G4'] * 1]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, en negras con puntillo', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Contar en dos, no en seis: el pulso grande de 6/8', 2,
                          'La dificultad exacta de esta pieza. El compás de 6/8 no se cuenta en seis corcheas sueltas — se siente en dos pulsos grandes, cada uno de tres corcheas.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'G4', 'E4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) Los dos pulsos grandes, marcados', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
            enumerate(['C4', 'D4', 'E4', 'E4', 'F4', 'G4', 'G4', 'F4', 'E4', 'D4', 'C4', 'D4'])]
    y = system_block(c, x0, w0, y, gap, 'b) La misma duración, en seis corcheas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'G4', 'E4', 'G4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Los dos pulsos sobre el acorde de Do, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V–I en Do mayor', 2,
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: los dos pulsos grandes se sienten con las dos manos a la vez.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · en el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha marca los dos pulsos grandes encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'A4', 'C5', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Los dos pulsos sobre Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
             enumerate(['F4', 'G4', 'A4', 'A4', 'C5', 'A4', 'A4', 'G4', 'F4', 'G4', 'A4', 'G4'])]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, en seis corcheas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia de los pulsos', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha marca sus dos pulsos grandes, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q.'} for p in ['G4', 'B4', 'D5', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Los dos pulsos sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
             enumerate(['G4', 'A4', 'B4', 'B4', 'D5', 'B4', 'B4', 'A4', 'G4', 'A4', 'B4', 'A4'])]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en seis corcheas', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · It’s Beginning to Look a Lot Like Christmas casi entera', 3,
                          'Con la partitura al lado: siente los dos pulsos grandes de cada compás, sin contar las seis corcheas por separado.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q.'} for p in ['C4', 'G4', 'E4', 'G4']] +
             [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'A4', 'C5', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · sintiendo los dos pulsos grandes de 6/8', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
