# -*- coding: utf-8 -*-
"""Taller de practica - Eso que tu me das (Arnau, cancion 9, Do
   mayor, 4/4). Nivel iniciacion: los acordes que cambian, sin miedo."""
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
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: cambio de acorde con la mano quieta', 1,
                          'Mueve solo los dedos necesarios de un acorde a otro, sin levantar toda la mano.')
    y -= 9
    ev1a = [{'pitches': p, 'dur': 'h'} for p in [DO, FA, SOL, DO]]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, cambiando con calma', ev1a, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los acordes que cambian, sin miedo', 2,
                          'Lo importante hoy: que la mano cambie de acorde a tiempo, sin frenar la canción.')
    y -= 9
    ev2a = [{'pitches': p, 'dur': 'q'} for p in [DO, LAm, FA, SOL] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Lam-Fa-Sol, un acorde por tiempo', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5', 'G4', 'E4', 'G4', 'C5', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) La melodía sola, para escuchar por dónde va', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5', 'G4', 'E4', 'G4', 'C5', 'G4']]
    bass2c = [{'pitches': p, 'dur': 'q'} for p in [DO, LAm, FA, SOL] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Melodía y acordes que cambian, juntos', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes principales de esta tonalidad.')
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
    c.drawString(MARGIN, y, 'Truco de estudio: practica solo los cambios de acorde, sin melodía, hasta que salgan solos.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el ciclo de acordes', 2,
                          'La izquierda cambia de acorde cada tiempo; la derecha canta encima, sin pararse.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'G4', 'F4']]
    bass1 = [{'pitches': p, 'dur': 'q'} for p in [DO, LAm, FA, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase sobre Do-Lam-Fa-Sol', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'G4', 'F4', 'E4', 'D4', 'E4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde cambia, la melodía no se frena', 3,
                          'La izquierda hace su ciclo de acordes; la derecha sigue su frase, sin dudar.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'E4', 'F4']]
    bass3 = [{'pitches': p, 'dur': 'q'} for p in [DO, LAm, FA, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Otra frase sobre el mismo ciclo', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F4', 'E4', 'D4', 'C4', 'D4', 'E4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación de la melodía', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Eso que tú me das casi entera', 2,
                          'Con la partitura al lado: deja que los acordes cambien sin miedo, con la melodía encima.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'C5', 'G4', 'E4', 'G4', 'C5', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'q'} for p in [DO, LAm, FA, SOL] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · acordes cambiando con confianza', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
