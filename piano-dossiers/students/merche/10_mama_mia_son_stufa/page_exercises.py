# -*- coding: utf-8 -*-
"""Taller de practica - Mama Mia, Mi Son Stufa (Merce, cancion 10,
   folk italiano, arr. Regina Pratley, Do mayor, 4/4, a 4 manos).
   Nivel basico pero solido: Allegro con brio -- el caracter
   energico del tempo, sin perder el control."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · MAMA MIA, MI SON STUFA (A 4 MANOS)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción popular italiana a 4 manos, en Do mayor. Hoy: el carácter enérgico del "Allegro con brio".')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Localiza el Do central como punto de referencia.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Allegro con brio: el carácter enérgico del tempo', 2,
                          'Lo que trabajamos hoy. "Allegro con brio" pide un tempo vivo y con energía: cada nota debe sonar clara y decidida, sin precipitarse ni perder el control.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase con energía y claridad, sin correr', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, muy despacio primero: para ganar control antes de acelerar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5']]
    bass2c = [{'pitches': DO, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase enérgica sobre el acorde de Do, repetido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: mantén la energía del "brio" sin perder claridad en ninguna nota.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la energía sobre el acorde repetido de Fa', 2,
                          'La izquierda repite su acorde de Fa con firmeza; la derecha mantiene la energía sin perder el control.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'F5']]
    bass1 = [{'pitches': FA, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase enérgica sobre el acorde de Fa, repetido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'F5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la energía no descontrola el acorde', 3,
                          'La izquierda repite su acorde de Sol con firmeza; la derecha mantiene el brío sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'E5', 'F#5', 'G5']]
    bass3 = [{'pitches': SOL, 'dur': 'q'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La energía sobre el acorde de Sol, repetido', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'E5', 'F#5', 'G5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sobre Sol', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Mama Mia, Mi Son Stufa casi entera', 3,
                          'Con la partitura al lado: mantén el "Allegro con brio", con energía y claridad en cada nota.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'F5']])
    bass5 = [{'pitches': p, 'dur': 'q'} for p in [DO, DO, DO, DO, FA, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Mama Mia, Mi Son Stufa casi completa · con la energía del brio', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
