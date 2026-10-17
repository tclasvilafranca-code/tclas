# -*- coding: utf-8 -*-
"""Taller de practica - Amiga Mia (Dilan, cancion 16, Re mayor, 4/4).
   Estructura DISTINTA otra vez: el foco es el PEDAL DE RESONANCIA -- la
   tecnica fisica de unir armonias con el pie derecho, algo que nunca se
   ha trabajado en un dosier anterior (todo se habia hecho solo con las
   manos hasta ahora)."""
from page_layout_common import *

SONG_KICKER = 'DILAN · MAYO · AMIGA MÍA (ALEJANDRO SANZ)'
TS = (4, 4)

RE = ['D3', 'F#3', 'A3']
LA = ['E2', 'A2', 'C#3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada lenta en Re mayor. El reto no son las manos: es el pie derecho.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('A4', 5), ('F#4', 3), ('G4', 4), ('E4', 2), ('F#4', 3), ('D4', 1)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Baja a saltos desde el La', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F#4', 3), ('D4', 1), ('A4', 5), ('D4', 1)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, desde el Fa#', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El pedal de resonancia: unir armonías con el pie', 2,
                          'Hasta ahora todo se ha hecho solo con las manos. Ahora entra el pie derecho: el pedal deja sonar las notas después de soltar los dedos, uniendo un acorde con el siguiente.')
    y -= 12
    ev2a = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in [(RE, 'Re'), (LA, 'La')] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Sin pedal: cada acorde se corta seco al soltar', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(RE, 'Re'), (LA, 'La')] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) Con pedal: pisa al tocar, suelta justo antes del siguiente acorde', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'F#4'] * 2]
    bass2c = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(RE, 'Re'), (LA, 'La')] * 2]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Las dos manos, con el pedal uniendo el sonido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes básicos de la balada.')
    y -= 11
    pattern_a = [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re')]
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La-Re, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Manos juntas con pedal, cambios de armonía, y la canción casi entera.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · melodía con pedal por debajo', 2,
                          'La izquierda suena larga gracias al pedal; la derecha canta encima, ligera.')
    y -= 11
    treb4 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('A4', 5), ('F#4', 3), ('G4', 4), ('E4', 2), ('F#4', 3), ('D4', 1), ('E4', 2), ('F#4', 3)]]
    bass4 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb4, bass4, 'a) La melodía sobre los acordes con pedal', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Cambiar el pedal justo a tiempo', 3,
                          'Cuando cambia el acorde de abajo, cambia el pedal: suelta y vuelve a pisar en el mismo instante en que tocas la nueva nota, no antes ni después.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'D4', 'A4', 'D4', 'G4', 'D4', 'A4', 'D4']]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(RE, 'Re'), (LA, 'La'), (SOL, 'Sol'), (LA, 'La')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'a) Un cambio de pedal por cada acorde nuevo', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Amiga Mía casi entera', 3,
                          'Con la partitura al lado: deja que el pedal haga el trabajo de unir, sin ensuciar el sonido con acordes mezclados.')
    y -= 11
    treb6 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('A4', 5), ('F#4', 3), ('G4', 4), ('E4', 2), ('F#4', 3), ('D4', 1), ('E4', 2), ('F#4', 3)]]
    treb6 += [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'D4', 'A4', 'D4', 'G4', 'D4', 'A4', 'D4']]
    bass6 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re'), (RE, 'Re'), (LA, 'La'), (SOL, 'Sol'), (LA, 'La')]]
    y = grand_staff_block(c, x0, w0, y, gap, treb6, bass6, 'La balada casi completa · Lento ♩≈70', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
