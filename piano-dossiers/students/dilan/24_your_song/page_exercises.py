# -*- coding: utf-8 -*-
"""Taller de practica - Your Song (Dilan, cancion 24 de 24, Mib mayor,
   4/4). Estructura DISTINTA otra vez -- y pieza de CIERRE del curso: el
   foco es la fluidez en una tonalidad con muchos bemoles, poniendo a
   prueba todo el camino recorrido desde Do mayor hasta aqui."""
from page_layout_common import *

SONG_KICKER = 'DILAN · JUNIO · YOUR SONG (ELTON JOHN) · CIERRE DE CURSO'
TS = (4, 4)

EbM = ['Eb2', 'G2', 'Bb2']
AbM = ['C3', 'Eb3', 'Ab3']
BbM = ['D3', 'F3', 'Bb3']
Cm = ['C3', 'Eb3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La canción de cierre del curso, en Mib mayor: tres bemoles, mucha fluidez.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mib mayor', 1,
                          'Un dedo por tecla: Mib(1) Fa(2) Sol(3) Lab(4) Sib(5). Los dedos 1 y 4 tocan teclas negras.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('Eb4', 1), ('F4', 2), ('G4', 3), ('Ab4', 4), ('G4', 3), ('F4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sintiendo los tres bemoles', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('Eb4', 1), ('G4', 3), ('Bb4', 5), ('G4', 3)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mib, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Fluidez en una tonalidad con muchos bemoles', 2,
                          'Tres bemoles a la vez ya no dan miedo si los lees con soltura, sin pararte en cada nota. Toca esta frase fluida, como una ola que no se corta.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['Eb4', 'F4', 'G4', 'Ab4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'a) Corcheas fluidas, sin cortes', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['Bb4', 'Ab4', 'G4', 'F4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) La misma fluidez, bajando', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in
              enumerate(['Eb4', 'F4', 'G4', 'Ab4', 'Bb4', 'Ab4', 'G4', 'F4'])]
    bass2c = [{'pitches': EbM, 'dur': 'w', 'label': 'Mib'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Fluidez sobre un acorde sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes de Mib mayor', 2,
                          'Mib–Lab–Sib–Dom: los acordes que sostienen la canción.')
    y -= 11
    pattern_a = [(EbM, 'Mib'), (AbM, 'Lab'), (BbM, 'Sib'), (Cm, 'Dom')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mib-Lab-Sib-Dom, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, fluidez con acordes que cambian, y el cierre del curso entero.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · melodía fluida sobre acordes', 2,
                          'La izquierda sostiene; la derecha fluye sin cortes, como agua.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['Eb4', 'F4', 'G4', 'Ab4'] * 4)]
    bass4 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(EbM, 'Mib'), (AbM, 'Lab')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La fluidez sobre Mib y Lab', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'La fluidez con acordes que cambian más rápido', 3,
                          'Ahora el acorde de abajo cambia cada dos tiempos: la izquierda se mueve sin que la derecha pierda su fluidez.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['Bb4', 'Ab4', 'G4', 'F4'] * 4)]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(EbM, 'Mib'), (BbM, 'Sib'), (AbM, 'Lab'), (EbM, 'Mib')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Fluidez con la izquierda moviéndose', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Your Song, y el cierre del curso', 3,
                          'Con la partitura al lado: esta es la canción número 24. Mira todo lo que sabes ya — cinco bemoles, acordes con séptima, compases nuevos, cruces de manos, pedal. Disfrútala.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['Eb4', 'F4', 'G4', 'Ab4'] * 2)]
    treb6 += [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['Bb4', 'Ab4', 'G4', 'F4'] * 2)]
    bass6 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(EbM, 'Mib'), (BbM, 'Sib')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · ♩≈66', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
