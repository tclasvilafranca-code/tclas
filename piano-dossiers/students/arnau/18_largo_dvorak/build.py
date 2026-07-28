import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'Largo-Sinfonia 5 Dvorak.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song18 = dict(
  num=18, title='Largo - Sinfonía nº5 Op. 95', subtitle='"Sinfonía del Nuevo Mundo" · A. Dvořák, arr. A.C. Escobés',
  tonalidad='Do mayor', compas='4/4', tempo='Largo', forma='Estrofa con frases largas',
  dificultad='Reto motivador (nivel básico)', manos='Melodía en frases largas + acordes sostenidos',
  la_cancion='Nuestro primer contacto con música clásica "de verdad", de una de las sinfonías más famosas del mundo. Las frases son largas y no se cortan.',
  difficult_cc='cc. 1–4', difficult_title='La frase larga que no se corta',
  reto='cantar mentalmente toda la frase de un tirón, sin pausas a mitad camino.',
  truco='canta la frase entera en voz alta antes de tocarla al piano.',
  sabias_que='Este tema es tan famoso que se conoce también como "Goin\' Home"; Dvořák lo compuso en Nueva York, inspirado en melodías populares americanas.',
  mini_staff_events=[{'pitch': p, 'dur': 'h', 'number': n} for p, n in
                      [('C4', 1), ('E4', 3)]] +
                     [{'pitch': 'G4', 'dur': 'w', 'number': 5}],
  nivel_kicker='ARNAU · RETO MOTIVADOR · CANCIÓN 18',
  total_songs=20,
)

cfg18 = dict(
  kicker='ARNAU · CANCIÓN 18 · LARGO (DVOŘÁK)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Largo (Dvořák)', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: notas larguísimas y sostenidas, en 4/4.',
  rhythm_events=[{'pitch': 'G4', 'dur': 'h'}, {'pitch': 'A4', 'dur': 'h'}],
  rhythm_time_sig=(4, 4),
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

    out_path = os.path.join(OUT_DIR, 'Arnau_18_Largo_Dvorak.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
