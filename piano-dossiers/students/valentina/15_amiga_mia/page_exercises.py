# -*- coding: utf-8 -*-
"""Taller de practica - Amiga Mia (Valentina, cancion 15, Re mayor,
   4/4, mismo archivo que Dilan). Nivel medio, un poco mas exigente:
   el bajo en anacrusa -- empezar antes del tiempo fuerte, no
   despues."""
from page_layout_common import *

SONG_KICKER = 'VALENTINA · NIVEL MEDIO · AMIGA MÍA (ALEJANDRO SANZ)'
TS = (4, 4)

RE = ['D3', 'F#3', 'A3']
LA = ['E2', 'A2', 'C#3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada lenta en Re mayor. Hoy: el bajo en anacrusa, empezar antes del tiempo fuerte.')
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

    y = exercise_heading(c, y, 2, 'El bajo en anacrusa: empezar antes del tiempo fuerte', 2,
                          'Lo de hoy. El acorde de la izquierda no cae justo en el "1": llega un poco antes, robando el último tiempo del compás anterior, como un impulso hacia el acorde siguiente.')
    y -= 12
    ev2a = [{'rest': True, 'dur': 'h.'}, {'pitches': RE, 'dur': 'q', 'label': 'Re (anacrusa)'},
            {'pitches': RE, 'dur': 'h.'}, {'pitches': LA, 'dur': 'q', 'label': 'La (anacrusa)'}]
    y = system_block(c, x0, w0, y, gap, 'a) Silencio, y el acorde llega justo antes del tiempo fuerte', ev2a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': RE, 'dur': 'h.'}, {'pitches': LA, 'dur': 'q', 'label': 'La (anacrusa)'},
            {'pitches': LA, 'dur': 'h.'}, {'pitches': SOL, 'dur': 'q', 'label': 'Sol (anacrusa)'}]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde llega, dura casi todo el compás, y ya viene el siguiente', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'F#4']]
    bass2c = [{'rest': True, 'dur': 'h.'}, {'pitches': RE, 'dur': 'q', 'label': 'Re (anacrusa)'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía ya suena mientras el bajo llega por sorpresa', grand_gap_mult=7.3, time_sig=TS)
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
    c.drawString(MARGIN, y, 'Ahora manos juntas: la anacrusa del bajo empuja la melodía hacia delante.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la melodía sobre el bajo anticipado', 2,
                          'La izquierda llega un poco antes del "1"; la derecha canta encima, sin perder el pulso.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'F#4', 'G4', 'E4']]
    bass1 = [{'rest': True, 'dur': 'h.'}, {'pitches': RE, 'dur': 'q', 'label': 'Re (anacrusa)'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El bajo llega antes; la melodía sigue su camino', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'F#4', 'G4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Independencia · la anacrusa no se contagia de la melodía', 3,
                          'La izquierda anticipa su entrada sin dudar; la derecha no cambia su ritmo por eso.')
    y -= 11
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'D4', 'A4', 'D4']]
    bass3 = [{'rest': True, 'dur': 'h.'}, {'pitches': LA, 'dur': 'q', 'label': 'La (anacrusa)'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El bajo de La llega antes de tiempo, sin dudar', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'A4', 'D4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, en otro orden', treb4, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Amiga Mía casi entera, con la anacrusa', 3,
                          'Con la partitura al lado: deja que el bajo empuje la frase hacia delante, sin frenarla.')
    y -= 11
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['A4', 'F#4', 'G4', 'E4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'D4', 'A4', 'D4']])
    bass5 = ([{'rest': True, 'dur': 'h.'}, {'pitches': RE, 'dur': 'q', 'label': 'Re'}] +
             [{'rest': True, 'dur': 'h.'}, {'pitches': LA, 'dur': 'q', 'label': 'La'}])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La balada casi completa · Lento ♩≈70, bajo anticipado', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
