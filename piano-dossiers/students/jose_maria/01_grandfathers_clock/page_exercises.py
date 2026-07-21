# -*- coding: utf-8 -*-
"""Taller de practica - My Grandfather's Clock (Jose Maria, cancion 1,
   Sol mayor, 4/4). Alumno adulto que va a su ritmo y no quiere
   estres: el angulo es el pulso tranquilo y constante -- como un
   reloj que nunca se acelera -- sin lenguaje de "reto" ni de prisa."""
from page_layout_common import *

SONG_KICKER = "JOSÉ MARÍA · SEPTIEMBRE · MY GRANDFATHER'S CLOCK"
TS = (4, 4)

SOL = ['G3', 'B3', 'D4']
DO = ['C3', 'E3', 'G3']
RE = ['D3', 'F#3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción tranquila en Sol mayor. Vamos a cuidar un pulso constante, sin ninguna prisa.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5). Tómate el tiempo que necesites para encontrar cada tecla con calma.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('D5', 5), ('C5', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('B4', 3), ('D5', 5), ('B4', 3)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El pulso del reloj: constante, sin acelerarse nunca', 2,
                          'Lo que vamos a cuidar en esta canción. Como un reloj de pared, el pulso de abajo no se apresura jamás — cuenta despacio y deja que cada nota larga suene entera.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) La melodía, tranquila y sin prisa', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'w'} for p in ['G3', 'C3', 'D3', 'G3']]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: una nota por compás entero, como el tictac', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4']]
    bass2c = [{'pitch': p, 'dur': 'w'} for p in ['G3', 'C3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, cada una a su aire', grand_gap_mult=7.3, time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad. Sin prisa, escuchando cada uno.')
    y -= 9
    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')] * 3
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Re-Sol, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el pulso de abajo tranquilo y la melodía cantando encima.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el pulso que nunca se acelera', 2,
                          'La izquierda marca el pulso, siempre igual de tranquilo; la derecha canta la melodía encima, sin que ninguna de las dos se apresure.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'C5', 'B4', 'A4', 'B4', 'C5', 'D5']]
    bass1 = [{'pitch': p, 'dur': 'w'} for p in ['G3', 'D3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía sobre el pulso tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'C5', 'B4', 'A4', 'B4', 'C5', 'D5', 'D5', 'C5', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para irla conociendo', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · cada mano a su aire', 3,
                          'La izquierda no cambia su ritmo pase lo que pase arriba; la derecha se mueve un poco más, tranquila también.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'C5']]
    bass3 = [{'pitch': p, 'dur': 'w'} for p in ['G3', 'C3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda firme; la derecha canta libre', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'A4', 'B4', 'A4', 'G4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un escalón más abajo', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · My Grandfather\'s Clock casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que el pulso de la izquierda te acompañe como el tictac tranquilo de un reloj.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['G4', 'A4', 'B4', 'C5', 'D5', 'C5', 'B4', 'A4', 'G4', 'B4', 'C5', 'B4', 'A4', 'B4', 'C5', 'D5']]
    bass5 = [{'pitch': p, 'dur': 'w'} for p in ['G3', 'C3', 'D3', 'G3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · tranquila, sin prisa', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
