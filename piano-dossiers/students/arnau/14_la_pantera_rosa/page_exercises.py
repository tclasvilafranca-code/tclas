# -*- coding: utf-8 -*-
"""Taller de practica - La Pantera Rosa (Arnau, cancion 14, Do
   mayor, 4/4). Nivel iniciacion con toque extra: el paso a
   escondidas, notas cromaticas de puntillas."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · NIVEL INICIACIÓN · LA PANTERA ROSA'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El famoso tema de dibujos animados, sigiloso y con swing. Hoy: notas "de puntillas".')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: caminar de puntillas', 1,
                          'Toca cada nota muy suave (piano), como si caminaras sin hacer ruido.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4', 'C4', 'D4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) Pasos suaves, sin acentos', ev1a, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El paso a escondidas: notas cromáticas', 2,
                          'Entre dos notas normales aparece una nota "intrusa" (con sostenido o bemol) — como un paso escondido.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'C#4', 'D4', 'D#4', 'E4', 'D#4', 'D4', 'C#4']]
    y = system_block(c, x0, w0, y, gap, 'a) El paso escondido, subiendo y bajando', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo camino, sin escondites: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'C#4', 'D4', 'D#4', 'E4', 'D#4', 'D4', 'C#4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El paso escondido sobre el acorde de Do, quieto', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Truco de estudio: toca cada nota "escondida" muy despacio antes de ponerla en tiempo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el paso escondido sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha da sus pasos de puntillas.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F#4', 'G4', 'G#4', 'A4', 'G#4', 'G4', 'F#4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El paso escondido sobre Fa, quieto', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin escondites: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se esconde con la melodía', 3,
                          'La izquierda queda quieta con su acorde; la derecha da sus pasos escondidos, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'G#4', 'A4', 'A#4', 'B4', 'A#4', 'A4', 'G#4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El paso escondido sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación, sin escondites', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · La Pantera Rosa casi entera', 3,
                          'Con la partitura al lado: deja que las notas escondidas suenen sigilosas, casi en secreto.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'C#4', 'D4', 'D#4', 'E4', 'D#4', 'D4', 'C#4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'F#4', 'G4', 'G#4', 'A4', 'G#4', 'G4', 'F#4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · sigilosa y escondida', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
