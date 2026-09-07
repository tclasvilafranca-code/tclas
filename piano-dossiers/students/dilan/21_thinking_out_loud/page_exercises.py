# -*- coding: utf-8 -*-
"""Taller de practica - Thinking Out Loud (Dilan, cancion 21, Re mayor,
   4/4). Estructura DISTINTA otra vez: la partitura real va rapida
   (♩=145) con corcheas continuas -- el foco es la IGUALDAD, que ninguna
   corchea se coma a la otra ni se atropelle, distinto del "sube la
   velocidad poco a poco" que se trabajara en My Favourite Things."""
from page_layout_common import *

SONG_KICKER = 'DILAN · JUNIO · THINKING OUT LOUD (ED SHEERAN)'
TS = (4, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['E2', 'A2', 'C#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Ed Sheeran en Re mayor, pero rápida (♩≈145). El reto: corcheas perfectamente iguales.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F#4', 3), ('A4', 5), ('G4', 4), ('E4', 2), ('D4', 1), ('E4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Mezcla de saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 5), ('D4', 1), ('F#4', 3), ('D4', 1)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, desde el La', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Corcheas iguales: ni carreras ni tropiezos', 2,
                          'A tempo rápido, el error más común es que las corcheas se aceleren solas o se atropellen entre ellas. Cuenta "1-y-2-y-3-y-4-y" por dentro, tocando cada corchea exactamente igual de larga.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D4', 'E4', 'F#4', 'G4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'a) Escalera de corcheas, sin acelerar', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'G4', 'F#4', 'E4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) La escalera al revés, misma igualdad', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D4', 'E4', 'F#4', 'G4'] * 4)]
    bass2c = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(RE, 'Re'), (SOL, 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Corcheas rápidas sobre un acorde largo y sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los acordes básicos, largos y sostenidos bajo las corcheas.')
    y -= 11
    pattern_a = [(RE, 'Re'), (LA, 'La'), (SOL, 'Sol'), (RE, 'Re')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La-Re, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, corcheas iguales con acordes largos, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · corcheas sobre acorde sostenido', 2,
                          'La izquierda suena larga, casi como si estuviera atada de un compás al siguiente; la derecha corre por encima, igual todo el rato.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D4', 'E4', 'F#4', 'G4'] * 4)]
    bass4 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(RE, 'Re'), (SOL, 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) Corcheas iguales sobre acorde largo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'La igualdad con acordes que cambian más rápido', 3,
                          'Ahora el acorde de abajo cambia cada dos tiempos: la izquierda tiene que moverse sin que la derecha pierda su igualdad.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'G4', 'F#4', 'E4'] * 4)]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(RE, 'Re'), (LA, 'La'), (SOL, 'Sol'), (RE, 'Re')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Corcheas iguales, acordes cada dos tiempos', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Thinking Out Loud casi entera', 3,
                          'Con la partitura al lado: si notas que te aceleras, para y vuelve a empezar más despacio. La igualdad importa más que la velocidad.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D4', 'E4', 'F#4', 'G4'] * 2)]
    treb6 += [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['A4', 'G4', 'F#4', 'E4'] * 2)]
    bass6 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(RE, 'Re'), (SOL, 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · ♩≈145', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
