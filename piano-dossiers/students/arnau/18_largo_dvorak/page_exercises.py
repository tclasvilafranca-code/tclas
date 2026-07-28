# -*- coding: utf-8 -*-
"""Taller de practica - Largo, Sinfonia n.5 'Del Nuevo Mundo' (Arnau,
   cancion 18, Do mayor, 4/4). Reto motivador (nivel basico): la
   frase larga que no se corta -- primer contacto con musica clasica
   "de verdad", con un fragmento a dos lineas de pentagrama."""
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
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: respirar solo al final de la frase', 1,
                          'Toca las cuatro notas seguidas, sin ninguna pausa entre ellas, y solo respira al terminar.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'w'} for p in ['C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Notas larguísimas, una respiración al final', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La frase larga que no se corta', 2,
                          'Lo importante hoy: cantar mentalmente toda la frase de un tirón, sin pararse a mitad camino.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Una frase que sube y baja sin cortes', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, con más notas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase larga sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, sostenidos y largos.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde entero por compás', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Truco de estudio: canta la frase entera en voz alta antes de tocarla — así no se corta al piano.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta su frase larga encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'C5', 'Bb4', 'A4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase sobre Fa, sostenido y quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'Bb4', 'C5', 'Bb4', 'A4', 'G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, con más notas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Un fragmento real, repartido en dos líneas', 3,
                          'Como en una partitura de verdad: la frase completa no cabe en una sola línea, así que se reparte en dos.')
    y -= 4
    ev_multi = [{'pitch': p, 'dur': 'q'} for p in
                ['E4', 'G4', 'A4', 'G4', 'E4', 'D4', 'C4', 'D4',
                 'E4', 'F4', 'G4', 'A4', 'G4', 'E4', 'D4', 'C4']]
    y = multi_system_block(c, x0, w0, y, gap, 'a) La frase real de la sinfonía, en dos líneas',
                            ev_multi, clef='treble', time_sig=TS, bars_per_line=2)
    y -= 6

    y = exercise_heading(c, y, 6, 'Reto extra · el tema casi entero', 3,
                          'Con la partitura al lado: deja que la frase respire solo al final, larga y sostenida.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'E4']] +
             [{'pitch': p, 'dur': 'h'} for p in ['A4', 'C5', 'Bb4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El tema casi completo · una frase larga y noble', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
