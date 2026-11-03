# -*- coding: utf-8 -*-
"""Taller de practica - Para Elisa (Luisa, cancion 22, Beethoven,
   version facil, La menor, 3/4). Nivel hobby, sin complicaciones:
   la melodia mas famosa -- tocala sin miedo."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · PARA ELISA'
TS = (3, 4)

LAm = ['A2', 'C3', 'E3']
SOL = ['G2', 'B2', 'D3']
FA = ['F2', 'A2', 'C3']
MI = ['E2', 'G#2', 'B2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Para Elisa, de Beethoven (versión fácil), en La menor. Hoy: la melodía más famosa, sin miedo.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Todas teclas blancas: La menor es el relativo de Do mayor.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2), ('A4', 1), ('B4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La melodía más famosa: tócala sin miedo', 2,
                          'Lo de hoy. Es una de las melodías más conocidas del mundo, pero no hay que ponerse nerviosa: tócala tranquila, a tu ritmo.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'E5', 'B4', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'a) El comienzo, tranquilo, sin prisa', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'E5', 'B4', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, muy despacio: para no agobiarse', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'E5']]
    bass2c = [{'pitches': LAm, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El comienzo sobre el acorde de La menor, tranquilo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'La progresión Am-E-Am en La menor', 2,
                          'Am–E–Am: los acordes principales de esta pieza, sin más complicación.')
    y -= 11
    pattern_a = [(LAm, 'Am'), (MI, 'E'), (LAm, 'Am')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Am-E-Am, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: disfruta tocando esta melodía tan conocida.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el comienzo sobre el acorde de Sol', 2,
                          'La izquierda sostiene el acorde de Sol, tranquila; la derecha canta encima, sin prisa.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'B4', 'D5']]
    bass1 = [{'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Sol, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'B4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · sin agobios, cada mano tranquila', 3,
                          'La izquierda sostiene su acorde de Fa sin moverse; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'A4', 'C5']]
    bass3 = [{'pitches': FA, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre Fa; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Para Elisa casi entera', 3,
                          'Con la partitura al lado: disfruta esta melodía tan famosa, sin agobios.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'E5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['B4', 'D5', 'C5']])
    bass5 = [{'pitches': LAm, 'dur': 'h.'}, {'pitches': MI, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Para Elisa casi completa · sin miedo, sin agobios', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
