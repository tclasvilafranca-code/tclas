# -*- coding: utf-8 -*-
"""Taller de practica - Santa Tell Me (Dilan, cancion 7, Mi menor, 4/4).
   Estructura DISTINTA otra vez: la partitura real tiene un pasaje donde la
   mano izquierda SALTA POR ENCIMA de la derecha (marcado "LH over / RH" en
   la partitura). Esa tecnica -- el cruce de manos -- nunca se ha trabajado
   en ningun dosier anterior, asi que es el foco entero de esta ficha."""
from page_layout_common import *

SONG_KICKER = 'DILAN · DICIEMBRE · SANTA TELL ME (ARIANA GRANDE)'
TS = (4, 4)

MIm = ['E3', 'G3', 'B3']
LAm = ['C3', 'E3', 'A3']
SIm = ['D3', 'F#3', 'B3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción navideña en Mi menor. Aquí el reto es un salto: cruzar una mano sobre la otra.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El dedo 2 toca la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sintiendo el Fa#', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('G4', 3), ('B4', 5), ('G4', 3)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Cruce de manos: la izquierda salta por encima', 2,
                          'En la partitura real pone "LH over RH": tu mano izquierda deja su sitio y salta por encima de la derecha para tocar notas agudas. La derecha no se mueve — solo la izquierda vuela.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E3', 'G3', 'B3', 'G3'] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Tu mano derecha se queda aquí, firme', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'B4', 'G4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Tu mano izquierda salta aquí arriba (aunque esté en clave de sol)', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['E5', 'D5', 'B4', 'G4'] * 2]
    bass2c = [{'pitch': p, 'dur': 'q'} for p in ['E3', 'G3', 'B3', 'G3'] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos juntas: la izquierda salta y vuelve sin chocar', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Manos juntas, el salto rápido, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · posición normal (sin cruce todavía)', 2,
                          'Antes de saltar, asegúrate de que cada mano sabe su sitio por separado.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2), ('E4', 1), ('G4', 3)]]
    bass1 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(MIm, 'Mim'), (LAm, 'Lam'), (SIm, 'Sim'), (MIm, 'Mim')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Melodía sobre acordes, cada mano en su sitio', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El salto rápido: corcheas que cruzan', 3,
                          'Ahora el cruce en corcheas, más ligero y rápido — como en la canción real.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['B4', 'D5', 'E5', 'D5'] * 4)]
    bass5 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['E3', 'G3', 'B3', 'G3'] * 4)]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) El salto en corcheas: izquierda arriba, derecha abajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Santa Tell Me casi entera', 3,
                          'Con la partitura al lado: mira bien cuándo pone "LH over" y deja que la izquierda salte con confianza.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('G4', 3), ('F#4', 2), ('E4', 1), ('G4', 3)]]
    treb6 += [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['B4', 'D5', 'E5', 'D5'] * 2)]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(MIm, 'Mim'), (LAm, 'Lam'), (SIm, 'Sim'), (MIm, 'Mim')]]
    bass6 += [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['E3', 'G3', 'B3', 'G3'] * 2)]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · ♩≈92', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
