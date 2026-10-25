# -*- coding: utf-8 -*-
"""Taller de practica - Nuovo Cinema Paradiso (Sandi, cancion 8,
   Ennio Morricone, arr. A.C. Escobes, Re menor -- armadura de 1
   bemol confirmada por render directo, compas mixto 4/4-2/4).
   Nivel avanzado: el cromatismo expresivo -- notas que colorean
   la melodia sin cambiar de tonalidad."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · NUOVO CINEMA PARADISO'
TS = (4, 4)

REm = ['D2', 'F2', 'A2']
SOLm = ['G2', 'Bb2', 'D3']
LA = ['A2', 'C#3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Nuovo Cinema Paradiso, de Ennio Morricone, en Re menor. Hoy: el cromatismo expresivo.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re menor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa(3) Sol(4) La(5). El Sib es la única alteración de la armadura.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('F4', 3), ('G4', 4), ('A4', 5), ('G4', 4), ('F4', 3), ('E4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido completo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'D5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El cromatismo expresivo: notas que colorean la melodía', 3,
                          'La dificultad de hoy. La melodía se adorna con notas cromáticas de paso (fuera de la tonalidad) que no cambian la armonía, solo la tiñen de color y tensión expresiva: hay que destacarlas sutilmente, no esconderlas ni acentuarlas de más.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'D5', 'F5']]
    y = system_block(c, x0, w0, y, gap, 'a) El Do# cromático que resuelve en Re: un color, no un cambio de tonalidad', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['F5', 'E5', 'D5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Sin el cromatismo: la misma línea, más plana, para comparar el efecto', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'D5', 'F5']]
    bass2c = [{'pitches': REm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El color cromático sobre el acorde de Re menor, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en Re menor', 2,
                          'Rem–Solm–La: los acordes principales de esta tonalidad menor.')
    y -= 11
    pattern_a = [(REm, 'Rem'), (SOLm, 'Solm'), (LA, 'La'), (REm, 'Rem')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Rem-Solm-La-Rem, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: destaca cada nota cromática con delicadeza, sin romper el fraseo cantabile.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el cromatismo sobre el acorde de Sol menor', 3,
                          'La izquierda sostiene el acorde de Sol menor, tranquila; la derecha canta la línea cromática encima, con fraseo cantabile.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F#4', 'G4', 'Bb4']]
    bass1 = [{'pitches': SOLm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El color cromático sobre Sol menor, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['Bb4', 'A4', 'G4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin cromatismo: para comparar el color perdido', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de La no se contagia del color cromático', 3,
                          'La izquierda sostiene el acorde de La sin moverse; la derecha destaca la nota cromática con delicadeza, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G#4', 'A4', 'C5']]
    bass3 = [{'pitches': LA, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El color cromático sobre La; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, bajando con fraseo cantabile', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Nuovo Cinema Paradiso casi entera', 3,
                          'Con la partitura al lado: destaca cada color cromático con delicadeza, dentro de un fraseo amplio y cantabile.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['D5', 'C#5', 'D5', 'F5']] +
             [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F#4', 'G4', 'Bb4']])
    bass5 = [{'pitches': REm, 'dur': 'w'}, {'pitches': SOLm, 'dur': 'w'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Nuovo Cinema Paradiso casi completa · cromatismo expresivo, con delicadeza', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
