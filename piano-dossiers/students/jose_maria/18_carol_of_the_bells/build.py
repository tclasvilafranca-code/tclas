import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', 'carol-of-the-bells   NAVIDAD_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song18 = dict(
  num=18, title='Carol of the Bells', subtitle='Villancico tradicional ucraniano · Mykola Leontovych',
  tonalidad='Sol menor', compas='3/4', tempo='Con energía, sin prisa', forma='Ostinato',
  dificultad='Para disfrutar, sin prisa', manos='Dibujo repetido + acordes',
  la_cancion='Un villancico tradicional ucraniano, muy conocido, en Sol menor. Aquí cuidamos que el pequeño dibujo de cuatro notas se repita sin cansar la mano.',
  difficult_cc='cc. 1–12', difficult_title='El dibujo que se repite, sin cansarse',
  reto='que la mano no se apriete al repetir el mismo dibujo muchas veces seguidas.',
  truco='deja que los dedos "caminen" sin esfuerzo sobre el dibujo, como quien pasea sin prisa por el mismo camino.',
  sabias_que='"Carol of the Bells" (1916) se basa en un canto popular ucraniano de Año Nuevo llamado "Shchedryk", de Mykola Leontovych.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('Bb4', 3), ('A4', 2), ('G4', 1)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib', 'Fa'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol menor',
  posicion_texto='Mano derecha en posición de SOL menor (un dedo por tecla); izquierda: los acordes Solm, Dom y Re, sin prisa.',
  ritmo_texto='Ritmo: compás de 3/4 — el mismo dibujo de cuatro notas se repite, sin cansar la mano.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa).',
                   'El dibujo repetido, muy despacio al principio, con la mano relajada.',
                   'Los acordes Solm-Dom-Re con la izquierda.',
                   'Las dos manos juntas, dejando que el dibujo se repita sin esfuerzo.'],
  checklist_items=['Encuentro SOL y pongo bien los dedos.', 'El dibujo se repite sin cansar la mano.',
                    'Sé los acordes Solm, Dom y Re de memoria.', 'Las dos manos juntas sin ninguna tensión.'],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · MAYO',
  total_songs=21,
)

cfg18 = dict(
  kicker='JOSÉ MARÍA · MAYO · CAROL OF THE BELLS',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('G4', 'A4'), ('G4', 'Bb4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'Eb5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Solm, Dom, Re...) y di si es mayor o menor.',
  chords=[['G2', 'Bb2', 'D3'], ['C3', 'Eb3', 'G3'], ['D3', 'F#3', 'A3'], ['G2', 'Bb2', 'D3']],
  song_title='Carol of the Bells', song_key='Sol menor',
  progression_desc='Estos son los acordes reales de esta pieza. Escribe el grado de cada uno en Sol menor (i, iv, V...).',
  progression=['Solm', 'Dom', 'Re', 'Solm'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: el dibujo repetido de cuatro notas, en 3/4.',
  rhythm_events=[{'pitch': 'A4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'},
                 {'pitch': 'Bb4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'}],
  rhythm_time_sig=(3, 4),
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

    out_path = os.path.join(OUT_DIR, 'JoseMaria_18_Carol_Of_The_Bells.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
