import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', '4 MANOS_diabelli-anton-romance-166580_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song13 = dict(
  num=13, title='Romance', subtitle='Anton Diabelli · Sonata a 4 manos Op.163 No.1, Mvmt.2',
  tonalidad='Do mayor', compas='4/4', tempo='Andantino', forma='Tema con repetición (a 4 manos)',
  dificultad='Nivel avanzado', manos='Melodía legato + acompañamiento en corcheas, a 4 manos',
  la_cancion='El segundo movimiento de esta sonata de Diabelli para piano a 4 manos, en Do mayor. La partitura pide "sempre legato": cada nota debe ligarse con la siguiente sin la menor interrupción de sonido.',
  difficult_cc='Toda la pieza', difficult_title='El legato absoluto: sin cortes entre las notas',
  reto='ligar cada nota con la siguiente sin ningún hueco de silencio, soltando el dedo justo cuando el siguiente ya pisa la tecla.',
  truco='practica muy despacio, sintiendo el peso del brazo transferirse de un dedo a otro sin levantar la mano ni un instante.',
  sabias_que='Anton Diabelli, además de compositor, fue el editor musical que encargó a Beethoven las célebres "Variaciones Diabelli" sobre un vals suyo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4), ('E4', 3), ('D4', 2)]],
  nivel_kicker='SANDI · NIVEL AVANZADO · MARZO',
  total_songs=16,
)

cfg13 = dict(
  kicker='SANDI · MARZO · ROMANCE (DIABELLI)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Romance', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la línea legato, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 4,
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

    out_path = os.path.join(OUT_DIR, 'Sandi_13_Romance_Diabelli.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
