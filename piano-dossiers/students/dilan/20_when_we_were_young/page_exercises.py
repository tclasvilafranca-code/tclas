# -*- coding: utf-8 -*-
"""Taller de practica - When We Were Young (Dilan, cancion 20, Re menor,
   4/4). Estructura DISTINTA otra vez: la partitura real esta llena de
   acordes con cifrado de bajo (Fmaj7/A, Gm7...) -- el foco es un
   concepto teorico nuevo: el BAJO no siempre es la fundamental del
   acorde. Primera vez en Re menor para Dilan."""
from page_layout_common import *

SONG_KICKER = 'DILAN · MAYO · WHEN WE WERE YOUNG (ADELE)'
TS = (4, 4)

DM = ['D3', 'F3', 'A3']
FM = ['F3', 'A3', 'C4']
FM_A = ['A2', 'F3', 'A3']
BbM = ['D3', 'F3', 'Bb3']
GM = ['G2', 'Bb2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Adele, en Re menor. Los acordes llevan un bajo que no siempre es la fundamental.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re menor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa(3) Sol(4) La(5). Todo teclas blancas, centro tonal en Re.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 5), ('F4', 3), ('G4', 4), ('E4', 2), ('F4', 3), ('D4', 1)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Baja a saltos desde el La', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 3), ('D4', 1), ('A4', 5), ('D4', 1)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re menor, desde el Fa', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El bajo que no es la fundamental', 2,
                          'Un acorde de Fa siempre tiene las notas Fa-La-Do... pero la nota más grave no siempre es el Fa. Cuando el bajo es otra nota del acorde, se escribe "Fa/La": el mismo acorde, apoyado en otra pierna.')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FM, 'Fa'), (FM, None)]]
    y = system_block(c, x0, w0, y, gap, 'a) Fa, con el bajo normal (Fa abajo)', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FM_A, 'Fa/La'), (FM_A, None)]]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo acorde de Fa, con el bajo en La (Fa/La)', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'A4']]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DM, 'Rem'), (FM_A, 'Fa/La')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) De Rem a Fa/La: el bajo baja solo un escalón', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes de la canción en Re menor', 2,
                          'Rem–Fa–Sib–Fa: la progresión que sostiene la balada.')
    y -= 11
    pattern_a = [(DM, 'Rem'), (FM, 'Fa'), (BbM, 'Sib/Re'), (FM, 'Fa')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Rem-Fa-Sib-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, un bajo que camina, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · melodía sobre acordes con bajo variado', 2,
                          'La izquierda cambia de bajo aunque el acorde de arriba sea parecido; la derecha canta encima.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('A4', 5), ('F4', 3), ('G4', 4), ('E4', 2), ('F4', 3), ('D4', 1), ('E4', 2), ('F4', 3)]]
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DM, 'Rem'), (FM_A, 'Fa/La'), (GM, 'Solm'), (FM, 'Fa')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) El bajo camina, el acorde canta', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El bajo que baja escalón a escalón', 3,
                          'Escucha cómo el bajo baja de nota en nota (Re, Do, Sib, La) aunque los acordes de arriba cambien de forma distinta. Eso es lo que hace un bajo con inversiones: suena conectado.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'A4', 'D5', 'C5', 'Bb4', 'A4']]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DM, 'Rem'), (FM_A, 'Fa/La')]] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) El bajo Re-Fa/La, repetido con calma', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · When We Were Young casi entera', 3,
                          'Con la partitura al lado: fíjate en el cifrado con barra ("/") — te dice qué nota va en el bajo.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('A4', 5), ('F4', 3), ('G4', 4), ('E4', 2), ('F4', 3), ('D4', 1), ('E4', 2), ('F4', 3)]]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'A4', 'D5', 'C5', 'Bb4', 'A4']]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(DM, 'Rem'), (FM_A, 'Fa/La'), (GM, 'Solm'), (FM, 'Fa'), (DM, 'Rem'), (FM_A, 'Fa/La'), (BbM, 'Sib/Re'), (FM, 'Fa')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La balada casi completa · ♩≈68', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
