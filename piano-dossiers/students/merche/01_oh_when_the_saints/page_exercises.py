# -*- coding: utf-8 -*-
"""Taller de practica - Oh, When the Saints (Merce, cancion 1,
   arr. Gilbert DeBenedetti, Do mayor, 4/4). Mismo arreglo que el
   de Julia, pero con un enfoque distinto y propio: el silencio
   que cuenta -- el bajo entra justo despues del silencio, en su
   sitio exacto. Nivel basico pero solido, tono adulto."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · OH, WHEN THE SAINTS'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un clásico espiritual americano, en Do mayor. Hoy trabajamos la precisión del silencio antes de entrar.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Localiza el Do central como punto de referencia.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El silencio que cuenta: el bajo entra a tiempo', 2,
                          'Lo que trabajamos hoy. El acompañamiento de la izquierda empieza con un silencio de negra: hay que contarlo con la misma precisión que una nota.')
    y -= 9
    ev2a = [{'rest': True, 'dur': 'q'}] + [{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3']] + \
           [{'rest': True, 'dur': 'q'}] + [{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3']]
    y = system_block(c, x0, w0, y, gap, 'a) El silencio, y la entrada justo después', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'C3', 'E3', 'G3', 'C3', 'C3', 'E3', 'G3']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea sin silencio, para comparar la diferencia', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4']]
    bass2c = [{'rest': True, 'dur': 'q'}] + [{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Manos juntas: silencio abajo, melodía arriba sin parar', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: la melodía canta la letra mientras el bajo entra tras su silencio.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el bajo con silencio', 2,
                          'La derecha canta la frase "Oh, when the saints"; la izquierda entra tras su silencio de negra, en el acorde de Fa.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4']]
    bass1 = [{'rest': True, 'dur': 'q'}] + [{'pitches': FA, 'dur': 'q'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El bajo entra tras el silencio, sobre Fa', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el silencio no descoloca la melodía', 3,
                          'La izquierda cuenta su silencio con calma; la derecha sigue cantando su frase sin esperarla.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4']]
    bass3 = [{'rest': True, 'dur': 'q'}] + [{'pitches': SOL, 'dur': 'q'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El bajo entra tras el silencio, sobre Sol', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Oh, When the Saints casi entera', 3,
                          'Con la partitura al lado: cuenta el silencio con precisión y entra en el tiempo exacto.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'D4']] +
             [{'pitch': 'C4', 'dur': 'w'}])
    bass5 = ([{'rest': True, 'dur': 'q'}] + [{'pitches': DO, 'dur': 'q'}] * 3 +
             [{'pitches': DO, 'dur': 'w'}])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Oh, When the Saints casi completa · con el silencio que cuenta', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
