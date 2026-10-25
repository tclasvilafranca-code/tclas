import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'Como entrenar a tu dragon.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song21 = dict(
  num=21, title='Cómo entrenar a tu dragón (tema de vuelo)', subtitle='John Powell',
  tonalidad='Do mayor → Re mayor (modula)', compas='4/4', tempo='♩≈120, con vuelo', forma='Tema',
  dificultad='Un reto de modulación', manos='Melodía + acordes, con cambio de tonalidad',
  la_cancion='El tema de vuelo de "Cómo entrenar a tu dragón" (John Powell). El reto es de modulación: la pieza empieza en Do mayor y, a mitad de camino, se desplaza a Re mayor.',
  difficult_cc='cc. 1–8', difficult_title='El cambio de armadura: la tonalidad cambia a mitad de camino',
  reto='sentir el nuevo centro tonal cuando la música modula, no solo leer las alteraciones nuevas sobre la marcha.',
  truco='toca primero la frase en Do mayor, luego la misma frase transportada a Re mayor, y siente cómo cambia la "casa" de la música.',
  sabias_que='John Powell compuso la banda sonora de "Cómo entrenar a tu dragón" (2010) usando instrumentos celtas para dar un carácter de vuelo y aventura.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('G4', 5), ('E4', 3), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · JUNIO',
  total_songs=22,
)

cfg21 = dict(
  kicker='JOSEP · JUNIO · CÓMO ENTRENAR A TU DRAGÓN',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol, Lam...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['A2', 'C3', 'E3']],
  song_title='Cómo entrenar a tu dragón', song_key='Do mayor → Re mayor',
  progression_desc='Estos son los acordes de la primera parte. Escribe el grado de cada uno en Do mayor (I, IV, V, vi...).',
  progression=['Do', 'Fa', 'Sol', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras que después se desplazan de tonalidad, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song21)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg21)
    c.save()

    writer = PdfWriter()
    source_pages = PdfReader(SOURCE_PDF).pages
    for p in source_pages[:2]:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_21_Como_Entrenar_A_Tu_Dragon.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
