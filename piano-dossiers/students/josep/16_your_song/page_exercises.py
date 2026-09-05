# -*- coding: utf-8 -*-
"""Taller de practica - Your Song (Josep, cancion 16, Fa mayor pese
   al nombre del archivo, compas mixto 4/4<->2/4). Enfoque: la
   pausa breve -- un compas mas corto sirve para tomar aliento antes
   de la siguiente frase."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · MAYO · YOUR SONG (ELTON JOHN)'
TS44 = (4, 4)
TS24 = (2, 4)

FA = ['F2', 'A2', 'C3']
Am = ['A2', 'C3', 'E3']
SIb = ['Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un clásico de Elton John en Fa mayor. El reto: el compás corto que sirve para respirar.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición', ev1a, clef='treble', time_sig=TS44)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS44)
    y -= 3

    y = exercise_heading(c, y, 2, 'La pausa breve: un compás corto que respira', 2,
                          'La dificultad exacta de esta canción. De vez en cuando aparece un compás de 2/4, más corto — como una pequeña bocanada de aire antes de seguir la frase.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase larga, en 4/4', ev2a, clef='treble', time_sig=TS44)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) El compás corto: la pausa que respira, en 2/4', ev2b, clef='treble', time_sig=TS24)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']]
    bass2c = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase larga sobre el acorde de Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS44)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Fa–Lam–Sib–Do: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (Am, 'Lam'), (SIb, 'Sib'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Lam-Sib-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS44)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, en los dos compases: deja que el compás corto respire, sin cortar la frase.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · en 4/4, sobre el acorde de Lam', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta la frase larga en 4/4.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'B4']]
    bass1 = [{'pitches': Am, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase larga sobre Lam, sostenido entero', grand_gap_mult=7.3, time_sig=TS44)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'B4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, en 4/4: para comparar', treb2, clef='treble', time_sig=TS44)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el compás corto que respira, con las dos manos', 3,
                          'La izquierda marca el acorde con una negra firme en 2/4; la derecha toma aire con la pausa breve antes de seguir.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'Bb4']]
    bass3 = [{'pitches': SIb, 'dur': 'h'}] * 1
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El compás corto, en 2/4: la pausa que respira', grand_gap_mult=7.3, time_sig=TS24)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'C5', 'D5', 'E5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase larga, un escalón más arriba', treb4, clef='treble', time_sig=TS44)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Your Song casi entera', 3,
                          'Con la partitura al lado: deja que el compás corto respire, sin cortar el hilo de la frase.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'B4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [FA, FA, Am, Am]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · en 4/4, con el compás corto respirando por dentro', grand_gap_mult=7.3, time_sig=TS44)

    exercises_footer(c, 4)
    c.showPage()
