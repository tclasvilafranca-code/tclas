import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' THINKING OUT LOUD _ Ed Sheeran_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song21 = dict(
  num=21, title='Thinking Out Loud', subtitle='Ed Sheeran',
  tonalidad='Re mayor', compas='4/4', tempo='Rápido ♩≈145', forma='Estrofa-estribillo',
  dificultad='Un reto de igualdad', manos='Corcheas continuas + acordes',
  la_cancion='Una balada de Ed Sheeran, en Re mayor, pero tocada rápido. El reto es que las corcheas suenen todas exactamente iguales.',
  difficult_cc='cc. 1–8', difficult_title='Corcheas iguales a tempo rápido',
  reto='que ninguna corchea se acelere ni se atropelle con la siguiente.',
  truco='practica con un pulso interno muy claro, contando "1-y-2-y-3-y-4-y" en voz alta antes de tocar rápido.',
  sabias_que='"Thinking Out Loud" (2014) ganó el Grammy a la Canción del Año en 2016, y es una de las canciones de boda más populares en todo el mundo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('G4', 4), ('F#4', 3), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE mayor (el 3 en el Fa#); izquierda: acordes Re, Sol y La, largos y sostenidos.',
  ritmo_texto='Ritmo: compás de 4/4, rápido — cada corchea debe durar exactamente lo mismo que la anterior.',
  estudiar_steps=['Busca RE y tócala 3 veces (tu nota casa).',
                   'Las corcheas muy despacio primero, comprobando que son iguales.',
                   'Los acordes Re-Sol-La con la izquierda, largos y sostenidos.',
                   'Las dos manos juntas, subiendo la velocidad solo cuando salga igual.'],
  checklist_items=['Encuentro RE y pongo bien los dedos.', 'Mis corcheas suenan todas iguales de largas.',
                    'Sé los acordes Re, Sol y La de memoria.', 'Junto las dos manos sin acelerar sin querer.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · JUNIO',
  total_songs=24,
)

cfg21 = dict(
  kicker='DILAN · JUNIO · THINKING OUT LOUD',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['E2', 'A2', 'C#3'], ['D3', 'F#3', 'A3']],
  song_title='Thinking Out Loud', song_key='Re mayor',
  progression_desc='Estos acordes sostienen la canción. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'La', 'Sol', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: corcheas continuas, todas exactamente iguales.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'e', 'beam': i // 4} for i in range(16)],
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

    out_path = os.path.join(OUT_DIR, 'Dilan_21_Thinking_Out_Loud.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
