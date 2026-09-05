# -*- coding: utf-8 -*-
"""Taller de practica - Theme from Schindler's List (Valentina,
   cancion 14, Sol menor, 4/4, mismo archivo que Dilan). Nivel medio,
   un poco mas exigente: la octava grave que sostiene todo el color
   -- un bajo profundo y resonante bajo la melodia."""
from page_layout_common import *

SONG_KICKER = "VALENTINA · NIVEL MEDIO · THEME FROM SCHINDLER'S LIST (JOHN WILLIAMS)"
TS = (4, 4)

SOLm = ['G2', 'Bb2', 'D3']
DOm = ['C3', 'Eb3', 'G3']
REm = ['D3', 'F3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de una banda sonora, en Sol menor. Hoy: la octava grave que sostiene el color.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Saltos amplios: precisión sin mirar el teclado', 1,
                          'Esta melodía salta lejos. Practica el salto solo: cae exactamente en la nota, sin tantear ni mirar.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'D5', 'G4', 'D5', 'G4', 'D5', 'G4', 'D5'] * 1 + ['G4', 'D5', 'G4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'a) Salto de 5ª: Sol-Re, ida y vuelta, cada vez más seguro', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Eb5', 'G4', 'Eb5', 'G4', 'Eb5', 'G4', 'Eb5', 'G4', 'Eb5', 'G4', 'Eb5']]
    y = system_block(c, x0, w0, y, gap, 'b) Salto de 6ª: Sol-Mib, todavía más lejos', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'La octava grave que sostiene todo el color', 2,
                          'Lo de hoy. La izquierda baja al registro más grave del piano y sostiene la octava entera: un color oscuro y resonante que sostiene toda la frase.')
    y -= 12
    ev2a = [{'pitch': 'G2', 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'a) Primero, solo la nota grave: siente lo hondo que suena', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': ['G2', 'G3'], 'dur': 'w'}]
    y = system_block(c, x0, w0, y, gap, 'b) Ahora la octava entera: el color se hace más rico', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'D5']]
    bass2c = [{'pitches': ['G2', 'G3'], 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase flota sobre la octava grave', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en Sol menor', 2,
                          'Solm–Rem–Dom: los acordes naturales de la tonalidad.')
    y -= 11
    pattern_a = [(SOLm, 'Solm'), (REm, 'Rem'), (DOm, 'Dom'), (SOLm, 'Solm')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Solm-Rem-Dom-Solm, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas, la octava grave bajo la melodía, y el tema casi entero.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase completa sobre la octava grave', 2,
                          'La izquierda sostiene la octava de Sol menor; la derecha canta la frase entera por encima.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'D5', 'D5', 'C5', 'Bb4', 'G4']]
    bass4 = [{'pitches': ['G2', 'G3'], 'dur': 'w'}, {'pitches': ['D2', 'D3'], 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La frase completa, con la octava grave debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'La octava que cambia de raíz', 3,
                          'Ahora la octava grave se mueve de nota, aunque siga sonando profunda: Sol, luego Do.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'A4', 'G4', 'A4', 'Bb4', 'D5']]
    bass5 = [{'pitches': ['D2', 'D3'], 'dur': 'w'}, {'pitches': ['C2', 'C3'], 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) La frase que baja y vuelve a subir', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, "Reto final · Theme from Schindler's List casi entero, con la octava grave", 3,
                          'Con la partitura al lado: deja que el color grave sostenga toda la frase, sin forzar.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'D5', 'D5', 'C5', 'Bb4', 'G4']]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'A4', 'G4', 'A4', 'Bb4', 'D5']]
    bass6 = [{'pitches': ['G2', 'G3'], 'dur': 'w'}, {'pitches': ['D2', 'D3'], 'dur': 'w'},
             {'pitches': ['C2', 'C3'], 'dur': 'w'}, {'pitches': ['G2', 'G3'], 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'El tema casi completo · Expresivo ♩≈66, hondo y resonante', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
