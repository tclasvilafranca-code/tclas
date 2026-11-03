import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'NEL', 'petite chanson.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song10 = dict(
  num=10, title='Petite Chanson', subtitle='Riccardo Collu (a 4 manos)',
  tonalidad='Do mayor', compas='4/4', tempo='Andante ♩≈80', forma='Tema con frases largas',
  dificultad='Un reto de continuidad', manos='Flujo continuo + melodía',
  la_cancion='Una pieza de Riccardo Collu en Do mayor, pensada para tocar a 4 manos. El reto es de continuidad: la segunda parte fluye en corcheas sin parar nunca, de principio a fin.',
  difficult_cc='cc. 1–8', difficult_title='Movimiento perpetuo: sin ningún hueco',
  reto='mantener el flujo de corcheas absolutamente continuo, sin que se note ningún hueco al cambiar de acorde.',
  truco='practica el cambio de acorde muy despacio, asegurándote de que la última corchea de un acorde y la primera del siguiente están exactamente a la misma distancia que las demás.',
  sabias_que='Riccardo Collu es un compositor contemporáneo que escribe piezas pedagógicas a 4 manos para que alumno y profesor toquen juntos.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='NEL · NIVEL MEDIO-ALTO · FEBRERO',
  total_songs=22,
)

cfg10 = dict(
  kicker='NEL · FEBRERO · PETITE CHANSON',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Petite Chanson', song_key='Do mayor',
  progression_desc='Estos son los acordes reales de la pieza. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real del flujo: corcheas continuas, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'e'}] * 16,
  rhythm_time_sig=(4, 4),
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

    out_path = os.path.join(OUT_DIR, 'Nel_10_Petite_Chanson.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
