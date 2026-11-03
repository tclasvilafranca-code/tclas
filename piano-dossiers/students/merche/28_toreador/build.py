import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'TOREADOR-BIZET.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song28 = dict(
  num=28, title='Toreador', subtitle='de Carmen · Level Four · Georges Bizet, arr. Gilbert DeBenedetti',
  tonalidad='Fa mayor', compas='4/4', tempo='March time', forma='Marcha (reto final del álbum)',
  dificultad='Reto final', manos='Melodía marcial + acorde picado y acentuado',
  la_cancion='El célebre "Toreador" de la ópera Carmen, de Bizet, en Fa mayor: el reto final de este cuaderno. El acompañamiento marcha con acordes picados (staccato), cortos y decididos.',
  difficult_cc='Toda la pieza', difficult_title='El acorde picado y acentuado: corto y decidido',
  reto='tocar cada acorde del acompañamiento corto y separado, con firmeza, sin arrastrar el sonido de uno al siguiente.',
  truco='imagina que cada acorde "rebota" de la tecla, como una pelota que no se queda pegada al suelo.',
  sabias_que='"Toreador" (el Coro de los Toreros) pertenece a la ópera Carmen (1875) de Georges Bizet, y es una de las melodías de ópera más reconocibles del mundo.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA: Fa(1) Sol(2) La(3) Sib(4) Do(5). El Sib es la única tecla negra de esta posición.',
  estudiar_steps=[
      'Encuentra el Fa central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de Fa (Fa-La-Do) picado con la izquierda: corto y decidido.',
      'Comprueba que cada acorde suena separado del siguiente, sin arrastrarse.',
      'Junta las manos despacio: la izquierda marca el paso con acordes picados, la derecha canta con fuerza.',
  ],
  checklist_items=[
      '¿Suenan mis acordes picados, cortos y separados?',
      '¿Mantengo la firmeza sin tensar el brazo?',
      '¿Toco el acorde de Fa con seguridad?',
      '¿He completado todo el cuaderno de este curso?',
  ],
  nivel_kicker='MERCÈ · RETO FINAL · JUNIO',
  total_songs=28,
)

cfg28 = dict(
  kicker='MERCÈ · JUNIO · TOREADOR (RETO FINAL)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='Toreador', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el acorde picado, en 4/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song28)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg28)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_28_Toreador.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
