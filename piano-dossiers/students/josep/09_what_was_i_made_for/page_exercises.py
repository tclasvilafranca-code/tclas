# -*- coding: utf-8 -*-
"""Taller de practica - What Was I Made For? (Josep, cancion 9, Do
   mayor, 4/4). Mismo arreglo que el de Dilan (contar silencios) y
   el de Eva (pianissimo constante), pero enfoque DISTINTO para
   Josep: el ARCO DINAMICO LARGO -- crecer y menguar a lo largo de
   una frase entera de 8 compases, no mantener un volumen fijo."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · ENERO · WHAT WAS I MADE FOR? (BILLIE EILISH)'
TS = (4, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
Em = ['E3', 'G3', 'B3']
Am = ['A2', 'C3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Billie Eilish en Do mayor. El reto: un arco dinámico largo, no un volumen fijo.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Todo teclas blancas.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('E4', 3), ('D4', 2), ('F4', 4), ('E4', 3), ('G4', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 5), ('E4', 3), ('C4', 1), ('E4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El arco dinámico largo: crecer y menguar en 8 compases', 2,
                          'La dificultad exacta de esta canción. La frase entera dibuja un arco: empieza suave, crece hasta un punto y vuelve a bajar — no se trata de mantener un volumen fijo.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'E4', 'G4', 'E4', 'C5', 'A4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja: siente el arco completo de la frase', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'C4', 'C4', 'C4', 'C4', 'C4', 'C4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma nota ocho veces: el volumen debe moverse igual, sin la ayuda de la melodía', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'E4', 'G4', 'E4', 'C5', 'A4', 'G4', 'E4']]
    bass2c = [{'pitches': p, 'dur': 'h'} for p in [DO, Em, FA, DO, Em, FA, DO, Em]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El arco de la melodía sobre los acordes reales', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–vi en Do mayor', 2,
                          'Do–Mim–Fa–Lam: los acordes reales de esta canción, más ricos que un simple I-IV-V.')
    y -= 11
    pattern_a = [(DO, 'Do'), (Em, 'Mim'), (FA, 'Fa'), (Am, 'Lam')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Mim-Fa-Lam, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el arco dinámico se dibuja entre las dos, no solo con la melodía.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el arco dinámico completo', 2,
                          'La izquierda sostiene los acordes reales; la derecha dibuja el arco entero, creciendo hacia la mitad de la frase y bajando otra vez.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'G4', 'C5', 'A4', 'G4', 'E4', 'D4', 'C4']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [DO, Em, FA, DO, Em, FA, DO, Em]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El arco entero, con los acordes reales debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'D4', 'E4', 'G4', 'E4', 'D4', 'C4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando dónde está el punto más alto', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no dibuja su propio arco', 3,
                          'La izquierda toca los acordes con un volumen estable; solo la derecha dibuja el crecimiento y la bajada del arco.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'C5', 'G4', 'E4', 'D4', 'C4']]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [Am, FA, Am, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde estable; la melodía dibuja el arco', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'C5', 'A4', 'G4', 'E4', 'D4', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: el arco un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · What Was I Made For casi entera', 3,
                          'Con la partitura al lado: no toques todo al mismo volumen — deja que la frase respire, crezca y vuelva a bajar.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'h'} for p in
             ['C4', 'E4', 'G4', 'E4', 'C5', 'A4', 'G4', 'E4', 'G4', 'A4', 'C5', 'A4', 'G4', 'E4', 'D4', 'C4']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [DO, Em, FA, DO, Em, FA, Am, FA, DO, Em, FA, DO, Em, FA, Am, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈78, con el arco siempre presente', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
