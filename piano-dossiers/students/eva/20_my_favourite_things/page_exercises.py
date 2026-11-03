# -*- coding: utf-8 -*-
"""Taller de practica - My Favourite Things (Eva, cancion 20, Mi menor,
   3/4). Mismo arreglo que el de Dilan (que trabaja un METODO de subir la
   velocidad poco a poco), pero enfoque DISTINTO para Eva: el APOYO DEL
   VALS -- sentir un pequeno peso del brazo en el primer tiempo de cada
   compas y dejar los otros dos tiempos ligeros, casi flotando. Es una
   cuestion de tacto/fraseo, no de metodo de estudio ni de velocidad."""
from page_layout_common import *

SONG_KICKER = 'EVA · JUNIO · MY FAVOURITE THINGS (SOUND OF MUSIC)'
TS = (3, 4)

MIm = ['E3', 'G3', 'B3']
DO = ['C3', 'E3', 'G3']
LAm = ['C3', 'E3', 'A3']
RE = ['D3', 'F#3', 'A3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un vals de "Sonrisas y lágrimas", en Mi menor. El reto: el apoyo natural del vals.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El dedo 2 toca siempre la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('F#4', 2), ('G4', 3), ('A4', 4), ('B4', 5), ('A4', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('G4', 3), ('B4', 5), ('G4', 3)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El apoyo del vals: peso en el primer tiempo, ligereza en los otros dos', 2,
                          'La dificultad exacta de esta canción. Cada compás de vals se apoya con un pequeño peso del brazo en el primer tiempo, y los otros dos tiempos quedan ligeros, casi flotando — sin acentuarlos nunca.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in
            ['E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'E4', 'F#4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) La melodía, sintiendo el apoyo al empezar cada compás', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h.'} for p in ['E3', 'D3', 'E3', 'F#3']]
    y = system_block(c, x0, w0, y, gap, 'b) La izquierda: una nota larga por compás, sin estorbar el apoyo', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in
              ['E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'E4', 'F#4', 'G4', 'A4']]
    bass2c = [{'pitch': p, 'dur': 'h.'} for p in ['E3', 'D3', 'E3', 'F#3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, sintiendo el mismo apoyo juntas', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Los acordes reales de la canción, arpegiados', 2,
                          'Mim–Re–Lam–Do: los mismos cuatro acordes de la canción, esta vez desgranados nota a nota en vez de en bloque.')
    y -= 11
    pattern_a = [(MIm, 'Mim'), (RE, 'Re'), (LAm, 'Lam'), (DO, 'Do')]
    eva = [{'pitch': p[i], 'dur': 'q', 'label': (l if i == 0 else None)}
           for p, l in pattern_a for i in range(3)]
    y = system_block(c, x0, w0, y, gap, 'a) Los cuatro acordes, uno a uno en corcheas de tres', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el apoyo del vals se mueve con los acordes reales de la canción.')
    y -= 15
    gap = 7.05
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el apoyo se mueve con los acordes', 2,
                          'La melodía sigue apoyándose en el primer tiempo de cada compás; la izquierda cambia de acorde sin romper esa ligereza.')
    y -= 9
    treb4 = [{'pitch': p, 'dur': 'q'} for p in
             ['E4', 'G4', 'B4', 'A4', 'G4', 'F#4', 'E4', 'C4', 'A4', 'F#4', 'D4', 'D4']]
    bass4 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(MIm, 'Mim'), (RE, 'Re'), (LAm, 'Lam'), (DO, 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La melodía apoyada, con los acordes reales debajo', grand_gap_mult=7.05, time_sig=TS)

    treb4b = [{'pitch': p, 'dur': 'q'} for p in
              ['E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'E4', 'F#4', 'G4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando dónde cae el apoyo', treb4b, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 5, 'Independencia · el apoyo no se pierde aunque la melodía vuele', 3,
                          'La derecha se mueve en corcheas, más rápida; la izquierda mantiene su nota larga y su apoyo tranquilo, sin contagiarse.')
    y -= 5
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 6} for i, p in enumerate(
             ['E4', 'F#4', 'G4', 'A4', 'B4', 'A4'] * 2 + ['G4', 'F#4', 'E4', 'D4', 'E4', 'F#4'] * 2)]
    bass5 = [{'pitch': p, 'dur': 'h.'} for p in ['E3', 'D3', 'E3', 'F#3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) La melodía vuela; la izquierda no se altera', grand_gap_mult=7.05, time_sig=TS)

    treb5b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F#4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un poco más alta', treb5b, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 6, 'Reto final · My Favourite Things casi entera', 3,
                          'Con la partitura al lado: mantén siempre ese pequeño apoyo al empezar cada compás, sin que llegue nunca a sonar golpeado.')
    y -= 5
    treb6 = [{'pitch': p, 'dur': 'q'} for p in
             ['E4', 'F#4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'E4', 'F#4', 'G4', 'A4',
              'E4', 'G4', 'B4', 'A4', 'G4', 'F#4', 'E4', 'C4', 'A4', 'F#4', 'D4', 'D4']]
    bass6 = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in
             [(MIm, 'Mim'), (DO, 'Do'), (RE, 'Re'), (MIm, 'Mim'), (MIm, 'Mim'), (RE, 'Re'), (LAm, 'Lam'), (DO, 'Do')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La canción casi completa · ♩≈160, con el apoyo del vals', grand_gap_mult=7.05, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
