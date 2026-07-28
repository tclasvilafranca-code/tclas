# -*- coding: utf-8 -*-
"""Hoja de calentamiento de la canción 1 (Chopsticks).

   Todo el material sale de la propia pieza:
     - mismo compás (3/4) y misma escritura (las dos manos en clave de Sol
       sobre UN pentagrama, como la edición de DeBenedetti)
     - mismo dedo (2 en cada mano, según la indicación impresa)
     - los mismos intervalos que la pieza abre: 2ª -> 3ª -> 5ª
     - el ritmo de la parte B (blanca + negra) y los silencios de los cc. 13-16
   Cada ejercicio es una CÉLULA transportada grado a grado (principio de
   secuencia), no notas sueltas: 6 compases por línea, 18 notas por línea.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from hoja_calentamiento import build_calentamiento, _rep, _rep1

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU', ' Chopsticks.pdf')

R = {'rest': True, 'dur': 'q'}


def seq(cells, n=3):
    """Encadena células repetidas: la base de todo ejercicio técnico real."""
    out = []
    for cell in cells:
        out += _rep(cell, n) if isinstance(cell, (list, tuple)) else _rep1(cell, n)
    return out


CFG = dict(
    kicker='Arnau · canción 1 · Chopsticks',
    page_num=3,
    time_sig=(3, 4),
    intro='Cinco minutos antes de abrir la partitura. Todo lo de esta hoja está sacado de '
          'Chopsticks: el mismo compás, la misma clave y los mismos intervalos que la pieza abre.',
    reglas=['SOLO EL DEDO 2 DE CADA MANO',
            'LAS DOS MANOS EN CLAVE DE SOL',
            'CUENTA “UN-DOS-TRES” EN VOZ ALTA'],
    ejercicios=[
        dict(num=1, titulo='El dedo 2 camina',
             pista='una sola mano · tres golpes por tecla, y te mueves a la siguiente',
             events=seq(['C4', 'D4', 'E4', 'F4', 'G4', 'F4']) +
                    seq(['E4', 'D4', 'C4', 'D4', 'E4', 'C4'])),
        dict(num=2, titulo='Las dos manos pegadas · 2ª',
             pista='como empieza la pieza: teclas vecinas, un solo golpe limpio',
             events=seq([('C4', 'D4'), ('D4', 'E4'), ('E4', 'F4'),
                         ('F4', 'G4'), ('G4', 'A4'), ('F4', 'G4')])),
        dict(num=3, titulo='Se abren · 3ª',
             pista='una tecla en medio · así suenan los cc. 3–4',
             events=seq([('C4', 'E4'), ('D4', 'F4'), ('E4', 'G4'),
                         ('F4', 'A4'), ('G4', 'B4'), ('E4', 'G4')])),
        dict(num=4, titulo='Se abren más · 5ª',
             pista='tres teclas en medio · así suenan los cc. 5–8',
             events=seq([('C4', 'G4'), ('D4', 'A4'), ('E4', 'B4'),
                         ('F4', 'C5'), ('G4', 'D5'), ('E4', 'B4')])),
        dict(num=5, titulo='La apertura de la pieza, seguida',
             pista='2ª → 3ª → 5ª y vuelta · el juego entero de Chopsticks',
             events=seq([('F4', 'G4'), ('E4', 'G4'), ('E4', 'B4'),
                         ('E4', 'B4'), ('E4', 'G4'), ('F4', 'G4')])),
        dict(num=6, titulo='El vals de la parte B',
             pista='una larga y una corta · así son los cc. 17–32',
             events=[{'pitches': list(d), 'dur': 'h'} for d in [('F4', 'G4')]] +
                    [{'pitches': ['F4', 'G4'], 'dur': 'q'}] +
                    [{'pitches': ['E4', 'G4'], 'dur': 'h'}, {'pitches': ['E4', 'G4'], 'dur': 'q'}] +
                    [{'pitches': ['E4', 'B4'], 'dur': 'h'}, {'pitches': ['E4', 'B4'], 'dur': 'q'}] +
                    [{'pitches': ['E4', 'G4'], 'dur': 'h'}, {'pitches': ['E4', 'G4'], 'dur': 'q'}] +
                    [{'pitches': ['F4', 'G4'], 'dur': 'h'}, {'pitches': ['F4', 'G4'], 'dur': 'q'}] +
                    [{'pitches': ['F4', 'G4'], 'dur': 'h.'}]),
        dict(num=7, titulo='Contar el silencio',
             pista='lo más difícil de la pieza (cc. 13–16): el silencio dura igual que la nota',
             events=([{'pitches': ['F4', 'G4'], 'dur': 'q'}, R, R] +
                     [R, {'pitches': ['F4', 'G4'], 'dur': 'q'}, R] +
                     [R, R, {'pitches': ['F4', 'G4'], 'dur': 'q'}] +
                     [{'pitches': ['E4', 'G4'], 'dur': 'q'}, R,
                      {'pitches': ['E4', 'G4'], 'dur': 'q'}] +
                     [R, {'pitches': ['E4', 'G4'], 'dur': 'q'}, R] +
                     [{'pitches': ['F4', 'G4'], 'dur': 'h.'}])),
    ],
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = os.path.join(HERE, '_cal_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_calentamiento(c, CFG)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(tmp).pages:
        writer.add_page(p)
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    out = os.path.join(OUT_DIR, 'Arnau_01_Calentamiento_y_Partitura.pdf')
    with open(out, 'wb') as f:
        writer.write(f)
    os.remove(tmp)
    print('generated', out)


if __name__ == '__main__':
    main()
