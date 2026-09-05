import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'Grandfather.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song22 = dict(
  num=22, title="My Grandfather's Clock", subtitle='Level Three · Henry Clay Work, arr. Gilbert DeBenedetti',
  tonalidad='Sol mayor', compas='4/4', tempo='With precision', forma='Estrofa',
  dificultad='Nivel básico', manos='Melodía con cambios de posición + acordes',
  la_cancion='La clásica canción "My Grandfather\'s Clock", en Sol mayor. La mano cambia varias veces de posición a lo largo de la pieza: hoy trabajamos deslizarla con suavidad, sin mirar el teclado.',
  difficult_cc='Toda la pieza', difficult_title='El cambio de posición: cuando cambia el dedo guía',
  reto='desplazar la mano entera a la nueva posición con suavidad, en el momento justo, sin mirar el teclado.',
  truco='antes de tocar, localiza con el tacto dónde está la nueva nota del dedo 1, y desliza la mano hacia allí sin prisa.',
  sabias_que='"My Grandfather\'s Clock" (1876), de Henry Clay Work, fue una de las canciones más vendidas del siglo XIX en partitura impresa.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL: Sol(1) La(2) Si(3) Do(4) Re(5). El Fa# es la única alteración de esta tonalidad.',
  estudiar_steps=[
      'Encuentra el Sol central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de Sol (Sol-Si-Re) con la izquierda, con calma.',
      'Busca en la partitura dónde cambia el dedo 1 de posición, y practica solo ese salto.',
      'Junta las manos despacio: la izquierda sostiene su acorde, la derecha se desliza a cada nueva posición.',
  ],
  checklist_items=[
      '¿Encuentro cada nueva posición sin mirar el teclado?',
      '¿El cambio de posición suena suave, sin saltos bruscos?',
      '¿Toco el acorde de Sol con seguridad?',
      '¿Puedo tocar la canción entera sin pararme?',
  ],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · MAYO',
  total_songs=28,
)

cfg22 = dict(
  kicker='MERCÈ · MAYO · MY GRANDFATHER\'S CLOCK',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Do, Re...) y di si es mayor o menor.',
  chords=[['G2', 'B2', 'D3'], ['C3', 'E3', 'G3'], ['D2', 'F#2', 'A2'], ['G2', 'B2', 'D3']],
  song_title="My Grandfather's Clock", song_key='Sol mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Sol mayor (I, IV, V...).',
  progression=['Sol', 'Do', 'Re', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el cambio de posición, en 4/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song22)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg22)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_22_Grandfathers_Clock.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
