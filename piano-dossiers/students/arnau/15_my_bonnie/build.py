import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'MyBonnie.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song15 = dict(
  num=15, title='My Bonnie Lies Over the Ocean', subtitle='Level Two · arr. Gilbert DeBenedetti',
  tonalidad='Do mayor', compas='3/4', tempo='Slowly, longingly', forma='Estrofa',
  dificultad='Reto motivador (nivel básico)', manos='Cambio de posición + cruce de manos',
  la_cancion='Nuestro primer reto de nivel básico: la izquierda cambia de posición a mitad de frase, y al final incluso "visita" una nota alta.',
  difficult_cc='Toda la pieza', difficult_title='El cambio de posición, izquierda',
  reto='que la izquierda encuentre su nuevo sitio sin mirar y sin perder el pulso.',
  truco='marca con lápiz en la partitura el compás exacto donde cambia la posición.',
  sabias_que='"My Bonnie" es una canción escocesa tradicional del siglo XIX; "Bonnie" significa "guapa" o "querida" en escocés.',
  mini_staff_events=[{'pitch': p, 'dur': 'h.', 'number': n} for p, n in
                      [('C4', 1), ('E4', 3)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 5}],
  nivel_kicker='ARNAU · RETO MOTIVADOR · CANCIÓN 15',
  total_songs=20,
)

cfg15 = dict(
  kicker='ARNAU · CANCIÓN 15 · MY BONNIE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='My Bonnie', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: notas largas y tranquilas, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h.'}, {'pitch': 'D4', 'dur': 'h.'}],
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song15)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg15)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Arnau_15_My_Bonnie.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
