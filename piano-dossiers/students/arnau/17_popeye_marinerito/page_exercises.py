# -*- coding: utf-8 -*-
"""Taller de practica - Popeye el marinerito (Arnau, cancion 17,
   Sol mayor, 3/4). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6). Reto motivador (nivel
   basico): consolidando Sol mayor, ahora en vals."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · RETO MOTIVADOR · POPEYE EL MARINERITO'
TS = (3, 4)
KEY = 'Sol mayor'

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D2', 'F#2', 'A2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Otra vez Sol mayor, pero ahora en vals. Ya conoces el Fa sostenido de la canción anterior.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y junta las palmas como en oración, estirando a los lados.',
        'Balancéate en 3 tiempos, "uno-dos-tres", como un vals.',
        'Localiza en el aire el Fa sostenido, sin mirar el teclado.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: la misma posición de Sol mayor, contando de tres en tres.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('D5', 5), ('C5', 4)]]
    y = system_block(c, x0, w0, y, gap, 'a) La posición de Sol mayor, en vals', ev1a, clef='treble', time_sig=TS, key_sig=KEY)

    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'F#4', 'G4', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Una frase de vals con Fa sostenido (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS, key_sig=KEY)

    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Sol-Do-Re-Sol', eva, clef='bass', time_sig=TS, key_sig=KEY)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: cuenta el vals en voz alta, "uno-dos-tres", mientras la izquierda sostiene el acorde.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. El acorde de Do queda quieto; la derecha baila su vals.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'B4', 'C5', 'D5', 'E5']]
    bass1 = [{'pitches': DO, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: el vals sobre Do, quieto', grand_gap_mult=6.8, time_sig=TS, key_sig=KEY)

    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'F#4', 'G4', 'A4', 'B4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'B4', 'C5', 'D5', 'E5']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [SOL, SOL, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: Popeye el marinerito casi entera', grand_gap_mult=6.8, time_sig=TS, key_sig=KEY)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca el acorde de Sol y luego el de Re: ¿cuál es más agudo?',
        'Cuenta a la vez que el profesor toca: ¿son 3 pulsos por compás?',
        'Toca la frase con y sin el Fa sostenido: ¿oyes la diferencia?',
    ], dot_color=BLOQUE_COLOR[4])
    y -= 6

    y = bloque_heading(c, y, 6, 'Aquí sí se escribe: sobre el papel, con la partitura delante.')
    y -= 4
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Escribe el grado (I, IV, V) de cada acorde: Sol__  Do__  Re__  Sol__')
    y -= 6
    y = answer_box_row(c, MARGIN, y - 4, 4, (CONTENT_W - 3 * 6) / 4, gap=6)

    exercises_footer(c, 4)
    c.showPage()
