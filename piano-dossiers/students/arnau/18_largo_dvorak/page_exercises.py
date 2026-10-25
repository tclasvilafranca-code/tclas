# -*- coding: utf-8 -*-
"""Taller de practica - Largo, Sinfonia n.5 'Del Nuevo Mundo' (Arnau,
   cancion 18, Do mayor, 4/4). Formato por BLOQUES del Dosier
   Exhaustivo de Ejercicios de Piano (bloques 1,2,3,4,6). Reto
   motivador (nivel basico): primer contacto con musica clasica real,
   con un fragmento a dos lineas de pentagrama."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · RETO MOTIVADOR · LARGO (DVOŘÁK)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Música clásica de verdad, en Do mayor. Hoy: una frase larga que no se puede cortar en medio.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Respira profundo 3 veces, contando hasta 4 en cada respiración.',
        'Canta mentalmente una frase larga sin parar, como preparación para tocarla así.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Hoy: cantar mentalmente toda la frase de un tirón, sin pausas.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'w'} for p in ['C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Notas larguísimas, una respiración al final', ev1a, clef='treble', time_sig=TS)

    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Una frase que sube y baja sin cortes (la dificultad de hoy)', ev2a, clef='treble', time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: canta la frase entera en voz alta antes de tocarla — así no se corta al piano.')
    y -= 15
    gap = 6.7
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Un fragmento real, repartido en dos líneas — como en la partitura de verdad.')
    y -= 4
    ev_multi = [{'pitch': p, 'dur': 'q'} for p in
                ['E4', 'G4', 'A4', 'G4', 'E4', 'D4', 'C4', 'D4',
                 'E4', 'F4', 'G4', 'A4', 'G4', 'E4', 'D4', 'C4']]
    y = multi_system_block(c, x0, w0, y, gap, 'a) La frase real de la sinfonía, en dos líneas',
                            ev_multi, clef='treble', time_sig=TS, bars_per_line=2)
    y -= 4

    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'E4']] +
             [{'pitch': p, 'dur': 'h'} for p in ['A4', 'C5', 'Bb4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: el tema casi entero, manos juntas', grand_gap_mult=6.6, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Escucha la frase completa dos veces: ¿dónde "respira", al principio o al final?',
        'Toca el acorde de Do y luego el de Fa: ¿cuál es más grave?',
        'Compara la frase tocada rápido y tocada Largo: ¿cuál transmite más calma?',
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
