# -*- coding: utf-8 -*-
"""Hoja de calentamiento de la canción 1 (Chopsticks).

   El material DERIVA de la pieza, pero no la copia: se transporta, se invierte
   o se amplía. Los compases literales viven en las hojas "al piano", con su
   número de compás. Si las dos hojas usan las mismas notas acaban siendo la
   misma hoja — paso en la primera versión y esta corregido.

   Lo que se hereda de la partitura:
     - mismo compás (3/4) y misma escritura (las dos manos en clave de Sol
       sobre UN pentagrama, como la edición de DeBenedetti)
     - mismo dedo (2 en cada mano, según la indicación impresa)
     - los mismos intervalos que la pieza abre: 2ª -> 3ª -> 6ª -> 8ª
       (medidos sobre la partitura; ver TRANSCRIPCION_01_CHOPSTICKS.md)
     - el ritmo de la parte B (blanca + negra, en terceras paralelas) y los
       silencios de los cc. 15-16
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
    page_num=5,
    time_sig=(3, 4),
    intro='Cinco minutos antes de abrir la partitura. Todo lo de esta hoja está sacado de '
          'Chopsticks: el mismo compás, la misma clave y los mismos intervalos que la pieza abre.',
    reglas=['SOLO EL DEDO 2 DE CADA MANO',
            'EMPIEZA A ♩=60',
            'CUENTA “UN-DOS-TRES” EN VOZ ALTA'],
    ejercicios=[
        dict(num=1, titulo='El dedo 2 camina',
             pista='primero la mano derecha, después la izquierda · tres golpes por tecla',
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
        dict(num=4, titulo='Se abren mucho · 6ª y 8ª',
             pista='cuatro y seis teclas en medio · así suenan los cc. 5–8',
             events=seq([('D4', 'B4'), ('C4', 'C5'), ('D4', 'B4'),
                         ('E4', 'A4'), ('D4', 'B4'), ('C4', 'C5')])),
        # El viaje de la pieza, pero TRANSPORTADO un grado: el calentamiento
        # generaliza, la hoja 'al piano' cita los compases tal cual. Si los dos
        # usan las mismas notas, las dos hojas acaban siendo la misma.
        dict(num=5, titulo='El viaje entero, empezando más arriba',
             pista='2ª → 3ª → 6ª → 8ª y vuelta, un grado por encima de la pieza',
             events=seq([('G4', 'A4'), ('F4', 'A4'), ('E4', 'C5'),
                         ('D4', 'D5'), ('E4', 'C5'), ('F4', 'B4')])),
        # la pieza baja en terceras; el calentamiento las SUBE, que es el gesto
        # contrario y el que no vas a practicar tocando la canción
        dict(num=6, titulo='El vals, pero subiendo',
             pista='una larga y una corta · en la pieza las terceras bajan, aquí suben',
             events=[e for d in [('E4', 'G4'), ('F4', 'A4'), ('G4', 'B4'),
                                 ('A4', 'C5'), ('B4', 'D5')]
                     for e in ({'pitches': list(d), 'dur': 'h'},
                               {'pitches': list(d), 'dur': 'q'})] +
                    [{'pitches': ['C5', 'E5'], 'dur': 'h.'}]),
        dict(num=7, titulo='Contar el silencio',
             pista='lo más difícil de la pieza (cc. 15–16): el silencio dura igual que la nota',
             events=([{'pitches': ['G4', 'A4'], 'dur': 'q'}, R, R] +
                     [R, {'pitches': ['G4', 'A4'], 'dur': 'q'}, R] +
                     [R, R, {'pitches': ['G4', 'A4'], 'dur': 'q'}] +
                     [{'pitches': ['F4', 'A4'], 'dur': 'q'}, R,
                      {'pitches': ['F4', 'A4'], 'dur': 'q'}] +
                     [R, {'pitches': ['F4', 'A4'], 'dur': 'q'}, R] +
                     [{'pitches': ['G4', 'A4'], 'dur': 'h.'}])),
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
