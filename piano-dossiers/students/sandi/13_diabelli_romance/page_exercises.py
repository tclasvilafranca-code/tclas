# -*- coding: utf-8 -*-
"""Taller de practica - Romance (Sandi, cancion 13, Anton Diabelli,
   Sonata a 4 manos Op.163 No.1 Mvmt.2, Do mayor -- armadura sin
   alteraciones confirmada por render directo, 4/4, Andantino, a 4
   manos). Nivel avanzado: el legato absoluto -- unir cada nota con
   la siguiente, sin cortes."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · ROMANCE (DIABELLI, A 4 MANOS)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Romance, de Anton Diabelli, a 4 manos, en Do mayor. Hoy: el legato absoluto.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). El Primo mantiene esta posición fija durante toda la pieza.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido completo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El legato absoluto: sin cortes entre las notas', 3,
                          'La dificultad de hoy. La partitura pide "sempre legato": cada nota debe ligarse con la siguiente sin el menor hueco de silencio, como si una sola respiración recorriera toda la frase.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'a) Una frase legato: suelta el dedo justo cuando el siguiente ya pisa', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Bajando, con la misma continuidad absoluta', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e'} for p in ['E4', 'F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El acompañamiento en corcheas ligadas, sempre legato, sobre el acorde de Do', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes principales de esta tonalidad.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: el legato debe sonar como una sola línea continua, sin costuras.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el legato sobre el acorde de Fa', 3,
                          'La izquierda sostiene el acorde de Fa; la derecha liga cada nota con la siguiente, sin ninguna interrupción de sonido.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'C5']]
    bass1 = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El legato sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: comprueba que no queda ningún hueco entre notas', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acompañamiento en corcheas también liga sin cortes', 3,
                          'La izquierda toca el acompañamiento en corcheas ligadas, sempre legato; la derecha sostiene su línea sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'D5']]
    bass3 = [{'pitch': p, 'dur': 'e'} for p in ['G3', 'A3', 'B3', 'C4', 'B3', 'A3', 'G3', 'F#3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El legato sobre el acompañamiento de Sol, sempre ligado', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando con el mismo legato', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Romance casi entera', 3,
                          'Con la partitura al lado: mantén la línea legato absoluta del principio al final, sin ninguna costura audible.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'C5']])
    bass5 = [{'pitches': DO, 'dur': 'w'}, {'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Romance casi completa · legato absoluto, sin costuras', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
