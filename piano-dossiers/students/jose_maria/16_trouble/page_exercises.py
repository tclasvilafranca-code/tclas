# -*- coding: utf-8 -*-
"""Taller de practica - Trouble (Jose Maria, cancion 16, Sol mayor,
   4/4). Enfoque relajado: la anacrusa que respira -- la frase
   empieza un poco antes del primer tiempo fuerte, con calma, sin
   adelantarse de golpe."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · MARZO · TROUBLE (COLDPLAY)'
TS = (4, 4)

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D3', 'F#3', 'A3']
Em = ['E2', 'G2', 'B2']
Bm = ['B2', 'D3', 'F#3']
FA_NAT = ['F2', 'A2', 'C3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Coldplay en Sol mayor. Sin prisa: la frase empieza un poco antes, con calma.')
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

    y = exercise_heading(c, y, 2, 'La anacrusa que respira: empieza un poco antes, con calma', 2,
                          'Lo que vamos a cuidar en esta pieza. La frase empieza justo antes del primer tiempo fuerte — sin adelantarse de golpe, solo un pequeño impulso tranquilo.')
    y -= 9
    ev2a = [{'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'h'},
            {'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'a) La anacrusa, con su pequeño impulso tranquilo', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'G4', 'G4', 'A4', 'D4', 'A4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, empezando en el tiempo fuerte: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'h'},
              {'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'h'}]
    bass2c = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La anacrusa sobre el acorde de Sol, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Sol–Mim–Sim–Fa: los acordes reales de esta canción (el Fa es "prestado", fuera de la tonalidad, algo típico de Coldplay).')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (Em, 'Mim'), (Bm, 'Sim'), (FA_NAT, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Mim-Sim-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: la anacrusa respira mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la anacrusa sobre el acorde de Re', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha respira su pequeño impulso antes de cada frase.')
    y -= 7
    treb1 = [{'rest': True, 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'D5', 'dur': 'h'},
             {'rest': True, 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'E5', 'dur': 'h'}]
    bass1 = [{'pitches': RE, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La anacrusa sobre Re, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'D5', 'D5', 'E5', 'A4', 'E5', 'E5', 'F#5']]
    y = system_block(c, x0, w0, y, gap, 'b) Empezando en el tiempo fuerte: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia de la anacrusa', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha respira su impulso, sin que ninguna se apresure.')
    y -= 7
    treb3 = [{'rest': True, 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'h'},
             {'rest': True, 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'D5', 'dur': 'h'}]
    bass3 = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La anacrusa sobre Do; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'C5', 'C5', 'D5', 'G4', 'D5', 'D5', 'E5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, empezando en el tiempo fuerte', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Trouble casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que cada anacrusa respire antes de su frase.')
    y -= 7
    treb5 = ([{'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'h'},
              {'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'h'}] +
             [{'rest': True, 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'D5', 'dur': 'h'},
              {'rest': True, 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'E5', 'dur': 'h'}])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [SOL, SOL, RE, RE]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con la anacrusa respirando', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
