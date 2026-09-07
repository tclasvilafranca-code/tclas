import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'LUISA', 'perfect-ed-sheeran-easy-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song23 = dict(
  num=23, title='Perfect', subtitle='Ed Sheeran, arr. Nicki Allan',
  tonalidad='Do mayor', compas='12/8', tempo='Balada, tranquilo', forma='Estrofa con primera y segunda vez',
  dificultad='Nivel hobby', manos='Melodía + acorde repetido, sin complicarse',
  la_cancion='La conocida balada de Ed Sheeran, en Do mayor. Es una canción de amor con un vaivén suave y continuo: hoy solo hay que dejarla fluir, sin contar nada.',
  difficult_cc='cc. 1–4', difficult_title='Una canción de amor: déjala fluir',
  reto='dejar que la música fluya sola, sin ponerte a contar cada nota.',
  truco='escucha el vaivén como si fuera una nana: no hace falta contar, solo sentirlo.',
  sabias_que='"Perfect" (2017) de Ed Sheeran fue escrita como una carta de amor y se convirtió en una de las canciones más pedidas en bodas de todo el mundo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='LUISA · NIVEL HOBBY · MAYO',
  total_songs=28,
)

cfg23 = dict(
  kicker='LUISA · MAYO · PERFECT (ED SHEERAN)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Perfect', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el vaivén con puntillo, en doce por ocho.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q.'}] * 4,
  rhythm_time_sig=(12, 8),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song23)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg23)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Luisa_23_Perfect.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
