import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JOSE_MARIA', " Grandfather_s Clock.pdf")
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song1 = dict(
  num=1, title="My Grandfather's Clock", subtitle='Henry Clay Work · arr. Gilbert DeBenedetti',
  tonalidad='Sol mayor', compas='4/4', tempo='Con calma ♩≈90', forma='Estrofa narrativa',
  dificultad='Para disfrutar, sin prisa', manos='Melodía + pulso tranquilo',
  la_cancion='Una canción tranquila en Sol mayor que cuenta la historia de un viejo reloj de pared. Aquí no hay ninguna prisa: el objetivo es cuidar un pulso constante, como el tictac de un reloj que nunca se acelera.',
  difficult_cc='cc. 1–8', difficult_title='El pulso que nunca se acelera',
  reto='mantener el pulso de la izquierda igual de tranquilo de principio a fin, sin apresurarse.',
  truco='cuenta en voz baja "uno, dos, tres, cuatro" muy despacio antes de empezar, y no sueltes ese conteo mientras tocas.',
  sabias_que='Henry Clay Work escribió esta canción en 1876; con el tiempo, la expresión inglesa "grandfather clock" (reloj de pie) nació precisamente de esta canción.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('D5', 5), ('C5', 4)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol, con calma',
  posicion_texto='Mano derecha en posición de SOL mayor (un dedo por tecla); izquierda: los acordes Sol, Do y Re, sin prisa.',
  ritmo_texto='Ritmo: compás de 4/4, tranquilo — siente el pulso de la izquierda como un tictac que no se acelera.',
  estudiar_steps=['Busca SOL y tócala 3 veces (tu nota casa), sin prisa.',
                   'Mano izquierda sola: el pulso, siempre igual de tranquilo.',
                   'Mano derecha sola: la melodía, a tu aire.',
                   'Las dos manos juntas, cuando te sientas cómodo — no hay ninguna prisa.'],
  checklist_items=['Encuentro SOL y me tomo mi tiempo con los dedos.', 'El pulso de la izquierda no se acelera nunca.',
                    'Disfruto la melodía sin perseguir la velocidad.', 'Las dos manos juntas suenan tranquilas.'],
  nivel_kicker='JOSÉ MARÍA · A SU RITMO · SEPTIEMBRE',
  total_songs=21,
)

cfg1 = dict(
  kicker='JOSÉ MARÍA · SEPTIEMBRE · MY GRANDFATHER\'S CLOCK',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª. Sin prisa.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Do, Re...) y di si es mayor o menor.',
  chords=[['G3', 'B3', 'D4'], ['C3', 'E3', 'G3'], ['D3', 'F#3', 'A3'], ['G3', 'B3', 'D4']],
  song_title="My Grandfather's Clock", song_key='Sol mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Sol mayor (I, IV, V...).',
  progression=['Sol', 'Do', 'Re', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real de la melodía: negras tranquilas, en 4/4.',
  rhythm_events=[{'pitch': 'D5', 'dur': 'q'}] * 8,
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

    out_path = os.path.join(OUT_DIR, 'JoseMaria_01_Grandfathers_Clock.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
