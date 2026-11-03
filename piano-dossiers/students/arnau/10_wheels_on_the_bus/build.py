import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', ' The Wheels on the Bus.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song10 = dict(
  num=10, title='The Wheels on the Bus', subtitle='Canción infantil tradicional · arr. Jim Paterson',
  tonalidad='Fa mayor', compas='4/4', tempo='Alegre', forma='Estrofa',
  dificultad='Nivel iniciación', manos='Nota repetida + acordes',
  la_cancion='Nuestra primera canción con un bemol: Fa mayor. Las ruedas del autobús "giran y giran" con la misma nota repetida.',
  difficult_cc='cc. 1–4', difficult_title='Las ruedas que giran: la misma nota',
  reto='mantener el mismo dedo firme mientras repites la nota, sin cansarte.',
  truco='deja caer la mano una sola vez y "rebota" suave para cada repetición.',
  sabias_que='"The Wheels on the Bus" se escribió en Estados Unidos en los años 30 y hoy se canta en decenas de idiomas distintos.',
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA: Fa(1) Sol(2) La(3) Sib(4) Do(5). El dedo 4 toca una tecla negra: es el Sib de la armadura.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4)]] +
                     [{'pitch': 'C5', 'dur': 'h', 'number': 5}, {'pitch': 'F4', 'dur': 'h', 'number': 1}],
  time_sig=(4, 4),
  nivel_kicker='ARNAU · NIVEL INICIACIÓN · CANCIÓN 10',
  total_songs=20,
)

cfg10 = dict(
  kicker='ARNAU · CANCIÓN 10 · THE WHEELS ON THE BUS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb1', 'D2', 'F2'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='The Wheels on the Bus', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la rueda que gira, en 4/4.',
  rhythm_events=[{'pitch': 'C5', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song10)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg10)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Arnau_10_The_Wheels_On_The_Bus.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
