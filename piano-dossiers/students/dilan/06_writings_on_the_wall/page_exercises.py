# -*- coding: utf-8 -*-
"""Taller de practica - Writing's on the Wall (Dilan, cancion 6, Fa mayor, 4/4)
   Estructura DISTINTA a las 5 anteriores: aqui el foco no es un patron
   ritmico sino la EXPRESION -- matices de piano/forte y un toque cromatico.
   Los acordes I-IV-V se mueven a la pagina 2 para dejar sitio a esto."""
from page_layout_common import *

SONG_KICKER = 'DILAN · ENERO · WRITING’S ON THE WALL (SAM SMITH)'
TS = (4, 4)

FA = ['F3', 'A3', 'C4']
SIB = ['Bb2', 'D3']
DO = ['C3', 'E3', 'G3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de James Bond en Fa mayor. El reto aquí no es el ritmo: es la expresión.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Fa mayor', 1,
                          'Un dedo por tecla: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca la tecla negra Sib.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Baja desde Do, sintiendo el Sib', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('F4', 1), ('A4', 3), ('C5', 5), ('A4', 3)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Fa, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'Matices: la misma frase, piano y forte', 2,
                          'La dificultad real de esta canción no es técnica, es expresiva. Toca exactamente la misma frase tres veces, cambiando solo el volumen.')
    y -= 12
    frase = [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('F4', 1)]
    ev2a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in frase]
    y = system_block(c, x0, w0, y, gap, 'a) Piano (p) — suave, casi un susurro', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in frase]
    y = system_block(c, x0, w0, y, gap, 'b) Forte (f) — con peso, sin golpear', ev2b, clef='treble', time_sig=TS)

    ev2c = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in frase]
    y = system_block(c, x0, w0, y, gap, 'c) Con reguladores: empieza en p y termina en f, sin saltos bruscos', ev2c, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 3, 'El toque cromático: una nota fuera de la escala', 2,
                          'La canción se escapa un instante de Fa mayor con una nota cromática. Practícala despacio para que no te sorprenda.')
    y -= 12
    ev3a = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'C#5', 'D5', 'C#5'] * 3]
    y = system_block(c, x0, w0, y, gap, 'a) Do-Do#-Re-Do#, el paso cromático', ev3a, clef='treble', time_sig=TS)

    ev3b = [{'pitch': p, 'dur': 'q'} for p in ['F3', 'F#3', 'G3', 'F#3'] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El mismo paso, una octava abajo, en la izquierda', ev3b, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora los acordes de la tonalidad, y luego junta las manos con los matices ya aprendidos.')
    y -= 20
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Acordes I–IV–V en Fa mayor', 2,
                          'Fa–Sib–Do: los tres acordes que sostienen toda la balada.')
    y -= 11
    pattern_a = [(FA, 'Fa'), (DO, 'Do'), (SIB, 'Sib'), (DO, 'Do')] * 4
    eva = [{'pitches': p, 'dur': 'q', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Fa-Sib-Do-Fa, un acorde por tiempo', eva, clef='bass', time_sig=TS)

    pattern_b = []
    for chord, lab in [(FA, 'Fa'), (SIB, 'Sib'), (DO, 'Do'), (FA, 'Fa')]:
        pattern_b.append({'pitches': [chord[0]], 'dur': 'h', 'label': lab})
        pattern_b.append({'pitches': chord[1:], 'dur': 'h'})
    y = system_block(c, x0, w0, y, gap, 'b) Bajo y acorde en blancas, con calma', pattern_b, clef='bass', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 5, 'Manos juntas · la derecha canta fuerte, la izquierda acompaña suave', 3,
                          'Dos capas de volumen a la vez: la melodía en forte, el acompañamiento en piano, sin que se tapen.')
    y -= 11
    treb1 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('F4', 1)]]
    bass1 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in [(FA, 'Fa'), (FA, None), (SIB, 'Sib'), (SIB, None)]]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Melodía en forte sobre acompañamiento en piano', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in
             ['C5', 'Bb4', 'A4', 'G4', 'F4', 'G4', 'A4', 'Bb4', 'C5', 'Bb4', 'A4', 'F4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, memorizando dónde crece y dónde baja', treb2, clef='treble', time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 6, 'Reto final · Writing’s on the Wall casi entera', 3,
                          'Con la partitura al lado: cuida el volumen tanto como las notas. Una balada se toca con las orejas, no solo con los dedos.')
    y -= 11
    treb5 = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
             [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('F4', 1)]]
    treb5 += [{'pitch': p, 'dur': 'q'} for p in ['C5', 'C#5', 'D5', 'C#5', 'D5', 'C5', 'Bb4', 'A4']]
    bass5 = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
             [(FA, 'Fa'), (FA, None), (SIB, 'Sib'), (SIB, None), (DO, 'Do'), (DO, None), (FA, 'Fa'), (FA, None)]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La balada casi completa · Lento expresivo ♩≈68', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
