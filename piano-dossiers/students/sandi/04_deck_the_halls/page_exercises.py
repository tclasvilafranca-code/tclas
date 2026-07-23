# -*- coding: utf-8 -*-
"""Taller de practica - Deck the Halls (Sandi, cancion 4, trad.
   galesa, arr. Jim Paterson, Fa mayor -- armadura de 1 bemol, Sib,
   confirmada por render directo, 4/4). Nivel avanzado: el ritmo
   punteado -- largo-corto, con precision matematica exacta."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · DECK THE HALLS'
TS = (4, 4)

FA = ['F2', 'A2', 'C3']
DO = ['C3', 'E3', 'G3']
SIb = ['Bb2', 'D3', 'F3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Deck the Halls, villancico tradicional galés, en Fa mayor. Hoy: el ritmo punteado exacto.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El Sib es la única alteración de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido completo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'F5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El ritmo punteado: largo-corto, con precisión exacta', 3,
                          'La dificultad de hoy. El punteado clásico de este villancico exige una relación matemática exacta de 3 a 1 entre la nota larga y la corta: no vale aproximarla de oído, hay que sentir la subdivisión interna.')
    y -= 9
    ev2a = [{'pitch': 'F4', 'dur': 'q.'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'q.'}, {'pitch': 'Bb4', 'dur': 'e'}]
    y = system_block(c, x0, w0, y, gap, 'a) Largo-corto exacto: la corchea dura la mitad exacta de la parte larga', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': 'C5', 'dur': 'q.'}, {'pitch': 'Bb4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'q.'}, {'pitch': 'G4', 'dur': 'e'}]
    y = system_block(c, x0, w0, y, gap, 'b) Bajando, con la misma precisión rítmica exacta', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': 'F4', 'dur': 'q.'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'q.'}, {'pitch': 'Bb4', 'dur': 'e'}]
    bass2c = [{'pitches': FA, 'dur': 'h'}, {'pitches': FA, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El ritmo punteado sobre el acorde de Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes principales de esta tonalidad.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SIb, 'Sib'), (DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: cada figura punteada debe sonar con la misma proporción exacta 3 a 1.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el ritmo punteado sobre el acorde de Do', 3,
                          'La izquierda sostiene el acorde de Do, tranquila; la derecha marca el punteado exacto, sin redondear la proporción.')
    y -= 7
    treb1 = [{'pitch': 'G4', 'dur': 'q.'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'Bb4', 'dur': 'q.'}, {'pitch': 'C5', 'dur': 'e'}]
    bass1 = [{'pitches': DO, 'dur': 'h'}, {'pitches': DO, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El ritmo punteado sobre Do, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Contraste: las mismas notas sin punteado, en negras iguales', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Sol (V de V) no descoloca el ritmo', 3,
                          'La izquierda toca el acorde de Sol mayor -- una dominante secundaria prestada de Do mayor, ajena a Fa mayor -- inmóvil; la derecha mantiene su punteado exacto.')
    y -= 7
    treb3 = [{'pitch': 'D5', 'dur': 'q.'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'A4', 'dur': 'e'}]
    bass3 = [{'pitches': SOL, 'dur': 'h'}, {'pitches': SOL, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El ritmo punteado sobre Sol (dominante secundaria); el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Contraste: la misma línea, sin punteado', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Deck the Halls casi entero', 3,
                          'Con la partitura al lado: mantén la proporción exacta 3 a 1 en cada figura punteada, del principio al final.')
    y -= 7
    treb5 = ([{'pitch': 'F4', 'dur': 'q.'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'q.'}, {'pitch': 'Bb4', 'dur': 'e'}] +
             [{'pitch': 'C5', 'dur': 'q.'}, {'pitch': 'Bb4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'q.'}, {'pitch': 'G4', 'dur': 'e'}])
    bass5 = [{'pitches': FA, 'dur': 'h'}, {'pitches': FA, 'dur': 'h'}, {'pitches': SIb, 'dur': 'h'}, {'pitches': DO, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Deck the Halls casi completo · ritmo punteado exacto', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
