# -*- coding: utf-8 -*-
"""Taller de practica - It's Beginning to Look a Lot Like Christmas
   (Valentina, cancion 7, Piano Duet, Do mayor, 6/8, mismo archivo que
   Dilan). Nivel medio, un poco mas exigente: la textura a cuatro
   manos -- equilibrar quien lleva la melodia, porque el papel
   cambia a mitad de pieza."""
from page_layout_common import *

SONG_KICKER = "VALENTINA · NIVEL MEDIO · IT'S BEGINNING TO LOOK A LOT LIKE CHRISTMAS (A 4 MANOS)"
TS = (6, 8)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico a dúo, en Do mayor y 6/8. Hoy: equilibrar quién lleva la melodía.')
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

    y = exercise_heading(c, y, 2, 'La textura a cuatro manos: equilibrar quién lleva la melodía', 2,
                          'Esta pieza es para dos pianistas. Hoy el papel cambia: primero tú llevas la melodía y tu compañero acompaña, luego los papeles se intercambian.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4', 'G4', 'F4', 'E4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'a) Primero tú llevas la melodía (Piano 1)', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in [(DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (DO, 'Do')]]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora tú acompañas: el papel de tu compañero (Piano 2)', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in [(DO, 'Do'), (SOL, 'Sol')]]
    bass2c = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C3', 'D3', 'E3', 'G3', 'F3', 'E3'])]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Ahora al revés: tú acompañas, la melodía va abajo', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Manos juntas, el cambio de papel, y la ronda casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · tu melodía sobre el acompañamiento', 2,
                          'Tu melodía (Piano 1) sobre los acordes largos de tu compañero (Piano 2).')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4', 'F4', 'E4', 'D4'] * 2)]
    bass4 = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) Tu melodía sobre los acordes largos', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El cambio de papel: ahora tú acompañas', 3,
                          'Los acordes largos suben a tu mano; la melodía baja a la de tu compañero. Escúchala sin taparla.')
    y -= 11
    treb5 = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]]
    bass5 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C3', 'D3', 'E3', 'F3', 'E3', 'D3'] * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Ahora tú acompañas; la melodía va abajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · la ronda casi entera, con el papel cambiado', 3,
                          'Con tu compañero en la otra parte: la primera mitad llevas tú, la segunda acompañas.')
    y -= 11
    treb6 = ([{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4', 'F4', 'E4', 'D4'])] +
             [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa')]])
    bass6 = ([{'pitches': p, 'dur': 'q.', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa')]] +
             [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C3', 'D3', 'E3', 'F3', 'E3', 'D3'])])
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La ronda casi completa · ♩.≈100, el papel se intercambia', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
