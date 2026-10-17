import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JULIA', 'BELLA Y BESTIA_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song20 = dict(
  num=20, title='Beauty and Beast', subtitle='La Bella y la Bestia, arr. Naf',
  tonalidad='Fa mayor', compas='4/4', tempo='♩ = 80', forma='Estrofa',
  dificultad='Nivel inicial, con toque extra', manos='Melodía que vuela una octava + acorde repetido',
  la_cancion='El famoso tema de La Bella y la Bestia, en Fa mayor. La propia partitura pide que la mano derecha toque una octava más arriba de lo escrito: ¡la melodía vuela alto!',
  difficult_cc='cc. 1–4', difficult_title='La octava que vuela: la derecha toca más alto',
  reto='acordarte de tocar una octava más arriba de lo que ves escrito, sin perder la posición de la mano.',
  truco='antes de empezar, busca con la mano la octava de arriba y quédate ahí todo el rato, como si fuera tu nueva casa.',
  sabias_que='La Bella y la Bestia (1991) fue la primera película de animación de la historia nominada al Óscar a mejor película.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA: Fa(1) Sol(2) La(3) Sib(4) Do(5). El Sib es la única tecla negra de esta posición.',
  estudiar_steps=[
      'Encuentra el Fa central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de Fa (Fa-La-Do) con la mano izquierda, repitiéndolo con calma.',
      'Ahora sube una octava con la melodía: busca el Fa de arriba y quédate ahí.',
      'Junta las manos despacio: la izquierda repite su acorde, la derecha vuela arriba.',
  ],
  checklist_items=[
      '¿Encuentras el Sib sin dudar?',
      '¿Tocas la melodía una octava más arriba de lo escrito?',
      '¿El acorde de la izquierda suena igual de firme en cada tiempo?',
      '¿Puedes tocar la canción entera sin pararte?',
  ],
  nivel_kicker='JULIA · NIVEL INICIAL · MAYO',
  total_songs=24,
)

cfg20 = dict(
  kicker='JULIA · MAYO · BEAUTY AND BEAST',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='Beauty and Beast', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: silencio, corcheas que despegan y nota larga, en 4/4.',
  rhythm_events=([{'rest': True, 'dur': 'h'}] + [{'pitch': 'A4', 'dur': 'e'}] * 4 + [{'pitch': 'C5', 'dur': 'h'}]),
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song20)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg20)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Julia_20_Beauty_And_Beast.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
