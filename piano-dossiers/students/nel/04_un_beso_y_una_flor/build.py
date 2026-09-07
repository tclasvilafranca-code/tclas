import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'NEL', ' Un-beso-y-una-flor-nino-bravo_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song4 = dict(
  num=4, title='Un Beso y una Flor', subtitle='Nino Bravo',
  tonalidad='Fa mayor', compas='4/4', tempo='Allegro', forma='Estrofa-estribillo',
  dificultad='Un reto de entrada', manos='Melodía con anacrusa + acordes',
  la_cancion='Una canción de Nino Bravo en Fa mayor, alegre y con muchos acordes. El reto es de entrada: cada frase real arranca con un pequeño impulso (silencio y nota corta) antes del tiempo fuerte.',
  difficult_cc='cc. 1–8', difficult_title='La anacrusa: el mismo impulso cada vez',
  reto='hacer que la pequeña nota de entrada antes de cada frase suene exactamente igual las veces que se repite.',
  truco='piensa en la anacrusa como un trampolín: un salto corto y decidido que te lanza hacia la frase, no una nota que se toca de más.',
  sabias_que='Nino Bravo grabó "Un Beso y una Flor" en 1972; el cantante valenciano falleció poco después, en un accidente de tráfico, a los 28 años.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA mayor (el 4 en la tecla negra Sib); izquierda: los acordes Fa, Sib y Do.',
  ritmo_texto='Ritmo: compás de 4/4, Allegro — cada frase empieza con la misma pequeña anacrusa.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'La anacrusa sola, muchas veces, hasta que suene siempre igual.',
                   'Los acordes Fa-Sib-Do con la izquierda, sin prisa.',
                   'Las dos manos juntas, con la anacrusa siempre igual de decidida.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'Mi anacrusa suena igual cada vez que se repite.',
                    'Sé los acordes Fa, Sib y Do de memoria.', 'Las dos manos juntas mantienen el impulso.'],
  nivel_kicker='NEL · NIVEL MEDIO-ALTO · OCTUBRE',
  total_songs=22,
)

cfg4 = dict(
  kicker='NEL · OCTUBRE · UN BESO Y UNA FLOR',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='Un Beso y una Flor', song_key='Fa mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Sib'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: silencio de corchea y corcheas seguidas, la anacrusa de la canción, en 4/4.',
  rhythm_events=[{'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
                 {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'Bb4', 'dur': 'e'},
                 {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}] * 2,
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

    out_path = os.path.join(OUT_DIR, 'Nel_04_Un_Beso_Y_Una_Flor.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
