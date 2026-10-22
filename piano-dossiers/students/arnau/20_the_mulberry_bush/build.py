import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'the-mulberry-bush-185807.4 manos.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song20 = dict(
  num=20, title='The Mulberry Bush', subtitle='Tradicional, arr. Regina Pratley (a 4 manos)',
  tonalidad='Do mayor', compas='6/8', tempo='Allegro, con balanceo', forma='Estrofa (a dúo)',
  dificultad='Nivel iniciación', manos='Balanceo de 6/8 + acordes, a 4 manos',
  la_cancion='El gran cierre de tu primer cuaderno: una canción de corro a 4 manos, para tocar junto al profesor.',
  difficult_cc='cc. 1–4', difficult_title='El balanceo de seis corcheas, en corro',
  reto='sentir el compás en dos grupos de tres, girando como en un corro.',
  truco='primero tu parte sola, muy despacio; luego a dúo con el profesor.',
  sabias_que='"The Mulberry Bush" es una canción de corro inglesa tradicional: los niños giran de la mano cantando alrededor de un árbol imaginario.',
  mini_staff_events=[{'pitch': p, 'dur': 'e', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3)]] +
                     [{'pitch': 'D4', 'dur': 'q.', 'number': 2}],
  time_sig=(6, 8),
  nivel_kicker='ARNAU · NIVEL INICIACIÓN · CANCIÓN 20 · ¡FINAL!',
  total_songs=20,
)

cfg20 = dict(
  kicker='ARNAU · CANCIÓN 20 · THE MULBERRY BUSH',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='The Mulberry Bush', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el balanceo de seis corcheas, en 6/8.',
  rhythm_events=[{'pitch': 'C4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'},
                 {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}],
  rhythm_time_sig=(6, 8),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song20)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg20)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Arnau_20_The_Mulberry_Bush.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
