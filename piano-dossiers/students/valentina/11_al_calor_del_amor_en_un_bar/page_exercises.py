# -*- coding: utf-8 -*-
"""Taller de practica - Al Calor del Amor en un Bar (Valentina,
   cancion 11, Mi menor, 4/4, mismo archivo que Dilan). Nivel medio,
   un poco mas exigente: la subida cromatica hacia el estribillo --
   una escala de semitonos que empuja hacia el clímax."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · AL CALOR DEL AMOR EN UN BAR (GABINETE CALIGARI)'
TS = (4, 4)

MIm = ['E3', 'G3', 'B3']
LAm = ['C3', 'E3', 'A3']
SIm = ['D3', 'F#3', 'B3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de rock español en Mi menor. Hoy: la subida cromática hacia el estribillo.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El dedo 2 toca siempre la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sintiendo el Fa#', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'G4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'La subida cromática hacia el estribillo', 2,
                          'Lo de hoy. Una escalera de semitonos, todos pegados, que empuja hacia arriba sin descanso hasta llegar al estribillo. Cuenta cada tecla, blanca o negra, por igual.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'a) Mi hasta Si, semitono a semitono, sin saltarse ninguno', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A#4', 'A4', 'G#4', 'G4', 'F#4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma escalera, bajando de vuelta', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'F#4', 'G4']]
    bass2c = [{'pitches': MIm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El principio de la subida sobre el acorde de Mim', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en Mi menor', 2,
                          'Mim–Sim–Lam: los acordes de la familia.')
    y -= 11
    pattern_a = [(MIm, 'Mim'), (SIm, 'Sim'), (LAm, 'Lam'), (MIm, 'Mim')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mim-Sim-Lam-Mim, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: la subida cromática arriba, el acorde firme abajo.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la subida completa sobre el acorde de Lam', 2,
                          'La izquierda sostiene el acorde de Lam entero; la derecha sube la escalera cromática encima.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'F#4', 'G4']]
    bass1 = [{'pitches': LAm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La subida sobre Lam, sin prisa', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G#4', 'A4', 'A#4', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) El final de la subida, hasta llegar a Si', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia de la subida', 3,
                          'La izquierda sostiene su acorde de Sim sin moverse; la derecha sube sin arrastrarla.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G#4', 'A4', 'A#4', 'B4']]
    bass3 = [{'pitches': SIm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El final de la subida sobre Sim; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A#4', 'A4', 'G#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Al Calor del Amor casi entera, con la subida', 3,
                          'Con la partitura al lado: deja que la escalera cromática empuje sin frenar hasta el estribillo.')
    y -= 11
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'F#4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G#4', 'A4', 'A#4', 'B4']])
    bass5 = [{'pitches': MIm, 'dur': 'w'}, {'pitches': LAm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Allegretto, la subida sin frenar', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
