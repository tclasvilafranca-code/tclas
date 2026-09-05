# -*- coding: utf-8 -*-
"""Taller de practica - The Swan / El Cisne (Eva, cancion 2, Sol mayor, 3/4).
   Mismo arreglo que el de Dilan (que trabaja el legato), pero enfoque
   DISTINTO para Eva: el control de la DINAMICA. Un cisne desliza sin hacer
   ruido -- el reto es mantener el volumen bajo y estable de principio a fin,
   sin que ningun golpe accidental "salpique" el sonido."""
from page_layout_common import *

SONG_KICKER = 'EVA · SEPTIEMBRE · THE SWAN (SAINT-SAËNS)'
TS = (3, 4)


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una pieza clásica en Sol mayor. El reto: deslizarse sin hacer ruido, con el volumen siempre bajo control.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento de matices: la misma frase, mp y pp', 1,
                          'Toca esta frase dos veces con las mismas notas: primero mezzopiano (mp), controlado; luego pianissimo (pp), casi un susurro.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('B4', 3), ('A4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Mezzopiano (mp): con cuerpo, pero sin golpear', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('B4', 3), ('A4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Pianissimo (pp): la misma frase, casi un susurro', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El agua nunca hace ruido: dinámica estable de principio a fin', 2,
                          'La dificultad exacta de esta canción. No es tocar flojo un momento: es mantenerlo flojo TODO el rato, sin que ninguna nota se escape más fuerte que las demás.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja sin que ninguna nota "salpique" más fuerte', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
            ['G3', 'D4', 'B3', 'D4', 'G3', 'B3'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda fluye igual de bajito, sin acentos', ev2b, clef='bass', time_sig=TS)

    ev2c = [{'pitch': p, 'dur': 'h.'} for p in ['D5', 'C5', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'c) Notas largas: aguanta el volumen sin que decaiga de golpe', ev2c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad, tan elegantes como la melodía.')
    y -= 12
    pattern_a = [(['G3', 'B3', 'D4'], 'Sol'), (['D3', 'F#3', 'A3'], 'Re'), (['C3', 'E3', 'G3'], 'Do')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Re-Do, un acorde por tiempo, siempre piano', eva, clef='bass', time_sig=TS)

    pattern_b = [('D3', 'Sol'), ('B2', None), ('G2', None), ('G3', 'Do'), ('E3', None), ('C3', None),
                 ('A3', 'Re'), ('F#3', None), ('D3', None), ('D3', 'Sol'), ('B2', None), ('G2', None)]
    evb = [{'pitch': p, 'dur': 'q', 'label': l} for p, l in pattern_b]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, arpegiados nota a nota', evb, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: las dos igual de flojitas, sin que ninguna tape a la otra.')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · dos voces, un solo volumen', 2,
                          'La izquierda fluye y la derecha canta, pero ninguna de las dos debe sonar más que la otra: equilibrio total.')
    y -= 8
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4']] + [{'pitch': 'C5', 'dur': 'h.'}]
    bass1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['G3', 'D4', 'B3', 'D4', 'G3', 'B3'] * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Frase entera, las dos manos en equilibrio', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando el volumen exacto', treb2, clef='treble', time_sig=TS)
    y -= 2

    y = exercise_heading(c, y, 5, 'Independencia dinámica · una mano crece, la otra no', 3,
                          'La izquierda se queda siempre igual de bajito; la derecha hace un crescendo pequeño y vuelve a bajar, sin arrastrar a la otra mano.')
    y -= 8
    treb3 = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'B4', 'D5', 'B4', 'G4', 'A4']]
    bass3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['G3', 'D4', 'B3', 'D4', 'G3', 'B3'] * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La derecha crece un poco y vuelve; la izquierda no se mueve de sitio', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'A4', 'G4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un escalón más abajo', treb4, clef='treble', time_sig=TS)
    y -= 2

    y = exercise_heading(c, y, 6, 'Reto final · El Cisne casi entero', 3,
                          'Con la partitura al lado: deja que la izquierda fluya como el agua y la derecha cante sin nunca subir el volumen de golpe.')
    y -= 8
    treb5 = [{'pitch': 'C5', 'dur': 'h.'}] + [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4']]
    treb5 += [{'pitch': 'A4', 'dur': 'h.'}] + [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5']]
    bass5 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['G3', 'D4', 'B3', 'D4', 'G3', 'B3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Andante ♩≈96, siempre suave', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
