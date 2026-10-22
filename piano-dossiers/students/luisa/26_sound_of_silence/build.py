import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'LUISA', ' The-sound-of-silence-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song26 = dict(
  num=26, title='The Sound of Silence', subtitle='Simon & Garfunkel, arr. J. Sampol',
  tonalidad='Re menor', compas='4/4', tempo='Tranquilo', forma='Estrofa',
  dificultad='Nivel hobby', manos='Melodía + acordes, sin complicarse',
  la_cancion='La célebre canción de Simon & Garfunkel, en Re menor. Tiene un ambiente tranquilo y reflexivo: hoy solo hay que escucharla despacio, como quien escucha el silencio.',
  difficult_cc='cc. 1–8', difficult_title='El silencio que habla: escuchar por dentro',
  reto='tocar despacio y con calma, dejando espacio entre las frases, sin prisa.',
  truco='antes de tocar, respira y escucha el silencio de la habitación: esa calma es el espíritu de la canción.',
  sabias_que='"The Sound of Silence" (1964), de Simon & Garfunkel, se convirtió en un éxito inesperado cuando se remezcló con guitarras eléctricas en 1965.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F4', 3), ('E4', 2), ('D4', 1), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa', 'Sol', 'La', 'Sib', 'Do'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re menor',
  posicion_texto='Mano derecha en posición de RE menor: Re(1) Mi(2) Fa(3) Sol(4) La(5). El Sib es la única alteración de esta tonalidad.',
  estudiar_steps=[
      'Encuentra el Re central y coloca ahí el dedo 1 de tu mano derecha.',
      'Respira y escucha el silencio antes de empezar a tocar.',
      'Toca el acorde de Re menor con la izquierda, con calma.',
      'Junta las manos despacio, disfrutando del ambiente tranquilo de la canción.',
  ],
  checklist_items=[
      '¿Toco despacio, sin prisa?',
      '¿Dejo espacio entre las frases, como un silencio?',
      '¿Reconozco el Sib de esta tonalidad?',
      '¿Puedo tocar la canción entera sin agobiarme?',
  ],
  nivel_kicker='LUISA · NIVEL HOBBY · JUNIO',
  total_songs=28,
)

cfg26 = dict(
  kicker='LUISA · JUNIO · THE SOUND OF SILENCE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'Bb4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Rem, Solm, Lam...) y di si es mayor o menor.',
  chords=[['D3', 'F3', 'A3'], ['G2', 'Bb2', 'D3'], ['A2', 'C3', 'E3'], ['D3', 'F3', 'A3']],
  song_title='The Sound of Silence', song_key='Re menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re menor (i, iv, v...).',
  progression=['Rem', 'Solm', 'Lam', 'Rem'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la melodía tranquila, en 4/4.',
  rhythm_events=[{'pitch': 'F4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song26)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg26)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Luisa_26_The_Sound_Of_Silence.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
