import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', ' la-promesa-MELENDI.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song15 = dict(
  num=15, title='La Promesa', subtitle='Melendi',
  tonalidad='Sol mayor', compas='4/4', tempo='Pop ♩≈96', forma='Estrofa-estribillo',
  dificultad='Un reto de conducción', manos='Voces conducidas + melodía',
  la_cancion='Una canción de Melendi en Sol mayor. Aquí el reto es la conducción de voces: pasar de un acorde a otro sin que la mano salte, usando la nota común como eje.',
  difficult_cc='cc. 1–8', difficult_title='La nota común entre acordes',
  reto='encontrar la nota que se repite entre dos acordes seguidos y dejarla quieta mientras el resto se mueve.',
  truco='antes de cambiar de acorde, mira qué nota ya tienes puesta que también está en el siguiente.',
  sabias_que='"La Promesa" es una de las canciones más coreadas en los conciertos de Melendi; la escribió pensando en una relación que se rompe pero deja una promesa pendiente.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('D5', 5), ('C5', 4)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL (un dedo por tecla); izquierda: los acordes Sol, Do y Re, conducidos por su nota común.',
  ritmo_texto='Ritmo: compás de 4/4, pop — deja que los acordes se muevan suave, sin sobresaltos.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: busca la nota común entre cada dos acordes.',
                   'Mano derecha sola: la melodía, tranquila.',
                   'Las dos manos juntas: mueve los acordes por el camino más corto.'],
  checklist_items=['Encuentro SOL y pongo bien los dedos.', 'Encuentro la nota común entre acordes seguidos.',
                    'La mano izquierda no salta bruscamente.', 'Junto las dos manos con movimiento suave.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · MAYO',
  total_songs=21,
)

cfg15 = dict(
  kicker='EVA · MAYO · LA PROMESA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Do, Re...) y di si es mayor o menor.',
  chords=[['G3', 'B3', 'D4'], ['D3', 'F#3', 'A3'], ['C3', 'E3', 'G3'], ['G3', 'B3', 'D4']],
  song_title='La Promesa', song_key='Sol mayor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Sol mayor (I, IV, V...).',
  progression=['Sol', 'Re', 'Do', 'Sol', 'Re', 'Do', 'Sol', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras que se mueven suave, en 4/4.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song15)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg15)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_15_La_Promesa.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
