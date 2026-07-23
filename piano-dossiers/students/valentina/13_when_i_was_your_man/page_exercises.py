# -*- coding: utf-8 -*-
"""Taller de practica - When I Was Your Man (Valentina, cancion 13,
   Do mayor, 4/4, mismo archivo que Dilan y Sandi). Nivel medio, un
   poco mas exigente: el bajo en arpegio -- romper el acorde en vez
   de tocarlo en bloque."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · WHEN I WAS YOUR MAN (BRUNO MARS)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de piano solo en Do mayor. Hoy: el bajo en arpegio, rompiendo el acorde.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El bajo en arpegio: romper el acorde en vez de tocarlo en bloque', 2,
                          'Lo de hoy. En lugar de un acorde entero de golpe, la izquierda lo reparte nota a nota: raíz, tercera, quinta, tercera, como una ola que sube y baja.')
    y -= 12
    ev2a = [{'pitches': DO, 'dur': 'w', 'label': 'Do'}]
    y = system_block(c, x0, w0, y, gap, 'a) Primero, el acorde en bloque: para comparar', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3', 'E3']]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora roto: raíz-tercera-quinta-tercera', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'C4']]
    bass2c = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3', 'E3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El arpegio abajo, la nota sostenida arriba', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Fa–Sol–Do–Sol: memoriza el orden antes de memorizar las notas.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sol-Do-Sol, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el arpegio abajo sostiene la melodía de arriba.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el arpegio de Fa', 2,
                          'La izquierda reparte el acorde de Fa nota a nota; la derecha canta la melodía por encima.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['F4', 'F4']]
    bass1 = [{'pitch': p, 'dur': 'q'} for p in ['F2', 'A2', 'C3', 'A2']]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El arpegio de Fa, con la melodía sostenida', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3', 'C4', 'F2', 'A2', 'C3', 'F3']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo el arpegio, Do y Fa seguidos: para memorizar el dibujo', treb2, clef='bass', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · el arpegio no se contagia de la melodía', 3,
                          'La izquierda reparte el acorde de Sol sin perder el dibujo; la derecha canta sin arrastrarla.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'G4']]
    bass3 = [{'pitch': p, 'dur': 'q'} for p in ['G2', 'B2', 'D3', 'B2']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Melodía en negras sobre el arpegio de Sol', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · When I Was Your Man casi entera, con el arpegio', 3,
                          'Con la partitura al lado: deja que el arpegio de la izquierda fluya como una ola, sin cortes.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'F4', 'G4', 'C4']]
    bass6 = ([{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3', 'E3']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F2', 'A2', 'C3', 'A2']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G2', 'B2', 'D3', 'B2']] +
             [{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3', 'E3']])
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La balada casi completa · ♩≈72, arpegio como una ola', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
