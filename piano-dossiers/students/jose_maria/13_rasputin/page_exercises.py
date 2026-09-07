# -*- coding: utf-8 -*-
"""Taller de practica - Rasputin (Jose Maria, cancion 13, Si menor,
   4/4). Enfoque relajado: el mismo acorde, una y otra vez, con la
   muneca suelta -- distinto del enfoque de acentos marcados usado
   con Josep para la misma cancion."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · FEBRERO · RASPUTIN (BONEY M.)'
TS = (4, 4)

Bm = ['B2', 'D3', 'F#3']
Em = ['E2', 'G2', 'B2']
FS = ['F#2', 'A#2', 'C#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Boney M. en Si menor, rápida. Sin prisa: el mismo acorde, con la muñeca suelta.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Si menor', 1,
                          'Un dedo por tecla: Si(1) Do#(2) Re(3) Mi(4) Fa#(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('B4', 1), ('C#5', 2), ('D5', 3), ('C#5', 2), ('B4', 1), ('C#5', 2), ('D5', 3), ('C#5', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'F#5', 'D5', 'F#5'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Si menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El mismo acorde, una y otra vez, con la muñeca suelta', 2,
                          'Lo que vamos a cuidar en esta pieza. Aunque la canción sea rápida, el acorde se repite igual muchas veces — la muñeca tiene que quedarse suelta, sin apretarse nunca.')
    y -= 9
    ev2a = [{'pitches': Bm, 'dur': 'q'}] * 8
    y = system_block(c, x0, w0, y, gap, 'a) El acorde repetido, con la muñeca relajada', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': Bm, 'dur': 'h'}] * 4
    y = system_block(c, x0, w0, y, gap, 'b) El mismo acorde, más despacio: para sentir la muñeca suelta', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'B4', 'C#5', 'D5', 'C#5', 'B4', 'C#5']]
    bass2c = [{'pitches': Bm, 'dur': 'q'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde repetido, sin apretar', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en Si menor', 2,
                          'Sim–Mim–Fa#: los acordes reales de esta pieza.')
    y -= 11
    pattern_a = [(Bm, 'Sim'), (Em, 'Mim'), (FS, 'Fa#'), (Bm, 'Sim')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sim-Mim-Fa#-Sim, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el acorde se repite mientras la muñeca queda suelta.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el acorde repetido de Mim', 2,
                          'La izquierda repite su acorde con la muñeca suelta; la derecha canta la melodía encima, sin ninguna prisa.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F#4', 'E4', 'F#4', 'G4', 'F#4', 'E4', 'F#4']]
    bass1 = [{'pitches': Em, 'dur': 'q'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El acorde de Mim repetido, con la muñeca suelta', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F#4', 'G4', 'F#4', 'E4', 'D4', 'C#4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde repetido no se contagia de la melodía', 3,
                          'La izquierda repite su acorde, siempre relajada; la derecha canta despacio, sin que ninguna se apresure.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C#5', 'C#5', 'A#4', 'C#5', 'C#5', 'C#5', 'A#4', 'C#5']]
    bass3 = [{'pitches': FS, 'dur': 'q'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde de Fa# repetido; la mano no se aprieta', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía, un poco más abajo', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Rasputin casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que la muñeca quede suelta aunque el acorde se repita rápido.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'B4', 'C#5', 'D5', 'C#5', 'B4', 'C#5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F#4', 'E4', 'F#4', 'G4', 'F#4', 'E4', 'F#4']])
    bass5 = [{'pitches': Bm, 'dur': 'q'}] * 8 + [{'pitches': Em, 'dur': 'q'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con la muñeca siempre suelta', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
