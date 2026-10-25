# -*- coding: utf-8 -*-
"""Hoja de agudeza visual y auditiva de la canción 1 (Chopsticks).

   Registro y figuras tomados de la partitura real (ver
   TRANSCRIPCION_01_CHOPSTICKS.md):
     - clave de Sol (la pieza no usa clave de Fa en ningún momento)
     - registro Do4 - Mi5
     - figuras que aparecen: negra, blanca, blanca con puntillo y silencio
       de negra (estos últimos en los cc. 15-16)

   PARTE 1: el orden de las notas es deliberadamente IRREGULAR — si hubiera
   patrón, el alumno lo adivinaría en vez de leerlo.

   PARTE 2: las preguntas salen de lo que la pieza hace de verdad. Chopsticks
   es una canción de intervalos que se abren y se cierran, así que la pregunta
   central es "cerca o lejos"; y tiene dos partes de carácter opuesto, así que
   la otra es "A o B".
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
    intro='Esta hoja no se toca: se lee y se escucha. La primera mitad la haces tú solo; la '
          'segunda la dirige quien esté contigo, y en ella no puedes mirar el teclado.',
    sub_leer='di el nombre de cada nota en voz alta, seguido y sin parar',
    chuleta_pitches=['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5'],
    chuleta_nombres=['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do', 'Re', 'Mi'],
    ejercicios=[
        dict(num=1, titulo='Las notas de la pieza',
             pista='solo Mi, Fa, Sol y Si · son las que más usa Chopsticks',
             events=q('G4', 'B4', 'E4', 'F4', 'E4', 'G4', 'B4', 'G4', 'F4',
                      'E4', 'F4', 'B4', 'G4', 'E4', 'B4')),
        dict(num=2, titulo='Ahora todas',
             pista='se añaden Do, Re y La · ojo al Do de abajo, lleva línea adicional',
             events=q('C5', 'A4', 'E4', 'D5', 'G4', 'B4', 'F4', 'C5', 'A4',
                      'E4', 'D4', 'G4', 'B4', 'F4', 'C4')),
        dict(num=3, titulo='Todo mezclado',
             pista='la prueba de verdad · blancas y silencios sin avisar',
             events=[{'pitch': 'B4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'h'},
                     {'pitch': 'F4', 'dur': 'q'}, R, {'pitch': 'C5', 'dur': 'q'},
                     {'pitch': 'A4', 'dur': 'h'}, {'pitch': 'G4', 'dur': 'q'},
                     {'pitch': 'E5', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}, R,
                     {'pitch': 'F4', 'dur': 'h.'}]),
    ],
    crono='¿Cuánto tardas en el ejercicio 3, sin fallos?',
    escucha=dict(
        sub='sin mirar el teclado · rodea con lápiz lo que oigas',
        profe=[
            ('A', 'Toca DOS notas sueltas, seguidas, con las teclas de la pieza (Do Re Mi Fa '
                  'Sol La Si). Que diga si la segunda sube, baja o es la misma.'),
            ('B', 'Toca las DOS MANOS a la vez en una posición de la pieza: la 2ª (Fa+Sol) y '
                  'la 3ª (Mi+Sol) son CERCA; la 6ª (Re+Si) y la 8ª (Do+Do) son LEJOS.'),
            ('C', 'Toca cuatro compases sueltos de la partitura. La parte A es el picoteo de '
                  'negras; la parte B es el vals, una larga y una corta.'),
            ('+', 'Y sin escribir nada: toca una nota, que la cante con la voz y luego la busque '
                  'en el piano. Es el que más oído da y no ocupa sitio en la hoja.'),
        ],
        filas=[
            dict(letra='A', titulo='¿Sube o baja?',
                 pista='la segunda nota respecto a la primera',
                 n=10, opciones=['↑', '↓', '=']),
            dict(letra='B', titulo='¿Cerca o lejos?',
                 pista='las dos manos a la vez · es el juego entero de esta pieza',
                 n=8, opciones=['cerca', 'lejos']),
            dict(letra='C', titulo='¿Parte A o parte B?',
                 pista='picoteo de negras, o vals de larga y corta',
                 n=6, opciones=['A', 'B']),
        ],
    ),
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
