# -*- coding: utf-8 -*-
"""Taller de practica - El Condor Pasa (Sandi, cancion 5, trad.
   andina, Daniel Alomia Robles, arr. Peter Edvinsson, Re menor --
   armadura de 1 bemol, Sib, confirmada por render directo, 4/4).
   Nivel avanzado: el acompanamiento en corcheas repetidas -- firmeza
   sin rigidez, mano relajada."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · EL CÓNDOR PASA'
TS = (4, 4)

REm = ['D2', 'F2', 'A2']
FA = ['F2', 'A2', 'C3']
C7 = ['C2', 'E2', 'G2', 'Bb2']
A7 = ['A2', 'C#3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El Cóndor Pasa, melodía tradicional andina, en Re menor. Hoy: las corcheas repetidas, firmes sin rigidez.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re menor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa(3) Sol(4) La(5). El Sib es la única alteración de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('F4', 3), ('G4', 4), ('A4', 5), ('G4', 4), ('F4', 3), ('E4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido completo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'D5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El acompañamiento en corcheas repetidas: firmeza sin rigidez', 3,
                          'La dificultad de hoy. Repetir el mismo acorde en corcheas, compás tras compás, tienta a tensar la muñeca. El reto es mantener firmeza en el sonido sin que el brazo se agarrote: pequeños rebotes relajados, no golpes secos.')
    y -= 9
    ev2a = [{'pitches': FA, 'dur': 'e'}] * 8
    y = system_block(c, x0, w0, y, gap, 'a) El acorde de Fa repetido en corcheas: muñeca suelta, sonido firme', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': C7, 'dur': 'e'}] * 8
    y = system_block(c, x0, w0, y, gap, 'b) El mismo gesto sobre Do7: la séptima no debe tensar la mano', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'D5', 'F5']]
    bass2c = [{'pitches': REm, 'dur': 'e'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre las corcheas repetidas de Re menor', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V7 en Re menor', 2,
                          'Rem–Sol–La7 (o su variante A7): los acordes principales de esta tonalidad menor.')
    y -= 11
    pattern_a = [(REm, 'Rem'), (FA, 'Fa'), (A7, 'A7'), (REm, 'Rem')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Rem-Fa-A7-Rem, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: las corcheas repetidas deben sonar iguales entre sí, sin acentos accidentales.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre las corcheas repetidas de Fa', 3,
                          'La izquierda repite el acorde de Fa en corcheas, relajada; la derecha canta la melodía encima, sin dejarse arrastrar por el pulso de abajo.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F5', 'E5', 'F5', 'A5']]
    bass1 = [{'pitches': FA, 'dur': 'e'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Fa, con las corcheas repetidas debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F5', 'E5', 'F5', 'A5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar la independencia', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la séptima de Do7 no aprieta la mano', 3,
                          'La izquierda repite el acorde de Do7 en corcheas, relajada pese a la cuarta nota; la derecha no se contagia de ninguna tensión.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'C5', 'E5']]
    bass3 = [{'pitches': C7, 'dur': 'e'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre Do7; la mano izquierda se mantiene relajada', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en otro orden', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · El Cóndor Pasa casi entero', 3,
                          'Con la partitura al lado: las corcheas repetidas deben sonar firmes y regulares, con la muñeca siempre suelta.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'D5', 'F5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F5', 'E5', 'F5', 'A5']])
    bass5 = [{'pitches': REm, 'dur': 'e'}] * 8 + [{'pitches': FA, 'dur': 'e'}] * 8
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El Cóndor Pasa casi completo · corcheas firmes, muñeca relajada', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
