# -*- coding: utf-8 -*-
"""Taller de practica - Lucia (Dilan, cancion 18, La menor, 4/4).
   Estructura DISTINTA otra vez: la partitura real reparte cada acorde en
   un dibujo de "olas" en la izquierda (no lo toca de golpe) -- un
   acompañamiento arpegiado tipo bajo de Alberti, nunca trabajado antes
   en un dosier de Dilan."""
from page_layout_common import *

SONG_KICKER = 'DILAN · MAYO · LUCÍA (JOAN MANUEL SERRAT)'
TS = (4, 4)

AM = ['C3', 'E3', 'A3']
DM = ['D2', 'F2', 'A2']
E7 = ['E2', 'G#2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Serrat en La menor. La izquierda no toca los acordes de golpe: los reparte en olas.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'La ola de la izquierda: preparando el bajo de Alberti', 1,
                          'Antes de acompañar la canción, aprende el dibujo de ola solo, en la mano izquierda: raíz-quinta-tercera-quinta, una y otra vez, sin pararte.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q'} for p in ['A2', 'E3', 'C3', 'E3'] * 3]
    y = system_block(c, x0, w0, y, gap, 'a) Ola pequeña en La menor: raíz-quinta-tercera-quinta', ev1a, clef='bass', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['A2', 'E3', 'C3', 'A3', 'E3', 'C3', 'E3', 'A2'] * 1 + ['A2', 'E3', 'C3', 'E3']]
    y = system_block(c, x0, w0, y, gap, 'b) Ola más amplia: la misma idea, abarcando una octava entera', ev1b, clef='bass', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El acompañamiento en olas', 2,
                          'La izquierda no toca el acorde entero de golpe: lo reparte en un dibujo que sube y baja, como una ola pequeña que se repite todo el rato.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A2', 'C3', 'A2', 'C3'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'a) La menor: raíz-tercera, raíz-tercera', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D2', 'A2', 'F2', 'A2'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Re menor: el mismo dibujo, otra base', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'A4', 'C5'] * 2]
    bass2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A2', 'C3', 'A2', 'C3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La ola por debajo de la melodía', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V7 en La menor', 2,
                          'Lam–Rem–Mi7: el Mi7 lleva Sol sostenido, la sensible que tira hacia La.')
    y -= 11
    pattern_a = [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mi7-Lam, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas con la ola, la ola con acordes que cambian, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · melodía sobre la ola', 2,
                          'La izquierda repite su dibujo de ola; la derecha canta la melodía por encima.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('C5', 3), ('D5', 4), ('B4', 2), ('E5', 5), ('D5', 4), ('A4', 1), ('B4', 2), ('C5', 3)]]
    bass4 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A2', 'C3', 'A2', 'C3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La melodía sobre la ola', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'La ola cambia de acorde cada compás', 3,
                          'La misma ola, pero cambiando de acorde en cada compás: Lam, luego Rem, luego Mi7. La forma es igual, la base cambia.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'A4', 'C5', 'A4', 'C5', 'A4', 'C5']]
    bass5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A2', 'C3', 'A2', 'C3'] * 2)] +
             [{'pitch': p, 'dur': 'e', 'beam': i // 4 + 2} for i, p in enumerate(['D2', 'A2', 'F2', 'A2'] * 2)])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Lam y Rem, cada uno con su ola', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Lucía casi entera', 3,
                          'Con la partitura al lado: deja que la ola de la izquierda fluya sin pararse a pensar en cada nota.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('C5', 3), ('D5', 4), ('B4', 2), ('E5', 5), ('D5', 4), ('A4', 1), ('B4', 2), ('C5', 3)]]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'A4', 'C5', 'A4', 'C5', 'A4', 'C5']]
    bass6 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(
             (['A2', 'C3', 'A2', 'C3'] * 2 + ['D2', 'A2', 'F2', 'A2'] * 2) * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · ♩≈78', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
