import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'engine'))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_theory_generic import build_theory_page, W, H
from page_exercises import page1, page2
from page_harmony_generic import build_harmony_page

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', '..', '..', 'assets')
SOURCE_PDF = os.path.join(HERE, '..', 'source', 'VALENTINA', 'Copia de  la-promesa-MELENDI.pdf')
OUT_DIR = os.path.join(HERE, '..', '..', '..', 'output')

song16 = dict(
  num=16, title='La Promesa', subtitle='Melendi',
  tonalidad='Sol mayor', compas='4/4', tempo='Lento ♩≈76', forma='Estrofa-estribillo',
  dificultad='Nivel medio', manos='Salto de octava en el bajo + melodía',
  la_cancion='Una canción de Melendi, en Sol mayor. Hoy: el salto de octava en el bajo, firme y limpio, sin tantear.',
  difficult_cc='cc. 1–8', difficult_title='El salto de octava en el bajo: firme y limpio',
  reto='caer exactamente en la octava sin mirar demasiado el teclado, confiando en la memoria de la mano.',
  truco='practica el salto muy despacio, memorizando la distancia física entre las dos teclas antes de acelerar.',
  sabias_que='"La Promesa" (2013) de Melendi es una de sus canciones más populares y habla de una promesa de amor incumplida.',
  mini_staff_events=[{'pitch': p, 'dur': 'q', 'number': n} for p, n in
                      [('G4', 1), ('A4', 2), ('B4', 3), ('C5', 4), ('B4', 3), ('A4', 2)]] +
                     [{'pitch': 'G4', 'dur': 'h', 'number': 1}],
  tonic_solfege='Sol', quinta_solfege='Re',
  keyboard_notes=['Sol', 'La', 'Si', 'Do', 'Re', 'Mi', 'Fa#'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Sol',
  posicion_texto='Mano derecha en posición de SOL: Sol(1) La(2) Si(3) Do(4) Re(5). Todo teclas blancas, sin alteraciones.',
  estudiar_steps=['Toca la posición de 5 dedos en Sol mayor.',
                   'Practica el salto de octava en el bajo, muy despacio.',
                   'Añade la melodía por encima, sin perder el salto.',
                   'Junta ambas manos, dejando que el salto sea firme y limpio.'],
  checklist_items=['Reconozco la posición de Sol de un vistazo', 'El salto de octava cae limpio, sin tantear',
                    'Mantengo el pulso mientras salto', 'La melodía suena tranquila por encima'],
  nivel_kicker='VALENTINA · NIVEL MEDIO · MAYO',
  total_songs=22,
)

cfg16 = dict(
  kicker='VALENTINA · MAYO · LA PROMESA (MELENDI)',
  intervals_desc='Toca (o imagina) cada pareja de notas, siempre desde SOL, y escribe el intervalo: 2ª, 3ª, 4ª, 5ª, 6ª u 8ª.',
  intervals=[('G4', 'A4'), ('G4', 'B4'), ('G4', 'C5'), ('G4', 'D5'), ('G4', 'E5'), ('G4', 'G5')],
  chords_desc='Identifica cada acorde: nómbralo (Sol, Re, Do...) y di si es mayor o menor.',
  chords=[['G3', 'B3', 'D4'], ['D3', 'F#3', 'A3'], ['C3', 'E3', 'G3'], ['G3', 'B3', 'D4']],
  song_title='La Promesa', song_key='Sol mayor',
  progression_desc='Estos son los acordes de la canción. Escribe el grado de cada uno en Sol mayor (I, IV, V...).',
  progression=['Sol', 'Re', 'Do', 'Sol'],
  progression_mode='roman',
  rhythm_desc='Lee y marca el ritmo real: el salto de octava en negras, en 4/4.',
  rhythm_events=[{'pitch': p, 'dur': 'q'} for p in ['G2', 'G3', 'G2', 'G3']],
  rhythm_time_sig=(4, 4),
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

    out_path = os.path.join(OUT_DIR, "Valentina_16_La_Promesa.pdf")
    with open(out_path, 'wb') as f:
        writer.write(f)

    for p in (theory_path, ex_path, harmony_path):
        os.remove(p)
    print('generated', out_path)


if __name__ == '__main__':
    main()
