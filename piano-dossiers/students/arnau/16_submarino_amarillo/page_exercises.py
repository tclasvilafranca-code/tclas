# -*- coding: utf-8 -*-
"""Taller de practica - El Submarino Amarillo (Arnau, cancion 16,
   Sol mayor, 4/4). Reto motivador (nivel basico): primera cancion
   con sostenido -- Fa#, indicado una vez en la armadura."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · RETO MOTIVADOR · EL SUBMARINO AMARILLO'
TS = (4, 4)
KEY = 'Sol mayor'

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D2', 'F#2', 'A2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un reto especial: nuestra primera canción en Sol mayor, con un sostenido en el Fa.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento: posición de 5 dedos en Sol mayor', 1,
                          'Dedo 1 en Sol: Sol(1) La(2) Si(3) Do(4) Re(5). El dedo 3 no toca Fa, así que no hay que pensar en el sostenido aquí.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('D5', 5), ('C5', 4), ('B4', 3), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja la posición de Sol mayor', ev1a, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 2, 'El Fa que ya no se escribe cada vez: la armadura', 2,
                          'Cada vez que aparece un Fa en esta canción, es Fa sostenido — el sostenido ya está anunciado al principio del pentagrama.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C5', 'B4', 'A4', 'F#4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) Una frase con Fa sostenido dentro', ev2a, clef='treble', time_sig=TS, key_sig=KEY)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C5', 'B4', 'A4', 'G4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase sin el Fa: para escuchar la diferencia', ev2b, clef='treble', time_sig=TS, key_sig=KEY)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C5', 'B4', 'A4', 'F#4', 'G4', 'A4']]
    bass2c = [{'pitches': SOL, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase sobre el acorde de Sol, quieto', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Re-Sol, un acorde por compás entero', eva, clef='bass', time_sig=TS, key_sig=KEY)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Truco de estudio: toca solo los Fa de la canción, uno por uno, para memorizar dónde están.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase sobre el acorde de Do', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta con su Fa sostenido.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'C5', 'B4', 'C5', 'A4', 'F#4', 'G4']]
    bass1 = [{'pitches': DO, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase sobre Do, quieto', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin Fa: para comparar', treb2, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se altera con la melodía', 3,
                          'La izquierda queda quieta con su acorde; la derecha usa su Fa sostenido, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'D5', 'C5', 'A4', 'F#4', 'G4']]
    bass3 = [{'pitches': RE, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase sobre Re; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación, terminando en el Fa sostenido', treb4, clef='treble', time_sig=TS, key_sig=KEY)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · El Submarino Amarillo casi entera', 3,
                          'Con la partitura al lado: ¡disfruta este primer reto en Sol mayor!')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D5', 'D5', 'C5', 'B4', 'A4', 'F#4', 'G4', 'A4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'C5', 'B4', 'C5', 'A4', 'F#4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [SOL, SOL, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · con su sostenido y todo', grand_gap_mult=7.3, time_sig=TS, key_sig=KEY)

    exercises_footer(c, 4)
    c.showPage()
