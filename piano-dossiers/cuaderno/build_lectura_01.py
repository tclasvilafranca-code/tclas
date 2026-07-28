# -*- coding: utf-8 -*-
"""Hoja de agudeza visual de la canción 1 (Chopsticks).

   Registro y figuras tomados de la partitura real:
     - clave de Sol (la pieza no usa clave de Fa en ningún momento)
     - registro Mi4 - Re5
     - figuras que aparecen: negra, blanca, blanca con puntillo y silencio
       de negra (estos últimos en los cc. 13-16)

   El orden de las notas es deliberadamente IRREGULAR: si hubiera patrón,
   el alumno lo adivinaría en vez de leerlo. Ninguna célula se repite.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from hoja_lectura import build_lectura

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU', ' Chopsticks.pdf')

R = {'rest': True, 'dur': 'q'}


def q(*names):
    return [{'pitch': n, 'dur': 'q'} for n in names]


CFG = dict(
    kicker='Arnau · canción 1 · Chopsticks',
    page_num=6,
    time_sig=(3, 4),
    intro='No se toca el piano en esta hoja: solo se lee. Di el nombre de cada nota en voz alta, '
          'seguido y sin parar. Son las mismas notas y las mismas figuras que vas a encontrar en '
          'la partitura.',
    reglas=['DI EL NOMBRE EN VOZ ALTA',
            'SIN PARAR, DE IZQUIERDA A DERECHA',
            'SI PUEDES, CÁNTALA'],
    chuleta_pitches=['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5'],
    chuleta_nombres=['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do', 'Re'],
    ejercicios=[
        dict(num=1, titulo='Las notas de la pieza',
             pista='solo Mi, Fa, Sol y Si · son las cuatro que usa Chopsticks',
             events=q('G4', 'B4', 'E4', 'F4', 'E4', 'G4', 'B4', 'G4', 'F4',
                      'E4', 'F4', 'B4', 'G4', 'E4', 'B4') +
                    q('E4', 'G4', 'F4', 'B4', 'E4', 'G4', 'F4', 'B4', 'E4',
                      'G4', 'F4', 'G4', 'B4', 'E4', 'F4')),
        dict(num=2, titulo='Ahora todas',
             pista='se añaden Do, Re y La · atención al Do de abajo, lleva línea adicional',
             events=q('C5', 'A4', 'E4', 'D5', 'G4', 'B4', 'F4', 'C5', 'A4',
                      'E4', 'D4', 'G4', 'B4', 'F4', 'C4') +
                    q('A4', 'E4', 'D5', 'G4', 'C4', 'F4', 'B4', 'A4', 'E4',
                      'D4', 'F4', 'C5', 'G4', 'B4', 'E4')),
        dict(num=3, titulo='Con blancas',
             pista='la figura larga de los cc. 17–32 · la blanca dura dos tiempos',
             events=[{'pitch': 'G4', 'dur': 'h'}, {'pitch': 'E4', 'dur': 'q'},
                     {'pitch': 'B4', 'dur': 'h'}, {'pitch': 'F4', 'dur': 'q'},
                     {'pitch': 'C5', 'dur': 'h'}, {'pitch': 'A4', 'dur': 'q'},
                     {'pitch': 'E4', 'dur': 'h'}, {'pitch': 'D5', 'dur': 'q'},
                     {'pitch': 'F4', 'dur': 'h.'}]),
        dict(num=4, titulo='Con silencios',
             pista='los cc. 13–16 · en el silencio no digas nada, pero cuenta igual',
             events=[{'pitch': 'E4', 'dur': 'q'}, R, {'pitch': 'G4', 'dur': 'q'},
                     R, {'pitch': 'B4', 'dur': 'q'}, R,
                     {'pitch': 'F4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, R,
                     R, {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'},
                     {'pitch': 'G4', 'dur': 'h.'}]),
        dict(num=5, titulo='Todo mezclado',
             pista='la prueba de verdad · notas, blancas y silencios sin avisar',
             events=[{'pitch': 'B4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'h'},
                     {'pitch': 'F4', 'dur': 'q'}, R, {'pitch': 'C5', 'dur': 'q'},
                     {'pitch': 'A4', 'dur': 'h'}, {'pitch': 'G4', 'dur': 'q'},
                     {'pitch': 'D5', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}, R,
                     {'pitch': 'F4', 'dur': 'h.'}]),
    ],
    crono='¿Cuánto tardas en leer el ejercicio 5 entero, sin fallos?',
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = os.path.join(HERE, '_lec_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_lectura(c, CFG)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(tmp).pages:
        writer.add_page(p)
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    out = os.path.join(OUT_DIR, 'Arnau_01_Lectura_y_Partitura.pdf')
    with open(out, 'wb') as f:
        writer.write(f)
    os.remove(tmp)
    print('generated', out)


if __name__ == '__main__':
    main()
