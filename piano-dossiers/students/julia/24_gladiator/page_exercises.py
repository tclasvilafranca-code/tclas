# -*- coding: utf-8 -*-
"""Taller de practica - Honor Him / Gladiator (Julia, cancion 24,
   Hans Zimmer, arreglo facil verificado en Re mayor -- armadura de
   2 sostenidos, F# y C#, NO La mayor como sugeria el catalogo
   inicial -- 3/4). Nivel inicial con toque extra: la tonalidad
   nueva de Re mayor, con sus dos sostenidos guardianes."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · GLADIATOR (HONOR HIM)'
TS = (3, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['A2', 'C#3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de Gladiator, de Hans Zimmer, en Re mayor. Hoy: ¡una tonalidad nueva, con dos sostenidos!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). ¡El Fa# es una tecla negra!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('F#4', 3), ('E4', 2), ('D4', 1), ('E4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los dos sostenidos que cuidan la casa', 2,
                          'Lo que vamos a practicar hoy. El Fa sostenido y el Do sostenido son las dos llaves que guardan la tonalidad de Re mayor: no los olvides ni una vez.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) El Fa sostenido, guardián de la escalera', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C#5', 'D5', 'C#5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) El Do sostenido, guardián de arriba', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4']]
    bass2c = [{'pitches': RE, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El acorde de Re, con sus dos sostenidos, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La-Re, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el acorde sostenido cuida los sostenidos mientras la melodía canta.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde de Sol', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta con sus sostenidos encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F#4']]
    bass1 = [{'pitches': SOL, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Sol, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin acorde: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · los sostenidos no mueven el acorde', 3,
                          'La izquierda queda quieta con su acorde; la derecha toca sus sostenidos sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C#5', 'B4', 'A4', 'G4']]
    bass3 = [{'pitches': LA, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Los sostenidos sobre La; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C#5', 'D5', 'E5', 'D5', 'C#5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Gladiator casi entera', 3,
                          'Con la partitura al lado: ¡no olvides los dos sostenidos que guardan la tonalidad!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C#5', 'D5', 'C#5', 'B4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [RE, RE, SOL, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Gladiator casi completa · con los sostenidos guardianes', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
