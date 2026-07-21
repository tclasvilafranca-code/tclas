# -*- coding: utf-8 -*-
"""Taller de practica - Interstellar (Jose Maria, cancion 6, Do
   mayor, 3/4). Enfoque relajado: el legato que no se corta -- cada
   nota se une a la siguiente sin ningun hueco, como una sola
   respiracion larga."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · NOVIEMBRE · INTERSTELLAR (HANS ZIMMER)'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de Interstellar (Hans Zimmer) en Do mayor. Sin prisa: todo unido, sin huecos.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas, sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El legato que no se corta', 2,
                          'Lo que vamos a cuidar en esta pieza. Cada nota se une a la siguiente sin ningún hueco de silencio, como una sola respiración larga, sin prisa.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase unida, sin ningún hueco', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Otra frase, igual de unida: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase unida sobre el acorde sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol–Do: los acordes de esta tonalidad, uno por compás entero, sin prisa.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: la frase se mantiene unida sobre el acorde sostenido.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el legato sobre el acorde de Fa', 2,
                          'La izquierda sostiene su acorde entero, quieta; la derecha canta la frase unida, sin ningún hueco.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'F4', 'G4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El legato sobre Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'G4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia de la melodía', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha canta despacio, sin que ninguna se apresure.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F4', 'G4', 'A4', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El legato sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'A4', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Interstellar casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que cada frase quede unida, como una sola respiración larga.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'F4', 'G4', 'A4']])
    bass5 = [{'pitches': DO, 'dur': 'h.'}] * 3 + [{'pitches': FA, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · muy tranquila, todo unido', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
