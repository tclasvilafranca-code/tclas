# -*- coding: utf-8 -*-
"""Taller de practica - Honor Him / Gladiator (Merce, cancion 11,
   Hans Zimmer, arreglo facil verificado en Re mayor -- 2
   sostenidos, F# y C#, mismo archivo que el de Julia -- 3/4).
   Enfoque propio y distinto: el crescendo y el diminuendo, la
   musica que crece y se calma. Nivel basico pero solido."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · GLADIATOR (HONOR HIM)'
TS = (3, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['A2', 'C#3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de Gladiator, de Hans Zimmer, en Re mayor. Hoy: el crescendo y el diminuendo.')
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

    y = exercise_heading(c, y, 2, 'El crescendo y el diminuendo: la música que crece y se calma', 2,
                          'Lo que trabajamos hoy. La pieza crece de piano a mezzoforte y luego se calma de nuevo: el volumen debe cambiar de forma gradual, no de golpe.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase que crece: cada nota, un poco más fuerte', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F#4', 'E4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) La frase que se calma: cada nota, un poco más suave', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4']]
    bass2c = [{'pitches': RE, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El crescendo sobre el acorde de Re, sostenido', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: el acorde sostenido acompaña el crecimiento y la calma de la melodía.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el crescendo sobre el acorde de Sol', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha crece de forma gradual encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C#5', 'D5', 'C#5']]
    bass1 = [{'pitches': SOL, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El crescendo sobre Sol, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C#5', 'D5', 'C#5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el diminuendo no descoloca el acorde', 3,
                          'La izquierda sostiene su acorde sin moverse; la derecha se calma poco a poco sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'B4', 'A4', 'G4', 'A4']]
    bass3 = [{'pitches': LA, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El diminuendo sobre La; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'E4', 'D4', 'E4', 'F#4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más abajo', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Gladiator casi entera', 3,
                          'Con la partitura al lado: haz que el volumen crezca y se calme de forma gradual, sin golpes.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'A4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F#4', 'E4', 'D4', 'E4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [RE, RE, SOL, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Gladiator casi completa · con el crescendo y el diminuendo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
