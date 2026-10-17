import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'La Pantera Rosa.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song24 = dict(
  num=24, title='La Pantera Rosa', subtitle='Henry Mancini, arr. escolar',
  tonalidad='Do mayor', compas='4/4', tempo='Con swing, sigiloso', forma='Estrofa con cromatismos',
  dificultad='Nivel básico', manos='Melodía cromática + acordes',
  la_cancion='El famosísimo tema de la Pantera Rosa. Toda la melodía se construye con segundas menores (medio tono): la distancia cromática más pequeña que existe entre dos teclas vecinas.',
  difficult_cc='Toda la pieza', difficult_title='El intervalo de segunda menor: el paso más pequeño',
  reto='afinar con precisión el medio tono exacto entre cada nota natural y su vecina cromática.',
  truco='toca las dos teclas (blanca y negra) una junto a la otra y escucha lo cerca que suenan: eso es una segunda menor.',
  sabias_que='Henry Mancini compuso este tema en 1963 para la película "La Pantera Rosa", y ganó un Grammy por ello.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · JUNIO',
  total_songs=28,
)

cfg24 = dict(
  kicker='MERCÈ · JUNIO · LA PANTERA ROSA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª menor, 2ª mayor, 3ª...',
  intervals=[('C4', 'C#4'), ('C4', 'D4'), ('C4', 'D#4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'F#4')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='La Pantera Rosa', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: las segundas menores, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song24)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg24)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_24_La_Pantera_Rosa.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
