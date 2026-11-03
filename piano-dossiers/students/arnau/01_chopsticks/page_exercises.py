# -*- coding: utf-8 -*-
"""Taller de practica - Chopsticks (Arnau, cancion 1, Do mayor, 3/4).
   Formato por BLOQUES del Dosier Exhaustivo de Ejercicios de Piano
   (bloques 1,2,3,4,6 -- 5 y 7 descartados). Nivel iniciacion, 9 anos."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · CHOPSTICKS'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El juego de piano más famoso del mundo, en Do mayor: las dos manos se turnan sin chocar.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos con energía, como si tuvieras frío en los dedos.',
        'Abre y cierra los puños con los brazos estirados, 10 veces.',
        'Junta las palmas como en oración y estira suavemente hacia los lados.',
        'Camina los dedos sobre la tapa cerrada del piano, dedo 1-2-3-2-1.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: la posición de Do mayor y el turno de las dos manos, sin chocar.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Posición de 5 dedos: Do(1) Re(2) Mi(3) Fa(4) Sol(5)', ev1a, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'b) El turno de las dos manos, cada una espera su vez', grand_gap_mult=7.0, time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Estrategia de estudio: practica cada mano por separado antes de juntarlas.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. La izquierda sostiene el acorde de Fa; la derecha juega su turno.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['F4', 'G4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: el turno de la derecha sobre Fa, quieto', grand_gap_mult=6.8, time_sig=TS)

    treb5 = ([{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4', 'E4']] +
             [{'pitch': p, 'dur': 'h.'} for p in ['F4', 'G4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [DO, DO, DO, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: Chopsticks casi entera', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca Do y luego Sol: ¿la segunda nota es más aguda o más grave?',
        'Toca los acordes de Do, Fa y Sol seguidos: ¿cuál suena "como si terminara la frase"?',
        'Toca las 3 primeras notas de Chopsticks de memoria, sin partitura: ¿las reconoces?',
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
