# -*- coding: utf-8 -*-
"""Taller de practica - A Sky Full of Stars (Valentina, cancion 3, Fa
   mayor, 4/4, mismo archivo que Dilan). Nivel medio, un poco mas
   exigente: el acento en el contratiempo -- la energia que no cae
   donde se espera."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · A SKY FULL OF STARS (COLDPLAY)'
TS = (4, 4)

FA = ['F4', 'A4']
SIB = ['Bb4', 'D5', 'F5']
DO = ['C5', 'E5', 'G5']
FA_B = ['F3', 'A3', 'C4']
SIB_B = ['Bb2', 'D3']
DO_B = ['C3', 'E3', 'G3']


def _offbeat_chords(chords_labels):
    """Silencio-corchea, luego nota-corchea y nota-negra: el acento cae
       en el 'y' del tiempo, no en el tiempo mismo."""
    events = []
    for item, lab in chords_labels:
        events.append({'rest': True, 'dur': 'e'})
        if isinstance(item, list):
            events.append({'pitches': item, 'dur': 'e', 'label': lab})
            events.append({'pitches': item, 'dur': 'q'})
        else:
            events.append({'pitch': item, 'dur': 'e', 'label': lab})
            events.append({'pitch': item, 'dur': 'q'})
    return events


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un himno pop en Fa mayor. Hoy: el acento en el contratiempo, la energía que llega tarde.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Calentamiento rítmico: siente el silencio antes de entrar', 1,
                          'Cuenta "1-y-2" en voz alta: el silencio ocupa el "1", la nota entra justo en el "y".')
    y -= 12
    ev1a = [{'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'q'}] * 4
    y = system_block(c, x0, w0, y, gap, 'a) Silencio-nota-nota, muy regular', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': 'F4', 'dur': 'q'}] * 8
    y = system_block(c, x0, w0, y, gap, 'b) Comparación: lo mismo, pero sin contratiempo', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El acento en el contratiempo: la energía que no cae donde se espera', 2,
                          'Lo de hoy. La nota no entra en el tiempo fuerte, sino justo después: eso le da su empuje.')
    y -= 12
    ev2a = _offbeat_chords([('F3', None)] * 4)
    y = system_block(c, x0, w0, y, gap, 'a) Sola la izquierda: el contratiempo en Fa grave', ev2a, clef='bass', time_sig=TS)

    ev2b = _offbeat_chords([('F4', None), ('A4', None)] * 2)
    y = system_block(c, x0, w0, y, gap, 'b) Sola la derecha: el mismo contratiempo, alternando', ev2b, clef='treble', time_sig=TS)

    ev2c = _offbeat_chords([(FA, 'Fa'), (SIB, 'Sib')] * 2)
    y = system_block(c, x0, w0, y, gap, 'c) El acorde entero en contratiempo: Fa-Sib', ev2c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes de esta tonalidad, la base del estribillo.')
    y -= 12
    pattern_a = [(FA_B, 'Fa'), (SIB_B, 'Sib'), (DO_B, 'Do'), (FA_B, 'Fa')] * 2
    eva = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, dos por compás', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el contratiempo cae igual en las dos a la vez.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el contratiempo, a la vez', 2,
                          'Las dos manos entran justo después del tiempo fuerte, exactamente juntas.')
    y -= 11
    treb1 = _offbeat_chords([(FA, 'Fa'), (SIB, 'Sib')])
    bass1 = _offbeat_chords([(FA_B, 'Fa'), (SIB_B, 'Sib')])
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Las dos manos entran tarde, juntas de verdad', grand_gap_mult=7.3, time_sig=TS)

    treb2 = _offbeat_chords([(FA, 'Fa'), (SIB, 'Sib'), (DO, 'Do'), (FA, 'Fa')])
    y = system_block(c, x0, w0, y, gap, 'b) La progresión completa, en contratiempo: Fa-Sib-Do-Fa', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Precisión rítmica · el contratiempo con cambios rápidos', 3,
                          'El mismo contratiempo, pero el acorde cambia cada vez: no dejes que se despiste.')
    y -= 11
    treb3 = _offbeat_chords([(FA, 'Fa'), (SIB, 'Sib')])
    bass3 = _offbeat_chords([(FA_B, 'Fa'), (SIB_B, 'Sib')])
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Los acordes cambian rápido: el contratiempo no se pierde', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(
             ['F4', 'A4', 'Bb4', 'C5', 'A4', 'D5', 'F5', 'D5'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: el mismo dibujo, en corcheas iguales', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · el estribillo casi entero, en contratiempo', 3,
                          'Con la partitura al lado: mantén la energía en el "y" del tiempo, del principio al final.')
    y -= 11
    treb5 = _offbeat_chords([(FA, 'Fa'), (SIB, 'Sib'), (DO, 'Do'), (FA, 'Fa')])
    bass5 = _offbeat_chords([(FA_B, 'Fa'), (SIB_B, 'Sib'), (DO_B, 'Do'), (FA_B, 'Fa')])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'El estribillo casi completo · Enérgico ♩≈100, contratiempo firme', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
