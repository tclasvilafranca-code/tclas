# -*- coding: utf-8 -*-
"""Taller de practica - America (My Country 'Tis of Thee) (Jose
   Maria, cancion 3, Do mayor, 3/4). Tono relajado: el compas de vals
   solemne, contando tres tiempos iguales sin apresurar ninguno."""
from page_layout_common import *

SONG_KICKER = "JOSÉ MARÍA · OCTUBRE · AMERICA (MY COUNTRY 'TIS OF THEE)"
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un himno tranquilo en Do mayor. Aquí cuidamos que los tres tiempos del compás suenen igual de firmes.')
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

    y = exercise_heading(c, y, 2, 'Los tres tiempos, igual de firmes', 2,
                          'Lo que vamos a cuidar en esta canción. En un compás de 3/4 es fácil que el segundo o el tercer tiempo se apresuren — cuenta despacio y deja que los tres pesen igual.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'C5', 'G4', 'E4', 'D4', 'E4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'a) La melodía, contando los tres tiempos por dentro', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'G3', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: una nota que ocupa el compás entero', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'C5', 'G4', 'E4', 'D4', 'E4', 'F4']]
    bass2c = [{'pitch': p, 'dur': 'h.'} for p in ['C3', 'G2', 'C3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, cada una a su aire', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: los tres tiempos del compás, siempre igual de firmes.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · los tres tiempos parejos', 2,
                          'La izquierda marca el compás con una nota larga; la derecha canta la melodía sintiendo los tres tiempos igual de firmes.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'C4', 'D4', 'E4', 'F4', 'G4', 'C5']]
    bass1 = [{'pitch': p, 'dur': 'h.'} for p in ['C3', 'C3', 'F2']]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre el compás firme', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'G4', 'E4', 'D4', 'E4', 'F4', 'G4', 'C5', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para irla conociendo', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el compás no se acelera', 3,
                          'La izquierda mantiene su nota larga sin cambiar de ritmo; la derecha se mueve tranquila, contando siempre tres.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'E4', 'D4', 'C4', 'D4', 'E4', 'F4', 'G4', 'E4']]
    bass3 = [{'pitch': p, 'dur': 'h.'} for p in ['G2', 'C3', 'G2']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda firme; la derecha canta libre', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C4', 'E4', 'G4', 'F4', 'A4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, con saltos tranquilos', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · America casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que los tres tiempos de cada compás suenen igual de firmes.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['E4', 'F4', 'G4', 'C5', 'G4', 'E4', 'D4', 'E4', 'F4', 'C5', 'G4', 'E4', 'D4', 'E4', 'F4', 'G4', 'C5', 'G4']]
    bass5 = [{'pitch': p, 'dur': 'h.'} for p in ['C3', 'G2', 'C3', 'F2', 'G2', 'C3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · sin prisa, con firmeza tranquila', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
