# -*- coding: utf-8 -*-
"""Taller de practica - Fur Elise (Merce, cancion 25, Beethoven,
   La menor -- armadura sin alteraciones, 3/4). Nivel basico pero
   solido: la alternancia rapida -- dos notas vecinas que se
   turnan sin parar, como en el famoso comienzo."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · FÜR ELISE (BEETHOVEN)'
TS = (3, 4)

LAm = ['A2', 'C3', 'E3']
REm = ['D2', 'F2', 'A2']
MI = ['E2', 'G#2', 'B2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Für Elise, de Beethoven, en La menor. Hoy: la alternancia rápida entre dos notas vecinas.')
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

    y = exercise_heading(c, y, 2, 'La alternancia rápida: dos notas que se turnan', 2,
                          'Lo que trabajamos hoy. El famoso comienzo alterna dos notas vecinas (Mi y Re#) una y otra vez, relajada: como una respiración que no se tensa.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in
            enumerate(['E4', 'D#4', 'E4', 'D#4', 'E4', 'D#4', 'E4', 'D#4', 'E4', 'D#4', 'E4', 'D#4'])]
    y = system_block(c, x0, w0, y, gap, 'a) La alternancia rápida, relajada, sin tensar la muñeca', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D#4', 'E4', 'D#4', 'E4', 'D#4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma alternancia, muy despacio: para aprender el gesto', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['E4', 'D#4', 'E4', 'D#4', 'E4', 'D#4']]
    bass2c = [{'pitches': LAm, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La alternancia sobre el acorde de La menor, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en La menor', 2,
                          'La menor–Re menor–Mi (con el sensible Sol#): los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(LAm, 'Lam'), (REm, 'Rem'), (MI, 'Mi'), (LAm, 'Lam')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mi-Lam, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: la alternancia se mantiene relajada mientras suena el acorde.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la alternancia sobre el acorde de Re menor', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha alterna sus dos notas relajada.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['A4', 'G4', 'A4', 'G4', 'A4', 'G4']]
    bass1 = [{'pitches': REm, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La alternancia sobre Re menor, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'A4', 'G4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma alternancia, muy despacio: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la alternancia no descoloca el acorde', 3,
                          'La izquierda sostiene el acorde de Mi con su sensible Sol#, quieta; la derecha alterna sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['B4', 'A#4', 'B4', 'A#4', 'B4', 'A#4']]
    bass3 = [{'pitches': MI, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La alternancia sobre Mi; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A#4', 'B4', 'A#4', 'B4', 'A#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, muy despacio', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Für Elise casi entera', 3,
                          'Con la partitura al lado: mantén la alternancia relajada, sin tensar la muñeca ni un momento.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['E4', 'D#4', 'E4', 'D#4', 'E4', 'D#4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'C5']])
    bass5 = [{'pitches': LAm, 'dur': 'h.'}, {'pitches': LAm, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Für Elise casi completa · con la alternancia rápida y relajada', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
