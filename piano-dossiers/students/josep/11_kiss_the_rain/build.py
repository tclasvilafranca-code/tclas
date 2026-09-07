import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', ' kiss-the-rain-yiruma-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song11 = dict(
  num=11, title='Kiss the Rain', subtitle='Yiruma',
  tonalidad='Do mayor', compas='4/4', tempo='♩≈76', forma='Tema',
  dificultad='Un reto de arpegio', manos='Arpegio de octava + acordes sostenidos',
  la_cancion='Una pieza instrumental de Yiruma en Do mayor, muy conocida. El reto es de arpegio: un dibujo que recorre una octava entera, subiendo y bajando, mientras la izquierda sostiene el acorde.',
  difficult_cc='cc. 1–4', difficult_title='El arpegio que sube y baja, sin perder el pulso',
  reto='que el arpegio recorra la octava entera sin que el pulso de fondo se acelere ni se frene.',
  truco='cuenta en voz alta mientras tocas el arpegio, muy despacio al principio, hasta que el pulso quede clavado.',
  sabias_que='"Kiss the Rain" (2002) del pianista surcoreano Yiruma es una de las piezas de piano contemporáneo más escuchadas del mundo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · MARZO',
  total_songs=22,
)

cfg11 = dict(
  kicker='JOSEP · MARZO · KISS THE RAIN',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Sol, Lam, Fa...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['G2', 'B2', 'D3'], ['A2', 'C3', 'E3'], ['F2', 'A2', 'C3']],
  song_title='Kiss the Rain', song_key='Do mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V, vi...).',
  progression=['Do', 'Sol', 'Lam', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: arpegio en corcheas que resuelve en notas largas, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'},
                 {'pitch': 'E4', 'dur': 'h'}, {'pitch': 'C4', 'dur': 'h'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song11)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg11)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_11_Kiss_The_Rain.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
