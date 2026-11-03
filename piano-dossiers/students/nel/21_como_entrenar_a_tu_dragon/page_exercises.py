# -*- coding: utf-8 -*-
"""Taller de practica - Como entrenar a tu dragon, tema de vuelo
   (Nel, cancion 21, empieza en Do mayor y modula a Re mayor).
   Enfoque: el cambio de armadura -- la tonalidad cambia a mitad de
   camino, y hay que sentir el nuevo centro tonal."""
from page_layout_common import *

SONG_KICKER = 'NEL · JUNIO · CÓMO ENTRENAR A TU DRAGÓN (TEMA DE VUELO)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
Am = ['A2', 'C3', 'E3']
RE = ['D3', 'F#3', 'A3']
SOLD = ['G3', 'B3', 'D4']
LA = ['A3', 'C#4', 'E4']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de vuelo de "Cómo entrenar a tu dragón". El reto: la tonalidad cambia a mitad de camino.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('G4', 5), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El cambio de armadura: la tonalidad cambia a mitad de camino', 2,
                          'La dificultad exacta de esta canción. La pieza empieza en Do mayor y, a mitad de camino, se desplaza a Re mayor — hay que sentir el nuevo centro tonal, no solo leer las alteraciones nuevas.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'G4', 'E4', 'D4', 'C4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase, en Do mayor', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'A4', 'F#4', 'E4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, ahora en Re mayor: el cambio de armadura', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'A4', 'F#4', 'E4', 'D4', 'E4']]
    bass2c = [{'pitches': RE, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase en Re mayor sobre el acorde de Re, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la primera parte', 2,
                          'Do–Fa–Sol–Lam: los acordes de la sección en Do mayor.')
    y -= 11
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (Am, 'Lam')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Lam, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, en las dos tonalidades: siente el nuevo centro cuando cambie la armadura.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · en Do mayor, sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta la frase en Do mayor.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'C5', 'A4', 'G4', 'F4', 'G4']]
    bass1 = [{'pitches': FA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase en Do mayor sobre Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'G4', 'A4', 'C5', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, en Do mayor: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · ya en Re mayor, sobre el acorde de La', 3,
                          'La izquierda sostiene el nuevo acorde, quieta; la derecha canta ya instalada en la nueva tonalidad, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C#5', 'E5', 'C#5', 'B4', 'A4', 'B4']]
    bass3 = [{'pitches': LA, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase en Re mayor sobre La; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'C#5', 'D5', 'E5', 'F#5', 'E5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · el momento del cambio de tonalidad', 3,
                          'Con la partitura al lado: siente cómo la música se desplaza de Do mayor a Re mayor sin perder el hilo.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'G4', 'E4', 'D4', 'C4', 'D4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'A4', 'F#4', 'E4', 'D4', 'E4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, DO, RE, RE]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · el momento exacto del cambio de tonalidad', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
