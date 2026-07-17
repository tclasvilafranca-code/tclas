# -*- coding: utf-8 -*-
"""Taller de practica - Soldadito de Hierro (Eva, cancion 5, LA MENOR, 4/4).
   Mismo arreglo que el de Dilan (que trabaja los grupos de tres), pero
   enfoque DISTINTO para Eva: el CRESCENDO hacia el estribillo. La cancion
   real crece de estrofa intima a estribillo grande -- el reto es construir
   ese crecimiento poco a poco, no dar el salto de golpe."""
from page_layout_common import *

SONG_KICKER = 'EVA · NOVIEMBRE · SOLDADITO DE HIERRO (NIL MOLINER)'
TS = (4, 4)

AM = ['A2', 'C3', 'E3']
DM = ['D2', 'F2', 'A2']
E7 = ['E2', 'G#2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción en La menor con la derecha muy viva. El reto: construir el crescendo hacia el estribillo.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento de matices: la misma frase, piano y forte', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Toca esta frase en saltos de terceras dos veces: primero piano, luego forte.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('B4', 2), ('D5', 4), ('C5', 3), ('E5', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Piano: saltos de terceras, contenidos', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('B4', 2), ('D5', 4), ('C5', 3), ('E5', 5)] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Forte: la misma frase, con toda su fuerza', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'De piano a forte: el crecimiento en tres pasos', 2,
                          'La dificultad exacta de esta canción. La estrofa empieza íntima (p) y crece hasta el estribillo (f) — pero el crecimiento tiene que sentirse gradual, no un salto brusco.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'B4', 'A4', 'C5', 'D5', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) Piano (p): la estrofa, íntima y contenida', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'B4', 'A4', 'C5', 'D5', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Mezzoforte (mf): la misma frase, un escalón más', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'B4', 'A4', 'C5', 'D5', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'c) Forte (f): la misma frase, el estribillo con toda su fuerza', ev2c, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V7 en La menor', 2,
                          'Lam–Rem–Mi7: los acordes de esta tonalidad menor, aquí más movidos que en la canción real.')
    y -= 9
    pattern_a = [(AM, 'Lam'), (E7, 'Mi7'), (DM, 'Rem'), (E7, 'Mi7')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Mi7-Rem-Mi7, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'e', 'beam': i // 2, 'label': l} for i, (p, l) in enumerate(
        [(AM, 'Lam'), (AM, None), (E7, 'Mi7'), (E7, None), (DM, 'Rem'), (DM, None), (AM, 'Lam'), (AM, None)] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, repetidos en corcheas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: deja que el crescendo suba con las dos manos a la vez.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · construyendo el crescendo', 2,
                          'Las dos manos crecen juntas, de p a f, sin que ninguna se adelante a la otra.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'B4', 'A4', 'C5', 'D5', 'C5', 'A4']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [AM, DM, E7, AM]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Piano: la estrofa, contenida en las dos manos', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['A4', 'C5', 'B4', 'D5'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) La melodía se mueve más rápido cuando crece', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia dinámica · el estribillo con toda su fuerza', 3,
                          'Ahora el crescendo llega al final: las dos manos suenan grandes, sin perder la precisión de los grupos de tres.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['C5', 'D5', 'E5', 'D5'] * 4)]
    bass3 = [{'pitches': AM, 'dur': 'q'}, {'pitches': AM, 'dur': 'q'}, {'pitches': DM, 'dur': 'q'}, {'pitches': DM, 'dur': 'q'},
             {'pitches': E7, 'dur': 'q'}, {'pitches': E7, 'dur': 'q'}, {'pitches': AM, 'dur': 'q'}, {'pitches': AM, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Forte total: las dos manos a plena potencia', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: las mismas notas, tranquilas', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Soldadito de Hierro casi entero', 3,
                          'Con la partitura al lado: siente cómo la canción crece de estrofa a estribillo, sin dar el salto de golpe.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
             ['A4', 'C5', 'B4'] * 4 + ['C5', 'D5', 'E5'] * 4)]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [AM, DM, E7, AM, DM, AM]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Enérgico ♩≈84, con crescendo', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
