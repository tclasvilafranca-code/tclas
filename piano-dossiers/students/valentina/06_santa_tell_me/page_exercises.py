# -*- coding: utf-8 -*-
"""Taller de practica - Santa Tell Me (Valentina, cancion 6, Mi menor,
   4/4, mismo archivo que Dilan). Nivel medio, un poco mas exigente:
   el staccato marcado -- notas cortas y precisas, sin usar el cruce
   de manos que ya trabajo Dilan."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · SANTA TELL ME (ARIANA GRANDE)'
TS = (4, 4)

MIm = ['E3', 'G3', 'B3']
LAm = ['C3', 'E3', 'A3']
SIm = ['D3', 'F#3', 'B3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción navideña en Mi menor. Hoy: el staccato, notas cortas y precisas.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El dedo 2 toca siempre la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sintiendo el Fa#', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'G4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El staccato marcado: notas cortas y precisas', 2,
                          'Lo de hoy. Cada nota suena breve, como si la tecla quemara: sube el dedo justo después de tocar, dejando aire entre nota y nota.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'G4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) La frase, corta y ligera: staccato', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['B4', 'A4', 'G4', 'F#4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) La frase que baja, igual de corta', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'G4']]
    bass2c = [{'pitches': MIm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El staccato sobre el acorde de Mim, sostenido debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en Mi menor', 2,
                          'Mim–Lam–Sim: los acordes naturales de la tonalidad.')
    y -= 11
    pattern_a = [(MIm, 'Mim'), (LAm, 'Lam'), (SIm, 'Sim'), (MIm, 'Mim')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mim-Lam-Sim-Mim, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el staccato arriba, el acorde sostenido debajo.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el staccato sobre el acorde de Lam', 2,
                          'La izquierda sostiene el acorde de Lam; la derecha toca corto y preciso encima.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'A4', 'E4', 'A4']]
    bass1 = [{'pitches': LAm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Staccato sobre Lam, sostenido debajo', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'A4', 'E4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del staccato', 3,
                          'La izquierda sostiene su acorde de Sim sin moverse; la derecha toca corto sin arrastrarla.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'B4', 'F#4']]
    bass3 = [{'pitches': SIm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Staccato sobre Sim; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'B4', 'F#4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Santa Tell Me casi entera, en staccato', 3,
                          'Con la partitura al lado: cada nota corta y precisa, sin perder el pulso.')
    y -= 11
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'B4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['C5', 'A4', 'E4', 'A4']])
    bass5 = [{'pitches': MIm, 'dur': 'w'}, {'pitches': LAm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈92, staccato firme', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
