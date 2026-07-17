# -*- coding: utf-8 -*-
"""Taller de practica - Can't Help Falling in Love (Eva, cancion 1, Re mayor,
   3/4). Mismo arreglo que el de Dilan, pero enfoque DISTINTO: aqui el foco es
   la PROGRESION ARMONICA -- un acorde nuevo casi cada compas, incluido un
   prestamo armonico (Do#7, que no es de la familia de Re mayor) antes de
   resolver a Fa#m. Nunca se trabaja aqui el arpegio de vals que ya usa Dilan."""
from page_layout_common import *

SONG_KICKER = 'EVA · SEPTIEMBRE · CAN’T HELP FALLING IN LOVE'
TS = (3, 4)

RE = ['D3', 'F#3', 'A3']
FAsm = ['F#2', 'A2', 'C#3']
SIm = ['B2', 'D3', 'F#3']
SOL = ['G2', 'B2', 'D3']
LA = ['A2', 'C#3', 'E3']
DOsm7 = ['C#3', 'F3', 'G#3', 'B3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un vals de Elvis Presley en Re mayor. El reto: la progresión armónica se mueve casi cada compás.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento de acordes: reconócelos sin dudar', 1,
                          'Antes de leer la progresión completa, aprende a reconocer cada acorde de un vistazo: Re, Sol, La y Si menor.')
    y -= 12
    ev1a = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (SIm, 'Sim')]]
    y = system_block(c, x0, w0, y, gap, 'a) Los cuatro acordes principales, uno por compás', ev1a, clef='bass', time_sig=TS)

    ev1b = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(SIm, 'Sim'), (LA, 'La'), (SOL, 'Sol'), (RE, 'Re')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos cuatro, en orden inverso', ev1b, clef='bass', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'La progresión que se mueve rápido: un acorde por compás', 2,
                          'La dificultad exacta de esta canción. La armonía real cambia casi en cada compás — apréndela como una frase, no acorde a acorde.')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
            [(RE, 'Re'), (FAsm, 'Fa#m'), (SIm, 'Sim'), (SOL, 'Sol')]]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Fa#m-Sim-Sol, la primera frase real', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
            [(RE, 'Re'), (LA, 'La'), (SIm, 'Sim'), (SOL, 'Sol')]]
    y = system_block(c, x0, w0, y, gap, 'b) Re-La-Sim-Sol, la segunda frase', ev2b, clef='bass', time_sig=TS)

    ev2c = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(LA, 'La'), (SIm, 'Sim'), (SOL, 'Sol'), (RE, 'Re')]]
    y = system_block(c, x0, w0, y, gap, 'c) La-Sim-Sol-Re, la vuelta a casa', ev2c, clef='bass', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes básicos de la tonalidad, arpegiados.')
    y -= 12
    pattern_a = [('D2', 'Re'), ('F#3', None), ('A3', None), ('G2', 'Sol'), ('B2', None), ('D3', None),
                 ('A2', 'La'), ('C#3', None), ('E3', None), ('D2', 'Re'), ('F#3', None), ('A3', None)]
    eva = [{'pitch': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La-Re, arpegiados nota a nota', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
                 [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La')] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos tres, ahora en bloque y más rápido', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la melodía canta notas largas mientras la armonía se mueve debajo.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre la progresión', 2,
                          'La izquierda cambia de acorde cada compás; la derecha sostiene una nota larga y la deja sonar hasta el siguiente cambio.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'h.', 'number': n} for p, n in [('D4', 1), ('C#4', 1), ('B3', 1), ('A3', 1)]]
    bass1 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(RE, 'Re'), (FAsm, 'Fa#m'), (SIm, 'Sim'), (SOL, 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Notas largas, sintiendo cada cambio de acorde debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'h.'} for p in ['D4', 'C#4', 'B3', 'A3', 'D4', 'C#4', 'B3', 'A3']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando su forma', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El préstamo armónico: el acorde que no es de la familia', 3,
                          'Antes del final, aparece un Do#7 que no pertenece a Re mayor — es un préstamo que tira con fuerza hacia Fa#m. Escúchalo: suena "de fuera" antes de resolver.')
    y -= 11
    ev5a = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(FAsm, 'Fa#m'), (DOsm7, 'Do#7'), (FAsm, 'Fa#m'), (DOsm7, 'Do#7')]]
    y = system_block(c, x0, w0, y, gap, 'a) Fa#m y su préstamo Do#7, alternando', ev5a, clef='bass', time_sig=TS)

    treb5b = [{'pitch': p, 'dur': 'q'} for p in ['C#4', 'E4', 'G4', 'F#4', 'A4', 'G4', 'F#4', 'E4', 'C#4']]
    bass5b = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(FAsm, 'Fa#m'), (DOsm7, 'Do#7'), (FAsm, 'Fa#m')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5b, bass5b, 'b) El acorde sorpresa con la melodía real encima', grand_gap_mult=7.3, time_sig=TS)

    y = exercise_heading(c, y, 6, 'Reto final · la canción casi entera', 3,
                          'Con la partitura al lado: sigue la progresión de acordes como si fuera una frase, no una lista.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'h.'} for p in ['D4', 'C#4', 'B3', 'D4', 'E4', 'D4', 'C#4', 'D4']]
    bass6 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(RE, 'Re'), (FAsm, 'Fa#m'), (SIm, 'Sim'), (SOL, 'Sol'),
              (RE, 'Re'), (LA, 'La'), (SIm, 'Sim'), (SOL, 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción completa · Lento ♩≈76, con ternura', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
