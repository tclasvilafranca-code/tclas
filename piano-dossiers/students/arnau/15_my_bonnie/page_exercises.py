# -*- coding: utf-8 -*-
"""Taller de practica - My Bonnie Lies Over the Ocean (Arnau, cancion
   15, Do mayor, 3/4). Reto motivador (nivel basico): el cambio de
   posicion de la mano izquierda a mitad de frase, y un primer
   contacto con el cruce de manos al final."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · RETO MOTIVADOR · MY BONNIE'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un reto especial en Do mayor: la izquierda cambia de sitio a mitad de frase. ¡Tú puedes!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: encontrar la nueva posición sin mirar', 1,
                          'Practica saltar la mano izquierda de un Do grave a un Do más agudo, sin mirar el teclado.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'h.'} for p in ['C3', 'C4', 'C3', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'a) El salto de posición, solo con la izquierda', ev1a, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El cambio de posición ("shift") de la izquierda', 2,
                          'A mitad de la canción, la izquierda se traslada a una posición nueva y se queda ahí un rato.')
    y -= 9
    ev2a = [{'pitches': p, 'dur': 'h.'} for p in [DO, FA]]
    y = system_block(c, x0, w0, y, gap, 'a) Posición 1: Do grave', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': ['C4', 'E4', 'G4'], 'dur': 'h.'}, {'pitches': ['F3', 'A3', 'C4'], 'dur': 'h.'}]
    y = system_block(c, x0, w0, y, gap, 'b) Posición 2, ya trasladada: un peldaño más arriba', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h.'} for p in ['E4', 'D4', 'C4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'h.'}] * 2 + [{'pitches': ['F3', 'A3', 'C4'], 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sigue igual; la izquierda es la que cambia', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 1,
                          'Do–Fa–Sol: los acordes de esta tonalidad, en las dos posiciones de la izquierda.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde entero por compás', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Truco de estudio: marca con lápiz en la partitura el compás exacto donde la izquierda cambia de sitio.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía no nota el cambio', 2,
                          'La derecha sigue cantando su frase tranquila; la izquierda, debajo, hace su viaje de una posición a otra.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'A4', 'G4', 'F4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] + [{'pitches': ['Bb3', 'D4', 'F4'], 'dur': 'h.'}] * 2 + [{'pitches': FA, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La izquierda viaja de Fa a Sib y vuelve', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para escuchar la frase entera', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Primer contacto: un dedo de la izquierda "visita" arriba', 3,
                          'Al final de la canción la izquierda toca, por un instante, más alto que la derecha — el primer paso hacia el cruce de manos.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h.'} for p in ['C4', 'D4']]
    bass3 = [{'pitch': 'G3', 'dur': 'h.'}, {'pitch': 'E4', 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda sube a visitar una nota alta y vuelve', grand_gap_mult=7.3, time_sig=TS)
    y = nota_estilo_local(c, y, 'Nota de ergonomía: si la mano es pequeña, mueve todo el brazo hacia la nota alta — no solo estires los dedos.')

    y = exercise_heading(c, y, 6, 'Reto extra · My Bonnie casi entera', 3,
                          'Con la partitura al lado: siente cuándo la izquierda cambia de sitio, sin perder el pulso.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h.'} for p in ['E4', 'D4', 'C4']] +
             [{'pitch': p, 'dur': 'h.'} for p in ['E4', 'F4', 'G4']])
    bass5 = [{'pitches': DO, 'dur': 'h.'}] * 3 + [{'pitches': ['F3', 'A3', 'C4'], 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con el cambio de posición', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()


def nota_estilo_local(c, y, texto, height=30):
    c.setFillColor(HexColor('#F4EFE3'))
    c.roundRect(MARGIN, y - height, CONTENT_W, height, 5, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(MARGIN, y - height, 3, height, fill=1, stroke=0)
    wrap_text_common(c, texto, MARGIN + 12, y - 12, 'DejaVuSans', 8.2, CONTENT_W - 24, 11.0, color=HexColor('#5A4A20'))
    return y - height - 8
