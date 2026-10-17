# -*- coding: utf-8 -*-
"""Taller de practica - Puff the Magic Dragon (Arnau, cancion 8, Do
   mayor, 4/4). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6)."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · PUFF THE MAGIC DRAGON'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción tranquila y soñadora en Do mayor. Hoy: notas largas que flotan, sin ninguna prisa.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Rotaciones muy lentas de muñeca, como si flotaras en el agua.',
        'Estira cada dedo por separado, muy despacio, sin prisa.',
        'Respira profundo 3 veces, contando hasta 4 en cada respiración.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: dejar sonar cada nota entera, sin cortarla antes de tiempo.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'w', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5)]]
    y = system_block(c, x0, w0, y, gap, 'a) Tres notas muy largas, sin prisa', ev1a, clef='treble', time_sig=TS)

    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'G4', 'C5', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Notas largas que flotan, subiendo y bajando (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: práctica lenta con precisión antes que velocidad — que cada nota suene entera y limpia.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. El acorde queda quieto y suave; la melodía flota encima.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['F4', 'A4', 'C5', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: flotando sobre Fa, quieto', grand_gap_mult=6.8, time_sig=TS)

    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['E4', 'G4', 'C5', 'G4']] +
             [{'pitch': p, 'dur': 'h'} for p in ['F4', 'A4', 'C5', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: Puff the Magic Dragon casi entera', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca una nota larga: ¿sigue sonando cuando cuentas hasta 4?',
        'Toca Mi-Sol-Do: ¿la melodía sube, baja o se queda igual?',
        'Cierra los ojos y escucha la frase completa: ¿te suena tranquila o movida?',
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
