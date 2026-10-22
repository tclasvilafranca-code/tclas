import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'counting-stars-easy-piano-solo.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song2 = dict(
  num=2, title='Counting Stars', subtitle='OneRepublic · arr. Becky Messer (Easy Version)',
  tonalidad='Do mayor', compas='4/4', tempo='♩≈120', forma='Estrofa-estribillo',
  dificultad='Un reto de síncopa', manos='Melodía sincopada + acordes',
  la_cancion='Una canción de OneRepublic en Do mayor, en su versión fácil. El reto es rítmico: la melodía entra justo antes o después del tiempo, nunca encima — hay que sentir el silencio con la misma firmeza que la nota.',
  difficult_cc='cc. 1–8', difficult_title='La síncopa: entrar fuera del tiempo',
  reto='sentir el silencio de corchea con la misma precisión que una nota, para que la entrada "fuera de tiempo" suene decidida y no dudosa.',
  truco='cuenta las corcheas en voz baja ("1-y-2-y-3-y-4-y") y toca justo en el "y" que corresponda, sin adelantarte ni atrasarte.',
  sabias_que='"Counting Stars" (2013) de OneRepublic mezcla pop con toques de folk y gospel; su videoclip fue grabado en un antiguo edificio antes de ser demolido.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('E4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]] +
                     [{'pitch': 'C4', 'dur': 'h.', 'number': 1}],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · SEPTIEMBRE',
  total_songs=22,
)

cfg2 = dict(
  kicker='JOSEP · SEPTIEMBRE · COUNTING STARS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'E4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'A4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Do, Fa, Sol...) y di si es mayor o menor.',
  chords=[['C3', 'E3', 'G3'], ['F2', 'A2', 'C3'], ['G2', 'B2', 'D3'], ['C3', 'E3', 'G3']],
  song_title='Counting Stars', song_key='Do mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Do mayor (I, IV, V...).',
  progression=['Do', 'Fa', 'Sol', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: silencio de corchea, corchea, negra — la síncopa de la canción, en 4/4.',
  rhythm_events=[{'rest': True, 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'q'},
                 {'rest': True, 'dur': 'e'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'q'}] * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song2)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg2)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_02_Counting_Stars.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
