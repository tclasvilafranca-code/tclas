# -*- coding: utf-8 -*-
"""Taller de practica - What Was I Made For? (Eva, cancion 3, Do mayor, 4/4).
   Mismo arreglo que el de Dilan (que cuenta los silencios), pero enfoque
   DISTINTO para Eva: el TOQUE MUY SUAVE. Esta balada vive en un pianissimo
   casi constante -- el reto es controlar el sonido sin que se pierda ni se
   escape, tocando siempre muy cerca de la tecla."""
from page_layout_common import *

SONG_KICKER = 'EVA · OCTUBRE · WHAT WAS I MADE FOR? (BILLIE EILISH)'
TS = (4, 4)


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada muy sencilla en Do mayor. El reto: tocar muy suave sin perder el control del sonido.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas, sonido claro y desnudo.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('E4', 3), ('D4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sin ningún golpe', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado, muy suave', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El toque casi sin peso: pianissimo de verdad', 2,
                          'La dificultad exacta de esta canción. Toca tan cerca de la tecla que casi no la sientas bajar del todo, pero sin que la nota deje de sonar clara.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase completa, sin ningún acento accidental', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'D4', 'E4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Notas largas: aguanta el pianissimo sin que se apague de golpe', ev2b, clef='treble', time_sig=TS)

    pattern_c = [(['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa'),
                 (['E2', 'G2', 'B2'], 'Mim'), (['C3', 'E3', 'G3'], 'Do')]
    ev2c = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_c]
    y = system_block(c, x0, w0, y, gap, 'c) El acompañamiento: acordes largos, casi un susurro', ev2c, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes básicos, aquí más movidos que en la canción real.')
    y -= 9
    pattern_a = [(['C3', 'E3', 'G3'], 'Do'), (['G2', 'B2', 'D3'], 'Sol'),
                 (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Sol-Fa-Do, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = []
    for root, up, lab in [('C2', ['E3', 'G3'], 'Do'), ('G2', ['B2', 'D3'], 'Sol'),
                            ('F2', ['A2', 'C3'], 'Fa'), ('C2', ['E3', 'G3'], 'Do')]:
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
    c.drawString(MARGIN, y, 'Ahora junta las manos: deja que el acorde sostenga a la melodía, siempre en pianissimo.')
    y -= 15
    gap = 7.0
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el mismo volumen todo el rato', 2,
                          'La izquierda sostiene el acorde largo, sin peso; la derecha canta encima, igual de suave, sin que ninguna de las dos suba de golpe.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4']]
    bass1 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(['C3', 'E3', 'G3'], 'Do'), (['E2', 'G2', 'B2'], 'Mim')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase con su acorde, en equilibrio suave', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in
             ['C4', 'C4', 'C4', 'D4', 'C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4', 'C4', 'E4', 'D4', 'E4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando el volumen exacto', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia dinámica · la izquierda no se mueve', 3,
                          'La izquierda mantiene el mismo acorde sin cambiar de volumen; la derecha se mueve un poco más, pero sin romper el pianissimo general.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': v} for p, v in
             [('E4', 'q'), ('D4', 'q'), ('C4', 'h'), ('D4', 'q'), ('E4', 'q'), ('C4', 'h')]]
    bass3 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde no se mueve; la melodía respira encima', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['C4', 'E4', 'D4', 'F4', 'E4', 'G4', 'F4', 'E4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía en corcheas, sin perder el volumen bajo', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · casi la canción entera', 3,
                          'Con la partitura al lado: mantén el pianissimo de principio a fin, sin que ninguna nota se escape más fuerte.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'C4',
              'D4', 'C4', 'B3', 'C4', 'E4', 'E4', 'D4', 'C4', 'C4', 'C4', 'D4', 'C4']]
    bass5 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in
             [(['C3', 'E3', 'G3'], 'Do'), (['E2', 'G2', 'B2'], 'Mim'), (['F2', 'A2', 'C3'], 'Fa'),
              (['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Lento ♩≈78, pianissimo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
