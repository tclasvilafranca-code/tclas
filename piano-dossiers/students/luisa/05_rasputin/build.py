import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'LUISA', 'rasputin easy.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song5 = dict(
  num=5, title='Rasputin A (Easy Piano)', subtitle='Boney M.',
  tonalidad='Si menor', compas='4/4', tempo='Moderato', forma='Estrofa',
  dificultad='Nivel hobby', manos='Melodía + acordes, sin complicarse',
  la_cancion='El famoso "Rasputin" de Boney M., en Si menor. Si te pierdes tocando, canta la letra en tu cabeza: te ayuda a no perder el hilo, sin agobiarte.',
  difficult_cc='cc. 1–8', difficult_title='La letra que acompaña: canta por dentro',
  reto='seguir la letra en tu cabeza mientras tocas, para no perder el hilo de la melodía.',
  truco='si te despistas, tararea la letra por dentro: te lleva de vuelta a la melodía sin agobios.',
  sabias_que='"Rasputin" (1978) de Boney M. narra, de forma libre, la vida de Grigori Rasputín, el místico ruso de la corte del zar Nicolás II.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('B4', 1), ('C#5', 2), ('D5', 3), ('C#5', 2), ('B4', 1), ('C#5', 2)]] +
                     [{'pitch': 'B4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Si', quinta_solfege='Fa#',
  keyboard_notes=['Si', 'Do#', 'Re', 'Mi', 'Fa#', 'Sol', 'La'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Si menor',
  posicion_texto='Mano derecha en posición de SI menor: Si(1) Do#(2) Re(3) Mi(4) Fa#(5). Tranquila, solo dos teclas negras.',
  estudiar_steps=[
      'Encuentra el Si y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de Si menor (Si-Re-Fa#) con la izquierda, sin prisa.',
      'Canta la letra por dentro mientras tocas la melodía con la derecha.',
      'Junta las manos despacio: nada de agobios, solo disfrutar.',
  ],
  checklist_items=[
      '¿Canto la letra por dentro, sin agobiarme?',
      '¿Toco el acorde de Si menor con calma?',
      '¿Disfruto la canción, sin prisa?',
      '¿Puedo tocar el principio sin pararme?',
  ],
  nivel_kicker='LUISA · NIVEL HOBBY · OCTUBRE',
  total_songs=28,
)

cfg5 = dict(
  kicker='LUISA · OCTUBRE · RASPUTIN',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('B4', 'C#5'), ('B4', 'D5'), ('B4', 'E5'), ('B4', 'F#5'), ('B4', 'G5'), ('B4', 'B5')],
  chords_desc='Identifica cada acorde: nómbralo (Sim, Mim, Fa#...) y di si es mayor o menor.',
  chords=[['B2', 'D3', 'F#3'], ['E2', 'G2', 'B2'], ['F#2', 'A#2', 'C#3'], ['B2', 'D3', 'F#3']],
  song_title='Rasputin', song_key='Si menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Si menor (i, iv, V...).',
  progression=['Sim', 'Mim', 'Fa#', 'Sim'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la melodía tranquila, en 4/4.',
  rhythm_events=[{'pitch': 'D4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song5)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg5)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Luisa_05_Rasputin.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
