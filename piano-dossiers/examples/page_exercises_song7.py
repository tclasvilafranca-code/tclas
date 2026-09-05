# -*- coding: utf-8 -*-
"""Taller de practica - Chopsticks (Cancion 7 de 20, Nivel 1, Do mayor, compas 3/4)
   Pieza especial: un dedo de cada mano. Tema: que las dos manos toquen exactamente a la vez."""
from page_layout_common import *

SONG_KICKER = 'NIVEL 1 · EMPIEZO · CHOPSTICKS'
TS = (3, 4)


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Esta pieza es distinta: se toca con un solo dedo de cada mano. El reto es la sincronía perfecta.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    # ---------- EJERCICIO 1: dos notas, un dedo (3 systems) ----------
    y = exercise_heading(c, y, 1, 'Dos notas con un solo dedo', 1,
                          'Usa solo el dedo 2 (índice). Golpea las dos teclas como si fueran palillos chinos.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['D4', 'E4'] * 6]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Mi, con el dedo 2, marcando el vals (3/4)', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['D4', 'D4', 'E4', 'D4', 'D4', 'E4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Re-Re-Mi, el patrón exacto del "chopsticks"', ev1b, clef='treble', time_sig=TS)

    ev1c = [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'c) Subiendo y bajando, siempre con el dedo 2', ev1c, clef='treble', time_sig=TS)
    y -= 6

    # ---------- EJERCICIO 2: sincronía exacta de las manos (dedicado) ----------
    y = exercise_heading(c, y, 2, 'Las dos manos exactamente a la vez', 2,
                          'La dificultad exacta de esta canción (compases 1-4). Cuenta 1-2-3 en voz alta y baja los dos dedos justo en el "1".')
    y -= 12
    treb2a = [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['D4', 'D4', 'E4', 'D4', 'D4', 'E4'] * 2]
    bass2a = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
              ([(['G2'], 'Sol'), (['C3'], 'Do'), (['C3'], None)] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb2a, bass2a, 'a) Las dos manos, patrón completo de la melodía', grand_gap_mult=7.3)

    ev2c = [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['D4', 'D4', 'D4', 'C4', 'C4', 'C4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Practica sola la mano derecha, contando 1-2-3', ev2c, clef='treble', time_sig=TS)
    y -= 6

    # ---------- EJERCICIO 3: la mano izquierda, un dedo también ----------
    y = exercise_heading(c, y, 3, 'La izquierda, también con un dedo', 2,
                          'Sol grave, marcando el "1" del vals: la base sobre la que baila la melodía.')
    y -= 12
    evb2 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
            [(['G2'], 'Sol'), (['C3'], 'Do'), (['C3'], None)] * 4]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Do, el bajo del vals', evb2, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora las dos manos juntas, con la sonrisa puesta: este vals divertido se repite una y otra vez.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    # ---------- EJERCICIO 4: manos juntas ----------
    y = exercise_heading(c, y, 4, 'Manos juntas · el vals completo', 2,
                          'Un dedo en cada mano, cayendo exactamente a la vez en cada "1" del compás.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['D4', 'D4', 'E4', 'D4', 'D4', 'E4'] * 2]
    bass1 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['G2'], 'Sol'), (['C3'], 'Do'), (['C3'], None)] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase completa, a tempo de vals (♩≈120)', grand_gap_mult=7.3)

    treb2 = [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['D4', 'D4', 'C4', 'D4', 'D4', 'C4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: bajando un escalón', treb2, clef='treble', time_sig=TS)
    y -= 4

    # ---------- EJERCICIO 5: independencia ritmica ----------
    y = exercise_heading(c, y, 5, 'Independencia rítmica · el vals firme', 3,
                          'La derecha marca el patrón; la izquierda no falla ni un solo "1" del compás.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['E4', 'E4', 'D4', 'E4', 'E4', 'D4'] * 2]
    bass3 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['G2'], 'Sol'), (['C3'], 'Do'), (['C3'], None)] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda no falla ni un "1"', grand_gap_mult=7.3)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['D4', 'D4', 'E4', 'E4', 'D4', 'D4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: el patrón en corcheas, más rápido', treb4, clef='treble', time_sig=TS)
    y -= 4

    # ---------- EJERCICIO 6: reto final ----------
    y = exercise_heading(c, y, 6, 'Reto final · Chopsticks completo', 3,
                          'Con la partitura al lado: sincronía exacta, un dedo en cada mano, sin perder la risa.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['D4', 'D4', 'E4', 'D4', 'D4', 'E4']]
    treb5 += [{'pitch': p, 'dur': 'q', 'number': 2} for p in ['F4', 'F4', 'G4', 'F4', 'F4', 'G4']]
    bass5 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['G2'], 'Sol'), (['C3'], 'Do'), (['C3'], None)] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza completa · ♩≈120, vals divertido', grand_gap_mult=7.3)

    exercises_footer(c, 4)
    c.showPage()
