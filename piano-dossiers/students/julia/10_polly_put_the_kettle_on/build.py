import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JULIA', 'Polly Put the Kettle On.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song10 = dict(
  num=10, title='Polly Put the Kettle On', subtitle='Traditional · arr. Jim Paterson',
  tonalidad='Fa mayor', compas='4/4', tempo='Tranquilo', forma='Estrofa',
  dificultad='Nivel inicial', manos='Notas ligadas + acordes',
  la_cancion='Una canción tradicional inglesa en Fa mayor. Hoy practicamos que las notas queden unidas, sin ningún corte entre una y otra.',
  difficult_cc='cc. 1–4', difficult_title='Las notas ligadas: sin cortar entre una y otra',
  reto='que cada nota se una a la siguiente sin ningún hueco, como agua que se sirve sin salpicar.',
  truco='no levantes el dedo hasta tocar la siguiente tecla, para que no se escape ningún hueco de silencio.',
  sabias_que='"Polly Put the Kettle On" es una rima infantil inglesa de finales del siglo XVIII sobre poner la tetera para el té.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1), ('G4', 2)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA mayor (un dedo por tecla); izquierda: los acordes Fa, Sib y Do.',
  ritmo_texto='Ritmo: compás de 4/4, tranquilo — las notas quedan unidas, sin cortes.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'La frase unida, sin levantar el dedo antes de tiempo.',
                   'Los acordes Fa-Sib-Do con la izquierda.',
                   'Las dos manos juntas, con la frase bien unida.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'Mis notas quedan unidas, sin huecos.',
                    'Sé los acordes Fa, Sib y Do de memoria.', 'Las dos manos juntas suenan unidas.'],
  nivel_kicker='JULIA · NIVEL INICIAL · DICIEMBRE',
  total_songs=24,
)

cfg10 = dict(
  kicker='JULIA · DICIEMBRE · POLLY PUT THE KETTLE ON',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='Polly Put the Kettle On', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la frase unida, en 4/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song10)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg10)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Julia_10_Polly_Put_The_Kettle_On.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
