import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'LUISA', 'bazzoni-maurizio-sonatina-per-bambini-(4 manos).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song18 = dict(
  num=18, title='Sonatina per bambini', subtitle='Maurizio Bazzoni · a 4 manos',
  tonalidad='La menor', compas='4/4', tempo='Moderato', forma='Estrofa (a 4 manos)',
  dificultad='Nivel hobby', manos='Melodía + acorde sostenido, a 4 manos, sin complicarse',
  la_cancion='Una sonatina para niños de Bazzoni, en La menor, a cuatro manos. La melodía repite la misma idea sencilla una y otra vez: hoy solo hay que disfrutarla, sin agobios.',
  difficult_cc='cc. 1–4', difficult_title='El acorde que se repite: sencillo y alegre',
  reto='disfrutar de lo sencilla que es esta idea que se repite, sin ponerte nerviosa.',
  truco='una vez la aprendas, verás que se repite: no hace falta memorizar nada nuevo cada vez.',
  sabias_que='Bazzoni escribió esta sonatina especialmente para que un niño y su maestro la toquen juntos, a cuatro manos.',
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
      'Toca la idea que se repite con la derecha, sin prisa.',
      'Junta las manos despacio, disfrutando de lo sencilla que resulta.',
  ],
  checklist_items=[
      '¿Reconozco la idea que se repite?',
      '¿Toco el acorde de La menor con seguridad?',
      '¿Reconozco el sensible Sol# cuando aparece?',
      '¿Puedo tocar la sonatina entera sin agobiarme?',
  ],
  nivel_kicker='LUISA · NIVEL HOBBY · FEBRERO',
  total_songs=28,
)

cfg18 = dict(
  kicker='LUISA · FEBRERO · SONATINA PER BAMBINI',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A3', 'B3'), ('A3', 'C4'), ('A3', 'D4'), ('A3', 'E4'), ('A3', 'F4'), ('A3', 'A4')],
  chords_desc='Identifica cada acorde: nómbralo (Lam, Rem, Mi...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['D2', 'F2', 'A2'], ['E2', 'G#2', 'B2'], ['A2', 'C3', 'E3']],
  song_title='Sonatina per bambini', song_key='La menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en La menor (i, iv, V...).',
  progression=['Lam', 'Rem', 'Mi', 'Lam'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la melodía repetida, en 4/4.',
  rhythm_events=[{'pitch': 'C5', 'dur': 'q'}] * 8,
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

    out_path = os.path.join(OUT_DIR, 'Luisa_18_Sonatina_Per_Bambini.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
