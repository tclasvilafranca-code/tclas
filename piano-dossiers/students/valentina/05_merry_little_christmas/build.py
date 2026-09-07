import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', ' have-yourself-a-merry-little-christmas_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song5 = dict(
  num=5, title='Have Yourself a Merry Little Christmas', subtitle='Ralph Blane · Hugh Martin, villancico clásico',
  tonalidad='Do mayor', compas='4/4', tempo='Tranquilo ♩≈66', forma='Estrofa',
  dificultad='Nivel medio', manos='Dos voces en la derecha + acordes',
  la_cancion='Un villancico clásico en Do mayor. Hoy: dos voces conviviendo dentro de una sola mano, una quieta y otra que se mueve.',
  difficult_cc='cc. 1–8', difficult_title='Las voces internas: escuchar más de una línea a la vez',
  reto='distinguir con el oído la voz que se queda quieta de la que se mueve, sin que se mezclen.',
  truco='toca primero cada voz por separado, cantándola en voz alta, antes de juntarlas en la misma mano.',
  sabias_que='"Have Yourself a Merry Little Christmas" (1944) se escribió para la película "Meet Me in St. Louis" y Frank Sinatra pidió que se cambiara su letra original, más triste, por una más esperanzadora.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='VALENTINA · NIVEL MEDIO · NOVIEMBRE',
  total_songs=22,
)

cfg5 = dict(
  kicker='VALENTINA · NOVIEMBRE · HAVE YOURSELF A MERRY LITTLE CHRISTMAS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['F2', 'A2', 'C3']],
  song_title='Have Yourself a Merry Little Christmas', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: las dos voces en negras, en 4/4.',
  rhythm_events=[{'pitches': p, 'dur': 'q'} for p in [['C4', 'G4'], ['D4', 'G4'], ['E4', 'G4'], ['D4', 'G4']]],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song5)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg5)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_05_Merry_Little_Christmas.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
