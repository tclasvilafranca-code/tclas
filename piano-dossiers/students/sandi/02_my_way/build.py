import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', ' MY WAY _ Jacques Revaux_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song2 = dict(
  num=2, title='My Way', subtitle='Jacques Revaux · Claude François (Comme d\'habitude)',
  tonalidad='Do mayor', compas='4/4', tempo='Moderately slow', forma='Estrofa con modulaciones de color',
  dificultad='Nivel avanzado', manos='Melodía + armonía extendida',
  la_cancion='El clásico "My Way", en Do mayor. La armonía se enriquece con acordes prestados (Fa menor) y dominantes secundarias (La7, Do7) que tiñen brevemente la tonalidad antes de resolver.',
  difficult_cc='Toda la pieza', difficult_title='Los acordes prestados: cuando el modo cambia un instante',
  reto='reconocer de oído y de vista cada acorde prestado o dominante secundaria, sin perder la sensación de "salida y vuelta" a la tonalidad.',
  truco='toca cada acorde prestado inmediatamente después de su acorde "normal" (Fa-Fam, Re-La7-Re) para sentir el contraste de color.',
  sabias_que='"My Way" (1969), con música original de Jacques Revaux y letra en inglés de Paul Anka, se basa en la canción francesa "Comme d\'habitude". Fue popularizada por Frank Sinatra.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]],
  nivel_kicker='SANDI · NIVEL AVANZADO · SEPTIEMBRE',
  total_songs=16,
)

cfg2 = dict(
  kicker='SANDI · SEPTIEMBRE · MY WAY',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Fam, La7...) y di si es mayor, menor o de séptima.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'Ab2', 'C3'], ['A2', 'C#3', 'E3', 'G3'], ['D2', 'F2', 'A2']],
  song_title='My Way', song_key='Do mayor',
  progression_desc='Estos son algunos acordes de la canción. Escribe el grado o función de cada uno en Do mayor (I, iv prestado, V7/ii...).',
  progression=['Do', 'Fam', 'La7', 'Rem'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: la melodía tranquila, en 4/4.',
  rhythm_events=[{'pitch': 'C4', 'dur': 'h'}] * 4,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song2)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg2)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_02_My_Way.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
