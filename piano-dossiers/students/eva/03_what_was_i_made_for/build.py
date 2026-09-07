import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', 'what-was-i-made-for-billie-eilish.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song3 = dict(
  num=3, title='What Was I Made For?', subtitle='Billie Eilish',
  tonalidad='Do mayor', compas='4/4', tempo='Lento ♩≈70', forma='Estrofa',
  dificultad='Fácil, pero exigente en el control', manos='Melodía + acordes suaves',
  la_cancion='Una balada muy sencilla en Do mayor, casi susurrada. Aquí el reto no es leer las notas: es tocar tan suave que el sonido no se pierda ni se rompa.',
  difficult_cc='cc. 1–8', difficult_title='El pianissimo controlado',
  reto='mantener un volumen muy bajo durante toda la frase, sin que ninguna nota se escape más fuerte.',
  truco='toca tan cerca de la tecla como puedas, sin levantar el dedo antes del ataque.',
  sabias_que='Billie Eilish escribió esta canción para la película "Barbie" (2023) y ganó el Óscar a Mejor Canción Original.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('E4', 3), ('D4', 2)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  checklist_items=['Encuentro DO y pongo bien los dedos.', 'Toco siempre en pianissimo, sin acentos.',
                    'Ninguna nota se me escapa más fuerte que las demás.', 'Junto las dos manos, en equilibrio suave.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · OCTUBRE',
  total_songs=21,
)

cfg3 = dict(
  kicker='EVA · OCTUBRE · WHAT WAS I MADE FOR?',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Mim, Fa...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['E2', 'G2', 'B2'], ['F2', 'A2', 'C3'], ['C3', 'E3', 'G3']],
  song_title='What Was I Made For?', song_key='Do mayor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Do mayor (I, iii, IV, vi...).',
  progression=['Do', 'Mim', 'Fa', 'Do', 'Fa', 'Do', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras suaves y una nota larga, sin acentos.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 3 + [{'pitch': 'C4', 'dur': 'h'}] +
                [{'pitch': 'D4', 'dur': 'q'}] * 3 + [{'pitch': 'C4', 'dur': 'h'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song3)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg3)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_03_What_Was_I_Made_For.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
