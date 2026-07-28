# -*- coding: utf-8 -*-
"""Taller de practica - Rain Rain Go Away (Arnau, cancion 19, Do
   mayor, 4/4, a 4 manos). Nivel iniciacion: notas largas que
   dialogan entre el profesor (Secondo) y el alumno (Primo)."""
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
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: notas largas y firmes', 1,
                          'Toca cada nota y déjala sonar entera, contando hasta 4 antes de la siguiente.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'w'} for p in ['C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Cuatro notas muy largas', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El diálogo a cuatro manos', 2,
                          'Tu parte (Primo) y la del profesor (Secondo) se responden: cuando tú acabas tu frase, entra la suya.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'a) Tu frase (Primo), con calma', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'D4', 'C4', 'B3']]
    y = system_block(c, x0, w0, y, gap, 'b) La frase del profesor (Secondo), más grave', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'F4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Tu frase, sobre el acorde de Do', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Truco de estudio: primero practica tu parte sola; luego pide al profesor que toque la suya contigo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · tu frase sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha toca tu parte (Primo) encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'C5', 'A4', 'G4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Tu frase sobre Fa, quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Tu frase, con más notas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · escuchar sin perder tu parte', 3,
                          'Aunque suene el Secondo del profesor debajo, tu parte de arriba no cambia.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h'} for p in ['B4', 'C5', 'B4', 'A4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Tu frase sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación, un poco más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Rain Rain Go Away casi entera', 3,
                          'Con la partitura al lado: toca tu parte firme, dejando espacio al profesor para la suya.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h'} for p in ['G4', 'A4', 'G4', 'F4']] +
             [{'pitch': p, 'dur': 'h'} for p in ['A4', 'C5', 'A4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · tu parte (Primo)', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
