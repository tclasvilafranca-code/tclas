# -*- coding: utf-8 -*-
"""Taller de practica - Sweet Child O' Mine (Josep, cancion 20, Sib
   mayor, 4/4). Enfoque: el salto de posicion -- la mano cambia de
   sitio de un bloque de 5 dedos a otro, sin mirar el teclado."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · JUNIO · SWEET CHILD O’ MINE (GUNS N’ ROSES)'
TS = (4, 4)

Bb = ['Bb2', 'D3', 'F3']
F = ['F2', 'A2', 'C3']
Eb = ['Eb2', 'G2', 'Bb2']
Ab = ['Ab2', 'C3', 'Eb3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un clásico de Guns N\' Roses en Sib mayor. El reto: la mano salta de posición sin mirar.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sib mayor', 1,
                          'Un dedo por tecla: Sib(1) Do(2) Re(3) Mib(4) Fa(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('Bb4', 1), ('C5', 2), ('D5', 3), ('Eb5', 4), ('F5', 5), ('Eb5', 4), ('D5', 3), ('C5', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'D5'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sib, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El salto de posición: la mano cambia de sitio sin mirar', 2,
                          'La dificultad exacta de esta canción. La mano tiene que saltar de un bloque de 5 dedos a otro, de golpe, sin buscar las teclas con la vista.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'D5', 'F4', 'A4', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) El salto: de Sib a Fa, de golpe', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'Eb5', 'F5', 'Eb5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo camino, paso a paso: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'D5', 'F4', 'A4', 'C5', 'A4']]
    bass2c = [{'pitches': Bb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El salto sobre el acorde de Sib, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Sib–Lab–Mib–Sib: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(Bb, 'Sib'), (Ab, 'Lab'), (Eb, 'Mib'), (Bb, 'Sib')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sib-Lab-Mib-Sib, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la mano derecha salta mientras el acorde de la izquierda no se mueve.')
    y -= 13
    gap = 7.05
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el salto sobre el acorde de Mib', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha salta de posición sin mirar.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['Eb5', 'G5', 'Bb5', 'G5', 'Bb4', 'D5', 'F5', 'D5']]
    bass1 = [{'pitches': Eb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El salto sobre Mib, sostenido entero', grand_gap_mult=7.05, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['Eb5', 'F5', 'G5', 'Ab5', 'Bb5', 'Ab5', 'G5', 'F5']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo camino, paso a paso: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del salto', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha salta de posición, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['Ab4', 'C5', 'Eb5', 'C5', 'Eb4', 'G4', 'Bb4', 'G4']]
    bass3 = [{'pitches': Ab, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El salto vuela; el acorde de Lab no se mueve', grand_gap_mult=7.05, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['Ab4', 'Bb4', 'C5', 'Db5', 'Eb5', 'Db5', 'C5', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: el mismo camino, un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 6, 'Reto final · Sweet Child O\' Mine casi entera', 3,
                          'Con la partitura al lado: deja que la mano salte de posición con decisión, sin mirar el teclado.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'D5', 'F4', 'A4', 'C5', 'A4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['Eb5', 'G5', 'Bb5', 'G5', 'Bb4', 'D5', 'F5', 'D5']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [Bb, Bb, Eb, Eb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con la mano saltando de posición', grand_gap_mult=7.05, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
