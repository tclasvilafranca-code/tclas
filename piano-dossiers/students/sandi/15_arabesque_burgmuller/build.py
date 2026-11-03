import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', 'arabesque-burgmuller-( 4 MANOS).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song15 = dict(
  num=15, title='Arabesque', subtitle='J.F.F. Burgmüller Op.100 No.2, arr. four hands by MB',
  tonalidad='Do mayor', compas='2/4', tempo='Allegro scherzando', forma='Rondó (A-B-A), a 4 manos',
  dificultad='Nivel avanzado', manos='Staccato veloz + acompañamiento repetido, a 4 manos',
  la_cancion='La célebre Arabesque de Burgmüller, en esta versión a cuatro manos. El Piano 1 corre en semicorcheas staccato mientras el Piano 2 repite acordes: cada nota debe soltarse al instante, incluso a tempo real.',
  difficult_cc='Toda la pieza', difficult_title='El staccato veloz: dedos ligeros a tempo real',
  reto='mantener un staccato limpio y ligero incluso a la velocidad del Allegro scherzando, sin que las notas se peguen entre sí.',
  truco='practica primero muy despacio, exagerando el staccato, y ve acelerando poco a poco sin perder esa separación entre notas.',
  sabias_que='Johann Friedrich Franz Burgmüller compuso "Arabesque" como parte de sus 25 Études faciles et progressives, Op.100, uno de los cuadernos de estudio más usados en la enseñanza del piano.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]],
  nivel_kicker='SANDI · NIVEL AVANZADO · ABRIL',
  total_songs=16,
)

cfg15 = dict(
  kicker='SANDI · ABRIL · ARABESQUE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Arabesque', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el staccato veloz, en 2/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'e'}] * 4,
  rhythm_time_sig=(2, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song15)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg15)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_15_Arabesque.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
