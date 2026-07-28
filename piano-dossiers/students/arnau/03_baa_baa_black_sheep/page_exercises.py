# -*- coding: utf-8 -*-
"""Taller de practica - Baa Baa Black Sheep (Arnau, cancion 3, Do mayor,
   4/4). Nivel iniciacion: la melodia con acordes que cambian debajo,
   Do-Fa-Sol."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · BAA BAA BLACK SHEEP'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción tradicional inglesa muy conocida. Hoy: la melodía cantando, con acordes que cambian debajo.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: notas repetidas, mano quieta', 1,
                          'Repite Do tres veces sin mover la muñeca, después salta a Mi. Sonido parejo, sin acentos raros.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('C4', 1), ('C4', 1), ('E4', 3), ('E4', 3), ('E4', 3), ('G4', 5), ('G4', 5)]]
    y = system_block(c, x0, w0, y, gap, 'a) Notas repetidas y un salto', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El acorde que cambia: Do–Fa–Sol', 2,
                          'Lo importante de esta canción: la izquierda cambia de acorde varias veces sin perder el pulso.')
    y -= 9
    pattern2a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    ev2a = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern2a] * 2
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, cambiando cada negra', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h'} for p in ['C3', 'F2', 'G2', 'C3']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la nota grave del acorde (la que sujeta el pulgar)', ev2b, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 1,
                          'Do–Fa–Sol: exactamente los que usa esta canción.')
    y -= 11
    ev3a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa')]] + \
           [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOL, 'Sol'), (DO, 'Do')]]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, dos por compás', ev3a, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Truco de estudio: di en voz alta "Do, Fa, Sol" mientras cambia la izquierda, antes de tocarlo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · melodía sobre acorde de Do', 2,
                          'La izquierda sostiene el acorde de Do entero; la derecha canta encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'C4', 'D4', 'E4']]
    bass1 = [{'pitches': DO, 'dur': 'h'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) "Baa, baa, black sheep" sobre Do', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F4', 'E4', 'D4']]
    bass2 = [{'pitches': FA, 'dur': 'h'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2, bass2, 'b) "Have you any wool" sobre Fa', grand_gap_mult=7.3, time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde cambia, la melodía no se para', 3,
                          'La izquierda salta de Fa a Sol; la derecha sigue su frase sin frenar.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'G4', 'F4']]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [FA, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) "Yes sir, yes sir" con Fa-Sol debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · la canción casi entera', 2,
                          'Con la partitura al lado: sigue el ciclo Do-Fa-Sol-Do de principio a fin.')
    y -= 7
    treb4 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'C4', 'D4', 'E4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F4', 'E4', 'D4']])
    bass4 = [{'pitches': DO, 'dur': 'h'}] * 2 + [{'pitches': FA, 'dur': 'h'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'Las dos primeras frases juntas', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
