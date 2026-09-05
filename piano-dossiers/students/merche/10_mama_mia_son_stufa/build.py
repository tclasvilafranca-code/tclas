import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', '-mama-mia-son-stufa.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song10 = dict(
  num=10, title='Mama Mia, Mi Son Stufa', subtitle='Canción popular italiana · arr. Regina Pratley',
  tonalidad='Do mayor', compas='4/4', tempo='Allegro con brio', forma='Estrofa (a 4 manos)',
  dificultad='Nivel básico', manos='Melodía enérgica + acompañamiento en bloque, a 4 manos',
  la_cancion='Una canción popular italiana a cuatro manos, en Do mayor, marcada "Allegro con brio": un tempo vivo y con energía que hoy trabajamos con control.',
  difficult_cc='cc. 1–4', difficult_title='Allegro con brio: el carácter enérgico del tempo',
  reto='mantener la energía y la velocidad del pulso sin precipitarte ni perder claridad en ninguna nota.',
  truco='practica primero muy despacio, y ve acelerando poco a poco hasta sentir el "brio" sin perder el control.',
  sabias_que='"Allegro con brio" es una indicación italiana muy usada por compositores como Beethoven: significa "rápido, con vivacidad y energía".',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · DICIEMBRE',
  total_songs=28,
)

cfg10 = dict(
  kicker='MERCÈ · DICIEMBRE · MAMA MIA, MI SON STUFA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Mama Mia, Mi Son Stufa', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la frase enérgica, en 4/4.',
  rhythm_events=[{'pitch': 'G4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song10)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg10)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_10_Mama_Mia_Son_Stufa.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
