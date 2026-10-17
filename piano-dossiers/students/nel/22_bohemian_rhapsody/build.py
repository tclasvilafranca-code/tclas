import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'NEL', 'Bohemian Rhapsody.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song22 = dict(
  num=22, title='Bohemian Rhapsody', subtitle='Queen (apertura, piano solo)',
  tonalidad='Sib mayor', compas='4/4 / 5/4 (mixto)', tempo='Moderato ♩≈66', forma='Sección de apertura',
  dificultad='Un reto de compás', manos='Acordes + melodía, compás cambiante',
  la_cancion='La apertura de "Bohemian Rhapsody" de Queen, en Sib mayor. El reto es de compás: de vez en cuando aparece un compás de 5/4, un tiempo más de lo habitual.',
  difficult_cc='cc. 1–8', difficult_title='El compás de 5: un tiempo más de lo habitual',
  reto='sentir el tiempo extra del compás de 5/4 sin acortarlo ni perderlo por el camino.',
  truco='cuenta en voz alta "1-2-3-4-5" en ese compás, marcando bien el quinto tiempo antes de volver al 4/4.',
  sabias_que='"Bohemian Rhapsody" (1975) de Queen no tenía estribillo ni se ajustaba a ningún formato de radio habitual, y aun así fue un éxito enorme.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('Bb4', 1), ('C5', 2), ('D5', 3), ('Eb5', 4), ('F5', 5), ('Eb5', 4)]] +
                     [{'pitch': 'Bb4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sib', quinta_solfege='Fa',
  keyboard_notes=['Sib', 'Do', 'Re', 'Mib', 'Fa', 'Sol', 'La'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sib',
  posicion_texto='Mano derecha en posición de SIB mayor (un dedo por tecla); izquierda: los acordes Sib, Mib, Fa y Solm.',
  ritmo_texto='Ritmo: el compás cambia entre 4/4 y 5/4 — el 5/4 añade un tiempo extra que no se puede perder.',
  estudiar_steps=['Busca SIB y tócala 3 veces (tu nota casa).',
                   'La frase en 4/4, contando con calma.',
                   'El compás de 5/4, contando "1-2-3-4-5" en voz alta.',
                   'Las dos manos juntas, sin perder el tiempo extra del 5/4.'],
  checklist_items=['Encuentro SIB y pongo bien los dedos.', 'Siento el tiempo extra del compás de 5/4.',
                    'Sé los acordes Sib, Mib, Fa y Solm de memoria.', 'Las dos manos juntas sin perder ningún tiempo.'],
  nivel_kicker='NEL · NIVEL MEDIO-ALTO · JUNIO',
  total_songs=22,
)

cfg22 = dict(
  kicker='NEL · JUNIO · BOHEMIAN RHAPSODY',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SIB, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('Bb4', 'C5'), ('Bb4', 'D5'), ('Bb4', 'Eb5'), ('Bb4', 'F5'), ('Bb4', 'G5'), ('Bb4', 'Bb5')],
  chords_desc='Identifica cada acorde: nómbralo (Sib, Mib, Fa, Solm...) y di si es mayor o menor.',
  chords=[['Bb2', 'D3', 'F3'], ['Eb2', 'G2', 'Bb2'], ['F2', 'A2', 'C3'], ['G2', 'Bb2', 'D3']],
  song_title='Bohemian Rhapsody', song_key='Sib mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Sib mayor (I, IV, V, vi...).',
  progression=['Sib', 'Mib', 'Fa', 'Solm'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: negras que cambian de compás, entre 4/4 y 5/4.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song22)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg22)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Nel_22_Bohemian_Rhapsody.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
