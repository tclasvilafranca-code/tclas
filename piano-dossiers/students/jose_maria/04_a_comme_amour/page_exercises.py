# -*- coding: utf-8 -*-
"""Taller de practica - A comme Amour (Jose Maria, cancion 4, Mi
   menor, 4/4). La partitura real usa semicorcheas en pasajes
   rapidos de arpegio; aqui se trabaja el mismo gesto con corcheas
   (la subdivision mas rapida del motor), con un enfoque relajado:
   dejar que la mano se deslice suelta, sin apretar, como el agua."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · OCTUBRE · A COMME AMOUR (RICHARD CLAYDERMAN)'
TS = (4, 4)

Em = ['E2', 'G2', 'B2']
Am = ['A2', 'C3', 'E3']
B = ['B2', 'D#3', 'F#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una pieza de Richard Clayderman en Mi menor. Sin prisa: notas rápidas, mano suelta.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). Sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('B4', 5), ('A4', 4), ('G4', 3), ('F#4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('G4', 3), ('B4', 5), ('G4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El agua que fluye: notas rápidas, sin apretar la mano', 2,
                          'Lo que vamos a cuidar en esta pieza. Hay un pasillo corto de notas rápidas — deja que la mano se deslice suelta, sin apretar ni un dedo, como el agua que corre.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'F#4', 'G4', 'F#4'] * 2)] + \
           [{'pitch': p, 'dur': 'h'} for p in ['G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) El pasillo rápido, resolviendo sin prisa', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'G4', 'E4', 'G4', 'B4', 'E5']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, en negras tranquilas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'F#4', 'G4', 'F#4'] * 2)] + \
             [{'pitch': p, 'dur': 'h'} for p in ['G4', 'E4']]
    bass2c = [{'pitches': Em, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El pasillo suelto sobre el acorde de Mim, quieto', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en Mi menor', 2,
                          'Mim–Lam–Si: los acordes reales de esta pieza, sin prisa.')
    y -= 11
    pattern_a = [(Em, 'Mim'), (Am, 'Lam'), (B, 'Si'), (Em, 'Mim')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mim-Lam-Si-Mim, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el pasillo rápido fluye mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el agua que fluye sobre el acorde', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha deja correr su pasillo rápido, sin apretar ningún dedo.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'B4', 'C5', 'B4'] * 2)] + \
            [{'pitch': p, 'dur': 'h'} for p in ['C5', 'A4']]
    bass1 = [{'pitches': Am, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El agua fluye sobre Lam, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'B4', 'A4', 'G4', 'F#4', 'G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del agua', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha deja correr su pasillo rápido, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['B4', 'C#5', 'D#5', 'C#5'] * 2)] + \
            [{'pitch': p, 'dur': 'h'} for p in ['D#5', 'B4']]
    bass3 = [{'pitches': B, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El agua fluye; el acorde de Si no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D#5', 'C#5', 'B4', 'A4', 'B4', 'C#5', 'D#5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · A comme Amour casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que el agua fluya siempre suelta, sobre un acorde que no se mueve.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'F#4', 'G4', 'F#4'] * 2)] +
             [{'pitch': p, 'dur': 'h'} for p in ['G4', 'E4']] +
             [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'B4', 'C5', 'B4'] * 2)] +
             [{'pitch': p, 'dur': 'h'} for p in ['C5', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [Em, Em, Am, Am]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · ♩≈69, sin prisa, con el agua fluyendo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
