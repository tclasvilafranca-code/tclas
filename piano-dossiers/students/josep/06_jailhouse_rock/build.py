import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'jailhouse-rock-elvis-presley-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song6 = dict(
  num=6, title='Jailhouse Rock', subtitle='Elvis Presley · arr. Sadie King',
  tonalidad='Do mayor', compas='4/4', tempo='♩≈150, Swing', forma='Estrofa',
  dificultad='Un reto de digitación', manos='Patrón fijo de dedos + melodía',
  la_cancion='Una canción de Elvis Presley en Do mayor, con swing. El reto es de digitación: la izquierda salta de acorde en acorde, pero la forma de la mano y el orden de los dedos (5-3-2-1) no cambian nunca.',
  difficult_cc='cc. 1–8', difficult_title='La digitación fija: 5-3-2-1',
  reto='mantener siempre el mismo orden de dedos al saltar la izquierda de un acorde a otro, sin reajustar la mano cada vez.',
  truco='memoriza la forma de la mano como un molde fijo — solo cambia de sitio en el teclado, nunca de forma.',
  sabias_que='"Jailhouse Rock" (1957) de Elvis Presley incluye una de las coreografías de baile más icónicas del rock and roll, creada por el propio Elvis.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · DICIEMBRE',
  total_songs=22,
)

cfg6 = dict(
  kicker='JOSEP · DICIEMBRE · JAILHOUSE ROCK',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Jailhouse Rock', song_key='Do mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: corcheas con swing, en 4/4.',
  rhythm_events=[{'pitch': 'G4', 'dur': 'e'}] * 16,
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

    out_path = os.path.join(OUT_DIR, 'Josep_06_Jailhouse_Rock.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
