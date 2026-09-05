# -*- coding: utf-8 -*-
"""Taller de practica - It's Beginning to Look a Lot Like Christmas (Dilan,
   cancion 8, Piano Duet, Do mayor, 6/8). Estructura DISTINTA otra vez:
   compas compuesto (6/8, nunca usado en un dosier de Dilan) + duo real
   (Piano 1 + Piano 2), asi que el foco es mantener el vaiven de 6/8
   SINCRONIZADO con otra persona -- y un ritmo con enganche (negra con
   puntillo + corchea) que no ha aparecido en ningun otro dosier."""
from page_layout_common import *

SONG_KICKER = "DILAN · DICIEMBRE · IT'S BEGINNING TO LOOK A LOT LIKE CHRISTMAS (A 4 MANOS)"
TS = (6, 8)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico a dúo, en Do mayor y compás de 6/8: el vaivén se siente de dos en dos.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor, con vaivén', 1,
                          'Grupos de tres corcheas: siente DOS grandes pulsos por compás, no seis golpes sueltos.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4', 'G4', 'F4', 'E4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'a) Dos olas de tres notas', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'E4', 'G4', 'E4', 'C4', 'G4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, en cada ola', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El vaivén a dúo: tú tocas una ola, tu compañero la otra', 2,
                          'Esta pieza es para dos pianistas. El reto no son las notas: es que las dos olas de 6/8 suenen como una sola, sin que nadie se adelante ni se retrase.')
    y -= 12
    ev2a = ([{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['C4', 'D4', 'E4']] +
            [{'rest': True, 'dur': 'e'}] * 3) * 2
    y = system_block(c, x0, w0, y, gap, 'a) Tu ola (Piano 1): suena y calla', ev2a, clef='treble', time_sig=TS)

    ev2b = ([{'rest': True, 'dur': 'e'}] * 3 +
            [{'pitch': p, 'dur': 'e', 'beam': 1} for p in ['G3', 'F3', 'E3']]) * 2
    y = system_block(c, x0, w0, y, gap, 'b) La ola del profe (Piano 2): calla y responde', ev2b, clef='bass', time_sig=TS)

    treb2c = ([{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['C4', 'D4', 'E4']] +
              [{'rest': True, 'dur': 'e'}] * 3) * 2
    bass2c = ([{'rest': True, 'dur': 'e'}] * 3 +
              [{'pitch': p, 'dur': 'e', 'beam': 1} for p in ['G3', 'F3', 'E3']]) * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos olas juntas: se turnan sin pisarse', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V, con el vaivén', 2,
                          'Do–Sol–Fa–Do: un acorde largo por cada gran pulso del compás.')
    y -= 11
    pattern_a = [(DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Un acorde por ola', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, el ritmo con enganche, y la ronda casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · las dos partes a la vez', 2,
                          'Tu melodía (Piano 1) sobre los acordes largos de tu compañero (Piano 2).')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4', 'F4', 'E4', 'D4'] * 2)]
    bass4 = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) Tu melodía sobre los acordes largos', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El ritmo con enganche: negra con puntillo + corchea', 3,
                          'Un ritmo nuevo, típico de este villancico: una nota larga que "engancha" con una cortita antes del siguiente pulso.')
    y -= 11
    ev5a = [{'pitch': p, 'dur': d} for p, d in [('C4', 'q.'), ('D4', 'e'), ('E4', 'q')] * 4]
    y = system_block(c, x0, w0, y, gap, 'a) Larga-corta-larga: siente el enganche', ev5a, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · la ronda casi entera', 3,
                          'Con tu compañero en la otra parte: cuenta los dos grandes pulsos y deja que las olas se turnen.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4', 'F4', 'E4', 'D4'] * 2)]
    treb6 += [{'pitch': p, 'dur': d} for p, d in [('C4', 'q.'), ('D4', 'e'), ('E4', 'q')] * 2]
    bass6 = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in
             [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do'), (DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La ronda casi completa · ♩.≈100', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
