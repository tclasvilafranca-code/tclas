# -*- coding: utf-8 -*-
"""Taller de practica - Writing's on the Wall (Eva, cancion 9, Fa mayor, 4/4).
   Mismo arreglo que el de Dilan (que trabaja matices y el toque cromatico),
   pero enfoque DISTINTO para Eva: los ACORDES AMPLIOS. La partitura real de
   este tema de Bond usa acordes que abren la mano mas de lo habitual -- el
   reto es extenderla sin tension."""
from page_layout_common import *

SONG_KICKER = 'EVA · ENERO · WRITING’S ON THE WALL (SAM SMITH)'
TS = (4, 4)

FA = ['F2', 'A2', 'C3', 'F3']
SIB = ['Bb2', 'D3', 'F3', 'Bb3']
DO = ['C2', 'E3', 'G3', 'C4']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de James Bond en Fa mayor. El reto: acordes amplios que abren la mano sin tensión.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca la tecla negra Sib.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos amplios por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('C5', 5), ('A4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Acordes amplios: extender la mano sin tensión', 2,
                          'La dificultad exacta de esta canción. El acorde abarca una octava entera — estírate desde la muñeca, no fuerces los dedos.')
    y -= 9
    ev2a = [{'pitches': FA, 'dur': 'h'}, {'pitches': SIB, 'dur': 'h'}, {'pitches': DO, 'dur': 'h'}, {'pitches': FA, 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'a) Acordes de octava completa, uno por compás', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['F3', 'F4', 'A3', 'A4', 'C4', 'C5', 'F3', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Salto de octava dentro del acorde, relajando la muñeca', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitches': FA, 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'c) Aguanta el acorde amplio una redonda entera, sin tensión', ev2c, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad, aquí en posición cerrada.')
    y -= 9
    pattern_a = [(['F3', 'A3', 'C4'], 'Fa'), (['Bb2', 'D3', 'F3'], 'Sib'),
                 (['C3', 'E3', 'G3'], 'Do'), (['F3', 'A3', 'C4'], 'Fa')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitch': p, 'dur': 'q', 'label': l} for p, l in
                 [('F2', 'Fa'), ('A3', None), ('C4', None), ('Bb2', 'Sib'), ('D4', None), ('F4', None),
                  ('C3', 'Do'), ('E3', None), ('G3', None), ('F2', 'Fa'), ('A3', None), ('C4', None)]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, arpegiados nota a nota', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: los acordes amplios de la izquierda sostienen la melodía de la derecha.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · acordes amplios bajo la melodía', 2,
                          'La izquierda abre bien la mano para el acorde de octava; la derecha canta encima, relajada.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['C5', 'Bb4', 'A4', 'F4']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [FA, SIB, DO, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Acordes amplios sosteniendo la frase', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'Bb4', 'A4', 'F4', 'A4', 'C5', 'Bb4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando su forma', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la mano abierta no se cierra', 3,
                          'La izquierda mantiene el acorde amplio sin cerrar la mano; la derecha se mueve libre encima.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['A4', 'C5', 'Bb4', 'A4'] * 2)]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [FA, SIB]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde amplio no se mueve; la melodía sí', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4', 'Bb4', 'D5', 'C5', 'Bb4', 'A4', 'C5', 'F4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía en un registro más agudo', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Writing’s on the Wall casi entera', 3,
                          'Con la partitura al lado: abre la mano para cada acorde amplio sin perder la relajación de la muñeca.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'h'} for p in ['C5', 'Bb4', 'A4', 'F4', 'C5', 'Bb4', 'A4', 'F4']]
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [FA, SIB, DO, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Balada ♩≈88, con amplitud', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
