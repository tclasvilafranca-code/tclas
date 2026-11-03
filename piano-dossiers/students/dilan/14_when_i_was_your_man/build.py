import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' WHEN I WAS YOUR MAN _ Bruno Mars_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song14 = dict(
  num=14, title='When I Was Your Man', subtitle='Bruno Mars',
  tonalidad='Do mayor', compas='4/4', tempo='Lento ♩≈72', forma='Estrofa-estribillo',
  dificultad='Un reto de memoria', manos='Acordes en bloque + melodía',
  la_cancion='Una balada de piano solo, en Do mayor. Casi toda la izquierda son acordes en bloque que hay que memorizar de verdad.',
  difficult_cc='cc. 1–8', difficult_title='Tocar de memoria, sin mirar',
  reto='memorizar la forma de cada acorde en la mano, para no tener que leer cada nota.',
  truco='mira el acorde, tócalo, y a la tercera repetición tapa la partitura y tócalo solo de memoria.',
  sabias_que='Bruno Mars tocó "When I Was Your Man" él solo al piano en los Grammy de 2014 — sin banda, solo voz y piano, algo poco habitual en una gala así.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 5), ('E4', 3), ('F4', 4), ('D4', 2), ('E4', 3), ('C4', 1)]] +
                     [{'pitch': 'C4', 'dur': 'h', 'number': 1}],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · ABRIL',
  total_songs=24,
)

cfg14 = dict(
  kicker='DILAN · ABRIL · WHEN I WAS YOUR MAN',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='When I Was Your Man', song_key='Do mayor',
  progression_desc='Estos acordes sostienen la balada. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Fa', 'Sol', 'Do', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: acordes largos y tranquilos, como pide una balada lenta.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h'}] * 4,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song14)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg14)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_14_When_I_Was_Your_Man.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
