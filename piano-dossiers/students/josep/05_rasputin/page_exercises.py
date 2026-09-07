# -*- coding: utf-8 -*-
"""Taller de practica - Rasputin (Josep, cancion 5, Si menor, 4/4).
   Angulo: ACENTOS MARCADOS -- cada acorde con un golpe decidido y
   energico, como un baile ruso, sin que el pulso se ablande nunca."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · NOVIEMBRE · RASPUTIN (BONEY M.)'
TS = (4, 4)

Bm = ['B2', 'D3', 'F#3']
Em = ['E2', 'G2', 'B2']
FS = ['F#2', 'A#2', 'C#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Boney M. en Si menor. El reto: acentos marcados y decididos, como un baile enérgico.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Si menor', 1,
                          'Un dedo por tecla: Si(1) Do#(2) Re(3) Mi(4) Fa#(5). El dedo 2 toca la tecla negra Do#.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('B4', 1), ('D5', 3), ('C#5', 2), ('E5', 4), ('D5', 3), ('F#5', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('B4', 1), ('D5', 3), ('F#5', 5), ('D5', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Si menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Acentos marcados: un golpe decidido en cada acorde', 2,
                          'La dificultad exacta de esta canción. Cada acorde cae con energía, como un paso de baile — nada de acordes flojos o difuminados.')
    y -= 9
    ev2a = [{'pitches': p, 'dur': 'q'} for p in [Bm, Bm, Em, Em, FS, FS, Bm, Bm]]
    y = system_block(c, x0, w0, y, gap, 'a) Acordes en bloque, cada uno con un golpe claro', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C#5', 'B4', 'D5', 'F#5', 'E5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) La melodía, con el mismo carácter decidido', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C#5', 'B4', 'D5', 'F#5', 'E5', 'D5']]
    bass2c = [{'pitches': p, 'dur': 'q'} for p in [Bm, Bm, Em, Em, FS, FS, Bm, Bm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, acentuando juntas cada tiempo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en Si menor', 2,
                          'Sim–Mim–Fa#: los tres acordes de esta tonalidad. El Fa# lleva un La# — la sensible que empuja hacia Si.')
    y -= 11
    pattern_a = [(Bm, 'Sim'), (Em, 'Mim'), (FS, 'Fa#'), (Bm, 'Sim')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sim-Mim-Fa#-Sim, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: los acentos marcados suenan en las dos manos a la vez.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · acentos que caen a la vez', 2,
                          'La izquierda marca el acorde con energía; la derecha canta la melodía con el mismo carácter decidido, sin ablandarse.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F#5', 'F#5', 'E5', 'D5', 'F#5', 'A5', 'G5', 'F#5']]
    bass1 = [{'pitches': p, 'dur': 'q'} for p in [Bm, Bm, Em, Em, FS, FS, Bm, Bm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía con acentos, sobre acordes marcados', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'B4', 'A4', 'B4', 'D5', 'F#5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando el carácter', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acento no se pierde al separar las manos', 3,
                          'La izquierda marca acordes cortos y secos; la derecha se mueve más rápido, pero con el mismo carácter enérgico.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D5', 'C#5', 'D5', 'F#5', 'E5', 'D5', 'C#5', 'B4'] * 2)]
    bass3 = [{'pitches': p, 'dur': 'q'} for p in [Bm, Em, FS, Bm, Bm, Em, FS, Bm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La derecha vuela; los acordes de la izquierda no se ablandan', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#5', 'E5', 'D5', 'C#5', 'B4', 'D5', 'F#5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un escalón más abajo', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Rasputin casi entera', 3,
                          'Con la partitura al lado: mantén el carácter enérgico y marcado de principio a fin, como un baile que no pierde fuerza.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['D5', 'D5', 'C#5', 'B4', 'D5', 'F#5', 'E5', 'D5', 'F#5', 'F#5', 'E5', 'D5', 'F#5', 'A5', 'G5', 'F#5']]
    bass5 = [{'pitches': p, 'dur': 'q'} for p in [Bm, Bm, Em, Em, FS, FS, Bm, Bm, Bm, Bm, Em, Em, FS, FS, Bm, Bm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈128, con energía de principio a fin', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
