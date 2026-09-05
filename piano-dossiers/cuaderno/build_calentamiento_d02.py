# -*- coding: utf-8 -*-
"""Calentamiento de Can't Help Falling in Love (Dilan, avanzado).

   DERIVA de la pieza, no la copia: el acorde roto se transporta por toda la
   tonalidad, la escala se trabaja en terceras y el gesto se invierte. Los
   compases literales estan en las hojas "al piano".
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from hoja_calentamiento import build_calentamiento
from dilan_02_data import arpegio

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                          ' cant-help-falling-in-love-.pdf')
RE = 'Re mayor'

ESCALA = ['D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4',
          'A4', 'B4', 'C5', 'D5']


def esc(ps, b0):
    return [{'pitch': p, 'dur': 'e', 'beam': b0 + i // 3} for i, p in enumerate(ps)]


def terceras(pares):
    return [{'pitches': list(d), 'dur': 'q'} for d in pares]


CFG = dict(
    kicker='Dilan · canción 2 · Can’t Help Falling in Love',
    page_num=5, time_sig=(3, 4), key_sig=RE, gap=7.0,
    intro='Cinco minutos antes de abrir la partitura. La tonalidad es Re mayor y el gesto de toda '
          'la canción es un acorde roto que sube y baja. Aquí se trabaja ese gesto en TODA la '
          'tonalidad, no solo en los acordes que la pieza usa.',
    reglas=['ARMADURA DE RE: FA♯ Y DO♯', 'MANOS SEPARADAS PRIMERO', 'SIN ACENTUAR LA PRIMERA'],
    ejercicios=[
        dict(num=1, titulo='Escala de Re mayor · dos octavas',
             pista='manos separadas · el pulgar por debajo sin que se oiga el bache',
             events=esc(ESCALA, 10) + esc(list(reversed(ESCALA))[1:14], 20) +
                    [{'pitch': 'D3', 'dur': 'q'}], bars_per_line=5, clef='bass'),
        dict(num=2, titulo='El acorde roto, por toda la tonalidad',
             pista='el gesto de la canción sobre los seis grados de Re mayor, no solo sobre cuatro',
             events=(arpegio('D3', 'F3', 'A3', 'D4') + arpegio('E3', 'G3', 'B3', 'E4') +
                     arpegio('F3', 'A3', 'C4', 'F4') + arpegio('G3', 'B3', 'D4', 'G4') +
                     arpegio('A3', 'C4', 'E4', 'A4') + arpegio('B3', 'D4', 'F4', 'B4')),
             bars_per_line=3, clef='bass'),
        dict(num=3, titulo='El gesto al revés',
             pista='la pieza sube y baja · aquí bajas y subes, que es lo que nunca practicas',
             events=(arpegio('D4', 'A3', 'F3', 'D3') + arpegio('E4', 'B3', 'G3', 'E3') +
                     arpegio('F4', 'C4', 'A3', 'F3') + arpegio('G4', 'D4', 'B3', 'G3')),
             bars_per_line=4, clef='bass'),
        dict(num=4, titulo='Terceras dobles en Re mayor',
             pista='lo que la pieza no te da · las dos notas exactamente juntas',
             events=terceras([('D4', 'F4'), ('E4', 'G4'), ('F4', 'A4'), ('G4', 'B4'),
                              ('A4', 'C5'), ('B4', 'D5'), ('A4', 'C5'), ('G4', 'B4'),
                              ('F4', 'A4'), ('E4', 'G4')]) +
                    [{'pitches': ['D4', 'F4'], 'dur': 'h'}],
             bars_per_line=4),
        dict(num=5, titulo='El mismo acorde roto, con la mano derecha',
             pista='la mano que aquí solo pone una nota por compás · ahora le toca trabajar',
             events=(arpegio('D4', 'F4', 'A4', 'D5') + arpegio('B3', 'D4', 'F4', 'B4') +
                     arpegio('G3', 'B3', 'D4', 'G4') + arpegio('A3', 'C5', 'E5', 'A5')),
             bars_per_line=4),
    ],
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = os.path.join(HERE, '_c2_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H)); build_calentamiento(c, CFG); c.save()
    wr = PdfWriter()
    for p in PdfReader(tmp).pages: wr.add_page(p)
    for p in PdfReader(SOURCE_PDF).pages: wr.add_page(p)
    out = os.path.join(OUT_DIR, 'Dilan_02_Calentamiento_y_Partitura.pdf')
    with open(out, 'wb') as f: wr.write(f)
    os.remove(tmp); print('generated', out)


if __name__ == '__main__':
    main()
