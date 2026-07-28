import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'Eso-que-tu-me-das. Jarabe de Palo.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song9 = dict(
  num=9, title='Eso que tú me das', subtitle='Jarabe de Palo',
  tonalidad='Do mayor', compas='4/4', tempo='Alegre', forma='Estrofa (parte 1)',
  dificultad='Nivel iniciación', manos='Acordes que cambian',
  la_cancion='Una canción española muy pegadiza y conocida. La izquierda cambia de acorde varias veces por compás, sin miedo.',
  difficult_cc='cc. 1–4', difficult_title='Los acordes que cambian, sin miedo',
  reto='cambiar de acorde a tiempo, sin que la mano se pare a pensar.',
  truco='practica solo los cambios de acorde, sin melodía, hasta que salgan solos.',
  sabias_que='Jarabe de Palo fue un grupo español liderado por Pau Donés; "Eso que tú me das" es una de sus canciones más queridas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}, {'pitch': 'E4', 'dur': 'h', 'number': 3}],
  nivel_kicker='ARNAU · NIVEL INICIACIÓN · CANCIÓN 9',
  total_songs=20,
)

cfg9 = dict(
  kicker='ARNAU · CANCIÓN 9 · ESO QUE TÚ ME DAS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol, Lam...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['A2', 'C3', 'E3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3']],
  song_title='Eso que tú me das', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, vi, IV, V...).',
  progression=['Do', 'Lam', 'Fa', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el cambio de acorde cada tiempo, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song9)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg9)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Arnau_09_Eso_Que_Tu_Me_Das.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
