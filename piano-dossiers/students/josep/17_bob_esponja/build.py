import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSEP', 'bob-esponja-cancion-inicial-.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song17 = dict(
  num=17, title='Bob Esponja (canción inicial)', subtitle='Tema de la serie animada',
  tonalidad='Mi mayor', compas='4/4', tempo='Alegre y saltarín', forma='Estrofa',
  dificultad='Un reto de carácter', manos='Staccato + acordes',
  la_cancion='La canción inicial de Bob Esponja, en Mi mayor. El reto es de carácter: cada nota es corta y decidida, como un saltito, con un pequeño silencio detrás.',
  difficult_cc='cc. 1–4', difficult_title='El staccato que salta: corto y decidido',
  reto='que cada nota suene corta y suelta, sin arrastrarla hasta la siguiente.',
  truco='imagina que cada nota es una pelotita que rebota: toca y suelta enseguida, dejando que el silencio haga su parte.',
  sabias_que='La canción inicial de "Bob Esponja" (1999) fue compuesta por el equipo de la serie con un estilo de canción marinera tradicional.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('E4', 1), ('F#4', 2), ('G#4', 3), ('A4', 4), ('B4', 5), ('A4', 4)]] +
                     [{'pitch': 'E4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Mi', quinta_solfege='Si',
  keyboard_notes=['Mi', 'Fa#', 'Sol#', 'La', 'Si', 'Do#', 'Re#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Mi',
  posicion_texto='Mano derecha en posición de MI mayor (un dedo por tecla, dedos 2, 3 y 5 en teclas negras); izquierda: los acordes Mi, La y Si.',
  ritmo_texto='Ritmo: compás de 4/4, alegre — cada nota corta y suelta, con un silencio detrás.',
  estudiar_steps=['Busca MI y tócala 3 veces (tu nota casa).',
                   'El staccato: notas cortas con su silencio detrás.',
                   'Los acordes Mi-La-Si con la izquierda.',
                   'Las dos manos juntas, sin perder el carácter saltarín.'],
  checklist_items=['Encuentro MI y pongo bien los dedos.', 'Cada nota suena corta y decidida.',
                    'Sé los acordes Mi, La y Si de memoria.', 'Las dos manos juntas mantienen el carácter.'],
  nivel_kicker='JOSEP · NIVEL MEDIO-ALTO · MAYO',
  total_songs=22,
)

cfg17 = dict(
  kicker='JOSEP · MAYO · BOB ESPONJA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde MI, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('E4', 'F#4'), ('E4', 'G#4'), ('E4', 'A4'), ('E4', 'B4'), ('E4', 'C#5'), ('E4', 'E5')],
  chords_desc='Identifica cada acorde: nómbralo (Mi, La, Si...) y di si es mayor o menor.',
  chords=[['E2', 'G#2', 'B2'], ['A2', 'C#3', 'E3'], ['B2', 'D#3', 'F#3'], ['E2', 'G#2', 'B2']],
  song_title='Bob Esponja', song_key='Mi mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Mi mayor (I, IV, V...).',
  progression=['Mi', 'La', 'Si', 'Mi'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: negras cortas separadas por silencios, en 4/4.',
  rhythm_events=[{'pitch': 'G#4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
                 {'pitch': 'B4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'rest': True, 'dur': 'q'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song17)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg17)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Josep_17_Bob_Esponja.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
