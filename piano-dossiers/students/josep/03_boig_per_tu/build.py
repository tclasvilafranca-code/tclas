import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', ' Boig per tu, Sau_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song3 = dict(
  num=3, title='Boig per tu', subtitle='Sau · arr. Pilar Sanz',
  tonalidad='La menor', compas='4/4', tempo='♩≈92', forma='Estrofa-estribillo',
  dificultad='Un reto de ritmo', manos='Melodía punteada + acordes',
  la_cancion='Una canción de Sau en La menor. El reto es rítmico: un vaivén de corchea con puntillo y semicorchea que recorre toda la melodía, con un Sol# que empuja hacia el La final.',
  difficult_cc='cc. 1–8', difficult_title='El ritmo punteado',
  reto='marcar con claridad la diferencia entre la nota larga (con puntillo) y la corta que la sigue, sin igualarlas.',
  truco='divide mentalmente cada negra en cuatro y cuenta "ta-ta-ta-ta": la nota larga dura tres de esos golpes, la corta solo uno.',
  sabias_que='Sau fue uno de los grupos pioneros del rock català; "Boig per tu" (1975) es una de sus canciones más emblemáticas.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('E5', 5), ('D5', 4)]] +
                     [{'pitch': 'A4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La menor',
  posicion_texto='Mano derecha en posición de LA menor (un dedo por tecla); izquierda: los acordes Lam, Rem y Mi (con el Sol# de la sensible).',
  ritmo_texto='Ritmo: compás de 4/4 — el vaivén punteado (larga-corta) se repite en casi toda la melodía.',
  estudiar_steps=['Busca LA y tócala 3 veces (tu nota casa).',
                   'El ritmo punteado a cámara lenta, contando por dentro.',
                   'Los acordes Lam-Rem-Mi con la izquierda, sin prisa.',
                   'Las dos manos juntas, con el punteado siempre claro.'],
  checklist_items=['Encuentro LA y pongo bien los dedos.', 'Distingo claramente la nota larga de la corta.',
                    'Sé los acordes Lam, Rem y Mi de memoria.', 'El punteado no se difumina al juntar las manos.'],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · OCTUBRE',
  total_songs=22,
)

cfg3 = dict(
  kicker='JOSEP · OCTUBRE · BOIG PER TU',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D3', 'F3', 'A3'], ['E3', 'G#3', 'B3'], ['A2', 'C3', 'E3']],
  song_title='Boig per tu', song_key='La menor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en La menor (i, iv, V...).',
  progression=['Lam', 'Rem', 'Mi', 'Lam'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real de la melodía: corchea con puntillo y semicorchea, en 4/4.',
  rhythm_events=[{'pitch': 'C5', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'q'},
                 {'pitch': 'E4', 'dur': 'q.'}, {'pitch': 'D4', 'dur': 'e'}, {'pitch': 'C4', 'dur': 'q'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song3)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg3)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_03_Boig_Per_Tu.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
