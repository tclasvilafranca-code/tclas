# -*- coding: utf-8 -*-
"""Taller de practica - Can't Help Falling in Love (Josep, cancion 1,
   Re mayor, 3/4). Angulo propio para Josep (45 anos, con experiencia):
   el RUBATO CON CRITERIO -- estirar levemente el final de cada frase
   y volver al pulso, sin que se note el "enganche". Distinto del
   vals-arpegio de Dilan y de la lectura armonica de Eva."""
from page_layout_common import *

SONG_KICKER = 'JOSEP · SEPTIEMBRE · CAN\'T HELP FALLING IN LOVE'
TS = (3, 4)

RE = ['D3', 'F#3', 'A3']
SOL = ['G2', 'B2', 'D3']
LA = ['E2', 'A2', 'C#3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un vals lento en Re mayor. El reto: un rubato con criterio, no un descontrol del tempo.')
    y -= 20
    gap = 7.6
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 1, 'Posición de 5 dedos en Re mayor', 1,
                          'Un dedo por tecla: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El dedo 3 toca siempre la tecla negra Fa#.')
    y -= 12
    ev1a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('F#4', 3), ('E4', 2), ('G4', 4), ('F#4', 3), ('E4', 2)] * 2]
    y = system_block(c, x0, w0, y, gap, 'a) Saltos por la posición', ev1a, clef='treble', time_sig=TS)

    ev1b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('D4', 1), ('A4', 5), ('F#4', 3), ('A4', 5)] * 3]
    y = system_block(c, x0, w0, y, gap, 'b) El acorde de Re, desgranado', ev1b, clef='treble', time_sig=TS)
    y -= 6

    y = exercise_heading(c, y, 2, 'El rubato con criterio: estirar y volver, sin que se note', 2,
                          'La dificultad exacta de esta canción. No es tocar irregular: es alargar un poquito el final de cada frase — como una pequeña respiración — y volver enseguida al pulso de siempre.')
    y -= 12
    ev2a = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4', 'D4', 'F#4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'a) Tempo giusto: la frase entera, sin estirar nada todavía', ev2a, clef='treble', time_sig=TS)

    ev2b = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4']] + [{'pitch': 'D4', 'dur': 'h.'}]
    y = system_block(c, x0, w0, y, gap, 'b) La misma frase: ahora la última nota se estira un compás entero', ev2b, clef='treble', time_sig=TS)

    treb2c = [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F#4', 'E4', 'D4', 'F#4']] + [{'pitch': 'A4', 'dur': 'h.'}]
    bass2c = [{'pitches': p, 'dur': 'q'} for p in [RE, RE, RE, SOL, SOL, SOL, LA, LA, LA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb2c, bass2c, 'c) Otra frase con el mismo gesto: estira y vuelve', grand_gap_mult=7.3, time_sig=TS)
    y -= 4

    y = exercise_heading(c, y, 3, 'Acordes I–IV–V en Re mayor', 2,
                          'Re–Sol–La: los tres acordes de esta tonalidad, el terreno sobre el que se apoya el rubato.')
    y -= 11
    pattern_a = [(RE, 'Re'), (RE, None), (SOL, 'Sol'), (SOL, None), (LA, 'La'), (LA, None)]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'a) Re-Sol-La, un acorde por compás entero', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Ahora junta las manos: el rubato se siente con las dos, no solo con la melodía.')
    y -= 15
    gap = 7.05
    x0, w0 = MARGIN, CONTENT_W

    y = exercise_heading(c, y, 4, 'Manos juntas · el rubato con las dos manos', 2,
                          'Cuando la melodía estira su última nota, la izquierda también se relaja un instante — el rubato es de las dos manos juntas, no solo de la derecha.')
    y -= 9
    treb1 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4']] + [{'pitch': 'D4', 'dur': 'h.'}]
    bass1 = [{'pitches': p, 'dur': 'q'} for p in [RE, RE, RE, SOL, SOL, SOL]] + [{'pitches': RE, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) La frase entera, estirando juntas al final', grand_gap_mult=7.05, time_sig=TS)

    treb2 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'F#4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'E4', 'F#4']]
    y = system_block(c, x0, w0, y, gap, 'b) Solo la melodía, sin estirar: para comparar', treb2, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 5, 'Independencia · el pulso de fondo no se pierde nunca', 3,
                          'Aunque la melodía respire y se estire, cuenta el pulso por dentro sin parar — así el rubato suena con criterio y no como un despiste.')
    y -= 5
    treb3 = [{'pitch': p, 'dur': 'e', 'beam': i // 2} for i, p in enumerate(['D4', 'F#4', 'A4', 'F#4', 'G4', 'F#4'] * 3)]
    bass3 = [{'pitches': p, 'dur': 'h.'} for p in [RE, SOL, LA]]
    y = grand_staff_block(c, x0, w0, y, gap, treb3, bass3, 'a) Melodía en movimiento; acordes largos que no se apresuran', grand_gap_mult=7.05, time_sig=TS)

    treb4 = [{'pitch': p, 'dur': 'q'} for p in ['F#4', 'G4', 'A4', 'G4', 'F#4', 'E4', 'D4', 'F#4', 'A4']]
    y = system_block(c, x0, w0, y, gap, 'b) Variación: la frase un poco más alta', treb4, clef='treble', time_sig=TS)
    y -= 1

    y = exercise_heading(c, y, 6, 'Reto final · Can\'t Help Falling In Love casi entera', 3,
                          'Con la partitura al lado: estira solo donde de verdad respira la frase, y vuelve enseguida al pulso — ese es el criterio.')
    y -= 5
    treb5 = [{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4', 'F#4', 'E4']] + [{'pitch': 'D4', 'dur': 'h.'}]
    treb5 += [{'pitch': p, 'dur': 'q'} for p in ['A4', 'G4', 'F#4', 'E4', 'D4', 'F#4']] + [{'pitch': 'A4', 'dur': 'h.'}]
    bass5 = [{'pitches': p, 'dur': 'h.'} for p in [RE, SOL, LA, RE, LA, RE]]
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'La canción casi completa · ♩≈72, con rubato con criterio', grand_gap_mult=7.05, time_sig=TS)

    exercises_footer(c, 4)
    c.showPage()
