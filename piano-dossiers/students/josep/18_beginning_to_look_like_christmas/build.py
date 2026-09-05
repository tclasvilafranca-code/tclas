import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'its-beginning-to-look-a-lot-like-christmas-piano-duet.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song18 = dict(
  num=18, title="It's Beginning to Look a Lot Like Christmas", subtitle='Meredith Willson (a 4 manos)',
  tonalidad='Do mayor', compas='6/8', tempo='Con vaivén ♩.≈100', forma='Estrofa (a dúo)',
  dificultad='Un reto de compás', manos='Melodía + acordes, a 4 manos',
  la_cancion='Un villancico clásico en Do mayor y compás de 6/8, pensado para tocar a 4 manos. El reto es de compás: sentir el pulso grande de dos, no seis corcheas sueltas.',
  difficult_cc='cc. 1–8', difficult_title='Contar en dos, no en seis: el pulso grande de 6/8',
  reto='sentir cada compás como dos pulsos grandes, en vez de contar las seis corcheas una a una.',
  truco='balancea el cuerpo suavemente en dos, como un vals lento, mientras cuentas por dentro "uno-dos".',
  sabias_que='"It\'s Beginning to Look a Lot Like Christmas" (1951) de Meredith Willson ha sido versionada por más de 300 artistas distintos.',
  mini_staff_events=[{'pitch': p, 'dur': 'e', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'q.', 'number': 1}],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · MAYO',
  total_songs=22,
)

cfg18 = dict(
  kicker='JOSEP · MAYO · IT’S BEGINNING TO LOOK A LOT LIKE CHRISTMAS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title="It's Beginning to Look a Lot Like Christmas", song_key='Do mayor',
  progression_desc='Estos son los acordes de la pieza. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: dos pulsos grandes con puntillo por compás, en 6/8.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q.'}] * 4,
  rhythm_time_sig=(6, 8),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song18)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg18)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_18_Beginning_To_Look_Like_Christmas.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
