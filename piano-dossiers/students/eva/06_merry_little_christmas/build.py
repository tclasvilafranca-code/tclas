import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', 'have-yourself-a-merry-little-christmas_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song6 = dict(
  num=6, title='Have Yourself a Merry Little Christmas', subtitle='Ralph Blane · Hugh Martin',
  tonalidad='Do mayor', compas='4/4', tempo='Tranquilo ♩≈92', forma='Estrofa',
  dificultad='Un reto de conversación', manos='Diálogo entre las manos',
  la_cancion='Un villancico clásico en Do mayor. Aquí el reto es un diálogo: una mano pregunta con una frase corta y la otra responde, como un coro.',
  difficult_cc='cc. 1–8', difficult_title='El diálogo entre las manos',
  reto='que la respuesta de la otra mano entre exactamente en su sitio, sin dudar ni adelantarse.',
  truco='cuenta el silencio de la mano que espera como si ya estuviera tocando por dentro.',
  sabias_que='La canción se escribió para la película "Meet Me in St. Louis" (1944); Frank Sinatra pidió después que se cambiara la letra original, más triste, por una más esperanzadora.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  checklist_items=['Encuentro DO y pongo bien los dedos.', 'La mano que espera cuenta el silencio por dentro.',
                    'La respuesta entra exactamente en su sitio.', 'Las dos manos dialogan sin dudar.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · DICIEMBRE',
  total_songs=21,
)

cfg6 = dict(
  kicker='EVA · DICIEMBRE · MERRY LITTLE CHRISTMAS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Have Yourself a Merry Little Christmas', song_key='Do mayor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Do mayor (I, IV, V...).',
  progression=['Do', 'Sol', 'Fa', 'Sol', 'Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras tranquilas y cálidas, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song6)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg6)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_06_Merry_Little_Christmas.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
