# -*- coding: utf-8 -*-
"""Taller de practica - Oh When the Saints (Oriol, cancion 10,
   Primer Level, arr. Gilbert DeBenedetti, Do mayor, 4/4, mismo
   archivo que Julia y Merce). Nivel medio, sin agobiar: el
   acompanamiento sencillo -- acordes que se repiten, sin
   complicarte."""
from page_layout_common import *

SONG_KICKER = 'ORIOL · NIVEL MEDIO · OH WHEN THE SAINTS'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Oh When the Saints, tradicional, en Do mayor. Hoy: el acompañamiento sencillo, sin complicarte.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El acompañamiento sencillo: acordes que se repiten', 2,
                          'Lo de hoy. La izquierda repite el mismo acorde varias veces seguidas: no hay nada que memorizar de nuevo cada vez, solo repetir con seguridad.')
    y -= 9
    ev2a = [{'pitches': DO, 'dur': 'q'}] * 4
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Do, repetido cuatro veces, con seguridad', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': FA, 'dur': 'q'}] * 4
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, repetido igual, sin complicarte', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5']]
    bass2c = [{'pitches': DO, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde de Do, repetido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes, sin más complicación.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: el acorde se repite, sencillo, mientras la melodía canta.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde repetido de Fa', 2,
                          'La izquierda repite el acorde de Fa, sin complicarse; la derecha canta encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'F5']]
    bass1 = [{'pitches': FA, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Fa, repetido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'F5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · sin agobios, cada mano tranquila', 3,
                          'La izquierda repite su acorde de Sol; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G5']]
    bass3 = [{'pitches': SOL, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre Sol, repetido', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G5', 'D5', 'B4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Oh When the Saints casi entera', 3,
                          'Con la partitura al lado: repite el acorde con seguridad, sin agobios.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'F5']])
    bass5 = [{'pitches': p, 'dur': 'q'} for p in [DO, DO, DO, DO, FA, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Oh When the Saints casi completa · sencilla, sin agobios', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
