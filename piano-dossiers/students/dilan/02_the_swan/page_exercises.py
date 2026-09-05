# -*- coding: utf-8 -*-
"""Taller de practica - The Swan / El Cisne (Dilan, cancion 2 de 5, Sol mayor, 3/4)
   Tema: el legato de verdad -- conectar cada nota con la siguiente sin cortar
   el sonido, mientras la izquierda fluye como el agua."""
from page_layout_common import *

SONG_KICKER = 'DILAN · SEPTIEMBRE · THE SWAN (SAINT-SAËNS)'
TS = (3, 4)


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una pieza clásica en Sol mayor. El reto: el legato de verdad, sin cortar el sonido entre notas.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Escala ligada: cada nota nace de la anterior', 1,
                          'Nada de calentamiento por bloques hoy: practica la escala de Sol como una sola frase continua, sin ningún corte de sonido entre una nota y la siguiente.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('D5', 5), ('C5', 4), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4)]]
    y = system_block(c, x0, w0, y, gap, 'a) Subiendo ligado, sin parar el sonido', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D5', 5), ('C5', 4), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('D5', 5), ('C5', 4), ('B4', 3), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'b) Bajando ligado, sin parar el sonido', ev1b, clef='treble', time_sig=TS)

    ev1c = [{'pitch': p, 'dur': 'q'} for p in
            ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'c) La escala completa, subiendo y bajando de un tirón', ev1c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El legato de verdad: sin cortes entre notas', 2,
                          'La dificultad exacta de esta canción. Cada nota "nace" de la anterior: no levantes el dedo hasta que el siguiente ya esté apoyado.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in
            ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'a) Escala legato: sin huecos, sin golpes', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
            ['G3', 'B3', 'D4', 'B3', 'G3', 'D4'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: el agua que fluye, sin parar', ev2b, clef='bass', time_sig=TS)

    ev2c = ([{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4']] + [{'pitch': 'C5', 'dur': 'h.'}] +
            [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'B4']] + [{'pitch': 'A4', 'dur': 'h.'}])
    y = system_block(c, x0, w0, y, gap, 'c) La frase real: movimiento + nota larga que se apaga sola', ev2c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad, tan elegantes como la melodía.')
    y -= 12
    pattern_a = [(['G3', 'B3', 'D4'], 'Sol'), (['C3', 'E3', 'G3'], 'Do'), (['D3', 'F#3', 'A3'], 'Re')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Re, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [('G2', 'Sol'), ('B2', None), ('D3', None), ('C3', 'Do'), ('E3', None), ('G3', None),
                 ('D3', 'Re'), ('F#3', None), ('A3', None), ('G2', 'Sol'), ('B2', None), ('D3', None)]
    evb = [{'pitch': p, 'dur': 'q', 'label': l} for p, l in pattern_b]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, arpegiados nota a nota', evb, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: deja que la melodía flote, tranquila, sobre el agua que fluye abajo.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía flota sobre el agua', 2,
                          'La izquierda fluye sin parar; la derecha canta cada frase legato, sin cortar el sonido.')
    y -= 11
    treb1 = ([{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4']] + [{'pitch': 'C5', 'dur': 'h.'}] +
             [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'B4']] + [{'pitch': 'A4', 'dur': 'h.'}])
    bass1 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['G3', 'B3', 'D4', 'B3', 'G3', 'D4'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase completa, muy ligada', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in
             ['D5', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para memorizar el legato', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia rítmica · el agua no para', 3,
                          'La izquierda mantiene el acorde sostenido; la derecha se mueve sola, fluida, sin apoyarse en ella.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['G4', 'A4', 'B4', 'A4', 'G4', 'B4'] * 4)]
    bass3 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(['G2', 'B2', 'D3'], 'Sol'), (['C3', 'E3', 'G3'], 'Do'),
              (['D3', 'F#3', 'A3'], 'Re'), (['G2', 'B2', 'D3'], 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda sostiene; la derecha fluye', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['G4', 'B4', 'C5', 'B4', 'A4', 'G4'] * 3)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía en corcheas ligadas', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · El Cisne casi entero', 3,
                          'Con la partitura al lado: legato de verdad, sin prisa, dejando que cada frase respire.')
    y -= 11
    treb5 = (([{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4']] + [{'pitch': 'C5', 'dur': 'h.'}] +
              [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'B4']] + [{'pitch': 'A4', 'dur': 'h.'}]) * 2)
    bass5 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['G3', 'B3', 'D4', 'B3', 'G3', 'D4'] * 8)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La pieza casi completa · Andante ♩≈96, muy ligado', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
