import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'WRITING_S ON THE WALL _ Sam Smith_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song6 = dict(
  num=6, title="Writing's on the Wall", subtitle='Sam Smith · de la película "Spectre" (James Bond)',
  tonalidad='Fa mayor', compas='4/4', tempo='Lento expresivo ♩≈68', forma='Estrofa-estribillo',
  dificultad='Un reto expresivo', manos='Melodía + acordes',
  la_cancion='Balada dramática de la banda sonora de James Bond. Aquí el reto no son las notas: es tocar con matices reales de volumen.',
  difficult_cc='cc. 1–8', difficult_title='Matices: piano y forte de verdad',
  reto='que se note de verdad la diferencia entre tocar suave y tocar fuerte, sin que todo suene igual.',
  truco='toca la misma frase tres veces seguidas cambiando solo el volumen, exagerando al principio para sentir la diferencia.',
  sabias_que='Sam Smith escribió esta canción para "Spectre" (2015), la 24ª película de James Bond. Ganó el Oscar y el Globo de Oro a la Mejor Canción Original.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4)]] +
                     [{'pitch': 'F4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA (un dedo por tecla, el 4 en el Sib); izquierda: acordes Fa, Sib y Do.',
  ritmo_texto='Ritmo: compás de 4/4, lento y expresivo — cuenta con calma, sin prisa por llegar a la siguiente nota.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'Toca la melodía tres veces: piano, forte, y con crescendo real.',
                   'Los acordes Fa-Sib-Do con la izquierda, uno por compás.',
                   'Las dos manos juntas, cuidando el volumen de cada una por separado.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'Sé tocar la misma frase en piano y en forte.',
                    'Toco el paso cromático (Do-Do#-Re) sin dudar.', 'Junto las dos manos con los matices.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · ENERO',
  total_songs=8,
)

cfg6 = dict(
  kicker='DILAN · ENERO · WRITING’S ON THE WALL',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do, Rem...) y di si es mayor o menor.',
  chords=[['F4', 'A4', 'C5'], ['Bb4', 'D5', 'F5'], ['C4', 'E4', 'G4'], ['D4', 'F4', 'A4']],
  song_title="Writing's on the Wall", song_key='Fa mayor',
  progression_desc='La balada se apoya en estos tres acordes de Fa mayor. Escribe si cada uno es tónica (T), subdominante (SD) o dominante (D).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo: frase larga y tranquila, con una nota final que se sostiene.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'q'}] * 6 + [{'pitch': 'B4', 'dur': 'h'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song6)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg6)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_06_Writings_On_The_Wall.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
