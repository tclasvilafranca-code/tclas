import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' arabesque-burgmuller-( 4 manos).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song7 = dict(
  num=10, title='Arabesque', subtitle='J. F. Burgmüller, Op. 100 nº 2 · arreglo a 4 manos',
  tonalidad='Do mayor', compas='2/4', tempo='Allegro scherzando ♩≈132', forma='Rondó (A-B-A)',
  dificultad='Un reto de conjunto', manos='Piano 1 + Piano 2 (a dúo)',
  la_cancion='Un estudio clásico muy famoso, escrito para tocarse a cuatro manos: tú en una parte, tu profe (o un compañero) en la otra.',
  difficult_cc='cc. 1–8', difficult_title='Tocar en conjunto, sin perder el pulso',
  reto='mantener tu parte firme mientras suena la otra, sin acelerar ni frenar para "esperarla".',
  truco='cuenta en voz alta mientras tocas solo, y luego repite contando por dentro cuando toques a dúo.',
  sabias_que='Burgmüller escribió 25 Études Faciles (Op. 100) para que sus alumnos progresaran poco a poco; "Arabesque" es la número 2 y es una de las piezas para piano más tocadas del mundo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('E4', 3), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · FEBRERO',
  total_songs=24,
)

cfg7 = dict(
  kicker='DILAN · FEBRERO · ARABESQUE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol, Rem...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['D3', 'F3', 'A3']],
  song_title='Arabesque', song_key='Do mayor',
  progression_desc='El estudio se apoya en estos tres acordes de Do mayor. Escribe si cada uno es tónica (T), subdominante (SD) o dominante (D).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo: el giro rápido de corcheas, seguido de negras tranquilas.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}] * 2 +
                [{'pitch': 'C4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}],
  rhythm_time_sig=(2, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song7)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg7)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_10_Arabesque.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
