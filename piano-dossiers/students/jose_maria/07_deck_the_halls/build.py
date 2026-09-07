import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', ' Deck the Halls (with Boughs of Holly) NAVIDAD.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song7 = dict(
  num=7, title='Deck the Halls', subtitle='Tradicional · arr. Jim Paterson',
  tonalidad='Fa mayor', compas='4/4', tempo='Alegre, sin prisa', forma='Estrofa',
  dificultad='Para disfrutar, sin prisa', manos='Saltos cortos + acordes',
  la_cancion='Un villancico alegre en Fa mayor. Aquí cuidamos que la muñeca se quede suelta en cada salto pequeño, sin ponerse rígida.',
  difficult_cc='cc. 1–8', difficult_title='Saltos pequeños, muñeca suelta',
  reto='que la muñeca acompañe cada salto sin tensarse, incluso cuando la mano se mueve varias veces seguidas.',
  truco='antes de saltar, suelta la muñeca como si sacudieras una gota de agua — luego apoya la mano con esa misma soltura.',
  sabias_que='"Deck the Halls" es un villancico galés cuya melodía es mucho más antigua que su letra en inglés, que data del siglo XIX.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA mayor (el 4 en la tecla negra Sib); izquierda: los acordes Fa, Sib y Do, tranquilos.',
  ritmo_texto='Ritmo: compás de 4/4, alegre — pero sin que la muñeca se tense en los saltos.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'Los saltos pequeños solos, sintiendo la muñeca suelta.',
                   'Los acordes Fa-Sib-Do con la izquierda, sin prisa.',
                   'Las dos manos juntas, con la muñeca siempre relajada.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'La muñeca no se tensa en los saltos.',
                    'Sé los acordes Fa, Sib y Do de memoria.', 'Las dos manos juntas suenan alegres y relajadas.'],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · DICIEMBRE',
  total_songs=21,
)

cfg7 = dict(
  kicker='JOSÉ MARÍA · DICIEMBRE · DECK THE HALLS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='Deck the Halls', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Sib'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras alegres, en 4/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song7)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg7)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'JoseMaria_07_Deck_The_Halls.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
