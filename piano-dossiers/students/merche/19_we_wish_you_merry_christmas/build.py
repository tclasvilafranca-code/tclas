import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'WE WISH YOU A MERRY CHRISTMAS.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song19 = dict(
  num=19, title='We Wish You a Merry Christmas', subtitle='Villancico tradicional · arr. Gilbert DeBenedetti',
  tonalidad='Sol mayor', compas='3/4', tempo='Alegre', forma='Estrofa con acordes de séptima',
  dificultad='Nivel básico', manos='Melodía + acordes de séptima que resuelven',
  la_cancion='El popular villancico "We Wish You a Merry Christmas", en Sol mayor. Los acordes de séptima (como Re7) crean tensión y piden resolver al acorde siguiente: hoy sentimos ese contraste.',
  difficult_cc='Toda la pieza', difficult_title='Los acordes de séptima que resuelven: tensión y descanso',
  reto='sentir cómo un acorde de séptima pide resolver, y disfrutar el momento en que sí lo hace.',
  truco='toca el acorde de séptima y espera un momento antes de resolver, escuchando cómo la tensión se relaja.',
  sabias_que='"We Wish You a Merry Christmas" es un villancico tradicional inglés del siglo XVI, y su estribillo es uno de los más reconocibles de la Navidad.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL: Sol(1) La(2) Si(3) Do(4) Re(5). El Fa# es la única alteración de esta tonalidad.',
  estudiar_steps=[
      'Encuentra el Sol central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de Re7 (Re-Fa#-La-Do) con la izquierda, sintiendo su tensión.',
      'Resuelve el Re7 al acorde de Sol, y siente cómo la tensión se relaja.',
      'Junta las manos despacio: la izquierda hace la tensión y la resolución, la derecha canta.',
  ],
  checklist_items=[
      '¿Siento la tensión del acorde de séptima?',
      '¿Disfruto el momento en que resuelve?',
      '¿Toco el acorde de Sol con seguridad?',
      '¿Puedo tocar la canción entera sin pararme?',
  ],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · ABRIL',
  total_songs=28,
)

cfg19 = dict(
  kicker='MERCÈ · ABRIL · WE WISH YOU A MERRY CHRISTMAS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Do, Re...) y di si es mayor o menor.',
  chords=[['G2', 'B2', 'D3'], ['C3', 'E3', 'G3'], ['D2', 'F#2', 'A2', 'C3'], ['G2', 'B2', 'D3']],
  song_title='We Wish You a Merry Christmas', song_key='Sol mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Sol mayor (I, IV, V7...).',
  progression=['Sol', 'Do', 'Re7', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el acorde de séptima que resuelve, en 3/4.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'h.'}] * 2,
  rhythm_time_sig=(3, 4),
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

    out_path = os.path.join(OUT_DIR, 'Merce_19_We_Wish_You_A_Merry_Christmas.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
