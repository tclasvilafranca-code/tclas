# -*- coding: utf-8 -*-
"""Taller de practica - Perfect (Luisa, cancion 23, Ed Sheeran,
   Do mayor, 12/8). Nivel hobby, sin complicaciones: una cancion de
   amor -- dejala fluir, sin contar."""
from page_layout_common import *

SONG_KICKER = 'LUISA · NIVEL HOBBY · PERFECT (ED SHEERAN)'
TS = (12, 8)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La famosa balada de Ed Sheeran, en Do mayor. Hoy: una canción de amor, déjala fluir sin contar.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Sin complicarse, todas teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4', 'C4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Una canción de amor: déjala fluir, sin contar', 2,
                          'Lo de hoy. Esta canción tiene un vaivén suave y continuo, como una nana: no hay que contar nada, solo dejar que fluya con calma.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) El vaivén, tranquilo', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, muy despacio: dejándola fluir', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'C4', 'E4']]
    bass2c = [{'pitches': DO, 'dur': 'q.'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El vaivén sobre el acorde de Do, tranquilo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes, sin más complicación.')
    y -= 11
    eva = ([{'pitches': DO, 'dur': 'q.', 'label': 'Do'}] * 2 + [{'pitches': FA, 'dur': 'q.', 'label': 'Fa'}] * 2 +
           [{'pitches': SOL, 'dur': 'q.', 'label': 'Sol'}] * 2 + [{'pitches': DO, 'dur': 'q.', 'label': 'Do'}] * 2)
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Do, dos vaivenes por acorde', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas, sin agobios: deja que la canción fluya sola, sin contar nada.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el vaivén sobre el acorde de Fa', 2,
                          'La izquierda repite su acorde de Fa, tranquila; la derecha canta encima, sin prisa.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'A4', 'G4', 'F4']]
    bass1 = [{'pitches': FA, 'dur': 'q.'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El vaivén sobre Fa, repetido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · sin agobios, cada mano tranquila', 3,
                          'La izquierda repite su acorde de Sol; la derecha canta sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q.'} for p in ['G4', 'B4', 'A4', 'G4']]
    bass3 = [{'pitches': SOL, 'dur': 'q.'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El vaivén sobre Sol, repetido', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q.'} for p in ['D5', 'C5', 'B4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Perfect casi entera', 3,
                          'Con la partitura al lado: deja que la canción fluya, sin contar, sin agobios.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q.'} for p in ['C4', 'D4', 'E4', 'D4']] +
             [{'pitch': p, 'dur': 'q.'} for p in ['F4', 'G4', 'A4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'q.'} for p in [DO, DO, DO, DO, FA, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Perfect casi completa · fluyendo, sin agobios', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
