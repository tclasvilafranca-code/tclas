import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'NEL', 'Rasputyn.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song5 = dict(
  num=5, title='Rasputin', subtitle='Boney M.',
  tonalidad='Si menor', compas='4/4', tempo='♩≈128', forma='Estrofa-estribillo',
  dificultad='Un reto de carácter', manos='Acordes marcados + melodía',
  la_cancion='Una canción de Boney M. en Si menor, rápida y bailable. El reto es de carácter: cada acorde tiene que caer con energía, como un paso de baile, sin ablandarse nunca.',
  difficult_cc='cc. 1–8', difficult_title='Acentos marcados y decididos',
  reto='que cada acorde suene con un golpe claro y decidido, sin que ninguno se quede flojo o difuminado.',
  truco='imagina que cada acorde es un paso de baile: el peso del cuerpo cae de golpe, no se desliza.',
  sabias_que='"Rasputin" (1978) de Boney M. cuenta, con bastantes licencias históricas, la vida del místico ruso Grigori Rasputín.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('B4', 1), ('C#5', 2), ('D5', 3), ('E5', 4), ('F#5', 5), ('E5', 4)]] +
                     [{'pitch': 'B4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Si', quinta_solfege='Fa#',
  keyboard_notes=['Si', 'Do#', 'Re', 'Mi', 'Fa#', 'Sol', 'La'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Si menor',
  posicion_texto='Mano derecha en posición de SI menor (un dedo por tecla, el 2 en Do#); izquierda: los acordes Sim, Mim y Fa# (con el La# de la sensible).',
  ritmo_texto='Ritmo: compás de 4/4, rápido — cada acorde con un acento decidido, como un baile.',
  estudiar_steps=['Busca SI y tócala 3 veces (tu nota casa).',
                   'Los acordes Sim-Mim-Fa# con la izquierda, cada uno con energía.',
                   'La melodía sola, con el mismo carácter marcado.',
                   'Las dos manos juntas, acentuando siempre a la vez.'],
  checklist_items=['Encuentro SI y pongo bien los dedos.', 'Cada acorde suena con un golpe claro.',
                    'Sé los acordes Sim, Mim y Fa# de memoria.', 'El carácter enérgico no decae al juntar las manos.'],
  nivel_kicker='NEL · NIVEL MEDIO-ALTO · NOVIEMBRE',
  total_songs=22,
)

cfg5 = dict(
  kicker='NEL · NOVIEMBRE · RASPUTIN',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('B4', 'C#5'), ('B4', 'D5'), ('B4', 'E5'), ('B4', 'F#5'), ('B4', 'G5'), ('B4', 'B5')],
  chords_desc='Identifica cada acorde: nómbralo (Sim, Mim, Fa#...) y di si es mayor o menor.',
  chords=[['B2', 'D3', 'F#3'], ['E2', 'G2', 'B2'], ['F#2', 'A#2', 'C#3'], ['B2', 'D3', 'F#3']],
  song_title='Rasputin', song_key='Si menor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Si menor (i, iv, V...).',
  progression=['Sim', 'Mim', 'Fa#', 'Sim'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: negras marcadas, acentuando cada tiempo, en 4/4.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}] * 8,
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

    out_path = os.path.join(OUT_DIR, 'Nel_05_Rasputin.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
