# -*- coding: utf-8 -*-
"""Taller de practica - When I Was Your Man (Sandi, cancion 10,
   Bruno Mars, Do mayor -- armadura sin alteraciones, aunque los
   acordes en bloque llevan alteraciones cromaticas distintas casi
   en cada uno, mismo archivo que Dilan y Eva, 4/4). Nivel avanzado:
   los acordes en bloque con alteraciones distintas -- lectura
   armonica rapida."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · WHEN I WAS YOUR MAN'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
MIm7 = ['E2', 'G2', 'B2', 'D3']
LAb = ['Ab2', 'C3', 'Eb3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'When I Was Your Man, de Bruno Mars, en Do mayor. Hoy: los acordes en bloque con alteraciones distintas.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Punto de partida antes de leer los acordes cromáticos.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido completo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los acordes en bloque con alteraciones distintas', 3,
                          'La dificultad de hoy. La canción presenta acordes en bloque, uno tras otro, cada uno con su propia alteración cromática: hay que leer e identificar el color de cada acorde al instante, sin pararse a pensar cada nota.')
    y -= 9
    ev2a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(MIm7, 'Mim7'), (LAb, 'Lab')]]
    y = system_block(c, x0, w0, y, gap, 'a) Dos acordes en bloque, cada uno con su propio color: léelos de un vistazo', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (FA, 'Fa')]]
    y = system_block(c, x0, w0, y, gap, 'b) Vuelta a lo conocido: el contraste hace más evidente el color cromático anterior', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['G4', 'Ab4']]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(MIm7, 'Mim7'), (LAb, 'Lab')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía siguiendo el color de cada acorde en bloque', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: la base diatónica sobre la que se apoyan los acordes cromáticos.')
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: identifica cada acorde en bloque al instante, sin perder el pulso de la melodía.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde de Mi menor 7', 3,
                          'La izquierda sostiene el acorde de Mi menor 7, con su color propio; la derecha canta encima, leyendo el color sin dudar.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G4']]
    bass1 = [{'pitches': MIm7, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Mi menor 7, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Lab no descoloca la lectura', 3,
                          'La izquierda toca el acorde de Lab, un color ajeno a Do mayor; la derecha mantiene su línea, identificando el cambio sin arrastrarse.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['Ab4', 'C5', 'Eb5', 'C5']]
    bass3 = [{'pitches': LAb, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre Lab; el color cromático queda claro', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['Eb5', 'C5', 'Ab4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en otro orden', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · When I Was Your Man casi entera', 3,
                          'Con la partitura al lado: lee cada acorde en bloque al instante, sin pararte a pensar cada nota por separado.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['Ab4', 'C5', 'Eb5', 'C5']])
    bass5 = [{'pitches': MIm7, 'dur': 'w'}, {'pitches': LAb, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'When I Was Your Man casi completa · lectura armónica rápida', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
