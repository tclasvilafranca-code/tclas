# -*- coding: utf-8 -*-
"""Taller de practica - My Way (Sandi, cancion 2, Jacques Revaux,
   Do mayor, 4/4, Moderately slow). Nivel avanzado: los acordes
   prestados y las dominantes secundarias -- el color armonico que
   se escapa un instante de la tonalidad, y vuelve."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · MY WAY (JACQUES REVAUX)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
FAm = ['F2', 'Ab2', 'C3']
A7 = ['A2', 'C#3', 'E3', 'G3']
C7 = ['C3', 'E3', 'G3', 'Bb3']
REm = ['D2', 'F2', 'A2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'My Way, de Jacques Revaux, en Do mayor. Hoy: los acordes prestados y las dominantes secundarias.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Punto de partida antes de salir de la tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido completo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los acordes prestados: cuando el modo cambia un instante', 3,
                          'La dificultad de hoy. La canción usa Fa menor (préstamo del modo menor sobre la misma tónica Fa) y dominantes secundarias como A7 (que resuelve en Re menor) y Do7 (que resuelve en Fa): acordes "de paso" que salen de Do mayor un instante y vuelven.')
    y -= 9
    ev2a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FA, 'Fa'), (FAm, 'Fam')]]
    y = system_block(c, x0, w0, y, gap, 'a) Fa mayor y Fa menor: el mismo grado, el modo prestado', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(A7, 'A7'), (REm, 'Rem')]]
    y = system_block(c, x0, w0, y, gap, 'b) La7 resuelve en Re menor: una dominante prestada de otra tonalidad', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'C4']]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(C7, 'Do7'), (FA, 'Fa')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Do7 resuelve en Fa: dominante secundaria hacia el IV grado', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: la base sobre la que se apoyan todos los acordes prestados.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: siente cómo el Fa menor y las dominantes secundarias tiñen la armonía sin romperla.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre Fa menor prestado', 3,
                          'La izquierda sostiene el acorde de Fa menor; la derecha canta encima, sintiendo el oscurecimiento momentáneo antes de volver a Do.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'Ab4', 'F4', 'C5']]
    bass1 = [{'pitches': FAm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Fa menor, prestado', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'A4', 'F4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Comparación: la misma melodía sobre Fa mayor (sin préstamo)', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la dominante secundaria no descoloca la melodía', 3,
                          'La izquierda toca La7 (dominante de Re menor); la derecha mantiene su línea sin dejarse arrastrar por la tensión armónica de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'C#5', 'A4', 'E5']]
    bass3 = [{'pitches': A7, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre La7; la tensión resuelve después, no aquí', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'F4', 'A4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) La resolución: la misma línea, ya sobre Re menor', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · My Way casi entera', 3,
                          'Con la partitura al lado: reconoce cada acorde prestado o dominante secundaria mientras suena, sin perder el pulso ni la calma.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C5', 'Ab4', 'F4', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['E5', 'C#5', 'A4', 'E5']])
    bass5 = [{'pitches': FAm, 'dur': 'w'}, {'pitches': A7, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'My Way casi completa · con el color de los acordes prestados', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
