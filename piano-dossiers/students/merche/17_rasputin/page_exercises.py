# -*- coding: utf-8 -*-
"""Taller de practica - Rasputin (Merce, cancion 17, Boney M.,
   Si menor -- armadura de 2 sostenidos confirmada por los
   simbolos Bm-Em-F#7-Bm, 4/4; la partitura original solo trae
   simbolos de acorde, sin notas de bajo escritas). Nivel basico
   pero solido: los simbolos de acorde -- construir tu propio
   acompanamiento."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · RASPUTIN'
TS = (4, 4)

SIm = ['B2', 'D3', 'F#3']
MIm = ['E2', 'G2', 'B2']
FAd = ['F#2', 'A#2', 'C#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Rasputin, de Boney M., en Si menor. Hoy: leer los símbolos de acorde y construir tu acompañamiento.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Si menor', 1,
                          'Un dedo por tecla: Si(1) Do#(2) Re(3) Mi(4) Fa#(5). El Do# y el Fa# son las teclas negras de esta posición.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('B4', 1), ('C#5', 2), ('D5', 3), ('C#5', 2), ('B4', 1), ('C#5', 2), ('D5', 3), ('C#5', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'D5', 'F#5', 'D5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Si menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los símbolos de acorde: construir tu acompañamiento', 2,
                          'Lo que trabajamos hoy. La partitura original solo trae letras (Bm, Em, F#7): no hay bajo escrito. Hay que traducir cada letra al acorde y tocarlo con la izquierda.')
    y -= 9
    ev2a = [{'pitches': SIm, 'dur': 'w', 'label': 'Bm'}]
    y = system_block(c, x0, w0, y, gap, 'a) "Bm" se traduce: Si-Re-Fa#, el acorde de Si menor', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': MIm, 'dur': 'w', 'label': 'Em'}]
    y = system_block(c, x0, w0, y, gap, 'b) "Em" se traduce: Mi-Sol-Si, el acorde de Mi menor', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'B4', 'C#5']]
    bass2c = [{'pitches': SIm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acompañamiento que has construido: Si menor', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en Si menor', 2,
                          'Si menor–Mi menor–Fa# (con el sensible Do#): los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(SIm, 'Sim'), (MIm, 'Mim'), (FAd, 'Fa#'), (SIm, 'Sim')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sim-Mim-Fa#-Sim, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el acompañamiento que has construido sostiene la melodía.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre tu acompañamiento de Mi menor', 2,
                          'La izquierda sostiene el acorde que ha construido a partir de "Em"; la derecha canta la melodía encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F#4', 'E4', 'F#4']]
    bass1 = [{'pitches': MIm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Mi menor, construido a partir de "Em"', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F#4', 'E4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el sensible Do# sobre tu acorde de "F#7"', 3,
                          'La izquierda sostiene el acorde que ha construido a partir de "F#7", simplificado; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C#5', 'D5', 'C#5', 'B4']]
    bass3 = [{'pitches': FAd, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre el acorde construido a partir de "F#7"; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'B4', 'C#5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más abajo', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Rasputin casi entera', 3,
                          'Con la partitura al lado: traduce cada símbolo de acorde a su acompañamiento antes de tocar.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'B4', 'C#5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F#4', 'E4', 'F#4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [SIm, MIm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Rasputin casi completa · con tu acompañamiento construido', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
