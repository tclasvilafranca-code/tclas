# -*- coding: utf-8 -*-
"""Taller de practica - Polly Put the Kettle On (Arnau, cancion 11,
   Fa mayor, 4/4). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6)."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · POLLY PUT THE KETTLE ON'
TS = (4, 4)
KEY = 'Fa mayor'

FA = ['F2', 'A2', 'C3']
SIb = ['Bb1', 'D2', 'F2']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Otra canción en Fa mayor, tranquila. Hoy: notas ligadas, sin cortar entre una y otra.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Rotaciones lentas de muñeca, en el aire y sobre la tapa cerrada.',
        'Legato en el aire: mueve la mano de un punto a otro sin "cortes" en el movimiento.',
        'Estira cada dedo por separado, muy despacio.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: unir cada nota con la siguiente, sin ningún hueco.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) La posición de Fa mayor, ligada', ev1a, clef='treble', time_sig=TS, key_sig=KEY)

    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['C5', 'Bb4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Notas largas y unidas (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS, key_sig=KEY)

    pattern_a = [(FA, 'Fa'), (SIb, 'Sib'), (DO, 'Do'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Fa-Sib-Do-Fa', eva, clef='bass', time_sig=TS, key_sig=KEY)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: canta la frase con "aaaa" sin parar, y luego imita eso al piano.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. El acorde de Sib queda quieto; la derecha liga sus notas.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['D5', 'C5', 'Bb4', 'A4']]
    bass1 = [{'pitches': SIb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: legato sobre Sib, quieto', grand_gap_mult=6.8, time_sig=TS, key_sig=KEY)

    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['C5', 'Bb4', 'A4', 'G4']] +
             [{'pitch': p, 'dur': 'h'} for p in ['D5', 'C5', 'Bb4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [FA, FA, SIb, SIb]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: Polly Put the Kettle On casi entera', grand_gap_mult=6.8, time_sig=TS, key_sig=KEY)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca dos notas ligadas y luego dos notas cortadas: ¿oyes la diferencia?',
        'Toca Do-Bb-A-Sol: ¿la melodía sube o baja?',
        'Toca el acorde de Fa y luego el de Do: ¿cuál es más agudo?',
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
