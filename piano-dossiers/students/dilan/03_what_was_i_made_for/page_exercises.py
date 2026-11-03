# -*- coding: utf-8 -*-
"""Taller de practica - What Was I Made For? (Dilan, cancion 3 de 5, Do mayor, 4/4)
   Tema: contar los compases de silencio y entrar en el momento exacto -- la
   melodia deja mucho espacio vacio antes de "hablar"."""
from page_layout_common import *

SONG_KICKER = 'DILAN · OCTUBRE · WHAT WAS I MADE FOR? (BILLIE EILISH)'
TS = (4, 4)


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada muy sencilla en Do mayor. El reto: contar los silencios y entrar en el momento exacto.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento rítmico: cuenta y aplaude el silencio', 1,
                          'Antes de tocar ninguna nota, entrena el reloj interno: cuenta en voz alta y aplaude solo en las negras marcadas, dejando los silencios completamente vacíos.')
    y -= 12
    ev1a = ([{'pitch': 'C4', 'dur': 'q'}, {'pitch': 'C4', 'dur': 'q'},
              {'rest': True, 'dur': 'q'}, {'rest': True, 'dur': 'q'}] * 4)
    y = system_block(c, x0, w0, y, gap, 'a) Aplaude-aplaude-silencio-silencio, cuatro veces seguidas', ev1a, clef='treble', time_sig=TS)

    ev1b = ([{'rest': True, 'dur': 'w'}] +
            [{'pitch': 'C4', 'dur': 'q'}] * 4) * 2
    y = system_block(c, x0, w0, y, gap, 'b) Un compás entero de silencio, luego entra seguro', ev1b, clef='treble', time_sig=TS)

    ev1c = ([{'pitch': 'C4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}] * 8)
    y = system_block(c, x0, w0, y, gap, 'c) Entradas cortas y rápidas: aplaude-silencio, sin perder el pulso', ev1c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Contar el silencio y entrar en su sitio', 2,
                          'La dificultad exacta de esta canción. Cuenta los compases vacíos por dentro, como si ya estuvieras tocando, y entra sin dudar.')
    y -= 12
    ev2a = ([{'rest': True, 'dur': 'w'}] * 2 +
            [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'D4', 'C4']] +
            [{'pitch': 'C4', 'dur': 'h'}, {'pitch': 'C4', 'dur': 'h'}])
    y = system_block(c, x0, w0, y, gap, 'a) Dos compases vacíos, cuenta y entra', ev2a, clef='treble', time_sig=TS)

    ev2b = ([{'rest': True, 'dur': 'w'}] + [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4']]) * 2
    y = system_block(c, x0, w0, y, gap, 'b) Un compás de silencio, uno de melodía, alternando', ev2b, clef='treble', time_sig=TS)

    pattern_c = [(['C3', 'E3', 'G3'], 'Do'), (['E2', 'G2', 'B2'], 'Mim'),
                 (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do')]
    ev2c = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_c]
    y = system_block(c, x0, w0, y, gap, 'c) El acompañamiento: acordes largos y quietos', ev2c, clef='bass', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes básicos, aquí más movidos que en la canción real.')
    y -= 12
    pattern_a = [(['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa'),
                 (['G2', 'B2', 'D3'], 'Sol'), (['C3', 'E3', 'G3'], 'Do')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = []
    for root, up, lab in [('C2', ['E3', 'G3'], 'Do'), ('F2', ['A2', 'C3'], 'Fa'),
                            ('G2', ['B2', 'D3'], 'Sol'), ('C2', ['E3', 'G3'], 'Do')]:
        pattern_b.append({'pitch': root, 'dur': 'q', 'label': lab})
        pattern_b.append({'pitches': up, 'dur': 'q'})
        pattern_b.append({'pitches': up, 'dur': 'q'})
        pattern_b.append({'pitches': up, 'dur': 'q'})
    y = system_block(c, x0, w0, y, gap, 'b) Bajo-acorde-acorde-acorde, apoyado', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: deja que el acorde sostenga el silencio hasta que la melodía entre.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · entra en tu momento exacto', 2,
                          'La izquierda sostiene el acorde largo; la derecha cuenta el silencio por dentro y entra sin dudar.')
    y -= 11
    treb1 = ([{'rest': True, 'dur': 'w'}] * 2 +
             [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'D4', 'C4']] +
             [{'pitch': 'C4', 'dur': 'h'}, {'pitch': 'C4', 'dur': 'h'}])
    bass1 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(['C3', 'E3', 'G3'], 'Do'), (['E2', 'G2', 'B2'], 'Mim'),
              (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase completa, con su silencio inicial', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in
             ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4', 'D4', 'C4', 'C4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin los silencios (para memorizarla)', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia rítmica · precisión al entrar', 3,
                          'La izquierda no se mueve del acorde; la derecha entra y sale con precisión de reloj.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': v} for p, v in
             [('E4', 'q'), ('D4', 'q'), ('C4', 'h'), ('D4', 'q'), ('E4', 'q'), ('C4', 'h'),
              ('F4', 'q'), ('E4', 'q'), ('D4', 'h'), ('E4', 'q'), ('D4', 'q'), ('C4', 'h')]]
    bass3 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa'),
              (['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde no se mueve; la melodía sí', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['C4', 'E4', 'D4', 'F4', 'E4', 'G4', 'F4', 'E4'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía en corcheas, más fluida', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · casi la canción entera', 3,
                          'Con la partitura al lado: no adelantes la entrada, deja que el silencio pese lo que tiene que pesar.')
    y -= 11
    treb5 = ([{'rest': True, 'dur': 'w'}] * 2 +
             [{'pitch': p, 'dur': 'q'} for p in
              ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4',
               'D4', 'C4', 'B3', 'C4', 'E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'C4']])
    bass5 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(['C3', 'E3', 'G3'], 'Do'), (['E2', 'G2', 'B2'], 'Mim'), (['F2', 'A2', 'C3'], 'Fa'),
              (['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do'),
              (['G2', 'B2', 'D3'], 'Sol'), (['C3', 'E3', 'G3'], 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Lento ♩≈78, con calma', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
