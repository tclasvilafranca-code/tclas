import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', 'Amiga mia-alejandro Sanz.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song14 = dict(
  num=14, title='Amiga Mía', subtitle='Alejandro Sanz',
  tonalidad='Re mayor', compas='4/4', tempo='Balada ♩≈80', forma='Estrofa-estribillo',
  dificultad='Un reto de conexión', manos='Legato de dedos + acordes',
  la_cancion='Una balada de Alejandro Sanz en Re mayor. Aquí el reto es conectar los acordes SOLO con la mano, sin usar el pedal: sustituyendo dedos en las notas comunes.',
  difficult_cc='cc. 1–8', difficult_title='El legato de dedos, sin pedal',
  reto='encontrar la nota común entre un acorde y el siguiente y sostenerla con el mismo dedo, para que no se note el cambio.',
  truco='antes de tocar dos acordes seguidos, busca qué nota se repite entre ellos — esa es tu punto de unión.',
  sabias_que='Alejandro Sanz escribió esta canción pensando en la amistad verdadera; se convirtió en una de las más versionadas de su repertorio en directo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('A4', 5), ('G4', 4)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE (el 3 en la tecla negra Fa#); izquierda: los acordes Re, Sol y La, conectados con los dedos.',
  ritmo_texto='Ritmo: compás de 4/4, balada — deja que cada acorde se conecte con el siguiente sin pedal.',
  estudiar_steps=['Busca RE y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: busca la nota común entre cada dos acordes.',
                   'Mano derecha sola: la melodía, tranquila.',
                   'Las dos manos juntas: conecta todo con los dedos, sin pisar el pedal.'],
  checklist_items=['Encuentro RE y pongo bien los dedos.', 'Encuentro la nota común entre acordes seguidos.',
                    'Conecto los acordes sin usar el pedal.', 'Junto las dos manos con legato de dedos.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · MAYO',
  total_songs=21,
)

cfg14 = dict(
  kicker='EVA · MAYO · AMIGA MÍA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['E2', 'A2', 'C#3'], ['D3', 'F#3', 'A3']],
  song_title='Amiga Mía', song_key='Re mayor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Re mayor (I, IV, V...).',
  progression=['Re', 'La', 'Sol', 'La', 'Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras tranquilas y conectadas, en 4/4.',
  rhythm_events=[{'pitch': 'F#4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song14)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg14)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_14_Amiga_Mia.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
