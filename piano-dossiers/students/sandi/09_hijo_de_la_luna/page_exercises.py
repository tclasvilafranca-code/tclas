# -*- coding: utf-8 -*-
"""Taller de practica - Hijo de la Luna (Sandi, cancion 9, Mecano,
   arr. Unai Karam, Re menor -- armadura de 1 bemol, Sib, confirmada
   por render directo -- transportada desde el Mi menor original,
   6/8). Nivel avanzado: el silencio que abre el compas -- entrar
   tarde, sin prisa, cada vez."""
from page_layout_common import *

SONG_KICKER = 'SANDI · NIVEL AVANZADO · HIJO DE LA LUNA'
TS = (6, 8)

REm = ['D2', 'F2', 'A2']
DO = ['C2', 'E2', 'G2']
LA7 = ['A1', 'C#2', 'E2', 'G2']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Hijo de la Luna, de Mecano, en Re menor. Hoy: el silencio que abre el compás.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re menor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa(3) Sol(4) La(5). El Sib es la única alteración de esta tonalidad.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in
            enumerate(['D4', 'E4', 'F4', 'G4', 'A4', 'G4'])]
    y = system_block(c, x0, w0, y, gap, 'a) Recorrido por la posición, en corcheas', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'e'} for p in ['D4', 'F4', 'A4', 'F4', 'D4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re menor, arpegiado en corcheas', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El silencio que abre el compás: entrar tarde, sin prisa', 3,
                          'La dificultad de hoy. Cada grupo empieza con un silencio de corchea antes de las notas: hay que sentir ese silencio con la misma precisión que una nota, sin anticiparse ni tocar antes de tiempo.')
    y -= 9
    ev2a = [{'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
            {'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}]
    y = system_block(c, x0, w0, y, gap, 'a) Silencio-nota-nota, dos veces: siente el silencio antes de entrar', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'D5', 'dur': 'e'},
            {'rest': True, 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo patrón, un escalón más arriba', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
              {'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}]
    bass2c = [{'pitches': REm, 'dur': 'q.'}, {'pitches': REm, 'dur': 'q.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) El silencio inicial sobre el acorde de Re menor, sostenido', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes i–III–V7 en Re menor', 2,
                          'Rem–Do–La7: los acordes principales de esta tonalidad menor.')
    y -= 11
    pattern_a = [(REm, 'Rem'), (DO, 'Do'), (LA7, 'La7'), (REm, 'Rem')]
    eva = [{'pitches': p, 'dur': 'q.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Rem-Do-La7-Rem, un acorde por pulso de tres corcheas', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora manos juntas: el silencio inicial debe sentirse igual de firme que cualquier nota.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el silencio que abre, sobre el acorde de Do', 3,
                          'La izquierda sostiene el acorde de Do, tranquila; la derecha entra después del silencio, sin anticiparse.')
    y -= 7
    treb1 = [{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'},
             {'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'}]
    bass1 = [{'pitches': DO, 'dur': 'q.'}, {'pitches': DO, 'dur': 'q.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El silencio inicial sobre Do, sostenido', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e'} for p in ['E4', 'G4', 'E4', 'F4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'b) Sin el silencio: las mismas notas seguidas, para sentir la diferencia', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde de La7 no adelanta la entrada', 3,
                          'La izquierda toca La7 con firmeza; la derecha espera el silencio completo antes de entrar, sin dejarse arrastrar por el bajo.')
    y -= 7
    treb3 = [{'rest': True, 'dur': 'e'}, {'pitch': 'C#5', 'dur': 'e'}, {'pitch': 'E5', 'dur': 'e'},
             {'rest': True, 'dur': 'e'}, {'pitch': 'D5', 'dur': 'e'}, {'pitch': 'C#5', 'dur': 'e'}]
    bass3 = [{'pitches': LA7, 'dur': 'q.'}, {'pitches': LA7, 'dur': 'q.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El silencio inicial sobre La7; la entrada no se adelanta', grand_gap_mult=7.3, time_sig=TS)
    y -= 5

    treb4 = [{'pitch': p, 'dur': 'e'} for p in ['B4', 'C#5', 'E5', 'D5', 'C#5', 'B4']]
    y = system_block(c, x0, w0, y, gap, 'b) Contraste: la misma línea, sin el silencio inicial', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Hijo de la Luna casi entera', 3,
                          'Con la partitura al lado: siente cada silencio inicial con la misma firmeza que una nota, sin anticiparte nunca.')
    y -= 7
    treb5 = ([{'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
              {'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}] +
             [{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'},
              {'rest': True, 'dur': 'e'}, {'pitch': 'F4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'}])
    bass5 = [{'pitches': REm, 'dur': 'q.'}, {'pitches': REm, 'dur': 'q.'}, {'pitches': DO, 'dur': 'q.'}, {'pitches': DO, 'dur': 'q.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'Hijo de la Luna casi completa · silencio firme, entrada exacta', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
