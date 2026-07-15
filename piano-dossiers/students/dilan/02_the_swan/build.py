import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'the-swan.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song2 = dict(
  num=2, title='The Swan (El Cisne)', subtitle='Camille Saint-Saëns · de "El Carnaval de los Animales"',
  tonalidad='Sol mayor', compas='3/4', tempo='Andante ♩≈96', forma='Tema con frases largas',
  dificultad='Un reto de control', manos='Melodía legato + arpegio',
  la_cancion='Una de las piezas más bellas del repertorio clásico: una melodía larga y serena que "canta" sobre un acompañamiento que fluye como el agua.',
  difficult_cc='cc. 1–8', difficult_title='El legato de verdad',
  reto='conectar cada nota con la siguiente sin cortar el sonido, sin golpes.',
  truco='imagina que la melodía es un solo movimiento continuo del brazo, sin saltos entre teclas.',
  sabias_que='Saint-Saëns compuso "El Cisne" en 1886 para "El Carnaval de los Animales", pero prohibió que se publicara en vida: temía que eclipsara el resto de su obra. No se estrenó en público hasta después de su muerte, en 1922.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('B4', 3), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  time_sig=(3, 4),
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL (un dedo por tecla); izquierda: arpegio fluido sobre Sol, Do y Re.',
  ritmo_texto='Ritmo: compás de 3/4, Andante — cuenta 1-2-3 por dentro, sin marcarlo con golpes.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: el arpegio fluido, como el agua.',
                   'Mano derecha sola, muy legato, sin levantar el dedo antes de tiempo.',
                   'Las dos manos juntas: despacio, dejando que la melodía respire.'],
  checklist_items=['Encuentro SOL y pongo bien los dedos.', 'La izquierda fluye sin cortes.',
                    'La derecha conecta cada nota con la siguiente (legato).', 'Junto las dos manos, con calma.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · SEPTIEMBRE-OCTUBRE',
  total_songs=24,
)

cfg2 = dict(
  kicker='DILAN · SEPTIEMBRE-OCTUBRE · THE SWAN',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Do, Re, Mim...) y di si es mayor o menor.',
  chords=[['G4', 'B4', 'D5'], ['C4', 'E4', 'G4'], ['D4', 'F#4', 'A4'], ['E4', 'G4', 'B4']],
  song_title='The Swan', song_key='Sol mayor',
  progression_desc='El Cisne está escrito en notación clásica, sin cifrado de acordes — pero toda la pieza se sostiene sobre estos tres acordes. Escribe si cada uno es tónica (T), subdominante (SD) o dominante (D).',
  progression=['Sol', 'Do', 'Re', 'Sol'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real de la frase: una nota larga que respira y luego tres negras que avanzan, en 3/4.',
  rhythm_events=([{'pitch': 'B4', 'dur': 'h.'}] + [{'pitch': 'B4', 'dur': 'q'}] * 3) * 2,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song2)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg2)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Dilan_02_The_Swan.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
