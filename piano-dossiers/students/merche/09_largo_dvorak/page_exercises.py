# -*- coding: utf-8 -*-
"""Taller de practica - Largo, Sinfonia n.5 (Merce, cancion 9,
   Dvorak, Do mayor, 4/4). Mismo arreglo compartido con Julia,
   pero con enfoque propio y distinto: la pregunta y la respuesta
   -- la frase que vuelve, un poco mas abajo, con una respuesta
   mas resuelta. Nivel basico pero solido, tono adulto."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · LARGO (DVORÁK)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El Largo de la Sinfonía del Nuevo Mundo, en Do mayor. Hoy: la pregunta musical y su respuesta.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Localiza el Do central como punto de referencia.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La pregunta y la respuesta', 2,
                          'Lo que trabajamos hoy. La melodía plantea una frase que queda "abierta" (la pregunta) y luego la repite un poco más abajo, resolviendo hacia el Do (la respuesta).')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'G4']] + [{'pitch': 'G4', 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'a) La pregunta: termina abierta, sobre el Sol', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F4', 'F4']] + [{'pitch': 'C4', 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'b) La respuesta: la misma idea, resolviendo en el Do', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'G4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La pregunta sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: dale a la pregunta un carácter abierto, y a la respuesta uno resuelto.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la pregunta sobre el acorde de Sol', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha plantea la pregunta, dejándola abierta.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5', 'D5']] + [{'pitch': 'D5', 'dur': 'w'}]
    bass1 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La pregunta sobre Sol, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la respuesta resuelve sin mover el acorde', 3,
                          'La izquierda sostiene el acorde de Fa, quieta; la derecha responde resolviendo hacia una nota de reposo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'C5']] + [{'pitch': 'F4', 'dur': 'w'}]
    bass3 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La respuesta resolviendo sobre Fa; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sin la resolución final', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · el Largo casi entero', 3,
                          'Con la partitura al lado: deja la pregunta abierta y resuelve con calma en la respuesta.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'G4']] + [{'pitch': 'G4', 'dur': 'w'}] +
             [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F4', 'F4']] + [{'pitch': 'C4', 'dur': 'w'}])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, SOL, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El Largo casi completo · con la pregunta y su respuesta', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
