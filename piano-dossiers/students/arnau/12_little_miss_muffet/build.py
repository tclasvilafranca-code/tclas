import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'Little Miss Muffet.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song12 = dict(
  num=12, title='Little Miss Muffet', subtitle='Traditional · arr. Jim Paterson',
  tonalidad='Fa mayor', compas='6/8', tempo='Con balanceo', forma='Estrofa',
  dificultad='Nivel iniciación', manos='Balanceo de 6/8 + acordes',
  la_cancion='Un cuento cantado en Fa mayor sobre una araña y un cuenco de leche. Se cuenta en dos grupos de tres corcheas.',
  difficult_cc='cc. 1–4', difficult_title='El balanceo de seis corcheas',
  reto='sentir el compás en dos grupos de tres, no en seis pulsos sueltos.',
  truco='cuenta "uno-dos-tres, uno-dos-tres" marcando un poco más los "unos".',
  sabias_que='"Little Miss Muffet" es una rima infantil inglesa que aparece impresa por primera vez en 1805, aunque puede ser mucho más antigua.',
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — Fa mayor, en 6/8',
  posicion_texto='Mano derecha en posición de FA. Este compás se cuenta en dos grupos de tres corcheas por compás.',
  mini_staff_events=[{'pitch': p, 'dur': 'e', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3)]] +
                     [{'pitch': 'Bb4', 'dur': 'q.', 'number': 4}],
  time_sig=(6, 8),
  nivel_kicker='ARNAU · NIVEL INICIACIÓN · CANCIÓN 12',
  total_songs=20,
)

cfg12 = dict(
  kicker='ARNAU · CANCIÓN 12 · LITTLE MISS MUFFET',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb1', 'D2', 'F2'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='Little Miss Muffet', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el balanceo de seis corcheas, en 6/8.',
  rhythm_events=[{'pitch': 'F4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
                 {'pitch': 'Bb4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}],
  rhythm_time_sig=(6, 8),
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

    out_path = os.path.join(OUT_DIR, 'Arnau_12_Little_Miss_Muffet.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
