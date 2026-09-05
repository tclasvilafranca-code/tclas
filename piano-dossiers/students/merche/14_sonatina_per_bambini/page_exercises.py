# -*- coding: utf-8 -*-
"""Taller de practica - Sonatina per bambini (Merce, cancion 14,
   M. Bazzoni, La menor -- armadura sin alteraciones, confirmada
   por el titulo "In la minore" y el sensible Sol# en la parte del
   maestro, 4/4, a 4 manos). Nivel basico pero solido: el signo
   8va -- se toca una octava mas alta de lo escrito."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · SONATINA PER BAMBINI (A 4 MANOS)'
TS = (4, 4)

LAm = ['A2', 'C3', 'E3']
REm = ['D2', 'F2', 'A2']
MI = ['E2', 'G#2', 'B2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una sonatina para niños de Bazzoni, en La menor, a 4 manos. Hoy: el signo 8va.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Todas teclas blancas: La menor es el relativo de Do mayor.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2), ('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5', 'C5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El signo 8va: una octava más alta de lo escrito', 2,
                          'Lo que trabajamos hoy. La línea de puntos "8va" sobre el pentagrama indica que hay que tocar una octava más alta de lo que está escrito, sin cambiar la digitación.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5', 'C5', 'A4', 'C5', 'E5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'a) Escrito en su octava normal', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['A5', 'C6', 'E6', 'C6', 'A5', 'C6', 'E6', 'C6']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, tocada bajo el signo 8va: una octava más alta', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5', 'C5']]
    bass2c = [{'pitches': LAm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde de La menor, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en La menor', 2,
                          'La menor–Re menor–Mi (con el sensible Sol#): los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(LAm, 'Lam'), (REm, 'Rem'), (MI, 'Mi'), (LAm, 'Lam')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mi-Lam, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el acorde sostenido acompaña la melodía tocada una octava más alta.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía 8va sobre el acorde de Re menor', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta una octava más alta de lo escrito.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'F5', 'A5', 'F5']]
    bass1 = [{'pitches': REm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía 8va sobre Re menor, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'F5', 'A5', 'F5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el sensible Sol# no descoloca el acorde', 3,
                          'La izquierda sostiene el acorde de Mi con su sensible Sol#, quieta; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'G#5', 'B5', 'G#5']]
    bass3 = [{'pitches': MI, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El sensible sobre el acorde de Mi; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G#5', 'B5', 'E6', 'B5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Sonatina per bambini casi entera', 3,
                          'Con la partitura al lado: recuerda tocar la melodía una octava más alta bajo el signo 8va.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['D5', 'F5', 'A5', 'F5']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [LAm, REm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Sonatina per bambini casi completa · con el signo 8va', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
