# -*- coding: utf-8 -*-
"""Taller de practica - Counting Stars (Jose Maria, cancion 2, Do
   mayor, 4/4). Distinto del angulo de Josep (la sincopa): aqui,
   alumno que va a su ritmo, el foco es la nota larga que sostiene
   -- la izquierda aguanta sin soltar mientras la derecha se mueve
   tranquila encima."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · SEPTIEMBRE · COUNTING STARS (ONEREPUBLIC)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de OneRepublic en Do mayor. Aquí, la izquierda aguanta una nota larga sin soltar.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas, sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('G4', 5), ('E4', 3), ('G4', 5)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La nota larga que sostiene, sin soltar', 2,
                          'Lo que vamos a cuidar en esta canción. La izquierda toca una sola nota larga y la deja sonar entera, sin volver a tocarla, mientras la derecha se mueve tranquila encima.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) La melodía, tranquila y sin prisa', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'w'} for p in ['C3', 'C3']]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: una nota larga por compás entero, sin soltar', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4']]
    bass2c = [{'pitch': p, 'dur': 'w'} for p in ['C3', 'F2']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, cada una a su aire', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, sin prisa.')
    y -= 11
    pattern_a = [(DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (SOL, 'Sol')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: la izquierda sostiene y la derecha canta encima.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la nota que sostiene todo el compás', 2,
                          'La izquierda toca su nota larga y la deja vivir; la derecha canta la melodía encima, sin que ninguna se apresure.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'C4', 'D4', 'E4', 'E4', 'D4', 'C4', 'C4']]
    bass1 = [{'pitch': p, 'dur': 'w'} for p in ['C3', 'F2']]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre la nota que aguanta', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para irla conociendo', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la nota larga no se contagia', 3,
                          'La izquierda se queda quieta con su nota sostenida; la derecha se mueve un poco más, tranquila también.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F4', 'E4', 'D4', 'C4', 'D4', 'E4', 'C4']]
    bass3 = [{'pitch': p, 'dur': 'w'} for p in ['G2', 'C3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda no se mueve; la derecha canta libre', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'D4', 'F4', 'E4', 'G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, con saltos tranquilos', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Counting Stars casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que la nota larga de la izquierda suene entera cada vez.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4', 'D4', 'C4', 'C4', 'C4']]
    bass5 = [{'pitch': p, 'dur': 'w'} for p in ['C3', 'F2', 'G2', 'C3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈120, sin prisa', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
