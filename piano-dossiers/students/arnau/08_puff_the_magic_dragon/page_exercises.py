# -*- coding: utf-8 -*-
"""Taller de practica - Puff the Magic Dragon (Arnau, cancion 8, Do
   mayor, 4/4). Nivel iniciacion: la melodia que suena, notas largas
   que flotan sin prisa."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · PUFF THE MAGIC DRAGON'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción tranquila y soñadora en Do mayor. Hoy: notas largas que flotan, sin ninguna prisa.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: respirar entre frases', 1,
                          'Toca la nota y cuenta hasta 4 en tu cabeza antes de la siguiente — como respirar.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'w', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5)]]
    y = system_block(c, x0, w0, y, gap, 'a) Tres notas muy largas, sin prisa', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La melodía que sueña: notas largas, flotando', 2,
                          'Lo importante hoy: dejar sonar cada nota entera, sin cortarla antes de tiempo.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'G4', 'C5', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) Notas largas que flotan, subiendo y bajando', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'C5', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, ahora andando: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'G4', 'C5', 'G4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía flotando sobre el acorde de Do', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: la melodía flota mientras el acorde se queda quieto y suave.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · flotando sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde suave, sin moverse; la derecha flota con notas largas.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['F4', 'A4', 'C5', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Flotando sobre Fa, quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'C5', 'A4', 'G4', 'F4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, andando: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se apura con la melodía', 3,
                          'La izquierda queda quieta y suave; la derecha flota, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'B4', 'D5', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Flotando sobre Sol, quieto', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'D5', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación, un poco más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Puff the Magic Dragon casi entera', 3,
                          'Con la partitura al lado: deja que cada nota suene entera, sin prisa.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['E4', 'G4', 'C5', 'G4']] +
             [{'pitch': p, 'dur': 'h'} for p in ['F4', 'A4', 'C5', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · flotando con calma', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
