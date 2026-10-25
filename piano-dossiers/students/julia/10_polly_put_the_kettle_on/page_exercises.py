# -*- coding: utf-8 -*-
"""Taller de practica - Polly Put the Kettle On (Julia, cancion 10,
   Fa mayor, 4/4). Nivel inicial: las notas ligadas -- sin cortar
   entre una y otra, como agua que se sirve sin salpicar."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · POLLY PUT THE KETTLE ON'
TS = (4, 4)

FA = ['F2', 'A2', 'C3']
SIb = ['Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción tradicional en Fa mayor. Hoy las notas van ligadas, sin cortar entre una y otra.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). ¡Busca tu nota casa, el Fa!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Las notas ligadas: sin cortar entre una y otra', 2,
                          'Lo que vamos a practicar hoy. Cada nota se une a la siguiente sin ningún hueco, como servir agua sin salpicar.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase unida, sin ningún corte', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e'} for p in ['F4', 'F4', 'G4', 'G4', 'A4', 'A4', 'Bb4', 'Bb4']] + \
           [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, marcando cada nota: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']]
    bass2c = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase unida sobre el acorde de Fa', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: la frase queda unida mientras el acorde se queda quieto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase unida sobre el acorde de Sib', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta su frase sin cortarla.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'C5', 'Bb4', 'C5', 'D5', 'C5']]
    bass1 = [{'pitches': SIb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase unida sobre Sib, quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e'} for p in ['Bb4', 'Bb4', 'C5', 'C5', 'D5', 'D5', 'C5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, marcando cada nota: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se corta con la frase', 3,
                          'La izquierda queda quieta con su acorde; la derecha canta sin cortes, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'F5', 'E5', 'D5', 'C5', 'D5']]
    bass3 = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase unida sobre Do; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e'} for p in ['C5', 'C5', 'D5', 'D5', 'E5', 'E5', 'D5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, marcando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Polly Put the Kettle On casi entera', 3,
                          'Con la partitura al lado: ¡deja que cada nota se una a la siguiente, sin cortarla!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'C5', 'Bb4', 'C5', 'D5', 'C5']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [FA, FA, SIb, SIb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con las notas unidas', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
