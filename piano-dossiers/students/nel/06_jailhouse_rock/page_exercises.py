# -*- coding: utf-8 -*-
"""Taller de practica - Jailhouse Rock (Nel, cancion 6, Do mayor,
   4/4). Angulo: la DIGITACION FIJA -- la izquierda repite siempre el
   mismo patron de dedos 5-3-2-1 al saltar de un acorde a otro, tal
   como marca la partitura real."""
from page_layout_common import *

SONG_KICKER = 'NEL · DICIEMBRE · JAILHOUSE ROCK (ELVIS PRESLEY)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3', 'C4']
FA = ['F2', 'A2', 'C3', 'F3']
SOL = ['G2', 'B2', 'D3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Elvis Presley en Do mayor. El reto: la izquierda repite siempre el mismo patrón de dedos.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('D4', 2), ('G4', 5), ('F4', 4), ('E4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La digitación fija: 5-3-2-1, siempre igual', 2,
                          'La dificultad exacta de esta canción. La izquierda salta de acorde en acorde, pero la forma de la mano y el orden de los dedos (5-3-2-1) no cambian nunca.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'number': n, 'beam': i // 4} for i, (p, n) in
            enumerate([('C3', 5), ('E3', 3), ('G3', 2), ('C4', 1)] * 2)]
    y = system_block(c, x0, w0, y, gap, 'a) Sobre Do: 5-3-2-1, subiendo y repitiendo', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'number': n, 'beam': i // 4} for i, (p, n) in
            enumerate([('F2', 5), ('A2', 3), ('C3', 2), ('F3', 1)] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) La misma forma, saltando a Fa', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'G4', 'F4', 'E4', 'G4', 'G4', 'F4', 'E4']]
    bass2c = [{'pitch': p, 'dur': 'e', 'number': n, 'beam': i // 4} for i, (p, n) in
              enumerate([('G2', 5), ('B2', 3), ('D3', 2), ('G3', 1)] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Sobre Sol: la misma forma, otra vez', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes de esta tonalidad, la base de la digitación fija.')
    y -= 11
    pattern_a = [(['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa'),
                 (['G2', 'B2', 'D3'], 'Sol'), (['C3', 'E3', 'G3'], 'Do')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la digitación fija de la izquierda no cambia aunque la melodía se mueva.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la digitación fija sostiene la melodía', 2,
                          'La izquierda repite su patrón 5-3-2-1 sin dudar; la derecha canta encima con el carácter marcado de un rock and roll.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'G4', 'F4', 'E4', 'G4', 'G4', 'F4', 'E4']]
    bass1 = [{'pitch': p, 'dur': 'e', 'number': n, 'beam': i // 4} for i, (p, n) in
             enumerate([('C3', 5), ('E3', 3), ('G3', 2), ('C4', 1)] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre el patrón fijo de Do', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'G4', 'F4', 'E4', 'D4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando su forma', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el patrón no se rompe al cambiar de acorde', 3,
                          'La izquierda salta de Do a Fa a Sol sin perder nunca el orden 5-3-2-1; la derecha se mueve libre encima.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['G4', 'E4', 'F4', 'D4', 'E4', 'C4', 'D4', 'C4'] * 2)]
    bass3 = [{'pitch': p, 'dur': 'e', 'number': n, 'beam': i // 4} for i, (p, n) in
             enumerate([('F2', 5), ('A2', 3), ('C3', 2), ('F3', 1), ('G2', 5), ('B2', 3), ('D3', 2), ('G3', 1)] * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda cambia de acorde sin cambiar de forma', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la escala completa, con marcha', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Jailhouse Rock casi entera', 3,
                          'Con la partitura al lado: deja que la izquierda encuentre sola su forma 5-3-2-1 en cada acorde nuevo.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['G4', 'G4', 'F4', 'E4', 'G4', 'G4', 'F4', 'E4', 'E4', 'D4', 'C4', 'G4', 'F4', 'E4', 'D4', 'C4']]
    bass5 = [{'pitch': p, 'dur': 'e', 'number': n, 'beam': i // 4} for i, (p, n) in
             enumerate([('C3', 5), ('E3', 3), ('G3', 2), ('C4', 1)] * 4 +
                       [('F2', 5), ('A2', 3), ('C3', 2), ('F3', 1)] * 2 +
                       [('G2', 5), ('B2', 3), ('D3', 2), ('G3', 1)] * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈150, con swing', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
