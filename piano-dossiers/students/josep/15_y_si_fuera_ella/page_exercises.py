# -*- coding: utf-8 -*-
"""Taller de practica - Y si fuera ella (Josep, cancion 15, Fa
   mayor, 4/4). Enfoque: el acorde abierto -- la mano se estira para
   cubrir un acorde extendido (fundamental, quinta y decima), sin
   tensarse."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · ABRIL · Y SI FUERA ELLA (ALEJANDRO SANZ)'
TS = (4, 4)

FA = ['F2', 'A2', 'C3']
DO = ['C3', 'E3', 'G3']
REm = ['D3', 'F3', 'A3']
SIb = ['Bb2', 'D3', 'F3']

FA_OPEN = ['F2', 'C3', 'A3']
DO_OPEN = ['C3', 'G3', 'E4']
REm_OPEN = ['D3', 'A3', 'F4']
SIb_OPEN = ['Bb2', 'F3', 'D4']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Alejandro Sanz en Fa mayor. El reto: el acorde abierto que estira la mano.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El acorde abierto: la mano que se estira, sin apretar', 2,
                          'La dificultad exacta de esta canción. El acorde de la izquierda se abre — fundamental, quinta y una décima arriba — y la mano tiene que estirarse sin ponerse rígida.')
    y -= 9
    ev2a = [{'pitches': p, 'dur': 'h'} for p in [FA_OPEN, DO_OPEN, REm_OPEN, SIb_OPEN]]
    y = system_block(c, x0, w0, y, gap, 'a) Los acordes abiertos: Fa-Do-Rem-Sib', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h'} for p in [FA, DO, REm, SIb]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, cerrados: para comparar la distancia', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'Bb4', 'A4', 'G4', 'F4', 'G4', 'A4', 'Bb4']]
    bass2c = [{'pitches': FA_OPEN, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde abierto de Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Fa–Do–Rem–Sib: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (DO, 'Do'), (REm, 'Rem'), (SIb, 'Sib')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Do-Rem-Sib, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el acorde abierto sostiene mientras la melodía canta encima.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde abierto de Do', 2,
                          'La izquierda se estira sobre el acorde abierto, sin tensarse; la derecha canta la melodía tranquila encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'A4']]
    bass1 = [{'pitches': DO_OPEN, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Do abierto, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'A4', 'B4', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde abierto no se contagia de la melodía', 3,
                          'La izquierda queda estirada sobre su acorde abierto, sin moverse; la derecha canta despacio encima, sin arrastrarla.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'B4']]
    bass3 = [{'pitches': REm_OPEN, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde abierto de Rem no se mueve; la melodía canta libre', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'B4', 'C5', 'D5', 'E5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Y si fuera ella casi entera', 3,
                          'Con la partitura al lado: deja que la mano se estire sin prisa sobre cada acorde abierto.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C5', 'Bb4', 'A4', 'G4', 'F4', 'G4', 'A4', 'Bb4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [FA_OPEN, FA_OPEN, DO_OPEN, DO_OPEN]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con los acordes abiertos sosteniendo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
