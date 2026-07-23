import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', 'Copia de  Deck the Halls (with Boughs of Holly) NAVIDAD.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song4 = dict(
  num=4, title='Deck the Halls', subtitle='Villancico tradicional galés, arr. Jim Paterson',
  tonalidad='Fa mayor', compas='4/4', tempo='Alegre', forma='Estrofa',
  dificultad='Nivel avanzado', manos='Melodía punteada + acordes',
  la_cancion='El popular villancico galés, en Fa mayor. Todo el arreglo se apoya en un ritmo punteado (larga-corta) que debe sonar con una proporción exacta de 3 a 1, no aproximada.',
  difficult_cc='Toda la pieza', difficult_title='El ritmo punteado: largo-corto, con precisión exacta',
  reto='sentir la subdivisión interna del punteado, tocando la nota corta exactamente donde corresponde, ni antes ni después.',
  truco='subdivide mentalmente cada figura larga en tres partes iguales antes de tocar la corta: la corta ocupa siempre la última de esas tres partes.',
  sabias_que='"Deck the Halls" desciende de una melodía galesa de Año Nuevo del siglo XVI ("Nos Galan"); la letra en inglés que conocemos hoy es del siglo XIX.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4), ('A4', 3), ('G4', 2)]],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA: Fa(1) Sol(2) La(3) Sib(4) Do(5). El Sib es la única alteración de esta tonalidad.',
  estudiar_steps=[
      'Marca el pulso y subdivide cada figura larga en tres partes iguales mentalmente.',
      'Toca solo los ritmos punteados con una sola nota repetida, sin melodía, hasta que la proporción sea exacta.',
      'Añade la melodía real sobre ese mismo ritmo ya interiorizado.',
      'Junta las manos, comprobando que el punteado no se redondea al añadir el acorde.',
  ],
  checklist_items=[
      '¿La nota corta llega exactamente en su lugar, ni antes ni después?',
      '¿Mantengo la proporción 3 a 1 en todas las figuras punteadas?',
      '¿Reconozco el acorde de Sol como dominante secundaria prestada?',
      '¿Puedo tocar la pieza entera sin que el punteado se redondee?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · OCTUBRE',
  total_songs=16,
)

cfg4 = dict(
  kicker='SANDI · OCTUBRE · DECK THE HALLS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do, Sol...) y di si es mayor o menor.',
  chords=[['F3', 'A3', 'C4'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['G2', 'B2', 'D3']],
  song_title='Deck the Halls', song_key='Fa mayor',
  progression_desc='Estos son algunos acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V, V/V...).',
  progression=['Fa', 'Sib', 'Do', 'Sol'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: el punteado exacto, en 4/4.',
  rhythm_events=[{'pitch': 'F4', 'dur': 'q.'}, {'pitch': 'G4', 'dur': 'e'}] * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song4)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg4)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Sandi_04_Deck_The_Halls.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
