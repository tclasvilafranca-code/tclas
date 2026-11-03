# -*- coding: utf-8 -*-
"""Taller de practica - Adagio en Sol menor (Valentina, cancion 10,
   Albinoni, Sol menor, 3/4, mismo archivo que Dilan). Nivel medio,
   un poco mas exigente: el ligado real -- cambiar de dedo sin que se
   note, sin cortar el sonido."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · ADAGIO EN SOL MENOR (ALBINONI)'
TS = (3, 4)

SOLm = ['G2', 'Bb2', 'D3']
DOm = ['C3', 'Eb3', 'G3']
REm = ['D3', 'F3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una pieza barroca lenta en Sol menor. Hoy: el ligado real, cambiando de dedo sin cortar.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Control del sonido sostenido: escucha cómo se apaga', 1,
                          'Toca cada nota una sola vez y escúchala apagarse por completo antes de pasar a la siguiente, sin prisa.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'h.', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('Bb4', 3), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Una nota por compás entero, escuchando el silencio después', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': v, 'number': n} for p, v, n in
            [('G4', 'h', 1), ('A4', 'q', 2), ('Bb4', 'h', 3), ('A4', 'q', 2),
             ('G4', 'h', 1), ('A4', 'q', 2), ('Bb4', 'h', 3), ('C5', 'q', 4)]]
    y = system_block(c, x0, w0, y, gap, 'b) Dos notas ligadas por compás, sin ningún golpe entre ellas', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El ligado real: cambiar de dedo sin que se note', 2,
                          'Lo de hoy. Para ligar de verdad, a veces hay que sustituir un dedo por otro sobre la misma tecla, sin volver a tocarla: el sonido no se corta ni un instante.')
    y -= 12
    ev2a = [{'pitch': 'G4', 'dur': 'h.', 'number': n} for n in [1, 2, 3]]
    y = system_block(c, x0, w0, y, gap, 'a) La misma tecla, cambiando de dedo por dentro: 1-2-3', ev2a, clef='treble', time_sig=TS)

    frase = [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('D5', 5), ('C5', 4), ('Bb4', 3), ('A4', 2), ('G4', 1)]
    ev2b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in frase]
    y = system_block(c, x0, w0, y, gap, 'b) La frase entera, sin cortar el sonido entre notas', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitch': p, 'dur': 'q'} for p in ['G3', 'A3', 'Bb3', 'C4', 'D4', 'C4', 'Bb3', 'A3', 'G3']]
    y = system_block(c, x0, w0, y, gap, 'c) La misma frase, una octava abajo, en la izquierda', ev2c, clef='bass', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en Sol menor', 2,
                          'Solm–Dom–Rem: un acorde por compás entero, tan largo y quieto como pide el Adagio.')
    y -= 11
    pattern_a = [(SOLm, 'Solm'), (DOm, 'Dom'), (REm, 'Rem'), (SOLm, 'Solm')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Solm-Dom-Rem-Solm, un acorde por compás', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, el ligado real en toda la frase, y el Adagio casi entero.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía ligada flota sobre los acordes', 2,
                          'La izquierda sostiene el acorde largo; la derecha canta por encima, sin ningún corte.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': d} for p, d in
             [('D5', 'q'), ('C5', 'q'), ('Bb4', 'q'), ('A4', 'h.'), ('G4', 'q'), ('A4', 'q'), ('Bb4', 'q'), ('A4', 'h.')]]
    bass1 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(SOLm, 'Solm'), (DOm, 'Dom'), (REm, 'Rem'), (SOLm, 'Solm')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase completa, con los acordes debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El ligado bajo el acorde que se mueve', 3,
                          'La izquierda cambia de acorde sin sobresaltos; la derecha mantiene el sonido ligado todo el tiempo.')
    y -= 11
    treb5a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('Bb4', 3), ('A4', 2)]]
    bass5a = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(SOLm, 'Solm'), (DOm, 'Dom')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5a, bass5a, 'a) Melodía ligada sobre el cambio de acorde', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Adagio en Sol menor casi entero, ligado', 3,
                          'Con la partitura al lado: cuida el ligado real de principio a fin, sin cortes.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4', 'G4']]
    treb6 += [{'pitch': p, 'dur': d} for p, d in
              [('G4', 'q'), ('A4', 'q'), ('Bb4', 'q'), ('C5', 'h.'), ('D5', 'q'), ('C5', 'q'), ('Bb4', 'q'), ('G4', 'h.')]]
    bass6 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(SOLm, 'Solm'), (DOm, 'Dom'), (REm, 'Rem'), (SOLm, 'Solm'),
              (DOm, 'Dom'), (REm, 'Rem'), (SOLm, 'Solm')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'El Adagio casi completo · ♩≈54, ligado de principio a fin', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
