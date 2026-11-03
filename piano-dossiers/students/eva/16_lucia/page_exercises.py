# -*- coding: utf-8 -*-
"""Taller de practica - Lucia (Eva, cancion 16, La menor, 4/4). Mismo
   arreglo que el de Dilan (que trabaja el bajo de Alberti), pero enfoque
   DISTINTO para Eva: los MATICES QUE CUENTAN UNA HISTORIA -- la letra
   narra una historia real, y la dinamica debe seguir el relato, no
   quedarse plana."""
from page_layout_common import *

SONG_KICKER = 'EVA · MAYO · LUCÍA (JOAN MANUEL SERRAT)'
TS = (4, 4)

AM = ['A2', 'C3', 'E3']
DM = ['D2', 'F2', 'A2']
E7 = ['E2', 'G#2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Serrat en La menor. El reto: los matices siguen la historia, sin quedarse planos.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en La menor', 1,
                          'Un dedo por tecla: La(1) Si(2) Do(3) Re(4) Mi(5). Misma armadura que Do mayor, centro tonal en La.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('B4', 2), ('D5', 4), ('E5', 5), ('D5', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 1), ('C5', 3), ('E5', 5), ('C5', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de La menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Los matices que cuentan la historia', 2,
                          'La dificultad exacta de esta canción. La letra narra algo real — toca la misma frase tres veces, contando con el volumen si la historia empieza tranquila, se agita o se calma otra vez.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'B4', 'A4', 'C5', 'D5', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) Piano: el principio de la historia, tranquilo', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'B4', 'A4', 'C5', 'D5', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Forte: el momento más intenso de la historia', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'B4', 'A4', 'C5', 'D5', 'C5', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'c) Piano otra vez: la historia se calma al final', ev2c, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V7 en La menor', 2,
                          'Lam–Rem–Mi7: los acordes de esta tonalidad menor.')
    y -= 9
    pattern_a = [(AM, 'Lam'), (E7, 'Mi7'), (DM, 'Rem'), (AM, 'Lam')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Lam-Mi7-Rem-Lam, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(AM, 'Lam'), (DM, 'Rem'), (E7, 'Mi7'), (AM, 'Lam')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas tranquilas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: deja que la dinámica cuente la historia con las dos manos a la vez.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el principio tranquilo de la historia', 2,
                          'La izquierda sostiene el acorde con calma; la derecha canta piano, como si empezara a contar algo.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'C5', 'B4', 'A4', 'C5', 'D5', 'C5', 'A4']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [AM, DM, E7, AM]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Piano, contenido, el inicio de la historia', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['A4', 'C5', 'B4', 'D5'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) La historia se agita: la melodía se mueve más rápido', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'El momento más intenso, a dos manos', 3,
                          'Ahora las dos manos suenan grandes juntas — el clímax de la historia, sin perder precisión.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['C5', 'E5', 'D5', 'C5'] * 4)]
    bass3 = [{'pitches': p, 'dur': 'q'} for p in [AM, AM, DM, DM, E7, E7, AM, AM]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Forte total: el clímax de la historia', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5', 'A4', 'B4', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: las mismas notas, tranquilas', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Lucía casi entera', 3,
                          'Con la partitura al lado: deja que los matices cuenten la historia completa, de principio a fin.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['A4', 'C5', 'B4', 'A4', 'C5', 'D5', 'C5', 'A4', 'C5', 'E5', 'D5', 'C5', 'B4', 'A4', 'C5', 'A4']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [AM, DM, E7, AM, AM, DM, E7, AM]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈84, con relato', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
