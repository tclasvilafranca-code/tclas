# -*- coding: utf-8 -*-
"""Taller de practica - Arabesque (Valentina, cancion 9, Burgmuller
   Op.100 a 4 manos, Do mayor, 2/4, mismo archivo que Dilan y Sandi).
   Nivel medio, un poco mas exigente: el equilibrio a dos pianos --
   que ninguna parte tape a la otra."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · ARABESQUE (BURGMÜLLER, A 4 MANOS)'
TS = (2, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un estudio clásico a cuatro manos, en Do mayor. Hoy: el equilibrio entre las dos partes.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas, ligero y rápido.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Baja desde Sol, con chispa', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El equilibrio a dos pianos: que ninguna parte tape a la otra', 2,
                          'Cuando las dos partes suenan a la vez, tienes que escuchar si tu volumen deja oír a la otra. Practica primero cada una por separado, luego juntas y equilibradas.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'E4', 'C4', 'E4'] * 3]
    y = system_block(c, x0, w0, y, gap, 'a) Tu parte (Piano 1): la voz que debe destacar un poco', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['C3', 'E3', 'G3', 'E3'] * 6)]
    y = system_block(c, x0, w0, y, gap, 'b) La parte del profe (Piano 2): más flojita, de fondo', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'E4', 'C4', 'E4'] * 3]
    bass2c = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['C3', 'E3', 'G3', 'E3'] * 6)]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos juntas: tu parte destaca, la otra acompaña', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'El giro rápido', 3,
                          'El adorno que da nombre a la pieza: un giro de cuatro notas, ligero como una pluma.')
    y -= 11
    ev3a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'D4', 'C4', 'D4'] * 6)]
    y = system_block(c, x0, w0, y, gap, 'a) Mi-Re-Do-Re, el giro completo', ev3a, clef='treble', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Los acordes de la tonalidad, el equilibrio invertido, y la pieza casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: la base armónica de todo el estudio.')
    y -= 11
    pattern_a = [(DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (SOL, 'Sol')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Sol-Fa-Sol, un acorde por tiempo', eva, clef='bass', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El equilibrio invertido: ahora tú acompañas', 3,
                          'Los papeles se cambian: ahora tu parte queda de fondo y la otra destaca. Baja tu volumen sin perder el pulso.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['G4', 'E4', 'C4', 'E4'] * 3)]
    bass5 = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3', 'E3', 'C3', 'E3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Ahora tú de fondo; la otra parte destaca', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Arabesque casi entero, con el equilibrio cuidado', 3,
                          'Con tu profe o compañero en la otra parte: escucha en todo momento quién debe destacar.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'D4', 'C4', 'D4'] * 2)]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['G4', 'E4', 'C4', 'E4'] * 3]
    bass6 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(DO, 'Do')] * 4 + [(FA, 'Fa')] * 4 + [(SOL, 'Sol')] * 4 + [(DO, 'Do')] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La pieza casi completa · Allegro scherzando, equilibrada', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
