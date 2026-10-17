import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', '4 MANOS_diabelli-anton-romance-166580.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song7 = dict(
  num=7, title='Romance', subtitle="Anton Diabelli · 6 Sonatas, Op. 163 nº1 (a 4 manos)",
  tonalidad='Do mayor', compas='2/2 (alla breve)', tempo='Andante', forma='Tema con frases largas',
  dificultad='Un reto de quietud', manos='Posición fija a 4 manos',
  la_cancion='Un romance de Diabelli en Do mayor, pensado para tocar a 4 manos. El reto es de quietud: la parte Primo se toca entera sin mover la mano de su posición de cinco dedos.',
  difficult_cc='cc. 1–8', difficult_title='La mano estacionaria',
  reto='que la mano derecha no se desplace ni una sola vez en toda la pieza, solo cambien los dedos.',
  truco='antes de tocar, apoya los cinco dedos sobre sus cinco teclas y siente ese "molde" — no lo sueltes hasta el final.',
  sabias_que='Anton Diabelli fue compositor y editor musical; publicó obras de Beethoven y Schubert, además de sus propias piezas pedagógicas a 4 manos.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · DICIEMBRE',
  total_songs=22,
)

cfg7 = dict(
  kicker='JOSEP · DICIEMBRE · ROMANCE (DIABELLI)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Romance', song_key='Do mayor',
  progression_desc='Estos son los acordes del Secondo. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: blancas tranquilas, en 2/2 (alla breve).',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h'}] * 8,
  rhythm_time_sig=(2, 2),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song7)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg7)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_07_Romance_Diabelli.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
