import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de  WHEN I WAS YOUR MAN _ Bruno Mars_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song13 = dict(
  num=13, title='When I Was Your Man', subtitle='Bruno Mars',
  tonalidad='Do mayor', compas='4/4', tempo='Lento ♩≈72', forma='Estrofa-estribillo',
  dificultad='Nivel medio', manos='Bajo en arpegio + melodía',
  la_cancion='Una balada de piano solo de Bruno Mars, en Do mayor. Hoy: el bajo en arpegio, repartiendo el acorde nota a nota en vez de tocarlo en bloque.',
  difficult_cc='cc. 1–8', difficult_title='El bajo en arpegio: romper el acorde en vez de tocarlo en bloque',
  reto='mantener el dibujo del arpegio fluido y regular, como una ola, sin que suene entrecortado.',
  truco='toca primero el acorde en bloque para sentir su forma, y luego repártelo nota a nota sin cambiar la mano de sitio.',
  sabias_que='"When I Was Your Man" (2012) de Bruno Mars es una balada de piano solo, sin apenas producción añadida, algo poco habitual en sus canciones más conocidas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='VALENTINA · NIVEL MEDIO · ABRIL',
  total_songs=22,
)

cfg13 = dict(
  kicker='VALENTINA · ABRIL · WHEN I WAS YOUR MAN (BRUNO MARS)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['G2', 'B2', 'D3']],
  song_title='When I Was Your Man', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Fa', 'Sol', 'Do', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el arpegio del bajo, en 4/4.',
  rhythm_events=[{'pitch': p, 'dur': 'q'} for p in ['C3', 'E3', 'G3', 'E3']],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song13)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg13)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_13_When_I_Was_Your_Man.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
