# -*- coding: utf-8 -*-
"""Taller de practica - Soldadito de Hierro (Valentina, cancion 4, La
   menor, 4/4, mismo archivo que Dilan, Eva y Sandi). Nivel medio, un
   poco mas exigente: el tresillo en la mano izquierda -- firme
   mientras la derecha canta arriba."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · SOLDADITO DE HIERRO (NIL MOLINER)'
TS = (4, 4)

AM = ['A2', 'C3']
DM = ['D2', 'F2', 'A2']
E7 = ['E2', 'G#2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción en La menor. Hoy: el tresillo pasa a la izquierda, mientras la derecha canta.')
    y -= 15
    gap = 7.35
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Misma armadura que Do mayor, pero el centro tonal es La.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('C5', 3), ('B4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, con soltura', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('E5', 5), ('C5', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El tresillo en la izquierda: firme mientras la derecha canta', 2,
                          'La dificultad de hoy. El grupo de tres ya no está en la melodía: ahora vive en la izquierda, como un motor que no para.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['A3', 'C3', 'E3'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'a) Solo la izquierda: el tresillo, firme y regular', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'D4', 'C4', 'B4', 'A4', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Sola la derecha: la melodía larga, que canta encima', ev2b, clef='treble', time_sig=TS)
    y -= 3

    ev2c = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['D3', 'F3', 'A3'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'c) El mismo tresillo, un escalón más arriba: Re-Fa-La', ev2c, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V7 en La menor', 2,
                          'Lam–Rem–Mi7: los acordes de esta tonalidad menor, con el Sol sostenido del Mi7.')
    y -= 9
    pattern_a = [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mi7-Lam, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: la izquierda no para en tresillos, la derecha canta tranquila arriba.')
    y -= 15
    gap = 7.05
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la izquierda vuela, la derecha canta', 2,
                          'La izquierda se mueve ligera en tresillos; la derecha sostiene la melodía larga, sin prisa.')
    y -= 8
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'D4', 'C4', 'B4', 'A4', 'C5']]
    bass1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['A3', 'C3', 'E3'] * 8)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La izquierda vuela; la derecha canta arriba', grand_gap_mult=7.3, time_sig=TS)
    y -= 3

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['E3', 'C3', 'A3'] * 8)]
    y = system_block(c, x0, w0, y, gap, 'b) Solo el tresillo, para sentir su vuelo', treb2, clef='bass', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 5, 'Independencia rítmica · la melodía no se contagia', 3,
                          'La izquierda no para de moverse en tresillos; la derecha sostiene cada nota larga sin cortarla.')
    y -= 8
    treb3 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'C5', 'B4', 'A4', 'C5', 'B4']]
    bass3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['D3', 'F3', 'A3'] * 8)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La derecha sostiene; la izquierda no para', grand_gap_mult=7.3, time_sig=TS)
    y -= 3

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma melodía, en negras tranquilas', treb4, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 6, 'Reto final · Soldadito de Hierro, con la izquierda viva', 3,
                          'Con la partitura al lado: el tresillo firme abajo, la melodía tranquila arriba.')
    y -= 8
    treb5 = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'D4', 'C4', 'B4', 'A4', 'C5']]
    bass5 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
             ['A3', 'C3', 'E3'] * 4 + ['D3', 'F3', 'A3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Enérgico ♩≈84, izquierda firme', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
