import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'Para Elisa.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song25 = dict(
  num=25, title='Für Elise', subtitle='Ludwig van Beethoven',
  tonalidad='La menor', compas='3/4', tempo='Poco moto', forma='Estrofa (versión simplificada)',
  dificultad='Nivel básico', manos='Alternancia rápida + acordes',
  la_cancion='El célebre "Für Elise" de Beethoven, en La menor, en esta versión simplificada. El famoso comienzo alterna dos notas vecinas (Mi y Re#) una y otra vez: hoy trabajamos esa alternancia relajada.',
  difficult_cc='cc. 1–2', difficult_title='La alternancia rápida: dos notas que se turnan',
  reto='mantener la alternancia entre las dos notas relajada, sin tensar la muñeca ni acelerarse de más.',
  truco='practica el "turno" de las dos notas muy despacio primero, acelerando solo cuando la mano esté relajada.',
  sabias_que='Beethoven compuso "Für Elise" hacia 1810, pero la pieza no se publicó hasta 1867, cuarenta años después de su muerte.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2), ('A4', 1), ('B4', 2)]] +
                     [{'pitch': 'A4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La menor',
  posicion_texto='Mano derecha en posición de LA menor: La(1) Si(2) Do(3) Re(4) Mi(5). Todas teclas blancas, como el relativo menor de Do mayor.',
  estudiar_steps=[
      'Encuentra el La central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica la alternancia Mi-Re#-Mi-Re# muy despacio, con la muñeca relajada.',
      'Practica el acorde de La menor (La-Do-Mi) con la izquierda, con calma.',
      'Junta las manos despacio: la izquierda sostiene su acorde, la derecha alterna sin tensarse.',
  ],
  checklist_items=[
      '¿La alternancia suena relajada, sin tensión en la muñeca?',
      '¿Reconozco el Re# como sensible de Mi menor?',
      '¿Toco el acorde de La menor con seguridad?',
      '¿Puedo tocar el principio entero sin pararme?',
  ],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · JUNIO',
  total_songs=28,
)

cfg25 = dict(
  kicker='MERCÈ · JUNIO · FÜR ELISE (BEETHOVEN)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D2', 'F2', 'A2'], ['E2', 'G#2', 'B2'], ['A2', 'C3', 'E3']],
  song_title='Für Elise', song_key='La menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en La menor (i, iv, V...).',
  progression=['Lam', 'Rem', 'Mi', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la alternancia rápida, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'e'}] * 12,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song25)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg25)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_25_Para_Elisa.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
