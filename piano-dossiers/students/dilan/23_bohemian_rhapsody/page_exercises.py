# -*- coding: utf-8 -*-
"""Taller de practica - Bohemian Rhapsody (Dilan, cancion 23, Sib mayor,
   4/4). Estructura DISTINTA otra vez -- y pieza-cumbre del curso: la
   partitura real esta llena de acordes con septima (C7, F7...) que se
   mueven deprisa. El foco es la LECTURA FLUIDA de cifrado armonico
   rico, poniendo en juego todo lo aprendido sobre acordes este año."""
from page_layout_common import *

SONG_KICKER = 'DILAN · JUNIO · BOHEMIAN RHAPSODY (QUEEN)'
TS = (4, 4)

BbM = ['D3', 'F3', 'Bb3']
C7 = ['C3', 'E3', 'Bb3']
FM = ['F2', 'A2', 'C3']
Gm = ['G2', 'Bb2', 'D3']
EbM = ['Eb2', 'G2', 'Bb2']
Cm = ['C3', 'Eb3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La pieza más rica en acordes de todo el año, en Sib mayor. Aquí se junta todo lo aprendido.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Los seis acordes del año, uno detrás de otro', 1,
                          'La pieza de cierre del curso junta todo lo aprendido: reconoce cada forma de acorde y encadénalas sin parar, como pasando las páginas de un álbum entero.')
    y -= 12
    ev1a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
            [(BbM, 'Sib'), (C7, 'Do7'), (FM, 'Fa'), (Gm, 'Solm'), (EbM, 'Mib'), (Cm, 'Dom')]]
    y = system_block(c, x0, w0, y, gap, 'a) Los seis, con calma, sintiendo cada forma', ev1a, clef='bass', time_sig=TS)

    ev1b = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
            [(BbM, 'Sib'), (C7, 'Do7'), (FM, 'Fa'), (Gm, 'Solm'), (EbM, 'Mib'), (Cm, 'Dom'), (BbM, 'Sib'), (FM, 'Fa')]]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora el doble de rápido, sin dudar entre uno y otro', ev1b, clef='bass', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Leer con fluidez: acordes con séptima', 2,
                          'Esta canción se mueve por muchos acordes distintos, varios con séptima (C7, F7...). El reto es reconocerlos y tocarlos sin dudar, como leyendo una frase, no letra a letra.')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(BbM, 'Sib'), (C7, 'Do7')]]
    y = system_block(c, x0, w0, y, gap, 'a) Sib, y su vecino con séptima: Do7', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FM, 'Fa'), (Gm, 'Solm')]]
    y = system_block(c, x0, w0, y, gap, 'b) Fa, y el acorde menor Sol menor', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'C5']]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(BbM, 'Sib'), (C7, 'Do7')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Sib a Do7, con la melodía encima', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'La progresión real de la canción', 2,
                          'Sib–Do7–Fa–Solm: cuatro acordes distintos, tal como abre la canción de verdad.')
    y -= 11
    pattern_a = [(BbM, 'Sib'), (C7, 'Do7'), (FM, 'Fa'), (Gm, 'Solm')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sib-Do7-Fa-Solm, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, más acordes de la canción, y el fragmento casi entero.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la progresión real', 2,
                          'La izquierda se mueve por Sib-Do7-Fa-Solm; la derecha canta encima.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('Bb4', 1), ('C5', 2), ('D5', 3), ('Eb5', 4), ('D5', 3), ('C5', 2), ('Bb4', 1), ('C5', 2)]]
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(BbM, 'Sib'), (C7, 'Do7'), (FM, 'Fa'), (Gm, 'Solm')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La melodía sobre la progresión', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Dos acordes más de la canción', 3,
                          'Mib mayor y Do menor: los otros dos colores que aparecen más adelante en la canción real.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['Eb5', 'D5', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4']]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(EbM, 'Mib'), (Cm, 'Dom'), (EbM, 'Mib'), (Cm, 'Dom')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Mib-Dom-Mib-Dom, dos colores nuevos', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Bohemian Rhapsody casi entera', 3,
                          'Con la partitura al lado: seis acordes distintos en total. Léelos con calma la primera vez, luego busca la fluidez.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('Bb4', 1), ('C5', 2), ('D5', 3), ('Eb5', 4), ('D5', 3), ('C5', 2), ('Bb4', 1), ('C5', 2)]]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['Eb5', 'D5', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4']]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(BbM, 'Sib'), (C7, 'Do7'), (FM, 'Fa'), (Gm, 'Solm'), (EbM, 'Mib'), (Cm, 'Dom'), (EbM, 'Mib'), (BbM, 'Sib')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'El fragmento casi completo · ♩≈66', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
