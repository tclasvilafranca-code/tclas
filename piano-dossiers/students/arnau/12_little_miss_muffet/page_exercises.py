# -*- coding: utf-8 -*-
"""Taller de practica - Little Miss Muffet (Arnau, cancion 12, Fa
   mayor, 6/8). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6). Registro de las corcheas
   con plica arriba limitado a A4 como maximo para que la barra no
   invada la cabecera del ejercicio."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · LITTLE MISS MUFFET'
TS = (6, 8)
KEY = 'Fa mayor'

FA = ['F2', 'A2', 'C3']
SIb = ['Bb1', 'D2', 'F2']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un cuento cantado en Fa mayor, en 6/8: se cuenta en dos grupos de tres.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Balancéate suavemente de un pie a otro contando "uno-dos-tres, uno-dos-tres".',
        'Camina los dedos sobre la tapa cerrada, en grupos de tres.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: el balanceo de seis corcheas, en dos grupos de tres.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['E4', 'F4', 'G4', 'A4', 'G4', 'F4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Seis corcheas, en dos grupos de tres', ev1a, clef='treble', time_sig=TS, key_sig=KEY)

    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['G4', 'F4', 'E4', 'D4', 'E4', 'F4'])]
    y = system_block(c, x0, w0, y, gap, 'b) El vaivén, como un columpio (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS, key_sig=KEY)

    pattern_a = [(FA, 'Fa'), (SIb, 'Sib')] + [(DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Fa-Sib-Do-Fa', eva, clef='bass', time_sig=TS, key_sig=KEY)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: cuenta "uno-dos-tres, uno-dos-tres" en voz alta antes de tocar, marcando los "unos".')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. El acorde queda quieto; la derecha se balancea encima.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
             enumerate(['G4', 'F4', 'E4', 'D4', 'E4', 'F4'])]
    bass1 = [{'pitches': FA, 'dur': 'q.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: el vaivén sobre Fa, sostenido', grand_gap_mult=6.8, time_sig=TS, key_sig=KEY)

    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
              enumerate(['E4', 'F4', 'G4', 'A4', 'G4', 'F4'])] +
             [{'pitch': p, 'dur': 'e', 'beam': (i // 3) + 2} for i, p in
              enumerate(['G4', 'F4', 'E4', 'D4', 'E4', 'F4'])])
    bass5 = [{'pitches': p, 'dur': 'q.'} for p in [FA, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: Little Miss Muffet casi entera', grand_gap_mult=6.8, time_sig=TS, key_sig=KEY)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca los dos grupos de tres corcheas: ¿suenan iguales o distintos?',
        'Toca el acorde de Fa y luego el de Sib: ¿cuál es más grave?',
        'Balancéate mientras el profesor toca: ¿en qué nota "cae" tu peso?',
    ], dot_color=BLOQUE_COLOR[4])
    y -= 6

    y = bloque_heading(c, y, 6, 'Aquí sí se escribe: sobre el papel, con la partitura delante.')
    y -= 4
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Escribe el grado (I, IV, V) de cada acorde: Fa__  Sib__  Do__  Fa__')
    y -= 6
    y = answer_box_row(c, MARGIN, y - 4, 4, (CONTENT_W - 3 * 6) / 4, gap=6)

    exercises_footer(c, 4)
    c.showPage()
