import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_clase import page_clase, page_tarjeta_casa, W, H

HERE = os.path.dirname(__file__)
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', ' Chopsticks.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp_path = os.path.join(HERE, '_tmp.pdf')
    c = canvas.Canvas(tmp_path, pagesize=(W, H))
    page_clase(c)
    page_tarjeta_casa(c)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for p in PdfReader(tmp_path).pages:
        writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'PREVIEW_Arnau_01_Chopsticks_v2.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)
    os.remove(tmp_path)
    print('generated', out_path)


if __name__ == '__main__':
    main()
