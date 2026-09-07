import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'LUISA', ' bela-ciao.easy')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song1 = dict(
  num=1, title='Bela Ciao', subtitle='La Casa de Papel · arr. Anderson Miranda Fernandes',
  tonalidad='Sol mayor', compas='2/4', tempo='Moderato', forma='Estrofa',
  dificultad='Nivel hobby', manos='Melodía + acordes, sin complicarse',
  la_cancion='La versión de Bela Ciao de La Casa de Papel, en Sol mayor. Hoy, sin agobios: muchas frases empiezan con un pequeño silencio, y solo hay que esperar tranquila antes de entrar.',
  difficult_cc='cc. 1–4', difficult_title='El silencio antes de empezar: sin prisa',
  reto='esperar tranquila el pequeño silencio inicial, sin ponerte nerviosa ni adelantarte.',
  truco='cuenta despacio, sin agobiarte, y entra cuando te toque: no hay ninguna prisa.',
  sabias_que='"Bela Ciao" es un canto popular italiano que se hizo mundialmente famoso gracias a la serie La Casa de Papel.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL: Sol(1) La(2) Si(3) Do(4) Re(5). Solo el Fa# es distinto, tranquila.',
  estudiar_steps=[
      'Encuentra el Sol central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de Sol (Sol-Si-Re) con la izquierda, sin prisa.',
      'Practica esperar el pequeño silencio antes de entrar con la melodía.',
      'Junta las manos despacio: nada de agobios, solo disfrutar.',
  ],
  checklist_items=[
      '¿Espero tranquila el silencio, sin ponerme nerviosa?',
      '¿Toco el acorde de Sol sin complicarme?',
      '¿Disfruto la canción, sin prisa?',
      '¿Puedo tocar el principio sin pararme?',
  ],
  nivel_kicker='LUISA · NIVEL HOBBY · SEPTIEMBRE',
  total_songs=28,
)

cfg1 = dict(
  kicker='LUISA · SEPTIEMBRE · BELA CIAO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Do, Re...) y di si es mayor o menor.',
  chords=[['G2', 'B2', 'D3'], ['C3', 'E3', 'G3'], ['D2', 'F#2', 'A2'], ['G2', 'B2', 'D3']],
  song_title='Bela Ciao', song_key='Sol mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Sol mayor (I, IV, V...).',
  progression=['Sol', 'Do', 'Re', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el silencio y la entrada tranquila, en 2/4.',
  rhythm_events=([{'rest': True, 'dur': 'e'}] + [{'pitch': 'D4', 'dur': 'e'}] * 3) * 2,
  rhythm_time_sig=(2, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song1)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg1)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Luisa_01_Bela_Ciao.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
