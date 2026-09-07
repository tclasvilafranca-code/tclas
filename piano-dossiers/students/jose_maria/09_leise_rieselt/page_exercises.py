# -*- coding: utf-8 -*-
"""Taller de practica - Leise rieselt der Schnee (Jose Maria, cancion
   9, Do mayor, 3/4, a 4 manos). Tono relajado: notas largas que se
   sostienen varios compases sin volver a tocarlas, dejando que el
   sonido se apague solo -- como copos de nieve cayendo despacio."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · DICIEMBRE · LEISE RIESELT DER SCHNEE (A 4 MANOS)'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un villancico alemán tranquilo en Do mayor, a 4 manos. Las notas se sostienen sin volver a tocarlas.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas, sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('C4', 1), ('D4', 2), ('E4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La nota que se sostiene, sin volver a tocarla', 2,
                          'Lo que vamos a cuidar en esta pieza. Una nota larga dura varios compases — apóyala una vez y déjala apagarse sola, como un copo de nieve que cae despacio.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h.'} for p in ['E4', 'D4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'a) Notas largas: apoya y deja que se apaguen solas', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'G3', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: el mismo cuidado, sin prisa', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'E4', 'C4']]
    bass2c = [{'pitches': p, 'dur': 'h.'} for p in [DO, FA, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, sosteniendo cada una su nota', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, sin prisa.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: cada nota larga se sostiene mientras la otra se mueve despacio.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la nota que se sostiene sobre el acorde', 2,
                          'La izquierda toca su acorde y lo deja sonar; la derecha sostiene su nota larga encima, sin volver a tocarla.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'E4', 'C4']]
    bass1 = [{'pitches': p, 'dur': 'h.'} for p in [DO, FA, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La nota larga sobre el acorde sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'G4', 'E4', 'D4', 'C4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para irla conociendo', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · una mano sostiene, la otra se mueve', 3,
                          'La izquierda sostiene su nota larga sin moverse; la derecha canta despacio encima, sin que ninguna se apresure.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4']]
    bass3 = [{'pitch': p, 'dur': 'h.'} for p in ['C3', 'F2', 'C3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda sostiene; la derecha canta libre', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5', 'G4', 'E4', 'D4', 'E4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, con saltos tranquilos', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Leise rieselt der Schnee casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que cada nota larga se apague sola, como la nieve que cae.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'h.'} for p in ['E4', 'D4', 'C4', 'G4', 'E4', 'C4']]
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [DO, SOL, DO, FA, SOL, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · piano, muy tranquila', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
