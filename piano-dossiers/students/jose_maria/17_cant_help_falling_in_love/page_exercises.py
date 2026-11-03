# -*- coding: utf-8 -*-
"""Taller de practica - Can't Help Falling in Love (Jose Maria,
   cancion 17, Re mayor, 3/4). Enfoque relajado: el volumen bajito
   que no se pierde -- tocar suave sin que el sonido se apague o
   desaparezca, distinto de los enfoques usados con Dilan (arpegio
   de vals), Eva (progresion armonica) y Josep/Nel (rubato)."""
from page_layout_common import *

SONG_KICKER = "JOSÉ MARÍA · ABRIL · CAN'T HELP FALLING IN LOVE (ELVIS PRESLEY)"
TS = (3, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['A2', 'C#3', 'E3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Una balada de Elvis Presley en Re mayor. Sin prisa: suave, sin que el sonido se pierda.')
    y -= 15
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5).')
    y -= 9
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('E4', 2), ('F#4', 3), ('E4', 2), ('D4', 1), ('E4', 2)]]
    y = system_block(c, x0, w0, y, gap, 'a) Un paseo tranquilo por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4'] * 4]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, nota a nota', ev1b, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 2, 'El volumen bajito que no se pierde', 2,
                          'Lo que vamos a cuidar en esta pieza. Tocar suave no es tocar sin fuerza — el sonido tiene que llegar igual de claro, aunque sea bajito, sin apagarse.')
    y -= 9
    ev2a = [{'pitch': p, 'dur': 'h.'} for p in ['F#4', 'E4', 'D4']]
    y = system_block(c, x0, w0, y, gap, 'a) Notas suaves, pero con el sonido bien presente', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4']]
    y = system_block(c, x0, w0, y, gap, 'b) La misma idea, un poco más movida: para comparar', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'h.'} for p in ['F#4', 'E4', 'D4']]
    bass2c = [{'pitches': RE, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) La melodía suave sobre el acorde de Re, sostenido entero', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes de esta tonalidad, sin prisa.')
    y -= 11
    pattern_a = [(RE, 'Re'), (SOL, 'Sol'), (LA, 'La'), (RE, 'Re')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La-Re, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos, sin prisa: el volumen se mantiene bajito, sin perderse.')
    y -= 15
    gap = 7.1
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el volumen suave sobre el acorde de Sol', 2,
                          'La izquierda sostiene el acorde entero, quieta y suave; la derecha canta bajito, sin que el sonido se pierda.')
    y -= 7
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'F#4', 'E4']]
    bass1 = [{'pitches': SOL, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) El volumen suave sobre Sol, sostenido entero', grand_gap_mult=7.3, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'F#4', 'E4', 'D4', 'E4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin prisa: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 5, 'Independencia · el acorde no se contagia del volumen', 3,
                          'La izquierda queda absolutamente quieta y suave con su acorde; la derecha canta bajito, sin que ninguna se apresure.')
    y -= 7
    treb3 = [{'pitch': p, 'dur': 'h.'} for p in ['A4', 'G4', 'F#4']]
    bass3 = [{'pitches': LA, 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) El volumen suave sobre La; el acorde no se mueve', grand_gap_mult=7.3, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F#4', 'E4', 'F#4', 'G4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la misma idea, un poco más arriba', treb4, clef='treble', time_sig=TS)
    y -= 3

    y = exercise_heading(c, y, 6, 'Para disfrutar · Can\'t Help Falling in Love casi entera', 3,
                          'Con la partitura al lado, sin ninguna prisa: deja que el sonido se mantenga suave, sin que se pierda ni se apague.')
    y -= 7
    treb5 = ([{'pitch': p, 'dur': 'h.'} for p in ['F#4', 'E4', 'D4']] +
             [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'F#4', 'E4']])
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [RE, RE, RE, SOL, SOL, SOL]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · piano, sin que el sonido se pierda', grand_gap_mult=7.3, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
