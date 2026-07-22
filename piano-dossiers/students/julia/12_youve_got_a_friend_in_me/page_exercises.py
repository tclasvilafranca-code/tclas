# -*- coding: utf-8 -*-
"""Taller de practica - You've Got a Friend in Me (Julia, cancion
   12, Do mayor, 4/4). Nivel inicial: dos voces que caminan juntas
   -- las dos manos se mueven a la vez, como dos amigos que
   caminan al mismo paso. Enfoque distinto del que tendran Merce y
   Luisa para la misma cancion."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · YOU\'VE GOT A FRIEND IN ME'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de amistad en Do mayor. Hoy las dos manos caminan juntas, ¡al mismo paso!')
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

    y = exercise_heading(c, y, 2, 'Dos voces que caminan juntas', 2,
                          'Lo que vamos a practicar hoy. Las dos manos se mueven a la vez, cada una con su nota — como dos amigos que caminan al mismo paso, sin adelantarse.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'C4', 'D4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) La voz de arriba, sola primero', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'D3', 'E3', 'D3', 'C3', 'D3', 'E3', 'D3']]
    y = system_block(c, x0, w0, y, gap, 'b) La voz de abajo, con el mismo paso', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'C4', 'D4', 'E4', 'D4']]
    bass2c = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'D3', 'E3', 'D3', 'C3', 'D3', 'E3', 'D3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos voces, caminando juntas al mismo paso', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora las dos manos caminan juntas todo el rato, como buenos amigos.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · caminando en Fa', 2,
                          'Las dos manos se mueven a la vez, cada una con su nota, como dos amigos caminando al mismo paso.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'G4', 'A4', 'G4']]
    bass1 = [{'pitch': p, 'dur': 'q'} for p in ['F3', 'G3', 'A3', 'G3', 'F3', 'G3', 'A3', 'G3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Las dos voces caminando en Fa', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4', 'F4', 'A4', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la voz de arriba: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · cada voz con su propio camino', 3,
                          'Las dos manos caminan a la vez, pero cada una sigue su propio camino de notas, sin chocar.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'A4', 'B4', 'A4']]
    bass3 = [{'pitch': p, 'dur': 'q'} for p in ['G3', 'A3', 'B3', 'A3', 'G3', 'A3', 'B3', 'A3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Las dos voces caminando en Sol', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4', 'G4', 'B4', 'D5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, con saltos', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · You\'ve Got a Friend in Me casi entera', 3,
                          'Con la partitura al lado: ¡deja que las dos manos caminen juntas, como buenos amigos!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'C4', 'D4', 'E4', 'D4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'G4', 'A4', 'G4']])
    bass5 = ([{'pitch': p, 'dur': 'q'} for p in ['C3', 'D3', 'E3', 'D3', 'C3', 'D3', 'E3', 'D3']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F3', 'G3', 'A3', 'G3', 'F3', 'G3', 'A3', 'G3']])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con las dos voces caminando juntas', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
