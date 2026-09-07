# -*- coding: utf-8 -*-
"""Taller de practica - Un Beso y una Flor (Nel, cancion 4, Fa
   mayor, 4/4). Angulo: la ANACRUSA -- cada frase real de la cancion
   arranca con un pequeno impulso (silencio de corchea + nota) antes
   del primer tiempo fuerte del compas."""
from page_layout_common import *

SONG_KICKER = 'NEL · OCTUBRE · UN BESO Y UNA FLOR (NINO BRAVO)'
TS = (4, 4)

FA = ['F2', 'A2', 'C3']
BB = ['Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Nino Bravo en Fa mayor. El reto: la misma anacrusa antes de cada frase.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca siempre la tecla negra Sib.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('G4', 2), ('Bb4', 4), ('A4', 3), ('C5', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('C5', 5), ('A4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La anacrusa: el mismo impulso antes de cada frase', 2,
                          'La dificultad exacta de esta canción. Cada frase real empieza con un silencio de corchea y luego una nota corta que "empuja" hacia el tiempo fuerte — ese impulso debe sonar igual cada vez.')
    y -= 9
    ev2a = ([{'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
             {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'Bb4', 'dur': 'e'},
             {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}] * 2)
    y = system_block(c, x0, w0, y, gap, 'a) Silencio-empujón-frase: siente el impulso inicial', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'A4', 'A4', 'C5', 'Bb4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, sin el silencio inicial: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = ([{'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
               {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'Bb4', 'dur': 'e'},
               {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}] * 2)
    bass2c = [{'pitches': p, 'dur': 'h'} for p in [FA, FA, BB, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La anacrusa sobre un bajo tranquilo y sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (BB, 'Sib'), (DO, 'Do'), (BB, 'Sib')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Sib, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: la anacrusa se apoya en un bajo que no se mueve de sitio.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la anacrusa sobre el bajo firme', 2,
                          'La izquierda sostiene el acorde entero; la derecha entra siempre con el mismo pequeño impulso antes del tiempo fuerte.')
    y -= 7
    treb1 = ([{'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
              {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'Bb4', 'dur': 'e'},
              {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}] * 2)
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [FA, FA, FA, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La anacrusa, con el acorde de Fa sostenido debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'Bb4', 'A4', 'G4', 'A4', 'Bb4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando dónde cae el impulso', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el bajo no se contagia del impulso', 3,
                          'La izquierda queda perfectamente quieta con el acorde sostenido; la derecha entra y sale con su anacrusa sin arrastrar a la de abajo.')
    y -= 7
    treb3 = ([{'rest': True, 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'},
              {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'D5', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'},
              {'pitch': 'Bb4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}] * 2)
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [BB, BB, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El impulso vuela; el acorde no se altera', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'C5', 'Bb4', 'A4', 'Bb4', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Un Beso y una Flor casi entera', 3,
                          'Con la partitura al lado: haz que cada anacrusa suene exactamente igual, como una firma que se repite frase tras frase.')
    y -= 7
    treb5 = ([{'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
              {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'Bb4', 'dur': 'e'},
              {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}] * 2 +
             [{'rest': True, 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'},
              {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'D5', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'},
              {'pitch': 'Bb4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}] * 2)
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [FA, FA, BB, FA, BB, BB, DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Allegro, con la anacrusa siempre igual', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
