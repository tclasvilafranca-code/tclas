import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'Baa Baa Black Sheep.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song3 = dict(
  num=3, title='Baa Baa Black Sheep', subtitle='Traditional · arr. Jim Paterson',
  tonalidad='Do mayor', compas='4/4', tempo='Alegre', forma='Estrofa',
  dificultad='Nivel iniciación', manos='Melodía + acordes que cambian',
  la_cancion='Una canción tradicional inglesa muy famosa, sobre una oveja negra. La izquierda cambia de acorde varias veces: Do, Fa y Sol.',
  difficult_cc='cc. 1–8', difficult_title='El cambio de acorde: Do–Fa–Sol',
  reto='cambiar de acorde con la izquierda sin que la melodía de la derecha se pare.',
  truco='di en voz alta el nombre del acorde un poco antes de tocarlo.',
  sabias_que='La melodía de "Baa Baa Black Sheep" es la misma que la de "Twinkle Twinkle Little Star" y la canción del abecedario en inglés.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('C4', 1), ('E4', 3), ('E4', 3)]] +
                     [{'pitch': 'G4', 'dur': 'h', 'number': 5}, {'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='ARNAU · NIVEL INICIACIÓN · CANCIÓN 3',
  total_songs=20,
)

cfg3 = dict(
  kicker='ARNAU · CANCIÓN 3 · BAA BAA BLACK SHEEP',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Baa Baa Black Sheep', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: notas repetidas y un salto, en 4/4.',
  rhythm_events=[{'pitch': 'C4', 'dur': 'q'}, {'pitch': 'C4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song3)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg3)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Arnau_03_Baa_Baa_Black_Sheep.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
