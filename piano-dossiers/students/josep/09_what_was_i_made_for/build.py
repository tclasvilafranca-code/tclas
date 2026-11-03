import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'what-was-i-made-for-billie-eilish-easy-piano.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song9 = dict(
  num=9, title='What Was I Made For?', subtitle='Billie Eilish',
  tonalidad='Do mayor', compas='4/4', tempo='♩≈78', forma='Estrofa',
  dificultad='Un reto de fraseo', manos='Melodía con arco dinámico + acordes',
  la_cancion='Una balada de Billie Eilish en Do mayor. El reto es de fraseo: la frase dibuja un arco entero, creciendo hasta un punto y volviendo a bajar, en vez de mantener un volumen fijo de principio a fin.',
  difficult_cc='cc. 1–8', difficult_title='El arco dinámico largo',
  reto='que el volumen crezca y baje suavemente a lo largo de toda la frase, sin saltos ni escalones.',
  truco='marca a lápiz dónde está el punto más alto de la frase, y dibuja mentalmente una colina desde el principio hasta ese punto y de vuelta.',
  sabias_que='"What Was I Made For?" (2023) fue escrita para la película "Barbie" y ganó el Óscar a la Mejor Canción Original.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · ENERO',
  total_songs=22,
)

cfg9 = dict(
  kicker='JOSEP · ENERO · WHAT WAS I MADE FOR?',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Mim, Fa, Lam...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['E3', 'G3', 'B3'], ['F2', 'A2', 'C3'], ['A2', 'C3', 'E3']],
  song_title='What Was I Made For?', song_key='Do mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Do mayor (I, iii, IV, vi...).',
  progression=['Do', 'Mim', 'Fa', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: blancas tranquilas dibujando un arco, en 4/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h'}] * 8,
  rhythm_time_sig=(4, 4),
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

    out_path = os.path.join(OUT_DIR, 'Josep_09_What_Was_I_Made_For.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
