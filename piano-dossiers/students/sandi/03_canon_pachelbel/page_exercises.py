# -*- coding: utf-8 -*-
"""Taller de practica - Canon en Re (Sandi, cancion 3, Johann
   Pachelbel, Re mayor -- armadura de 2 sostenidos, Fa# y Do#,
   confirmada por render directo, 4/4). Nivel avanzado: el bajo
   ostinato -- la misma progresion, una y otra vez, mientras la
   melodia se hace cada vez mas elaborada."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · CANON EN RE (PACHELBEL)'
TS = (4, 4)

RE = ['D2', 'F#2', 'A2']
SOL = ['G2', 'B2', 'D3']
LA = ['A2', 'C#3', 'E3']
SIm = ['B2', 'D3', 'F#3']
FA_m = ['F#2', 'A2', 'C#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Canon en Re, de Pachelbel, en Re mayor. Hoy: el bajo ostinato que sostiene todo el edificio.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El Fa# y el Do# son las alteraciones de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('A4', 5), ('G4', 4), ('F#4', 3), ('E4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido completo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'D5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El bajo ostinato: la misma progresión, una y otra vez', 3,
                          'La dificultad de hoy. Toda la pieza se sostiene sobre una progresión de ocho acordes que se repite sin cambiar: Re-La-Sim-Fa#m-Sol-Re-Sol-La. La melodía se vuelve cada vez más elaborada encima, pero el bajo no se inmuta.')
    y -= 9
    ev2a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
            [(RE, 'Re'), (LA, 'La'), (SIm, 'Sim'), (FA_m, 'F#m')]]
    y = system_block(c, x0, w0, y, gap, 'a) Los primeros cuatro acordes del ostinato, memorízalos', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
            [(SOL, 'Sol'), (RE, 'Re'), (SOL, 'Sol'), (LA, 'La')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los cuatro siguientes: el ciclo completo del ostinato', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['D5', 'C#5', 'B4', 'A4']]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(RE, 'Re'), (LA, 'La'), (SIm, 'Sim'), (FA_m, 'F#m')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Una melodía sencilla sobre el ostinato completo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes principales, la base armónica del ostinato.')
    y -= 11
    pattern_a = [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La-Re, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el ostinato se repite exacto mientras la melodía se hace más rápida encima.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía en corcheas sobre el ostinato', 3,
                          'La izquierda repite el ostinato Re-La, sin variarlo nunca; la derecha empieza a moverse en corcheas, un escalón más elaborada que antes.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e'} for p in ['D5', 'C#5', 'B4', 'A4', 'D5', 'C#5', 'B4', 'A4']]
    bass1 = [{'pitches': RE, 'dur': 'h'}, {'pitches': LA, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Corcheas sobre Re-La, el ostinato inmutable', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e'} for p in ['A4', 'B4', 'C#5', 'D5', 'A4', 'B4', 'C#5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, subiendo en vez de bajar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el ostinato sigue igual aunque la melodía se acelere', 3,
                          'La izquierda repite Sim-F#m sin alterarse; la derecha se mueve en corcheas más rápidas, sin arrastrar al bajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e'} for p in ['F#4', 'G4', 'A4', 'B4', 'F#4', 'G4', 'A4', 'B4']]
    bass3 = [{'pitches': SIm, 'dur': 'h'}, {'pitches': FA_m, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Corcheas sobre Sim-F#m; el ostinato no se contagia', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Contraste: la misma línea, en negras tranquilas', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Canon en Re casi entero', 3,
                          'Con la partitura al lado: el bajo ostinato debe sonar exactamente igual en cada repetición, sin importar lo elaborada que se vuelva la melodía.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e'} for p in ['D5', 'C#5', 'B4', 'A4', 'D5', 'C#5', 'B4', 'A4']] +
             [{'pitch': p, 'dur': 'e'} for p in ['F#4', 'G4', 'A4', 'B4', 'F#4', 'G4', 'A4', 'B4']])
    bass5 = [{'pitches': RE, 'dur': 'h'}, {'pitches': LA, 'dur': 'h'}, {'pitches': SIm, 'dur': 'h'}, {'pitches': FA_m, 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Canon en Re casi completo · el ostinato inmutable, la melodía que crece', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
