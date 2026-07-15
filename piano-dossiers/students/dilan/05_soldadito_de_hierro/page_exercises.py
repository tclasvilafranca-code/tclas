# -*- coding: utf-8 -*-
"""Taller de practica - Soldadito de Hierro (Dilan, cancion 5 de 5, Do mayor, 4/4)
   Tema: grupos de tres notas ligeros y rapidos en la derecha, mientras la
   izquierda descansa en acordes largos y tranquilos."""
from page_layout_common import *

SONG_KICKER = 'DILAN · NOVIEMBRE · SOLDADITO DE HIERRO (NIL MOLINER)'
TS = (4, 4)


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción en Do mayor con la derecha muy viva. El reto: grupos de tres notas ligeros y rápidos.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Baja y sube, con soltura', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('G4', 5), ('E4', 3), ('G4', 5)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, en otro orden', ev1b, clef='treble', time_sig=TS)

    ev1c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 5), ('F4', 4), ('E4', 4), ('E4', 3), ('D4', 3), ('D4', 2), ('C4', 2), ('C4', 1)]]
    y = system_block(c, x0, w0, y, gap, 'c) Repetida, bajando esta vez', ev1c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Grupos de tres, ligeros y rápidos', 2,
                          'La dificultad exacta de esta canción. Practica cada grupo de tres muy despacio, como un giro pequeño de la muñeca, y ve acelerando poco a poco.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'a) Grupos de tres subiendo: Do-Re-Mi', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
            [(['C3', 'E3', 'G3'], 'Do'), (['A2', 'C3', 'E3'], 'Lam'),
             (['F2', 'A2', 'C3'], 'Fa'), (['G2', 'B2', 'D3'], 'Sol')]]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: acordes largos y tranquilos, sin prisa', ev2b, clef='bass', time_sig=TS)

    ev2c = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['E4', 'F4', 'G4'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'c) Grupos de tres, un escalón más arriba: Mi-Fa-Sol', ev2c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, aquí en un dibujo distinto al de antes.')
    y -= 12
    pattern_a = [(['C3', 'E3', 'G3'], 'Do'), (['G2', 'B2', 'D3'], 'Sol'),
                 (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Sol-Fa-Do, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = []
    for root, lab in [(['C3'], 'Do'), (['G2', 'B2', 'D3'], 'Sol'), (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do')]:
        pattern_b.append({'pitches': root, 'dur': 'h', 'label': lab})
        pattern_b.append({'pitches': root, 'dur': 'h'})
    y = system_block(c, x0, w0, y, gap, 'b) Bajo y acorde en blancas, muy tranquilo', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la derecha vuela en grupos de tres, la izquierda se queda tranquila.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la derecha vuela, la izquierda descansa', 2,
                          'La izquierda sostiene el acorde largo; la derecha se mueve ligera en grupos de tres, sin prisa ni atropello.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4'] * 8)]
    bass1 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(['C3', 'E3', 'G3'], 'Do'), (['A2', 'C3', 'E3'], 'Lam'), (['F2', 'A2', 'C3'], 'Fa')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La derecha vuela en grupos de tres; la izquierda se queda tranquila', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['G4', 'F4', 'E4'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para sentir el vuelo de los grupos de tres', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia rítmica · el acorde no se mueve', 3,
                          'La izquierda sostiene el acorde entero, sin tocarlo de nuevo; la derecha no para de moverse en grupos de tres.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'E4', 'D4'] * 8)]
    bass3 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa'),
              (['G2', 'B2', 'D3'], 'Sol'), (['C3', 'E3', 'G3'], 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda sostiene el acorde entero; la derecha no para', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in
             ['C4', 'D4', 'E4', 'C4', 'D4', 'E4', 'C4', 'D4', 'E4', 'C4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: las mismas notas, pero en negras tranquilas', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Soldadito de Hierro casi entero', 3,
                          'Con la partitura al lado: ligero y rápido en la derecha, tranquilo y firme en la izquierda.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
             (['C4', 'D4', 'E4'] * 4 + ['E4', 'F4', 'G4'] * 4) * 2)]
    bass5 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(['C3', 'E3', 'G3'], 'Do'), (['A2', 'C3', 'E3'], 'Lam'), (['F2', 'A2', 'C3'], 'Fa'),
              (['C3', 'E3', 'G3'], 'Do'), (['G2', 'B2', 'D3'], 'Sol'), (['C3', 'E3', 'G3'], 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Enérgico ♩≈84, ligera', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
