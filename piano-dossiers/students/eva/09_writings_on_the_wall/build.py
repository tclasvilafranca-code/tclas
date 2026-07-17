import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', "WRITING_S ON THE WALL _ Sam Smith_.pdf")
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song9 = dict(
  num=9, title="Writing's on the Wall", subtitle='Sam Smith · James Bond',
  tonalidad='Fa mayor', compas='4/4', tempo='Balada ♩≈88', forma='Estrofa-estribillo',
  dificultad='Un reto de amplitud', manos='Acordes amplios + melodía',
  la_cancion='El tema de James Bond "Spectre", en Fa mayor. Aquí el reto no es la velocidad: son los acordes amplios, que abarcan una octava entera en la izquierda.',
  difficult_cc='cc. 1–8', difficult_title='Los acordes amplios, sin tensión',
  reto='abrir la mano para el acorde de octava sin forzar los dedos ni levantar la muñeca.',
  truco='estírate desde la muñeca, no desde los dedos — piensa en "alcanzar", no en "estirar".',
  sabias_que='Sam Smith ganó el Óscar a Mejor Canción Original por este tema en 2016, y batió el récord de la nota más grave alcanzada por una canción de James Bond.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA (el 4 en la tecla negra Sib); izquierda: acordes amplios de Fa, Sib y Do, de octava completa.',
  ritmo_texto='Ritmo: compás de 4/4, balada — deja que cada acorde amplio suene entero, sin cortarlo.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: el acorde amplio, sintiendo la octava sin forzar.',
                   'Mano derecha sola: la melodía, relajada.',
                   'Las dos manos juntas: la izquierda abierta, la derecha libre encima.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'Abro la mano para el acorde de octava sin dolor.',
                    'No tenso la muñeca al estirar.', 'Junto las dos manos con amplitud y calma.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · ENERO',
  total_songs=21,
)

cfg9 = dict(
  kicker='EVA · ENERO · WRITING’S ON THE WALL',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F3', 'A3', 'C4'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['F3', 'A3', 'C4']],
  song_title="Writing's on the Wall", song_key='Fa mayor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa', 'Sib', 'Do', 'Fa', 'Sib'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de los acordes amplios: blancas sostenidas, sin prisa.',
  rhythm_events=[{'pitch': 'C4', 'dur': 'h'}] * 4,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song9)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg9)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_09_Writings_On_The_Wall.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
