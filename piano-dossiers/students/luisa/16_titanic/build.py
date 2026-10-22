import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'LUISA', 'Titanic easy.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song16 = dict(
  num=16, title='Titanic (Mi Corazón Sigue)', subtitle='James Horner · arr. Ana Cristina Escobés',
  tonalidad='Do mayor', compas='2/4', tempo='Adagio', forma='Estrofa',
  dificultad='Nivel hobby', manos='Melodía + acordes, sin complicarse',
  la_cancion='El famoso tema de la película Titanic, en Do mayor. Es una melodía tranquila y un poco soñadora, como el mar: hoy solo hay que tocarla despacio, con calma.',
  difficult_cc='cc. 1–8', difficult_title='La canción del mar: despacio, con calma',
  reto='tocar despacio y con calma, sin ponerte nerviosa por hacerlo perfecto.',
  truco='imagina el mar tranquilo mientras tocas: deja que la melodía flote, sin prisa.',
  sabias_que='"My Heart Will Go On" (1997), de James Horner, ganó el Óscar a la Mejor Canción Original y es el tema principal de la película Titanic.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]],
  nivel_kicker='LUISA · NIVEL HOBBY · ENERO',
  total_songs=28,
)

cfg16 = dict(
  kicker='LUISA · ENERO · TITANIC',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Titanic', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la melodía tranquila, en 2/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h'}] * 4,
  rhythm_time_sig=(2, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song16)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg16)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Luisa_16_Titanic.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
