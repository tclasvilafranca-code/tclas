# -*- coding: utf-8 -*-
"""Taller de practica - A Sky Full of Stars (Dilan, cancion 4 de 5, Fa mayor, 4/4)
   Tema: el pulso "largo-corto" (negra con puntillo + corchea) firme y exacto,
   con las dos manos golpeando el mismo dibujo ritmico a la vez."""
from page_layout_common import *

SONG_KICKER = 'DILAN · OCTUBRE · A SKY FULL OF STARS (COLDPLAY)'
TS = (4, 4)

FA = ['F4', 'A4', 'C5']
SIB = ['Bb4', 'D5', 'F5']
DO = ['C5', 'E5', 'G5']
FA_B = ['F3', 'A3', 'C4']
SIB_B = ['Bb2', 'D3', 'F3']
DO_B = ['C3', 'E3', 'G3']


def _pulse_chords(chords_labels, octave_root=None):
    """Builds the 'long-short' pulse (dotted quarter + eighth) for a sequence of
       (pitches_or_pitch, label) pairs -- one pair of events per chord."""
    events = []
    for item, lab in chords_labels:
        if isinstance(item, list):
            events.append({'pitches': item, 'dur': 'q.', 'label': lab})
            events.append({'pitches': item, 'dur': 'e'})
        else:
            events.append({'pitch': item, 'dur': 'q.', 'label': lab})
            events.append({'pitch': item, 'dur': 'e'})
    return events


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un himno pop en Fa mayor, con el Sib. El reto: el pulso largo-corto firme en las dos manos.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca la tecla negra Sib.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('A4', 3), ('G4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja, sintiendo el Sib', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('C5', 5), ('A4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)

    ev1c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('F4', 2), ('G4', 2), ('G4', 3), ('A4', 3), ('A4', 4), ('Bb4', 4), ('Bb4', 5)]]
    y = system_block(c, x0, w0, y, gap, 'c) Repetida, cambiando de dedo', ev1c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El pulso largo-corto, firme y exacto', 2,
                          'La dificultad exacta de esta canción. Cuenta "larga-y-corta" muy despacio antes de tocarlo: la nota corta cae justo después del "y".')
    y -= 12
    ev2a = _pulse_chords([('F3', None)] * 8)
    y = system_block(c, x0, w0, y, gap, 'a) Sola la izquierda: el pulso largo-corto en Fa grave', ev2a, clef='bass', time_sig=TS)

    ev2b = _pulse_chords([('F4', None), ('A4', None)] * 4)
    y = system_block(c, x0, w0, y, gap, 'b) Sola la derecha: el mismo pulso, alternando notas', ev2b, clef='treble', time_sig=TS)

    ev2c = _pulse_chords([(FA, 'Fa'), (FA, None), (SIB, 'Sib'), (SIB, None)] * 2)
    y = system_block(c, x0, w0, y, gap, 'c) El acorde entero con el mismo pulso: Fa-Fa-Sib-Sib', ev2c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad, la base del estribillo.')
    y -= 12
    pattern_a = [(['F3', 'A3', 'C4'], 'Fa'), (['Bb2', 'D3', 'F3'], 'Sib'),
                 (['C3', 'E3', 'G3'], 'Do'), (['F3', 'A3', 'C4'], 'Fa')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = []
    for root, up, lab in [('F2', ['A3', 'C4'], 'Fa'), ('Bb2', ['D3', 'F3'], 'Sib'),
                            ('C3', ['E3', 'G3'], 'Do'), ('F2', ['A3', 'C4'], 'Fa')]:
        pattern_b.append({'pitch': root, 'dur': 'q', 'label': lab})
        pattern_b.append({'pitches': up, 'dur': 'q'})
        pattern_b.append({'pitches': up, 'dur': 'q'})
        pattern_b.append({'pitches': up, 'dur': 'q'})
    y = system_block(c, x0, w0, y, gap, 'b) Bajo-acorde-acorde-acorde, apoyado', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el mismo pulso largo-corto, golpeado a la vez por las dos.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el mismo pulso, a la vez', 2,
                          'Las dos manos golpean exactamente el mismo dibujo largo-corto, como un solo instrumento.')
    y -= 11
    chords4 = [(FA, 'Fa'), (FA, None), (SIB, 'Sib'), (SIB, None)] * 2
    roots4 = [(FA_B, 'Fa'), (FA_B, None), (SIB_B, 'Sib'), (SIB_B, None)] * 2
    treb1 = _pulse_chords(chords4)
    bass1 = _pulse_chords(roots4)
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Las dos manos golpean el mismo pulso, juntas de verdad', grand_gap_mult=7.3, time_sig=TS)

    chords4b = [(FA, 'Fa'), (FA, None), (SIB, 'Sib'), (SIB, None), (DO, 'Do'), (DO, None), (FA, 'Fa'), (FA, None)]
    treb2 = _pulse_chords(chords4b)
    y = system_block(c, x0, w0, y, gap, 'b) La progresión completa: Fa-Sib-Do-Fa', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Precisión rítmica · los acordes cambian más rápido', 3,
                          'El mismo pulso largo-corto, pero el acorde cambia en cada golpe: no dejes que se despiste.')
    y -= 11
    chords5 = [(FA, 'Fa'), (SIB, 'Sib'), (DO, 'Do'), (FA, 'Fa'), (SIB, 'Sib'), (DO, 'Do'), (FA, 'Fa'), (SIB, 'Sib')]
    roots5 = [(FA_B, 'Fa'), (SIB_B, 'Sib'), (DO_B, 'Do'), (FA_B, 'Fa'), (SIB_B, 'Sib'), (DO_B, 'Do'), (FA_B, 'Fa'), (SIB_B, 'Sib')]
    treb3 = _pulse_chords(chords5)
    bass3 = _pulse_chords(roots5)
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Los acordes cambian más rápido: el pulso no se despista', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['F4', 'A4', 'C5', 'A4', 'Bb4', 'D5', 'F5', 'D5'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: el mismo dibujo, en corcheas iguales', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · el estribillo casi entero', 3,
                          'Con la partitura al lado: el pulso largo-corto firme del principio al final, sin acelerar.')
    y -= 11
    chords6 = [(FA, 'Fa'), (FA, None), (SIB, 'Sib'), (SIB, None), (DO, 'Do'), (DO, None), (FA, 'Fa'), (FA, None),
               (SIB, 'Sib'), (SIB, None), (DO, 'Do'), (DO, None), (FA, 'Fa'), (FA, None), (SIB, 'Sib'), (SIB, None)]
    roots6 = [(FA_B, 'Fa'), (FA_B, None), (SIB_B, 'Sib'), (SIB_B, None), (DO_B, 'Do'), (DO_B, None), (FA_B, 'Fa'), (FA_B, None),
              (SIB_B, 'Sib'), (SIB_B, None), (DO_B, 'Do'), (DO_B, None), (FA_B, 'Fa'), (FA_B, None), (SIB_B, 'Sib'), (SIB_B, None)]
    treb5 = _pulse_chords(chords6)
    bass5 = _pulse_chords(roots6)
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El estribillo casi completo · Enérgico ♩≈100, pulso firme', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
