# -*- coding: utf-8 -*-
"""Taller de practica - The Mulberry Bush (Arnau, cancion 20, Do
   mayor, 6/8, a 4 manos). Formato por BLOQUES del Dosier Exhaustivo
   de Ejercicios de Piano (bloques 1,2,3,4,6). Gran final del
   cuaderno, a duo con el profesor (categoria C)."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · THE MULBERRY BUSH (A 4 MANOS)'
TS = (6, 8)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de corro en Do mayor, a 4 manos: el gran final de tu cuaderno, ¡a dúo con el profesor!')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Balancéate suavemente contando "uno-dos-tres, uno-dos-tres", como en un corro.',
        'Practica "entradas a la de tres" con el profesor: contad juntos y empezad a la vez.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Categoría C (conjunto): el balanceo de seis corcheas, en dos grupos de tres.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['C4', 'D4', 'E4', 'D4', 'C4', 'D4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Seis corcheas, en dos grupos de tres', ev1a, clef='treble', time_sig=TS)

    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['E4', 'D4', 'C4', 'D4', 'E4', 'D4'])]
    y = system_block(c, x0, w0, y, gap, 'b) El corro, girando de un lado a otro (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa')] + [(SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: primero tu parte sola, muy despacio; luego a dúo con el profesor.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. El acorde queda quieto; la derecha gira encima.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
             enumerate(['F4', 'G4', 'A4', 'G4', 'F4', 'G4'])]
    bass1 = [{'pitches': FA, 'dur': 'q.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: el corro sobre Fa, sostenido', grand_gap_mult=6.8, time_sig=TS)

    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
              enumerate(['C4', 'D4', 'E4', 'D4', 'C4', 'D4'])] +
             [{'pitch': p, 'dur': 'e', 'beam': (i // 3) + 2} for i, p in
              enumerate(['F4', 'G4', 'A4', 'G4', 'F4', 'G4'])])
    bass5 = [{'pitches': p, 'dur': 'q.'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: The Mulberry Bush casi entera, a dúo', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca los dos grupos de tres corcheas: ¿el segundo es igual que el primero?',
        'Escucha las dos partes juntas (Primo y Secondo): ¿cuál lleva la melodía?',
        'Toca el acorde de Do y luego el de Fa: ¿cuál es más grave?',
    ], dot_color=BLOQUE_COLOR[4])
    y -= 6

    y = bloque_heading(c, y, 6, 'Aquí sí se escribe: sobre el papel, con la partitura delante. ¡Último ejercicio del cuaderno!')
    y -= 4
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Escribe el grado (I, IV, V) de cada acorde: Do__  Fa__  Sol__  Do__')
    y -= 6
    y = answer_box_row(c, MARGIN, y - 4, 4, (CONTENT_W - 3 * 6) / 4, gap=6)

    exercises_footer(c, 4)
    c.showPage()
