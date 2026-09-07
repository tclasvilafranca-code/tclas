# -*- coding: utf-8 -*-
"""Taller de practica - Thinking Out Loud (Eva, cancion 19, Re mayor,
   4/4). Mismo arreglo que el de Dilan (que trabaja la igualdad de
   corcheas), pero enfoque DISTINTO para Eva: el ACOMPAÑAMIENTO TIPO
   GUITARRA -- un dibujo de acorde repetido, siempre identico, como un
   rasgueo que no cambia de forma."""
from page_layout_common import *

SONG_KICKER = 'EVA · JUNIO · THINKING OUT LOUD (ED SHEERAN)'
TS = (4, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['A2', 'C#3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Ed Sheeran en Re mayor. El reto: un dibujo repetido, siempre igual, como una guitarra.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('F#4', 3), ('E4', 2), ('A4', 5), ('G4', 4), ('F#4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('F#4', 3), ('A4', 5), ('F#4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El dibujo de guitarra: siempre exactamente igual', 2,
                          'La dificultad exacta de esta canción. El acompañamiento repite el mismo dibujo una y otra vez — como un rasgueo, tiene que sonar idéntico cada vez, sin variar.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D3', 'F#3', 'A3', 'F#3'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'a) El dibujo sobre Re, repetido cuatro veces idéntico', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['G2', 'B2', 'D3', 'B2'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo dibujo sobre Sol, sin cambiar la forma', ev2b, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes de esta tonalidad.')
    y -= 9
    pattern_a = [(RE, 'Re'), (LA, 'La'), (SOL, 'Sol'), (LA, 'La')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-La-Sol-La, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas tranquilas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el dibujo de guitarra se repite mientras la melodía canta encima.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el dibujo repetido bajo la melodía', 2,
                          'La izquierda repite el mismo dibujo sin variar nunca su forma; la derecha canta la melodía encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'G4', 'A4', 'F#4', 'D4', 'F#4', 'A4', 'F#4']]
    bass1 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D3', 'F#3', 'A3', 'F#3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El dibujo repetido, idéntico cada vez', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'F#4', 'G4', 'A4', 'F#4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando su forma', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el dibujo no cambia nunca', 3,
                          'La izquierda repite su dibujo exactamente igual mientras la derecha se mueve libre y más rápido encima.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['A4', 'F#4', 'G4', 'F#4'] * 2)]
    bass3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['D3', 'F#3', 'A3', 'F#3'] * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El dibujo no cambia; la melodía sí se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'F#4', 'A4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la escala completa, tranquila', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Thinking Out Loud casi entera', 3,
                          'Con la partitura al lado: repite el mismo dibujo de guitarra de principio a fin, sin que se deforme nunca.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['F#4', 'G4', 'A4', 'F#4', 'D4', 'F#4', 'A4', 'F#4', 'G4', 'A4', 'B4', 'A4', 'G4', 'F#4', 'D4', 'F#4']]
    bass5 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(
             ['D3', 'F#3', 'A3', 'F#3'] * 4 + ['G2', 'B2', 'D3', 'B2'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈79, con el dibujo firme', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
