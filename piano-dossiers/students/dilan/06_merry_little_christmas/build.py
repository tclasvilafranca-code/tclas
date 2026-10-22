import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'have-yourself-a-merry-little-christmas_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song6 = dict(
  num=6, title='Have Yourself a Merry Little Christmas', subtitle='Ralph Blane · Hugh Martin, villancico clásico',
  tonalidad='Do mayor', compas='4/4', tempo='Tranquilo ♩≈66', forma='Estrofa',
  dificultad='Un reto de armonía', manos='Melodía en acordes + acordes',
  la_cancion='Un villancico clásico de Hollywood, en Do mayor. La mano derecha no toca una melodía suelta: la toca en pequeños acordes, como un coro.',
  difficult_cc='cc. 1–8', difficult_title='Melodía armonizada',
  reto='tocar los pequeños acordes de la melodía sin que suenen duros ni desiguales entre sí.',
  truco='toca primero solo la nota de arriba (la melodía real), y cuando la sepas de memoria, añade la nota de abajo.',
  sabias_que='Esta canción se estrenó en la película "Meet Me in St. Louis" (1944), cantada por Judy Garland. La letra original era mucho más triste; se suavizó para la versión que todos cantamos hoy.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('E4', 3), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · DICIEMBRE',
  total_songs=24,
)

cfg6 = dict(
  kicker='DILAN · DICIEMBRE · MERRY LITTLE CHRISTMAS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Have Yourself a Merry Little Christmas', song_key='Do mayor',
  progression_desc='Estos acordes sostienen el villancico. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras tranquilas, todas iguales, como un villancico cantado despacio.',
  rhythm_events=[{'pitch': 'G4', 'dur': 'q'}] * 7 + [{'pitch': 'G4', 'dur': 'q'}],
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

    out_path = os.path.join(OUT_DIR, 'Dilan_06_Merry_Little_Christmas.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
