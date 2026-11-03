# -*- coding: utf-8 -*-
"""Taller de practica - Aloha Oe (Julia, cancion 19, Liliuokalani,
   Do mayor, compas partido/alla breve, escrito aqui en 4/4). Nivel
   inicial con toque extra: el compas partido -- se cuenta a 2, no
   a 4."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · ALOHA OE'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción hawaiana en Do mayor, "con moto". Hoy: ¡se cuenta a dos, no a cuatro!')
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

    y = exercise_heading(c, y, 2, 'El compás partido: se cuenta a 2, no a 4', 2,
                          'Lo que vamos a practicar hoy. Aunque el compás se escribe en cuatro tiempos, "Aloha Oe" se siente a dos: cada mitad del compás es un solo paso grande.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'D4', 'E4', 'D4', 'C4', 'D4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) Dos pasos grandes por compás: blanca, blanca', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': 'E4', 'dur': 'h.'}, {'pitch': 'F4', 'dur': 'q'},
            {'pitch': 'G4', 'dur': 'h.'}, {'pitch': 'F4', 'dur': 'q'}]
    y = system_block(c, x0, w0, y, gap, 'b) Un paso grande con puntillo, y un pasito corto al final', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'D4', 'E4', 'D4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Dos pasos grandes sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: siente los dos pasos grandes de cada compás.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · dos pasos grandes sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha da sus dos pasos grandes encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'G4', 'F4', 'G4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Dos pasos grandes sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, contando a dos: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el paso con puntillo, con acompañamiento', 3,
                          'La izquierda queda quieta con su acorde; la derecha da su paso largo con puntillo sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': 'G4', 'dur': 'h.'}, {'pitch': 'F4', 'dur': 'q'},
             {'pitch': 'A4', 'dur': 'h.'}, {'pitch': 'G4', 'dur': 'q'}]
    bass3 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El paso con puntillo sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': 'B4', 'dur': 'h.'}, {'pitch': 'A4', 'dur': 'q'},
             {'pitch': 'C5', 'dur': 'h.'}, {'pitch': 'B4', 'dur': 'q'}]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Aloha Oe casi entera', 3,
                          'Con la partitura al lado: ¡cuenta a dos y siente los pasos grandes de la canción hawaiana!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['C4', 'D4', 'E4', 'D4']] +
             [{'pitch': 'E4', 'dur': 'h.'}, {'pitch': 'F4', 'dur': 'q'},
              {'pitch': 'G4', 'dur': 'h.'}, {'pitch': 'F4', 'dur': 'q'}])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Aloha Oe casi completa · con los pasos grandes del compás partido', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
