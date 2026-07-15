# -*- coding: utf-8 -*-
"""Taller de practica - Soldadito de Hierro (Dilan, cancion 5 de 5, LA MENOR, 4/4)
   Tema: grupos de tres notas ligeros y rapidos en la derecha, mientras la
   izquierda descansa en acordes largos. La armadura no lleva alteraciones,
   pero la armonia real (Lam-Rem-Mi7-Lam) confirma que el centro tonal es
   LA MENOR, no Do mayor -- verificado sobre la partitura, no asumido."""
from page_layout_common import *

SONG_KICKER = 'DILAN · NOVIEMBRE · SOLDADITO DE HIERRO (NIL MOLINER)'
TS = (4, 4)

AM = ['A2', 'C3']
DM = ['D2', 'F2', 'A2']
E7 = ['E2', 'G#2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción en La menor con la derecha muy viva. El reto: grupos de tres notas ligeros y rápidos.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Misma armadura que Do mayor, pero el centro tonal es La.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('C5', 3), ('B4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, con soltura', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('E5', 5), ('C5', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, desgranado', ev1b, clef='treble', time_sig=TS)

    ev1c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('A4', 2), ('B4', 2), ('B4', 3), ('C5', 3), ('C5', 4), ('D5', 4), ('D5', 5)]]
    y = system_block(c, x0, w0, y, gap, 'c) Repetida, cambiando de dedo', ev1c, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Grupos de tres, ligeros y rápidos', 2,
                          'La dificultad exacta de esta canción. Practica cada grupo de tres muy despacio, como un giro pequeño de la muñeca, y ve acelerando poco a poco.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['B4', 'C5', 'D5'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'a) Grupos de tres subiendo: Si-Do-Re', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
            [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam')]]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: acordes largos y tranquilos, sin prisa', ev2b, clef='bass', time_sig=TS)
    y -= 3

    ev2c = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C5', 'D5', 'E5'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'c) Grupos de tres, un escalón más arriba: Do-Re-Mi', ev2c, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V7 en La menor', 2,
                          'Lam–Rem–Mi7: los acordes de esta tonalidad menor. El Mi7 lleva el Sol sostenido, la nota sensible que "tira" hacia el La.')
    y -= 12
    pattern_a = [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mi7-Lam, un acorde por tiempo', eva, clef='bass', time_sig=TS)
    y -= 3

    pattern_b = []
    for chord, lab in [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam')]:
        pattern_b.append({'pitches': [chord[0]], 'dur': 'h', 'label': lab})
        pattern_b.append({'pitches': chord[1:], 'dur': 'h'})
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
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['B4', 'C5', 'D5'] * 8)]
    bass1 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La derecha vuela en grupos de tres; la izquierda se queda tranquila', grand_gap_mult=7.3, time_sig=TS)
    y -= 3

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['E5', 'D5', 'C5'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para sentir el vuelo de los grupos de tres', treb2, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 5, 'Independencia rítmica · el acorde no se mueve', 3,
                          'La izquierda sostiene el acorde entero, sin tocarlo de nuevo; la derecha no para de moverse en grupos de tres.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['B4', 'D5', 'C5'] * 8)]
    bass3 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda sostiene el acorde entero; la derecha no para', grand_gap_mult=7.3, time_sig=TS)
    y -= 3

    treb4 = [{'pitch': p, 'dur': 'q'} for p in
             ['A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: las mismas notas, pero en negras tranquilas', treb4, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 6, 'Reto final · Soldadito de Hierro casi entero', 3,
                          'Con la partitura al lado: ligero y rápido en la derecha, tranquilo y firme en la izquierda.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
             (['B4', 'C5', 'D5'] * 4 + ['C5', 'D5', 'E5'] * 4) * 2)]
    bass5 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam'), (DM, 'Rem'), (AM, 'Lam')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Enérgico ♩≈84, ligera', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
