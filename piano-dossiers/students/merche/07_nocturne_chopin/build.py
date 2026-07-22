import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', ' nocturne-op9-chopin_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song7 = dict(
  num=7, title='Nocturne Op.9', subtitle='Frédéric Chopin, arr. Benny Chaw',
  tonalidad='Do mayor', compas='3/4', tempo='Tranquilo', forma='Estrofa con silencios',
  dificultad='Nivel básico', manos='Melodía expresiva con silencios + acordes',
  la_cancion='Una versión simplificada, en Do mayor, del célebre Nocturno de Chopin. La pieza tiene compases enteros de silencio: hoy trabajamos contarlos con la misma precisión que si estuviéramos tocando.',
  difficult_cc='cc. 2–8', difficult_title='El silencio expresivo: contar el compás de descanso',
  reto='contar un compás entero de silencio sin perder el pulso, y entrar justo a tiempo en la siguiente nota.',
  truco='mientras cuentas el silencio, marca cada tiempo con un ligero movimiento de la cabeza o el pie, sin tocar.',
  sabias_que='El Nocturno Op.9 nº2 de Chopin, compuesto hacia 1830-1832, es una de las piezas de piano más reconocibles del repertorio romántico.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · NOVIEMBRE',
  total_songs=28,
)

cfg7 = dict(
  kicker='MERCÈ · NOVIEMBRE · NOCTURNE OP.9 (CHOPIN)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Nocturne Op.9', song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: nota larga y silencio, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h.'}, {'rest': True, 'dur': 'h.'}] * 2,
  rhythm_time_sig=(3, 4),
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

    out_path = os.path.join(OUT_DIR, 'Merce_07_Nocturne_Chopin.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
