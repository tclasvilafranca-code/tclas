import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'NEL', 'YOUR SONG _ Elton John Dm.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song16 = dict(
  num=16, title='Your Song', subtitle='Elton John',
  tonalidad='Fa mayor', compas='4/4 / 2/4 (mixto)', tempo='Lento ♩≈80', forma='Estrofa-estribillo',
  dificultad='Un reto de fraseo', manos='Melodía + acordes, compás cambiante',
  la_cancion='Un clásico de Elton John, en Fa mayor pese a lo que sugiere el nombre del archivo. El reto es de fraseo: de vez en cuando aparece un compás de 2/4, más corto, como una pequeña pausa para respirar.',
  difficult_cc='cc. 1–8', difficult_title='La pausa breve: un compás corto que respira',
  reto='sentir el compás de 2/4 como una respiración natural, sin que rompa el hilo de la frase.',
  truco='respira de verdad, con el cuerpo, justo en ese compás corto — la música hace lo mismo que tú.',
  sabias_que='"Your Song" (1970) fue el primer gran éxito de Elton John, escrito junto a su letrista habitual, Bernie Taupin.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('Bb4', 4), ('C5', 5), ('Bb4', 4)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA mayor (un dedo por tecla); izquierda: los acordes Fa, Lam, Sib y Do.',
  ritmo_texto='Ritmo: el compás cambia entre 4/4 y 2/4 — el compás corto es una pausa para respirar.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'La frase larga en 4/4, sin prisa.',
                   'El compás corto de 2/4, sintiéndolo como una respiración.',
                   'Las dos manos juntas, dejando que la pausa breve respire de verdad.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'Siento el compás corto como una respiración.',
                    'Sé los acordes Fa, Lam, Sib y Do de memoria.', 'Las dos manos juntas sin cortar el hilo.'],
  nivel_kicker='NEL · NIVEL MEDIO-ALTO · MAYO',
  total_songs=22,
)

cfg16 = dict(
  kicker='NEL · MAYO · YOUR SONG',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Lam, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['A2', 'C3', 'E3'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3']],
  song_title='Your Song', song_key='Fa mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Fa mayor (I, iii, IV, V...).',
  progression=['Fa', 'Lam', 'Sib', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: negras que cambian de compás, entre 4/4 y 2/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}] * 8,
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

    out_path = os.path.join(OUT_DIR, 'Nel_16_Your_Song.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
