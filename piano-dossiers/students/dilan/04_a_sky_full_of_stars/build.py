import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' a-sky-full-of-stars-coldplay.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song4 = dict(
  num=4, title='A Sky Full of Stars', subtitle='Coldplay · con Avicii',
  tonalidad='Fa mayor', compas='4/4', tempo='Enérgico ♩≈100', forma='Estribillo repetido',
  dificultad='Un reto rítmico', manos='Acordes a dos manos',
  la_cancion='Un himno pop-electrónico de Coldplay. Las dos manos golpean el mismo pulso "largo-corto" a la vez, como un solo instrumento.',
  difficult_cc='cc. 1–4', difficult_title='El pulso largo-corto firme',
  reto='mantener el pulso largo-corto exacto en las dos manos a la vez, sin acelerar.',
  truco='cuenta "larga-y-corta" muy despacio antes de tocarlo, sintiendo dónde cae la nota corta.',
  sabias_que='Coldplay grabó esta canción junto al DJ y productor Avicii en 2014, mezclando el rock de la banda con sonido electrónico de baile.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4)]] +
                     [{'pitch': 'F4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA (un dedo por tecla, el 4 en el Sib); izquierda: acordes Fa, Sib y Do con el pulso largo-corto.',
  ritmo_texto='Ritmo: compás de 4/4, enérgico — el pulso largo-corto (negra con puntillo + corchea) se repite todo el rato.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: el pulso largo-corto, muy despacio.',
                   'Mano derecha sola: los acordes con el mismo pulso.',
                   'Las dos manos juntas: como un solo instrumento, sin acelerar.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'El pulso largo-corto suena firme.',
                    'Toco el Sib con el dedo 4 sin fallar.', 'Las dos manos golpean juntas, a la vez.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · OCTUBRE',
  total_songs=24,
)

cfg4 = dict(
  kicker='DILAN · OCTUBRE · A SKY FULL OF STARS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do, Rem...) y di si es mayor o menor.',
  chords=[['F4', 'A4', 'C5'], ['Bb4', 'D5', 'F5'], ['C4', 'E4', 'G4'], ['D4', 'F4', 'A4']],
  song_title='A Sky Full of Stars', song_key='Fa mayor',
  progression_desc='El estribillo se apoya en estos tres acordes de Fa mayor, con el pulso largo-corto encima. Escribe si cada uno es tónica (T), subdominante (SD) o dominante (D).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='function',
  rhythm_desc='Lee y marca el pulso largo-corto real: negra con puntillo + corchea, cuatro veces seguidas.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'}] * 4,
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

    out_path = os.path.join(OUT_DIR, 'Dilan_04_A_Sky_Full_Of_Stars.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
