# -*- coding: utf-8 -*-
"""Taller de practica - Arabesque (Eva, cancion 10, Burgmuller Op.100 a 4
   manos, Do mayor, 2/4). Mismo arreglo que el de Dilan (que trabaja el
   dialogo a duo), pero enfoque DISTINTO para Eva: la REGULARIDAD del giro
   rapido -- un estudio tecnico de igualdad de dedos, nota a nota, sin
   depender de otra persona."""
from page_layout_common import *

SONG_KICKER = 'EVA · FEBRERO · ARABESQUE (BURGMÜLLER, A 4 MANOS)'
TS = (2, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un estudio clásico a cuatro manos, en Do mayor. El reto: la regularidad exacta del giro rápido.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, con soltura', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El giro exacto: cada nota igual de fuerte', 2,
                          'La dificultad exacta de esta canción. El giro rápido de cuatro notas tiene que sonar perfectamente regular — ninguna nota más marcada que las demás.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'D4', 'C4', 'D4'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'a) Muy despacio: el giro, contando cada nota', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'D4', 'C4', 'D4'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'b) Un poco más rápido, sin perder la regularidad', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['G4', 'F4', 'E4', 'F4'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'c) El mismo giro, un escalón más arriba', ev2c, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
    y -= 9
    pattern_a = [(DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (DO, 'Do')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Sol-Fa-Do, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas tranquilas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el giro regular de la derecha sobre los acordes de la izquierda.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el giro regular sobre el acorde', 2,
                          'La izquierda sostiene el acorde sin moverse; la derecha gira con precisión de metrónomo, sin acelerar ni frenar.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'D4', 'C4', 'D4'] * 4)]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [DO, DO, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El giro regular, acorde firme debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['G4', 'F4', 'E4', 'F4'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) Solo el giro, memorizando la regularidad exacta', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Precisión · el giro con acordes que cambian', 3,
                          'Ahora el acorde cambia mientras el giro sigue regular — la izquierda no puede distraer a la derecha.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'D4', 'C4', 'D4'] * 4)]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde cambia; el giro no pierde su regularidad', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la escala completa, tranquila', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Arabesque casi entero', 3,
                          'Con la partitura al lado: mantén el giro perfectamente regular de principio a fin, como un estudio de verdad.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(
             ['E4', 'D4', 'C4', 'D4'] * 4 + ['G4', 'F4', 'E4', 'F4'] * 4)]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [DO, DO, DO, DO, FA, FA, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · Allegretto ♩≈108, muy regular', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
