# -*- coding: utf-8 -*-
"""Taller de practica - La Promesa (Eva, cancion 15, Sol mayor, 4/4). Mismo
   arreglo que el de Dilan (que trabaja la entrada a contratiempo), pero
   enfoque DISTINTO para Eva: la NOTA COMUN entre acordes -- moverse de un
   acorde al siguiente sin que la mano salte, dejando una nota quieta
   como eje."""
from page_layout_common import *

SONG_KICKER = 'EVA · MAYO · LA PROMESA (MELENDI)'
TS = (4, 4)

SOL = ['G3', 'B3', 'D4']
DO = ['C3', 'E3', 'G3']
RE = ['D3', 'F#3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Melendi en Sol mayor. El reto: pasar de un acorde a otro sin que la mano salte.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5). Todas teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('B4', 3), ('A4', 2), ('D5', 5), ('C5', 4), ('B4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('B4', 3), ('D5', 5), ('B4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, desde el Si', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La nota común: el eje entre dos acordes', 2,
                          'La dificultad exacta de esta canción. Entre Sol y Re hay una nota que se repite — encuéntrala y déjala quieta mientras el resto de la mano se mueve.')
    y -= 9
    ev2a = [{'pitches': SOL, 'dur': 'h'}, {'pitches': RE, 'dur': 'h'}, {'pitches': SOL, 'dur': 'h'}, {'pitches': RE, 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'a) Sol y Re, alternando, sin que la mano salte', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h', 'number': n} for p, n in [('D4', 5), ('D4', 5), ('D4', 5), ('D4', 5)]]
    y = system_block(c, x0, w0, y, gap, 'b) La nota común (Re): quieta mientras cambia el acorde', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitches': p, 'dur': 'q'} for p in [DO, RE, SOL, DO]]
    y = system_block(c, x0, w0, y, gap, 'c) Do-Re-Sol-Do, buscando siempre la nota que no se mueve', ev2c, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad.')
    y -= 9
    pattern_a = [(SOL, 'Sol'), (RE, 'Re'), (DO, 'Do'), (RE, 'Re')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Re-Do-Re, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas tranquilas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: los acordes se mueven suave, sin sobresaltos, bajo la melodía.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · movimiento suave de acordes', 2,
                          'La izquierda cambia de acorde sin saltos bruscos, buscando siempre la nota más cercana; la derecha canta encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5', 'B4', 'G4', 'B4', 'D5', 'B4']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [SOL, DO, RE, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El acorde se mueve suave, la melodía canta encima', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4', 'C5', 'D5', 'B4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando su forma', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no salta', 3,
                          'La izquierda encuentra siempre el camino más corto entre acordes; la derecha se mueve libre encima.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['D5', 'B4', 'C5', 'B4'] * 2)]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [SOL, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde no salta; la melodía sí se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'B4', 'D5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la escala completa, tranquila', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · La Promesa casi entera', 3,
                          'Con la partitura al lado: mueve los acordes siempre por el camino más corto, sin sobresaltos.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['B4', 'C5', 'D5', 'B4', 'G4', 'B4', 'D5', 'B4', 'C5', 'D5', 'B4', 'G4', 'A4', 'B4', 'D5', 'B4']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [SOL, RE, DO, SOL, RE, DO, SOL, RE]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈96, con movimiento suave', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
