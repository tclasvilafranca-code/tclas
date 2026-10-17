import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'OH WHEN THE SAINT.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song1 = dict(
  num=1, title='Oh, When the Saints', subtitle='Primer Level · arr. Gilbert DeBenedetti',
  tonalidad='Do mayor', compas='4/4', tempo='Lively', forma='Estrofa con letra',
  dificultad='Nivel básico', manos='Melodía cantada + acompañamiento con silencio inicial',
  la_cancion='Un espiritual americano muy conocido, en Do mayor. El acompañamiento de la mano izquierda empieza siempre con un silencio de negra antes de entrar: hoy trabajamos esa precisión.',
  difficult_cc='cc. 1–4', difficult_title='El silencio que cuenta: el bajo entra a tiempo',
  reto='contar el silencio inicial con la misma exactitud que si fuera una nota, sin adelantarse ni retrasarse.',
  truco='antes de tocar, cuenta en voz baja "uno (silencio), dos, tres, cuatro" y entra justo en el "dos".',
  sabias_que='"Oh, When the Saints Go Marching In" es un espiritual afroamericano que se hizo mundialmente famoso gracias al jazz de Nueva Orleans, especialmente por Louis Armstrong.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · SEPTIEMBRE',
  total_songs=28,
)

cfg1 = dict(
  kicker='MERCÈ · SEPTIEMBRE · OH, WHEN THE SAINTS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Oh, When the Saints', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: silencio de negra y acorde, en 4/4.',
  rhythm_events=([{'rest': True, 'dur': 'q'}] + [{'pitch': 'E3', 'dur': 'q'}] * 3) * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song1)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg1)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_01_Oh_When_The_Saints.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
