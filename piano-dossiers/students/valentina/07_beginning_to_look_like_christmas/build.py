import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', ' its-beginning-to-look-a-lot-like NAVIDAD (4 manos).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song7 = dict(
  num=7, title="It's Beginning to Look a Lot Like Christmas", subtitle='Piano Duet · arr. Rachel Chytelman',
  tonalidad='Do mayor', compas='6/8', tempo='Con vaivén ♩.≈100', forma='Estrofa (a dúo)',
  dificultad='Nivel medio, a dúo', manos='Piano 1 + Piano 2 (a dúo)',
  la_cancion='Un villancico clásico a cuatro manos, en Do mayor y 6/8. Hoy: equilibrar quién lleva la melodía, porque el papel cambia a mitad de pieza.',
  difficult_cc='cc. 1–8', difficult_title='La textura a cuatro manos: equilibrar quién lleva la melodía',
  reto='escuchar si tu parte lleva la melodía o el acompañamiento en cada momento, y ajustar el volumen a ese papel.',
  truco='cuando lleves la melodía, toca un poco más fuerte; cuando acompañes, toca más suave para dejarla brillar.',
  sabias_que='El compás de 6/8 se llama "compuesto": aunque se escriben seis corcheas, se sienten solo DOS grandes pulsos, cada uno dividido en tres — como el balanceo de una barca.',
  mini_staff_events=[{'pitch': p, 'dur': 'e', 'beam': 0} for p in ['C4', 'D4', 'E4']] +
                     [{'pitch': p, 'dur': 'e', 'beam': 1} for p in ['G4', 'F4', 'E4']],
  time_sig=(6, 8),
  nivel_kicker='VALENTINA · NIVEL MEDIO · DICIEMBRE',
  total_songs=22,
)

cfg7 = dict(
  kicker='VALENTINA · DICIEMBRE · BEGINNING TO LOOK LIKE CHRISTMAS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['G2', 'B2', 'D3'], ['F2', 'A2', 'C3'], ['C3', 'E3', 'G3']],
  song_title="It's Beginning to Look a Lot Like Christmas", song_key='Do mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Sol', 'Fa', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: dos olas de tres corcheas, en 6/8.',
  rhythm_events=[{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4', 'G4', 'F4', 'E4'])],
  rhythm_time_sig=(6, 8),
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

    out_path = os.path.join(OUT_DIR, "Valentina_07_Beginning_To_Look_Like_Christmas.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
