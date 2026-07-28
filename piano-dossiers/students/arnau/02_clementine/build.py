import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'Clementine.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song2 = dict(
  num=2, title='Clementine (Found a Peanut)', subtitle='Primer Level · arr. Gilbert DeBenedetti',
  tonalidad='Do mayor', compas='3/4', tempo='Con cariño, "tongue in cheek"', forma='Estrofa',
  dificultad='Nivel iniciación', manos='Melodía en la derecha + un alcance puntual',
  la_cancion='Una canción clásica americana sobre una chica llamada Clementine, medio en broma. Casi toda la melodía va con tu mano derecha.',
  difficult_cc='c. 2 y c. 10', difficult_title='El estiramiento de la izquierda',
  reto='que la izquierda baje a buscar una nota grave sin tensarse ni golpear.',
  truco='mueve todo el brazo hacia la nota, no solo el dedo — así no fuerzas una mano pequeña.',
  sabias_que='La melodía de "Clementine" también se usa para la canción "Found a Peanut", que canta la misma música con una letra distinta y muy graciosa.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('E4', 3), ('G4', 5), ('E4', 3), ('C4', 1)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='ARNAU · NIVEL INICIACIÓN · CANCIÓN 2',
  total_songs=20,
)

cfg2 = dict(
  kicker='ARNAU · CANCIÓN 2 · CLEMENTINE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Clementine', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: notas que caminan tranquilas, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'C4', 'dur': 'q'}, {'pitch': 'C4', 'dur': 'h.'}],
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song2)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg2)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Arnau_02_Clementine.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
