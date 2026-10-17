# -*- coding: utf-8 -*-
"""Taller de practica - Titanic, Mi Corazon Sigue (Luisa, cancion 16,
   James Horner, Do mayor, 2/4). Nivel hobby, sin complicaciones: la
   cancion del mar -- despacio, con calma."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · TITANIC'
TS = (2, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Titanic (Mi corazón sigue), de James Horner, en Do mayor. Hoy: la canción del mar, despacio.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La canción del mar: despacio, con calma', 2,
                          'Lo de hoy. Esta melodía es tranquila y un poco soñadora, como el mar: no hay que complicarse, solo tocarla despacio y con calma.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5', 'G4', 'E4', 'D4', 'E4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'a) La melodía tranquila, con calma', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5', 'G4', 'E4', 'D4', 'E4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, muy despacio: sin prisa', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4']]
    bass2c = [{'pitches': DO, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde de Do, tranquila', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes, sin más complicación.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: deja que la melodía flote, tranquila como el mar.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde de Fa, tranquila; la derecha canta encima, con calma.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Fa, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · sin agobios, cada mano tranquila', 3,
                          'La izquierda sostiene su acorde de Sol sin moverse; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Titanic casi entera', 3,
                          'Con la partitura al lado: disfruta, sin agobios, esta melodía tranquila del mar.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4']])
    bass5 = [{'pitches': DO, 'dur': 'h'}, {'pitches': FA, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Titanic casi completa · tranquila, sin agobios', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
