import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'Si-tu-no-estas-aqui-rosana_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song14 = dict(
  num=14, title='Si tú no estás aquí', subtitle='Rosana',
  tonalidad='Do mayor', compas='4/4 / 2/4 (mixto)', tempo='Balada ♩≈80', forma='Estrofa-estribillo',
  dificultad='Un reto de acento', manos='Melodía + acordes, compás cambiante',
  la_cancion='Una balada de Rosana en Do mayor. El reto es de acento: cuando el compás cambia de 4/4 a 2/4, el acento fuerte cae en un sitio distinto.',
  difficult_cc='cc. 1–8', difficult_title='El acento que se desplaza',
  reto='sentir dónde cae el acento fuerte en cada compás, sin quedarte solo con el número que estás contando.',
  truco='marca el acento con un ligero golpe de mano en el aire mientras cantas la melodía, para sentirlo antes de tocarlo.',
  sabias_que='"Si tú no estás aquí" es una de las baladas más conocidas de Rosana, cantautora gaditana con una carrera de más de 25 años.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · ABRIL',
  total_songs=22,
)

cfg14 = dict(
  kicker='JOSEP · ABRIL · SI TÚ NO ESTÁS AQUÍ',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Lam, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['A2', 'C3', 'E3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3']],
  song_title='Si tú no estás aquí', song_key='Do mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V, vi...).',
  progression=['Do', 'Lam', 'Fa', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: negras que cambian de compás, entre 4/4 y 2/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 8,
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

    out_path = os.path.join(OUT_DIR, 'Josep_14_Si_Tu_No_Estas_Aqui.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
