# -*- coding: utf-8 -*-
"""Taller de practica - When We Were Young (Eva, cancion 18, Re menor,
   4/4). Mismo arreglo que el de Dilan (que trabaja la teoria del bajo
   invertido), pero enfoque DISTINTO para Eva: el BAJO QUE CAMINA -- un
   ejercicio fisico de la mano izquierda, sintiendo los pasos del bajo
   bajo la mano en vez de analizarlos como teoria."""
from page_layout_common import *

SONG_KICKER = 'EVA · MAYO · WHEN WE WERE YOUNG (ADELE)'
TS = (4, 4)

DM = ['D3', 'F3', 'A3']
FM = ['F3', 'A3', 'C4']
BbM = ['Bb2', 'D3', 'F3']
GM = ['G2', 'Bb2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Adele, en Re menor. El reto: sentir los pasos del bajo caminando bajo la mano.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re menor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa(3) Sol(4) La(5). Todo teclas blancas, centro tonal en Re.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('F4', 3), ('E4', 2), ('A4', 5), ('G4', 4), ('F4', 3)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('F4', 3), ('A4', 5), ('F4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El bajo que camina, paso a paso', 2,
                          'La dificultad exacta de esta canción. El bajo baja escalón a escalón bajo el acorde — siente cada paso con el pulgar, sin dejar huecos.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D3', 'C3', 'Bb2', 'A2', 'G2', 'A2', 'Bb2', 'C3']]
    y = system_block(c, x0, w0, y, gap, 'a) El bajo solo, bajando y subiendo escalón a escalón', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'h'} for p in ['D3', 'C3', 'Bb2', 'A2']]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos pasos, más despacio, sintiendo cada uno', ev2b, clef='bass', time_sig=TS)

    ev2c = [{'pitch': p, 'dur': 'q'} for p in ['D3', 'C3', 'Bb2', 'A2', 'G2', 'F2', 'G2', 'A2']]
    y = system_block(c, x0, w0, y, gap, 'c) El bajo sigue caminando, un escalón más abajo', ev2c, clef='bass', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes de la canción en Re menor', 2,
                          'Rem–Fa–Sib–Sol: los acordes reales de la canción.')
    y -= 9
    pattern_a = [(DM, 'Rem'), (BbM, 'Sib'), (FM, 'Fa'), (GM, 'Sol')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Rem-Sib-Fa-Sol, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(DM, 'Rem'), (FM, 'Fa'), (BbM, 'Sib'), (GM, 'Sol')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas tranquilas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el bajo camina abajo mientras la melodía canta arriba.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el bajo camina bajo la melodía', 2,
                          'La izquierda camina paso a paso, sin prisa; la derecha canta la melodía encima, sin contagiarse del movimiento de abajo.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'G4', 'F4', 'E4']]
    bass1 = [{'pitch': p, 'dur': 'q'} for p in ['D3', 'C3', 'Bb2', 'A2', 'G2', 'A2', 'Bb2', 'C3']]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El bajo camina; la melodía sostiene notas largas', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F4', 'A4', 'F4', 'G4', 'A4', 'F4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando su forma', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el bajo no se detiene', 3,
                          'El bajo sigue caminando sin parar mientras la melodía se mueve más rápido encima.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['A4', 'G4', 'F4', 'E4'] * 4)]
    bass3 = [{'pitch': p, 'dur': 'q'} for p in ['D3', 'C3', 'Bb2', 'A2', 'G2', 'F2', 'G2', 'A2']]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El bajo sigue caminando; la melodía se mueve más rápido', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D4', 'F4', 'A4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la escala completa, tranquila', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · When We Were Young casi entera', 3,
                          'Con la partitura al lado: deja que el bajo camine sin parar de principio a fin, como un pulso que no se detiene.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'h'} for p in ['A4', 'G4', 'F4', 'E4', 'A4', 'G4', 'F4', 'D4']]
    bass5 = [{'pitch': p, 'dur': 'q'} for p in
             ['D3', 'C3', 'Bb2', 'A2', 'G2', 'A2', 'Bb2', 'C3', 'D3', 'C3', 'Bb2', 'A2', 'G2', 'F2', 'G2', 'A2']]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈68, con el bajo caminando', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
