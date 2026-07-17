# -*- coding: utf-8 -*-
"""Taller de practica - When I Was Your Man (Eva, cancion 12, Do mayor,
   4/4). Mismo arreglo que el de Dilan (que trabaja la memoria de los
   acordes), pero enfoque DISTINTO para Eva: el RUBATO -- estirar el
   tiempo de una balada de piano solo sin perder el pulso interior."""
from page_layout_common import *

SONG_KICKER = 'EVA · ABRIL · WHEN I WAS YOUR MAN (BRUNO MARS)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de piano solo en Do mayor. El reto: el rubato, estirar el tiempo sin perder el pulso interior.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 5), ('E4', 3), ('C4', 1), ('E4', 3), ('F4', 4), ('D4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Rubato: estirar el tiempo sin perder el pulso', 2,
                          'La dificultad exacta de esta canción. Alarga una nota importante y recupera el tiempo en la siguiente — como si respiraras dentro de la frase, no como si te pararas.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'D4', 'C4', 'C4', 'C4', 'C4', 'D4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Medido primero: exactamente igual de largas', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': v} for p, v in
            [('E4', 'q.'), ('D4', 'e'), ('C4', 'h'), ('C4', 'q'), ('D4', 'q'), ('E4', 'h')]]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora con rubato: la primera nota se alarga, luego se recupera', ev2b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Do mayor', 2,
                          'Do–Fa–Sol: los tres acordes básicos, aquí más movidos que en la canción real.')
    y -= 9
    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (FA, 'Fa')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Fa-Sol-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (SOL, 'Sol'), (FA, 'Fa'), (DO, 'Do')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas tranquilas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: deja que el rubato respire sin que el acorde pierda su sitio.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el rubato sobre el acorde', 2,
                          'La izquierda sostiene el acorde con calma; la derecha estira el tiempo de la frase, sin que la izquierda se pierda.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': v} for p, v in
             [('E4', 'q.'), ('D4', 'e'), ('C4', 'h'), ('C4', 'q'), ('D4', 'q'), ('E4', 'h')]]
    bass1 = [{'pitches': DO, 'dur': 'w'}, {'pitches': DO, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El acorde entero aguanta mientras la derecha respira', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F4', 'E4', 'D4', 'C4', 'D4', 'E4', 'F4', 'G4', 'E4', 'C4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando dónde respira', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'El rubato con acordes que cambian', 3,
                          'Ahora el acorde cambia mientras la melodía respira — la izquierda tiene que anticipar el cambio sin romper el rubato.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': v} for p, v in [('E4', 'h.'), ('D4', 'q'), ('C4', 'h.'), ('D4', 'q')]]
    bass3 = [{'pitches': p, 'dur': 'w'} for p in [DO]] + [{'pitches': p, 'dur': 'w'} for p in [FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde cambia sin romper el rubato de la melodía', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, tranquila', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · When I Was Your Man casi entera', 3,
                          'Con la partitura al lado: deja que el rubato cuente la historia, sin que la izquierda pierda nunca el pulso interior.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': v} for p, v in
             [('E4', 'q.'), ('D4', 'e'), ('C4', 'h'), ('C4', 'q'), ('D4', 'q'), ('E4', 'h'),
              ('G4', 'q.'), ('F4', 'e'), ('E4', 'h'), ('D4', 'q'), ('C4', 'q'), ('C4', 'q'), ('C4', 'q')]]
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [DO, FA, DO, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Balada libre ♩≈70, con rubato', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
