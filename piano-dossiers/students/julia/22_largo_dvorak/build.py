import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JULIA', 'Largo-Sinfonia 5 Dvorak.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song22 = dict(
  num=22, title='Largo - Sinfonía nº5 Op. 95', subtitle='"Sinfonía del Nuevo Mundo" · A. Dvořák, arr. A.C. Escobés',
  tonalidad='Do mayor', compas='4/4', tempo='Largo', forma='Estrofa con frases largas',
  dificultad='Nivel inicial, con toque extra', manos='Melodía en frases largas + acordes sostenidos',
  la_cancion='El famoso Largo de la Sinfonía del Nuevo Mundo, de Dvořák, en Do mayor. La melodía respira en frases muy largas que cruzan de un compás a otro sin cortarse.',
  difficult_cc='cc. 1–4', difficult_title='La frase larga que no se corta',
  reto='mantener el sonido conectado durante toda la frase, sin cortar entre un compás y el siguiente.',
  truco='canta la frase con la voz, sin respirar hasta el final: así sentirás dónde no debes cortar el sonido.',
  sabias_que='Este Largo, con su famosa melodía, se conoce también como "Goin\' Home" y es una de las piezas más queridas de Dvořák.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JULIA · NIVEL INICIAL · JUNIO',
  total_songs=24,
)

cfg22 = dict(
  kicker='JULIA · JUNIO · LARGO (DVORÁK)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Largo (Dvořák)', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la frase larga, con puntillo, en 4/4.',
  rhythm_events=([{'pitch': 'G4', 'dur': 'q.'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'h'}] * 2),
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song22)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg22)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Julia_22_Largo_Dvorak.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
