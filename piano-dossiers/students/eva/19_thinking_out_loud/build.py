import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', ' THINKING OUT LOUD _ Ed Sheeran_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song19 = dict(
  num=19, title='Thinking Out Loud', subtitle='Ed Sheeran',
  tonalidad='Re mayor', compas='4/4', tempo='♩≈79', forma='Estrofa-estribillo',
  dificultad='Un reto de constancia', manos='Dibujo repetido + melodía',
  la_cancion='Una canción de Ed Sheeran en Re mayor. Aquí el reto es de constancia: el acompañamiento repite el mismo dibujo de acorde una y otra vez, como un rasgueo de guitarra que nunca se deforma.',
  difficult_cc='cc. 1–8', difficult_title='El dibujo que nunca cambia',
  reto='que la mano izquierda repita exactamente el mismo dibujo cada vez, sin que ninguna repetición suene distinta a las demás.',
  truco='memoriza el dibujo como una forma fija de la mano, no como notas sueltas — muévela entera de un acorde a otro.',
  sabias_que='Ed Sheeran escribió esta canción para su entonces pareja; se convirtió en una de las canciones de boda más populares de la década de 2010.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('A4', 5), ('G4', 4)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE (el 3 en la tecla negra Fa#); izquierda: el dibujo repetido sobre Re, Sol y La.',
  ritmo_texto='Ritmo: compás de 4/4 — el dibujo de la izquierda se repite exactamente igual, como un rasgueo.',
  estudiar_steps=['Busca RE y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: el dibujo repetido, memorizándolo como una forma fija.',
                   'Mano derecha sola: la melodía, tranquila.',
                   'Las dos manos juntas: el dibujo firme abajo, la melodía libre arriba.'],
  checklist_items=['Encuentro RE y pongo bien los dedos.', 'El dibujo de la izquierda es idéntico cada vez.',
                    'No deformo el dibujo cuando cambia de acorde.', 'Las dos manos suenan constantes y firmes.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · JUNIO',
  total_songs=21,
)

cfg19 = dict(
  kicker='EVA · JUNIO · THINKING OUT LOUD',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['A2', 'C#3', 'E3'], ['D3', 'F#3', 'A3']],
  song_title='Thinking Out Loud', song_key='Re mayor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Re mayor (I, IV, V...).',
  progression=['Re', 'La', 'Sol', 'La', 'Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real del dibujo repetido: corcheas idénticas, en 4/4.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'e'}, {'pitch': 'F#4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'}, {'pitch': 'F#4', 'dur': 'e'}] * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song19)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg19)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_19_Thinking_Out_Loud.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
