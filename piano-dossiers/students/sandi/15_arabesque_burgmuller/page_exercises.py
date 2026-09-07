# -*- coding: utf-8 -*-
"""Taller de practica - Arabesque (Sandi, cancion 15, J.F.F.
   Burgmuller Op.100, arr. four hands by MB, Do mayor -- armadura
   sin alteraciones confirmada por render directo, 2/4, Allegro
   scherzando, mismo archivo que Dilan y Eva, a 4 manos). Nivel
   avanzado: el staccato veloz -- dedos ligeros a tempo real."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · ARABESQUE (BURGMÜLLER, A 4 MANOS)'
TS = (2, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Arabesque, de Burgmüller, a 4 manos, en Do mayor. Hoy: el staccato veloz.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). El Piano 1 se mueve muy rápido en esta posición.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El staccato veloz: dedos ligeros a tempo real', 3,
                          'La dificultad de hoy. Las notas rápidas del Piano 1 deben sonar staccato con precisión, no legato ni arrastradas: el dedo toca y se retira al instante, incluso a la velocidad del Allegro scherzando.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e'} for p in ['E4', 'F4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) Staccato veloz, subiendo: cada nota suelta al instante', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e'} for p in ['A4', 'G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Bajando, con la misma ligereza exacta', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e'} for p in ['E4', 'F4', 'G4', 'A4']]
    bass2c = [{'pitches': DO, 'dur': 'q'}, {'pitches': DO, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El staccato veloz sobre el acompañamiento repetido del Piano 2', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes principales de esta tonalidad.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el staccato veloz del Piano 1 debe destacar sobre los acordes repetidos del Piano 2.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el staccato veloz sobre el acorde de Fa', 3,
                          'La izquierda repite el acorde de Fa, staccato también; la derecha corre ligera, sin arrastrar ninguna nota.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e'} for p in ['F4', 'G4', 'A4', 'C5']]
    bass1 = [{'pitches': FA, 'dur': 'q'}, {'pitches': FA, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El staccato veloz sobre el acompañamiento de Fa', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e'} for p in ['F4', 'G4', 'A4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: comprueba que cada nota se suelta al instante', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acompañamiento de Sol no ralentiza el staccato', 3,
                          'La izquierda repite el acorde de Sol, staccato; la derecha mantiene su velocidad sin dejarse arrastrar por el acompañamiento.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e'} for p in ['G4', 'A4', 'B4', 'D5']]
    bass3 = [{'pitches': SOL, 'dur': 'q'}, {'pitches': SOL, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El staccato veloz sobre el acompañamiento de Sol', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e'} for p in ['D5', 'B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando con el mismo staccato', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Arabesque casi entera', 3,
                          'Con la partitura al lado: mantén el staccato ligero y preciso, incluso al tempo real del Allegro scherzando.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e'} for p in ['E4', 'F4', 'G4', 'A4']] +
             [{'pitch': p, 'dur': 'e'} for p in ['F4', 'G4', 'A4', 'C5']])
    bass5 = [{'pitches': DO, 'dur': 'q'}, {'pitches': DO, 'dur': 'q'}, {'pitches': FA, 'dur': 'q'}, {'pitches': FA, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Arabesque casi completa · staccato veloz, sin arrastrar ninguna nota', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
