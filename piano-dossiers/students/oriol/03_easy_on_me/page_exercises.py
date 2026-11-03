# -*- coding: utf-8 -*-
"""Taller de practica - Easy on Me (Oriol, cancion 3, Adele, arr.
   Holmes, Fa mayor -- armadura de 1 bemol, Sib, confirmada por
   render directo, 4/4). Nivel medio, sin agobiar: acordes anchos,
   sin miedo -- abrir la mano con calma."""
from page_layout_common import *

SONG_KICKER = 'ORIOL · NIVEL MEDIO · EASY ON ME (ADELE)'
TS = (4, 4)

FA = ['F2', 'A2', 'C3', 'F3']
DO = ['C2', 'E2', 'G2', 'C3']
SIb = ['Bb2', 'D3', 'F3', 'Bb3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Easy on Me, de Adele, en Fa mayor. Hoy: acordes anchos, abrir la mano con calma.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El Sib es la única alteración de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'F5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Acordes anchos, sin miedo: abrir la mano con calma', 2,
                          'Lo de hoy. La izquierda toca acordes con la raíz y su octava a la vez: hay que abrir la mano con tranquilidad, sin tensarla, buscando siempre la misma distancia.')
    y -= 9
    ev2a = [{'pitches': FA, 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Fa, con la octava abierta: relaja la mano al soltarlo', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': DO, 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, la misma apertura en otra tecla', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'F5']]
    bass2c = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde ancho de Fa, tranquilo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes principales de esta tonalidad.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SIb, 'Sib'), (DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: abre la mano con calma en cada acorde ancho.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde ancho de Sib', 2,
                          'La izquierda abre la mano en el acorde de Sib, tranquila; la derecha canta encima, sin prisa.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'Bb4']]
    bass1 = [{'pitches': SIb, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Sib, con la mano abierta', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Do no tensa la mano', 3,
                          'La izquierda abre la mano en el acorde de Do sin apretarla; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'E5', 'G5', 'C5']]
    bass3 = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre Do; la mano se abre sin tensión', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G5', 'E5', 'C5', 'E5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en otro orden', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Easy on Me casi entera', 3,
                          'Con la partitura al lado: abre la mano con calma en cada acorde ancho, sin tensarla nunca.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'F5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'Bb4']])
    bass5 = [{'pitches': FA, 'dur': 'w'}, {'pitches': SIb, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Easy on Me casi completa · acordes anchos, sin agobios', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
