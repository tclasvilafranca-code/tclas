# -*- coding: utf-8 -*-
"""Taller de practica - Chopsticks (Arnau, cancion 1, Do mayor, 3/4).
   Nivel iniciacion, 9 anos. Bloque 1 (calentamiento corto), bloque 2
   (tecnica: manos alternas en posicion de 5 dedos), bloque 3 (lectura
   del propio patron de la cancion), bloque 6 (dictado de grados)."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · CHOPSTICKS'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El juego de piano más famoso del mundo, en Do mayor: las dos manos se turnan sin chocar nunca.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: mano quieta, dedos que caminan', 1,
                          'Antes de tocar: apoya la mano en la tapa cerrada y camina con los dedos 1-2-3-2-1, sin mover la muñeca.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Posición de 5 dedos: Do(1) Re(2) Mi(3) Fa(4) Sol(5)', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El turno de las dos manos', 2,
                          'Esto es lo importante de hoy: una mano toca su turno entero y espera quieta mientras toca la otra.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Turno de la mano derecha, con calma', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.'} for p in ['C3', 'D3', 'E3']]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora responde la mano izquierda, en el mismo sitio', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos juntas: cada una espera su turno', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 1,
                          'Do–Fa–Sol: los tres acordes que acompañan a Chopsticks.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde entero por compás', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Estudia cada mano por separado antes de juntarlas: así ninguna "come" el turno de la otra.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el acorde de Fa se queda quieto', 2,
                          'La izquierda sostiene el acorde entero sin moverse; la derecha juega su turno encima, ligera.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['F4', 'G4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Turno de la derecha sobre Fa quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para comparar cómo suena sola', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia', 2,
                          'La izquierda queda firme con su acorde de Sol; la derecha se mueve, pero abajo no cambia nada.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'A4', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Turno de la derecha sobre Sol quieto', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, un peldaño más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Chopsticks casi entera', 2,
                          'Con la partitura al lado: ¡a jugar a pasarse la pelota entre las dos manos!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']] +
             [{'pitch': p, 'dur': 'h.'} for p in ['F4', 'G4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [DO, DO, DO, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · jugando con las dos manos', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
