import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'EVA', 'WHEN WE WERE YOUNG _ Adele Dm_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song18 = dict(
  num=18, title='When We Were Young', subtitle='Adele',
  tonalidad='Re menor', compas='4/4', tempo='♩≈68', forma='Estrofa-estribillo',
  dificultad='Un reto de bajo', manos='Bajo caminante + melodía',
  la_cancion='Una balada de Adele en Re menor. Aquí el reto es físico, no teórico: sentir el bajo caminando escalón a escalón bajo la mano, sin dejar huecos.',
  difficult_cc='cc. 1–8', difficult_title='El bajo que camina, sin pararse',
  reto='que el bajo baje y suba escalón a escalón sin ningún hueco ni tropiezo entre nota y nota.',
  truco='imagina que el pulgar de la izquierda está bajando una escalera, un peldaño exacto por cada tiempo.',
  sabias_que='Adele escribió esta canción tras reencontrarse con un amor de juventud; el título hace referencia a lo distintos que somos con el paso del tiempo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F4', 3), ('G4', 4), ('A4', 5), ('G4', 4)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa', 'Sol', 'La', 'Sib', 'Do'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re menor',
  posicion_texto='Mano derecha en posición de RE menor (un dedo por tecla); izquierda: los acordes Rem, Sib, Fa y Sol, con el bajo caminando.',
  ritmo_texto='Ritmo: compás de 4/4 — siente el bajo caminando escalón a escalón, sin ningún hueco.',
  estudiar_steps=['Busca RE menor y tócala 3 veces (tu nota casa).',
                   'Mano izquierda sola: el bajo caminando, paso a paso.',
                   'Mano derecha sola: la melodía, tranquila.',
                   'Las dos manos juntas: el bajo camina sin parar bajo la melodía.'],
  checklist_items=['Encuentro RE menor y pongo bien los dedos.', 'El bajo baja y sube sin ningún hueco.',
                    'La izquierda no se contagia del movimiento de la derecha.', 'Las dos manos suenan como un caminar constante.'],
  nivel_kicker='EVA · NIVEL MEDIO-ALTO · MAYO',
  total_songs=21,
)

cfg18 = dict(
  kicker='EVA · MAYO · WHEN WE WERE YOUNG',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'Bb4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Rem, Fa, Sib...) y di si es mayor o menor.',
  chords=[['D3', 'F3', 'A3'], ['Bb2', 'D3', 'F3'], ['F3', 'A3', 'C4'], ['G2', 'Bb2', 'D3']],
  song_title='When We Were Young', song_key='Re menor',
  progression_desc='Esta es la progresión real de la canción. Escribe el grado de cada acorde en Re menor (i, VI, III...).',
  progression=['Rem', 'Sib', 'Fa', 'Sol', 'Rem', 'Sib', 'Fa', 'Sol'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real del bajo: negras que caminan escalón a escalón, en 4/4.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'q'}, {'pitch': 'C4', 'dur': 'q'}, {'pitch': 'Bb3', 'dur': 'q'}, {'pitch': 'A3', 'dur': 'q'}] * 2,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song18)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg18)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Eva_18_When_We_Were_Young.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
