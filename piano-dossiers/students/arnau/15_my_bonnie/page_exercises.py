# -*- coding: utf-8 -*-
"""Taller de practica - My Bonnie Lies Over the Ocean (Arnau, cancion
   15, Do mayor, 3/4). Formato por BLOQUES del Dosier Exhaustivo de
   Ejercicios de Piano (bloques 1,2,3,4,6). Reto motivador (nivel
   basico): cambio de posicion de la izquierda + primer contacto con
   el cruce de manos."""
from page_layout_common import *

SONG_KICKER = 'ARNAU · RETO MOTIVADOR · MY BONNIE'
TS = (3, 4)

DO = ['C3', 'E3', 'G3']
FA = ['F2', 'A2', 'C3']
SOL = ['G2', 'B2', 'D3']


def page1(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de partitura y técnica · 1/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Un reto especial en Do mayor: la izquierda cambia de sitio a mitad de frase. ¡Tú puedes!')
    y -= 15
    gap = 7.3
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 1, 'Antes de sentarte al piano. Sin tocar ninguna tecla.')
    y -= 2
    y = bullet_list(c, y, [
        'Frota las manos y abre/cierra los puños con los brazos estirados.',
        'Con los ojos cerrados, mueve la mano izquierda a distintos puntos del aire y "aterriza" con confianza.',
        'Estira todo el brazo hacia un punto lejano y vuelve, muy despacio.',
    ], dot_color=BLOQUE_COLOR[1])
    y -= 8

    y = bloque_heading(c, y, 2, 'Ya en el piano. Categoría D (ergonomía): salta la izquierda sin mirar, sin forzar la muñeca.')
    y -= 4
    ev1a = [{'pitch': p, 'dur': 'h.'} for p in ['C3', 'C4', 'C3', 'C4']]
    y = system_block(c, x0, w0, y, gap, 'a) El salto de posición, solo con la izquierda', ev1a, clef='bass', time_sig=TS)

    ev2b = [{'pitches': ['C4', 'E4', 'G4'], 'dur': 'h.'}, {'pitches': ['F3', 'A3', 'C4'], 'dur': 'h.'}]
    y = system_block(c, x0, w0, y, gap, 'b) La nueva posición, ya trasladada (la dificultad de hoy)', ev2b, clef='bass', time_sig=TS)

    pattern_a = [(DO, 'Do'), (FA, 'Fa'), (SOL, 'Sol'), (DO, 'Do')]
    eva = [{'pitches': p, 'dur': 'h.', 'label': l} for p, l in pattern_a]
    y = system_block(c, x0, w0, y, gap, 'c) Acordes I-IV-V: Do-Fa-Sol-Do', eva, clef='bass', time_sig=TS)

    exercises_footer(c, 3)
    c.showPage()


def page2(c):
    y = exercises_header(c, SONG_KICKER, 'Ejercicios de práctica al piano · 2/2')
    c.setFont('DejaVuSans', 9.2)
    c.setFillColor(GRAY)
    c.drawString(MARGIN, y, 'Categoría E: marca con lápiz en la partitura el compás exacto donde la izquierda cambia de sitio.')
    y -= 15
    gap = 6.9
    x0, w0 = MARGIN, CONTENT_W

    y = bloque_heading(c, y, 3, 'Con la partitura al lado. La derecha canta tranquila mientras la izquierda viaja.')
    y -= 4
    treb1 = [{'pitch': p, 'dur': 'h.'} for p in ['G4', 'A4', 'G4', 'F4']]
    bass1 = [{'pitches': FA, 'dur': 'h.'}] + [{'pitches': ['Bb3', 'D4', 'F4'], 'dur': 'h.'}] * 2 + [{'pitches': FA, 'dur': 'h.'}]
    y = grand_staff_block(c, x0, w0, y, gap, treb1, bass1, 'a) Manos juntas: la izquierda viaja de Fa a Sib y vuelve', grand_gap_mult=6.8, time_sig=TS)

    treb5 = ([{'pitch': p, 'dur': 'h.'} for p in ['E4', 'D4', 'C4']] +
             [{'pitch': p, 'dur': 'h.'} for p in ['E4', 'F4', 'G4']])
    bass5 = [{'pitches': DO, 'dur': 'h.'}] * 3 + [{'pitches': ['F3', 'A3', 'C4'], 'dur': 'h.'}] * 3
    y = grand_staff_block(c, x0, w0, y, gap, treb5, bass5, 'b) Reto extra: My Bonnie casi entera', grand_gap_mult=6.8, time_sig=TS)
    y -= 6

    y = bloque_heading(c, y, 4, 'De oído. El profesor toca, Arnau responde en voz alta (no se escribe).')
    y -= 2
    y = bullet_list(c, y, [
        'Toca el acorde de Fa y luego el de Sib: ¿es el mismo sitio o ha cambiado?',
        'Toca la nota grave de cada posición: ¿sube o baja la izquierda?',
        'Escucha el final, cuando la izquierda "visita" una nota alta: ¿te sorprende?',
    ], dot_color=BLOQUE_COLOR[4])
    y -= 6

    y = bloque_heading(c, y, 6, 'Aquí sí se escribe: sobre el papel, con la partitura delante.')
    y -= 4
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'Escribe el grado (I, IV, V) de cada acorde: Do__  Fa__  Sol__  Do__')
    y -= 6
    y = answer_box_row(c, MARGIN, y - 4, 4, (CONTENT_W - 3 * 6) / 4, gap=6)

    exercises_footer(c, 4)
    c.showPage()
