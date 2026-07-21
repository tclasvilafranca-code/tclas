# -*- coding: utf-8 -*-
"""Taller de practica - Shallow (Jose Maria, cancion 15, Sol mayor,
   4/4). Enfoque relajado: el crecimiento lento -- de piano a
   forte, sin prisa por llegar, dejando que el sonido crezca solo."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · MARZO · SHALLOW (LADY GAGA & BRADLEY COOPER)'
TS = (4, 4)

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D3', 'F#3', 'A3']
Em = ['E2', 'G2', 'B2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de "A Star Is Born" en Sol mayor. Sin prisa: el sonido crece poco a poco.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El crecimiento lento: de piano a forte, sin prisa', 2,
                          'Lo que vamos a cuidar en esta pieza. El sonido crece poco a poco, de suave a fuerte, sin ningún salto brusco — deja que crezca solo, sin empujarlo.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'B4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase que crece, nota a nota', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, más movida: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'B4', 'D5']]
    bass2c = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase que crece sobre el acorde de Sol, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Sol–Re–Mim–Do: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (RE, 'Re'), (Em, 'Mim'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Re-Mim-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el sonido crece mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el crecimiento sobre el acorde de Re', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha deja crecer el sonido poco a poco.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['D4', 'E4', 'F#4', 'A4']]
    bass1 = [{'pitches': RE, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El crecimiento sobre Re, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del crecimiento', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha crece despacio, sin que ninguna se apresure.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'F#4', 'G4', 'B4']]
    bass3 = [{'pitches': Em, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El crecimiento sobre Mim; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F#4', 'G4', 'A4', 'B4', 'A4', 'G4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un poco más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Shallow casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que el sonido crezca poco a poco, sobre un acorde que no se mueve.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'B4', 'D5']] +
             [{'pitch': p, 'dur': 'h'} for p in ['D4', 'E4', 'F#4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [SOL, SOL, RE, RE]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con el sonido creciendo poco a poco', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
