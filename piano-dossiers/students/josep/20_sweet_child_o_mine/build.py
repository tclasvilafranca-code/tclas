import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'sweet-child-o-mine-guns-n-roses-easy-piano.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song20 = dict(
  num=20, title="Sweet Child O' Mine", subtitle="Guns N' Roses",
  tonalidad='Sib mayor', compas='4/4', tempo='♩≈125', forma='Riff-estrofa',
  dificultad='Un reto de posición', manos='Salto de posición + acordes',
  la_cancion="Un clásico de Guns N' Roses en Sib mayor. El reto es de posición: la mano tiene que saltar de un bloque de 5 dedos a otro, de golpe, sin buscar las teclas con la vista.",
  difficult_cc='cc. 1–4', difficult_title='El salto de posición: la mano cambia de sitio sin mirar',
  reto='saltar de una posición a otra sin dudar ni mirar el teclado, aterrizando limpio en la nueva posición.',
  truco='memoriza la distancia del salto con los ojos cerrados unos segundos antes de tocarlo, para que la mano "sepa" adónde va.',
  sabias_que='El riff inicial de "Sweet Child O\' Mine" (1987) lo compuso el guitarrista Slash casi en broma, calentando antes de un ensayo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('Bb4', 1), ('C5', 2), ('D5', 3), ('Eb5', 4), ('F5', 5), ('Eb5', 4)]] +
                     [{'pitch': 'Bb4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sib', quinta_solfege='Fa',
  keyboard_notes=['Sib', 'Do', 'Re', 'Mib', 'Fa', 'Sol', 'La'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sib',
  posicion_texto='Mano derecha en posición de SIB mayor (un dedo por tecla); izquierda: los acordes Sib, Lab y Mib.',
  ritmo_texto='Ritmo: compás de 4/4, con energía — la mano salta de posición de golpe.',
  estudiar_steps=['Busca SIB y tócala 3 veces (tu nota casa).',
                   'El salto de posición, muy despacio al principio, sintiendo la distancia.',
                   'Los acordes Sib-Lab-Mib con la izquierda.',
                   'Las dos manos juntas, con el salto cada vez más seguro.'],
  checklist_items=['Encuentro SIB y pongo bien los dedos.', 'El salto de posición aterriza limpio.',
                    'Sé los acordes Sib, Lab y Mib de memoria.', 'Las dos manos juntas sin dudar en el salto.'],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · JUNIO',
  total_songs=22,
)

cfg20 = dict(
  kicker='JOSEP · JUNIO · SWEET CHILD O’ MINE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SIB, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('Bb4', 'C5'), ('Bb4', 'D5'), ('Bb4', 'Eb5'), ('Bb4', 'F5'), ('Bb4', 'G5'), ('Bb4', 'Bb5')],
  chords_desc='Identifica cada acorde: nómbralo (Sib, Lab, Mib...) y di si es mayor o menor.',
  chords=[['Bb2', 'D3', 'F3'], ['Ab2', 'C3', 'Eb3'], ['Eb2', 'G2', 'Bb2'], ['Bb2', 'D3', 'F3']],
  song_title="Sweet Child O' Mine", song_key='Sib mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Sib mayor (I, bVII, IV...).',
  progression=['Sib', 'Lab', 'Mib', 'Sib'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: negras que saltan entre dos posiciones, en 4/4.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song20)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg20)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_20_Sweet_Child_O_Mine.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
