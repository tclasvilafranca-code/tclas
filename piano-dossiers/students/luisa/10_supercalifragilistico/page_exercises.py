# -*- coding: utf-8 -*-
"""Taller de practica - Supercalifragilisticoespialidoso (Luisa,
   cancion 10, Mary Poppins, Do mayor -> Fa mayor, 4/4). Nivel
   hobby, sin complicaciones: la palabra larguisima -- solo hay
   que disfrutarla, sin agobios."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · SUPERCALIFRAGILISTICOESPIALIDOSO'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
SIb = ['Bb2', 'D3', 'F3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La canción de Mary Poppins, en Do mayor. Hoy: disfrutar de la palabra larguísima, sin agobios.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La palabra larguísima: solo hay que disfrutarla', 2,
                          'Lo de hoy. A mitad de canción el sonido cambia un poco, hacia una "casa" nueva: no te agobies, solo disfruta la melodía alegre.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'E4', 'G4', 'D4', 'C4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase alegre, tranquila', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'A4', 'C5', 'G4', 'F4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, en la casa nueva: sin agobiarte', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'G4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase alegre sobre el acorde de Do, tranquilo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes, sin más complicación.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: disfruta de la canción en sus dos "casas".')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase alegre sobre el acorde de Sol', 2,
                          'La izquierda sostiene el acorde entero, tranquila; la derecha canta encima, alegre.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'D5', 'B4', 'A4', 'G4', 'A4']]
    bass1 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase alegre sobre Sol, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G5', 'D5', 'B4', 'G4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Otra variación de la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · sin agobios, en la casa nueva', 3,
                          'La izquierda sostiene el nuevo acorde, tranquila; la derecha canta ya en la casa nueva, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'F5', 'D5', 'C5', 'Bb4', 'C5']]
    bass3 = [{'pitches': SIb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase en la casa nueva de Fa, tranquila', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'Bb5', 'F5', 'D5', 'Bb4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en la casa de Fa', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Supercalifragilisticoespialidoso casi entera', 3,
                          'Con la partitura al lado: sin agobios, disfruta de la palabra larguísima hasta el final.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'E4', 'G4', 'D4', 'C4', 'D4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'A4', 'C5', 'G4', 'F4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Supercalifragilisticoespialidoso casi completa · sin agobios', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
