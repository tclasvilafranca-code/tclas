import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'ARNAU', 'ElSubmarinoAmarillo-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song16 = dict(
  num=16, title='El Submarino Amarillo', subtitle='John Lennon y Paul McCartney, arr. A.C. Escobés',
  tonalidad='Sol mayor', compas='4/4', tempo='Allegro', forma='Estrofa',
  dificultad='Reto motivador (nivel básico)', manos='Melodía con Fa sostenido + acordes',
  la_cancion='Un clásico de los Beatles. Nuestra primera canción en Sol mayor: un sostenido, en el Fa, que se anuncia una vez al principio.',
  difficult_cc='Toda la pieza', difficult_title='La nueva tonalidad: Sol mayor',
  reto='acordarte del Fa sostenido cada vez, sin que te lo recuerde una alteración al lado de la nota.',
  truco='toca solo los Fa de la canción, uno por uno, para memorizar dónde están.',
  sabias_que='"Yellow Submarine" (1966) la cantó Ringo Starr, y es una de las canciones más alegres y coreadas de los Beatles.',
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL: Sol(1) La(2) Si(3) Do(4) Re(5). El Fa de esta canción es siempre sostenido.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4)]] +
                     [{'pitch': 'D5', 'dur': 'h', 'number': 5}, {'pitch': 'G4', 'dur': 'h', 'number': 1}],
  time_sig=(4, 4),
  nivel_kicker='ARNAU · RETO MOTIVADOR · CANCIÓN 16',
  total_songs=20,
)

cfg16 = dict(
  kicker='ARNAU · CANCIÓN 16 · EL SUBMARINO AMARILLO',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Do, Re...) y di si es mayor o menor.',
  chords=[['G2', 'B2', 'D3'], ['C3', 'E3', 'G3'], ['D2', 'F#2', 'A2'], ['G2', 'B2', 'D3']],
  song_title='El Submarino Amarillo', song_key='Sol mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Sol mayor (I, IV, V...).',
  progression=['Sol', 'Do', 'Re', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la frase con el Fa sostenido, en 4/4.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}, {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'F#4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}],
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

    out_path = os.path.join(OUT_DIR, 'Arnau_16_El_Submarino_Amarillo.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
