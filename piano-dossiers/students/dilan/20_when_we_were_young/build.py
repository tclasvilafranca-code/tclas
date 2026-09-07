import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', 'WHEN WE WERE YOUNG _ Adele Dm_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song20 = dict(
  num=20, title='When We Were Young', subtitle='Adele',
  tonalidad='Re menor', compas='4/4', tempo='Lento ♩≈68', forma='Estrofa-estribillo',
  dificultad='Un reto de teoría', manos='Melodía + acordes con bajo variado',
  la_cancion='Una balada de Adele, en Re menor. Los acordes llevan cifrado con barra (Fa/La): el bajo no siempre es la fundamental.',
  difficult_cc='cc. 1–8', difficult_title='El bajo que no es la fundamental',
  reto='entender que "Fa/La" es el mismo acorde de Fa, pero apoyado en la nota La en vez de en Fa.',
  truco='toca primero el acorde con su bajo normal, y luego solo cambia la nota más grave — el resto no se mueve.',
  sabias_que='Adele es una de las artistas con más premios Grammy de la historia; "When We Were Young" (2015) fue Grabación del Año en los Grammy de 2017.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F4', 3), ('G4', 4), ('F4', 3), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa', 'Sol', 'La', 'Sib', 'Do'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Rem',
  posicion_texto='Mano derecha en posición de RE menor (un dedo por tecla); izquierda: acordes Rem, Fa y Sib, con bajos que cambian.',
  ritmo_texto='Ritmo: compás de 4/4, lento — deja que el bajo se mueva con calma bajo el acorde.',
  estudiar_steps=['Busca RE y tócala 3 veces (tu nota casa).',
                   'El acorde de Fa, primero con bajo normal y luego con bajo en La (Fa/La).',
                   'Los acordes Rem-Fa-Sib con la izquierda, fijándote en cada bajo.',
                   'Las dos manos juntas, escuchando cómo camina el bajo.'],
  checklist_items=['Encuentro RE y pongo bien los dedos.', 'Sé los acordes Rem, Fa y Sib de memoria.',
                    'Entiendo qué significa el cifrado "Fa/La".', 'Junto las dos manos con el bajo caminando.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · MAYO',
  total_songs=24,
)

cfg20 = dict(
  kicker='DILAN · MAYO · WHEN WE WERE YOUNG',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'Bb4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Rem, Fa, Sib...) y di si es mayor o menor. Fíjate en cuál lleva un bajo distinto.',
  chords=[['D3', 'F3', 'A3'], ['F3', 'A3', 'C4'], ['A2', 'F3', 'A3'], ['D3', 'F3', 'Bb3']],
  song_title='When We Were Young', song_key='Re menor',
  progression_desc='Estos acordes sostienen la balada. Escribe el grado de cada uno en Re menor (i, III, VI...).',
  progression=['Rem', 'Fa', 'Sib', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: blancas tranquilas, como pide una balada lenta.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'h'}] * 4,
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

    out_path = os.path.join(OUT_DIR, 'Dilan_20_When_We_Were_Young.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
