import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', 'SHALLOW_.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song15 = dict(
  num=15, title='Shallow', subtitle='Lady Gaga & Bradley Cooper · A Star Is Born',
  tonalidad='Sol mayor', compas='4/4', tempo='Balada ♩≈85', forma='Estrofa-estribillo',
  dificultad='Para disfrutar, sin prisa', manos='Crecimiento dinámico + acordes',
  la_cancion='Una canción de la película "A Star Is Born", en Sol mayor. Aquí cuidamos que el sonido crezca poco a poco, de suave a fuerte, sin prisa por llegar.',
  difficult_cc='cc. 1–4', difficult_title='El crecimiento lento: de piano a forte, sin prisa',
  reto='dejar que el sonido crezca solo, poco a poco, sin empujarlo de golpe hacia el final.',
  truco='imagina una ola que crece muy despacio desde la orilla: no se apresura, simplemente va a más.',
  sabias_que='"Shallow" (2018), de Lady Gaga y Bradley Cooper, ganó el Óscar a la mejor canción original ese mismo año.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL mayor (un dedo por tecla); izquierda: los acordes Sol, Re, Mim y Do, sin prisa.',
  ritmo_texto='Ritmo: compás de 4/4, balada — el sonido crece poco a poco, sin ningún salto brusco.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa).',
                   'La frase que crece, sin prisa, nota a nota.',
                   'Los acordes Sol-Re-Mim-Do con la izquierda.',
                   'Las dos manos juntas, dejando que el sonido crezca solo.'],
  checklist_items=['Encuentro SOL y pongo bien los dedos.', 'El sonido crece poco a poco, sin saltos.',
                    'Sé los acordes Sol, Re, Mim y Do de memoria.', 'Las dos manos juntas sin ninguna prisa.'],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · MARZO',
  total_songs=21,
)

cfg15 = dict(
  kicker='JOSÉ MARÍA · MARZO · SHALLOW',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Re, Mim, Do...) y di si es mayor o menor.',
  chords=[['G2', 'B2', 'D3'], ['D3', 'F#3', 'A3'], ['E2', 'G2', 'B2'], ['C3', 'E3', 'G3']],
  song_title='Shallow', song_key='Sol mayor',
  progression_desc='Estos son los acordes reales de la canción. Escribe el grado de cada uno en Sol mayor (I, V, vi, IV...).',
  progression=['Sol', 'Re', 'Mim', 'Do'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: notas que crecen sin prisa, en 4/4.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'h'}, {'pitch': 'D5', 'dur': 'h'}, {'pitch': 'C5', 'dur': 'h'}, {'pitch': 'A4', 'dur': 'h'}],
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song15)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg15)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'JoseMaria_15_Shallow.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
