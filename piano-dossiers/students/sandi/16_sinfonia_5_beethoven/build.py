import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'SANDI', 'Copia de 5#U00aa SINFONIA.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song16 = dict(
  num=16, title='Sinfonía Nº5 (1er movimiento)', subtitle='Ludwig van Beethoven, arr. Gilbert DeBenedetti · Level Three',
  tonalidad='Do menor', compas='2/4', tempo='Allegro con brio', forma='Forma sonata (exposición simplificada)',
  dificultad='Nivel avanzado · reto final', manos='El motivo del destino, en eco entre las manos',
  la_cancion='El célebre primer movimiento de la Sinfonía Nº5 de Beethoven, en Do menor. El famoso motivo del destino (corto-corto-corto-largo) se presenta y se repite como un eco exacto entre las manos.',
  difficult_cc='Toda la pieza', difficult_title='El motivo del destino: la repetición exacta entre las manos',
  reto='reproducir el motivo con la misma fuerza y el mismo ritmo exacto cada vez que rebota entre las manos.',
  truco='practica el motivo aislado con un solo dedo hasta que el ritmo sea perfecto, y solo entonces pásalo de una mano a otra.',
  sabias_que='Beethoven tardó varios años en componer esta sinfonía (estrenada en 1808); el motivo inicial de cuatro notas es posiblemente el más reconocible de toda la música clásica.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('C4', 1), ('D4', 2), ('Eb4', 3), ('F4', 4), ('G4', 5), ('F4', 4)]],
  tonic_solfege='Do', quinta_solfege='Sol',
  keyboard_notes=['Do', 'Re', 'Mib', 'Fa', 'Sol', 'Lab', 'Sib'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Do menor',
  posicion_texto='Mano derecha en posición de DO menor: Do(1) Re(2) Mib(3) Fa(4) Sol(5). El Sib, Mib y Lab son las alteraciones de esta tonalidad.',
  estudiar_steps=[
      'Practica el motivo (corto-corto-corto-largo) con una sola mano hasta que el ritmo sea exacto.',
      'Repite el motivo un escalón más abajo, comprobando que suena idéntico en ritmo e intensidad.',
      'Practica el motivo en ambas manos a la vez, en octavas.',
      'Junta todo el pasaje, cuidando que el eco entre las manos suene como una sola idea.',
  ],
  checklist_items=[
      '¿El motivo suena con el mismo ritmo exacto cada vez?',
      '¿El eco entre las manos mantiene la misma intensidad?',
      '¿Reconozco los acordes Dom, Fam y Solm de esta tonalidad?',
      '¿Puedo tocar el pasaje entero sin que el motivo pierda precisión?',
  ],
  nivel_kicker='SANDI · NIVEL AVANZADO · ABRIL',
  total_songs=16,
)

cfg16 = dict(
  kicker='SANDI · ABRIL · SINFONÍA Nº5',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde DO, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('C4', 'D4'), ('C4', 'Eb4'), ('C4', 'F4'), ('C4', 'G4'), ('C4', 'Ab4'), ('C4', 'C5')],
  chords_desc='Identifica cada acorde: nómbralo (Dom, Fam, Solm...) y di si es mayor o menor.',
  chords=[['C2', 'Eb2', 'G2'], ['F2', 'Ab2', 'C3'], ['G2', 'Bb2', 'D3'], ['C2', 'Eb2', 'G2']],
  song_title='Sinfonía Nº5', song_key='Do menor',
  progression_desc='Estos son los acordes de la pieza. Escribe el grado de cada uno en Do menor (i, iv, v...).',
  progression=['Dom', 'Fam', 'Solm', 'Dom'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el motivo del destino, en 2/4.',
  rhythm_events=[{'rest': True, 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'G4', 'dur': 'e'}, {'pitch': 'Eb4', 'dur': 'h'}],
  rhythm_time_sig=(2, 4),
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

    out_path = os.path.join(OUT_DIR, 'Sandi_16_Sinfonia_5_Beethoven.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
