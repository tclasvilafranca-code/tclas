import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'Y-si-fuera-ella-alejandro-sanz.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song15 = dict(
  num=15, title='Y si fuera ella', subtitle='Alejandro Sanz',
  tonalidad='Fa mayor', compas='4/4', tempo='Balada ♩≈76', forma='Estrofa-estribillo',
  dificultad='Un reto de estiramiento', manos='Acorde abierto + melodía',
  la_cancion='Una balada de Alejandro Sanz en Fa mayor. El reto es de estiramiento: los acordes de la izquierda se abren (fundamental, quinta y una décima arriba) y la mano tiene que cubrirlos sin ponerse rígida.',
  difficult_cc='cc. 1–4', difficult_title='El acorde abierto: la mano que se estira, sin apretar',
  reto='cubrir el acorde extendido con la mano relajada, sin que los dedos se agarroten al estirarse.',
  truco='estira la mano despacio sobre el teclado, sin tocar, sintiendo la distancia antes de apretar las teclas.',
  sabias_que='"Y si fuera ella" pertenece al álbum "El alma al aire" (2000) de Alejandro Sanz, uno de los discos más aclamados de su carrera.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA mayor (un dedo por tecla); izquierda: los acordes Fa, Do, Rem y Sib, abiertos.',
  ritmo_texto='Ritmo: compás de 4/4, balada — con acordes abiertos que piden a la mano un buen estiramiento.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'Los acordes abiertos, uno a uno, sintiendo el estiramiento sin apretar.',
                   'La melodía sola, con la mano derecha.',
                   'Las dos manos juntas, con la izquierda estirada y relajada.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'El acorde abierto no me tensa la mano.',
                    'Sé los acordes Fa, Do, Rem y Sib de memoria.', 'Las dos manos juntas suenan relajadas.'],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · ABRIL',
  total_songs=22,
)

cfg15 = dict(
  kicker='JOSEP · ABRIL · Y SI FUERA ELLA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Do, Rem, Sib...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['C3', 'E3', 'G3'], ['D3', 'F3', 'A3'], ['Bb2', 'D3', 'F3']],
  song_title='Y si fuera ella', song_key='Fa mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V, vi...).',
  progression=['Fa', 'Do', 'Rem', 'Sib'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras tranquilas, en 4/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song15)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg15)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_15_Y_Si_Fuera_Ella.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
