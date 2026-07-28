# -*- coding: utf-8 -*-
"""Taller de practica - Polly Put the Kettle On (Arnau, cancion 11,
   Fa mayor, 4/4). Nivel iniciacion: notas ligadas, sin cortar entre
   una y otra -- reforzando la armadura de Fa mayor."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · POLLY PUT THE KETTLE ON'
TS = (4, 4)
KEY = 'Fa mayor'

FA = ['F2', 'A2', 'C3']
SIb = ['Bb1', 'D2', 'F2']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Otra canción en Fa mayor, tranquila. Hoy: notas ligadas, sin cortar entre una y otra.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: legato con muñeca suave', 1,
                          'Une cada nota con la siguiente sin levantar el dedo antes de tiempo — como una cinta continua.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) La posición de Fa mayor, ligada', ev1a, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 2, 'Notas ligadas: sin cortar entre una y otra', 2,
                          'Lo importante hoy: que no se oiga ningún hueco entre las notas, como una frase hablada sin pausas.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['C5', 'Bb4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) Notas largas y unidas, bajando con calma', ev2a, clef='treble', time_sig=TS, key_sig=KEY)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'C5', 'Bb4', 'Bb4', 'A4', 'A4', 'G4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, marcando el ritmo: para comparar', ev2b, clef='treble', time_sig=TS, key_sig=KEY)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['C5', 'Bb4', 'A4', 'G4']]
    bass2c = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las notas ligadas sobre el acorde de Fa, quieto', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SIb, 'Sib'), (DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS, key_sig=KEY)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Truco de estudio: canta la frase con "aaaa" continuo, sin cortar, y luego imita eso al piano.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · legato sobre el acorde de Sib', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha liga sus notas encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['D5', 'C5', 'Bb4', 'A4']]
    bass1 = [{'pitches': SIb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Legato sobre Sib, quieto', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'C5', 'Bb4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, marcando el ritmo: para comparar', treb2, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se mueve con el legato', 3,
                          'La izquierda queda quieta con su acorde; la derecha liga sus notas, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h'} for p in ['E5', 'D5', 'C5', 'Bb4']]
    bass3 = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Legato sobre Do; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación, un poco más arriba', treb4, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Polly Put the Kettle On casi entera', 3,
                          'Con la partitura al lado: deja que las notas se unan, sin cortes.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['C5', 'Bb4', 'A4', 'G4']] +
             [{'pitch': p, 'dur': 'h'} for p in ['D5', 'C5', 'Bb4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [FA, FA, SIb, SIb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · notas ligadas', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    exercises_footer(c, 4)
    c.showPage()
