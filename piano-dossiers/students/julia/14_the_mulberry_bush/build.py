import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JULIA', 'THE MULBERRY BUSH.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song14 = dict(
  num=14, title='The Mulberry Bush', subtitle='Tradicional, arr. Regina Pratley (a 4 manos)',
  tonalidad='Do mayor', compas='6/8', tempo='Alegre, con balanceo', forma='Estrofa (a dúo)',
  dificultad='Nivel inicial', manos='Balanceo de 6/8 + acordes, a 4 manos',
  la_cancion='Una canción tradicional de corro infantil, en Do mayor y compás de 6/8, a 4 manos. Hoy nos balanceamos como en un columpio.',
  difficult_cc='cc. 1–4', difficult_title='El balanceo de seis corcheas, como un columpio',
  reto='sentir el compás de 6/8 en dos grandes impulsos, sin contar las seis corcheas una a una.',
  truco='balancéate suavemente con el cuerpo, como en un columpio, mientras cuentas "uno, dos".',
  sabias_que='"The Mulberry Bush" es una canción de corro infantil inglesa que se canta desde hace más de 200 años.',
  mini_staff_events=[{'pitch': p, 'dur': 'e', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'q.', 'number': 1}],
  nivel_kicker='JULIA · NIVEL INICIAL · ENERO',
  total_songs=24,
)

cfg14 = dict(
  kicker='JULIA · ENERO · THE MULBERRY BUSH',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='The Mulberry Bush', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: dos impulsos con puntillo por compás, en 6/8.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q.'}] * 4,
  rhythm_time_sig=(6, 8),
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

    out_path = os.path.join(OUT_DIR, 'Julia_14_The_Mulberry_Bush.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
