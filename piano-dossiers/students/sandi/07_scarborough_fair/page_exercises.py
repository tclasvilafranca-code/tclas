# -*- coding: utf-8 -*-
"""Taller de practica - Scarborough Fair (Sandi, cancion 7, balada
   tradicional inglesa, arr. Jim Paterson, armadura de 1 bemol (Sib)
   -- caracter modal, Re dorico -- confirmada por render directo,
   compas mixto 6/8 y 3/8 alternandose). Nivel avanzado: el compas
   cambiante -- 6/8 y 3/8, sin perder el pulso de la corchea."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · SCARBOROUGH FAIR'
TS68 = (6, 8)
TS38 = (3, 8)

REm = ['D2', 'F2', 'A2']
DO = ['C2', 'E2', 'G2']
FA = ['F2', 'A2', 'C3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Scarborough Fair, balada tradicional inglesa. Hoy: el compás cambiante, 6/8 y 3/8.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re menor (modo dórico)', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa(3) Sol(4) La(5). Sonido modal, sin sensible: recuerda a Re menor pero con carácter antiguo.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['D4', 'E4', 'F4', 'G4', 'A4', 'G4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición, en corcheas', ev1a, clef='treble', time_sig=TS68)

    ev1b = [{'pitch': p, 'dur': 'e'} for p in ['D4', 'F4', 'A4', 'F4', 'D4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re menor, arpegiado en corcheas', ev1b, clef='treble', time_sig=TS68)
    y -= 3

    y = exercise_heading(c, y, 2, 'El compás cambiante: 6/8 y 3/8, sin perder el pulso', 3,
                          'La dificultad de hoy. La pieza alterna compases de 6/8 (dos pulsos grandes de tres corcheas) y de 3/8 (un solo pulso de tres corcheas): la corchea debe seguir sonando exactamente igual de rápido al cambiar de compás, sin acelerones ni parones.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['D4', 'F4', 'A4', 'A4', 'G4', 'F4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Un compás de 6/8: dos pulsos grandes de tres corcheas', ev2a, clef='treble', time_sig=TS68)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['G4', 'F4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Un compás de 3/8: un solo pulso grande, sin frenar ni acelerar', ev2b, clef='treble', time_sig=TS38)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['D4', 'F4', 'A4'])]
    bass2c = [{'pitches': REm, 'dur': 'q.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Un compás de 3/8 con manos juntas: el mismo pulso que en 6/8', grand_gap_mult=7.3, time_sig=TS38)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–III–iv en Re dórico', 2,
                          'Rem–Do–Fa: los acordes característicos de este modo, sin sensible alterada.')
    y -= 11
    pattern_a = [(REm, 'Rem'), (DO, 'Do'), (FA, 'Fa'), (REm, 'Rem')]
    eva = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Rem-Do-Fa-Rem, un acorde por pulso de tres corcheas', eva, clef='bass', time_sig=TS68)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el pulso de la corchea no debe cambiar nunca, aunque el compás sí.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · de 6/8 a 3/8 sin fisuras', 3,
                          'La izquierda mece el acorde de Re menor en dos pulsos (6/8); la derecha responde con un solo pulso (3/8) exactamente a la misma velocidad de corchea.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['D5', 'C5', 'A4', 'A4', 'G4', 'F4'])]
    bass1 = [{'pitches': REm, 'dur': 'q.'}, {'pitches': REm, 'dur': 'q.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) 6/8 completo: dos pulsos grandes de Re menor', grand_gap_mult=7.3, time_sig=TS68)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['G4', 'A4', 'G4']]
    bass2 = [{'pitches': FA, 'dur': 'q.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2, bass2, 'b) 3/8: un solo pulso, a la misma velocidad exacta', grand_gap_mult=7.3, time_sig=TS38)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de Do no rompe el pulso modal', 3,
                          'La izquierda toca el acorde de Do (III grado del modo); la derecha mantiene su línea sin sensible, con el carácter antiguo intacto.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['E4', 'G4', 'C5', 'C5', 'B4', 'A4'])]
    bass3 = [{'pitches': DO, 'dur': 'q.'}, {'pitches': DO, 'dur': 'q.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La melodía modal sobre el acorde de Do, en 6/8', grand_gap_mult=7.3, time_sig=TS68)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['C5', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo gesto, comprimido en un compás de 3/8', treb4, clef='treble', time_sig=TS38)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Scarborough Fair casi entera', 3,
                          'Con la partitura al lado: mantén la corchea a la misma velocidad exacta al cruzar de 6/8 a 3/8 y viceversa.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['D5', 'C5', 'A4', 'A4', 'G4', 'F4'])] +
             [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['E5', 'G4', 'C5', 'C5', 'B4', 'A4'])])
    bass5 = [{'pitches': REm, 'dur': 'q.'}, {'pitches': REm, 'dur': 'q.'}, {'pitches': DO, 'dur': 'q.'}, {'pitches': DO, 'dur': 'q.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Scarborough Fair casi completa · pulso constante entre compases', grand_gap_mult=7.3, time_sig=TS68)

    exercises_footer(c, 4)
    c.showPage()
