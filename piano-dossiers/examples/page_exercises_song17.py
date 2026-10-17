# -*- coding: utf-8 -*-
"""Taller de practica - La Pantera Rosa (Cancion 17 de 20, Nivel 3, LA menor)
   Tema: notas y silencios -- respetar lo que no suena tambien cuenta."""
from page_layout_common import *

SONG_KICKER = 'NIVEL 3 · YA TOCO · LA PANTERA ROSA'


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Primera vez en LA menor, misteriosa. El reto: respetar los silencios, ¡lo que no suena también cuenta!')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en LA menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Todas teclas blancas, pero suena misteriosa.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('E5', 5), ('D5', 4), ('C5', 3), ('B4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, misterioso', ev1a, clef='treble')

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('E5', 5), ('C5', 3), ('A4', 1), ('C5', 3), ('E5', 5), ('C5', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, desgranado', ev1b, clef='treble')

    ev1c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('A4', 1), ('B4', 2), ('B4', 2), ('C5', 3), ('C5', 3), ('D5', 4), ('D5', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'c) Repetida, sigilosa como el gato', ev1c, clef='treble')
    y -= 6

    y = exercise_heading(c, y, 2, 'Notas y silencios: lo que no suena cuenta', 2,
                          'La dificultad exacta de esta canción (compases 1-4). Cuenta también los silencios, como si fueran notas mudas.')
    y -= 12
    ev2a = [{'pitch': 'A4', 'dur': 'q', 'number': 1}, {'rest': True, 'dur': 'q'},
            {'pitch': 'A4', 'dur': 'q', 'number': 1}, {'rest': True, 'dur': 'q'}] * 4
    y = system_block(c, x0, w0, y, gap, 'a) Nota-silencio-nota-silencio, contando siempre', ev2a, clef='treble')

    ev2b = [{'pitch': 'C5', 'dur': 'q', 'number': 3}, {'pitch': 'C5', 'dur': 'q', 'number': 3},
            {'rest': True, 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q', 'number': 2}] * 4
    y = system_block(c, x0, w0, y, gap, 'b) Dos notas, silencio, una nota: el patrón misterioso', ev2b, clef='treble')

    ev2c = [{'pitch': 'A4', 'dur': 'h', 'number': 1}, {'rest': True, 'dur': 'h'}] * 4
    y = system_block(c, x0, w0, y, gap, 'c) Blanca y silencio de blanca, dejando el aire', ev2c, clef='treble')
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes La menor y Mi', 2,
                          'Los dos acordes de esta tonalidad. Suenan misteriosos porque el acorde de La es menor.')
    y -= 12
    pattern_a = [(['A2', 'C3', 'E3'], 'Lam')] * 4 + [(['E2', 'G2', 'B2'], 'Mim')] * 4 + \
                [(['A2', 'C3', 'E3'], 'Lam')] * 4 + [(['E2', 'G2', 'B2'], 'Mim')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l if i % 4 == 0 else None} for i, (p, l) in enumerate(pattern_a)]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Mim, alternando misterioso', eva, clef='bass')

    pattern_b = [(['A2'], 'Lam'), (['C3', 'E3'], None), (['E2'], 'Mim'), (['G2', 'B2'], None)] * 4
    evb = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_b]
    y = system_block(c, x0, w0, y, gap, 'b) Bajo-y-acorde, con aire de suspense', evb, clef='bass')

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos con sigilo: como el gato de puntillas, sin hacer ruido de más.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el silencio también cuenta', 2,
                          'La izquierda marca el acorde misterioso; la derecha respeta cada silencio con precisión.')
    y -= 11
    treb1 = [{'pitch': 'A4', 'dur': 'q', 'number': 1}, {'rest': True, 'dur': 'q'},
             {'pitch': 'A4', 'dur': 'q', 'number': 1}, {'rest': True, 'dur': 'q'}] * 2
    treb1 += [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('C5', 3), ('C5', 3), ('B4', 2), ('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2), ('A4', 1)]]
    bass1 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['A2', 'C3', 'E3'], 'Lam')] * 8 + [(['E2', 'G2', 'B2'], 'Mim')] * 4 + [(['A2', 'C3', 'E3'], 'Lam')] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El tema completo, con sus silencios')

    treb2 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E5', 5), ('D5', 4), ('C5', 3), ('B4', 2), ('A4', 1), ('B4', 2), ('C5', 3), ('A4', 1)] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin los silencios (para compararla)', treb2, clef='treble')
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia rítmica · el gato sigiloso', 3,
                          'La derecha marca el ritmo misterioso, con silencios; la izquierda sostiene el acorde sin moverse.')
    y -= 11
    treb3 = [{'pitch': 'A4', 'dur': 'q', 'number': 1}, {'rest': True, 'dur': 'q'},
             {'pitch': 'C5', 'dur': 'q', 'number': 3}, {'rest': True, 'dur': 'q'}] * 4
    bass3 = [{'pitches': ['A2', 'C3', 'E3'], 'dur': 'q', 'label': 'Lam' if i == 0 else None} for i in range(16)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda firme, ignorando los silencios de arriba')

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['A4', 'C5', 'B4', 'D5', 'C5', 'E5', 'D5', 'C5'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía entera en corcheas, sin silencios', treb4, clef='treble')
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · La Pantera Rosa entera', 3,
                          'Con la partitura al lado: respeta cada silencio con la misma precisión que cada nota.')
    y -= 11
    treb5 = [{'pitch': 'A4', 'dur': 'q', 'number': 1}, {'rest': True, 'dur': 'q'},
             {'pitch': 'A4', 'dur': 'q', 'number': 1}, {'rest': True, 'dur': 'q'}] * 2
    treb5 += [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('C5', 3), ('C5', 3), ('B4', 2), ('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2), ('A4', 1)]]
    bass5 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(['A2', 'C3', 'E3'], 'Lam')] * 8 + [(['E2', 'G2', 'B2'], 'Mim')] * 4 + [(['A2', 'C3', 'E3'], 'Lam')] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El tema completo · ♩≈100, misterioso')

    exercises_footer(c, 4)
    c.showPage()
