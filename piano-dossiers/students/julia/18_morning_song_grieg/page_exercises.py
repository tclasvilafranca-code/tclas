# -*- coding: utf-8 -*-
"""Taller de practica - Morning Song (Julia, cancion 18, Grieg,
   Do mayor, 3/4). Nivel inicial con toque extra: las notas
   sorpresa -- sostenidos que aparecen sin avisar, sin cambiar
   de tonalidad."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · MORNING SONG (GRIEG)'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una pieza tranquila de Grieg en Do mayor. Hoy: ¡algunas notas sorpresa con sostenido!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). ¡Busca tu nota casa, el Do!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Las notas sorpresa: un sostenido sin avisar', 2,
                          'Lo que vamos a practicar hoy. De vez en cuando aparece una nota con sostenido (♯) que da color, aunque la canción sigue en Do mayor.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F#4', 'G4', 'F#4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) El Fa que se vuelve sostenido y vuelve a casa', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'G#4', 'A4', 'G#4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora con el Sol: la misma idea, un poco más arriba', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F#4', 'G4', 'F#4', 'F4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las notas sorpresa sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la izquierda respira despacio mientras la derecha canta.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía tranquila sobre el acorde de Do', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta despacio y con calma encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'C4', 'D4']]
    bass1 = [{'pitches': DO, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Do, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · la sorpresa del sostenido, con acompañamiento', 3,
                          'La izquierda queda quieta con su acorde; la derecha toca la nota sorpresa sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'G#4', 'A4', 'G#4', 'G4', 'F4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La sorpresa del sostenido sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G#4', 'A4', 'B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Morning Song casi entera', 3,
                          'Con la partitura al lado: ¡toca despacio y con calma, sintiendo cada nota sorpresa!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'C4', 'D4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F#4', 'G4', 'F#4', 'F4', 'E4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Morning Song casi completa · con la sorpresa del sostenido', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
