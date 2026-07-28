# -*- coding: utf-8 -*-
"""Taller de practica - We Wish You a Merry Christmas (Arnau, cancion
   7, Do mayor, 3/4). Nivel iniciacion: la respuesta del bajo, una
   conversacion tranquila entre las dos manos."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · WE WISH YOU A MERRY CHRISTMAS'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico clásico en Do mayor, en compás de 3/4. Hoy: la izquierda "responde" a la derecha.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: el vals tranquilo', 1,
                          'Cuenta "uno-dos-tres" con calma; el primer tiempo un poco más marcado.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3), ('C4', 1), ('E4', 3)]]
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Do, desgranado en 3/4', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La respuesta del bajo: una conversación tranquila', 2,
                          'La derecha canta una frase corta; la izquierda "le responde" con una nota grave.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'E4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'a) La derecha pregunta, con calma', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.'} for p in ['C3', 'G2', 'C3']]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda responde, en el mismo sitio', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'E4', 'C4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos voces, cada una en su turno', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 1,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')] * 1
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde entero por compás', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la conversación entre la derecha y la izquierda, tranquila.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · pregunta y respuesta sobre Fa', 2,
                          'La derecha pregunta con su frase; la izquierda responde con una nota grave de Fa.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['A4', 'F4', 'C4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Pregunta y respuesta sobre Fa', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'G4', 'A4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la respuesta no interrumpe', 3,
                          'La izquierda responde una sola vez por compás; la derecha no se detiene.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h.'} for p in ['B4', 'G4', 'D4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Pregunta y respuesta sobre Sol', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación de la melodía', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · We Wish You a Merry Christmas casi entera', 2,
                          'Con la partitura al lado: deja que la izquierda "conteste" con calma.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h.'} for p in ['G4', 'E4', 'C4']] +
             [{'pitch': p, 'dur': 'h.'} for p in ['A4', 'F4', 'C4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [DO, DO, DO, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · pregunta y respuesta', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
