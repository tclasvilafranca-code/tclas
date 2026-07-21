# -*- coding: utf-8 -*-
"""Taller de practica - Si tu no estas aqui (Josep, cancion 14, Do
   mayor, compas mixto 4/4<->2/4). Enfoque: el acento que se
   desplaza -- el pulso fuerte cambia de sitio segun el compas."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · ABRIL · SI TÚ NO ESTÁS AQUÍ (ROSANA)'
TS44 = (4, 4)
TS24 = (2, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
Am = ['A2', 'C3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Rosana en Do mayor. El reto: el acento se desplaza entre 4/4 y 2/4.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición', ev1a, clef='treble', time_sig=TS44)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS44)
    y -= 3

    y = exercise_heading(c, y, 2, 'El acento que se desplaza', 2,
                          'La dificultad exacta de esta canción. Cuando el compás cambia de 4/4 a 2/4, el acento fuerte cae en un sitio distinto — hay que sentirlo, no solo contarlo.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase en 4/4: el acento cae en el 1', ev2a, clef='treble', time_sig=TS44)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, en 2/4: el acento cambia de sitio', ev2b, clef='treble', time_sig=TS24)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4', 'D4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase en 4/4 sobre el acorde de Do, sostenido entero', grand_gap_mult=7.3, time_sig=TS44)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Do–Lam–Fa–Sol: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(DO, 'Do'), (Am, 'Lam'), (FA, 'Fa'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Lam-Fa-Sol, un acorde por compás entero', eva, clef='bass', time_sig=TS44)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, en los dos compases: siente dónde cae el acento cada vez.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · en 4/4, sobre el acorde de Lam', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta la frase en 4/4, con el acento en el primer tiempo.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4']]
    bass1 = [{'pitches': Am, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase en 4/4 sobre Lam, sostenido entero', grand_gap_mult=7.3, time_sig=TS44)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'B4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, en 4/4: para comparar', treb2, clef='treble', time_sig=TS44)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · en 2/4, con el acento en su nuevo sitio', 3,
                          'La izquierda sostiene su acorde con negras firmes en 2/4; la derecha canta, sintiendo dónde cae ahora el acento.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F4', 'E4', 'F4']]
    bass3 = [{'pitches': SOL, 'dur': 'h'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase en 2/4; el acorde de Sol marca el nuevo acento', grand_gap_mult=7.3, time_sig=TS24)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, en 2/4', treb4, clef='treble', time_sig=TS24)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Si tú no estás aquí casi entera', 3,
                          'Con la partitura al lado: recuerda que en la canción real el acento sigue desplazándose — aquí lo trabajamos en 4/4.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4', 'D4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, Am, Am]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · en 4/4, sintiendo el acento', grand_gap_mult=7.3, time_sig=TS44)

    exercises_footer(c, 4)
    c.showPage()
