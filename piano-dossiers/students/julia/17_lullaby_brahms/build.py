import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JULIA', ' Lulluby(cancion de cuna).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song17 = dict(
  num=17, title='Lullaby (Canción de cuna)', subtitle='Level Three · Johannes Brahms, arr. Gilbert DeBenedetti',
  tonalidad='Do mayor', compas='3/4', tempo='Muy tranquilo', forma='Estrofa',
  dificultad='Nivel inicial, con toque extra', manos='Vaivén suave + acordes',
  la_cancion='La famosa nana de Brahms, simplificada en Do mayor. Hoy mecemos con calma, siempre igual de suave, como acunar a un bebé.',
  difficult_cc='cc. 1–3', difficult_title='La nana que mece: suave y regular',
  reto='que cada nota se meza igual de suave que la anterior, sin ningún golpe brusco.',
  truco='imagina que tienes un bebé en brazos y lo meces con mucho cuidado, siempre igual.',
  sabias_que='La "Wiegenlied" (Nana) de Johannes Brahms (1868) es una de las canciones de cuna más famosas del mundo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JULIA · NIVEL INICIAL · MARZO',
  total_songs=24,
)

cfg17 = dict(
  kicker='JULIA · MARZO · LULLABY (BRAHMS)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Lullaby', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: notas largas y tranquilas, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h.'}] * 3,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song17)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg17)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Julia_17_Lullaby_Brahms.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
