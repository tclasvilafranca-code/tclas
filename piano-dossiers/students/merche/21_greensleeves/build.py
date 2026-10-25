import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'MERCHE', '-Greensleeves.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song21 = dict(
  num=21, title='Greensleeves', subtitle='Canción tradicional inglesa',
  tonalidad='La menor', compas='3/4', tempo='Moderato', forma='Estrofa (con pedale)',
  dificultad='Nivel básico', manos='Melodía legato + acordes con pedal',
  la_cancion='La célebre melodía tradicional inglesa "Greensleeves", en La menor. La partitura pide "con pedale": hoy aprendemos a usar el pedal derecho para unir los acordes sin cortar el sonido.',
  difficult_cc='Toda la pieza', difficult_title='El pedal de resonancia: unir los acordes',
  reto='cambiar el pedal justo en el momento en que cambia el acorde, sin mezclar dos acordes ni cortar el sonido.',
  truco='practica el gesto "pisa-suelta-pisa" exactamente en el cambio de acorde, escuchando que no se mezclen.',
  sabias_que='"Greensleeves" es una melodía inglesa del siglo XVI cuya autoría se ha atribuido tradicionalmente (sin pruebas históricas) al rey Enrique VIII.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('A4', 1), ('B4', 2), ('C5', 3), ('B4', 2), ('A4', 1), ('B4', 2)]] +
                     [{'pitch': 'A4', 'dur': 'h.', 'number': 1}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La menor',
  posicion_texto='Mano derecha en posición de LA menor: La(1) Si(2) Do(3) Re(4) Mi(5). Todas teclas blancas, como el relativo menor de Do mayor.',
  estudiar_steps=[
      'Encuentra el La central y coloca ahí el dedo 1 de tu mano derecha.',
      'Practica el pedal solo, sin tocar: pisa, suelta, pisa, con un pulso regular.',
      'Toca el acorde de La menor con la izquierda y usa el pedal para sostenerlo.',
      'Junta las manos despacio: cambia el pedal justo cuando cambia el acorde.',
  ],
  checklist_items=[
      '¿Cambio el pedal justo en el cambio de acorde?',
      '¿El sonido queda unido, sin cortes ni mezclas?',
      '¿Reconozco el sensible Sol# en el acorde de Mi?',
      '¿Puedo tocar la canción entera sin pararme?',
  ],
  nivel_kicker='MERCÈ · NIVEL BÁSICO · MAYO',
  total_songs=28,
)

cfg21 = dict(
  kicker='MERCÈ · MAYO · GREENSLEEVES',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde LA, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('A4', 'B4'), ('A4', 'C5'), ('A4', 'D5'), ('A4', 'E5'), ('A4', 'F5'), ('A4', 'A5')],
  chords_desc='Identifica cada acorde: nómbralo (Am, G, F, E...) y di si es mayor o menor.',
  chords=[['A2', 'C3', 'E3'], ['G2', 'B2', 'D3'], ['F2', 'A2', 'C3'], ['E2', 'G#2', 'B2']],
  song_title='Greensleeves', song_key='La menor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en La menor (i, VII, VI, V...).',
  progression=['Am', 'G', 'F', 'E'],
  progression_mode='function',
  rhythm_desc='Lee y marca el ritmo real: el acorde sostenido con pedal, en 3/4.',
  rhythm_events=[{'pitch': 'E4', 'dur': 'h.'}] * 2,
  rhythm_time_sig=(3, 4),
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theory_path = os.path.join(HERE, '_theory.pdf')
    ex_path = os.path.join(HERE, '_exercises.pdf')
    harmony_path = os.path.join(HERE, '_harmony.pdf')

    c = canvas.Canvas(theory_path, pagesize=(W, H))
    build_theory_page(c, os.path.join(ASSETS, 'asset_qr_real.png'), song21)
    c.save()

    c = canvas.Canvas(ex_path, pagesize=(W, H))
    page1(c)
    page2(c)
    c.save()

    c = canvas.Canvas(harmony_path, pagesize=(W, H))
    build_harmony_page(c, cfg21)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(SOURCE_PDF).pages:
        writer.add_page(p)
    for path in (theory_path, ex_path, harmony_path):
        for p in PdfReader(path).pages:
            writer.add_page(p)

    out_path = os.path.join(OUT_DIR, 'Merce_21_Greensleeves.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
