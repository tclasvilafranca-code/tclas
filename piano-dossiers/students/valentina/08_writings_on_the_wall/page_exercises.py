# -*- coding: utf-8 -*-
"""Taller de practica - Writing's on the Wall (Valentina, cancion 8,
   Fa mayor, 4/4, mismo archivo que Dilan). Nivel medio, un poco mas
   exigente: el crescendo largo -- construir tension frase a frase,
   en cuatro escalones, no solo dos matices sueltos."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · WRITING’S ON THE WALL (SAM SMITH)'
TS = (4, 4)

FA = ['F3', 'A3', 'C4']
SIB = ['Bb2', 'D3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de James Bond en Fa mayor. Hoy: el crescendo largo, escalón a escalón.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca siempre la tecla negra Sib.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('A4', 3), ('G4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sintiendo el Sib', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El crescendo largo: construir tensión frase a frase', 2,
                          'La dificultad de hoy. La misma frase, cuatro veces, subiendo de volumen cada vez, sin dar el salto de golpe: pp, luego p, luego mf, luego f.')
    y -= 12
    frase = [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('F4', 1)]
    ev2a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in frase]
    y = system_block(c, x0, w0, y, gap, 'a) pp — casi nada, un susurro', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in frase]
    y = system_block(c, x0, w0, y, gap, 'b) p — un poco más de cuerpo', ev2b, clef='treble', time_sig=TS)
    y -= 3

    ev2c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in frase]
    y = system_block(c, x0, w0, y, gap, 'c) mf — ya se nota la tensión que crece', ev2c, clef='treble', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora los acordes, y luego manos juntas con el crescendo ya construido.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes que sostienen toda la balada.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (DO, 'Do'), (SIB, 'Sib'), (DO, 'Do')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Manos juntas · el último escalón, en forte', 3,
                          'Después de los tres escalones de la página 1, este es el cuarto: forte, con peso pero sin golpear.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('F4', 1)]]
    bass1 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FA, 'Fa'), (FA, None), (SIB, 'Sib'), (SIB, None)]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) f — el escalón final, con todo el peso', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in
             ['C5', 'Bb4', 'A4', 'G4', 'F4', 'G4', 'A4', 'Bb4', 'C5', 'Bb4', 'A4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando dónde crece', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Writing’s on the Wall casi entera', 3,
                          'Con la partitura al lado: los cuatro escalones seguidos, del susurro al forte, sin saltos bruscos.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('F4', 1)]]
    treb5 += [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('F4', 1)]]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(FA, 'Fa'), (FA, None), (SIB, 'Sib'), (SIB, None), (DO, 'Do'), (DO, None), (FA, 'Fa'), (FA, None)]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La balada casi completa · Lento expresivo ♩≈68, crescendo largo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
