# -*- coding: utf-8 -*-
"""Taller de practica - Popeye el marinerito (Arnau, cancion 17,
   Sol mayor, 3/4). Reto motivador (nivel basico): consolidando Sol
   mayor, ahora en compas de vals."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · RETO MOTIVADOR · POPEYE EL MARINERITO'
TS = (3, 4)
KEY = 'Sol mayor'

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D2', 'F#2', 'A2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Otra vez Sol mayor, pero ahora en compás de vals. Ya conoces el Fa sostenido de la canción anterior.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: posición de Sol mayor, en 3/4', 1,
                          'La misma posición de la canción anterior, ahora contando de tres en tres.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('D5', 5), ('C5', 4)]]
    y = system_block(c, x0, w0, y, gap, 'a) La posición de Sol mayor, en vals', ev1a, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 2, 'El Fa sostenido, ya sin sorpresas', 2,
                          'Reconoce el Fa sostenido a primera vista: ya sabes que en esta tonalidad siempre es sostenido.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'F#4', 'G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'a) Una frase de vals con Fa sostenido', ev2a, clef='treble', time_sig=TS, key_sig=KEY)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'G4', 'G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase sin el Fa: para escuchar la diferencia', ev2b, clef='treble', time_sig=TS, key_sig=KEY)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'F#4', 'G4', 'A4', 'B4']]
    bass2c = [{'pitches': SOL, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase sobre el acorde de Sol, quieto', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad, en vals.')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Re-Sol, un acorde entero por compás', eva, clef='bass', time_sig=TS, key_sig=KEY)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Truco de estudio: cuenta el vals en voz alta, "uno-dos-tres", mientras la izquierda sostiene el acorde.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el vals sobre el acorde de Do', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta su frase de vals.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'B4', 'C5', 'D5', 'E5']]
    bass1 = [{'pitches': DO, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El vals sobre Do, quieto', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para comparar', treb2, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no baila el vals', 3,
                          'La izquierda queda quieta con su acorde; la derecha baila su vals, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'F#4', 'G4', 'A4', 'B4']]
    bass3 = [{'pitches': RE, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El vals sobre Re; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación, terminando en el Fa sostenido', treb4, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Popeye el marinerito casi entera', 3,
                          'Con la partitura al lado: baila el vals con confianza, ¡ya dominas Sol mayor!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'F#4', 'G4', 'A4', 'B4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'B4', 'C5', 'D5', 'E5']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [SOL, SOL, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · bailando en Sol mayor', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    exercises_footer(c, 4)
    c.showPage()
