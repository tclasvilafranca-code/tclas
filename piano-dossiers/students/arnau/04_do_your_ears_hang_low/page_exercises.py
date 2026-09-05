# -*- coding: utf-8 -*-
"""Taller de practica - Do Your Ears Hang Low (Arnau, cancion 4, Do
   mayor, 4/4). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6)."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · DO YOUR EARS HANG LOW'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción divertida en Do mayor. Hoy: el salto gracioso, ¡sube y baja como orejas!')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Estira cada dedo por separado, empujando con suavidad hacia arriba.',
        'Salto de rana: pequeños saltos de mano en el aire, entre dos posiciones imaginarias.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: el salto gracioso, que brinca de una nota grave a una aguda.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja la escalera entera', ev1a, clef='treble', time_sig=TS)

    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'C5', 'E4', 'C5', 'F4', 'D5', 'F4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) El brinco que se balancea (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: aísla el salto en sí mismo — practica solo el brinco, fuera de la frase, antes de unirlo.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. El acorde queda quieto; la derecha se balancea encima.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'D5', 'F4', 'D5', 'G4', 'E5', 'G4', 'E5']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: el brinco sobre Fa, quieto', grand_gap_mult=6.8, time_sig=TS)

    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'C5', 'E4', 'C5', 'F4', 'D5', 'F4', 'D5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'D5', 'F4', 'D5', 'G4', 'E5', 'G4', 'E5']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: Do Your Ears Hang Low casi entera', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca Mi y luego Do agudo: ¿el salto es hacia arriba o hacia abajo?',
        'Toca el brinco dos veces, una ligero y otra golpeado: ¿cuál suena mejor?',
        'Adivina la canción con solo las 3 primeras notas.',
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
