import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'LUISA', '_bazzoni-maurizio-sonatina-sol-maggiore (4 manos).pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song17 = dict(
  num=17, title='Sonatina N.2', subtitle='Maurizio Bazzoni · a 4 manos, in sol maggiore',
  tonalidad='Sol mayor', compas='4/4', tempo='Moderato', forma='Estrofa (a 4 manos)',
  dificultad='Nivel hobby', manos='Melodía + acompañamiento, a 4 manos, sin complicarse',
  la_cancion='La Sonatina N.2 de Bazzoni, en Sol mayor, a cuatro manos. Las dos partes tocan casi la misma melodía a la vez, como haciéndose compañía: hoy solo hay que tocar tranquilas, juntas, sin agobios.',
  difficult_cc='Toda la pieza', difficult_title='Tocar en pareja, sin prisa: las dos partes se acompañan',
  reto='tocar tranquila junto a tu pareja, sin ponerte nerviosa por ir a la vez.',
  truco='escuchad la una a la otra mientras tocáis: no hay prisa, solo acompañaros.',
  sabias_que='Esta sonatina está escrita para dos pianistas a la vez, cada una con su propia parte, pensada para tocar en compañía.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('A4', 2), ('G4', 1), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL: Sol(1) La(2) Si(3) Do(4) Re(5). El Fa# es la única alteración de esta tonalidad.',
  estudiar_steps=[
      'Encuentra el Sol central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el acorde de Sol (Sol-Si-Re) con la izquierda, tranquila.',
      'Toca la melodía con la derecha, sin prisa.',
      'Junta las manos despacio, disfrutando de tocar en pareja.',
  ],
  checklist_items=[
      '¿Toco tranquila, sin agobiarme?',
      '¿Toco el acorde de Sol con seguridad?',
      '¿Reconozco el Fa# sin dudar?',
      '¿Puedo tocar la sonatina entera sin pararme?',
  ],
  nivel_kicker='LUISA · NIVEL HOBBY · FEBRERO',
  total_songs=28,
)

cfg17 = dict(
  kicker='LUISA · FEBRERO · SONATINA N.2',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Do, Re...) y di si es mayor o menor.',
  chords=[['G2', 'B2', 'D3'], ['C3', 'E3', 'G3'], ['D2', 'F#2', 'A2'], ['G2', 'B2', 'D3']],
  song_title='Sonatina N.2', song_key='Sol mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Sol mayor (I, IV, V...).',
  progression=['Sol', 'Do', 'Re', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: la melodía tranquila, en 4/4.',
  rhythm_events=[{'pitch': 'B4', 'dur': 'q'}] * 8,
  rhythm_time_sig=(4, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song17)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg17)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Luisa_17_Sonatina_Sol_Maggiore.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
