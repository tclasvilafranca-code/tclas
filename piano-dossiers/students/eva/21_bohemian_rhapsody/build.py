import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', 'bohemian-rhapsody_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song21 = dict(
  num=21, title='Bohemian Rhapsody', subtitle='Queen · Freddie Mercury (1975)',
  tonalidad='Sib mayor', compas='4/4', tempo='Moderato ♩≈66', forma='Sección de apertura (piano solo)',
  dificultad='La pieza-cumbre del año', manos='Melodía + acordes con séptima',
  la_cancion='La apertura de piano de una de las canciones más famosas de la historia, en Sib mayor. Es la pieza con más acordes distintos del año: el reto aquí es escuchar su color antes de mirar el nombre.',
  difficult_cc='cc. 1–8', difficult_title='Escuchar el color de cada acorde',
  reto='reconocer de oído si un acorde suena mayor, menor o con tensión (séptima), antes de confirmarlo con la vista.',
  truco='toca cada acorde y espera un segundo escuchándolo entero antes de decir su nombre en voz alta.',
  sabias_que='"Bohemian Rhapsody" (1975) mezcla balada, ópera y rock en casi 6 minutos sin estribillo repetido — algo casi único en la música pop.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('Bb4', 1), ('C5', 2), ('D5', 3), ('Eb5', 4), ('D5', 3), ('C5', 2)]] +
                     [{'pitch': 'Bb4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Sib', quinta_solfege='Fa',
  keyboard_notes=['Sib', 'Do', 'Re', 'Mib', 'Fa', 'Sol', 'La'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sib',
  posicion_texto='Mano derecha en posición de SIB mayor (el 1 y el 4 en teclas negras); izquierda: Sib, Do7, Fa, Solm, Mib y Dom.',
  ritmo_texto='Ritmo: compás de 4/4, moderato — los acordes cambian con frecuencia, así que escucha cada cambio antes de moverte.',
  estudiar_steps=['Busca SIB y tócala 3 veces (tu nota casa).',
                   'Escucha cada acorde de la izquierda con calma, adivinando su color antes de mirar el nombre.',
                   'Los seis acordes con la izquierda, comparando mayor, menor y con séptima.',
                   'Las dos manos juntas, todo el fragmento, dejando que el oído confirme cada cambio.'],
  checklist_items=['Encuentro SIB y pongo bien los dedos.', 'Distingo de oído un acorde mayor de uno menor.',
                    'Reconozco el color del acorde con séptima (Do7).', 'Junto las dos manos escuchando cada cambio.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · JUNIO',
  total_songs=21,
)

cfg21 = dict(
  kicker='EVA · JUNIO · BOHEMIAN RHAPSODY',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SIB, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('Bb4', 'C5'), ('Bb4', 'D5'), ('Bb4', 'Eb5'), ('Bb4', 'F5'), ('Bb4', 'G5'), ('Bb4', 'Bb5')],
  chords_desc='Escucha cada acorde y luego identifícalo: nómbralo (Sib, Do7, Fa, Solm...) y di si es mayor, menor o con séptima.',
  chords=[['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3', 'Bb3'], ['F2', 'A2', 'C3'], ['G2', 'Bb2', 'D3']],
  song_title='Bohemian Rhapsody', song_key='Sib mayor',
  progression_desc='Estos acordes abren la canción real. Escribe el grado de cada uno en Sib mayor (I, II7, IV, v...).',
  progression=['Sib', 'Do7', 'Fa', 'Solm'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras tranquilas, con acordes que cambian cada compás.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song21)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg21)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_21_Bohemian_Rhapsody.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
