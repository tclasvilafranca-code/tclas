import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', 'Interstellar __.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song6 = dict(
  num=6, title='Interstellar (tema principal)', subtitle='Hans Zimmer',
  tonalidad='Do mayor', compas='3/4', tempo='Lento, muy expresivo', forma='Tema',
  dificultad='Para disfrutar, sin prisa', manos='Melodía legato + acordes',
  la_cancion='El tema principal de la banda sonora de Interstellar (Hans Zimmer), en Do mayor. Aquí cuidamos que cada nota quede unida a la siguiente, sin ningún hueco.',
  difficult_cc='cc. 1–9', difficult_title='El legato que no se corta',
  reto='que cada nota se una a la siguiente sin ningún hueco de silencio, como una sola respiración larga.',
  truco='imagina que cantas la frase con la voz, sin respirar entre nota y nota, y deja que los dedos hagan lo mismo.',
  sabias_que='Hans Zimmer compuso el tema de "Interstellar" (2014) inspirándose en un órgano de iglesia, buscando un sonido "íntimo y a la vez inmenso".',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('D4', 2), ('C4', 1)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · NOVIEMBRE',
  total_songs=21,
)

cfg6 = dict(
  kicker='JOSÉ MARÍA · NOVIEMBRE · INTERSTELLAR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Interstellar', song_key='Do mayor',
  progression_desc='Estos son los acordes de la pieza. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: negras unidas sin ningún hueco, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 9,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song6)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg6)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'JoseMaria_06_Interstellar.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
