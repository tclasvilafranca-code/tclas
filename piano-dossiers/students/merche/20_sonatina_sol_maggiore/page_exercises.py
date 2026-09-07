# -*- coding: utf-8 -*-
"""Taller de practica - Sonatina N.2 (Merce, cancion 20, M.
   Bazzoni, Sol mayor -- armadura de 1 sostenido confirmada por
   el titulo "in sol maggiore - in G Major", 4/4, a 4 manos).
   Nivel basico pero solido: dos volumenes a la vez -- fuerte
   arriba, piano abajo, equilibrio de conjunto."""
from page_layout_common import *

SONG_KICKER = 'MERCÈ · NIVEL BÁSICO · SONATINA N.2 (A 4 MANOS)'
TS = (4, 4)

SOL = ['G2', 'B2', 'D3']
DO = ['C3', 'E3', 'G3']
RE = ['D2', 'F#2', 'A2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'La Sonatina N.2 de Bazzoni, en Sol mayor, a 4 manos. Hoy: dos volúmenes a la vez.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Sol mayor', 1,
                          'Un dedo por tecla: Sol(1) La(2) Si(3) Do(4) Re(5). El Fa# es la única alteración de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'D5', 'B4'] * 2]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Sol, arpegiado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'Dos volúmenes a la vez: fuerte arriba, piano abajo', 2,
                          'Lo que trabajamos hoy. En esta sonatina, el Pianoforte 1 toca fuerte mientras el Pianoforte 2 toca suave, al mismo tiempo: cada parte mantiene su propio volumen.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'G4', 'A4', 'B4', 'A4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'a) Tu parte, fuerte (forte): con energía y decisión', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitches': SOL, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': SOL, 'dur': 'q'}, {'rest': True, 'dur': 'q'}] * 2
    y = system_block(c, x0, w0, y, gap, 'b) La parte de acompañamiento, suave (piano): sin dejarse arrastrar por el volumen de arriba', ev2b, clef='bass', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'G4']]
    bass2c = [{'pitches': SOL, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': SOL, 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Fuerte arriba, suave abajo: los dos volúmenes a la vez', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Sol mayor', 2,
                          'Sol–Do–Re: los tres acordes de esta tonalidad.')
    y -= 11
    pattern_a = [(SOL, 'Sol'), (DO, 'Do'), (RE, 'Re'), (SOL, 'Sol')]
    eva = [{'pitches': p, 'dur': 'w', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Sol-Do-Re-Sol, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: mantén tu volumen propio sin dejarte llevar por el de la otra mano.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · fuerte arriba sobre el acompañamiento suave de Do', 2,
                          'La izquierda toca suave (piano) el acorde de Do, con silencios; la derecha canta fuerte (forte) encima.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'C5']]
    bass1 = [{'pitches': DO, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': DO, 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Fuerte arriba, suave sobre Do', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'C5']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · dos volúmenes que no se contagian', 3,
                          'La izquierda mantiene su volumen suave sobre Re; la derecha mantiene el suyo fuerte, sin arrastrar a la de abajo.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'q'} for p in ['D5', 'E5', 'F#5', 'D5']]
    bass3 = [{'pitches': RE, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': RE, 'dur': 'q'}, {'rest': True, 'dur': 'q'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Fuerte arriba, suave sobre Re; los dos volúmenes conviven', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#5', 'G5', 'A5', 'F#5']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto extra · Sonatina N.2 casi entera', 3,
                          'Con la partitura al lado: mantén tu volumen propio sin dejarte contagiar por el de la otra parte.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'G4']] +
             [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'C5']])
    bass5 = ([{'pitches': SOL, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': SOL, 'dur': 'q'}, {'rest': True, 'dur': 'q'}] +
             [{'pitches': DO, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitches': DO, 'dur': 'q'}, {'rest': True, 'dur': 'q'}])
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Sonatina N.2 casi completa · con los dos volúmenes a la vez', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
