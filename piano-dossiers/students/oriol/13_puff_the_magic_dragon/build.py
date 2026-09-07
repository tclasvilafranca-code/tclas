import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ORIOL', 'Copia de puff-the-magic-dragon.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song13 = dict(
  num=13, title='Puff the Magic Dragon', subtitle='Peter, Paul and Mary · arr. Eric Moore',
  tonalidad='Do mayor', compas='4/4', tempo='Moderato', forma='Estrofa',
  dificultad='Nivel medio', manos='Melodía + acordes, sin complicarse',
  la_cancion='La entrañable canción folk de Peter, Paul and Mary, en Do mayor. Hoy nos fijamos en cómo la melodía dialoga: una frase pregunta, la siguiente responde.',
  difficult_cc='cc. 1–8', difficult_title='La frase que pregunta y responde: escucha el diálogo',
  reto='distinguir con el oído cuándo la frase "pregunta" (sube) y cuándo "responde" (baja y se calma).',
  truco='imagina una conversación: toca la primera frase como si preguntaras, y la segunda como si respondieras con calma.',
  sabias_que='"Puff, the Magic Dragon" (1963) de Peter, Paul and Mary está basada en un poema y, pese a rumores, sus autores siempre negaron que tratara sobre drogas: es simplemente sobre crecer y dejar atrás la infancia.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='ORIOL · NIVEL MEDIO · MARZO',
  total_songs=15,
)

cfg13 = dict(
  kicker='ORIOL · MARZO · PUFF THE MAGIC DRAGON',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Puff the Magic Dragon', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la frase que pregunta, en cuatro por cuatro.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 4,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song13)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg13)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Oriol_13_Puff_The_Magic_Dragon.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
