import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'JULIA', 'gladiator.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song24 = dict(
  num=24, title='Honor Him - Gladiator (Easy Version)', subtitle='Hans Zimmer',
  tonalidad='Re mayor', compas='3/4', tempo='♩ = 70', forma='Estrofa con frases sostenidas',
  dificultad='Nivel inicial, con toque extra', manos='Melodía + acorde sostenido, en una tonalidad nueva',
  la_cancion='El emotivo tema de Gladiator, de Hans Zimmer, en esta versión fácil. Es la primera canción de Julia en Re mayor: una tonalidad nueva, con dos sostenidos que hay que recordar siempre.',
  difficult_cc='cc. 1–8', difficult_title='Los dos sostenidos que cuidan la casa',
  reto='recordar el Fa sostenido y el Do sostenido cada vez que aparecen, sin dudar ni volver al blanco.',
  truco='antes de tocar, busca las dos teclas negras (Fa# y Do#) y tócalas un par de veces para que tu mano las recuerde.',
  sabias_que='Hans Zimmer compuso la banda sonora de Gladiator (2000) en tan solo unas semanas, y "Honor Him" se convirtió en uno de sus temas más interpretados en versión de piano.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('D4', 1), ('E4', 2), ('F#4', 3), ('E4', 2), ('D4', 1), ('E4', 2)]] +
                     [{'pitch': 'D4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Re', quinta_solfege='La',
  keyboard_notes=['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si', 'Do#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Re',
  posicion_texto='Mano derecha en posición de RE: Re(1) Mi(2) Fa#(3) Sol(4) La(5). El Fa# es la primera tecla negra de esta tonalidad nueva.',
  estudiar_steps=[
      'Encuentra el Re y coloca ahí el dedo 1 de tu mano derecha.',
      'Busca las dos teclas negras, Fa# y Do#, y tócalas varias veces para memorizarlas.',
      'Practica el acorde de Re (Re-Fa#-La) con la izquierda, con calma.',
      'Junta las manos despacio: la izquierda sostiene su acorde, la derecha canta con sus sostenidos.',
  ],
  checklist_items=[
      '¿Encuentro el Fa# y el Do# sin dudar?',
      '¿Toco el acorde de Re con la izquierda con seguridad?',
      '¿La melodía suena conectada, sin cortes bruscos?',
      '¿Puedo tocar la canción entera sin pararme?',
  ],
  nivel_kicker='JULIA · NIVEL INICIAL · JUNIO',
  total_songs=24,
)

cfg24 = dict(
  kicker='JULIA · JUNIO · GLADIATOR (HONOR HIM)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde RE, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('D4', 'E4'), ('D4', 'F#4'), ('D4', 'G4'), ('D4', 'A4'), ('D4', 'B4'), ('D4', 'D5')],
  chords_desc='Identifica cada acorde: nómbralo (Re, Sol, La...) y di si es mayor o menor.',
  chords=[['D3', 'F#3', 'A3'], ['G2', 'B2', 'D3'], ['A2', 'C#3', 'E3'], ['D3', 'F#3', 'A3']],
  song_title='Gladiator (Honor Him)', song_key='Re mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Re mayor (I, IV, V...).',
  progression=['Re', 'Sol', 'La', 'Re'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la frase sostenida, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h.'}] * 3,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song24)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg24)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Julia_24_Gladiator.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
