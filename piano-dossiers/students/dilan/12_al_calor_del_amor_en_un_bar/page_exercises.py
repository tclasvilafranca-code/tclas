# -*- coding: utf-8 -*-
"""Taller de practica - Al Calor del Amor en un Bar (Dilan, cancion 12,
   Mi menor, 4/4). Estructura DISTINTA otra vez: la partitura real usa un
   acorde de Fa# MAYOR (con Fa#-La#-Do#) que no pertenece a la familia de
   Mi menor -- un acorde "prestado" que sorprende el oido antes de resolver
   a Si menor. Ese es el foco entero: reconocer y sentir ese acorde sorpresa."""
from page_layout_common import *

SONG_KICKER = 'DILAN · ABRIL · AL CALOR DEL AMOR EN UN BAR (GABINETE CALIGARI)'
TS = (4, 4)

MIm = ['E3', 'G3', 'B3']
LAm = ['C3', 'E3', 'A3']
SIm = ['D3', 'F#3', 'B3']
FAsharp = ['F#3', 'A#3', 'C#4']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de rock español en Mi menor, con un acorde que se escapa de la tonalidad.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El dedo 2 toca la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('G4', 3), ('F#4', 2), ('A4', 4), ('G4', 3), ('B4', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) A saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('B4', 5), ('G4', 3), ('B4', 5)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El acorde sorpresa: Fa# mayor no es de la familia', 2,
                          'Mi menor tiene Fa# natural, pero no La sostenido. Este acorde toma prestado un La# de fuera de la tonalidad para dar más tirón antes de caer en Si menor. Escúchalo: suena distinto, "de fuera".')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FAsharp, 'Fa#'), (SIm, 'Sim')] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Fa# (sorpresa) resuelve a Sim (a casa)', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'A#4', 'C#5', 'B4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo salto, como melodía', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'A#4', 'C#5', 'B4'] * 2]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FAsharp, 'Fa#'), (SIm, 'Sim')] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos juntas: siente cómo "tira" hacia Si menor', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en Mi menor', 2,
                          'Mim–Sim–Lam: los acordes de la familia (sin la sorpresa).')
    y -= 11
    pattern_a = [(MIm, 'Mim'), (SIm, 'Sim'), (LAm, 'Lam'), (MIm, 'Mim')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mim-Sim-Lam-Mim, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, independencia rítmica, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · melodía sobre acordes', 2,
                          'La izquierda sostiene los acordes de la familia; la derecha se mueve por la posición.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 1), ('G4', 3), ('F#4', 2), ('A4', 4), ('G4', 3), ('B4', 5), ('A4', 4), ('G4', 3)]]
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(MIm, 'Mim'), (SIm, 'Sim'), (LAm, 'Lam'), (MIm, 'Mim')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La posición sobre los acordes', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia rítmica · el pulso firme, la melodía en corcheas', 3,
                          'La izquierda marca el pulso con calma; la derecha se mueve el doble de rápido.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['E4', 'G4', 'F#4', 'A4', 'G4', 'B4', 'A4', 'G4'] * 2)]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(MIm, 'Mim'), (MIm, None), (LAm, 'Lam'), (LAm, None)]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) El pulso firme bajo la melodía rápida', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Al Calor del Amor casi entera', 3,
                          'Con la partitura al lado: cuando llegue el acorde sorpresa, déjalo sonar distinto antes de resolver.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 1), ('G4', 3), ('F#4', 2), ('A4', 4), ('G4', 3), ('B4', 5), ('A4', 4), ('G4', 3)]]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'A#4', 'C#5', 'B4'] * 2]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(MIm, 'Mim'), (LAm, 'Lam'), (SIm, 'Sim'), (MIm, 'Mim')]]
    bass6 += [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FAsharp, 'Fa#'), (SIm, 'Sim')] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · Allegretto', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
