# -*- coding: utf-8 -*-
"""Taller de practica - Como entrenar a tu dragon, tema de vuelo
   (Jose Maria, cancion 21, empieza en Do mayor y modula a Re
   mayor). Enfoque relajado: el vuelo tranquilo -- las notas se
   mueven rapido, pero la muneca se queda quieta y relajada
   (distinto del enfoque de modulacion usado con Josep para la
   misma pieza)."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · JUNIO · CÓMO ENTRENAR A TU DRAGÓN (TEMA DE VUELO)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']
Am = ['A2', 'C3', 'E3']
RE = ['D3', 'F#3', 'A3']
SOLD = ['G3', 'B3', 'D4']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de vuelo de "Cómo entrenar a tu dragón". Sin prisa: las notas vuelan, la muñeca no.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas, sin prisa.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] + \
           [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'G4', 'E4', 'G4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El vuelo tranquilo: las notas se mueven, la muñeca no', 2,
                          'Lo que vamos a cuidar en esta pieza. Las notas vuelan rápido de una a otra, pero la muñeca se queda quieta y relajada — el vuelo viene de los dedos, no de la muñeca.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 8} for i, p in
            enumerate((['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']) * 2)]
    y = system_block(c, x0, w0, y, gap, 'a) El vuelo de corcheas, con la muñeca quieta', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Las mismas notas, tranquilas: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 8} for i, p in
              enumerate((['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']) * 2)]
    bass2c = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El vuelo sobre el acorde de Do, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la primera parte', 2,
                          'Do–Sol–Fa–Lam: los acordes de la sección en Do mayor.')
    y -= 11
    pattern_a = [(DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (Am, 'Lam')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Sol-Fa-Lam, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el vuelo pasa por las dos tonalidades, muñeca siempre quieta.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · en Do mayor, sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha vuela con sus corcheas, sin que la muñeca se mueva.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 8} for i, p in
             enumerate((['F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4', 'E4']) * 2)]
    bass1 = [{'pitches': FA, 'dur': 'h.'}, {'pitches': FA, 'dur': 'q'}, {'pitches': FA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El vuelo sobre Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · ya en Re mayor, sobre el acorde de Sol', 3,
                          'La izquierda sostiene el nuevo acorde, quieta; la derecha vuela ya instalada en la nueva tonalidad, con la muñeca relajada.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 8} for i, p in
             enumerate((['G4', 'A4', 'B4', 'A4', 'G4', 'F#4', 'E4', 'F#4']) * 2)]
    bass3 = [{'pitches': SOLD, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El vuelo en Re mayor sobre Sol, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F#4', 'E4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, tranquila', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · el momento del cambio de tonalidad', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que el vuelo pase de Do mayor a Re mayor con la muñeca siempre relajada.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 8} for i, p in
              enumerate((['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4']) * 2)] +
             [{'pitch': p, 'dur': 'e', 'beam': i // 8} for i, p in
              enumerate((['D4', 'E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'E4']) * 2)])
    bass5 = ([{'pitches': DO, 'dur': 'h.'}, {'pitches': DO, 'dur': 'q'}, {'pitches': DO, 'dur': 'w'}] +
             [{'pitches': RE, 'dur': 'h.'}, {'pitches': RE, 'dur': 'q'}, {'pitches': RE, 'dur': 'w'}])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · el vuelo pasando de Do mayor a Re mayor', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
