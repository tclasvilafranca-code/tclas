# -*- coding: utf-8 -*-
"""Taller de practica - Poema de Amor (Dilan, cancion 19, Sol menor, 4/4).
   Estructura DISTINTA otra vez: la partitura real empieza marcada
   "Recitado" -- sin pulso fijo, como si se hablara. Eso es DISTINTO del
   rubato estructurado de Adagio en Sol menor (que tenia una forma
   concreta de ensanchar la frase): aqui la libertad es total, mas cerca
   de la declamacion que de la musica medida."""
from page_layout_common import *

SONG_KICKER = 'DILAN · MAYO · POEMA DE AMOR (JOAN MANUEL SERRAT)'
TS = (4, 4)

SOLm = ['G2', 'Bb2', 'D3']
RE7 = ['D3', 'F#3', 'C4']
FA = ['F2', 'A2', 'C3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Serrat en Sol menor. Empieza "Recitado": sin pulso fijo, como hablando.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol menor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Sib(3) Do(4) Re(5). El dedo 3 toca la tecla negra Sib.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('Bb4', 3), ('G4', 1), ('A4', 2), ('C5', 4), ('Bb4', 3), ('D5', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Mezcla de saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D5', 5), ('Bb4', 3), ('G4', 1), ('Bb4', 3)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol menor, desde el Re', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Recitado: tocar sin pulso fijo, como si hablaras', 2,
                          'Esto no es rubato con una forma concreta: es libertad total, como declamar un poema. Alarga las notas largas, pasa rápido por las cortas, y no midas con el metrónomo en la cabeza.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': d} for p, d in [('D5', 'e'), ('D5', 'e'), ('C5', 'q'), ('Bb4', 'q.'), ('C5', 'e')]]
    y = system_block(c, x0, w0, y, gap, 'a) Recitado: sin pulso fijo, como si hablaras', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C5', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, ahora con pulso fijo — compara', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': d} for p, d in [('D5', 'e'), ('D5', 'e'), ('C5', 'q'), ('Bb4', 'q.'), ('C5', 'e')]] * 2
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOLm, 'Solm'), (RE7, 'Re7')] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La libertad de la voz, sobre el acorde sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes de Sol menor con el Re7 de verdad', 2,
                          'Solm–Re7–Solm–Fa: el Re7 lleva Fa sostenido, la sensible que tira hacia Sol.')
    y -= 11
    pattern_a = [(SOLm, 'Solm'), (RE7, 'Re7'), (SOLm, 'Solm'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Solm-Re7-Solm-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, el recitado con acordes que cambian, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el recitado sobre el acorde', 2,
                          'La izquierda sostiene; la derecha declama libre, sin pulso fijo.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': d} for p, d in [('D5', 'e'), ('D5', 'e'), ('C5', 'q'), ('Bb4', 'q.'), ('C5', 'e')]] * 2
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOLm, 'Solm'), (RE7, 'Re7')] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) El recitado sobre Solm y Re7', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'De lo libre a lo medido', 3,
                          'Primero el recitado sin pulso; luego la misma frase, pero ya con el pulso de la canción. Siente cómo cambia el carácter.')
    y -= 11
    treb5a = [{'pitch': p, 'dur': d} for p, d in [('D5', 'e'), ('D5', 'e'), ('C5', 'q'), ('Bb4', 'q.'), ('C5', 'e')]]
    y = system_block(c, x0, w0, y, gap, 'a) Libre: como se habla', treb5a, clef='treble', time_sig=TS)

    treb5b = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C5', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'b) Medido: ya con pulso, como se canta', treb5b, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Poema de Amor casi entero', 3,
                          'Con la partitura al lado: dale al principio la libertad del recitado, y luego entra en el pulso.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': d} for p, d in [('D5', 'e'), ('D5', 'e'), ('C5', 'q'), ('Bb4', 'q.'), ('C5', 'e')]]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C5', 'Bb4', 'D5', 'D5', 'C5', 'Bb4']]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(SOLm, 'Solm'), (RE7, 'Re7'), (SOLm, 'Solm'), (FA, 'Fa'), (SOLm, 'Solm'), (RE7, 'Re7')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · Andante', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
