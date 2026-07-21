# -*- coding: utf-8 -*-
"""Taller de practica - Bella Ciao (Josep, cancion 8, Sol menor, 4/4,
   a 4 manos). Angulo: el CONTRATIEMPO -- acordes cortos que caen
   entre los pulsos, como un acompanamiento de guitarra, tal como
   hace el Piano 2 de la version real."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · DICIEMBRE · BELLA CIAO (A 4 MANOS)'
TS = (4, 4)

Gm = ['G2', 'Bb2', 'D3']
Cm = ['C3', 'Eb3', 'G3']
D = ['D3', 'F#3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción popular italiana en Sol menor, a 4 manos. El reto: acordes que caen entre los pulsos.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol menor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Sib(3) Do(4) Re(5). El dedo 3 toca la tecla negra Sib.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('Bb4', 3), ('A4', 2), ('C5', 4), ('Bb4', 3), ('D5', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('Bb4', 3), ('D5', 5), ('Bb4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El contratiempo: acordes que caen entre los pulsos', 2,
                          'La dificultad exacta de esta pieza. El acompañamiento no toca en el tiempo, sino en el silencio de después — como el rasgueo de una guitarra que "chasquea" entre pulso y pulso.')
    y -= 9
    ev2a = [{'rest': True, 'dur': 'q'}, {'pitches': Gm, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': Gm, 'dur': 'q'}] * 2
    y = system_block(c, x0, w0, y, gap, 'a) Silencio-acorde, silencio-acorde: el contratiempo puro', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'q'} for p in [Gm, Gm, Gm, Gm]] * 2
    y = system_block(c, x0, w0, y, gap, 'b) El mismo acorde, ahora encima del tiempo: para comparar', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['D5', 'Bb4', 'C5', 'A4']]
    bass2c = [{'rest': True, 'dur': 'q'}, {'pitches': Gm, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': Gm, 'dur': 'q'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía larga sobre el contratiempo de abajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en Sol menor', 2,
                          'Solm–Dom–Re: los tres acordes de esta tonalidad. El Re lleva un Fa# — la sensible que empuja hacia Sol.')
    y -= 11
    pattern_a = [(Gm, 'Solm'), (Cm, 'Dom'), (D, 'Re'), (Gm, 'Solm')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Solm-Dom-Re-Solm, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el contratiempo se apoya en una melodía que sí respeta el pulso.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el contratiempo bajo la melodía', 2,
                          'La derecha canta la melodía en el tiempo; la izquierda "chasquea" el acorde justo en el hueco de después, nunca a la vez.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Bb4', 'C5', 'Bb4', 'A4', 'Bb4', 'C5', 'D5']]
    bass1 = [{'rest': True, 'dur': 'q'}, {'pitches': Gm, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': Gm, 'dur': 'q'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía en el tiempo; el acorde en el contratiempo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'A4', 'G4', 'A4', 'Bb4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando dónde cae el pulso', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el contratiempo no se contagia de la melodía', 3,
                          'La derecha se mueve más rápido; la izquierda sigue chasqueando exactamente en el mismo hueco, sin adelantarse.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['D5', 'C5', 'Bb4', 'A4', 'G4', 'Bb4', 'C5', 'D5'] * 2)]
    bass3 = [{'rest': True, 'dur': 'q'}, {'pitches': Cm, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': D, 'dur': 'q'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La derecha vuela; el contratiempo no se adelanta', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Bella Ciao casi entera', 3,
                          'Con la partitura al lado: mantén el chasquido del contratiempo exactamente en su sitio, canción entera.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['G4', 'Bb4', 'C5', 'Bb4', 'A4', 'Bb4', 'C5', 'D5', 'D5', 'C5', 'Bb4', 'A4', 'G4', 'A4', 'Bb4', 'G4']]
    bass5 = ([{'rest': True, 'dur': 'q'}, {'pitches': Gm, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': Gm, 'dur': 'q'}] * 2 +
             [{'rest': True, 'dur': 'q'}, {'pitches': Cm, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': D, 'dur': 'q'}] * 2)
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈100, con el contratiempo firme', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
