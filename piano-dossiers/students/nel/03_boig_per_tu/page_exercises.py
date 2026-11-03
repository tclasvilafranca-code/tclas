# -*- coding: utf-8 -*-
"""Taller de practica - Boig per tu (Nel, cancion 3, La menor, 4/4).
   Angulo: el RITMO PUNTEADO -- el vaiven caracteristico de corchea
   con puntillo + semicorchea que recorre toda la melodia real."""
from page_layout_common import *

SONG_KICKER = 'NEL · OCTUBRE · BOIG PER TU (SAU)'
TS = (4, 4)

LAm = ['A2', 'C3', 'E3']
REm = ['D3', 'F3', 'A3']
MI = ['E3', 'G#3', 'B3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Sau en La menor. El reto: el vaivén del ritmo punteado que recorre toda la melodía.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('B4', 2), ('D5', 4), ('C5', 3), ('E5', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('E5', 5), ('C5', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El ritmo punteado: ese vaivén tan característico', 2,
                          'La dificultad exacta de esta canción. Corchea con puntillo y semicorchea: la primera nota "se estira" y la segunda llega rápida y corta detrás.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': d} for p, d in
            [('E4', 'q.'), ('D4', 'e'), ('C4', 'q'), ('B3', 'q.'), ('A3', 'e'), ('C4', 'q')] +
            [('E4', 'q.'), ('D4', 'e'), ('C4', 'q'), ('B3', 'q.'), ('A3', 'e'), ('C4', 'q')]]
    y = system_block(c, x0, w0, y, gap, 'a) Larga-corta, larga-corta: el vaivén punteado', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'B3', 'A3', 'C4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, sin puntillo: para sentir la diferencia', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': d} for p, d in
              [('E4', 'q.'), ('D4', 'e'), ('C4', 'q'), ('B3', 'q.'), ('A3', 'e'), ('C4', 'q')] * 2]
    bass2c = [{'pitches': p, 'dur': 'h'} for p in [LAm, LAm, REm, LAm, MI, LAm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El punteado sobre el acorde firme debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en La menor', 2,
                          'Lam–Rem–Mi: los tres acordes de esta tonalidad. El Mi lleva un Sol# — la sensible que empuja hacia La.')
    y -= 11
    pattern_a = [(LAm, 'Lam'), (REm, 'Rem'), (MI, 'Mi'), (LAm, 'Lam')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mi-Lam, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el punteado se apoya en acordes largos y firmes debajo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el punteado sobre el acorde firme', 2,
                          'La izquierda sostiene el acorde entero, sin prisa; la derecha marca claramente el vaivén largo-corto de cada pareja de notas.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': d} for p, d in
             [('E4', 'q.'), ('D4', 'e'), ('C4', 'q'), ('B3', 'q.'), ('A3', 'e'), ('C4', 'q')] * 2]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [LAm, REm, MI, LAm, REm, LAm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El vaivén punteado, con el acorde debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'B4', 'D5', 'C5', 'E5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin puntillo: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del vaivén', 3,
                          'La izquierda queda perfectamente quieta con notas largas; la derecha marca el ritmo punteado sin que la de abajo se apresure.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': d} for p, d in
             [('C5', 'q.'), ('B4', 'e'), ('A4', 'q'), ('E4', 'q.'), ('D4', 'e'), ('C4', 'q')] * 2]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [LAm, MI, LAm, MI, LAm, MI]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El punteado vuela; el acorde no se altera', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'B4', 'A4', 'E4', 'D4', 'C4', 'B3', 'A3']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un escalón más abajo', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Boig per tu casi entera', 3,
                          'Con la partitura al lado: marca siempre con claridad la diferencia entre la nota larga y la corta del punteado.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': d} for p, d in
             [('E4', 'q.'), ('D4', 'e'), ('C4', 'q'), ('B3', 'q.'), ('A3', 'e'), ('C4', 'q'),
              ('E4', 'q.'), ('D4', 'e'), ('C4', 'q'), ('B3', 'q.'), ('A3', 'e'), ('C4', 'q')] +
             [('C5', 'q.'), ('B4', 'e'), ('A4', 'q'), ('E4', 'q.'), ('D4', 'e'), ('C4', 'q'), ('E4', 'q'), ('A4', 'q')]]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [LAm, REm, MI, LAm, LAm, MI, LAm, REm, MI, LAm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈92, con el punteado siempre claro', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
