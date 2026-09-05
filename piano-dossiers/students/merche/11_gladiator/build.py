import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'Gladyator.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song11 = dict(
  num=11, title='Honor Him - Gladiator (Easy Version)', subtitle='Hans Zimmer',
  tonalidad='Re mayor', compas='3/4', tempo='♩ = 70', forma='Estrofa con dinámica expresiva',
  dificultad='Nivel básico', manos='Melodía con matices dinámicos + acorde sostenido',
  la_cancion='El emotivo tema de Gladiator, de Hans Zimmer, en Re mayor. La pieza crece de piano a mezzoforte y luego se calma de nuevo: hoy trabajamos ese cambio gradual de volumen.',
  difficult_cc='cc. 1–8', difficult_title='El crescendo y el diminuendo: la música que crece y se calma',
  reto='hacer que el volumen cambie de forma gradual y controlada, sin saltos bruscos.',
  truco='practica la misma frase varias veces, aumentando el volumen nota a nota, hasta sentir un crecimiento natural.',
  sabias_que='Hans Zimmer compuso la banda sonora de Gladiator (2000) en tan solo unas semanas, y "Honor Him" se convirtió en uno de sus temas más interpretados en versión de piano.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('E4', 2), ('D4', 1), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El Fa# es la primera tecla negra de esta tonalidad.',
  estudiar_steps=[
      'Encuentra el Re y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de Re (Re-Fa#-La) con la izquierda, con calma.',
      'Toca la melodía dejando que el volumen crezca poco a poco, sin saltos.',
      'Junta las manos despacio: la izquierda sostiene su acorde, la derecha crece y se calma con naturalidad.',
  ],
  checklist_items=[
      '¿Encuentro el Fa# y el Do# sin dudar?',
      '¿El volumen crece de forma gradual, no de golpe?',
      '¿Toco el acorde de Re con la izquierda con seguridad?',
      '¿Puedo tocar la canción entera sin pararme?',
  ],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · DICIEMBRE',
  total_songs=28,
)

cfg11 = dict(
  kicker='MERCÈ · DICIEMBRE · GLADIATOR (HONOR HIM)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['A2', 'C#3', 'E3'], ['D3', 'F#3', 'A3']],
  song_title='Gladiator (Honor Him)', song_key='Re mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la frase que crece, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'q'}] * 6,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song11)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg11)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_11_Gladiator.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
