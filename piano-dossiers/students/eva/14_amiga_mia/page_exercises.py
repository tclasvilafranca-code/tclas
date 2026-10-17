# -*- coding: utf-8 -*-
"""Taller de practica - Amiga Mia (Eva, cancion 14, Re mayor, 4/4). Mismo
   arreglo que el de Dilan (que trabaja el pedal de resonancia), pero
   enfoque DISTINTO para Eva: el LEGATO DE DEDOS -- conectar los acordes
   solo con la mano, sin pedal, sustituyendo dedos para que no se note
   el cambio."""
from page_layout_common import *

SONG_KICKER = 'EVA · MAYO · AMIGA MÍA (ALEJANDRO SANZ)'
TS = (4, 4)

RE = ['D3', 'F#3', 'A3']
LA = ['E2', 'A2', 'C#3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Alejandro Sanz en Re mayor. El reto: unir los acordes solo con la mano, sin pedal.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('F#4', 3), ('E4', 2), ('A4', 5), ('G4', 4), ('F#4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición, sintiendo el Fa#', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('F#4', 3), ('A4', 5), ('F#4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Legato de dedos: unir sin pedal', 2,
                          'La dificultad exacta de esta canción, pero sin usar el pie. Sustituye el dedo en la nota común entre un acorde y el siguiente, para que no se note el cambio.')
    y -= 9
    ev2a = [{'pitches': RE, 'dur': 'h'}, {'pitches': LA, 'dur': 'h'}, {'pitches': SOL, 'dur': 'h'}, {'pitches': RE, 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'a) Los acordes, buscando la nota común entre cada dos', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 5), ('D4', 5), ('C#4', 4), ('C#4', 4)]]
    y = system_block(c, x0, w0, y, gap, 'b) La nota común entre Re y La: sostenla con el mismo dedo', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitches': RE, 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'c) Aguanta el acorde con los dedos, sin usar el pedal', ev2c, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes de esta tonalidad.')
    y -= 9
    pattern_a = [(RE, 'Re'), (LA, 'La'), (SOL, 'Sol'), (LA, 'La')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-La-Sol-La, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOL, 'Sol'), (LA, 'La'), (RE, 'Re'), (SOL, 'Sol')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas tranquilas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: los acordes se conectan solo con los dedos, sin pedal.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · legato de dedos bajo la melodía', 2,
                          'La izquierda cambia de acorde sustituyendo dedos, sin cortar el sonido; la derecha canta encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'G4', 'A4', 'F#4', 'D4', 'F#4', 'A4', 'F#4']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [LA, RE, LA, RE]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El acorde se une con los dedos, sin pedal', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'F#4', 'G4', 'A4', 'F#4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando su forma', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el legato de dedos no se rompe', 3,
                          'La izquierda conecta cada acorde con el siguiente sin ayuda del pedal; la derecha se mueve libre encima.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['A4', 'F#4', 'G4', 'F#4'] * 2)]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [RE, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde une sus notas comunes; la melodía se mueve libre', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'F#4', 'G4', 'B4', 'A4', 'G4', 'F#4', 'A4', 'D4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Amiga Mía casi entera', 3,
                          'Con la partitura al lado: une cada acorde con el siguiente solo con los dedos, sin pisar el pedal ni una vez.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['F#4', 'G4', 'A4', 'F#4', 'D4', 'F#4', 'A4', 'F#4', 'G4', 'A4', 'B4', 'A4', 'G4', 'F#4', 'D4', 'F#4']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [RE, LA, SOL, RE, RE, LA, SOL, RE]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Balada ♩≈80, sin pedal', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
