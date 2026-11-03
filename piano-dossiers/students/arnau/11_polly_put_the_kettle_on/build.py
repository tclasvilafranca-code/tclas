import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', ' Polly Put the Kettle On.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song11 = dict(
  num=11, title='Polly Put the Kettle On', subtitle='Traditional · arr. Jim Paterson',
  tonalidad='Fa mayor', compas='4/4', tempo='Tranquilo', forma='Estrofa',
  dificultad='Nivel iniciación', manos='Notas ligadas + acordes',
  la_cancion='Una canción tranquila en Fa mayor. Las notas se unen unas con otras, sin cortes, como una frase hablada.',
  difficult_cc='cc. 1–4', difficult_title='Las notas ligadas, sin cortes',
  reto='que no se oiga ningún hueco entre una nota y la siguiente.',
  truco='canta la frase con "aaaa" sin parar, y luego imita eso al piano.',
  sabias_que='Es una canción de cuna y juego tradicional inglesa, conocida desde el siglo XVIII, sobre poner la tetera al fuego para el té.',
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA: Fa(1) Sol(2) La(3) Sib(4) Do(5). Liga cada nota con la siguiente, sin cortar.',
  mini_staff_events=[{'pitch': p, 'dur': 'h', 'number': n} for p, n in
                      [('C5', 5), ('Bb4', 4)]] +
                     [{'pitch': 'A4', 'dur': 'h', 'number': 3}, {'pitch': 'G4', 'dur': 'h', 'number': 2}],
  time_sig=(4, 4),
  nivel_kicker='ARNAU · NIVEL INICIACIÓN · CANCIÓN 11',
  total_songs=20,
)

cfg11 = dict(
  kicker='ARNAU · CANCIÓN 11 · POLLY PUT THE KETTLE ON',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb1', 'D2', 'F2'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='Polly Put the Kettle On', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: notas largas y ligadas, en 4/4.',
  rhythm_events=[{'pitch': 'C5', 'dur': 'h'}, {'pitch': 'Bb4', 'dur': 'h'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song11)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg11)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Arnau_11_Polly_Put_The_Kettle_On.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
