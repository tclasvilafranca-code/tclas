# -*- coding: utf-8 -*-
"""Taller de practica - Silent Night, 4 hands (Merce, cancion 8,
   Do mayor, 3/4, a 4 manos). Nivel basico: el turno que se pasa
   -- la melodia viaja de una parte a la otra, y hay que entrar
   con seguridad justo cuando te toca."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · SILENT NIGHT (A 4 MANOS)'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Silent Night a 4 manos, en Do mayor. Hoy: entrar con seguridad cuando te toca el turno de la melodía.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Localiza el Do central como punto de referencia.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El turno que se pasa: entrar después del silencio del otro', 2,
                          'Lo que trabajamos hoy. Mientras una parte canta la melodía, la otra guarda silencio; luego se intercambian. Hay que entrar con seguridad justo cuando llega tu turno.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4']] + [{'rest': True, 'dur': 'h.'}] * 2
    y = system_block(c, x0, w0, y, gap, 'a) Tu turno, y luego dos compases de silencio esperando al otro', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'rest': True, 'dur': 'h.'}] * 2 + [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Dos compases esperando, y luego tu turno de nuevo', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Tu turno, con el acorde de Do sostenido debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: practica tu turno completo, con el acorde de acompañamiento.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el turno de la melodía sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta su turno de melodía con seguridad.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El turno sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el silencio de espera no rompe el pulso', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha espera su silencio y entra justo a tiempo.')
    y -= 7
    treb3 = [{'rest': True, 'dur': 'h.'}] + [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}, {'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El silencio de espera, y la entrada sobre Sol', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sin silencio', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Silent Night casi entera', 3,
                          'Con la partitura al lado: entra con seguridad justo cuando te toca el turno de la melodía.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4']] +
             [{'rest': True, 'dur': 'h.'}])
    bass5 = [{'pitches': DO, 'dur': 'h.'}, {'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Silent Night casi completa · con el turno que se pasa entre las partes', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
