import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'al-calor-del-amor-en-un-bar.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song12 = dict(
  num=12, title='Al Calor del Amor en un Bar', subtitle='Gabinete Caligari',
  tonalidad='Mi menor', compas='4/4', tempo='Allegretto ♩≈120', forma='Estrofa-estribillo',
  dificultad='Un reto de armonía', manos='Melodía + acordes',
  la_cancion='Un clásico del rock español, en Mi menor. Tiene un acorde "prestado" (Fa# mayor) que se escapa un instante de la tonalidad antes de resolver.',
  difficult_cc='cc. 5–8', difficult_title='El acorde sorpresa (Fa# mayor)',
  reto='reconocer que el Fa# mayor no pertenece a Mi menor, y sentir cómo tira hacia Si menor.',
  truco='toca Fa#-Sim varias veces seguidas hasta que tu oído reconozca la sorpresa antes de que tus dedos la toquen.',
  sabias_que='Gabinete Caligari fue un grupo español de rock de los años 80-90; "Al Calor del Amor en un Bar" es una de sus canciones más populares.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('G4', 3), ('F#4', 2), ('A4', 4), ('G4', 3), ('B4', 5)]] +
                     [{'pitch': 'E4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do', 'Re'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mim',
  posicion_texto='Mano derecha en posición de MI menor (el 2 en el Fa#); izquierda: acordes Mim, Sim, Lam, y el sorpresa Fa#.',
  ritmo_texto='Ritmo: compás de 4/4, allegretto — con chispa, sin arrastrar.',
  estudiar_steps=['Busca MI y tócala 3 veces (tu nota casa).',
                   'El salto Fa#-Sim, muy despacio, escuchando la sorpresa.',
                   'Los acordes Mim-Sim-Lam con la izquierda, uno por compás.',
                   'Las dos manos juntas, sin perder el pulso allegretto.'],
  checklist_items=['Encuentro MI y pongo bien los dedos.', 'Reconozco el acorde de Fa# mayor de oído.',
                    'Sé los acordes Mim, Sim y Lam de memoria.', 'Junto las dos manos con el pulso allegretto.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · ABRIL',
  total_songs=24,
)

cfg12 = dict(
  kicker='DILAN · ABRIL · AL CALOR DEL AMOR EN UN BAR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mim, Sim, Lam, Fa#...) y di si es mayor o menor.',
  chords=[['E3', 'G3', 'B3'], ['B2', 'D3', 'F#3'], ['A2', 'C3', 'E3'], ['F#3', 'A#3', 'C#4']],
  song_title='Al Calor del Amor en un Bar', song_key='Mi menor',
  progression_desc='Estos acordes aparecen en la canción, incluido el acorde sorpresa. Escribe el grado de cada uno en Mi menor (i, iv, v...) y marca cuál es "prestado".',
  progression=['Mim', 'Fa#', 'Sim', 'Mim'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras con chispa, allegretto.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song12)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg12)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_12_Al_Calor_Del_Amor_En_Un_Bar.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
