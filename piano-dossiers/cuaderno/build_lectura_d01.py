# -*- coding: utf-8 -*-
"""Agudeza visual y auditiva de El Cisne para Dilan (nivel avanzado).

   Qué cambia respecto a un nivel de iniciación:
     - se lee en las DOS claves, y con armadura: los Fa son ♯ sin que se avise
     - aparecen alteraciones accidentales sueltas (♮ y ♯), como en la sección
       central de la pieza
     - la parte de oído ya no pregunta agudo/grave: pregunta modo, grado y
       tipo de cadencia, que es lo que esta pieza usa de verdad
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from hoja_lectura import build_lectura

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN', 'the-swan.pdf')

SOL = 'Sol mayor'


def q(*n):
    return [{'pitch': p, 'dur': 'q'} for p in n]


CFG = dict(
    kicker='Dilan · canción 1 · El Cisne',
    page_num=6,
    time_sig=(3, 4),
    key_sig=SOL,
    intro='Ni una nota al piano en esta hoja. Arriba se lee en voz alta, en las dos claves y con '
          'armadura de Sol. Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
    sub_leer='di el nombre en voz alta · la armadura manda: todos los Fa son ♯',
    chuleta_clef='bass',
    chuleta_titulo='EL REGISTRO DE LA MANO IZQUIERDA (CLAVE DE FA)',
    chuleta_pitches=['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3'],
    chuleta_nombres=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa♯', 'Sol', 'La', 'Si'],
    ejercicios=[
        dict(num=1, titulo='Clave de Fa', clef='bass',
             pista='el registro donde vive el acompañamiento · orden irregular a propósito',
             events=q('D3', 'G2', 'B3', 'E3', 'A2', 'F3', 'C3', 'B2', 'G3', 'D3',
                      'A3', 'E3', 'G2', 'F3', 'C3')),
        dict(num=2, titulo='Clave de Sol',
             pista='el registro de la melodía · cuidado con las líneas adicionales',
             events=q('G5', 'B4', 'E5', 'A4', 'F5', 'D5', 'G4', 'C5', 'E4', 'F4',
                      'B4', 'G5', 'D5', 'A4', 'E5')),
        dict(num=3, titulo='Con alteraciones sueltas',
             pista='como la sección central · un ♯ o un ♮ solo vale hasta la barra de compás',
             events=[{'pitch': 'B4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'h'},
                     {'pitch': 'F5', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'},
                     {'pitch': 'C#5', 'dur': 'q'}, {'pitch': 'D5', 'dur': 'h'},
                     {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'E5', 'dur': 'q'},
                     {'pitch': 'D5', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'},
                     {'pitch': 'G4', 'dur': 'h.'}]),
    ],
    crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
    escucha=dict(
        sub='sin mirar el teclado · rodea con lápiz lo que oigas',
        profe=[
            ('A', 'Toca una tríada, en cualquier registro. Que diga si es MAYOR o MENOR. '
                  'Alterna sin patrón para que no lo adivine.'),
            ('B', 'En Sol mayor, toca el acorde de Sol (I), Do (IV) o Re (V), siempre después '
                  'de dar el Sol como referencia. Que identifique el grado.'),
            ('C', 'Toca dos acordes seguidos: si acabas en Sol suena CERRADA, si acabas en Re '
                  'queda ABIERTA, esperando. Es la diferencia entre punto y coma.'),
            ('+', 'Y sin escribir nada: toca los cuatro primeros compases de la izquierda y que '
                  'cante la melodía por encima. Si puede cantarla, es que ya la oye separada.'),
        ],
        filas=[
            dict(letra='A', titulo='¿Mayor o menor?',
                 pista='el acorde entero, de una vez',
                 n=10, opciones=['M', 'm']),
            dict(letra='B', titulo='¿Qué grado?',
                 pista='en Sol mayor · I = Sol, IV = Do, V = Re',
                 n=8, opciones=['I', 'IV', 'V']),
            dict(letra='C', titulo='¿Cerrada o abierta?',
                 pista='acaba en la tónica, o se queda esperando en la dominante',
                 n=6, opciones=['cerrada', 'abierta']),
        ],
    ),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = os.path.join(HERE, '_ld_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_lectura(c, CFG)
    c.save()
    wr = PdfWriter()
    for p in PdfReader(tmp).pages: wr.add_page(p)
    for p in PdfReader(SOURCE_PDF).pages: wr.add_page(p)
    out = os.path.join(OUT_DIR, 'Dilan_01_Lectura_y_Partitura.pdf')
    with open(out, 'wb') as f: wr.write(f)
    os.remove(tmp)
    print('generated', out)


if __name__ == '__main__':
    main()
