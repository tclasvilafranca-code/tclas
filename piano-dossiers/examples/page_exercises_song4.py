# -*- coding: utf-8 -*-
"""Taller de practica - Do Your Ears Hang Low? (Cancion 4 de 20, Nivel 1, Do mayor)
   Tema: notas repetidas, cambiando de dedo (3-2-1) para que suene agil."""
from page_layout_common import *

SONG_KICKER = 'NIVEL 1 · EMPIEZO · DO YOUR EARS HANG LOW?'


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El reto de esta canción: repetir la misma nota cambiando de dedo, sin que se atasque.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    # ---------- EJERCICIO 1: posicion de 5 dedos (3 systems) ----------
    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do', 1,
                          'Un dedo por tecla, ligero y saltarín, como pide esta canción graciosa.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('D4', 2), ('F4', 4), ('E4', 3), ('G4', 5), ('F4', 4), ('D4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos de tercera, ligero', ev1a, clef='treble')

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 5), ('G4', 5), ('F4', 4), ('F4', 4), ('E4', 3), ('E4', 3), ('D4', 2), ('D4', 2)]]
    ev1b += [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('C4', 1), ('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('C4', 1)]]
    y = system_block(c, x0, w0, y, gap, 'b) Notas dobles bajando desde Sol', ev1b, clef='treble')

    ev1c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3), ('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'c) Saltos alegres en el acorde de Do', ev1c, clef='treble')
    y -= 6

    # ---------- EJERCICIO 2: notas repetidas, cambio de dedo (dedicado, 3 systems) ----------
    y = exercise_heading(c, y, 2, 'Notas repetidas, cambiando de dedo', 2,
                          'La dificultad exacta de esta canción (compases 1-4). Cambia 3-2-1 en cada repetición para que suene ágil.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 3), ('E4', 2), ('E4', 1), ('D4', 2), ('E4', 3), ('E4', 2), ('E4', 1), ('D4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Mi-Mi-Mi con dedos 3-2-1', ev2a, clef='treble')

    ev2b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('C4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('E4', 2), ('E4', 1), ('D4', 2)]]
    ev2b += [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('G4', 5), ('G4', 4), ('G4', 3), ('F4', 4), ('E4', 3), ('E4', 2), ('E4', 1), ('C4', 1)]]
    y = system_block(c, x0, w0, y, gap, 'b) Do y Sol repetidos, distinto dedo cada vez', ev2b, clef='treble')

    ev2c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 2), ('D4', 1), ('E4', 3), ('E4', 2), ('D4', 2), ('D4', 1), ('C4', 1), ('C4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'c) Repetida y ligera, casi susurrando', ev2c, clef='treble')
    y -= 6

    # ---------- EJERCICIO 3: acordes I-IV-V (2 systems, clave de FA) ----------
    y = exercise_heading(c, y, 3, 'Acordes I–IV–V, ligeros y saltarines', 2,
                          'Do–Fa–Sol–Do con un toque juguetón: la mano se levanta un poco entre acorde y acorde.')
    y -= 12
    pattern_a = [(['C3', 'E3', 'G3'], 'Do'), (['C3', 'E3', 'G3'], None), (['F2', 'A2', 'C3'], 'Fa'), (['F2', 'A2', 'C3'], None)] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Do-Fa-Fa, con rebote', eva, clef='bass')

    pattern_b = [(['C3', 'E3', 'G3'], 'Do'), (['G2', 'B2', 'D3'], 'Sol'),
                 (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do')] * 4
    evb = [{'pitches': p, 'dur': 'q', 'label': l if i < 4 else None} for i, (p, l) in enumerate(pattern_b)]
    y = system_block(c, x0, w0, y, gap, 'b) Do-Sol-Fa-Do, girando por los tres acordes', evb, clef='bass')

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos con ganas de reír: ligera, saltarina, un poco tonta.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    # ---------- EJERCICIO 4: manos juntas ----------
    y = exercise_heading(c, y, 4, 'Manos juntas · notas repetidas sin atascos', 2,
                          'La izquierda marca el acorde; la derecha repite su nota cambiando de dedo cada vez.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 3), ('E4', 2), ('E4', 1), ('D4', 2), ('E4', 3), ('E4', 2), ('E4', 1), ('D4', 2)]]
    treb1 += [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('C4', 1), ('C4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('C4', 1)]]
    bass1 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['C3'], 'Do'), (['E3'], None), (['G3'], None), (['E3'], None)] * 2 +
              [(['F2', 'A2', 'C3'], 'Fa')] * 4 + [(['C3', 'E3', 'G3'], 'Do')] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Estrofa A, ligera')

    treb2 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('G4', 5), ('G4', 4), ('G4', 3), ('F4', 4), ('E4', 3), ('E4', 2), ('E4', 1), ('D4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía de la estrofa B', treb2, clef='treble')
    y -= 4

    # ---------- EJERCICIO 5: independencia ritmica ----------
    y = exercise_heading(c, y, 5, 'Independencia rítmica · saltarina', 3,
                          'La derecha repite y salta; la izquierda sostiene el acorde firme, sin moverse.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('C4', 1), ('C4', 2), ('E4', 3), ('E4', 2), ('G4', 5), ('G4', 4), ('E4', 3), ('C4', 1)] * 2]
    bass3 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['C3'], 'Do'), (['E3'], None), (['G3'], None), (['E3'], None)] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Repetida y con saltos, muy ágil')

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['E4', 'E4', 'D4', 'D4', 'C4', 'C4', 'D4', 'D4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la repetición en corcheas', treb4, clef='treble')
    y -= 4

    # ---------- EJERCICIO 6: reto final ----------
    y = exercise_heading(c, y, 6, 'Reto final · la canción entera', 3,
                          'Con la partitura al lado: repite cada nota cambiando de dedo, sin perder la sonrisa.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 3), ('E4', 2), ('E4', 1), ('D4', 2), ('E4', 3), ('E4', 2), ('E4', 1), ('D4', 2)]]
    treb5 += [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('C4', 1), ('C4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('C4', 1)]]
    bass5 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['C3'], 'Do'), (['E3'], None), (['G3'], None), (['E3'], None)] * 2 +
              [(['F2', 'A2', 'C3'], 'Fa')] * 4 + [(['C3', 'E3', 'G3'], 'Do')] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción completa · ♩≈108, gracioso')

    exercises_footer(c, 4)
    c.showPage()
