# -*- coding: utf-8 -*-
"""Taller de practica - Can't Help Falling in Love (Dilan, cancion 1 de 5, Re mayor, 3/4)
   Tema: el acompanamiento de vals arpegiado en la izquierda sosteniendo una
   melodia de notas largas en la derecha -- independencia total entre manos."""
from page_layout_common import *

SONG_KICKER = 'DILAN · SEPTIEMBRE · CAN’T HELP FALLING IN LOVE'
TS = (3, 4)


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un vals lento en Re mayor: la izquierda mece el arpegio sin parar mientras la derecha canta notas largas.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('F#4', 3), ('E4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sintiendo el Fa#', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('F#4', 3), ('A4', 5), ('F#4', 3)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, desgranado', ev1b, clef='treble', time_sig=TS)

    ev1c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('D4', 2), ('E4', 2), ('E4', 3), ('F#4', 3), ('F#4', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'c) Repetida, cambiando de dedo', ev1c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El vals arpegiado: la izquierda no para nunca', 2,
                          'La dificultad exacta de esta canción (compases 1-4). Aprende primero el dibujo de la izquierda solo, como un péndulo automático.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
            ['D3', 'F#3', 'A3', 'F#3', 'D4', 'A3'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'a) Solo la izquierda: el péndulo del vals, sin parar', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.', 'number': n} for p, n in
            [('D4', 1), ('D4', 1), ('E4', 2), ('F#4', 3)]]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la derecha: notas largas, contando 1-2-3 por dentro', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
            ['D4', 'F#4', 'A4', 'F#4', 'D4', 'A4'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'c) El mismo péndulo, una octava más arriba', ev2c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes de esta tonalidad. El bajo del vals se apoya siempre en ellos.')
    y -= 12
    pattern_a = [(['D3', 'F#3', 'A3'], 'Re'), (['G2', 'B2', 'D3'], 'Sol'), (['E2', 'A2', 'C#3'], 'La')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = []
    for chord_low, chord_up, lab in [(['D2'], ['F#3', 'A3'], 'Re'), (['G2'], ['B2', 'D3'], 'Sol'),
                                       (['A2'], ['A2', 'C#3'], 'La'), (['D2'], ['F#3', 'A3'], 'Re')]:
        pattern_b.append({'pitches': chord_low, 'dur': 'q', 'label': lab})
        pattern_b.append({'pitches': chord_up, 'dur': 'q'})
        pattern_b.append({'pitches': chord_up, 'dur': 'q'})
    y = system_block(c, x0, w0, y, gap, 'b) Bajo-acorde-acorde: el vals de verdad', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos de verdad: deja que la izquierda mezca mientras la derecha canta, tranquila.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía flota sobre el vals', 2,
                          'La izquierda mantiene el péndulo sin dudar; la derecha suelta cada nota larga y la deja sonar.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'h.', 'number': n} for p, n in [('D4', 1), ('F#4', 3), ('E4', 2), ('D4', 1)]]
    bass1 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['D3', 'F#3', 'A3', 'F#3', 'D4', 'A3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Frase A, notas largas sobre el péndulo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4']]
    treb2 += [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F#4', 'E4']]
    treb2 += [{'pitch': 'D4', 'dur': 'h.'}, {'pitch': 'F#4', 'dur': 'h.'}]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: mezcla de negras y notas largas', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia rítmica · la derecha se queda quieta', 3,
                          'La izquierda sigue meciendo el vals sin fallar; la derecha sostiene y no se mueve hasta que toque cambiar.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'h.', 'number': n} for p, n in [('A4', 5), ('A4', 5), ('G4', 4), ('F#4', 3)]]
    bass3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['D3', 'F#3', 'A3', 'F#3', 'D4', 'A3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La derecha aguanta arriba, sin prisa', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4'] * 3)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía en corcheas, más viva', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · la canción casi entera', 3,
                          'Con la partitura al lado: deja que el vals fluya solo en la izquierda y no lo pienses más.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'h.', 'number': n} for p, n in [('D4', 1), ('F#4', 3), ('E4', 2), ('D4', 1)]]
    treb5 += [{'pitch': p, 'dur': 'h.', 'number': n} for p, n in [('A4', 5), ('A4', 5), ('G4', 4), ('F#4', 3)]]
    bass5 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['D3', 'F#3', 'A3', 'F#3', 'D4', 'A3'] * 8)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción completa · ♩≈72, con calma', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
