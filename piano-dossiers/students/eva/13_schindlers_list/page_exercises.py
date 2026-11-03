# -*- coding: utf-8 -*-
"""Taller de practica - Theme from Schindler's List (Eva, cancion 13, Sol
   menor, 4/4). Mismo arreglo que el de Dilan (que trabaja el regulador
   dinamico), pero enfoque DISTINTO para Eva: el FRASEO LARGO -- tocar una
   frase entera como una sola respiracion, sin cortes ni pausas de aire."""
from page_layout_common import *

SONG_KICKER = "EVA · ABRIL · THEME FROM SCHINDLER'S LIST (JOHN WILLIAMS)"
TS = (4, 4)

SOLm = ['G2', 'Bb2', 'D3']
DOm = ['C3', 'Eb3', 'G3']
REm = ['D3', 'F3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'El tema de una banda sonora, en Sol menor. El reto: una frase entera en una sola respiración.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol menor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Sib(3) Do(4) Re(5). El dedo 3 toca la tecla negra Sib.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('Bb4', 3), ('A4', 2), ('C5', 4), ('D5', 5), ('C5', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición, sintiendo el Sib', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('Bb4', 3), ('D5', 5), ('Bb4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Una frase, una respiración', 2,
                          'La dificultad exacta de esta canción. Toca la frase entera de ocho compases sin ningún corte de sonido, como si no pudieras respirar hasta el final.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) Primera mitad de la frase, sin cortar el sonido', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Bb4', 'D5', 'C5', 'Bb4', 'A4', 'G4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Segunda mitad, continuando la misma respiración', ev2b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en Sol menor', 2,
                          'Solm–Dom–Rem: los acordes de esta tonalidad menor.')
    y -= 9
    pattern_a = [(SOLm, 'Solm'), (REm, 'Rem'), (DOm, 'Dom'), (REm, 'Rem')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Solm-Rem-Dom-Rem, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOLm, 'Solm'), (DOm, 'Dom'), (REm, 'Rem'), (SOLm, 'Solm')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas sostenidas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: deja que la frase entera respire sobre el acorde sostenido.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase larga sobre el acorde', 2,
                          'La izquierda sostiene el acorde sin cortarlo; la derecha canta la frase entera de un tirón, sin ninguna pausa de aire.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    bass1 = [{'pitches': p, 'dur': 'w'} for p in [SOLm, REm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase entera, sin ningún corte de sonido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Bb4', 'D5', 'C5', 'Bb4', 'A4', 'G4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando la respiración larga', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'La frase larga con acordes que cambian', 3,
                          'Ahora el acorde cambia dentro de la misma respiración — la izquierda avanza sin que la derecha corte el sonido.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [SOLm, REm, DOm, REm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde se mueve; la respiración de la melodía no se corta', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['G4', 'Bb4', 'A4', 'C5'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía en corcheas, más fluida', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · el tema casi entero', 3,
                          'Con la partitura al lado: toca la pieza entera pensando en una sola respiración larga, no en compases sueltos.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4', 'G4', 'Bb4', 'D5', 'C5', 'Bb4', 'A4', 'G4', 'G4']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [SOLm, REm, DOm, REm, SOLm, DOm, REm, SOLm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El tema casi completo · Adagio ♩≈60, una sola frase', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
