# -*- coding: utf-8 -*-
"""Taller de practica - Polly Put the Kettle On (Cancion 14 de 20, Nivel 2, FA mayor)
   Tema: tocar el Sib (tecla negra) con el dedo 4, sin fallar."""
from page_layout_common import *

SONG_KICKER = 'NIVEL 2 · AVANZO · POLLY PUT THE KETTLE ON'


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Primera vez en FA mayor: aparece el Sib (tecla negra). El reto es meter el dedo 4 sin fallar.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en FA', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca la tecla negra.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sintiendo la tecla negra', ev1a, clef='treble')

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('C5', 5), ('A4', 3), ('F4', 1), ('A4', 3), ('C5', 5), ('A4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble')

    ev1c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('F4', 1), ('G4', 2), ('G4', 2), ('A4', 3), ('A4', 3), ('Bb4', 4), ('Bb4', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'c) Repetida, sintiendo cada dedo', ev1c, clef='treble')
    y -= 6

    y = exercise_heading(c, y, 2, 'El Sib: Fa-Sib-Fa, sin fallar', 2,
                          'La dificultad exacta de esta canción (compases 1-4). Toca solo Fa-Sib-Fa varias veces, buscando la negra sin mirar.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in [('F4', 1), ('Bb4', 4), ('F4', 1)] * 5]
    ev2a.append({'pitch': 'F4', 'dur': 'q', 'number': 1})
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Fa, dieciséis veces seguidas', ev2a, clef='treble')

    ev2b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('A4', 3), ('G4', 2), ('F4', 1), ('Bb4', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Con pasos intermedios, para sentir la distancia', ev2b, clef='treble')

    ev2c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('F4', 1), ('Bb4', 4), ('Bb4', 4)] * 4]
    y = system_block(c, x0, w0, y, gap, 'c) Como en la canción, dos veces cada nota', ev2c, clef='treble')
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do–Fa: los tres acordes de esta tonalidad. El acorde de Sib usa la tecla negra.')
    y -= 12
    pattern_a = [(['F3', 'A3', 'C4'], 'Fa')] * 4 + [(['Bb2', 'D3', 'F3'], 'Sib')] * 4 + \
                [(['C3', 'E3', 'G3'], 'Do')] * 4 + [(['F2', 'A2', 'C3'], 'Fa')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l if i % 4 == 0 else None} for i, (p, l) in enumerate(pattern_a)]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, en bloque', eva, clef='bass')

    pattern_b = [(['F2'], 'Fa'), (['A2', 'C3'], None), (['Bb2'], 'Sib'), (['D3', 'F3'], None)] * 4
    evb = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_b]
    y = system_block(c, x0, w0, y, gap, 'b) Bajo-y-acorde, Fa y Sib alternando', evb, clef='bass')

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos en Fa mayor: alegre, con la hora del té en Inglaterra.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el Sib con confianza', 2,
                          'La izquierda marca el acorde; la derecha toca el Sib sin dudar, con el dedo 4.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in [('F4', 1), ('Bb4', 4), ('F4', 1)] * 2]
    treb1 += [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('F4', 1), ('F4', 1)]]
    bass1 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['F2', 'A2', 'C3'], 'Fa')] * 6 + [(['Bb2', 'D3', 'F3'], 'Sib')] * 5 + [(['F2', 'A2', 'C3'], 'Fa')] * 5)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Estrofa A, con el Sib firme')

    treb2 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2), ('F4', 1), ('A4', 3), ('C5', 5), ('F4', 1)] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía de la estrofa B', treb2, clef='treble')
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia rítmica · el Sib firme', 3,
                          'La derecha se mueve, con el Sib incluido; la izquierda sostiene el acorde sin moverse.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('F4', 1), ('Bb4', 4), ('A4', 3), ('G4', 2), ('F4', 1), ('Bb4', 4), ('A4', 3), ('G4', 2)] * 2]
    bass3 = [{'pitches': ['F2', 'A2', 'C3'], 'dur': 'q', 'label': 'Fa' if i == 0 else None} for i in range(16)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda firme, sin moverse')

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['F4', 'F4', 'Bb4', 'Bb4', 'A4', 'A4', 'G4', 'G4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: el Sib en corcheas', treb4, clef='treble')
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Polly entera', 3,
                          'Con la partitura al lado: encuentra el Sib con seguridad, sin mirar el teclado.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in [('F4', 1), ('Bb4', 4), ('F4', 1)] * 2]
    treb5 += [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('F4', 1), ('F4', 1)]]
    bass5 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['F2', 'A2', 'C3'], 'Fa')] * 6 + [(['Bb2', 'D3', 'F3'], 'Sib')] * 5 + [(['F2', 'A2', 'C3'], 'Fa')] * 5)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción completa · ♩≈100, alegre')

    exercises_footer(c, 4)
    c.showPage()
