import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'Hay un amigo en mi.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song12 = dict(
  num=12, title="You've Got a Friend in Me", subtitle='Toy Story · arr. Megan Harper',
  tonalidad='Do mayor', compas='4/4', tempo='Moderato', forma='Estrofa con acordes prestados',
  dificultad='Nivel básico', manos='Melodía + bajo con acordes prestados',
  la_cancion='El clásico tema de Toy Story, en Do mayor. El bajo se aleja a veces a un acorde con una nota alterada, fuera de la tonalidad, y después vuelve a casa: hoy reconocemos ese "acorde prestado".',
  difficult_cc='cc. 2, 6, 10', difficult_title='Los acordes prestados: el bajo se aleja y vuelve',
  reto='reconocer el momento en que el bajo toca una nota alterada y sentir cómo la música regresa después a Do mayor.',
  truco='fíjate en la mano izquierda: si aparece un bemol o un sostenido inesperado, sabes que es un acorde prestado.',
  sabias_que='"You\'ve Got a Friend in Me" (1995), de Randy Newman, fue la primera canción compuesta para una película de Pixar y hoy es un himno a la amistad.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · DICIEMBRE',
  total_songs=28,
)

cfg12 = dict(
  kicker='MERCÈ · DICIEMBRE · HAY UN AMIGO EN MÍ',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol, Sib...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['Bb2', 'D3', 'F3']],
  song_title='You\'ve Got a Friend in Me', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. El Sib es un acorde prestado, fuera de Do mayor: escribe su función (I, IV, V o "prestado").',
  progression=['Do', 'Sib (prestado)', 'Do', 'Fa'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: la melodía sobre el acorde prestado, en 4/4.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'q'}, {'pitch': 'F4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}] * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song12)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg12)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_12_Hay_Un_Amigo_En_Mi.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
