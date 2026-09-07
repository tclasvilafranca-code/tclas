# -*- coding: utf-8 -*-
"""Taller de practica - Bela Ciao (Luisa, cancion 1, arr. Anderson
   Miranda Fernandes, Sol mayor -- armadura de 1 sostenido, 2/4).
   Nivel hobby, sin complicaciones: el silencio antes de empezar,
   sin prisa."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · BELA CIAO'
TS = (2, 4)

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D2', 'F#2', 'A2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Bela Ciao, en Sol mayor. Hoy, sin prisa: el silencio antes de empezar cada frase.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5). Tranquila, solo el Fa# es distinto.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El silencio antes de empezar: sin prisa', 2,
                          'Lo de hoy. Muchas frases empiezan con un pequeño silencio: no hay que ponerse nervioso, solo esperar tranquila y entrar cuando toque.')
    y -= 9
    ev2a = [{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['D4', 'G4', 'B4']] + \
           [{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['D4', 'G4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'a) Espera, y entra tranquila', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e'} for p in ['D4', 'G4', 'B4', 'D4', 'D4', 'G4', 'B4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase sin el silencio: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['D4', 'G4', 'B4']]
    bass2c = [{'pitches': SOL, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El silencio, con el acorde de Sol debajo, tranquilo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad, sin más complicación.')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Re-Sol, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: el acorde espera mientras la melodía entra tranquila.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde de Do', 2,
                          'La izquierda sostiene el acorde entero, tranquila; la derecha entra después de su silencio.')
    y -= 7
    treb1 = [{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['C4', 'E4', 'G4']]
    bass1 = [{'pitches': DO, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El silencio sobre Do, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['C4', 'E4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · sin prisa, cada mano a su ritmo', 3,
                          'La izquierda espera con su acorde de Re; la derecha entra tranquila después de su silencio.')
    y -= 7
    treb3 = [{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['A4', 'D5', 'F#5']]
    bass3 = [{'pitches': RE, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El silencio sobre Re, sin agobios', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e'} for p in ['A4', 'D5', 'F#5', 'A5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, sin el silencio', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Bela Ciao casi entera', 3,
                          'Con la partitura al lado: tranquila, entra después de cada silencio, sin prisa.')
    y -= 7
    treb5 = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['D4', 'G4', 'B4']] +
             [{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['C4', 'E4', 'G4']])
    bass5 = [{'pitches': SOL, 'dur': 'h'}, {'pitches': DO, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Bela Ciao casi completa · con calma, sin prisa', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
