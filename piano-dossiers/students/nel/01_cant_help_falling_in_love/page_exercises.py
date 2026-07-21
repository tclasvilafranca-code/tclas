# -*- coding: utf-8 -*-
"""Taller de practica - Can't Help Falling in Love (Nel, cancion 1,
   Re mayor, 3/4). Angulo propio para Nel (12 anos, muy avanzado,
   quiere empuje): el VOICING -- dentro de un mismo acorde o intervalo
   en la mano derecha, la nota de arriba debe sonar mas que las demas,
   como si cantara por encima. Distinto del vals-arpegio de Dilan, la
   lectura armonica de Eva y el rubato con criterio de Josep."""
from page_layout_common import *

SONG_KICKER = "NEL · SEPTIEMBRE · CAN'T HELP FALLING IN LOVE"
TS = (3, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['E2', 'A2', 'C#3']

RE4 = ['D4', 'F#4', 'A4']
SOL4 = ['G4', 'B4', 'D5']
LA4 = ['A4', 'C#5', 'E5']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un vals lento en Re mayor. El reto: hacer que la nota de arriba cante por encima de las demás.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('G4', 4), ('F#4', 3), ('A4', 5), ('F#4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('F#4', 3), ('A4', 5), ('D5', 1)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, desgranado hasta la octava', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Voicing: la nota de arriba canta más que las demás', 2,
                          'La dificultad exacta de esta canción. Toca cada intervalo o acorde con las dos notas a la vez, pero deja que la de arriba suene más — como si la de abajo solo la acompañara en voz baja.')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'q'} for p in
            [['D4', 'F#4'], ['E4', 'G4'], ['F#4', 'A4'], ['G4', 'B4'], ['F#4', 'A4'], ['E4', 'G4'],
             ['D4', 'F#4'], ['E4', 'G4'], ['F#4', 'A4']]]
    y = system_block(c, x0, w0, y, gap, 'a) Intervalos de 3ª: la nota de arriba manda', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h.'} for p in [RE4, SOL4, LA4]]
    y = system_block(c, x0, w0, y, gap, 'b) Acordes completos: la más aguda siempre destaca', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitches': p, 'dur': 'q'} for p in
              [['D4', 'F#4'], ['E4', 'G4'], ['F#4', 'A4'], ['G4', 'B4'], ['F#4', 'A4'], ['E4', 'G4'], ['D4', 'F#4'], ['E4', 'G4'], ['F#4', 'A4']]]
    bass2c = [{'pitches': p, 'dur': 'h.'} for p in [RE, LA, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Con la izquierda debajo, sin que tape el voicing', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes de esta tonalidad, aquí como base de los acordes con voicing.')
    y -= 11
    pattern_a = [(RE, 'Re'), (LA, 'La'), (SOL, 'Sol'), (LA, 'La')] * 3
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-La-Sol-La, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el voicing se mantiene aunque la izquierda se mueva debajo.')
    y -= 15
    gap = 7.05
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el voicing no se pierde', 2,
                          'La derecha toca acordes completos, siempre con la nota de arriba destacada; la izquierda acompaña por debajo, sin competir con ella.')
    y -= 9
    treb1 = [{'pitches': p, 'dur': 'h.'} for p in [RE4, LA4]]
    bass1 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['D3', 'F#3', 'A3', 'F#3', 'D4', 'A3'] * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Acordes con voicing sobre un bajo en movimiento', grand_gap_mult=7.05, time_sig=TS)

    treb2 = [{'pitches': p, 'dur': 'q'} for p in
             [['D4', 'F#4'], ['G4', 'B4'], ['F#4', 'A4'], ['E4', 'G4'], ['D4', 'F#4'], ['F#4', 'A4'], ['G4', 'B4'], ['F#4', 'A4'], ['E4', 'G4']]]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la derecha, memorizando qué nota destaca en cada intervalo', treb2, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 5, 'Independencia · el voicing aguanta aunque la izquierda se mueva más', 3,
                          'La izquierda se mueve en corcheas sin parar; la derecha mantiene sus acordes con la nota de arriba siempre más presente.')
    y -= 5
    treb3 = [{'pitches': p, 'dur': 'h.'} for p in [SOL4, RE4]]
    bass3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['G2', 'B2', 'D3', 'B2', 'G3', 'D3'] * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda vuela; el voicing de la derecha no se altera', grand_gap_mult=7.05, time_sig=TS)

    treb4 = [{'pitches': p, 'dur': 'q'} for p in
             [['F#4', 'A4'], ['G4', 'B4'], ['A4', 'C#5'], ['G4', 'B4'], ['F#4', 'A4'], ['E4', 'G4'], ['D4', 'F#4'], ['F#4', 'A4'], ['A4', 'C#5']]]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: el mismo voicing, un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 6, "Reto final · Can't Help Falling In Love casi entera", 3,
                          'Con la partitura al lado: en cada acorde de la derecha, deja que la nota más aguda cante claramente por encima de las demás.')
    y -= 5
    treb5 = [{'pitches': p, 'dur': 'h.'} for p in [RE4, LA4, SOL4, RE4, LA4, RE4]]
    bass5 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['D3', 'F#3', 'A3', 'F#3', 'D4', 'A3'] * 6)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈72, con el voicing siempre presente', grand_gap_mult=7.05, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
