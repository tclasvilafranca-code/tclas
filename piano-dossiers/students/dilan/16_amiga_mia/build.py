import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'Amiga mia-alejandro Sanz.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song16 = dict(
  num=16, title='Amiga Mía', subtitle='Alejandro Sanz',
  tonalidad='Re mayor', compas='4/4', tempo='Lento ♩≈70', forma='Estrofa-estribillo',
  dificultad='Un reto de pedal', manos='Melodía + acordes con pedal',
  la_cancion='Una balada lenta de Alejandro Sanz, en Re mayor. Aquí entra por primera vez el pedal de resonancia, para unir los acordes.',
  difficult_cc='cc. 1–8', difficult_title='El pedal de resonancia',
  reto='cambiar el pedal exactamente cuando cambia el acorde, ni antes ni después.',
  truco='practica el cambio de pedal muy despacio: suelta y vuelve a pisar en el mismo golpe en que tocas la nueva nota.',
  sabias_que='Alejandro Sanz es uno de los artistas españoles con más premios Grammy Latinos de la historia; "Amiga Mía" es una de sus baladas más queridas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('F#4', 3), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE mayor (el 3 en el Fa#); izquierda: acordes Re, Sol y La, unidos con el pedal.',
  ritmo_texto='Ritmo: compás de 4/4, lento — deja que el pedal sostenga el sonido mientras cuentas con calma.',
  estudiar_steps=['Busca RE y tócala 3 veces (tu nota casa).',
                   'Practica el cambio de pedal solo, sin tocar notas, marcando el gesto con el pie.',
                   'Los acordes Re-Sol-La con la izquierda, cambiando el pedal en cada uno.',
                   'Las dos manos juntas, con el pedal uniendo el sonido.'],
  checklist_items=['Encuentro RE y pongo bien los dedos.', 'Sé los acordes Re, Sol y La de memoria.',
                    'Cambio el pedal justo cuando cambia el acorde.', 'Junto las dos manos con el pedal.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · MAYO',
  total_songs=24,
)

cfg16 = dict(
  kicker='DILAN · MAYO · AMIGA MÍA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['E2', 'A2', 'C#3'], ['D3', 'F#3', 'A3']],
  song_title='Amiga Mía', song_key='Re mayor',
  progression_desc='Estos acordes sostienen la balada. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: negras tranquilas, con acordes largos que el pedal sostiene.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song16)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg16)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_16_Amiga_Mia.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
