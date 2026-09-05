# -*- coding: utf-8 -*-
"""Taller de practica - Baa Baa Black Sheep (Arnau, cancion 3, Do
   mayor, 4/4). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6)."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · BAA BAA BLACK SHEEP'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción tradicional inglesa. Hoy: la melodía cantando, con acordes que cambian debajo.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Rotaciones suaves de muñeca, primero en el aire y luego sobre la tapa cerrada.',
        'Camina los dedos sobre la tapa cerrada, dedo 1-2-3-2-1, sin prisa.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: notas repetidas con la derecha, y el acorde que cambia con la izquierda.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('C4', 1), ('C4', 1), ('E4', 3), ('E4', 3), ('E4', 3), ('G4', 5), ('G4', 5)]]
    y = system_block(c, x0, w0, y, gap, 'a) Notas repetidas y un salto', ev1a, clef='treble', time_sig=TS)

    pattern2a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    ev2a = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern2a] * 2
    y = system_block(c, x0, w0, y, gap, 'b) Do-Fa-Sol-Do, cambiando cada negra (la dificultad de hoy)', ev2a, clef='bass', time_sig=TS)

    ev3a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa')]] + \
           [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOL, 'Sol'), (DO, 'Do')]]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', ev3a, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: di en voz alta "Do, Fa, Sol" mientras cambia la izquierda, antes de tocarlo.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. El acorde cambia; la melodía de la derecha no se para.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'C4', 'D4', 'E4']]
    bass1 = [{'pitches': DO, 'dur': 'h'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: "Baa, baa, black sheep" sobre Do', grand_gap_mult=6.8, time_sig=TS)

    treb4 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'C4', 'D4', 'E4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F4', 'E4', 'D4']])
    bass4 = [{'pitches': DO, 'dur': 'h'}] * 2 + [{'pitches': FA, 'dur': 'h'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'b) Reto extra: las dos primeras frases, con Do y Fa', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca el acorde de Do y luego el de Fa: ¿es la misma nota grave o cambia?',
        'Toca Do-Fa-Sol seguidos: ¿cuántos acordes distintos oyes?',
        'Canta "Baa, baa" antes de tocarlo: ¿empieza en una nota aguda o grave?',
    ], dot_color=BLOQUE_COLOR[4])
    y -= 6

    y = bloque_heading(c, y, 6, 'Aquí sí se escribe: sobre el papel, con la partitura delante.')
    y -= 4
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Escribe el grado (I, IV, V) de cada acorde: Do__  Fa__  Sol__  Do__')
    y -= 6
    y = answer_box_row(c, MARGIN, y - 4, 4, (CONTENT_W - 3 * 6) / 4, gap=6)

    exercises_footer(c, 4)
    c.showPage()
