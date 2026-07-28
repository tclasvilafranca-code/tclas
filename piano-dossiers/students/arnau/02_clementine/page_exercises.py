# -*- coding: utf-8 -*-
"""Taller de practica - Clementine / Found a Peanut (Arnau, cancion 2,
   Do mayor, 3/4). Nivel iniciacion: melodia solo con la derecha, y un
   estiramiento puntual de la izquierda hacia abajo (bloque D, manos
   pequenas: se avisa de no forzar, solo alcanzar con calma)."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · CLEMENTINE'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Casi toda la melodía va con la mano derecha; la izquierda solo alcanza una nota grave de vez en cuando.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: saltos pequeños en posición de 5 dedos', 1,
                          'Dedos 1-3-5 alternando, sin tensar la muñeca — como si picotearas las teclas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3), ('C4', 1), ('E4', 3)]]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Mi-Sol, ida y vuelta', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El estiramiento de la izquierda hacia abajo', 2,
                          'Ergonomía para manos pequeñas: la izquierda baja UNA vez a buscar una nota grave y vuelve a subir, sin prisa ni fuerza — solo alcanzar.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'D3', 'E3', 'D3', 'C3', 'D3']]
    y = system_block(c, x0, w0, y, gap, 'a) Practica el alcance solo, muy despacio', ev2a, clef='bass', time_sig=TS)

    treb2b = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']]
    bass2b = [{'rest': True, 'dur': 'h'}, {'pitch': 'C3', 'dur': 'q'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb2b, bass2b, 'b) La derecha canta, la izquierda solo alcanza al final de cada compás', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 1,
                          'Do–Fa–Sol, para acompañar cuando la izquierda sí que toca.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Canta la letra mientras tocas: "Oh, my darling, Clementine" — te ayuda a no perder el pulso.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'La frase de "Oh, my darling"', 2,
                          'El salto de corcheas hacia arriba: Sol-La-Sol, ligero, sin golpear.')
    y -= 7
    ev4a = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
            enumerate(['G4', 'A4'] * 6)]
    y = system_block(c, x0, w0, y, gap, 'a) El saltito repetido', ev4a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Manos juntas · solo en el compás del estiramiento', 2,
                          'La derecha sigue su melodía tranquila; la izquierda baja una sola vez, con calma, y sube.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'h.'} for p in ['E4', 'D4', 'C4']]
    bass5 = [{'rest': True, 'dur': 'h'}, {'pitch': 'C3', 'dur': 'q'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) El estiramiento dentro de la frase', grand_gap_mult=7.3, time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · el final de la canción', 2,
                          'Con la partitura al lado: la frase que termina en "Clementine", cantando bajito.')
    y -= 7
    treb6 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'D4', 'C4', 'D4']] + [{'pitch': 'C4', 'dur': 'h.'}]
    bass6 = [{'pitches': DO, 'dur': 'h.'}] * 2 + [{'pitches': SOL, 'dur': 'h.'}]
    # dur beats: treble 6*1 + 3 = 9 (3 bars 3/4); bass 3+3+3=9 -> ok
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'El final casi completo · con acordes sencillos debajo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
