# -*- coding: utf-8 -*-
"""Taller de practica - You've Got a Friend in Me (Merce, cancion
   12, Toy Story, arr. Megan Harper, Do mayor, 4/4). Mismo arreglo
   compartido con Julia, pero con enfoque propio y distinto: los
   acordes prestados -- el bajo se aleja de la tonalidad y vuelve.
   Nivel basico pero solido, tono adulto."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · HAY UN AMIGO EN MÍ'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
SIb = ['Bb2', 'D3', 'F3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, "You've Got a Friend in Me, de Toy Story, en Do mayor. Hoy: los acordes que se alejan y vuelven.")
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Localiza el Do central como punto de referencia.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los acordes prestados: el bajo se aleja y vuelve', 2,
                          'Lo que trabajamos hoy. El bajo se mueve a veces a un acorde con una nota alterada, fuera de Do mayor, y después regresa a casa: un "acorde prestado".')
    y -= 9
    ev2a = [{'pitches': DO, 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de casa: Do mayor', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': SIb, 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde prestado: Sib mayor, con su Sib bemol', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'C5']]
    bass2c = [{'pitches': SIb, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde prestado de Sib', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: siente cómo el acorde prestado da color antes de volver a casa.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · de Do al acorde prestado de Sib', 2,
                          'La izquierda toca el acorde de casa y luego el prestado; la derecha canta la melodía sin detenerse.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5']] + [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'C5']]
    bass1 = [{'pitches': DO, 'dur': 'w'}, {'pitches': SIb, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) De Do al acorde prestado de Sib, y vuelta', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía sobre el acorde de casa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el color prestado no descoloca la melodía', 3,
                          'La izquierda sostiene el acorde prestado sin dudar; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4']]
    bass3 = [{'pitches': SIb, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre el acorde prestado de Sib; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · You\'ve Got a Friend in Me casi entera', 3,
                          'Con la partitura al lado: siente cómo el acorde prestado da color antes de volver a casa.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'C5']])
    bass5 = [{'pitches': DO, 'dur': 'w'}, {'pitches': SIb, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, "You've Got a Friend in Me casi completa · con el acorde prestado", grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
