# -*- coding: utf-8 -*-
"""Taller de practica - My Favourite Things (Dilan, cancion 22, Mi menor,
   3/4). Estructura DISTINTA otra vez: la partitura real va muy rapida
   (♩=160, vals). El foco es un METODO de practica -- empezar despacio
   y subir la velocidad poco a poco -- distinto de la IGUALDAD trabajada
   en Thinking Out Loud (que ya iba siempre al tempo final)."""
from page_layout_common import *

SONG_KICKER = 'DILAN · JUNIO · MY FAVOURITE THINGS (SOUND OF MUSIC)'
TS = (3, 4)

MIm = ['E3', 'G3', 'B3']
DO = ['C3', 'E3', 'G3']
LAm = ['C3', 'E3', 'A3']
RE = ['D3', 'F#3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un vals de "Sonrisas y lágrimas", en Mi menor y muy rápido (♩≈160).')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El dedo 2 toca la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('B4', 5), ('G4', 3), ('A4', 4), ('F#4', 2), ('G4', 3), ('E4', 1)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Baja a saltos desde el Si', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 3), ('E4', 1), ('B4', 5), ('E4', 1)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, desde el Sol', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El método: empezar despacio, subir poco a poco', 2,
                          'Nadie toca esto rápido a la primera. La técnica de verdad es un método: aprende la frase muy despacio, y solo cuando salga perfecta, sube un poco la velocidad. Repite.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'A4', 'G4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'a) Paso 1 — muy despacio (♩≈80), sin fallos', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'A4', 'G4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Paso 2 — un poco más rápido (♩≈110), igual de limpio', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'A4', 'G4', 'F#4']]
    bass2c = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(MIm, 'Mim'), (MIm, None)]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Paso 3 — con la izquierda, todavía controlado', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Los acordes reales de la canción', 2,
                          'Mim–Do–Lam–Re: la canción real usa estos cuatro, no solo los tres básicos.')
    y -= 11
    pattern_a = [(MIm, 'Mim'), (DO, 'Do'), (LAm, 'Lam'), (RE, 'Re')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, el método de velocidad con acordes que se mueven, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el vals con acordes que cambian', 2,
                          'La izquierda marca un acorde por compás; la derecha canta la melodía por encima.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'A4', 'G4', 'F#4', 'E4', 'F#4', 'G4', 'A4', 'G4', 'F#4']]
    bass4 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(MIm, 'Mim'), (MIm, None), (DO, 'Do'), (DO, None)]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La melodía sobre Mim y Do', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El método aplicado con las dos manos', 3,
                          'Igual que en la página 1: primero muy despacio con las dos manos juntas, y solo subes la velocidad cuando salga sin fallos.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'E4', 'A4', 'F#4', 'B4', 'G4']]
    bass5 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(LAm, 'Lam'), (RE, 'Re')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Despacio primero: Lam y Re', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · My Favourite Things casi entera', 3,
                          'Con la partitura al lado: si te atropellas, vuelve al paso lento. La velocidad se gana, no se fuerza.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q'} for p in
             ['E4', 'G4', 'B4', 'A4', 'G4', 'F#4', 'E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'G4', 'E4', 'A4', 'F#4', 'B4', 'G4']]
    bass6 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(MIm, 'Mim'), (DO, 'Do'), (LAm, 'Lam'), (RE, 'Re'), (MIm, 'Mim'), (RE, 'Re')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · ♩≈160, con chispa', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
