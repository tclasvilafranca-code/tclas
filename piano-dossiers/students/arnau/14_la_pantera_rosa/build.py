import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'La Pantera Rosa.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song14 = dict(
  num=14, title='La Pantera Rosa', subtitle='Henry Mancini, arr. escolar',
  tonalidad='Do mayor', compas='4/4', tempo='Con swing, sigiloso', forma='Estrofa con cromatismos',
  dificultad='Nivel iniciación, con toque extra', manos='Melodía cromática + acordes',
  la_cancion='El tema de dibujos animados más sigiloso que existe. Entre las notas normales aparecen notas "escondidas", con sostenido.',
  difficult_cc='cc. 1–8', difficult_title='El paso a escondidas: notas cromáticas',
  reto='tocar la nota "intrusa" sin dudar, como un paso de puntillas.',
  truco='toca cada nota escondida muy despacio antes de ponerla en tiempo.',
  sabias_que='Henry Mancini compuso este tema en 1963; ganó un Grammy y es uno de los temas más reconocibles del cine.',
  mini_staff_events=[{'pitch': 'C4', 'dur': 'q', 'number': 1}, {'pitch': 'C#4', 'dur': 'q'},
                     {'pitch': 'D4', 'dur': 'q', 'number': 2}, {'pitch': 'D4', 'dur': 'q', 'number': 2}] +
                     [{'pitch': 'E4', 'dur': 'w', 'number': 3}],
  nivel_kicker='ARNAU · NIVEL INICIACIÓN · CANCIÓN 14',
  total_songs=20,
)

cfg14 = dict(
  kicker='ARNAU · CANCIÓN 14 · LA PANTERA ROSA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='La Pantera Rosa', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: pasos suaves con alguna nota escondida, en 4/4.',
  rhythm_events=[{'pitch': 'C4', 'dur': 'q'}, {'pitch': 'C#4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song14)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg14)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Arnau_14_La_Pantera_Rosa.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
