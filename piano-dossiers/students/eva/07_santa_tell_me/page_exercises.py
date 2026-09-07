# -*- coding: utf-8 -*-
"""Taller de practica - Santa Tell Me (Eva, cancion 7, Mi menor, 4/4).
   Mismo arreglo que el de Dilan (que trabaja el cruce de manos), pero
   enfoque DISTINTO para Eva: la SINCOPA pop -- notas que llegan un
   poquito antes de lo que el oido espera, el sello del genero."""
from page_layout_common import *

SONG_KICKER = 'EVA · DICIEMBRE · SANTA TELL ME (ARIANA GRANDE)'
TS = (4, 4)

MIm = ['E3', 'G3', 'B3']
LAm = ['A2', 'C3', 'E3']
SIm = ['B2', 'D3', 'F#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una canción navideña en Mi menor. El reto: la síncopa pop, notas que llegan antes de lo esperado.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Mi menor', 1,
                          'Un dedo por tecla: Mi(1) Fa#(2) Sol(3) La(4) Si(5). El dedo 2 toca la tecla negra Fa#.')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('G4', 3), ('F#4', 2), ('A4', 4), ('B4', 5), ('A4', 4)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición, sintiendo el Fa#', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('E4', 1), ('G4', 3), ('B4', 5), ('G4', 3)] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Mi menor, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'La síncopa: la nota que llega antes de tiempo', 2,
                          'La dificultad exacta de esta canción. En vez de caer justo en el tiempo, la nota entra un poquito antes — como si "se adelantara" al pulso.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'E4', 'G4', 'G4', 'B4', 'B4', 'A4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) Primero sin síncopa: todo justo en el tiempo', ev2a, clef='treble', time_sig=TS)

    ev2b = ([{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'q.'}] * 4)
    y = system_block(c, x0, w0, y, gap, 'b) Ahora con síncopa: silencio corto, luego la nota se adelanta', ev2b, clef='treble', time_sig=TS)

    ev2c = ([{'rest': True, 'dur': 'e'}, {'pitch': p, 'dur': 'q.'}] for p in [])
    ev2c = [{'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'q.'}, {'rest': True, 'dur': 'e'}, {'pitch': 'B4', 'dur': 'q.'},
            {'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'q.'}, {'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'q.'}]
    y = system_block(c, x0, w0, y, gap, 'c) La melodía real, sincopada de principio a fin', ev2c, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 3, 'Acordes i–iv–v en Mi menor', 2,
                          'Mim–Lam–Sim: los acordes naturales de la tonalidad.')
    y -= 9
    pattern_a = [(MIm, 'Mim'), (SIm, 'Sim'), (LAm, 'Lam'), (SIm, 'Sim')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Mim-Sim-Lam-Sim, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = [{'pitches': p, 'dur': 'e', 'beam': i // 2, 'label': l} for i, (p, l) in enumerate(
        [(MIm, 'Mim'), (MIm, None), (LAm, 'Lam'), (LAm, None), (SIm, 'Sim'), (SIm, None), (MIm, 'Mim'), (MIm, None)] * 2)]
    y = system_block(c, x0, w0, y, gap, 'b) Los mismos acordes, repetidos en corcheas', pattern_b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el acorde marca el pulso mientras la melodía se adelanta.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · la síncopa sobre el acorde firme', 2,
                          'La izquierda marca el pulso exacto, sin sincopar; la derecha se adelanta un poquito, como pide el estilo pop.')
    y -= 7
    treb1 = [{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'q.'}, {'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'q.'},
             {'rest': True, 'dur': 'e'}, {'pitch': 'B4', 'dur': 'q.'}, {'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'q.'}]
    bass1 = [{'pitches': p, 'dur': 'q'} for p in [MIm, MIm, MIm, MIm, LAm, LAm, LAm, LAm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El pulso firme abajo, la síncopa arriba', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['E4', 'G4', 'B4', 'A4'] * 4)]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sintiendo el adelanto', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia rítmica · dos pulsos distintos a la vez', 3,
                          'La izquierda no se contagia de la síncopa de la derecha: cada mano mantiene su propio dibujo rítmico.')
    y -= 7
    treb3 = [{'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'q.'}, {'rest': True, 'dur': 'e'}, {'pitch': 'B4', 'dur': 'q.'}]
    bass3 = [{'pitches': p, 'dur': 'h'} for p in [SIm, MIm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El acorde no se mueve; la melodía se adelanta sola', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'G4', 'F#4', 'A4', 'B4', 'A4', 'G4', 'F#4', 'E4', 'G4', 'B4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma frase, sin síncopa, para comparar', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Reto final · Santa Tell Me casi entera', 3,
                          'Con la partitura al lado: deja que la izquierda marque el pulso mientras la derecha se adelanta con soltura.')
    y -= 7
    treb5 = [{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'q.'}, {'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'q.'},
             {'rest': True, 'dur': 'e'}, {'pitch': 'B4', 'dur': 'q.'}, {'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'q.'},
             {'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'q.'}, {'rest': True, 'dur': 'e'}, {'pitch': 'F#4', 'dur': 'q.'}]
    bass5 = [{'pitches': p, 'dur': 'h'} for p in [MIm, LAm, SIm, MIm, LAm, MIm]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · Pop ♩≈100, con soltura', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
