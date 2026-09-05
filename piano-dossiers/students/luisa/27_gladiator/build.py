import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'LUISA', '-gladiator-by-hans-zimmer-easy-version.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song27 = dict(
  num=27, title='Gladiator (Honor Him)', subtitle='Hans Zimmer, arr. fácil',
  tonalidad='Re mayor', compas='3/4', tempo='Andante, solemne', forma='Estrofa',
  dificultad='Nivel hobby', manos='Melodía + acordes, sin complicarse',
  la_cancion='El tema de la banda sonora de Gladiator, de Hans Zimmer, en Re mayor. Suena grande y valiente, como una hazaña: hoy solo hay que tocarla sintiéndote fuerte por dentro.',
  difficult_cc='cc. 1–6', difficult_title='Una melodía heroica: siéntete valiente',
  reto='tocar con seguridad esta melodía tan grande, sin ponerte nerviosa.',
  truco='antes de tocar, respira hondo e imagina que eres valiente: la música suena mejor con esa seguridad.',
  sabias_que='El tema "Honor Him" de Gladiator (2000), compuesto por Hans Zimmer y Lisa Gerrard, es uno de los más reconocidos del cine.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('E4', 2), ('D4', 1), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El Fa# es la primera tecla negra de esta tonalidad.',
  estudiar_steps=[
      'Encuentra el Re central y coloca ahí el dedo 1 de tu mano derecha.',
      'Respira hondo e imagina que eres valiente antes de empezar.',
      'Toca el acorde de Re con la izquierda, con seguridad.',
      'Junta las manos despacio, sintiéndote fuerte mientras tocas.',
  ],
  checklist_items=[
      '¿Toco con seguridad, sin ponerme nerviosa?',
      '¿Toco el acorde de Re con firmeza?',
      '¿Reconozco el Fa# de esta tonalidad?',
      '¿Puedo tocar la melodía entera sin pararme?',
  ],
  nivel_kicker='LUISA · NIVEL HOBBY · JUNIO',
  total_songs=28,
)

cfg27 = dict(
  kicker='LUISA · JUNIO · GLADIATOR (HONOR HIM)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['A2', 'C#3', 'E3'], ['D3', 'F#3', 'A3']],
  song_title='Gladiator (Honor Him)', song_key='Re mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la melodía valiente, en 3/4.',
  rhythm_events=[{'pitch': 'F#4', 'dur': 'h.'}] * 2,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song27)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg27)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Luisa_27_Gladiator.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
