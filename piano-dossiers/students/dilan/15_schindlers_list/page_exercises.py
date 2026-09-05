# -*- coding: utf-8 -*-
"""Taller de practica - Theme from Schindler's List (Dilan, cancion 15,
   Sol menor, 4/4). Estructura DISTINTA otra vez: el foco es el REGULADOR
   -- crecer y apagarse DENTRO de una misma frase continua, no un
   contraste entre dos frases (como en Writing's on the Wall) ni un
   fraseo escalonado en pasos (como en Merry Little Christmas)."""
from page_layout_common import *

SONG_KICKER = "DILAN · ABRIL · THEME FROM SCHINDLER'S LIST (JOHN WILLIAMS)"
TS = (4, 4)

SOLm = ['G2', 'Bb2', 'D3']
DOm = ['C3', 'Eb3', 'G3']
REm = ['D3', 'F3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de una banda sonora, en Sol menor. Expresivo — vive del regulador, no del volumen fijo.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Saltos amplios: precisión sin mirar el teclado', 1,
                          'Esta melodía salta lejos, como una voz que canta con el corazón. Practica el salto solo: cae exactamente en la nota, sin tantear ni mirar.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'D5', 'G4', 'D5', 'G4', 'D5', 'G4', 'D5'] * 1 + ['G4', 'D5', 'G4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'a) Salto de 5ª: Sol-Re, ida y vuelta, cada vez más seguro', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Eb5', 'G4', 'Eb5', 'G4', 'Eb5', 'G4', 'Eb5', 'G4', 'Eb5', 'G4', 'Eb5']]
    y = system_block(c, x0, w0, y, gap, 'b) Salto de 6ª: Sol-Mib, todavía más lejos', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El regulador: crecer y apagarse en UNA sola frase', 2,
                          'Aquí no hay dos frases distintas en volumen: es UNA frase que respira sola, creciendo hacia el medio y apagándose otra vez. Como cuando alguien habla con el corazón.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'D5']]
    y = system_block(c, x0, w0, y, gap, 'a) Sube: mp que va creciendo hasta mf', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Baja: mf que se va apagando a mp', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'D5', 'D5', 'C5', 'Bb4', 'G4']]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOLm, 'Solm'), (SOLm, None), (SOLm, None), (SOLm, None)]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La frase entera: un solo arco de sonido', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Manos juntas, el regulador con acordes que se mueven, y el tema casi entero.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase que respira', 2,
                          'La izquierda sostiene el acorde; la derecha crece y se apaga por encima.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'D5', 'D5', 'C5', 'Bb4', 'G4']]
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOLm, 'Solm'), (REm, 'Rem'), (DOm, 'Dom'), (SOLm, 'Solm')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La frase completa, con los acordes debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'El regulador con acordes que cambian', 3,
                          'Ahora el crecer y apagarse pasa mientras los acordes de abajo también se mueven — mucho más difícil de coordinar.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'A4', 'G4', 'A4', 'Bb4', 'D5']]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(REm, 'Rem'), (DOm, 'Dom'), (SOLm, 'Solm'), (REm, 'Rem')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) La frase que baja y vuelve a subir', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, "Reto final · Theme from Schindler's List casi entero", 3,
                          'Con la partitura al lado: deja que la frase crezca y se apague sola, sin forzar.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'D5', 'D5', 'C5', 'Bb4', 'G4']]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C5', 'Bb4', 'A4', 'G4', 'A4', 'Bb4', 'D5']]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(SOLm, 'Solm'), (REm, 'Rem'), (DOm, 'Dom'), (SOLm, 'Solm'), (REm, 'Rem'), (DOm, 'Dom'), (SOLm, 'Solm'), (REm, 'Rem')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'El tema casi completo · Expresivo ♩≈66', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
