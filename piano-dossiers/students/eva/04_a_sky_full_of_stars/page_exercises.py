# -*- coding: utf-8 -*-
"""Taller de practica - A Sky Full of Stars (Eva, cancion 4, Fa mayor, 4/4).
   Mismo arreglo que el de Dilan (que trabaja el pulso largo-corto), pero
   enfoque DISTINTO para Eva: los ACORDES MARCADOS Y REPETIDOS. La cancion
   real vive de acordes que golpean con firmeza sobre el mismo pulso -- el
   reto es mantenerlos exactamente iguales de fuertes, sin acelerar."""
from page_layout_common import *

SONG_KICKER = 'EVA · OCTUBRE · A SKY FULL OF STARS (COLDPLAY)'
TS = (4, 4)

FA = ['F3', 'A3', 'C4']
SIB = ['Bb3', 'D4', 'F4']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un himno pop en Fa mayor, con el Sib. El reto: acordes marcados y repetidos, sin acelerar nunca.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca la tecla negra Sib.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('A4', 3), ('G4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sintiendo el Sib', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('C5', 5), ('A4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Acordes marcados y repetidos, sin acelerar', 2,
                          'La dificultad exacta de esta canción. Los acordes golpean con firmeza sobre el mismo pulso — el reto es que la décima repetición suene exactamente igual que la primera.')
    y -= 9
    ev2a = [{'pitches': FA, 'dur': 'q'}] * 8
    y = system_block(c, x0, w0, y, gap, 'a) El mismo acorde, ocho veces, sin cambiar de fuerza', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'q'} for p in [FA, FA, SIB, SIB, DO, DO, FA, FA]]
    y = system_block(c, x0, w0, y, gap, 'b) Fa-Fa-Sib-Sib-Do-Do-Fa-Fa, marcado y regular', ev2b, clef='bass', time_sig=TS)

    ev2c = [{'pitches': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate([FA, FA, SIB, SIB, DO, DO, FA, FA] * 2)]
    y = system_block(c, x0, w0, y, gap, 'c) Los mismos acordes, ahora al doble de rápido', ev2c, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad.')
    y -= 9
    pattern_a = [(FA, 'Fa'), (SIB, 'Sib'), (DO, 'Do'), (FA, 'Fa')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [('F2', 'Fa'), ('A3', None), ('C4', None), ('Bb2', 'Sib'), ('D4', None), ('F4', None),
                 ('C3', 'Do'), ('E3', None), ('G3', None), ('F2', 'Fa'), ('A3', None), ('C4', None)]
    evb = [{'pitch': p, 'dur': 'q', 'label': l} for p, l in pattern_b]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, arpegiados nota a nota', evb, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: los acordes marcan el pulso mientras la melodía se mueve encima.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el pulso firme, la melodía encima', 2,
                          'La izquierda marca los acordes exactamente igual de fuertes; la derecha canta la melodía sin arrastrar el tempo.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4', 'F4', 'A4', 'C5', 'A4']]
    bass1 = [{'pitches': p, 'dur': 'q'} for p in [FA, FA, FA, FA, SIB, SIB, SIB, SIB]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El acorde marca, la melodía respira encima', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'Bb4', 'A4', 'G4', 'F4', 'G4', 'A4', 'Bb4', 'C5', 'A4', 'F4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando el pulso exacto', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Precisión rítmica · los acordes cambian más rápido', 3,
                          'Los acordes cambian dos veces por compás en vez de una — la mano izquierda no puede dudar ni un instante.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'Bb4', 'A4', 'G4', 'A4', 'Bb4', 'C5']]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [FA, SIB, DO, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Los acordes cambian cada dos tiempos', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['F4', 'A4', 'G4', 'Bb4', 'A4', 'C5', 'Bb4', 'A4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía en corcheas, más viva', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · el estribillo casi entero', 3,
                          'Con la partitura al lado: deja que los acordes sean el metrónomo de la canción, firmes de principio a fin.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['F4', 'A4', 'C5', 'A4', 'F4', 'A4', 'C5', 'A4', 'Bb4', 'D5', 'C5', 'Bb4', 'A4', 'C5', 'Bb4', 'A4']]
    bass5 = [{'pitches': p, 'dur': 'q'} for p in
             [FA, FA, FA, FA, SIB, SIB, SIB, SIB, SIB, SIB, SIB, SIB, DO, DO, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈100, firme y regular', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
