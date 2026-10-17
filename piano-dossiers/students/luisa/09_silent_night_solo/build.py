import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'LUISA', ' Silent-Night.easy')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song9 = dict(
  num=9, title='Silent Night (solo)', subtitle='Franz X. Gruber · palabras de Joseph Mohr',
  tonalidad='Do mayor', compas='3/4', tempo='Gently', forma='Estrofa',
  dificultad='Nivel hobby', manos='Melodía suave + acordes',
  la_cancion='"Silent Night", en Do mayor, marcada "Gently" (con suavidad). Hoy solo hay que tocar cada nota como si arrullaras a un bebé, sin ningún golpe.',
  difficult_cc='cc. 1–4', difficult_title='Tocar con suavidad: como una nana',
  reto='tocar cada nota con suavidad, sin golpear ninguna tecla, como una nana tranquila.',
  truco='imagina que meces a un bebé mientras tocas: nada de golpes, todo suave.',
  sabias_que='"Silent Night" (Stille Nacht) fue compuesta en 1818 por Franz Xaver Gruber para una parroquia austríaca, y hoy se canta en más de 300 idiomas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='LUISA · NIVEL HOBBY · NOVIEMBRE',
  total_songs=28,
)

cfg9 = dict(
  kicker='LUISA · NOVIEMBRE · SILENT NIGHT (SOLO)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Silent Night (solo)', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: suave, sin golpes, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q.'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'q'}] * 2,
  rhythm_time_sig=(3, 4),
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

    out_path = os.path.join(OUT_DIR, 'Luisa_09_Silent_Night_Solo.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
