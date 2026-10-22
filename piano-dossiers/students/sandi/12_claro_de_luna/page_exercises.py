# -*- coding: utf-8 -*-
"""Taller de practica - Claro de Luna (Sandi, cancion 12, Beethoven,
   "Moonlight" Sonata Op.27 No.2, arr. simplificado Level 3 de G.
   DeBenedetti, sin alteraciones en esta version -- confirmado por
   render directo, 2/4). Nivel avanzado: el cruce de manos -- la
   melodia pasa de una mano a otra."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · CLARO DE LUNA (BEETHOVEN)'
TS = (2, 4)

LAm = ['A2', 'C3', 'E3']
REm = ['D2', 'F2', 'A2']
MI = ['E2', 'G#2', 'B2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Claro de Luna, de Beethoven (versión simplificada). Hoy: el cruce de manos.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Todas teclas blancas, como en esta versión simplificada.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'e'} for p in ['A3', 'C4', 'E4', 'A3']]
    y = system_block(c, x0, w0, y, gap, 'a) El arpegio de La menor, en corcheas ligeras', ev1a, clef='bass', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'h'} for p in ['A2', 'E3']]
    y = system_block(c, x0, w0, y, gap, 'b) Notas largas sostenidas, como la melodía original', ev1b, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El cruce de manos: la melodía pasa de una mano a otra', 3,
                          'La dificultad de hoy. Al principio, la mano derecha toca el arpegio grave (escrito en clave de Fa) mientras la izquierda sostiene la melodía; más adelante, los papeles se intercambian y la melodía sube a la mano derecha.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e'} for p in ['A3', 'C4', 'E4', 'A3']]
    y = system_block(c, x0, w0, y, gap, 'a) El arpegio grave (mano derecha, en clave de Fa): fluido y uniforme', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': 'A2', 'dur': 'h'}]
    y = system_block(c, x0, w0, y, gap, 'b) La melodía grave (mano izquierda): sostenida, sin apagarse', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e'} for p in ['A3', 'C4', 'E4', 'A3']]
    bass2c = [{'pitch': 'A2', 'dur': 'h'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Ambas manos juntas: arpegio arriba, melodía abajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en La menor', 2,
                          'Lam–Rem–Mi: los acordes que sostiene la armonía bajo el arpegio.')
    y -= 11
    pattern_a = [(LAm, 'Lam'), (REm, 'Rem'), (MI, 'Mi'), (LAm, 'Lam')]
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Rem-Mi-Lam, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora practica el cruce: cuando la melodía sube a la derecha, el arpegio baja a la izquierda.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos cruzadas · la melodía ya arriba, el arpegio abajo', 3,
                          'Después del cruce, la derecha sostiene la melodía en el registro agudo mientras la izquierda toma el arpegio: los papeles se han intercambiado por completo.')
    y -= 7
    treb1 = [{'pitch': 'A4', 'dur': 'h'}]
    bass1 = [{'pitch': p, 'dur': 'e'} for p in ['A3', 'C4', 'E4', 'A3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía arriba (derecha), el arpegio abajo (izquierda): el cruce completado', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía ya en la mano derecha: para sentir el cambio de registro', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el arpegio no contagia el tempo de la melodía', 3,
                          'La izquierda mantiene el arpegio fluido y uniforme; la derecha sostiene su nota larga sin dejarse arrastrar por la velocidad de abajo.')
    y -= 7
    treb3 = [{'pitch': 'E5', 'dur': 'h'}]
    bass3 = [{'pitch': p, 'dur': 'e'} for p in ['E3', 'G#3', 'B3', 'E3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía sobre el arpegio de Mi; ninguna mano arrastra a la otra', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'h'} for p in ['E5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía se mueve un poco, sin perder la calma', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Claro de Luna casi entero', 3,
                          'Con la partitura al lado: siente el momento exacto del cruce, sin que el arpegio se detenga ni un instante.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'A4']]
    bass5 = ([{'pitch': p, 'dur': 'e'} for p in ['A3', 'C4', 'E4', 'A3']] +
             [{'pitch': p, 'dur': 'e'} for p in ['A3', 'C4', 'E4', 'A3']])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Claro de Luna casi completo · el cruce de manos, sin interrupciones', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
