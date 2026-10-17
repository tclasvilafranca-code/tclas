# -*- coding: utf-8 -*-
"""Taller de practica - Aloha Oe (Arnau, cancion 13, Do mayor, compas
   partido). Formato por BLOQUES del Dosier Exhaustivo de Ejercicios
   de Piano (bloques 1,2,3,4,6)."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · ALOHA OE'
TS = (2, 2)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción hawaiana muy bonita, en Do mayor. Hoy: el compás partido, que se cuenta a 2.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Balancéate lentamente contando solo "1, 2" — cada pulso muy largo.',
        'Rotaciones suaves de muñeca, apoyadas en la tapa cerrada.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: sentir solo dos pulsos grandes por compás.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Dos pulsos grandes por compás', ev1a, clef='treble', time_sig=TS)

    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Cuatro notas por pulso, pero solo 2 pulsos (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: mueve la mano libre marcando solo "1, 2" por compás mientras tocas.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. La izquierda marca los dos pulsos; la derecha canta encima.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'E4']]
    bass1 = [{'pitches': FA, 'dur': 'h'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: la frase sobre Fa, dos pulsos grandes', grand_gap_mult=6.8, time_sig=TS)

    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'E4']])
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [DO, DO, DO, DO, FA, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: Aloha Oe casi entera', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Cuenta a la vez que el profesor toca: ¿son 2 pulsos o 4 por compás?',
        'Toca el acorde de Do y luego el de Fa: ¿cuál es más grave?',
        'Escucha la frase completa dos veces: ¿te parece rápida o tranquila?',
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
