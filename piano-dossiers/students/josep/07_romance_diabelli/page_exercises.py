# -*- coding: utf-8 -*-
"""Taller de practica - Romance, Diabelli (Josep, cancion 7, Do
   mayor, 2/2, a 4 manos). Angulo: la MANO ESTACIONARIA -- toda la
   pieza se toca sin mover la mano de sitio, tal como esta pensada
   la parte Primo original."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · DICIEMBRE · ROMANCE (DIABELLI, A 4 MANOS)'
TS = (2, 2)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un romance de Diabelli en Do mayor, a 4 manos. El reto: no mover la mano de sitio en toda la pieza.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La mano estacionaria: ni un solo movimiento de sitio', 2,
                          'La dificultad exacta de esta pieza. Los cinco dedos se quedan siempre sobre las mismas cinco teclas — toda la música ocurre sin desplazar la mano.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('D4', 2), ('F4', 4), ('E4', 3), ('G4', 5), ('F4', 4), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Sin moverse: solo cambian los dedos, no la mano', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h', 'number': n} for p, n in
            [('G4', 5), ('C4', 1), ('F4', 4), ('D4', 2), ('E4', 3), ('C4', 1), ('D4', 2), ('C4', 1)]]
    y = system_block(c, x0, w0, y, gap, 'b) Saltos dentro de la misma posición fija', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h', 'number': n} for p, n in
              [('C4', 1), ('E4', 3), ('D4', 2), ('F4', 4), ('E4', 3), ('G4', 5), ('F4', 4), ('D4', 2)]]
    bass2c = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Con el Secondo debajo, quieto también', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, la parte del Secondo.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (FA, 'Fa')] * 2
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Fa, un acorde por blanca', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la posición fija del Primo sobre el Secondo, sin moverse.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la posición fija sobre el Secondo', 2,
                          'La derecha se queda anclada en su posición de cinco dedos; la izquierda (o tu compañera) sostiene el acorde debajo.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h', 'number': n} for p, n in
             [('E4', 3), ('G4', 5), ('F4', 4), ('D4', 2), ('C4', 1), ('E4', 3), ('D4', 2), ('C4', 1)]]
    bass1 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía anclada, sobre el acorde de Do', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin moverse de la posición', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la posición aguanta aunque el Secondo se mueva', 3,
                          'El Secondo cambia de acorde debajo; la mano derecha no se mueve ni un centímetro de su posición fija.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h', 'number': n} for p, n in
             [('G4', 5), ('E4', 3), ('F4', 4), ('D4', 2), ('E4', 3), ('C4', 1), ('D4', 2), ('C4', 1)]]
    bass3 = [{'pitches': p, 'dur': 'w'} for p in [FA, SOL, FA, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El Secondo se mueve; el Primo no cambia de sitio', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'F4', 'E4', 'D4', 'C4', 'D4', 'E4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma posición, otro orden', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Romance casi entero', 3,
                          'Con la partitura al lado: comprueba al terminar que tu mano derecha no se movió de sitio ni una vez.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'h', 'number': n} for p, n in
             [('C4', 1), ('E4', 3), ('D4', 2), ('F4', 4), ('E4', 3), ('G4', 5), ('F4', 4), ('D4', 2),
              ('E4', 3), ('C4', 1), ('D4', 2), ('C4', 1), ('G4', 5), ('E4', 3), ('F4', 4), ('D4', 2)]]
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, SOL, DO, DO, FA, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El romance casi completo · alla breve, sin moverse', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
