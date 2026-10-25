import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', 'Trouble_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song16 = dict(
  num=16, title='Trouble', subtitle='Coldplay',
  tonalidad='Sol mayor', compas='4/4', tempo='Tranquilo ♩≈80', forma='Estrofa',
  dificultad='Para disfrutar, sin prisa', manos='Anacrusa + acordes',
  la_cancion='Una canción de Coldplay en Sol mayor. Aquí cuidamos la anacrusa: la frase empieza justo antes del primer tiempo fuerte, con un pequeño impulso tranquilo.',
  difficult_cc='cc. 1–8', difficult_title='La anacrusa que respira: empieza un poco antes, con calma',
  reto='sentir el pequeño impulso de la anacrusa sin adelantarte de golpe ni frenarte de más.',
  truco='piensa la anacrusa como una pequeña toma de aire antes de empezar a cantar la frase.',
  sabias_que='"Trouble" (2000) fue uno de los primeros grandes éxitos de Coldplay, del álbum "Parachutes".',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL mayor (un dedo por tecla); izquierda: los acordes Sol, Re y Do, sin prisa.',
  ritmo_texto='Ritmo: compás de 4/4, tranquilo — la frase empieza con un pequeño impulso justo antes del tiempo fuerte.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa).',
                   'La anacrusa, sin prisa, sintiendo el pequeño impulso.',
                   'Los acordes Sol-Re-Do con la izquierda.',
                   'Las dos manos juntas, dejando que la anacrusa respire.'],
  checklist_items=['Encuentro SOL y pongo bien los dedos.', 'La anacrusa respira, sin adelantarse de golpe.',
                    'Sé los acordes Sol, Re y Do de memoria.', 'Las dos manos juntas sin ninguna prisa.'],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · MARZO',
  total_songs=21,
)

cfg16 = dict(
  kicker='JOSÉ MARÍA · MARZO · TROUBLE',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Mim, Sim, Fa...) y di si es mayor o menor.',
  chords=[['G2', 'B2', 'D3'], ['E2', 'G2', 'B2'], ['B2', 'D3', 'F#3'], ['F2', 'A2', 'C3']],
  song_title='Trouble', song_key='Sol mayor',
  progression_desc='Estos son los acordes reales de la canción. El Fa es "prestado" (no pertenece a Sol mayor) — di si cada acorde suena tónica (T), subdominante (SD) o dominante (D).',
  progression=['Sol', 'Mim', 'Sim', 'Fa'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: la anacrusa antes de cada frase larga, en 4/4.',
  rhythm_events=[{'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'G4', 'dur': 'h'},
                 {'rest': True, 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'h'}],
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

    out_path = os.path.join(OUT_DIR, 'JoseMaria_16_Trouble.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
