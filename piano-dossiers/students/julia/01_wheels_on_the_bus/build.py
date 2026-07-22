import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JULIA', '  The Wheels on the Bus.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song1 = dict(
  num=1, title='The Wheels on the Bus', subtitle='Canción infantil tradicional · arr. Jim Paterson',
  tonalidad='Fa mayor', compas='4/4', tempo='Alegre', forma='Estrofa',
  dificultad='Nivel inicial', manos='Nota repetida + acordes',
  la_cancion='Una canción infantil muy conocida, en Fa mayor. Hoy jugamos con las ruedas que giran: tocar la misma nota varias veces seguidas, sin miedo.',
  difficult_cc='cc. 1–4', difficult_title='Las ruedas que giran: la misma nota, sin miedo',
  reto='que cada repetición de la rueda suene igual de clara, sin cansarse ni empujar más fuerte.',
  truco='imagina que tu dedo es una ruedecita que rebota sola en la tecla, ¡gira que gira!',
  sabias_que='"The Wheels on the Bus" es una canción infantil estadounidense que se canta con gestos de las manos desde hace más de 80 años.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('F4', 1), ('G4', 2), ('A4', 3), ('G4', 2), ('F4', 1)]] +
                     [{'pitch': 'F4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa', 'Sol', 'La', 'Sib', 'Do', 'Re', 'Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA mayor (un dedo por tecla); izquierda: los acordes Fa, Sib y Do.',
  ritmo_texto='Ritmo: compás de 4/4, alegre — la nota que gira y gira, sin cansarse.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'La rueda que gira: la misma nota, varias veces.',
                   'Los acordes Fa-Sib-Do con la izquierda.',
                   'Las dos manos juntas, ¡todas las ruedas girando!'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'La nota repetida no me cansa la mano.',
                    'Sé los acordes Fa, Sib y Do de memoria.', 'Las dos manos juntas suenan contentas.'],
  nivel_kicker='JULIA · NIVEL INICIAL · SEPTIEMBRE',
  total_songs=24,
)

cfg1 = dict(
  kicker='JULIA · SEPTIEMBRE · THE WHEELS ON THE BUS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde FA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('F4', 'G4'), ('F4', 'A4'), ('F4', 'Bb4'), ('F4', 'C5'), ('F4', 'D5'), ('F4', 'F5')],
  chords_desc='Identifica cada acorde: nómbralo (Fa, Sib, Do...) y di si es mayor o menor.',
  chords=[['F2', 'A2', 'C3'], ['Bb2', 'D3', 'F3'], ['C3', 'E3', 'G3'], ['F2', 'A2', 'C3']],
  song_title='The Wheels on the Bus', song_key='Fa mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Fa mayor (I, IV, V...).',
  progression=['Fa', 'Sib', 'Do', 'Fa'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la nota repetida, en 4/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song1)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg1)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Julia_01_Wheels_On_The_Bus.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
