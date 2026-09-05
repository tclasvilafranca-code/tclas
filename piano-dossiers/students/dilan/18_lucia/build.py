import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'DILAN', ' Lucia_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song18 = dict(
  num=18, title='Lucía', subtitle='Joan Manuel Serrat',
  tonalidad='La menor', compas='4/4', tempo='Andante ♩≈78', forma='Estrofa',
  dificultad='Un reto de acompañamiento', manos='Ola arpegiada + melodía',
  la_cancion='Una canción de Serrat, en La menor. La izquierda no toca los acordes de golpe: los reparte en un dibujo de "olas" que se repite.',
  difficult_cc='cc. 1–8', difficult_title='El acompañamiento en olas',
  reto='que la ola de la izquierda fluya sola, sin pensar nota a nota.',
  truco='practica la ola sin la melodía hasta que tu mano la toque sin mirar, como un runrún automático.',
  sabias_que='Joan Manuel Serrat es uno de los cantautores más influyentes en español; "Lucía" (1975) está dedicada a su hija recién nacida.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('D5', 4), ('C5', 3), ('B4', 2)]] +
                     [{'pitch': 'A4', 'dur': 'h', 'number': 1}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Lam',
  posicion_texto='Mano derecha en posición de LA menor (un dedo por tecla); izquierda: la ola arpegiada sobre Lam, Rem y Mi7.',
  ritmo_texto='Ritmo: compás de 4/4, Andante — deja que la ola de la izquierda fluya regular, como un runrún.',
  estudiar_steps=['Busca LA y tócala 3 veces (tu nota casa).',
                   'La ola de la izquierda sola, hasta que salga sin mirar.',
                   'Los acordes Lam-Rem-Mi7 con la izquierda, cada uno con su ola.',
                   'Las dos manos juntas, dejando que la ola fluya sola.'],
  checklist_items=['Encuentro LA y pongo bien los dedos.', 'Mi ola de la izquierda suena regular y fluida.',
                    'Sé los acordes Lam, Rem y Mi7 de memoria.', 'Junto las dos manos sin pararme a pensar.'],
  nivel_kicker='DILAN · NIVEL MEDIO-ALTO · MAYO',
  total_songs=24,
)

cfg18 = dict(
  kicker='DILAN · MAYO · LUCÍA',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi7...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D2', 'F2', 'A2'], ['E2', 'G#2', 'B2'], ['A2', 'C3', 'E3']],
  song_title='Lucía', song_key='La menor',
  progression_desc='Estos acordes sostienen la canción. Escribe el grado de cada uno en La menor (i, iv, V7...).',
  progression=['Lam', 'Rem', 'Mi7', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo: la ola en corcheas, tranquila y regular.',
  rhythm_events=[{'pitch': 'C4', 'dur': 'e', 'beam': i // 4} for i in range(8)] * 1 + [{'pitch': 'A3', 'dur': 'e', 'beam': 2 + i // 4} for i in range(8)],
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

    out_path = os.path.join(OUT_DIR, 'Dilan_18_Lucia.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
