# -*- coding: utf-8 -*-
"""Taller de practica - Arabesque (Dilan, cancion 7, Burgmuller Op.100 a 4 manos,
   Do mayor, 2/4). Estructura DISTINTA otra vez: como es una pieza a DUO de
   verdad (Piano 1 + Piano 2), el foco no es "manos juntas" sino tocar EN
   CONJUNTO -- mantener el pulso con otra persona y el dialogo entre partes."""
from page_layout_common import *

SONG_KICKER = 'DILAN · FEBRERO · ARABESQUE (BURGMÜLLER, A 4 MANOS)'
TS = (2, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un estudio clásico a cuatro manos, en Do mayor. Aquí no tocas solo: tocas EN DÚO.')
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

    y = exercise_heading(c, y, 2, 'Tocar a dúo: mantener el pulso con otra persona', 2,
                          'La dificultad real de esta pieza no está en tus dedos: está en encajar con la otra parte. Practica cada voz sola y luego con el profe (o un compañero) al piano de al lado.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4'] * 3]
    y = system_block(c, x0, w0, y, gap, 'a) Tu parte (Piano 1): negras tranquilas', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['E3', 'G3', 'C3', 'G3'] * 6)]
    y = system_block(c, x0, w0, y, gap, 'b) La parte del profe (Piano 2): corcheas que se mueven', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4'] * 3]
    bass2c = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['E3', 'G3', 'C3', 'G3'] * 6)]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos partes juntas: cuenta en voz alta para no perderte', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Los acordes de la tonalidad, el diálogo entre las dos partes, y la pieza casi entera.')
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

    y = exercise_heading(c, y, 5, 'El diálogo: una parte pregunta, la otra responde', 3,
                          'Así está construida la pieza real: una voz suena, calla, y la otra le responde. Nunca tocan exactamente lo mismo a la vez.')
    y -= 11
    treb5 = [{'pitch': 'C4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'G4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
             {'pitch': 'E4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    bass5 = [{'rest': True, 'dur': 'q'}, {'pitch': 'C3', 'dur': 'q'},
             {'rest': True, 'dur': 'q'}, {'pitch': 'E3', 'dur': 'q'},
             {'rest': True, 'dur': 'q'}, {'pitch': 'G3', 'dur': 'q'},
             {'rest': True, 'dur': 'q'}, {'pitch': 'E3', 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Pregunta-respuesta: nunca a la vez', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Arabesque casi entero', 3,
                          'Con tu profe o compañero en la otra parte: escúchate y escúchale. Tocar a dúo es hablar sin palabras.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'D4', 'C4', 'D4'] * 2)]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4'] * 3]
    bass6 = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
             ([(DO, 'Do')] * 4 + [(FA, 'Fa')] * 4 + [(SOL, 'Sol')] * 4 + [(DO, 'Do')] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La pieza casi completa · Allegro scherzando', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
