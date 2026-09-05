# -*- coding: utf-8 -*-
"""Taller de practica - The Sound of Silence (Luisa, cancion 26,
   Simon & Garfunkel, Re menor -- armadura de 1 bemol (Sib)
   confirmada por render directo, 4/4). Nivel hobby, sin
   complicaciones: el silencio que habla -- para escuchar por
   dentro."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · THE SOUND OF SILENCE'
TS = (4, 4)

REm = ['D3', 'F3', 'A3']
SOLm = ['G2', 'Bb2', 'D3']
LAm = ['A2', 'C3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'The Sound of Silence, de Simon & Garfunkel, en Re menor. Hoy: el silencio que habla.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re menor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa(3) Sol(4) La(5). El Sib es la única alteración de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('F4', 3), ('E4', 2), ('D4', 1), ('E4', 2), ('F4', 3), ('E4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'F4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El silencio que habla: para escuchar por dentro', 2,
                          'Lo de hoy. Esta canción tiene un ambiente tranquilo y reflexivo: no hay que complicarse, solo escucharla despacio, como quien escucha el silencio.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'F4', 'D4', 'E4', 'F4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) La melodía reflexiva, con calma', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'F4', 'D4', 'E4', 'F4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, muy despacio: escuchando el silencio', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'F4']]
    bass2c = [{'pitches': REm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre el acorde de Re menor, tranquilo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en Re menor', 2,
                          'Rem–Solm–Lam: los tres acordes de esta tonalidad, sin más complicación.')
    y -= 11
    pattern_a = [(REm, 'Rem'), (SOLm, 'Solm'), (LAm, 'Lam'), (REm, 'Rem')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Rem-Solm-Lam-Rem, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: escucha el silencio entre las notas.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el acorde de Sol menor', 2,
                          'La izquierda sostiene el acorde de Sol menor, tranquila; la derecha canta encima, con calma.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Bb4', 'D5', 'Bb4']]
    bass1 = [{'pitches': SOLm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Sol menor, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Bb4', 'D5', 'Bb4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · sin agobios, cada mano tranquila', 3,
                          'La izquierda sostiene su acorde de La menor sin moverse; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5', 'C5']]
    bass3 = [{'pitches': LAm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre La menor; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'C5', 'A4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · The Sound of Silence casi entera', 3,
                          'Con la partitura al lado: escucha el silencio entre las notas, sin agobios.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'F4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Bb4', 'D5', 'Bb4']])
    bass5 = [{'pitches': REm, 'dur': 'w'}, {'pitches': SOLm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'The Sound of Silence casi completa · escuchando, sin agobios', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
