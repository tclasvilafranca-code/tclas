# -*- coding: utf-8 -*-
"""Taller de practica - Hello (Sandi, cancion 11, Adele, Mi menor
   -- armadura de 1 sostenido, Fa#, confirmada por render directo,
   4/4, ♩=78). Nivel avanzado: la anacrusa que anticipa -- entrar
   justo antes del tiempo fuerte, sin prisa."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · HELLO (ADELE)'
TS = (4, 4)

Em = ['E2', 'G2', 'B2']
SOL = ['G2', 'B2', 'D3']
RE = ['D2', 'F#2', 'A2']
DO = ['C2', 'E2', 'G2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Hello, de Adele, en Mi menor. Hoy: la anacrusa que anticipa, entrando antes del tiempo fuerte.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El Fa# es la única alteración de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('B4', 5), ('A4', 4), ('G4', 3), ('F#4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido completo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'E5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La anacrusa que anticipa: entrar antes del tiempo fuerte', 3,
                          'La dificultad de hoy. La melodía entra justo antes del primer tiempo del compás siguiente, como quien toma impulso: hay que sentir ese adelanto sin apresurarlo ni retrasarlo.')
    y -= 9
    ev2a = [{'rest': True, 'dur': 'h.'}, {'pitch': 'B4', 'dur': 'q'}]
    y = system_block(c, x0, w0, y, gap, 'a) Silencio largo, y la anacrusa entra justo en el último tiempo', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': 'B4', 'dur': 'q'}, {'pitch': 'E5', 'dur': 'h.'}]
    y = system_block(c, x0, w0, y, gap, 'b) La anacrusa resuelve en la nota larga del compás siguiente', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'rest': True, 'dur': 'h.'}, {'pitch': 'B4', 'dur': 'q'}, {'pitch': 'E5', 'dur': 'h.'}, {'rest': True, 'dur': 'q'}]
    bass2c = [{'pitches': Em, 'dur': 'w'}, {'pitches': Em, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La anacrusa completa, sobre el acorde de Mi menor sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–VI–VII en Mi menor', 2,
                          'Mim–Do–Re: la conocida progresión de esta canción, típica del pop.')
    y -= 11
    pattern_a = [(Em, 'Mim'), (SOL, 'Sol'), (RE, 'Re'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mim-Sol-Re-Do, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: la anacrusa debe sonar con la misma calma que el resto de la frase.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la anacrusa sobre el acorde de Sol', 3,
                          'La izquierda sostiene el acorde de Sol, tranquila; la derecha anticipa la entrada justo antes del tiempo fuerte, sin apresurarse.')
    y -= 7
    treb1 = [{'rest': True, 'dur': 'h.'}, {'pitch': 'D5', 'dur': 'q'}, {'pitch': 'G5', 'dur': 'h.'}, {'rest': True, 'dur': 'q'}]
    bass1 = [{'pitches': SOL, 'dur': 'w'}, {'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La anacrusa sobre Sol, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'rest': True, 'dur': 'h.'}, {'pitch': 'D5', 'dur': 'q'}, {'pitch': 'G5', 'dur': 'h.'}, {'rest': True, 'dur': 'q'}]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: comprueba que la entrada no se adelanta', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Re no adelanta la anacrusa', 3,
                          'La izquierda sostiene el acorde de Re, firme; la derecha entra en su momento exacto, sin dejarse arrastrar por el bajo.')
    y -= 7
    treb3 = [{'rest': True, 'dur': 'h.'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'D5', 'dur': 'h.'}, {'rest': True, 'dur': 'q'}]
    bass3 = [{'pitches': RE, 'dur': 'w'}, {'pitches': RE, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La anacrusa sobre Re; la entrada no se adelanta', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'D5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Contraste: la misma melodía, sin anacrusa, para sentir la diferencia', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Hello casi entera', 3,
                          'Con la partitura al lado: siente cada anacrusa como un impulso natural, sin prisa ni retraso.')
    y -= 7
    treb5 = ([{'rest': True, 'dur': 'h.'}, {'pitch': 'B4', 'dur': 'q'}, {'pitch': 'E5', 'dur': 'h.'}, {'rest': True, 'dur': 'q'}] +
             [{'rest': True, 'dur': 'h.'}, {'pitch': 'D5', 'dur': 'q'}, {'pitch': 'G5', 'dur': 'h.'}, {'rest': True, 'dur': 'q'}])
    bass5 = [{'pitches': Em, 'dur': 'w'}, {'pitches': Em, 'dur': 'w'}, {'pitches': SOL, 'dur': 'w'}, {'pitches': SOL, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Hello casi completa · la anacrusa que anticipa, sin prisa', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
