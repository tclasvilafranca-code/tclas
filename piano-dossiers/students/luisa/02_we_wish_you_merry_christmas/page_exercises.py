# -*- coding: utf-8 -*-
"""Taller de practica - We Wish You a Merry Christmas (Luisa,
   cancion 2, arr. Gilbert DeBenedetti, Do mayor, 3/4). Nivel
   hobby, sin complicaciones: la respuesta del bajo -- cuando la
   derecha calla, la izquierda responde, como una conversacion
   tranquila."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · WE WISH YOU A MERRY CHRISTMAS'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'We Wish You a Merry Christmas, en Do mayor. Hoy, tranquila: la respuesta del bajo.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La respuesta del bajo: una conversación tranquila', 2,
                          'Lo de hoy. Cuando la mano derecha calla un momento, la izquierda responde sola: como una charla relajada entre las dos manos.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4']] + [{'rest': True, 'dur': 'h.'}]
    y = system_block(c, x0, w0, y, gap, 'a) La derecha canta, y luego calla', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'rest': True, 'dur': 'h.'}] + [{'pitch': p, 'dur': 'q'} for p in ['C3', 'D3', 'E3']]
    y = system_block(c, x0, w0, y, gap, 'b) Y ahora responde la izquierda, tranquila', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde de Do, tranquilo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes, sin más complicación.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: escucha cuándo le toca a cada una.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde de Fa', 2,
                          'La izquierda sostiene su acorde, tranquila; la derecha canta encima, sin prisa.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Fa, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · cada mano a su ritmo, sin agobios', 3,
                          'La izquierda espera y luego responde; la derecha canta primero, tranquila.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4']] + [{'rest': True, 'dur': 'h.'}]
    bass3 = [{'rest': True, 'dur': 'h.'}] + [{'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La derecha canta, y la izquierda responde', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sin la respuesta', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · We Wish You a Merry Christmas casi entera', 3,
                          'Con la partitura al lado: disfruta tranquila esa pequeña conversación entre las manos.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4']] + [{'rest': True, 'dur': 'h.'}])
    bass5 = [{'pitches': DO, 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'We Wish You a Merry Christmas casi completa · sin prisa', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
