# -*- coding: utf-8 -*-
"""Taller de practica - La Promesa (Valentina, cancion 16, Sol mayor,
   4/4, mismo archivo que Dilan). Nivel medio, un poco mas exigente:
   el salto de octava en el bajo -- firme y limpio, sin tantear."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · LA PROMESA (MELENDI)'
TS = (4, 4)

SOL = ['G3', 'B3', 'D4']
DO = ['C3', 'E3', 'G3']
RE = ['D3', 'F#3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Melendi en Sol mayor. Hoy: el salto de octava en el bajo, firme y limpio.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5). Sin alteraciones en la posición, todo teclas blancas.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('B4', 3), ('A4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El salto de octava en el bajo: firme y limpio', 2,
                          'Lo de hoy. La izquierda salta de la nota grave a su octava, y vuelve, sin tantear ni mirar demasiado: el salto se aprende con la memoria de la mano.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G2', 'G3', 'G2', 'G3', 'G2', 'G3', 'G2', 'G3']]
    y = system_block(c, x0, w0, y, gap, 'a) Sol grave-Sol agudo, ida y vuelta', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D2', 'D3', 'C2', 'C3', 'D2', 'D3', 'G2', 'G3']]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora Re, Do y Sol: los tres saltos de la canción', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5']]
    bass2c = [{'pitch': p, 'dur': 'q'} for p in ['G2', 'G3', 'G2', 'G3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía arriba, el salto de octava abajo', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: el salto de octava firme abajo, la melodía tranquila arriba.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el salto de octava', 2,
                          'La izquierda salta Sol grave-agudo sin dudar; la derecha canta encima, tranquila.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'A4']]
    bass1 = [{'pitch': p, 'dur': 'q'} for p in ['G2', 'G3', 'G2', 'G3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El salto de Sol, con la melodía encima', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · el salto no se contagia de la melodía', 3,
                          'La izquierda salta Re grave-agudo con precisión; la derecha no la arrastra.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'F#4', 'D4', 'F#4']]
    bass3 = [{'pitch': p, 'dur': 'q'} for p in ['D2', 'D3', 'D2', 'D3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El salto de Re; la melodía no lo despista', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'D4', 'F#4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en otro orden', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · La Promesa casi entera, con el salto de octava', 3,
                          'Con la partitura al lado: deja que el salto de la izquierda sea firme y limpio, sin tantear.')
    y -= 11
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'C5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'A4']])
    bass5 = ([{'pitch': p, 'dur': 'q'} for p in ['G2', 'G3', 'D2', 'D3']] +
             [{'pitch': p, 'dur': 'q'} for p in ['C2', 'C3', 'G2', 'G3']])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Lento ♩≈76, salto firme y limpio', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
