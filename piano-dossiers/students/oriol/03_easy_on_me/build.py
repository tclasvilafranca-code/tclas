import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ORIOL', 'Copia de easy-on-me-adele-simple-chorus.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song3 = dict(
  num=3, title='Easy on Me', subtitle='Adele, arr. Holmes',
  tonalidad='Fa mayor', compas='4/4', tempo='♩=120', forma='Estrofa',
  dificultad='Nivel medio', manos='Acordes anchos + melodía, sin complicarse',
  la_cancion='La balada de Adele, en Fa mayor. La izquierda toca acordes con la raíz y su octava a la vez: hoy solo hay que aprender a abrir la mano con calma, sin tensarla.',
  difficult_cc='cc. 1–8', difficult_title='Acordes anchos, sin miedo: abrir la mano con calma',
  reto='abrir la mano hasta la octava sin tensarla, buscando siempre la misma distancia entre los dedos.',
  truco='practica el salto de octava despacio, relajando la mano entre un acorde y el siguiente, antes de acelerar.',
  sabias_que='"Easy on Me" (2021) fue el primer sencillo del álbum "30" de Adele y debutó directamente en el número uno de las listas de varios países.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)]],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA: Fa(1) Sol(2) La(3) Sib(4) Do(5). El Sib es la única alteración de esta tonalidad.',
  estudiar_steps=[
      'Encuentra el Fa y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el salto de octava con la izquierda, relajando la mano entre acordes.',
      'Toca la melodía con la derecha, tranquila, sin prisa.',
      'Junta las manos despacio, comprobando que la mano izquierda no se tensa.',
  ],
  checklist_items=[
      '¿Abro la mano hasta la octava sin tensarla?',
      '¿Toco el acorde de Fa con seguridad?',
      '¿Reconozco el Sib de esta tonalidad?',
      '¿Puedo tocar la canción entera sin que la mano se canse?',
  ],
  nivel_kicker='ORIOL · NIVEL MEDIO · OCTUBRE',
  total_songs=15,
)

cfg3 = dict(
  kicker='ORIOL · OCTUBRE · EASY ON ME',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb2', 'D3', 'F3'], ['C2', 'E2', 'G2'], ['F2', 'A2', 'C3']],
  song_title='Easy on Me', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: los acordes anchos, en 4/4.',
  rhythm_events=[{'pitch': 'C4', 'dur': 'w'}] * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song3)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg3)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Oriol_03_Easy_On_Me.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
