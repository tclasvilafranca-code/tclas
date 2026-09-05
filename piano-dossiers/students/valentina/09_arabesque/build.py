import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de  arabesque-burgmuller-( 4 manos).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song9 = dict(
  num=9, title='Arabesque', subtitle='J. F. Burgmüller, Op. 100 nº 2 · arreglo a 4 manos',
  tonalidad='Do mayor', compas='2/4', tempo='Allegro scherzando ♩≈132', forma='Rondó (A-B-A)',
  dificultad='Nivel medio, a dúo', manos='Piano 1 + Piano 2 (a dúo)',
  la_cancion='Un estudio clásico de Burgmüller a cuatro manos, en Do mayor. Hoy: el equilibrio entre las dos partes, para que ninguna tape a la otra.',
  difficult_cc='cc. 1–8', difficult_title='El equilibrio a dos pianos: que ninguna parte tape a la otra',
  reto='escuchar constantemente el volumen de la otra parte y ajustar el tuyo para que ninguna se pierda.',
  truco='graba (o pide que te graben) tocando a dúo, y escucha si se entienden las dos partes por igual.',
  sabias_que='Friedrich Burgmüller escribió sus "25 Études faciles et progressives" Op. 100 como piezas de estudio con carácter propio, no solo ejercicios técnicos.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='VALENTINA · NIVEL MEDIO · FEBRERO',
  total_songs=22,
)

cfg9 = dict(
  kicker='VALENTINA · FEBRERO · ARABESQUE (BURGMÜLLER, A 4 MANOS)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['G2', 'B2', 'D3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3']],
  song_title='Arabesque', song_key='Do mayor',
  progression_desc='Estos son los acordes de la pieza. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Sol', 'Fa', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el giro rápido en corcheas, en 2/4.',
  rhythm_events=[{'pitch': p, 'dur': 'e', 'beam': i // 4} for i, p in enumerate(['E4', 'D4', 'C4', 'D4'] * 2)],
  rhythm_time_sig=(2, 4),
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

    out_path = os.path.join(OUT_DIR, "Valentina_09_Arabesque.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
