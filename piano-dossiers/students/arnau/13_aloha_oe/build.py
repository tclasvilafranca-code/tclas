import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'Aloha oe.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song13 = dict(
  num=13, title='Aloha Oe', subtitle='Música de la Reina Liliuokalani, arr. Regina Pratley',
  tonalidad='Do mayor', compas='Compás partido (alla breve)', tempo='Con moto', forma='Estrofa',
  dificultad='Nivel iniciación, con toque extra', manos='Melodía con notas largas + acordes',
  la_cancion='Una canción hawaiana muy bonita, compuesta por una reina. Se cuenta a 2, no a 4: es un compás partido.',
  difficult_cc='cc. 1–12', difficult_title='El compás partido: se cuenta a 2',
  reto='sentir solo dos pulsos grandes por compás, no cuatro pequeños.',
  truco='balancea la mano libre marcando solo "1, 2" mientras escuchas.',
  sabias_que='"Aloha Oe" la compuso la última reina de Hawái, Liliuokalani, en 1878, y hoy es casi un segundo himno de las islas.',
  mini_staff_events=[{'pitch': p, 'dur': 'h', 'number': n} for p, n in
                      [('C4', 1), ('E4', 3)]] +
                     [{'pitch': 'G4', 'dur': 'w', 'number': 5}],
  time_sig=(2, 2),
  nivel_kicker='ARNAU · NIVEL INICIACIÓN · CANCIÓN 13',
  total_songs=20,
)

cfg13 = dict(
  kicker='ARNAU · CANCIÓN 13 · ALOHA OE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Aloha Oe', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: dos pulsos grandes por compás.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h'}, {'pitch': 'G4', 'dur': 'h'}],
  rhythm_time_sig=(2, 2),
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

    out_path = os.path.join(OUT_DIR, 'Arnau_13_Aloha_Oe.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
