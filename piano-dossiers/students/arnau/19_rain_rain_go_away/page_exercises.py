# -*- coding: utf-8 -*-
"""Taller de practica - Rain Rain Go Away (Arnau, cancion 19, Do
   mayor, 4/4, a 4 manos). Formato por BLOQUES del Dosier Exhaustivo
   de Ejercicios de Piano (bloques 1,2,3,4,6). Categoria C (conjunto):
   sincronizacion de entradas a 4 manos con el profesor."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · RAIN RAIN GO AWAY (A 4 MANOS)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción a 4 manos en Do mayor: tú tocas el Primo, el profesor te acompaña con el Secondo.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Practica "entradas a la de tres" con el profesor: contad juntos y empezad a la vez.',
        'Camina los dedos sobre la tapa cerrada, muy firme, contando hasta 4.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Categoría C (conjunto): notas largas y firmes, para no perder el pulso juntos.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'w'} for p in ['C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Cuatro notas muy largas', ev1a, clef='treble', time_sig=TS)

    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Tu frase (Primo), con calma (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: primero practica tu parte sola; luego pide al profesor que toque la suya contigo.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. Tu parte (Primo) sobre el acorde quieto.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'C5', 'A4', 'G4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: tu frase sobre Fa, quieto', grand_gap_mult=6.8, time_sig=TS)

    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'F4']] +
             [{'pitch': p, 'dur': 'h'} for p in ['A4', 'C5', 'A4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: Rain Rain Go Away casi entera', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca su parte, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Escucha las dos partes juntas: ¿tu parte (Primo) suena más aguda o más grave?',
        'Toca el acorde de Do y luego el de Fa: ¿cuál es más grave?',
        'Cuenta a la vez que suena la canción: ¿entráis juntos al principio?',
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
