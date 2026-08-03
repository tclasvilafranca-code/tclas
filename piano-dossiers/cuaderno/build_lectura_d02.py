# -*- coding: utf-8 -*-
"""Agudeza visual y auditiva de Can't Help Falling in Love (Dilan, avanzado)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from hoja_lectura import build_lectura

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                          ' cant-help-falling-in-love-.pdf')
RE = 'Re mayor'
R = {'rest': True, 'dur': 'q'}


def q(*n):
    return [{'pitch': p, 'dur': 'q'} for p in n]


CFG = dict(
    kicker='Dilan · canción 2 · Can’t Help Falling in Love',
    page_num=6, time_sig=(3, 4), key_sig=RE,
    intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con armadura de Re. '
          'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
    sub_leer='di el nombre en voz alta · la armadura manda: Fa♯ y Do♯ siempre',
    chuleta_clef='bass',
    chuleta_titulo='EL REGISTRO DEL ACOMPAÑAMIENTO (CLAVE DE FA)',
    chuleta_pitches=['B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4'],
    chuleta_nombres=['Si', 'Do♯', 'Re', 'Mi', 'Fa♯', 'Sol', 'La', 'Si', 'Do♯', 'Re'],
    ejercicios=[
        dict(num=1, titulo='Clave de Fa', clef='bass',
             pista='donde vive el acorde roto · orden irregular a propósito',
             events=q('D3', 'A3', 'F3', 'B2', 'D4', 'C4', 'E3', 'G3', 'A2', 'F3',
                      'B3', 'D3', 'C3', 'A3', 'E3')),
        dict(num=2, titulo='Clave de Sol',
             pista='donde vive la melodía · una nota por compás, pero hay que encontrarla',
             events=q('D4', 'A4', 'F4', 'D5', 'B4', 'G4', 'E4', 'C5', 'A4', 'F4',
                      'D4', 'B4', 'E5', 'G4', 'C5')),
        dict(num=3, titulo='Con alteraciones sueltas',
             pista='la sección F♯m – C♯7 del final sale de la tonalidad · el ♮ dura hasta la barra',
             events=[{'pitch': 'A4', 'dur': 'q'}, {'pitch': 'G#4', 'dur': 'h'},
                     {'pitch': 'B4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'},
                     {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'E5', 'dur': 'h'},
                     {'pitch': 'D5', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'},
                     {'pitch': 'F4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'},
                     {'pitch': 'D4', 'dur': 'h.'}]),
    ],
    crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
    escucha=dict(
        sub='sin mirar el teclado · rodea con lápiz lo que oigas',
        profe=[
            ('A', 'Toca una tríada suelta. Que diga si es MAYOR o MENOR: la canción alterna las dos '
                  'todo el rato (Re, Fa♯m, Sim…).'),
            ('B', 'En Re mayor, y dando siempre el Re de referencia antes, toca el acorde de Re (I), '
                  'Sol (IV) o La (V). Que identifique el grado.'),
            ('C', 'Toca el acorde roto de un compás cualquiera. Que diga si empieza por la '
                  'FUNDAMENTAL (como en la pieza) o si lo has empezado por la tercera o la quinta.'),
            ('+', 'Y sin escribir: toca la izquierda de los cc. 1–3 y que cante la melodía encima.'),
        ],
        filas=[
            dict(letra='A', titulo='¿Mayor o menor?', pista='el acorde entero, de una vez',
                 n=10, opciones=['M', 'm']),
            dict(letra='B', titulo='¿Qué grado?', pista='en Re mayor · I = Re, IV = Sol, V = La',
                 n=8, opciones=['I', 'IV', 'V']),
            dict(letra='C', titulo='¿Empieza por la fundamental?', pista='el acorde roto, desde abajo o desde en medio',
                 n=6, opciones=['sí', 'no']),
        ],
    ),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = os.path.join(HERE, '_l2_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H)); build_lectura(c, CFG); c.save()
    wr = PdfWriter()
    for p in PdfReader(tmp).pages: wr.add_page(p)
    for p in PdfReader(SOURCE_PDF).pages: wr.add_page(p)
    out = os.path.join(OUT_DIR, 'Dilan_02_Lectura_y_Partitura.pdf')
    with open(out, 'wb') as f: wr.write(f)
    os.remove(tmp); print('generated', out)


if __name__ == '__main__':
    main()
