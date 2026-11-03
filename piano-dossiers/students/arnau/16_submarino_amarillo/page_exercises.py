# -*- coding: utf-8 -*-
"""Taller de practica - El Submarino Amarillo (Arnau, cancion 16,
   Sol mayor, 4/4). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6). Reto motivador (nivel
   basico): primera cancion en Sol mayor."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · RETO MOTIVADOR · EL SUBMARINO AMARILLO'
TS = (4, 4)
KEY = 'Sol mayor'

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D2', 'F#2', 'A2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un reto especial: nuestra primera canción en Sol mayor, con un sostenido en el Fa.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Localiza en el aire el grupo de "3 teclas negras": ahí vive el Fa sostenido de hoy.',
        'Camina los dedos sobre la tapa cerrada, dedo 1-2-3-4-5.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: posición de Sol mayor y el Fa sostenido, siempre igual.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('D5', 5), ('C5', 4), ('B4', 3), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja la posición de Sol mayor', ev1a, clef='treble', time_sig=TS, key_sig=KEY)

    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C5', 'B4', 'A4', 'F#4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Una frase con Fa sostenido dentro (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS, key_sig=KEY)

    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Sol-Do-Re-Sol', eva, clef='bass', time_sig=TS, key_sig=KEY)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: toca solo los Fa de la canción, uno por uno, para memorizar dónde están.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. El acorde de Do queda quieto; la derecha usa su Fa sostenido.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'C5', 'B4', 'C5', 'A4', 'F#4', 'G4']]
    bass1 = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: la frase sobre Do, quieto', grand_gap_mult=6.8, time_sig=TS, key_sig=KEY)

    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C5', 'B4', 'A4', 'F#4', 'G4', 'A4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'C5', 'B4', 'C5', 'A4', 'F#4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [SOL, SOL, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: El Submarino Amarillo casi entera', grand_gap_mult=6.8, time_sig=TS, key_sig=KEY)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca el Fa natural y luego el Fa sostenido: ¿los distingues?',
        'Toca el acorde de Sol y luego el de Do: ¿cuál es más agudo?',
        'Adivina la canción con solo las 3 primeras notas.',
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
