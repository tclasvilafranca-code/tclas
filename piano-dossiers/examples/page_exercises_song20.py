# -*- coding: utf-8 -*-
"""Taller de practica - Here We Go Round the Mulberry Bush (Cancion 20 de 20, Nivel 2, Do mayor, 6/8)
   Tema: el balanceo de 6/8 -- sentir DOS pulsos por compas, no seis golpes sueltos."""
from page_layout_common import *

SONG_KICKER = 'NIVEL 2 · AVANZO · HERE WE GO ROUND THE MULBERRY BUSH'
TS = (6, 8)


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Compás nuevo: 6/8. El reto es sentir DOS pulsos por compás («UN-dos-tres, DOS-dos-tres»), no seis golpes.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Do, balanceando', 1,
                          'Un dedo por tecla, sintiendo el balanceo de barco: dos grandes olas por compás.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
            ['C4', 'D4', 'E4', 'F4', 'G4', 'F4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'a) Sube y baja en grupos de tres, balanceando', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
            ['G4', 'F4', 'E4', 'D4', 'C4', 'D4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Bajando y subiendo, mismo balanceo', ev1b, clef='treble', time_sig=TS)

    ev1c = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
            ['C4', 'E4', 'G4', 'E4', 'C4', 'E4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'c) El acorde de Do, en grupos de tres', ev1c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El balanceo de 6/8: dos pulsos, no seis', 2,
                          'La dificultad exacta de esta canción (compases 1-4). Cuenta «UN-dos-tres, DOS-dos-tres» marcando el UN y el DOS.')
    y -= 12
    ev2a = [{'pitch': 'C4', 'dur': 'e', 'beam': 0},
            {'pitch': 'C4', 'dur': 'e', 'beam': 0}, {'pitch': 'C4', 'dur': 'e', 'beam': 0},
            {'pitch': 'G4', 'dur': 'e', 'beam': 1}, {'pitch': 'G4', 'dur': 'e', 'beam': 1}, {'pitch': 'G4', 'dur': 'e', 'beam': 1}] * 2
    y = system_block(c, x0, w0, y, gap, 'a) Do-Do-Do / Sol-Sol-Sol: siente los dos pulsos', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
            ['C4', 'D4', 'E4', 'F4', 'G4', 'A4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Escalera de seis notas, dos grupos de tres', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitch': 'G4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'e'},
            {'pitch': 'E4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'e'}] * 2
    y = system_block(c, x0, w0, y, gap, 'c) Negra-corchea: siente el balanceo largo-corto', ev2c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V, con el balanceo de 6/8', 2,
                          'Do–Fa–Sol–Do: un acorde por cada gran pulso, sintiendo el vaivén del barco.')
    y -= 12
    eva = []
    for chord, lab in [(['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa'),
                        (['G2', 'B2', 'D3'], 'Sol'), (['C3', 'E3', 'G3'], 'Do')]:
        eva.append({'pitches': chord, 'dur': 'q', 'label': lab})
        eva.append({'pitches': chord, 'dur': 'e'})
    y = system_block(c, x0, w0, y, gap, 'a) Un acorde por pulso, con su eco cortito', eva, clef='bass', time_sig=TS)

    evb = [{'pitches': p, 'dur': 'e'} for p in
           [['C3'], ['E3'], ['G3'], ['C3'], ['E3'], ['G3']] * 2]
    evb2 = [{'pitches': p['pitches'], 'dur': 'e', 'label': 'Do' if i == 0 else None} for i, p in enumerate(evb)]
    y = system_block(c, x0, w0, y, gap, 'b) Do arpegiado, en grupos de tres corcheas', evb2, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos con el balanceo del corro: dos grandes pulsos, como una barca.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el balanceo del corro', 2,
                          'La izquierda marca los dos pulsos grandes; la derecha canta la ronda infantil.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
             ['C4', 'D4', 'E4', 'F4', 'G4', 'F4'] * 2)]
    bass1 = []
    for chord, lab in [(['C3', 'E3', 'G3'], 'Do'), (['C3', 'E3', 'G3'], None),
                        (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do')]:
        bass1.append({'pitches': chord, 'dur': 'q', 'label': lab})
        bass1.append({'pitches': chord, 'dur': 'e'})
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La ronda completa, balanceando', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
             ['G4', 'A4', 'G4', 'F4', 'E4', 'D4'] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, para memorizarla cantando', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia rítmica · dos pulsos firmes', 3,
                          'La derecha se mueve en grupos de tres; la izquierda marca solo los dos grandes pulsos.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
             ['C4', 'E4', 'G4', 'E4', 'C4', 'E4'] * 2)]
    bass3 = []
    for i in range(4):
        bass3.append({'pitches': ['C3', 'E3', 'G3'], 'dur': 'q.', 'label': 'Do' if i == 0 else None})
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La izquierda marca solo el UN y el DOS', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': 'C4', 'dur': 'q'}, {'pitch': 'C4', 'dur': 'e'},
             {'pitch': 'E4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'e'}] * 2
    y = system_block(c, x0, w0, y, gap, 'b) Variación: negra-corchea en todo el compás', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · la ronda entera', 3,
                          'Con la partitura al lado: siente el balanceo de dos pulsos, no seis golpes sueltos.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(
             ['C4', 'D4', 'E4', 'F4', 'G4', 'F4'] * 2)]
    bass5 = []
    for chord, lab in [(['C3', 'E3', 'G3'], 'Do'), (['C3', 'E3', 'G3'], None),
                        (['F2', 'A2', 'C3'], 'Fa'), (['C3', 'E3', 'G3'], 'Do')]:
        bass5.append({'pitches': chord, 'dur': 'q', 'label': lab})
        bass5.append({'pitches': chord, 'dur': 'e'})
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La ronda completa · ♩.≈60, balanceado', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
