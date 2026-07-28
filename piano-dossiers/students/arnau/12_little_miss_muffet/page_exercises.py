# -*- coding: utf-8 -*-
"""Taller de practica - Little Miss Muffet (Arnau, cancion 12, Fa
   mayor, 6/8). Nivel iniciacion: el balanceo de seis corcheas en dos
   grupos de tres, como un compas compuesto."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · LITTLE MISS MUFFET'
TS = (6, 8)
KEY = 'Fa mayor'

FA = ['F2', 'A2', 'C3']
SIb = ['Bb1', 'D2', 'F2']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un cuento cantado en Fa mayor, en compás de 6/8: se cuenta en dos grupos de tres.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: dos grupos de tres corcheas', 1,
                          'Cuenta "uno-dos-tres, uno-dos-tres" por compás, marcando un poco más el primer "uno" de cada grupo.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['E4', 'F4', 'G4', 'A4', 'G4', 'F4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Seis corcheas, en dos grupos de tres', ev1a, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 2, 'El balanceo de seis corcheas, como un columpio', 2,
                          'La melodía se balancea en grupos de tres, subiendo y bajando con un vaivén suave.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['G4', 'F4', 'E4', 'D4', 'E4', 'F4'])]
    y = system_block(c, x0, w0, y, gap, 'a) El vaivén, bajando y volviendo a subir', ev2a, clef='treble', time_sig=TS, key_sig=KEY)

    ev2b = [{'pitch': p, 'dur': 'q.'} for p in ['C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo compás, ahora sin corcheas: para comparar', ev2b, clef='treble', time_sig=TS, key_sig=KEY)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
              enumerate(['A4', 'G4', 'F4', 'E4', 'F4', 'G4'])]
    bass2c = [{'pitches': FA, 'dur': 'q.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El vaivén sobre el acorde de Fa, quieto', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad, en compás de 6/8.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SIb, 'Sib')] + [(DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, dos acordes por compás', eva, clef='bass', time_sig=TS, key_sig=KEY)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el vaivén de la derecha sobre el acorde quieto de la izquierda.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el vaivén sobre el acorde de Sib', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha se balancea encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
             enumerate(['G4', 'F4', 'E4', 'D4', 'E4', 'F4'])]
    bass1 = [{'pitches': SIb, 'dur': 'q.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El vaivén sobre Sib, quieto', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb2 = [{'pitch': p, 'dur': 'q.'} for p in ['D5', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo compás, sin corcheas: para comparar', treb2, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se balancea con la melodía', 3,
                          'La izquierda queda quieta con su acorde; la derecha se balancea, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
             enumerate(['A4', 'G4', 'F4', 'E4', 'F4', 'G4'])]
    bass3 = [{'pitches': DO, 'dur': 'q.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El vaivén sube; el acorde de Do no se mueve', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb4 = [{'pitch': p, 'dur': 'q.'} for p in ['E5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación, un poco más arriba', treb4, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Little Miss Muffet casi entera', 3,
                          'Con la partitura al lado: deja que el compás se balancee, como un columpio.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
              enumerate(['E4', 'F4', 'G4', 'A4', 'G4', 'F4'])] +
             [{'pitch': p, 'dur': 'e', 'beam': (i // 3) + 2} for i, p in
              enumerate(['A4', 'G4', 'F4', 'E4', 'F4', 'G4'])])
    bass5 = [{'pitches': p, 'dur': 'q.'} for p in [FA, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · balanceándose en 6/8', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    exercises_footer(c, 4)
    c.showPage()
