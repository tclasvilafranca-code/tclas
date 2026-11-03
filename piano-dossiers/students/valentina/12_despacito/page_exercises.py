# -*- coding: utf-8 -*-
"""Taller de practica - Despacito (Valentina, cancion 12, La menor,
   4/4, mismo archivo que Dilan). Nivel medio, un poco mas exigente:
   el ostinato en octavas -- el mismo dibujo 3+3+2, pero con mas peso
   y alcance en la mano izquierda."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · DESPACITO (LUIS FONSI & DADDY YANKEE)'
TS = (4, 4)

AM = ['C3', 'E3', 'A3']
DM = ['D2', 'F2', 'A2']
EM = ['E2', 'G2', 'B2']
GROUPS_332 = [0, 0, 0, 1, 1, 1, 2, 2]


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un reggaetón en La menor. Hoy: el ostinato en octavas, el mismo dibujo con más peso.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento rítmico: siente el 3+3+2 sin tocar melodía', 1,
                          'Interioriza el dibujo del ostinato: aplaude solo el primer golpe de cada grupo, contando "1-2-3, 1-2-3, 1-2" en voz alta.')
    y -= 12
    ev1a = ([{'pitch': 'A4', 'dur': 'e'}, {'rest': True, 'dur': 'e'}, {'rest': True, 'dur': 'e'},
             {'pitch': 'A4', 'dur': 'e'}, {'rest': True, 'dur': 'e'}, {'rest': True, 'dur': 'e'},
             {'pitch': 'A4', 'dur': 'e'}, {'rest': True, 'dur': 'e'}] * 2)
    y = system_block(c, x0, w0, y, gap, 'a) Aplaude solo el inicio de cada grupo: 3+3+2', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': 'A4', 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    y = system_block(c, x0, w0, y, gap, 'b) Ahora las ocho corcheas, acentuando el inicio de cada grupo', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El ostinato en octavas: el mismo dibujo, con más peso', 2,
                          'Lo de hoy. En vez de una sola nota, la izquierda toca la octava entera en cada golpe del 3+3+2: más alcance, más peso, mismo dibujo rítmico.')
    y -= 12
    ev2a = [{'pitch': 'A2', 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    y = system_block(c, x0, w0, y, gap, 'a) Primero, una sola nota: para recordar el dibujo', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': ['A2', 'A3'], 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    y = system_block(c, x0, w0, y, gap, 'b) Ahora la octava entera, en cada golpe', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': 'E4', 'dur': 'e', 'beam': g} for g in GROUPS_332]
    bass2c = [{'pitches': ['A2', 'A3'], 'dur': 'e', 'beam': g} for g in GROUPS_332]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos: melodía arriba, octavas abajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en La menor', 2,
                          'Lam–Rem–Mim: los acordes naturales de la tonalidad.')
    y -= 11
    pattern_a = [(AM, 'Lam'), (DM, 'Rem'), (EM, 'Mim'), (AM, 'Lam')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mim-Lam, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el ostinato en octavas abajo, la melodía tranquila arriba.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía entra sobre el ostinato en octavas', 2,
                          'La izquierda repite el dibujo 3+3+2 en octavas; la derecha canta la melodía por encima.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 5), ('D4', 4), ('C4', 3), ('B3', 2), ('C4', 3), ('D4', 4), ('E4', 5), ('D4', 4)]]
    bass4 = [{'pitches': ['A2', 'A3'], 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La melodía sobre el ostinato en octavas', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · las octavas no se contagian de la melodía', 3,
                          'La izquierda repite su dibujo en octavas sin distraerse; la derecha canta libre encima.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'B3']] * 2
    bass5 = [{'pitches': ['D2', 'D3'], 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Melodía en negras sobre el ostinato en octavas de Rem', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Despacito casi entera, con las octavas', 3,
                          'Con la partitura al lado: deja que la izquierda repita su dibujo en octavas sin cansarse ni distraerse.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 5), ('D4', 4), ('C4', 3), ('B3', 2), ('C4', 3), ('D4', 4), ('E4', 5), ('D4', 4)]]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'B3']]
    bass6 = [{'pitches': ['A2', 'A3'], 'dur': 'e', 'beam': g} for g in GROUPS_332]
    bass6 += [{'pitches': ['A2', 'A3'], 'dur': 'e', 'beam': g} for g in GROUPS_332]
    bass6 += [{'pitches': ['A2', 'A3'], 'dur': 'e', 'beam': g} for g in GROUPS_332]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · ♩≈76, octavas firmes', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
