# -*- coding: utf-8 -*-
"""Taller de practica - Poema de Amor (Eva, cancion 17, Sol menor, 4/4).
   Mismo arreglo que el de Dilan (que trabaja el recitado libre), pero
   enfoque DISTINTO para Eva: el CONTRASTE DE ARTICULACION -- frases
   ligadas y cantadas frente a frases marcadas y declamadas, dentro de
   la misma cancion."""
from page_layout_common import *

SONG_KICKER = 'EVA · MAYO · POEMA DE AMOR (JOAN MANUEL SERRAT)'
TS = (4, 4)

SOLm = ['G2', 'Bb2', 'D3']
RE7 = ['D3', 'F#3', 'C4']
FA = ['F2', 'A2', 'C3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción de Serrat en Sol menor. El reto: frases ligadas y cantadas frente a frases marcadas.')
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

    y = exercise_heading(c, y, 2, 'Ligado y marcado: dos formas de decir la misma frase', 2,
                          'La dificultad exacta de esta canción. Toca la misma frase de dos formas: una cantada y conectada, y otra marcada, casi hablada, con cada nota separada.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) Ligado: la frase cantada, sin cortar el sonido', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Marcado: la misma frase, cada nota separada y hablada', ev2b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes de Sol menor con el Re7 de verdad', 2,
                          'Solm–Fa–Re7: los acordes reales de la canción, con la séptima de dominante.')
    y -= 9
    pattern_a = [(SOLm, 'Solm'), (FA, 'Fa'), (RE7, 'Re7'), (SOLm, 'Solm')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Solm-Fa-Re7-Solm, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(SOLm, 'Solm'), (FA, 'Fa'), (RE7, 'Re7'), (SOLm, 'Solm')]]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, en blancas tranquilas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el contraste entre lo ligado y lo marcado, con acorde debajo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la frase ligada, cantada', 2,
                          'La izquierda sostiene el acorde con calma; la derecha canta ligado, sin ningún corte de sonido.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    bass1 = [{'pitches': p, 'dur': 'h'} for p in [SOLm, FA, SOLm, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Ligado, cantado, sin cortes', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase, marcada y separada', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'El contraste con acordes reales debajo', 3,
                          'Ahora el acorde real acompaña cada tipo de articulación — la izquierda no cambia, pero la derecha sí cambia de carácter.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4']]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [RE7, SOLm, RE7, SOLm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Marcado: cada nota separada, con acorde real debajo', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['G4', 'Bb4', 'A4', 'C5'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía en corcheas, ligada', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Poema de Amor casi entero', 3,
                          'Con la partitura al lado: alterna entre lo cantado y lo marcado, según lo que pida la letra.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'q'} for p in
             ['G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'A4', 'G4', 'A4', 'Bb4', 'C5', 'D5', 'C5', 'Bb4', 'G4']]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [SOLm, FA, RE7, SOLm, SOLm, FA, RE7, SOLm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Libre ♩≈66, con contraste', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
