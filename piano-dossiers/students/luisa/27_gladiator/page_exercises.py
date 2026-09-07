# -*- coding: utf-8 -*-
"""Taller de practica - Honor Him / Gladiator (Luisa, cancion 27,
   Hans Zimmer, arreglo facil verificado en Re mayor -- 2
   sostenidos, F# y C#, mismo archivo que el de Julia y Merce --
   3/4). Nivel hobby, sin complicaciones: una melodia heroica --
   sientete valiente."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · GLADIATOR (HONOR HIM)'
TS = (3, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['A2', 'C#3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de Gladiator, de Hans Zimmer, en Re mayor. Hoy: una melodía heroica, siéntete valiente.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El Fa# es la primera tecla negra de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('F#4', 3), ('E4', 2), ('D4', 1), ('E4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Una melodía heroica: siéntete valiente', 2,
                          'Lo de hoy. Esta melodía suena grande y valiente, como una hazaña: no hay que complicarse, solo tocarla sintiéndote fuerte por dentro.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'D5', 'A4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'a) La melodía valiente, con seguridad', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'D5', 'A4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, muy despacio: sintiéndote valiente', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4']]
    bass2c = [{'pitches': RE, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde de Re, firme', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La-Re, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: siéntete valiente mientras tocas esta melodía.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde de Sol', 2,
                          'La izquierda sostiene el acorde de Sol, tranquila; la derecha canta encima, con valentía.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G5', 'D5', 'B4']]
    bass1 = [{'pitches': SOL, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Sol, valiente', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G5', 'D5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · sin agobios, cada mano tranquila', 3,
                          'La izquierda sostiene su acorde de La sin moverse; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C#5', 'E5', 'A5', 'E5', 'C#5']]
    bass3 = [{'pitches': LA, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre La; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'A4', 'D5', 'A4', 'F#4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Gladiator casi entera', 3,
                          'Con la partitura al lado: disfruta esta melodía heroica, sintiéndote valiente, sin agobios.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'D5', 'A4', 'F#4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G5', 'D5', 'B4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [RE, RE, SOL, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Gladiator casi completa · valiente, sin agobios', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
