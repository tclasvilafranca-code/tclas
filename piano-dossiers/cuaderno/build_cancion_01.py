# -*- coding: utf-8 -*-
"""Dosier completo de UNA canción: las 6 páginas en el orden definitivo.

       1  La partitura original
       2  Ficha de la partitura      (qué es esta pieza)
       3  Calentamiento              (antes de abrirla)
       4  Agudeza visual y auditiva  (ojo y oído, sin tocar)
       5  Al piano · por partes      (desmontar)
       6  Al piano · montarla        (reensamblar + velocidad)

   Este es el archivo que se imprime. Los build_*.py sueltos siguen existiendo
   para trabajar una hoja aislada sin regenerar el resto.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
import segno
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from ficha_info import build_ficha
from hoja_calentamiento import build_calentamiento
from hoja_lectura import build_lectura
from hoja_piano import build_piano

import build_ficha_01 as bf
import build_calentamiento_01 as bc
import build_lectura_01 as bl
import build_piano_01 as bp

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU', ' Chopsticks.pdf')
OUT = os.path.join(OUT_DIR, 'Arnau_01_Chopsticks_CUADERNO.pdf')


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    qr_png = os.path.join(OUT_DIR, '_qr_tmp.png')
    segno.make(bf.YT_URL, error='m').save(qr_png, scale=10, border=2,
                                          dark='#1A2332', light='#F3F1EA')
    bf.CFG['qr']['png'] = qr_png

    tmp = os.path.join(HERE, '_cancion_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_ficha(c, bf.CFG)
    build_calentamiento(c, bc.CFG)
    build_lectura(c, bl.CFG)
    build_piano(c, bp.PAG1)
    build_piano(c, bp.PAG2)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:      # 1 · la partitura va delante
        writer.add_page(p)
    for p in PdfReader(tmp).pages:             # 2-6 · las cinco hojas
        writer.add_page(p)
    with open(OUT, 'wb') as f:
        writer.write(f)
    os.remove(tmp)
    os.remove(qr_png)
    print('generated', OUT, '·', len(PdfReader(OUT).pages), 'páginas')


if __name__ == '__main__':
    main()
