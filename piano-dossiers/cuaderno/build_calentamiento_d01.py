# -*- coding: utf-8 -*-
"""Calentamiento de El Cisne para Dilan (nivel avanzado).

   A este nivel el calentamiento ya no es "mover los dedos": es preparar los
   problemas concretos de la pieza antes de abrirla — pero SIN copiar sus
   compases. Los compases literales van en las hojas "al piano", citados con su
   número. Aqui todo esta transportado, invertido o ampliado.
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


# Escala de Sol mayor, dos octavas, en corcheas con barra de tres en tres.
# Va en el REGISTRO DE LA IZQUIERDA, una octava por debajo de la melodia: los
# cc. 7-9 de la pieza son literalmente esta escala, y si el calentamiento la
# pone en el mismo sitio, la hoja acaba siendo la misma que la de 'al piano'
# (lo canta el auditor de duplicados con ocho notas seguidas identicas).
ESCALA = ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4',
          'E4', 'F4', 'G4']
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
                    [{'pitch': 'G2', 'dur': 'q'}],
             bars_per_line=5, clef='bass'),
        dict(num=2, titulo='Arpegio de Sol mayor',
             pista='es el acorde que la izquierda arpegia en los cc. 1–4 y 9–12',
             events=esc(ARPEGIO, 30) + esc(ARPEGIO, 40) + [{'pitch': 'G3', 'dur': 'h.'}],
             bars_per_line=5, clef='bass'),
        # El calentamiento NO reproduce compases de la pieza: los transporta.
        # Si se copian tal cual, esta hoja y la de 'al piano' acaban siendo la
        # misma, que es justo lo que paso en la primera version.
        dict(num=3, titulo='El dibujo de la izquierda, por grados',
             pista='sobre Sol, La, Si y vuelta · así vale para toda la pieza, no solo para el c. 1',
             events=(corcheas(['G2', 'D3', 'B3', 'D3', 'B3', 'D3']) +
                     corcheas(['A2', 'E3', 'C4', 'E3', 'C4', 'E3']) +
                     corcheas(['B2', 'F3', 'D4', 'F3', 'D4', 'F3']) +
                     corcheas(['A2', 'E3', 'C4', 'E3', 'C4', 'E3']) +
                     corcheas(['G2', 'D3', 'B3', 'D3', 'B3', 'D3']) +
                     corcheas(['F2', 'C3', 'A3', 'C3', 'A3', 'C3'])),
             bars_per_line=3, clef='bass'),
        # la escala literal de los cc. 7-9 vive en la hoja 'al piano': aqui va
        # la version que la pieza NO tiene, que es la que entrena de verdad
        dict(num=4, titulo='La escala en terceras dobles',
             pista='lo que la pieza no te da · las dos notas tienen que caer exactamente juntas',
             events=[{'pitches': list(d), 'dur': 'q'} for d in
                     [('G4', 'B4'), ('A4', 'C5'), ('B4', 'D5'), ('C5', 'E5'),
                      ('D5', 'F5'), ('E5', 'G5'),
                      ('D5', 'F5'), ('C5', 'E5'), ('B4', 'D5'), ('A4', 'C5')]] +
                    [{'pitches': ['G4', 'B4'], 'dur': 'h'}],
             bars_per_line=4),
        dict(num=5, titulo='El mismo dibujo, en Re mayor',
             pista='cambia de tonalidad y el problema sigue igual: que las seis corcheas suenen iguales',
             events=corcheas(['D3', 'A3', 'F4', 'A3', 'F4', 'A3'], 4),
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
