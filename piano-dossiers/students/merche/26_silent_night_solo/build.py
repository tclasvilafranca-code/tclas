import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'SILENT NINGT.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song26 = dict(
  num=26, title='Silent Night (solo)', subtitle='Franz X. Gruber · palabras de Joseph Mohr',
  tonalidad='Do mayor', compas='3/4', tempo='Gently', forma='Estrofa con acordes con bajo distinto',
  dificultad='Nivel básico', manos='Melodía + acordes con bajo distinto (slash chords)',
  la_cancion='"Silent Night" en su versión completa para piano solo, en Do mayor. Los símbolos de acorde incluyen barras, como "G/B" o "Am/C": la letra tras la barra indica qué nota va en el bajo.',
  difficult_cc='Toda la pieza', difficult_title='Los acordes con bajo distinto: leer las barras',
  reto='entender que la letra después de la barra es la nota del bajo, no el nombre del acorde en sí.',
  truco='toca primero el acorde completo y luego coloca la nota indicada tras la barra como la más grave, aunque no sea la fundamental.',
  sabias_que='"Silent Night" (Stille Nacht) fue compuesta en 1818 por Franz Xaver Gruber, y los acordes con bajo distinto (como G/B) son un recurso habitual en los arreglos modernos para dar más movimiento al bajo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · JUNIO',
  total_songs=28,
)

cfg26 = dict(
  kicker='MERCÈ · JUNIO · SILENT NIGHT (SOLO)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol, G/B...) y di cuál nota va en el bajo.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['B2', 'D3', 'G3']],
  song_title='Silent Night (solo)', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe qué nota va en el bajo de cada uno.',
  progression=['Do', 'G/B', 'Am/C', 'Fa'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: la melodía sobre el acorde con bajo distinto, en 3/4.',
  rhythm_events=[{'pitch': 'G4', 'dur': 'h.'}] * 2,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song26)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg26)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_26_Silent_Night_Solo.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
