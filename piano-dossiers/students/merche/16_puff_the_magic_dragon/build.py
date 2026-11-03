import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'Puff era un Drac Magic.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song16 = dict(
  num=16, title='Puff the Magic Dragon', subtitle='Peter, Paul and Mary · arr. Eric Moore',
  tonalidad='Do mayor', compas='4/4', tempo='Moderato', forma='Estrofa',
  dificultad='Nivel básico', manos='Melodía + bajo en octavas',
  la_cancion='La entrañable canción "Puff the Magic Dragon", en Do mayor. El acompañamiento de la izquierda toca la misma nota dos veces a la vez, una octava de distancia: hoy trabajamos alcanzar esa octava sin tensión.',
  difficult_cc='cc. 1–4', difficult_title='El bajo en octavas: alcanzar arriba y abajo a la vez',
  reto='estirar la mano para alcanzar limpiamente las dos notas de la octava, sin tensar el brazo ni la muñeca.',
  truco='practica la octava sola, soltando y relajando la mano entre cada repetición, para no acumular tensión.',
  sabias_que='"Puff the Magic Dragon" (1963), de Peter, Paul and Mary, está basada en un poema de Leonard Lipton sobre un dragón mágico y su amigo de la infancia.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · FEBRERO',
  total_songs=28,
)

cfg16 = dict(
  kicker='MERCÈ · FEBRERO · PUFF THE MAGIC DRAGON',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada octava del bajo: nómbrala (Do, Fa, Sol...) según su nota.',
  chords=[['C3', 'C4'], ['F2', 'F3'], ['G2', 'G3'], ['C3', 'C4']],
  song_title='Puff the Magic Dragon', song_key='Do mayor',
  progression_desc='Estos son los bajos de la canción, en octavas. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la melodía sobre la octava sostenida, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
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

    out_path = os.path.join(OUT_DIR, 'Merce_16_Puff_The_Magic_Dragon.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
