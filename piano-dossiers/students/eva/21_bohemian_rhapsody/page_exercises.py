# -*- coding: utf-8 -*-
"""Taller de practica - Bohemian Rhapsody (Eva, cancion 21, Sib mayor,
   4/4). Mismo arreglo que el de Dilan (que trabaja la LECTURA FLUIDA
   de muchos acordes distintos), pero enfoque DISTINTO para Eva: el
   OIDO -- escuchar el color de cada acorde (mayor, menor, con tension)
   y reconocerlo de oido antes de confirmar el nombre con la vista.
   Es un ejercicio de audicion, no de velocidad lectora."""
from page_layout_common import *

SONG_KICKER = 'EVA · JUNIO · BOHEMIAN RHAPSODY (QUEEN)'
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
    c.drawString(MARGIN, y, 'La pieza más rica en acordes de todo el año, en Sib mayor. El reto: escuchar antes de mirar.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Los seis acordes del año, escuchados con calma', 1,
                          'Toca cada acorde y deja que suene entero antes de pasar al siguiente. Cierra los ojos si te ayuda: escucha su color antes de mirar el nombre.')
    y -= 12
    ev1a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
            [(EbM, 'Mib'), (Cm, 'Dom'), (FM, 'Fa'), (Gm, 'Solm'), (BbM, 'Sib'), (C7, 'Do7')]]
    y = system_block(c, x0, w0, y, gap, 'a) Los seis, con calma, escuchando cada color', ev1a, clef='bass', time_sig=TS)

    ev1b = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in
            [(BbM, 'Sib'), (FM, 'Fa'), (C7, 'Do7'), (Gm, 'Solm'), (Cm, 'Dom'), (EbM, 'Mib'), (BbM, 'Sib'), (FM, 'Fa')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos, ahora más rápido, reconociéndolos de oído', ev1b, clef='bass', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Escucha antes de mirar: mayor, menor o con tensión', 2,
                          'La dificultad exacta de esta canción: seis colores de acorde distintos. Antes de leer el nombre, escucha si suena mayor (brillante), menor (más oscuro) o con tensión (el Do7, que "pide" resolver).')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FM, 'Fa'), (Gm, 'Solm'), (FM, 'Fa'), (Gm, 'Solm')]]
    y = system_block(c, x0, w0, y, gap, 'a) Compara: Fa mayor (brillante) frente a Sol menor (más oscuro)', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(C7, 'Do7'), (BbM, 'Sib'), (C7, 'Do7'), (BbM, 'Sib')]]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde con tensión: Do7, que pide resolver hacia Sib', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5']]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FM, 'Fa'), (Gm, 'Solm'), (BbM, 'Sib'), (C7, 'Do7')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Con la melodía encima, sigue el color de cada acorde debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'La progresión real, acorde a acorde, sin prisa', 2,
                          'Sib–Do7–Fa–Solm: dale a cada acorde tiempo de sobra para escucharlo entero antes de adivinar su nombre.')
    y -= 11
    pattern_a = [(BbM, 'Sib'), (C7, 'Do7'), (FM, 'Fa'), (Gm, 'Solm')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Los cuatro acordes reales, en redondas, dejando que resuenen', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, el oído siguiendo el color, y el fragmento casi entero.')
    y -= 15
    gap = 7.05
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el oído guía a la mano', 2,
                          'La izquierda cambia de acorde; deja que el oído note el cambio de color un instante antes de que la vista confirme el nombre.')
    y -= 9
    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5']]
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FM, 'Fa'), (Gm, 'Solm'), (BbM, 'Sib'), (C7, 'Do7')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La melodía, con el acorde cambiando debajo', grand_gap_mult=7.05, time_sig=TS)

    treb4b = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando su forma', treb4b, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 5, 'Independencia · el oído sigue el color aunque las manos se separen', 3,
                          'La derecha se mueve en corcheas; la izquierda sostiene el acorde entero, dejando que el color siga sonando.')
    y -= 5
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(
             ['Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4', 'Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'A4', 'G4', 'A4'])]
    bass5 = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in [(EbM, 'Mib'), (Cm, 'Dom')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) La derecha vuela; la izquierda sostiene el color entero', grand_gap_mult=7.05, time_sig=TS)

    treb5b = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'C5', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un poco más alta', treb5b, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 6, 'Reto final · Bohemian Rhapsody casi entera', 3,
                          'Con la partitura al lado: antes de tocar cada acorde nuevo, deja que tu oído adivine su color.')
    y -= 5
    treb6 = [{'pitch': p, 'dur': 'q'} for p in
             ['D5', 'C5', 'Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'C5', 'D5', 'Eb5', 'D5', 'C5', 'Bb4', 'A4']]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(EbM, 'Mib'), (Cm, 'Dom'), (BbM, 'Sib'), (C7, 'Do7'), (FM, 'Fa'), (Gm, 'Solm'), (C7, 'Do7'), (BbM, 'Sib')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'El fragmento casi completo · ♩≈66, escuchando cada color', grand_gap_mult=7.05, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
