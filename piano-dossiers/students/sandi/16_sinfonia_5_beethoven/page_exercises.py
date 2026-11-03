# -*- coding: utf-8 -*-
"""Taller de practica - Sinfonia No.5 (Sandi, cancion 16, Beethoven,
   1er movimiento simplificado Level 3, Do menor -- armadura de 3
   bemoles (Sib, Mib, Lab) confirmada por render directo, 2/4,
   Allegro con brio). Nivel avanzado, reto final: el motivo del
   destino -- la repeticion exacta entre las manos."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · SINFONÍA Nº5 (BEETHOVEN) · RETO FINAL'
TS = (2, 4)

DOm = ['C2', 'Eb2', 'G2']
FAm = ['F2', 'Ab2', 'C3']
SOLm = ['G2', 'Bb2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Sinfonía Nº5, de Beethoven, en Do menor. Reto final: el motivo del destino.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do menor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mib(3) Fa(4) Sol(5). El Sib, Mib y Lab son las alteraciones de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('Eb4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'Eb4', 'G4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El motivo del destino: la repetición exacta entre las manos', 3,
                          'La dificultad de hoy, y el reto final del cuaderno. El famoso motivo (corto-corto-corto-largo) lo presenta una mano, y la otra lo repite exactamente igual, como un eco: el ritmo y la intensidad deben coincidir nota por nota.')
    y -= 9
    ev2a = [{'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'Eb4', 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'a) El motivo original: corto-corto-corto-largo, con f decidido', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'b) El eco, un escalón más abajo: exactamente el mismo ritmo', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'Eb4', 'dur': 'h'}]
    bass2c = [{'rest': True, 'dur': 'e'}, {'pitch': 'G3', 'dur': 'e'}, {'pitch': 'G3', 'dur': 'e'}, {'pitch': 'G3', 'dur': 'e'}, {'pitch': 'Eb3', 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El motivo a la vez en las dos manos, en octavas: idéntico ritmo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en Do menor', 2,
                          'Dom–Fam–Solm: los tres acordes principales de esta tonalidad menor.')
    y -= 11
    pattern_a = [(DOm, 'Dom'), (FAm, 'Fam'), (SOLm, 'Solm'), (DOm, 'Dom')]
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Dom-Fam-Solm-Dom, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el eco entre las manos debe sonar como una sola voz que se repite.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el motivo y su eco, encadenados', 3,
                          'La derecha presenta el motivo; la izquierda responde con el mismo ritmo exacto, un escalón más abajo, como si fuera la misma voz continuando.')
    y -= 7
    treb1 = [{'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'Eb4', 'dur': 'h'}]
    bass1 = [{'rest': True, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': DOm, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El motivo arriba, con el acorde de Do menor esperando debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'b) El eco que sigue: mismo ritmo exacto, un escalón más abajo', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Fa menor no distorsiona el eco', 3,
                          'La izquierda sostiene el acorde de Fa menor; la derecha repite el motivo con la misma precisión rítmica, sin dejarse influir por el acorde de abajo.')
    y -= 7
    treb3 = [{'rest': True, 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'Ab4', 'dur': 'h'}]
    bass3 = [{'pitches': FAm, 'dur': 'h'}, {'pitches': FAm, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El motivo sobre el acorde de Fa menor, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'Eb4', 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'b) Vuelta al motivo original: para comparar la precisión', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Sinfonía Nº5 casi entera', 3,
                          'Con la partitura al lado: el motivo y su eco deben sonar como una única idea que rebota entre las manos, con la misma fuerza y el mismo ritmo exacto.')
    y -= 7
    treb5 = ([{'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'Eb4', 'dur': 'h'}] +
             [{'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'h'}])
    bass5 = [{'rest': True, 'dur': 'h'}, {'pitches': DOm, 'dur': 'h'}, {'rest': True, 'dur': 'h'}, {'pitches': SOLm, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Sinfonía Nº5 casi completa · el motivo del destino, exacto entre las manos', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
