# -*- coding: utf-8 -*-
"""Taller de practica - It's Beginning to Look a Lot Like Christmas (Eva,
   cancion 8, Piano Duet, Do mayor, 6/8). Mismo arreglo que el de Dilan (que
   trabaja el ritmo con enganche), pero enfoque DISTINTO para Eva: el
   ENSAMBLE -- empezar exactamente juntos y mantenerse sincronizados con
   otra persona sin mirarse todo el rato."""
from page_layout_common import *

SONG_KICKER = "EVA · DICIEMBRE · IT'S BEGINNING TO LOOK A LOT LIKE CHRISTMAS (A 4 MANOS)"
TS = (6, 8)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un dúo navideño en Do mayor y compás de 6/8. El reto: empezar juntos y mantenerse sincronizadas.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do mayor, en 6/8', 1,
                          'Un dedo por tecla: Do(1) Re(2) Mi(3) Fa(4) Sol(5). Siente el compás en dos grandes pulsos, no en seis pequeños.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'e'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4']] * 2
    y = system_block(c, x0, w0, y, gap, 'a) Corcheas suaves, sintiendo el vaivén de 6/8', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'e'} for p in ['C4', 'E4', 'G4', 'E4', 'C4', 'E4']] * 2
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Do, desgranado en el vaivén', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Empezar juntas: la respiración compartida', 2,
                          'La dificultad exacta de un dúo: antes de la primera nota, las dos tenéis que "respirar" el mismo tempo a la vez. Practica contando un compás entero en silencio antes de entrar.')
    y -= 9
    ev2a = ([{'rest': True, 'dur': 'e'}] * 6 + [{'pitch': p, 'dur': 'e'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4']])
    y = system_block(c, x0, w0, y, gap, 'a) Un compás de silencio contado por dentro, luego entra segura', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q.'} for p in ['C4', 'E4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Marca los dos grandes pulsos del compás, no los seis pequeños', ev2b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V, con el vaivén', 2,
                          'Do–Fa–Sol: los tres acordes, ahora en el ritmo de vaivén del 6/8.')
    y -= 9
    pattern_a = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in
                 [(FA, 'Fa'), (DO, 'Do'), (SOL, 'Sol'), (DO, 'Do')]]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Do-Sol-Do, un acorde por pulso grande', pattern_a, clef='bass', time_sig=TS)

    pattern_b = [{'pitch': p, 'dur': 'e', 'label': l} for p, l in
                 [('C2', 'Do'), ('E3', None), ('G3', None), ('F2', 'Fa'), ('A3', None), ('C4', None)]] * 2
    y = system_block(c, x0, w0, y, gap, 'b) Do y Fa, arpegiados en el vaivén', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el vaivén y la melodía sincronizados, como si tocaras con tu dúo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · las dos partes, en sincronía', 2,
                          'Imagina a tu compañera tocando la otra parte: mantén tu pulso firme, sin acelerar ni frenar, para que encajéis siempre.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4']] * 2
    bass1 = [{'pitches': p, 'dur': 'q.'} for p in [SOL, FA, DO, FA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La melodía y el acorde, en el mismo vaivén', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e'} for p in ['E4', 'F4', 'G4', 'A4', 'G4', 'F4']] * 2
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando el vaivén exacto', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'El silencio compartido antes de entrar', 3,
                          'Ahora practica la entrada con acorde real debajo: cuenta el compás vacío como si tu compañera ya estuviera tocando.')
    y -= 7
    treb3 = ([{'rest': True, 'dur': 'e'}] * 6 + [{'pitch': p, 'dur': 'e'} for p in ['C4', 'D4', 'E4', 'F4', 'G4', 'F4']])
    bass3 = [{'pitches': p, 'dur': 'q.'} for p in [DO, DO]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Silencio contado, luego entra segura con tu compañera', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e'} for p in ['C4', 'E4', 'G4', 'F4', 'A4', 'G4']] * 2
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la melodía un escalón más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · la ronda casi entera', 3,
                          'Con la partitura al lado: imagina el dúo completo y mantén tu parte firme de principio a fin.')
    y -= 7
    treb5 = [{'pitch': p, 'dur': 'e'} for p in
             ['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'F4', 'G4', 'A4', 'G4', 'F4']]
    bass5 = [{'pitches': p, 'dur': 'q.'} for p in [FA, SOL, DO, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La ronda casi completa · Vals ♩.≈60, con soltura', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
