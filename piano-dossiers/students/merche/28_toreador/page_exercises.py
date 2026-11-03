# -*- coding: utf-8 -*-
"""Taller de practica - Toreador, de Carmen (Merce, cancion 28,
   Georges Bizet, arr. Gilbert DeBenedetti, Fa mayor, 4/4, "March
   time"). Compartida con Jose Maria, pero con enfoque propio y
   distinto: el acorde picado y acentuado -- corto y decidido, sin
   arrastrar el sonido. Cancion final, la mas exigente del album."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO (RETO FINAL) · TOREADOR'
TS = (4, 4)

FA = ['F2', 'A2', 'C3']
SIb = ['Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El Toreador de Carmen, en Fa mayor. Hoy, el reto final: el acorde picado y acentuado.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El Sib es la única tecla negra de esta posición.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El acorde picado y acentuado: corto y decidido', 3,
                          'El reto final del álbum. El acompañamiento marcha con acordes picados (staccato): cortos, separados y con firmeza, sin arrastrar el sonido de uno al siguiente.')
    y -= 9
    ev2a = [{'pitches': FA, 'dur': 'q'}] * 4
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Fa, picado cuatro veces: corto y separado', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': SIb, 'dur': 'q'}] * 4
    y = system_block(c, x0, w0, y, gap, 'b) Lo mismo sobre Sib: cada golpe, corto y decidido', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'F5', 'C5']]
    bass2c = [{'pitches': FA, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía marcial sobre el acorde picado de Fa', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: el acorde picado marcha firme mientras la melodía canta con fuerza.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía marcial sobre el acorde picado de Sib', 2,
                          'La izquierda pica su acorde de Sib en cada tiempo; la derecha canta la melodía con firmeza.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'F5', 'Bb5', 'F5']]
    bass1 = [{'pitches': SIb, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía marcial sobre el acorde de Sib, picado', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'F5', 'Bb5', 'F5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el picado no descontrola el acorde', 3,
                          'La izquierda pica su acorde de Do con firmeza; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'G5', 'C6', 'G5']]
    bass3 = [{'pitches': DO, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre el acorde de Do, picado', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C6', 'G5', 'E5', 'G5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, invertida', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Toreador casi entera: el reto final del álbum', 3,
                          'Con la partitura al lado: marcha con firmeza, con cada acorde corto, decidido y bien acentuado.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'F5', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['D5', 'F5', 'Bb5', 'F5']])
    bass5 = [{'pitches': p, 'dur': 'q'} for p in [FA, FA, FA, FA, SIb, SIb, SIb, SIb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Toreador casi completa · con el acorde picado y acentuado, el reto final', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
