# -*- coding: utf-8 -*-
"""Genera 9 fichas de MUESTRA (1 por paso x 1 por nivel) para que la
   profesora revise el formato antes de encargar las 90 fichas completas
   (10 por paso x nivel x 3 niveles x 3 pasos)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from fichas_layout import (W, H, MARGIN, CONTENT_W, ficha_header, ficha_intro,
                            ficha_footer, ruled_box, system_block, grand_staff_block)

HERE = os.path.dirname(__file__)
OUT_PATH = os.path.join(HERE, 'Fichas_Muestra.pdf')


# ---------------------------------------------------------------------------
# PASO 1bis · CALENTAMIENTO DE DEDOS  (tecnica de muestra: escalas de 5 dedos)
# ---------------------------------------------------------------------------

def calentamiento_n1(c):
    y = ficha_header(c, 'Calentamiento de dedos', 1, 3, 'Escalas de 5 dedos: Do Mayor')
    y = ficha_intro(c, y, 'Coloca los 5 dedos sobre Do-Re-Mi-Fa-Sol, mano derecha. Sube y baja muy despacio, '
                          'sintiendo cada dedo. Repite cada sistema varias veces antes de pasar al siguiente.')
    gap = 8.2
    ev_a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'a) Sube y baja, contando 1-2-3-4-5', ev_a, clef='treble', time_sig=(4, 4))
    y -= 10
    ev_b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
            [('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4)]]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) Empieza al revés, desde el dedo 5', ev_b, clef='treble', time_sig=(4, 4))
    ficha_footer(c, 'Calentamiento · Nivel 1')
    c.showPage()


def calentamiento_n2(c):
    y = ficha_header(c, 'Calentamiento de dedos', 2, 3, 'Escalas de 5 dedos: manos juntas')
    y = ficha_intro(c, y, 'Las dos manos suben y bajan A LA VEZ, en la misma dirección (movimiento paralelo). '
                          'Cuenta en voz alta mientras tocas para que no se descoordinen.')
    gap = 7.8
    treb_a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    bass_a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('C3', 5), ('D3', 4), ('E3', 3), ('F3', 2), ('G3', 1), ('F3', 2), ('E3', 3), ('D3', 4)]]
    y = grand_staff_block(c, MARGIN, CONTENT_W, y, gap, treb_a, bass_a,
                           'a) Las dos manos suben y bajan juntas', grand_gap_mult=7.3, time_sig=(4, 4))
    y -= 8
    treb_b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4)]]
    bass_b = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('G3', 1), ('F3', 2), ('E3', 3), ('D3', 4), ('C3', 5), ('D3', 4), ('E3', 3), ('F3', 2)]]
    y = grand_staff_block(c, MARGIN, CONTENT_W, y, gap, treb_b, bass_b,
                           'b) Ahora empezando desde arriba', grand_gap_mult=7.3, time_sig=(4, 4))
    ficha_footer(c, 'Calentamiento · Nivel 2')
    c.showPage()


def calentamiento_n3(c):
    y = ficha_header(c, 'Calentamiento de dedos', 3, 3, 'Escalas de 5 dedos: movimiento contrario')
    y = ficha_intro(c, y, 'Las dos manos se alejan y se acercan a la vez, en direcciones OPUESTAS. '
                          'Es más difícil de coordinar: empieza muy despacio antes de acelerar.')
    gap = 7.6
    treb_a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]]
    bass_a = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in
              [('C3', 1), ('B2', 2), ('A2', 3), ('G2', 4), ('F2', 5), ('G2', 4), ('A2', 3), ('B2', 2)]]
    y = grand_staff_block(c, MARGIN, CONTENT_W, y, gap, treb_a, bass_a,
                           'a) Se separan y vuelven a juntarse, cada una a su ritmo', grand_gap_mult=7.3, time_sig=(4, 4))
    y -= 8
    ev_extra = [{'pitches': p, 'dur': 'q'} for p in [['C4', 'E4'], ['D4', 'F4'], ['E4', 'G4'], ['F4', 'A4']]]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'b) Extra: notas dobles en terceras, mano derecha', ev_extra, clef='treble', time_sig=(4, 4))
    ficha_footer(c, 'Calentamiento · Nivel 3')
    c.showPage()


# ---------------------------------------------------------------------------
# PASO 1 · AGUDEZA VISUAL  (lectura de notas en voz alta, con el tono correcto)
# ---------------------------------------------------------------------------

def agudeza_n1(c):
    y = ficha_header(c, 'Agudeza visual', 1, 3, 'Lectura de notas: clave de Sol')
    y = ficha_intro(c, y, 'Di el nombre de cada nota en voz alta, con el tono correcto (más grave o más agudo '
                          'según suba o baje el dibujo). No hace falta tocarlas: solo leerlas rápido.')
    gap = 8.2
    ev1 = [{'pitch': p, 'dur': 'q'} for p in ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'C5']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '1', ev1, clef='treble', time_sig=(4, 4))
    y -= 10
    ev2 = [{'pitch': p, 'dur': 'q'} for p in ['F4', 'G4', 'A4', 'G4', 'F4', 'E4', 'D5', 'C5']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '2', ev2, clef='treble', time_sig=(4, 4))
    y -= 10
    ev3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'B4', 'A4', 'C5', 'B4', 'D5', 'E5', 'D5']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '3', ev3, clef='treble', time_sig=(4, 4))
    ficha_footer(c, 'Agudeza visual · Nivel 1')
    c.showPage()


def agudeza_n2(c):
    y = ficha_header(c, 'Agudeza visual', 2, 3, 'Lectura de notas: clave de Sol y clave de Fa')
    y = ficha_intro(c, y, 'Lee cada sistema en voz alta, diciendo el nombre y la altura exacta. Alterna entre '
                          'las dos claves sin pararte a pensar mucho.')
    gap = 7.8
    ev1 = [{'pitch': p, 'dur': 'q'} for p in ['C4', 'E4', 'G4', 'F4', 'A4', 'D5', 'C5', 'B4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '1 · clave de Sol', ev1, clef='treble', time_sig=(4, 4))
    y -= 9
    ev2 = [{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3', 'F3', 'A3', 'D4', 'C4', 'B3']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '2 · clave de Fa', ev2, clef='bass', time_sig=(4, 4))
    y -= 9
    ev3 = [{'pitch': p, 'dur': 'q'} for p in ['G4', 'A4', 'B4', 'A4', 'G4', 'F4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '3 · clave de Sol, en 3/4', ev3, clef='treble', time_sig=(3, 4))
    ficha_footer(c, 'Agudeza visual · Nivel 2')
    c.showPage()


def agudeza_n3(c):
    y = ficha_header(c, 'Agudeza visual', 3, 3, 'Lectura de notas: claves y compases mixtos')
    y = ficha_intro(c, y, 'Lee rápido, sin pararte, cambiando de compás y de clave. Si te equivocas, sigue: '
                          'lo importante es no perder el ritmo de lectura.')
    gap = 7.3
    ev1 = [{'pitch': p, 'dur': 'q'} for p in ['C5', 'D5', 'E5', 'F5', 'G5', 'F5', 'E5', 'D5']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '1 · clave de Sol, agudo', ev1, clef='treble', time_sig=(4, 4))
    y -= 8
    ev2 = [{'pitch': p, 'dur': 'q'} for p in ['A2', 'G2', 'F2', 'E2', 'D2', 'E2', 'F2', 'G2']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '2 · clave de Fa, grave', ev2, clef='bass', time_sig=(4, 4))
    y -= 8
    ev3 = [{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['E4', 'F4', 'G4', 'A4', 'G4', 'F4'])]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '3 · clave de Sol, en 6/8', ev3, clef='treble', time_sig=(6, 8))
    y -= 8
    ev4 = [{'pitch': p, 'dur': 'q'} for p in ['D3', 'E3', 'F3', 'D3', 'E3', 'F3']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, '4 · clave de Fa, en 3/4', ev4, clef='bass', time_sig=(3, 4))
    ficha_footer(c, 'Agudeza visual · Nivel 3')
    c.showPage()


# ---------------------------------------------------------------------------
# PASO 4 · CIERRE Y RELAJACION DE DEDOS  (+ apuntes para la semana)
# ---------------------------------------------------------------------------

def cierre_n1(c):
    y = ficha_header(c, 'Cierre y relajación', 1, 3, 'Relajación: Do-Mi-Sol, muy tranquilo')
    y = ficha_intro(c, y, 'Toca esto muy despacio, dejando caer la mano sin peso. Es para relajar los dedos, '
                          'no para practicar nada nuevo.')
    gap = 8.2
    ev = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'E4', 'G4', 'E4']]
    y = system_block(c, MARGIN, CONTENT_W, y, gap, 'Respira, y deja sonar cada nota', ev, clef='treble', time_sig=(4, 4))
    y -= 14
    y = ruled_box(c, y, 88, 'Apuntes para esta semana')
    ficha_footer(c, 'Cierre · Nivel 1')
    c.showPage()


def cierre_n2(c):
    y = ficha_header(c, 'Cierre y relajación', 2, 3, 'Relajación: melodía con acompañamiento')
    y = ficha_intro(c, y, 'La izquierda sostiene el acorde sin moverse; la derecha canta muy despacio por encima. '
                          'Deja que el sonido se apague solo antes de la siguiente nota.')
    gap = 7.8
    treb = [{'pitch': p, 'dur': 'h'} for p in ['C4', 'D4', 'E4', 'D4']]
    bass = [{'pitches': ['C3', 'E3', 'G3'], 'dur': 'w'}, {'pitches': ['C3', 'E3', 'G3'], 'dur': 'w'}]
    y = grand_staff_block(c, MARGIN, CONTENT_W, y, gap, treb, bass, 'Respira, y deja sonar cada acorde', grand_gap_mult=7.3, time_sig=(4, 4))
    y -= 14
    y = ruled_box(c, y, 88, 'Apuntes para esta semana')
    ficha_footer(c, 'Cierre · Nivel 2')
    c.showPage()


def cierre_n3(c):
    y = ficha_header(c, 'Cierre y relajación', 3, 3, 'Relajación: acordes suaves I-IV-V-I')
    y = ficha_intro(c, y, 'Una progresión sencilla y calmada para terminar. Sigue siendo fácil: el objetivo es '
                          'bajar revoluciones, no practicar algo nuevo.')
    gap = 7.6
    treb = [{'pitch': p, 'dur': 'h'} for p in ['E4', 'F4', 'G4', 'E4']]
    bass = [{'pitches': p, 'dur': 'h', 'label': l} for p, l in
            [(['C3', 'E3', 'G3'], 'Do'), (['F2', 'A2', 'C3'], 'Fa'), (['G2', 'B2', 'D3'], 'Sol'), (['C3', 'E3', 'G3'], 'Do')]]
    y = grand_staff_block(c, MARGIN, CONTENT_W, y, gap, treb, bass, 'Do-Fa-Sol-Do, muy suave', grand_gap_mult=7.3, time_sig=(4, 4))
    y -= 14
    y = ruled_box(c, y, 88, 'Apuntes para esta semana')
    ficha_footer(c, 'Cierre · Nivel 3')
    c.showPage()


def main():
    c = canvas.Canvas(OUT_PATH, pagesize=(W, H))
    for fn in (calentamiento_n1, calentamiento_n2, calentamiento_n3,
               agudeza_n1, agudeza_n2, agudeza_n3,
               cierre_n1, cierre_n2, cierre_n3):
        fn(c)
    c.save()
    print('generated', OUT_PATH)


if __name__ == '__main__':
    main()
