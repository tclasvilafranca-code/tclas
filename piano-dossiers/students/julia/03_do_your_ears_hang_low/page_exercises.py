# -*- coding: utf-8 -*-
"""Taller de practica - Do Your Ears Hang Low (Julia, cancion 3, Do
   mayor, 4/4). Nivel inicial: el salto gracioso -- subir y bajar
   como orejas que se balancean."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · DO YOUR EARS HANG LOW'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción divertida en Do mayor. Hoy jugamos con el salto gracioso: ¡sube y baja como orejas!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). ¡Busca tu nota casa, el Do!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El salto gracioso: sube y baja como orejas', 2,
                          'Lo que vamos a practicar hoy. La melodía salta de una nota grave a una aguda y vuelve, como orejas que se balancean de un lado a otro.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'G4', 'C4', 'G4', 'D4', 'A4', 'D4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) El salto que se balancea', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo camino, paso a paso: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'G4', 'C4', 'G4', 'D4', 'A4', 'D4', 'A4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El salto sobre el acorde de Do, quieto', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: el salto se balancea mientras el acorde se queda quieto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el salto sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha se balancea arriba y abajo.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'C5', 'F4', 'C5', 'G4', 'D5', 'G4', 'D5']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El salto sobre Fa, quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'C5', 'Bb4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin saltos: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del salto', 3,
                          'La izquierda queda quieta con su acorde; la derecha se balancea, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'D5', 'G4', 'D5', 'A4', 'E5', 'A4', 'E5']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El salto vuela; el acorde de Sol no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un poco más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Do Your Ears Hang Low casi entera', 3,
                          'Con la partitura al lado: ¡deja que el salto se balancee, como orejas contentas!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'G4', 'C4', 'G4', 'D4', 'A4', 'D4', 'A4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'C5', 'F4', 'C5', 'G4', 'D5', 'G4', 'D5']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con el salto balanceándose', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
