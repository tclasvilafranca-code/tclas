# -*- coding: utf-8 -*-
"""Taller de practica - La Primavera (Oriol, cancion 2, Vivaldi,
   version facil, Do mayor, 4/4, mismo archivo que Luisa). Nivel
   medio, sin agobiar: el fluir constante -- notas iguales, sin
   detenerse."""
from page_layout_common import *

SONG_KICKER = 'ORIOL · NIVEL MEDIO · LA PRIMAVERA (VIVALDI)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La Primavera, de Vivaldi (versión fácil), en Do mayor. Hoy: el fluir constante, sin detenerse.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El fluir constante: notas iguales, sin detenerse', 2,
                          'Lo de hoy. Esta melodía fluye en corcheas continuas, como el agua de un arroyo: cada nota dura exactamente lo mismo, sin pararse ni acelerarse.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) El fluir constante, subiendo y bajando', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e'} for p in ['E4', 'F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Un escalón más arriba, con el mismo flujo constante', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    bass2c = [{'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El fluir constante sobre el acorde de Do, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes, sin más complicación.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: mantén el flujo constante mientras suena el acorde.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el fluir constante sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde de Fa, tranquila; la derecha fluye encima, sin detenerse.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El fluir constante sobre Fa, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e'} for p in ['Bb4', 'A4', 'G4', 'F4', 'G4', 'A4', 'Bb4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, bajando: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Sol no interrumpe el flujo', 3,
                          'La izquierda sostiene su acorde de Sol sin moverse; la derecha sigue fluyendo, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'A4']]
    bass3 = [{'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El fluir constante sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e'} for p in ['C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · La Primavera casi entera', 3,
                          'Con la partitura al lado: mantén el flujo constante de principio a fin, sin agobios.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']] +
             [{'pitch': p, 'dur': 'e'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']])
    bass5 = [{'pitches': DO, 'dur': 'w'}, {'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La Primavera casi completa · el fluir constante, sin detenerse', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
