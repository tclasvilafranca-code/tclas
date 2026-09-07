import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' YOUR SONG _ Elton John_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song24 = dict(
  num=24, title='Your Song', subtitle='Elton John · pieza de cierre del curso',
  tonalidad='Mib mayor', compas='4/4', tempo='Lento ♩≈66', forma='Estrofa-estribillo',
  dificultad='El cierre del curso', manos='Melodía fluida + acordes',
  la_cancion='La última canción del cuaderno de este curso, en Mib mayor: tres bemoles y una melodía que fluye sin cortes.',
  difficult_cc='cc. 1–8', difficult_title='Fluidez con muchos bemoles',
  reto='leer con soltura una tonalidad de tres bemoles, sin pararte nota a nota.',
  truco='localiza primero las tres teclas negras (Mib, Lab, Sib) antes de empezar, y deja que los dedos las recuerden solas.',
  sabias_que='"Your Song" (1970) fue el primer gran éxito de Elton John, con letra de Bernie Taupin; la escribieron en apenas veinte minutos.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('Eb4', 1), ('F4', 2), ('G4', 3), ('Ab4', 4), ('G4', 3), ('F4', 2)]] +
                     [{'pitch': 'Eb4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Mib', quinta_solfege='Sib',
  keyboard_notes=['Mib', 'Fa', 'Sol', 'Lab', 'Sib', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mib',
  posicion_texto='Mano derecha en posición de MIB mayor (el 1 y el 4 en teclas negras); izquierda: acordes Mib, Lab, Sib y Dom.',
  ritmo_texto='Ritmo: compás de 4/4, lento — deja que la melodía fluya como una frase larga, sin cortes.',
  estudiar_steps=['Busca MIB y tócala 3 veces (tu nota casa).',
                   'La melodía fluida, sin pararte en cada nota.',
                   'Los acordes Mib-Lab-Sib-Dom con la izquierda.',
                   'Las dos manos juntas: esta es tu última canción del curso. Disfrútala.'],
  checklist_items=['Encuentro MIB y pongo bien los dedos.', 'Leo los tres bemoles con soltura.',
                    'Sé los acordes Mib, Lab, Sib y Dom de memoria.', 'Junto las dos manos con fluidez, de principio a fin.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · JUNIO',
  total_songs=24,
)

cfg24 = dict(
  kicker='DILAN · JUNIO · YOUR SONG',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MIB, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('Eb4', 'F4'), ('Eb4', 'G4'), ('Eb4', 'Ab4'), ('Eb4', 'Bb4'), ('Eb4', 'C5'), ('Eb4', 'Eb5')],
  chords_desc='Identifica cada acorde: nómbralo (Mib, Lab, Sib, Dom...) y di si es mayor o menor.',
  chords=[['Eb3', 'G3', 'Bb3'], ['Ab2', 'C3', 'Eb3'], ['Bb2', 'D3', 'F3'], ['C3', 'Eb3', 'G3']],
  song_title='Your Song', song_key='Mib mayor',
  progression_desc='Estos acordes cierran el curso. Escribe el grado de cada uno en Mib mayor (I, IV, V, vi...).',
  progression=['Mib', 'Lab', 'Sib', 'Dom'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras tranquilas y fluidas, como cierre del curso.',
  rhythm_events=[{'pitch': 'G4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song24)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg24)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_24_Your_Song.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
