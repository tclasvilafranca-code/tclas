# -*- coding: utf-8 -*-
"""Taller de practica - Soldadito de Hierro (Sandi, cancion 1, Nil
   Moliner, La menor -- armadura sin alteraciones, pero armonia real
   Lam-Rem-Mi7-Lam confirma el centro tonal, mismo archivo que Dilan
   y Eva, 4/4). Nivel avanzado: el tresillo constante -- ni acelerar
   ni frenar, precision ritmica pura."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · SOLDADITO DE HIERRO (NIL MOLINER)'
TS = (4, 4)

AM = ['A2', 'C3']
DM = ['D2', 'F2', 'A2']
E7 = ['E2', 'G#2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Soldadito de Hierro, de Nil Moliner, en La menor. Hoy: el tresillo constante, sin acelerar ni frenar.')
    y -= 15
    gap = 7.35
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Misma armadura que Do mayor, pero el centro tonal es La.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('E5', 5), ('D5', 4), ('C5', 3), ('B4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido completo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('E5', 5), ('C5', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El tresillo constante: ni acelerar ni frenar', 3,
                          'La dificultad de hoy. Un metrónomo interno debe latir en cada tresillo: las tres corcheas ocupan siempre el mismo tiempo exacto, sin precipitarse al final ni arrastrarse al empezar.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['A4', 'B4', 'C5'] * 4 + ['C5', 'D5', 'E5'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'a) Con metrónomo mental: cuenta "uno-y-a" en cada tresillo, siempre igual', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['E5', 'D5', 'C5'] * 4 + ['C5', 'B4', 'A4'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) Bajando, con el mismo pulso interno inalterable', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['A4', 'C5', 'B4'] * 8)]
    bass2c = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El tresillo constante sobre el acorde sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V7 en La menor', 2,
                          'Lam–Rem–Mi7: los acordes de esta tonalidad menor. El Mi7 lleva el Sol sostenido, la nota sensible que "tira" hacia el La.')
    y -= 9
    pattern_a = [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mi7-Lam, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: cada tresillo debe sonar exactamente igual al anterior, sin fluctuar.')
    y -= 15
    gap = 7.05
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el tresillo constante sobre el acorde de Re menor', 3,
                          'La izquierda sostiene el acorde entero, inmóvil; la derecha repite tresillos perfectamente iguales entre sí, sin variación de velocidad.')
    y -= 8
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['D5', 'F5', 'A5'] * 8)]
    bass1 = [{'pitches': DM, 'dur': 'w'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Tresillos exactos sobre Re menor, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['A5', 'F5', 'D5'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, bajando: para comparar la regularidad', treb2, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Mi7 no se contagia del tresillo', 3,
                          'La izquierda sostiene el acorde de Mi7, con su sensible Sol#, inmóvil; la derecha no acelera aunque el acorde tenga más notas.')
    y -= 8
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['E5', 'G#5', 'B5'] * 8)]
    bass3 = [{'pitches': E7, 'dur': 'w'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Tresillos exactos sobre Mi7; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in
             ['A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Contraste: las mismas notas en negras, sin tresillo, para sentir la diferencia', treb4, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 6, 'Reto final · Soldadito de Hierro casi entero', 3,
                          'Con la partitura al lado y metrónomo: cada tresillo, exactamente igual de rápido que el anterior, del primero al último.')
    y -= 8
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
             (['A4', 'B4', 'C5'] * 4 + ['C5', 'D5', 'E5'] * 4) * 2)]
    bass5 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam'), (DM, 'Rem'), (AM, 'Lam')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · tresillo constante, ♩≈84', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
