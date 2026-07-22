# -*- coding: utf-8 -*-
"""Taller de practica - Piano Man (Merce, cancion 15, Billy Joel,
   Do mayor, 3/4, tempo rapido). Nivel basico pero solido: el vals
   veloz -- tres tiempos ligeros, sin pesadez, aunque el tempo sea
   rapido."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · PIANO MAN'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Piano Man, de Billy Joel, en Do mayor. Hoy: el vals veloz, ligero en sus tres tiempos.')
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

    y = exercise_heading(c, y, 2, 'El vals veloz: tres tiempos ligeros', 2,
                          'Lo que trabajamos hoy. Aunque el tempo es rápido, los tres tiempos del compás deben sonar ligeros, sin acentuar de más el primero como si fuera pesado.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'D4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) Los tres tiempos, ligeros, sin pesadez en el primero', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'rest': True, 'dur': 'q'},
            {'pitch': 'D4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    y = system_block(c, x0, w0, y, gap, 'b) Una nota y dos tiempos de silencio: sin perder el pulso', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Los tres tiempos ligeros sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: mantén los tres tiempos ligeros, aunque el tempo sea rápido.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el vals ligero sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha marca los tres tiempos con ligereza.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'E4', 'D4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Los tres tiempos sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la ligereza no descoloca el acorde', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha mantiene la ligereza sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F4', 'E4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Los tres tiempos sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Piano Man casi entera', 3,
                          'Con la partitura al lado: mantén el vals ligero, aunque el tempo sea rápido.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4']] +
             [{'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'rest': True, 'dur': 'q'}])
    bass5 = [{'pitches': DO, 'dur': 'h.'}, {'pitches': DO, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Piano Man casi completa · con el vals veloz y ligero', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
