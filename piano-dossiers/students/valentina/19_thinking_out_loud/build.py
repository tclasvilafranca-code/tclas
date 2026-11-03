import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de  THINKING OUT LOUD _ Ed Sheeran_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song19 = dict(
  num=19, title='Thinking Out Loud', subtitle='Ed Sheeran',
  tonalidad='Re mayor', compas='4/4', tempo='Rápido ♩≈145', forma='Estrofa-estribillo',
  dificultad='Nivel medio', manos='Bajo caminante + corcheas iguales',
  la_cancion='Una balada de Ed Sheeran en Re mayor, rápida. Hoy: el bajo caminante, una nota distinta en cada tiempo que enlaza los acordes como pasos.',
  difficult_cc='cc. 1–8', difficult_title='El bajo caminante: una nota distinta en cada tiempo',
  reto='caminar el bajo nota a nota sin perder el pulso mientras la derecha corre en corcheas iguales.',
  truco='practica el bajo caminante solo, muy despacio, hasta que cada paso salga natural antes de añadir la derecha.',
  sabias_que='"Thinking Out Loud" (2014) de Ed Sheeran fue nominada al Grammy a la Canción del Año y es una de las canciones más populares en bodas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('F#4', 3), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h', 'number': 1}],
  nivel_kicker='VALENTINA · NIVEL MEDIO · JUNIO',
  total_songs=22,
)

cfg19 = dict(
  kicker='VALENTINA · JUNIO · THINKING OUT LOUD (ED SHEERAN)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['E2', 'A2', 'C#3'], ['D3', 'F#3', 'A3']],
  song_title='Thinking Out Loud', song_key='Re mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'La', 'Sol', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el bajo caminante en negras, en 4/4.',
  rhythm_events=[{'pitch': p, 'dur': 'q'} for p in ['D4', 'E4', 'F#4', 'G4']],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song19)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg19)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, "Valentina_19_Thinking_Out_Loud.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
