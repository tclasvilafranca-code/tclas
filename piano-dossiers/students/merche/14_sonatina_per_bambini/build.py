import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', 'Maurizio Bazzoni sonatina para 4 manos.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song14 = dict(
  num=14, title='Sonatina per bambini', subtitle='Maurizio Bazzoni · a 4 manos',
  tonalidad='La menor', compas='4/4', tempo='Moderato', forma='Estrofa (a 4 manos, con 8va)',
  dificultad='Nivel básico', manos='Melodía bajo signo 8va + acorde sostenido, a 4 manos',
  la_cancion='Una sonatina para niños de Bazzoni, en La menor, a cuatro manos. La parte del alumno lleva encima una línea de puntos "8va": hay que tocar todo una octava más alta de lo escrito.',
  difficult_cc='cc. 1–4', difficult_title='El signo 8va: una octava más alta de lo escrito',
  reto='recordar durante toda la línea de puntos "8va" que hay que tocar una octava más arriba, sin cambiar la digitación.',
  truco='antes de empezar, busca con la mano la octava de arriba y quédate ahí mientras dure la línea de puntos.',
  sabias_que='El signo "8va" (ottava) se usa desde el siglo XVIII para evitar líneas adicionales excesivas en la partitura: una solución elegante para música muy aguda o muy grave.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2), ('A4', 1), ('B4', 2)]] +
                     [{'pitch': 'A4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La menor',
  posicion_texto='Mano derecha en posición de LA menor: La(1) Si(2) Do(3) Re(4) Mi(5). Todas teclas blancas, como el relativo menor de Do mayor.',
  estudiar_steps=[
      'Encuentra el La central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de La menor (La-Do-Mi) con la izquierda, con calma.',
      'Sube una octava con la melodía: busca el La de arriba y quédate ahí mientras dure el signo 8va.',
      'Junta las manos despacio: la izquierda sostiene su acorde, la derecha canta arriba.',
  ],
  checklist_items=[
      '¿Recuerdo tocar una octava más alta bajo el signo 8va?',
      '¿Toco el acorde de La menor con seguridad?',
      '¿Reconozco el sensible Sol# cuando aparece?',
      '¿Puedo tocar la sonatina entera sin pararme?',
  ],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · ENERO',
  total_songs=28,
)

cfg14 = dict(
  kicker='MERCÈ · ENERO · SONATINA PER BAMBINI',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A3', 'B3'), ('A3', 'C4'), ('A3', 'D4'), ('A3', 'E4'), ('A3', 'F4'), ('A3', 'A4')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D2', 'F2', 'A2'], ['E2', 'G#2', 'B2'], ['A2', 'C3', 'E3']],
  song_title='Sonatina per bambini', song_key='La menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en La menor (i, iv, V...).',
  progression=['Lam', 'Rem', 'Mi', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la melodía bajo el signo 8va, en 4/4.',
  rhythm_events=[{'pitch': 'C5', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song14)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg14)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_14_Sonatina_Per_Bambini.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
