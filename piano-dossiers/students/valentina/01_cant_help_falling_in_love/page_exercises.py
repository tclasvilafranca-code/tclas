# -*- coding: utf-8 -*-
"""Taller de practica - Can't Help Falling in Love (Valentina, cancion 1,
   Re mayor, 3/4, mismo archivo que Dilan y Eva). Nivel medio, un poco mas
   exigente: la melodia en octavas -- ampliar el alcance sin tension."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · CAN’T HELP FALLING IN LOVE'
TS = (3, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['A2', 'C#3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un vals de Elvis Presley en Re mayor. Hoy: la melodía en octavas, ampliar el alcance sin tensión.')
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
    y -= 6

    y = exercise_heading(c, y, 2, 'La melodía en octavas: ampliar el alcance sin tensión', 2,
                          'La dificultad de hoy. La misma frase, pero tocada con la nota grave y su octava a la vez. La mano se abre, pero la muñeca queda suelta: sin apretar.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Primero, la frase con una sola mano de notas', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitches': [p, p[:-1] + str(int(p[-1]) + 1)], 'dur': 'q'} for p in
            ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, ahora en octavas', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitches': [p, p[:-1] + str(int(p[-1]) + 1)], 'dur': 'q'} for p in ['D4', 'F#4', 'A4']]
    bass2c = [{'pitches': RE, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Octavas sobre el acorde de Re, sin prisa', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes de esta tonalidad. El bajo del vals se apoya siempre en ellos.')
    y -= 11
    pattern_a = [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: la izquierda sostiene el acorde, la derecha canta en octavas, sin apretar.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía en octavas sobre el acorde de Re', 2,
                          'La izquierda sostiene el acorde de Re; la derecha canta en octavas, con la muñeca relajada.')
    y -= 11
    treb1 = [{'pitches': [p, p[:-1] + str(int(p[-1]) + 1)], 'dur': 'q'} for p in ['D4', 'F#4', 'A4']]
    bass1 = [{'pitches': RE, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Octavas sobre Re, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'G4', 'F#4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin octavas: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · la mano izquierda no se contagia', 3,
                          'La izquierda sostiene su acorde de Sol sin moverse; la derecha abre la octava sin arrastrarla.')
    y -= 11
    treb3 = [{'pitches': [p, p[:-1] + str(int(p[-1]) + 1)], 'dur': 'q'} for p in ['G4', 'A4', 'B4']]
    bass3 = [{'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Octavas sobre Sol; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitches': [p, p[:-1] + str(int(p[-1]) + 1)], 'dur': 'q'} for p in ['B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando en octavas', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · la canción casi entera, en octavas', 3,
                          'Con la partitura al lado: deja la mano abierta pero suelta, sin agarrotarte en ningún salto.')
    y -= 11
    treb5 = ([{'pitches': [p, p[:-1] + str(int(p[-1]) + 1)], 'dur': 'q'} for p in ['D4', 'F#4', 'A4']] +
             [{'pitches': [p, p[:-1] + str(int(p[-1]) + 1)], 'dur': 'q'} for p in ['G4', 'A4', 'B4']])
    bass5 = [{'pitches': RE, 'dur': 'h.'}, {'pitches': SOL, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción completa en octavas · ♩≈72, con calma', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
