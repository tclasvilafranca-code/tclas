# -*- coding: utf-8 -*-
"""Taller de practica - Have Yourself a Merry Little Christmas (Dilan,
   cancion 6, Do mayor, 4/4). Estructura DISTINTA otra vez: la partitura real
   armoniza la melodia con pequenos acordes en la mano derecha (estilo
   villancico/himno), asi que el foco es "melodia en acordes" -- y un
   ejercicio nuevo de eco dinamico en tres pasos (mf-mp-p), distinto del
   contraste p/f de Writing's on the Wall."""
from page_layout_common import *

SONG_KICKER = 'DILAN · DICIEMBRE · HAVE YOURSELF A MERRY LITTLE CHRISTMAS'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico clásico en Do mayor. Aquí la melodía se toca en pequeños acordes.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('D4', 2), ('F4', 4), ('E4', 3), ('G4', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) A saltos, como campanitas', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('G4', 5), ('E4', 3), ('G4', 5)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Melodía en acordes: así se tocan los villancicos', 2,
                          'En la partitura real, la mano derecha no toca una sola nota: toca pequeños acordes que llevan la melodía, como un coro cantando a varias voces. Primero la melodía sola, luego con su armonía.')
    y -= 12
    melody = [('C4', 1), ('D4', 2), ('E4', 3), ('G4', 5)] * 4
    ev2a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in melody]
    y = system_block(c, x0, w0, y, gap, 'a) Primero solo la melodía', ev2a, clef='treble', time_sig=TS)

    harmon = [['A3', 'C4'], ['B3', 'D4'], ['C4', 'E4'], ['E4', 'G4']] * 4
    ev2b = [{'pitches': p, 'dur': 'q'} for p in harmon]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora con su pequeño acorde debajo', ev2b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los acordes que sostienen el villancico en la izquierda.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (FA, 'Fa')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, un eco que se aleja, y el villancico casi entero.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre los acordes', 2,
                          'La izquierda sostiene el acorde; la derecha canta la melodía por encima.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in [('C4', 1), ('D4', 2), ('E4', 3), ('G4', 5)] * 2]
    bass1 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (SOL, 'Sol'), (DO, 'Do'), (SOL, 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase con su acompañamiento', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Eco navideño: cada vez más flojito', 3,
                          'La misma frase, tres veces, como si te alejaras calle abajo cantando villancicos: primero con voz normal, luego más flojo, luego casi un susurro.')
    y -= 11
    phrase = [('C4', 'q'), ('E4', 'q'), ('G4', 'q'), ('E4', 'q')]
    ev5a = [{'pitch': p, 'dur': d} for p, d in phrase]
    y = system_block(c, x0, w0, y, gap, 'a) mf — voz normal', ev5a, clef='treble', time_sig=TS)

    ev5b = [{'pitch': p, 'dur': d} for p, d in phrase]
    y = system_block(c, x0, w0, y, gap, 'b) mp — ya más lejos', ev5b, clef='treble', time_sig=TS)

    ev5c = [{'pitch': p, 'dur': d} for p, d in phrase]
    y = system_block(c, x0, w0, y, gap, 'c) p — casi un susurro, se pierde a lo lejos', ev5c, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · el villancico casi entero', 3,
                          'Con la partitura al lado: deja que los acordes largos sostengan la melodía, sin prisa.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in [('C4', 1), ('D4', 2), ('E4', 3), ('G4', 5)] * 4]
    bass6 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'El villancico casi completo · ♩≈66, con dulzura', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
