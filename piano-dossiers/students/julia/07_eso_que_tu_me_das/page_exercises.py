# -*- coding: utf-8 -*-
"""Taller de practica - Eso que tu me das (Julia, cancion 7, Do
   mayor, 4/4). Nivel inicial: los acordes que cambian, sin miedo --
   la cancion real tiene varios acordes distintos, uno detras de
   otro."""
from page_layout_common import *

SONG_KICKER = 'JULIA · NIVEL INICIAL · ESO QUE TÚ ME DAS (JARABE DE PALO)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
SOL = ['G2', 'B2', 'D3']
Am = ['A2', 'C3', 'E3']
FA = ['F2', 'A2', 'C3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Jarabe de Palo en Do mayor. Hoy los acordes cambian, ¡pero sin ningún miedo!')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). ¡Busca tu nota casa, el Do!')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseíto por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'E4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los acordes que cambian, sin miedo', 2,
                          'Lo que vamos a practicar hoy. Esta canción tiene varios acordes distintos, uno detrás de otro — hay que cambiar de sitio sin miedo, sin pararse a pensar.')
    y -= 9
    ev2a = [{'pitches': p, 'dur': 'h'} for p in [DO, SOL, Am, FA]]
    y = system_block(c, x0, w0, y, gap, 'a) Cuatro acordes seguidos, sin parar', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'w'} for p in [DO, Am]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, más despacio: para comparar', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'G4', 'E4', 'D4', 'C4', 'D4']]
    bass2c = [{'pitches': p, 'dur': 'h'} for p in [DO, SOL, Am, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía sobre los acordes que cambian', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Do–Sol–Lam–Fa: los acordes reales de esta canción.')
    y -= 11
    pattern_a = [(DO, 'Do'), (SOL, 'Sol'), (Am, 'Lam'), (FA, 'Fa')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Sol-Lam-Fa, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: los acordes cambian mientras la melodía canta encima.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · Sol y Lam, sin miedo al cambio', 2,
                          'La izquierda cambia de Sol a Lam a tiempo; la derecha canta la melodía, sin pararse.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'D5', 'B4', 'A4', 'G4', 'A4']]
    bass1 = [{'pitches': p, 'dur': 'w'} for p in [SOL, Am]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre Sol y Lam, uno tras otro', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'D5', 'B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para irla conociendo', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · Fa y Do, cambiando a tiempo', 3,
                          'La izquierda cambia de acorde justo a tiempo; la derecha canta, sin que ninguna se pierda.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'C5', 'A4', 'G4', 'F4', 'G4']]
    bass3 = [{'pitches': p, 'dur': 'w'} for p in [FA, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre Fa y Do, cambiando sin miedo', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'A4', 'C5', 'F5', 'C5', 'A4', 'F4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, con saltos', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Eso que tú me das casi entera', 3,
                          'Con la partitura al lado: ¡cambia de acorde sin miedo, uno detrás de otro!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'G4', 'E4', 'D4', 'C4', 'D4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'D5', 'B4', 'A4', 'G4', 'A4']])
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [DO, SOL, Am, FA]] + [{'pitches': p, 'dur': 'w'} for p in [SOL, Am]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · cambiando de acorde sin miedo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
