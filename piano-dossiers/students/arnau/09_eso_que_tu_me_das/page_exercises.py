# -*- coding: utf-8 -*-
"""Taller de practica - Eso que tu me das (Arnau, cancion 9, Do
   mayor, 4/4). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6)."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · ESO QUE TÚ ME DAS'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
LAm = ['A2', 'C3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción española muy pegadiza, en Do mayor. Hoy: los acordes que cambian, sin miedo.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Junta las palmas como en oración y estira suavemente hacia los lados.',
        'Con la mano en el aire, "dibuja" en el aire la forma de un acorde y cambia a otra forma.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: que la mano cambie de acorde a tiempo, sin frenar.')
    y -= 4
    ev1a = [{'pitches': p, 'dur': 'h'} for p in [DO, FA, SOL, DO]]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, cambiando con calma', ev1a, clef='bass', time_sig=TS)

    ev2a = [{'pitches': p, 'dur': 'q'} for p in [DO, LAm, FA, SOL] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Do-Lam-Fa-Sol, un acorde por tiempo (la dificultad de hoy)', ev2a, clef='bass', time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: practica solo los cambios de acorde, sin melodía, hasta que salgan solos.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. La izquierda cambia cada tiempo; la derecha no se para.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'G4', 'F4']]
    bass1 = [{'pitches': p, 'dur': 'q'} for p in [DO, LAm, FA, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: la frase sobre Do-Lam-Fa-Sol', grand_gap_mult=6.8, time_sig=TS)

    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5', 'G4', 'E4', 'G4', 'C5', 'G4']]
    bass5 = [{'pitches': p, 'dur': 'q'} for p in [DO, LAm, FA, SOL] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: Eso que tú me das casi entera', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca el acorde de Do y luego el de Lam: ¿es mayor o menor el segundo?',
        'Toca los 4 acordes seguidos: ¿cuántos cambios distintos oyes?',
        'Adivina la canción con solo los 2 primeros acordes.',
    ], dot_color=BLOQUE_COLOR[4])
    y -= 6

    y = bloque_heading(c, y, 6, 'Aquí sí se escribe: sobre el papel, con la partitura delante.')
    y -= 4
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Escribe el grado (I, vi, IV, V) de cada acorde: Do__  Lam__  Fa__  Sol__')
    y -= 6
    y = answer_box_row(c, MARGIN, y - 4, 4, (CONTENT_W - 3 * 6) / 4, gap=6)

    exercises_footer(c, 4)
    c.showPage()
