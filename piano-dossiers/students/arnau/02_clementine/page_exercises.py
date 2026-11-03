# -*- coding: utf-8 -*-
"""Taller de practica - Clementine / Found a Peanut (Arnau, cancion 2,
   Do mayor, 3/4). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6). Categoria D (ergonomia,
   manos pequenas) aplicada al estiramiento de la izquierda."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · CLEMENTINE'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Casi toda la melodía va con la mano derecha; la izquierda solo alcanza una nota grave de vez en cuando.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados, 10 veces.',
        'Estira cada dedo por separado, empujando con suavidad hacia arriba.',
        'Estira todo el brazo hacia un punto lejano en el aire y vuelve, muy despacio — preparación para el estiramiento de la izquierda de hoy.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Categoría D (ergonomía): la izquierda baja UNA vez, sin forzar, moviendo todo el brazo.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3), ('C4', 1), ('E4', 3)]]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Mi-Sol, ida y vuelta', ev1a, clef='treble', time_sig=TS)

    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'D3', 'E3', 'D3', 'C3', 'D3']]
    y = system_block(c, x0, w0, y, gap, 'b) El estiramiento de la izquierda, solo, muy despacio', ev2a, clef='bass', time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: canta la letra mientras tocas — "Oh, my darling, Clementine" — para no perder el pulso.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. La derecha canta tranquila; la izquierda baja una sola vez y sube.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']]
    bass1 = [{'rest': True, 'dur': 'h'}, {'pitch': 'C3', 'dur': 'q'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: el estiramiento dentro de la frase', grand_gap_mult=6.8, time_sig=TS)

    treb6 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'D4', 'C4', 'D4']] + [{'pitch': 'C4', 'dur': 'h.'}]
    bass6 = [{'pitches': DO, 'dur': 'h.'}] * 2 + [{'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'b) Reto extra: el final de Clementine, casi completo', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca Mi y luego el Do grave de la izquierda: ¿sube o baja?',
        'Toca los acordes Do-Fa-Sol-Do: ¿cuál suena como si "terminara la frase"?',
        'Canta "Oh, my darling" antes de tocarlo: ¿coincide con las notas reales?',
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
