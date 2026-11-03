# -*- coding: utf-8 -*-
"""Taller de practica - Someone You Loved (Jose Maria, cancion 5, Do
   mayor, 4/4). Enfoque relajado: un acompanamiento de la izquierda
   que fluye sin detenerse (balanceo), mientras la derecha sostiene
   la melodia con calma."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · NOVIEMBRE · SOMEONE YOU LOVED (LEWIS CAPALDI)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
Am = ['A2', 'C3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Lewis Capaldi en Do mayor. Sin prisa: la izquierda balancea sin parar.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas, sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El balanceo: el acompañamiento que no se detiene', 2,
                          'Lo que vamos a cuidar en esta pieza. La izquierda mece un dibujo que no para nunca, tranquilo y constante, como un balanceo suave.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e'} for p in ['C3', 'E3', 'G3', 'E3'] * 4]
    y = system_block(c, x0, w0, y, gap, 'a) El balanceo solo, sin parar', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h'} for p in ['C5', 'B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La melodía sola, para irla conociendo', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['C5', 'B4', 'A4', 'G4']]
    bass2c = [{'pitch': p, 'dur': 'e'} for p in ['C3', 'E3', 'G3', 'E3'] * 4]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sostenida sobre el balanceo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Do–Sol–Lam–Fa: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(DO, 'Do'), (SOL, 'Sol'), (Am, 'Lam'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Sol-Lam-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el balanceo fluye mientras la melodía se sostiene.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el balanceo de Fa', 2,
                          'La izquierda mece su acompañamiento sin detenerse; la derecha sostiene la melodía tranquila encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['F4', 'E4', 'D4', 'C4']]
    bass1 = [{'pitch': p, 'dur': 'e'} for p in ['F2', 'A2', 'C3', 'A2'] * 4]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El balanceo de Fa, sin detenerse', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el balanceo no se contagia de la melodía', 3,
                          'La izquierda mece su balanceo constante; la derecha canta despacio encima, sin que ninguna se apresure.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'B4', 'C5']]
    bass3 = [{'pitch': p, 'dur': 'e'} for p in ['G2', 'B2', 'D3', 'B2'] * 4]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El balanceo de Sol; la melodía canta libre', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'D4', 'E4', 'F4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un poco más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Someone You Loved casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que el balanceo fluya solo mientras la melodía se sostiene encima.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'h'} for p in ['C5', 'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4']]
    bass5 = ([{'pitch': p, 'dur': 'e'} for p in ['C3', 'E3', 'G3', 'E3'] * 4] +
             [{'pitch': p, 'dur': 'e'} for p in ['F2', 'A2', 'C3', 'A2'] * 4])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · balada, con el balanceo fluyendo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
