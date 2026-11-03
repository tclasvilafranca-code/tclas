# -*- coding: utf-8 -*-
"""Taller de practica - Adagio (Jose Maria, cancion 20, La menor,
   3/4). OJO: el subtitulo de la partitura dice "Sol menor" pero la
   armadura real (verificada en la imagen) no lleva ninguna
   alteracion -- este arreglo esta transportado a La menor. Enfoque
   relajado: el viaje del volumen, de piano a forte y de vuelta,
   sin miedo a los cambios."""
from page_layout_common import *

SONG_KICKER = 'JOSÉ MARÍA · JUNIO · ADAGIO (ALBINONI)'
TS = (3, 4)

Am = ['A2', 'C3', 'E3']
Dm = ['D3', 'F3', 'A3']
E = ['E3', 'G#3', 'B3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El Adagio de Albinoni en La menor. Sin prisa: el volumen viaja, de suave a fuerte y vuelta.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2), ('A4', 1), ('B4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'E5'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El viaje del volumen: de piano a forte, sin miedo', 2,
                          'Lo que vamos a cuidar en esta pieza. La partitura pide piano, luego un poco más (mp) y después forte — hay que atreverse a los cambios, sin quedarse siempre igual de flojo.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h.'} for p in ['C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) Empezando muy suave (piano)', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.'} for p in ['E5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, ya más fuerte (forte): para sentir el cambio', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h.'} for p in ['C5', 'B4', 'A4']]
    bass2c = [{'pitches': Am, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase suave sobre el acorde de Lam, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en La menor', 2,
                          'Lam–Rem–Mi: los acordes de esta tonalidad, sin prisa.')
    y -= 11
    pattern_a = [(Am, 'Lam'), (Dm, 'Rem'), (E, 'Mi'), (Am, 'Lam')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mi-Lam, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el volumen viaja mientras el acorde no se mueve.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el volumen suave sobre el acorde de Rem', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha empieza muy suave, sin miedo a crecer después.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['D5', 'C5', 'B4']]
    bass1 = [{'pitches': Dm, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El volumen suave sobre Rem, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'B4', 'A4', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del volumen', 3,
                          'La izquierda queda absolutamente quieta con su acorde; la derecha viaja de suave a fuerte, sin que ninguna se apresure.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h.'} for p in ['E5', 'D5', 'C5']]
    bass3 = [{'pitches': E, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El volumen viaja sobre Mi; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'C5', 'B4', 'C5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un poco más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · el Adagio casi entero', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que el volumen viaje de suave a fuerte, sin miedo a los cambios.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h.'} for p in ['C5', 'B4', 'A4']] +
             [{'pitch': p, 'dur': 'h.'} for p in ['D5', 'C5', 'B4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [Am, Am, Am, Dm, Dm, Dm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El Adagio casi completo · con el volumen viajando, sin miedo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
