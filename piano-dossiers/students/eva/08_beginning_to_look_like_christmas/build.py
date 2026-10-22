import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', ' its-beginning-to-look-a-lot-like (4 manos).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song8 = dict(
  num=8, title="It's Beginning to Look a Lot Like Christmas", subtitle='Piano Duet · a 4 manos',
  tonalidad='Do mayor', compas='6/8', tempo='Vals ♩.≈60', forma='Estrofa',
  dificultad='Un reto de conjunto', manos='Ensamble a 4 manos',
  la_cancion='Un villancico a dúo en Do mayor y compás de 6/8. Aquí el reto no es técnico: es el ensamble — empezar exactamente juntas y mantenerse sincronizadas.',
  difficult_cc='cc. 1–8', difficult_title='El ensamble: empezar y mantenerse juntas',
  reto='sentir el mismo tempo que tu compañera antes de tocar la primera nota, y no acelerar ni frenar sola.',
  truco='cuenta un compás entero en silencio, "respirando" el tempo, antes de dar la entrada.',
  sabias_que='Esta canción se escribió en 1951 y describe la nieve de Nueva York, aunque su compositor, Meredith Willson, vivía en California y casi no había visto nieve en años.',
  mini_staff_events=[{'pitch': p, 'dur': 'e', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] * 2,
  time_sig=(6, 8),
  checklist_items=['Encuentro DO y pongo bien los dedos.', 'Cuento el compás vacío antes de entrar.',
                    'Mantengo mi pulso firme sin acelerar ni frenar.', 'Suena como un dúo de verdad, sincronizado.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · DICIEMBRE',
  total_songs=21,
)

cfg8 = dict(
  kicker='EVA · DICIEMBRE · BEGINNING TO LOOK LIKE CHRISTMAS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title="It's Beginning to Look a Lot Like Christmas", song_key='Do mayor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Do', 'Fa', 'Sol', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real del vaivén de 6/8: dos grandes pulsos por compás, no seis pequeños.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q.'}] * 4,
  rhythm_time_sig=(6, 8),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song8)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg8)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_08_Beginning_To_Look_Like_Christmas.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
