# -*- coding: utf-8 -*-
"""Taller de practica - When We Were Young (Valentina, cancion 18,
   Re menor, 4/4, mismo archivo que Dilan). Nivel medio, un poco mas
   exigente: el acorde con novena -- un color mas denso, anadiendo
   una nota mas a la triada."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · WHEN WE WERE YOUNG (ADELE)'
TS = (4, 4)

DM = ['D3', 'F3', 'A3']
DM9 = ['D3', 'F3', 'A3', 'E4']
FM = ['F3', 'A3', 'C4']
BbM = ['Bb2', 'D3', 'F3']
GM = ['G2', 'Bb2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Adele, en Re menor. Hoy: el acorde con novena, un color más denso.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re menor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa(3) Sol(4) La(5). Sin alteraciones en la posición.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('F4', 3), ('G4', 4), ('F4', 3), ('E4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'F4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El acorde con novena: un color más denso', 2,
                          'Lo de hoy. Añade la novena (Mi) al acorde de Re menor: ya no es solo Rem, es Rem9, un color más denso y un poco melancólico.')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DM, 'Rem'), (DM, None)]]
    y = system_block(c, x0, w0, y, gap, 'a) Rem, la tríada simple: para comparar', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DM9, 'Rem9'), (DM9, None)]]
    y = system_block(c, x0, w0, y, gap, 'b) Rem9, con la novena añadida: escucha el color', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'A4']]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DM9, 'Rem9'), (FM, 'Fa')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) De Rem9 a Fa: el color denso se resuelve', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes de la canción en Re menor', 2,
                          'Rem–Fa–Sib–Fa: la progresión que sostiene la balada.')
    y -= 11
    pattern_a = [(DM, 'Rem'), (FM, 'Fa'), (BbM, 'Sib'), (FM, 'Fa')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Rem-Fa-Sib-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el color denso de la novena bajo la melodía.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el Rem9', 2,
                          'La izquierda sostiene el Rem9 entero; la derecha canta encima, dejando sonar el color.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'A4', 'F4']]
    bass1 = [{'pitches': DM9, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase sobre Rem9, tranquilo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'A4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · el color denso no se contagia', 3,
                          'La izquierda sostiene su Rem9 sin moverse; la derecha canta sin arrastrarla.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'E4']]
    bass3 = [{'pitches': DM9, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La frase sobre Rem9; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, subiendo', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · When We Were Young casi entera, con el Rem9', 3,
                          'Con la partitura al lado: deja sonar el color denso del Rem9 antes de resolver a Fa.')
    y -= 11
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'A4', 'F4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F4', 'E4']])
    bass5 = [{'pitches': DM9, 'dur': 'w'}, {'pitches': FM, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La balada casi completa · ♩≈68, con el color del Rem9', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
