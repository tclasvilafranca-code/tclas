# -*- coding: utf-8 -*-
"""Taller de practica - Nuovo Cinema Paradiso (Nel, cancion 13,
   Sib mayor, compas mixto 4/4<->2/4). Enfoque: el compas que cambia
   -- contar 4 y luego contar 2, sin perder el hilo de la musica."""
from page_layout_common import *

SONG_KICKER = 'NEL · ABRIL · NUOVO CINEMA PARADISO (ENNIO MORRICONE)'
TS44 = (4, 4)
TS24 = (2, 4)

Bb = ['Bb2', 'D3', 'F3']
F = ['F2', 'A2', 'C3']
Gm = ['G2', 'Bb2', 'D3']
Eb = ['Eb2', 'G2', 'Bb2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de Ennio Morricone en Sib mayor. El reto: el compás cambia entre 4/4 y 2/4.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sib mayor', 1,
                          'Un dedo por tecla: Sib(1) Do(2) Re(3) Mib(4) Fa(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('Bb4', 1), ('C5', 2), ('D5', 3), ('Eb5', 4), ('F5', 5), ('Eb5', 4), ('D5', 3), ('C5', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un recorrido por la posición', ev1a, clef='treble', time_sig=TS44)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'D5', 'F5', 'D5'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sib, desgranado', ev1b, clef='treble', time_sig=TS44)
    y -= 3

    y = exercise_heading(c, y, 2, 'El compás que cambia: contar 4 y luego contar 2', 2,
                          'La dificultad exacta de esta canción. La música pasa de 4/4 a 2/4 sin avisar — hay que sentir el cambio de pulso, sin perder el hilo.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'a) La frase en 4/4', ev2a, clef='treble', time_sig=TS44)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'Eb5', 'F5', 'Eb5', 'D5', 'C5', 'Bb4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, ahora en 2/4: cuenta solo 1-2', ev2b, clef='treble', time_sig=TS24)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'C5']]
    bass2c = [{'pitches': Bb, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase en 4/4 sobre el acorde de Sib, sostenido entero', grand_gap_mult=7.3, time_sig=TS44)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes reales de la canción', 2,
                          'Sib–Fa–Solm–Mib: los cuatro acordes reales de esta canción.')
    y -= 11
    pattern_a = [(Bb, 'Sib'), (F, 'Fa'), (Gm, 'Solm'), (Eb, 'Mib')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sib-Fa-Solm-Mib, un acorde por compás entero', eva, clef='bass', time_sig=TS44)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, en los dos compases: sin perder el hilo cuando cambia el pulso.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · en 4/4, sobre el acorde de Fa', 2,
                          'La izquierda sostiene el acorde entero, quieta; la derecha canta la frase en 4/4.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']]
    bass1 = [{'pitches': F, 'dur': 'w'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase en 4/4 sobre Fa, sostenido entero', grand_gap_mult=7.3, time_sig=TS44)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'G4', 'A4', 'Bb4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, en 4/4: para comparar', treb2, clef='treble', time_sig=TS44)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · en 2/4, contando solo hasta dos', 3,
                          'La izquierda sostiene su acorde con negras firmes en 2/4; la derecha canta despacio, contando 1-2, 1-2.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'Eb5', 'F5', 'Eb5', 'D5', 'C5', 'Bb4', 'C5']]
    bass3 = [{'pitches': Gm, 'dur': 'h'}] * 4
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase en 2/4; el acorde de Solm marca 1-2', grand_gap_mult=7.3, time_sig=TS24)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F5', 'Eb5', 'D5', 'C5', 'Bb4', 'C5', 'D5', 'Eb5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, en 2/4', treb4, clef='treble', time_sig=TS24)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Nuovo Cinema Paradiso casi entera', 3,
                          'Con la partitura al lado: recuerda que en la canción real este pasaje continúa cambiando entre 4/4 y 2/4 — aquí lo trabajamos en 4/4.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4']])
    bass5 = [{'pitches': p, 'dur': 'w'} for p in [Bb, Bb, F, F]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · en 4/4, sin perder el hilo', grand_gap_mult=7.3, time_sig=TS44)

    exercises_footer(c, 4)
    c.showPage()
