# -*- coding: utf-8 -*-
"""Taller de practica - Aloha Oe (Arnau, cancion 13, Do mayor, compas
   partido). Nivel iniciacion con toque extra: el compas partido se
   cuenta a 2, no a 4."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · ALOHA OE'
TS = (2, 2)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción hawaiana muy bonita, en Do mayor. Hoy: el compás partido, que se cuenta a 2.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: dos pulsos grandes por compás', 1,
                          'En vez de contar 1-2-3-4, cuenta solo "1, 2" — cada pulso dura el doble.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Dos pulsos grandes por compás', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El compás partido: se cuenta a 2, no a 4', 2,
                          'Lo importante hoy: sentir solo dos pulsos fuertes por compás, aunque haya varias notas dentro de cada uno.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) Cuatro notas por pulso, pero solo 2 pulsos', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'G4', 'A4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo camino, con notas largas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4']]
    bass2c = [{'pitches': DO, 'dur': 'h'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase sobre el acorde de Do, dos pulsos', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por pulso', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Truco de estudio: mueve la mano (o la cabeza) marcando solo 2 tiempos grandes por compás.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase sobre el acorde de Fa', 2,
                          'La izquierda marca los dos pulsos grandes; la derecha canta su frase encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'E4']]
    bass1 = [{'pitches': FA, 'dur': 'h'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase sobre Fa, dos pulsos grandes', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'h'} for p in ['F4', 'A4', 'Bb4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, con notas largas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no cuenta a 4', 3,
                          'La izquierda marca solo 2 pulsos; la derecha tiene más notas, pero el pulso grande no cambia.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'F4']]
    bass3 = [{'pitches': SOL, 'dur': 'h'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase sobre Sol, dos pulsos grandes', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'B4', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación, con notas largas', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Aloha Oe casi entera', 3,
                          'Con la partitura al lado: cuenta a 2, no a 4, y deja que la melodía fluya.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'E4']])
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [DO, DO, DO, DO, FA, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · contando a 2', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
