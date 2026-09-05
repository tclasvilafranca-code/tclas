# -*- coding: utf-8 -*-
"""Taller de practica - Bohemian Rhapsody (Nel, cancion 22, Sib
   mayor, compas mixto 4/4<->5/4). Enfoque: el compas de 5 -- un
   tiempo mas de lo habitual, distinto del enfoque de lectura de
   acordes usado con Dilan y de color armonico usado con Eva."""
from page_layout_common import *

SONG_KICKER = 'NEL · JUNIO · BOHEMIAN RHAPSODY (QUEEN)'
TS44 = (4, 4)
TS54 = (5, 4)

Bb = ['Bb2', 'D3', 'F3']
Eb = ['Eb2', 'G2', 'Bb2']
F = ['F2', 'A2', 'C3']
Gm = ['G2', 'Bb2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La apertura de Bohemian Rhapsody (Queen), en Sib mayor. El reto: el compás de 5.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sib mayor', 1,
                          'Un dedo por tecla: Sib(1) Do(2) Re(3) Mib(4) Fa(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('Bb4', 1), ('C5', 2), ('D5', 3), ('Eb5', 4), ('F5', 5), ('Eb5', 4), ('D5', 3), ('C5', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición', ev1a, clef='treble', time_sig=TS44)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'D5'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sib, desgranado', ev1b, clef='treble', time_sig=TS44)
    y -= 3

    y = exercise_heading(c, y, 2, 'El compás de 5: un tiempo más de lo habitual', 2,
                          'La dificultad exacta de esta canción. De vez en cuando aparece un compás de 5/4 — un tiempo extra que no se puede perder ni acortar.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase, en 4/4', ev2a, clef='treble', time_sig=TS44)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'Eb5', 'F5', 'Eb5', 'D5', 'C5', 'Bb4', 'C5', 'D5', 'Eb5']]
    y = system_block(c, x0, w0, y, gap, 'b) El compás de 5: un tiempo más, en 5/4', ev2b, clef='treble', time_sig=TS54)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'D5']]
    bass2c = [{'pitches': Bb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase en 4/4 sobre el acorde de Sib, sostenido entero', grand_gap_mult=7.3, time_sig=TS44)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Sib–Mib–Fa–Solm: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(Bb, 'Sib'), (Eb, 'Mib'), (F, 'Fa'), (Gm, 'Solm')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sib-Mib-Fa-Solm, un acorde por compás entero', eva, clef='bass', time_sig=TS44)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, en los dos compases: no pierdas el tiempo extra del 5/4.')
    y -= 13
    gap = 7.05
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · en 4/4, sobre el acorde de Mib', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta la frase en 4/4.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['Eb5', 'F5', 'G5', 'Ab5', 'G5', 'F5', 'Eb5', 'F5']]
    bass1 = [{'pitches': Eb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase en 4/4 sobre Mib, sostenido entero', grand_gap_mult=7.05, time_sig=TS44)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G5', 'F5', 'Eb5', 'F5', 'G5', 'Ab5', 'G5', 'F5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, en 4/4: para comparar', treb2, clef='treble', time_sig=TS44)
    y -= 1

    y = exercise_heading(c, y, 5, 'Independencia · en el compás de 5, con las dos manos', 3,
                          'La izquierda sostiene su acorde y añade un tiempo extra; la derecha canta los cinco tiempos completos, sin perder ninguno.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G5', 'Ab5', 'Bb5', 'Ab5', 'G5', 'F5', 'Eb5', 'F5', 'G5', 'Ab5']]
    bass3 = [{'pitches': Gm, 'dur': 'w'}, {'pitches': Gm, 'dur': 'q'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Los cinco tiempos, con el acorde de Solm sosteniendo', grand_gap_mult=7.05, time_sig=TS54)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['Bb5', 'Ab5', 'G5', 'Ab5', 'Bb5', 'C6', 'Bb5', 'Ab5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en 4/4', treb4, clef='treble', time_sig=TS44)
    y -= 1

    y = exercise_heading(c, y, 6, 'Reto final · Bohemian Rhapsody casi entera', 3,
                          'Con la partitura al lado: recuerda que la canción real sigue cambiando de compás — aquí lo trabajamos en 4/4.')
    y -= 4
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'D5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['Eb5', 'F5', 'G5', 'Ab5', 'G5', 'F5', 'Eb5', 'F5']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [Bb, Bb, Eb, Eb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · en 4/4, sin perder el hilo', grand_gap_mult=6.75, time_sig=TS44)

    exercises_footer(c, 4)
    c.showPage()
