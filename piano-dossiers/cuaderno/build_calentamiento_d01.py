# -*- coding: utf-8 -*-
"""Calentamiento de El Cisne para Dilan (nivel avanzado).

   A este nivel el calentamiento ya no es "mover los dedos": es preparar los
   dos problemas concretos de la pieza antes de abrirla.
     1. la escala y el arpegio de Sol mayor, que es la tonalidad
     2. la célula de acompañamiento de la izquierda, transportada por los
        grados que la pieza usa de verdad
     3. la escala de los cc. 7-9, que está literalmente escrita en la obra
   Todo con armadura, no con sostenidos sueltos.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from hoja_calentamiento import build_calentamiento
from dilan_01_data import corcheas, CELULA_I, CELULA_ii, CELULA_I7

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN', 'the-swan.pdf')

SOL = 'Sol mayor'


def neg(*p):
    return [{'pitch': n, 'dur': 'q'} for n in p]


# escala de Sol mayor, dos octavas, en corcheas con barra de tres en tres
ESCALA = ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5',
          'E5', 'F5', 'G5']
ESCALA_BAJA = list(reversed(ESCALA))[1:]


def esc(pitches, beam0):
    out = []
    for i, p in enumerate(pitches):
        out.append({'pitch': p, 'dur': 'e', 'beam': beam0 + i // 3})
    return out


ARPEGIO = ['G3', 'B3', 'D4', 'G4', 'B4', 'D5', 'G5', 'D5', 'B4', 'G4', 'D4', 'B3']

CFG = dict(
    kicker='Dilan · canción 1 · El Cisne',
    page_num=5,
    time_sig=(3, 4),
    key_sig=SOL,
    gap=7.0,
    intro='Cinco minutos antes de abrir la partitura. Todo sale de la pieza: la tonalidad es Sol '
          'mayor, la izquierda no para en 55 compases y la escala del ejercicio 4 está escrita '
          'tal cual en los cc. 7–9.',
    reglas=['ARMADURA DE SOL: TODOS LOS FA SON ♯',
            'EMPIEZA A ♩=60',
            'MANOS SEPARADAS PRIMERO'],
    ejercicios=[
        dict(num=1, titulo='Escala de Sol mayor · dos octavas',
             pista='manos separadas · el pulgar pasa por debajo sin que se oiga el bache',
             # una escala de ida y vuelta en corcheas SIEMPRE suma un numero
             # impar (2n-1), asi que nunca cuadra sola en 3/4: la nota final
             # tiene que valer una negra para cerrar el compas.
             events=esc(ESCALA, 10) + esc(ESCALA_BAJA[:13], 20) +
                    [{'pitch': 'G3', 'dur': 'q'}],
             bars_per_line=5),
        dict(num=2, titulo='Arpegio de Sol mayor',
             pista='es el acorde que la izquierda arpegia en los cc. 1–4 y 9–12',
             events=esc(ARPEGIO, 30) + esc(ARPEGIO, 40) + [{'pitch': 'G3', 'dur': 'h.'}],
             bars_per_line=5, clef='bass'),
        dict(num=3, titulo='La célula de la izquierda, tal cual',
             pista='los tres acordes reales de la primera frase: Sol · La menor/Sol · Sol maj7',
             events=(corcheas(CELULA_I, 2) + corcheas(CELULA_ii, 2) +
                     corcheas(CELULA_I7, 1) + corcheas(CELULA_I, 1)),
             bars_per_line=3, clef='bass'),
        dict(num=4, titulo='La escala que hay dentro de la pieza',
             pista='cc. 7–9 · de Mi4 a Sol5 sin un solo salto: tócala cantándola',
             events=esc(['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5'], 50) +
                    [{'pitch': 'G5', 'dur': 'h.'}] +
                    esc(['G5', 'F5', 'E5', 'D5', 'C5', 'B4', 'A4', 'G4', 'F4'], 60) +
                    [{'pitch': 'E4', 'dur': 'h.'}],
             bars_per_line=5),
        dict(num=5, titulo='Las dos manos a distinto volumen',
             pista='la izquierda pp y la derecha p · el ejercicio de toda la pieza',
             events=corcheas(CELULA_I, 4),
             bars_per_line=4, clef='bass'),
    ],
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = os.path.join(HERE, '_cd_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_calentamiento(c, CFG)
    c.save()
    wr = PdfWriter()
    for p in PdfReader(tmp).pages: wr.add_page(p)
    for p in PdfReader(SOURCE_PDF).pages: wr.add_page(p)
    out = os.path.join(OUT_DIR, 'Dilan_01_Calentamiento_y_Partitura.pdf')
    with open(out, 'wb') as f: wr.write(f)
    os.remove(tmp)
    print('generated', out)


if __name__ == '__main__':
    main()
