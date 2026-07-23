# -*- coding: utf-8 -*-
"""Taller de practica - Thinking Out Loud (Valentina, cancion 19, Re
   mayor, 4/4, mismo archivo que Dilan). Nivel medio, un poco mas
   exigente: el bajo caminante -- una nota distinta en cada tiempo,
   enlazando los acordes como pasos."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · THINKING OUT LOUD (ED SHEERAN)'
TS = (4, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['E2', 'A2', 'C#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Ed Sheeran en Re mayor. Hoy: el bajo caminante, paso a paso entre acordes.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F#4', 3), ('A4', 5), ('G4', 4), ('E4', 2), ('D4', 1), ('E4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Mezcla de saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 5), ('D4', 1), ('F#4', 3), ('D4', 1)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, desde el La', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El bajo caminante: una nota distinta en cada tiempo', 2,
                          'Lo de hoy. En vez de repetir el mismo acorde, la izquierda camina nota a nota, enlazando un acorde con el siguiente como si diera pasos.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q', 'label': l} for p, l in
            [('D3', 'Re'), ('E3', None), ('F#3', None), ('G3', 'Sol')]]
    y = system_block(c, x0, w0, y, gap, 'a) Re camina hasta Sol: Re-Mi-Fa#-Sol', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q', 'label': l} for p, l in
            [('G3', 'Sol'), ('F#3', None), ('E3', None), ('D3', 'Re')]]
    y = system_block(c, x0, w0, y, gap, 'b) Y vuelve caminando de Sol a Re', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D4', 'E4', 'F#4', 'G4'] * 2)]
    bass2c = [{'pitch': p, 'dur': 'q'} for p in ['D3', 'E3', 'F#3', 'G3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Corcheas iguales arriba, bajo caminante abajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los acordes básicos, para reconocer hacia dónde camina el bajo.')
    y -= 11
    pattern_a = [(RE, 'Re'), (LA, 'La'), (SOL, 'Sol'), (RE, 'Re')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-La-Sol-Re, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, el bajo caminando bajo la melodía, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · corcheas sobre el bajo caminante', 2,
                          'La izquierda camina nota a nota; la derecha corre por encima, sin perder su igualdad.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D4', 'E4', 'F#4', 'G4'] * 4)]
    bass4 = [{'pitch': p, 'dur': 'q'} for p in
             ['D3', 'E3', 'F#3', 'G3', 'F#3', 'E3', 'D3', 'C#3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) Corcheas iguales sobre el bajo que camina', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El bajo caminante que enlaza acordes distintos', 3,
                          'Ahora el bajo camina de Re a La y de vuelta, siempre nota a nota, sin saltos bruscos.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'G4', 'F#4', 'E4'] * 4)]
    bass5 = [{'pitch': p, 'dur': 'q'} for p in
             ['D3', 'C#3', 'B2', 'A2', 'C#3', 'D3', 'E3', 'F#3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) El bajo camina entre Re y La', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Thinking Out Loud casi entera, con el bajo caminante', 3,
                          'Con la partitura al lado: deja que el bajo camine sin prisa, un paso por cada tiempo.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D4', 'E4', 'F#4', 'G4'] * 2)]
    treb6 += [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'G4', 'F#4', 'E4'] * 2)]
    bass6 = [{'pitch': p, 'dur': 'q'} for p in
             ['D3', 'E3', 'F#3', 'G3', 'F#3', 'E3', 'D3', 'C#3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · ♩≈145, bajo caminante', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
