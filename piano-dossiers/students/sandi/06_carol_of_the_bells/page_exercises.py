# -*- coding: utf-8 -*-
"""Taller de practica - Carol of the Bells (Sandi, cancion 6, M.
   Leontovych, arr. Jim Paterson, Sol menor -- armadura de 2
   bemoles, Sib y Mib, confirmada por render directo, 3/4). Nivel
   avanzado: el ostinato en la melodia -- la campana que repite,
   la armonia que cambia debajo."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · CAROL OF THE BELLS'
TS = (3, 4)

SOLm = ['G2', 'Bb2', 'D3']
DOm = ['C2', 'Eb2', 'G2']
RE = ['D2', 'F#2', 'A2']
MIb = ['Eb2', 'G2', 'Bb2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Carol of the Bells, de Leontovych, en Sol menor. Hoy: el ostinato de campana en la melodía.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol menor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Sib(3) Do(4) Re(5). El Sib y el Mib son las alteraciones de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('Bb4', 3), ('C5', 4), ('D5', 5), ('C5', 4)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'Bb4', 'D5'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol menor, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El ostinato en la melodía: la campana que repite', 3,
                          'La dificultad de hoy. La derecha repite el mismo motivo de cuatro notas, como una campana, mientras la izquierda cambia de acorde debajo: el ostinato está arriba esta vez, no abajo.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['B4', 'C5', 'D5', 'C5'] * 3)]
    y = system_block(c, x0, w0, y, gap, 'a) El motivo de campana, repetido tres veces exactas', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(SOLm, 'Solm'), (DOm, 'Dom'), (RE, 'Re')]]
    y = system_block(c, x0, w0, y, gap, 'b) La armonía que cambia debajo: Solm-Dom-Re, un acorde por compás', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['B4', 'C5', 'D5', 'C5'] * 3)]
    bass2c = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in [(SOLm, 'Solm'), (DOm, 'Dom')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La campana arriba, la armonía cambiando debajo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–iv–V en Sol menor', 2,
                          'Solm–Dom–Re: el Re mayor lleva el Fa# sensible, la nota que "tira" hacia el Sol.')
    y -= 11
    pattern_a = [(SOLm, 'Solm'), (DOm, 'Dom'), (RE, 'Re'), (SOLm, 'Solm')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Solm-Dom-Re-Solm, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: la campana no varía nunca, aunque la armonía cambie constantemente debajo.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la campana sobre el acorde de Do menor', 3,
                          'La izquierda sostiene el acorde de Do menor; la derecha repite el motivo de campana exactamente igual que sobre Sol menor.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['Eb5', 'F5', 'G5', 'F5'] * 3)]
    bass1 = [{'pitches': DOm, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La campana sobre Do menor, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['Eb5', 'F5', 'G5', 'F5'] * 3)]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la campana: para comprobar que no varía', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el Re mayor con Fa# no descoloca la campana', 3,
                          'La izquierda toca el acorde de Re mayor con su sensible Fa#; la derecha sigue repitiendo el mismo motivo, sin alterarse por el cambio armónico.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['F#5', 'G5', 'A5', 'G5'] * 3)]
    bass3 = [{'pitches': RE, 'dur': 'h.'}] * 2
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) La campana sobre Re mayor; la sensible Fa# no la distrae', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#5', 'G5', 'A5']]
    y = system_block(c, x0, w0, y, gap, 'b) Contraste: la misma línea, sin ostinato, en negras', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Carol of the Bells casi entera', 3,
                          'Con la partitura al lado: la campana debe sonar exactamente igual en cada compás, sin importar qué acorde suene debajo.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['B4', 'C5', 'D5', 'C5'] * 3)] +
             [{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['Eb5', 'F5', 'G5', 'F5'] * 3)])
    bass5 = [{'pitches': SOLm, 'dur': 'h.'}, {'pitches': SOLm, 'dur': 'h.'}, {'pitches': DOm, 'dur': 'h.'}, {'pitches': DOm, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Carol of the Bells casi completa · la campana inmutable', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
