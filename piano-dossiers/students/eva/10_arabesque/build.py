import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', ' arabesque-burgmuller-( 4 manos).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song10 = dict(
  num=10, title='Arabesque', subtitle='Burgmüller · a 4 manos',
  tonalidad='Do mayor', compas='2/4', tempo='Allegretto ♩≈108', forma='Estudio',
  dificultad='Un reto de igualdad', manos='Giro regular + acordes',
  la_cancion='Un estudio clásico de Burgmüller a cuatro manos, en Do mayor. Aquí el reto es técnico de verdad: que el giro rápido de cuatro notas suene perfectamente regular.',
  difficult_cc='cc. 1–8', difficult_title='El giro exacto, nota a nota',
  reto='que las cuatro notas del giro suenen exactamente igual de fuertes y de largas, sin ningún acento accidental.',
  truco='practica primero muy despacio, casi parando en cada nota, antes de acelerar.',
  sabias_que='Friedrich Burgmüller compuso 25 estudios de este tipo (Op.100) específicamente para que los alumnos jóvenes desarrollasen técnica con piezas que sonaran bonitas, no solo ejercicios secos.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  checklist_items=['Encuentro DO y pongo bien los dedos.', 'El giro suena perfectamente regular, sin acentos.',
                    'No acelero ni freno el giro sin querer.', 'Junto las dos manos con precisión de metrónomo.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · FEBRERO',
  total_songs=21,
)

cfg10 = dict(
  kicker='EVA · FEBRERO · ARABESQUE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['G2', 'B2', 'D3'], ['F2', 'A2', 'C3'], ['C3', 'E3', 'G3']],
  song_title='Arabesque', song_key='Do mayor',
  progression_desc='Esta es la progresión real del estudio. Escribe el grado de cada acorde en Do mayor (I, IV, V...).',
  progression=['Do', 'Sol', 'Fa', 'Do', 'Sol', 'Fa', 'Do', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real del giro: corcheas perfectamente regulares, en 2/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}] * 2,
  rhythm_time_sig=(2, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song10)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg10)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_10_Arabesque.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
