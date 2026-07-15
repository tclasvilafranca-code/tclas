import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' la-promesa-MELENDI.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song17 = dict(
  num=17, title='La Promesa', subtitle='Melendi',
  tonalidad='Sol mayor', compas='4/4', tempo='Lento ♩≈76', forma='Estrofa-estribillo',
  dificultad='Un reto rítmico', manos='Melodía + acordes',
  la_cancion='Una canción de Melendi, en Sol mayor. Casi cada frase entra después de un silencio, a contratiempo.',
  difficult_cc='cc. 1–8', difficult_title='Entrar a contratiempo, tras el silencio',
  reto='entrar justo en su sitio después del silencio, sin adelantarse ni quedarte corto.',
  truco='cuenta el silencio en voz alta ("y-1, y-2...") hasta que la entrada sea automática.',
  sabias_que='Melendi es uno de los cantautores españoles más escuchados de las últimas dos décadas; "La Promesa" es una de sus canciones más coreadas en directo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('B4', 3), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h', 'number': 1}],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · MAYO',
  total_songs=24,
)

cfg17 = dict(
  kicker='DILAN · MAYO · LA PROMESA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Re, Do...) y di si es mayor o menor.',
  chords=[['G3', 'B3', 'D4'], ['D3', 'F#3', 'A3'], ['C3', 'E3', 'G3'], ['G3', 'B3', 'D4']],
  song_title='La Promesa', song_key='Sol mayor',
  progression_desc='Estos acordes sostienen la canción. Escribe el grado de cada uno en Sol mayor (I, IV, V...).',
  progression=['Sol', 'Re', 'Do', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: silencio, tres corcheas, y una nota larga — la entrada típica de esta canción.',
  rhythm_events=([{'rest': True, 'dur': 'e'}] + [{'pitch': 'D5', 'dur': 'e'}] * 3 + [{'pitch': 'D5', 'dur': 'h'}]) * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song17)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg17)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_17_La_Promesa.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
