# -*- coding: utf-8 -*-
"""Dosier completo de Can't Help Falling in Love (Dilan): las 6 paginas."""
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
import build_ficha_d02 as bf, build_calentamiento_d02 as bc
import build_lectura_d02 as bl, build_piano_d02 as bp

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = bf.SOURCE_PDF
OUT = os.path.join(OUT_DIR, 'Dilan_02_CantHelp_CUADERNO.pdf')


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    qr = os.path.join(OUT_DIR, '_qr_t2.png')
    segno.make(bf.YT_URL, error='m').save(qr, scale=10, border=2,
                                          dark='#1A2332', light='#F3F1EA')
    bf.CFG['qr']['png'] = qr
    tmp = os.path.join(HERE, '_full2.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_ficha(c, bf.CFG); build_calentamiento(c, bc.CFG)
    build_lectura(c, bl.CFG); build_piano(c, bp.PAG1); build_piano(c, bp.PAG2)
    c.save()
    wr = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages: wr.add_page(p)
    for p in PdfReader(tmp).pages: wr.add_page(p)
    with open(OUT, 'wb') as f: wr.write(f)
    os.remove(tmp); os.remove(qr)
    print('generated', OUT, '·', len(PdfReader(OUT).pages), 'paginas')


if __name__ == '__main__':
    main()
