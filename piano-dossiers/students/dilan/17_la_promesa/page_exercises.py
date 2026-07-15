# -*- coding: utf-8 -*-
"""Taller de practica - La Promesa (Dilan, cancion 17, Sol mayor, 4/4).
   Estructura DISTINTA otra vez: la partitura real empieza siempre con un
   silencio y entra a contratiempo (anacrusa) -- el foco es aprender a
   ENTRAR DESPUES DEL SILENCIO con seguridad, sin adelantarse ni
   quedarse corto."""
from page_layout_common import *

SONG_KICKER = 'DILAN · MAYO · LA PROMESA (MELENDI)'
TS = (4, 4)

SOL = ['G3', 'B3', 'D4']
DO = ['C3', 'E3', 'G3']
RE = ['D3', 'F#3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Melendi en Sol mayor. Casi siempre entra después de un silencio, a contratiempo.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5). Todas teclas blancas.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D5', 5), ('B4', 3), ('C5', 4), ('A4', 2), ('B4', 3), ('G4', 1)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Baja a saltos desde el Re', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('B4', 3), ('G4', 1), ('D5', 5), ('G4', 1)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, desde el Si', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'La entrada a contratiempo: después del silencio', 2,
                          'La canción casi nunca empieza en el primer tiempo: hay un silencio y luego entra. Cuenta el silencio por dentro y entra justo en su sitio, sin dudar.')
    y -= 12
    cell = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['B4', 'A4', 'G4']] + [{'pitch': 'D5', 'dur': 'h'}])
    ev2a = cell * 2
    y = system_block(c, x0, w0, y, gap, 'a) Silencio, tres corcheas, y una nota larga', ev2a, clef='treble', time_sig=TS)

    cell_b = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['G4', 'A4', 'B4']] + [{'pitch': 'C5', 'dur': 'h'}])
    ev2b = cell_b * 2
    y = system_block(c, x0, w0, y, gap, 'b) El mismo dibujo, subiendo esta vez', ev2b, clef='treble', time_sig=TS)

    treb2c = cell * 2
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOL, 'Sol'), (DO, 'Do')] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Con la izquierda sosteniendo el acorde', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Re–Do–Sol: los acordes básicos de la tonalidad.')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (RE, 'Re'), (DO, 'Do'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Re-Do-Sol, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, la entrada a contratiempo con acordes que cambian, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · melodía sobre acordes', 2,
                          'La izquierda sostiene el acorde; la derecha entra después del silencio.')
    y -= 11
    cell = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['B4', 'A4', 'G4']] + [{'pitch': 'D5', 'dur': 'h'}])
    treb4 = cell * 2
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOL, 'Sol'), (RE, 'Re'), (DO, 'Do'), (SOL, 'Sol')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La entrada a contratiempo, con acordes', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'La entrada con acordes que cambian de verdad', 3,
                          'Ahora el acorde cambia CADA VEZ que entras, no siempre el mismo. Escucha el cambio antes de tocar.')
    y -= 11
    cell_b = ([{'rest': True, 'dur': 'e'}] + [{'pitch': p, 'dur': 'e'} for p in ['G4', 'A4', 'B4']] + [{'pitch': 'C5', 'dur': 'h'}])
    treb5 = cell_b * 2
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DO, 'Do'), (RE, 'Re'), (SOL, 'Sol'), (RE, 'Re')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) El acorde cambia en cada entrada', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · La Promesa casi entera', 3,
                          'Con la partitura al lado: cuenta el silencio por dentro y entra siempre con seguridad.')
    y -= 11
    treb6 = cell * 2
    treb6 += cell_b * 1
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(SOL, 'Sol'), (RE, 'Re'), (DO, 'Do'), (SOL, 'Sol'), (DO, 'Do'), (RE, 'Re')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · Lento ♩≈76', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
