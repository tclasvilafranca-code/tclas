import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'Popeye el marinerito.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song17 = dict(
  num=17, title='Popeye el marinerito', subtitle='Arr. A.C. Escobés',
  tonalidad='Sol mayor', compas='3/4', tempo='Allegretto', forma='Estrofa',
  dificultad='Reto motivador (nivel básico)', manos='Vals en Sol mayor + acordes',
  la_cancion='El tema del marinero más fuerte de los dibujos animados, ahora en compás de vals. Seguimos afianzando Sol mayor.',
  difficult_cc='Toda la pieza', difficult_title='Sol mayor, ahora en vals',
  reto='mantener el compás de vals mientras recuerdas el Fa sostenido.',
  truco='cuenta el vals en voz alta, "uno-dos-tres", mientras la izquierda sostiene el acorde.',
  sabias_que='Popeye apareció por primera vez en un cómic en 1929, y su música de cabecera es una de las más reconocibles del cine de animación clásico.',
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — Sol mayor, en vals',
  posicion_texto='Mano derecha en posición de SOL. El Fa de esta canción sigue siendo siempre sostenido, como en la anterior.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3)]] +
                     [{'pitch': 'C5', 'dur': 'h.', 'number': 4}],
  time_sig=(3, 4),
  nivel_kicker='ARNAU · RETO MOTIVADOR · CANCIÓN 17',
  total_songs=20,
)

cfg17 = dict(
  kicker='ARNAU · CANCIÓN 17 · POPEYE EL MARINERITO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Do, Re...) y di si es mayor o menor.',
  chords=[['G2', 'B2', 'D3'], ['C3', 'E3', 'G3'], ['D2', 'F#2', 'A2'], ['G2', 'B2', 'D3']],
  song_title='Popeye el marinerito', song_key='Sol mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Sol mayor (I, IV, V...).',
  progression=['Sol', 'Do', 'Re', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el vals con el Fa sostenido, en 3/4.',
  rhythm_events=[{'pitch': 'G4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'F#4', 'dur': 'q'}],
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song17)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg17)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Arnau_17_Popeye_El_Marinerito.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
