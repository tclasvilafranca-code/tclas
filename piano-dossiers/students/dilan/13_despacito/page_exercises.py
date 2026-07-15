# -*- coding: utf-8 -*-
"""Taller de practica - Despacito (Dilan, cancion 13, La menor, 4/4).
   Estructura DISTINTA otra vez: el reto no es la melodia, es el OSTINATO
   sincopado de la izquierda (agrupado 3+3+2 corcheas, el patron tipico del
   reggaeton) -- una mano que repite un dibujo ritmico fijo mientras la
   otra canta encima."""
from page_layout_common import *

SONG_KICKER = 'DILAN · ABRIL · DESPACITO (LUIS FONSI & DADDY YANKEE)'
TS = (4, 4)

AM = ['C3', 'E3', 'A3']
DM = ['D2', 'F2', 'A2']
EM = ['E2', 'G2', 'B2']
GROUPS_332 = [0, 0, 0, 1, 1, 1, 2, 2]


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un reggaetón en La menor. El reto no es la melodía: es el dibujo rítmico de la izquierda.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Misma armadura que Do mayor, centro tonal en La.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 5), ('D4', 4), ('C4', 3), ('B3', 2), ('C4', 3), ('D4', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Baja y sube desde el Mi', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('E4', 5), ('C4', 3), ('E4', 5)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El ostinato con síncopa: 3+3+2', 2,
                          'Ocho corcheas por compás, pero NO agrupadas de dos en dos: se agrupan 3+3+2. Es el patrón típico del reggaetón — cuenta "1-2-3, 1-2-3, 1-2" en vez de "1-2, 1-2, 1-2, 1-2".')
    y -= 12
    ev2a = [{'pitch': 'A2', 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    y = system_block(c, x0, w0, y, gap, 'a) La izquierda: una sola nota, con el dibujo 3+3+2', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': 'E4', 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    y = system_block(c, x0, w0, y, gap, 'b) El mismo dibujo, en la derecha', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': 'E4', 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    bass2c = [{'pitch': 'A2', 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos con el mismo dibujo 3+3+2', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Manos juntas, el ostinato con melodía encima, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · melodía sobre acordes', 2,
                          'La izquierda sostiene los acordes; la derecha canta la melodía por encima.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 5), ('D4', 4), ('C4', 3), ('B3', 2), ('C4', 3), ('D4', 4), ('E4', 5), ('D4', 4)]]
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(AM, 'Lam'), (DM, 'Rem'), (EM, 'Mim'), (AM, 'Lam')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La melodía sobre los acordes', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El ostinato con la melodía real encima', 3,
                          'Ahora la izquierda mantiene su dibujo 3+3+2 mientras la derecha canta de verdad. No dejes que la izquierda se contagie del ritmo de la derecha.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'B3']] * 2
    bass5 = [{'pitch': 'A2', 'dur': 'e', 'beam': g} for g in GROUPS_332] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Melodía en negras sobre el ostinato en corcheas', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Despacito casi entera', 3,
                          'Con la partitura al lado: deja que la izquierda repita su dibujo sin distraerse con la derecha.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 5), ('D4', 4), ('C4', 3), ('B3', 2), ('C4', 3), ('D4', 4), ('E4', 5), ('D4', 4)]]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'B3']]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(AM, 'Lam'), (DM, 'Rem'), (EM, 'Mim'), (AM, 'Lam')]]
    bass6 += [{'pitch': 'A2', 'dur': 'e', 'beam': g} for g in GROUPS_332]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · ♩≈76', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
